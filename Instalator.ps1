$packages = @("pyyaml","pyinstaller","json2xml","xmltodict","customtkinter")
foreach ($package in $packages) {
    Write-Host "pobieram bibliotekę $package"
    pip install $package
}

Write-Host "Pomyślnie pobrano potrzebne biblioteki: "
foreach ($package in $packages) {
    Write-Host "$package"
}
