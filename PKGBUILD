# Maintainer: Andrii Salivon <andrijsalivon@gmail.com>
pkgname=kipresence
pkgver=0.0.1
pkgrel=1
pkgdesc="System service that updates Discord status with KiCad activity."
arch=('x86_64')
url="https://github.com/salivo/KiPresence"
license=('MIT')
makedepends=("python")
source=("kipresence.py"
        "kicad_connect.py"
        "kipresence.service"
        "requirements.txt")
noextract=()
sha256sums=('f7aeab98f22102018bf79e09b8554739cf348894d1cfdcdbb88182e23da79aab'
            '2ab623f96755684997efe34763b04876fd3c1c369a41fdbf7151bf653245bd4c'
            'e1c283514c2833b6c787ecba50a38047b670eb39d3c65c3335471134d5c5b79a'
            'edc2ced1cdc3bd222881c82c6c30e952d6722b46057c2476700e08f92ed77a8e')

prepare() {
    cd "$srcdir"
    python -m venv venv
    source venv/bin/activate
    python -m pip install -r requirements.txt
}

build() {
  cd "$srcdir"
  source venv/bin/activate
  HIDDEN=$(awk '{print "--hidden-import="$1}' requirements.txt)
  pyinstaller --onefile --clean --strip $HIDDEN kipresence.py
}

package() {
    cd "$srcdir"
    install -Dm755 dist/kipresence "$pkgdir/usr/bin/kipresence"
    install -Dm644 kipresence.service "$pkgdir/etc/systemd/user/kipresence.service"

}
