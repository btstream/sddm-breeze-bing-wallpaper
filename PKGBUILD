# Maintainer: Your Name <your@email.com>
pkgname=sddm-breeze-bing-wallpaper
pkgver=1.1
pkgrel=1
pkgdesc="Automatically set Bing daily wallpaper as SDDM breeze theme background"
arch=('any')
url="https://github.com/btstream/sddm-breeze-bing-wallpaper"
license=('MIT')
depends=('python' 'python-requests' 'sddm')
source=("sddm-breeze-bing-wallpaper.py"
    "sddm-breeze-bing-wallpaper.service"
    "sddm-breeze-bing-wallpaper.timer"
    "theme.conf.user")
md5sums=('df9ed4c34119ba2108532f20fa323d20'
         'f16f002bf7482894f819463e7755f717'
         '014e2161eab4379d340be395e333a07c'
         '620dbce94ff5d50e5c7f8437be1c9ab9')

package() {
    # Install Python script
    install -Dm755 "$srcdir/sddm-breeze-bing-wallpaper.py" "$pkgdir/usr/lib/sddm/sddm-breeze-bing-wallpaper.py"

    # Install systemd units
    install -Dm644 "$srcdir/sddm-breeze-bing-wallpaper.service" "$pkgdir/usr/lib/systemd/system/sddm-breeze-bing-wallpaper.service"
    install -Dm644 "$srcdir/sddm-breeze-bing-wallpaper.timer" "$pkgdir/usr/lib/systemd/system/sddm-breeze-bing-wallpaper.timer"

    # Install theme configuration
    install -Dm644 "$srcdir/theme.conf.user" "$pkgdir/usr/share/sddm/themes/breeze/theme.conf.user"
}
