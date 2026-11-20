$ErrorActionPreference = 'Stop'
$d = "$env:TEMP\claude\osm"
$need = (Get-Content -Raw -Encoding utf8 "$d\need.json" | ConvertFrom-Json).need
function Enc([double]$x){ [int64]$v=[math]::Round($x*1e5); $v = if($v -lt 0){ -bnot ($v -shl 1) } else { $v -shl 1 }; $s=''; while($v -ge 0x20){ $s+=[char][int]((0x20 -bor ($v -band 0x1f))+63); $v = $v -shr 5 }; $s+[char][int]($v+63) }
function Poly($pts){ $s='';$pla=0;$plo=0; foreach($p in $pts){ $la=[math]::Round($p[1]*1e5); $lo=[math]::Round($p[0]*1e5); $s+=Enc(($la-$pla)/1e5); $s+=Enc(($lo-$plo)/1e5); $pla=$la;$plo=$lo }; $s }
$out = New-Object System.Collections.ArrayList
foreach($prof in @(@('c','routed-car'),@('f','routed-foot'))){
  $legs = @($need | ? { $_[2] -eq $prof[0] })
  for($i=0; $i -lt $legs.Count; $i+=20){
    $chunk = $legs[$i..([Math]::Min($i+19,$legs.Count-1))]
    $wp = ($chunk | % { "{0},{1};{2},{3}" -f $_[3][1],$_[3][0],$_[4][1],$_[4][0] }) -join ';'
    $u = "https://routing.openstreetmap.de/$($prof[1])/route/v1/driving/${wp}?overview=false&steps=true&geometries=geojson"
    $r = $null
    for($k=0;$k -lt 4;$k++){ try { $r = Invoke-RestMethod -Uri $u -Headers @{ 'User-Agent'='route-planner-dev/1.0' } -TimeoutSec 120; break } catch { Start-Sleep -Seconds (5*($k+1)) } }
    if(-not $r -or $r.code -ne 'Ok'){ "FAIL chunk $i $($prof[0])"; continue }
    for($j=0;$j -lt $chunk.Count;$j++){
      $leg = $r.routes[0].legs[2*$j]; $n = $chunk[$j]
      $pts = New-Object System.Collections.ArrayList
      foreach($st in $leg.steps){ foreach($c in $st.geometry.coordinates){ if($pts.Count -eq 0 -or ($pts[$pts.Count-1][0] -ne $c[0] -or $pts[$pts.Count-1][1] -ne $c[1])){ [void]$pts.Add($c) } } }
      $steps = foreach($st in $leg.steps){ ,@($st.maneuver.type, ([string]$st.maneuver.modifier), ([string]$st.name), [math]::Round($st.distance), [math]::Round($st.maneuver.location[1],5), [math]::Round($st.maneuver.location[0],5)) }
      [void]$out.Add([ordered]@{ k = "$($n[0])`t$($n[1])|$($n[2])"; g = (Poly $pts); d = [math]::Round($leg.distance); t = [math]::Round($leg.duration); s = @($steps) })
    }
    "done $($prof[0]) $($i+$chunk.Count)/$($legs.Count)"
    Start-Sleep -Milliseconds 1200
  }
}
$json = ConvertTo-Json -InputObject @($out) -Depth 6 -Compress
[IO.File]::WriteAllText("$d\road_new.json", $json, [Text.UTF8Encoding]::new($false))
"WROTE $($out.Count) legs"
