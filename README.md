# SDDM Breeze Bing Wallpaper

Automatically updates the SDDM (Simple Desktop Display Manager) login screen wallpaper with Bing's daily wallpaper.

## Features

- Fetches Bing's daily wallpaper automatically
- Supports multiple resolutions (UHD/4K, 2K, 1080p)
- Can be installed as a systemd service with timer
- Lightweight Python implementation

## Dependencies

- Python 3.x
- python-requests
- SDDM with Breeze theme

## Installation

### For Arch Linux

Clone this repo, `makepkg` and install.

### Manual Installation

1. Clone this repository
2. Install dependencies of `python-requests`, archlinux for example:

   ```bash
   sudo pacman -S python-requests
   ```

3. Copy files to appropriate locations:

   ```bash
   sudo cp sddm-breeze-bing-wallpaper.py /usr/local/bin/
   sudo cp sddm-breeze-bing-wallpaper.service /etc/systemd/system/
   sudo cp sddm-breeze-bing-wallpaper.timer /etc/systemd/system/
   ```

## Usage

### Enable and start the service

```bash
sudo systemctl enable --now sddm-breeze-bing-wallpaper.timer
```

### Check service status

```bash
systemctl status sddm-breeze-bing-wallpaper.service
```

### Manual run

```bash
/usr/local/bin/sddm-breeze-bing-wallpaper.py
```

## License

GPLv2