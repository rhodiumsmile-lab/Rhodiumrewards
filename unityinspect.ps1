$aar = 'C:\Users\a\.gradle\caches\modules-2\files-2.1\com.unity3d.ads\unity-ads\4.20.0\8b709e1ef8ae67bfaeb5ad20f04d70c4219c36c5\unity-ads-4.20.0.aar'
$tmp = Join-Path $env:TEMP 'unityads_inspect'
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory -Path $tmp | Out-Null
Expand-Archive -Path $aar -DestinationPath $tmp -Force
$classes = (Get-ChildItem -Path $tmp -Recurse -File -Filter 'classes.jar' | Select-Object -First 1).FullName
Write-Output "CLASSES=$classes"
& 'C:\java\jdk-17.0.12+7\bin\javap.exe' -classpath $classes -p com.unity3d.ads.LoadListener
Write-Output '---'
& 'C:\java\jdk-17.0.12+7\bin\javap.exe' -classpath $classes -p com.unity3d.ads.InterstitialAd
Write-Output '---'
& 'C:\java\jdk-17.0.12+7\bin\javap.exe' -classpath $classes -p com.unity3d.ads.RewardedAd
Write-Output '---'
& 'C:\java\jdk-17.0.12+7\bin\javap.exe' -classpath $classes -p com.unity3d.ads.BannerAd
