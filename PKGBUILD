# Maintainer: Your Name <your@email.com>
pkgname=sddm-breeze-bing-wallpaper
pkgver=1.0
pkgrel=3
pkgdesc="Automatically set Bing daily wallpaper as SDDM breeze theme background"
arch=('any')
url="https://github.com/btstream/sddm-breeze-bing-wallpaper"
license=('MIT')
depends=('python' 'python-requests' 'sddm')
source=("sddm-breeze-bing-wallpaper.py"
        "sddm-breeze-bing-wallpaper.service"
        "sddm-breeze-bing-wallpaper.timer"
        "theme.conf.user")
md5sums=('8c27d4758f867986d2667f92a0255e8c'
         '4fa9dbdcbec551ac76210306f0ab9868'
         'f6eeb53a4048ada1f5bd1496cb8bea39'
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
