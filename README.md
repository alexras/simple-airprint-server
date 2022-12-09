# Simple AirPrint Server

I have an older laser printer that doesn't natively support Apple's AirPrint technology. This means that my iOS devices can't see my printer, even if that printer is shared from my Mac Mini.

It turns out that the reason the shared printer on my Mac Mini isn't visible to AirPrint is due to some missing metadata in its DNS-SD (a.k.a. Bonjour) broadcast related to Apple's URF driverless printing standard. The script contained in this repo is a simple way to expose a second service that contains the relevant metadata.

This should work on any recent macOS version (I've tested it on macOS Monterey 12.16.1) without any additional dependencies.

## Usage

This script creates a modified copy of an existing DNS-SD IPP service. You can find the service corresponding to your printer using a tool like [Tildesoft's Discovery](https://itunes.apple.com/us/app/discovery-dns-sd-browser/id1381004916?mt=12).

Once you know your service's name, run:

```bash
./airprint-server.py "<name of service here>"
```

This script is based on [a GeekBitZone tutorial](https://www.geekbitzone.com/posts/macos/airprint/macos-airprint/) and the [CUPS AirPrint documentation](https://wiki.debian.org/CUPSAirPrint).
