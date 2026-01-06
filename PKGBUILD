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
            '49d66c7ed5023ef3a0ee54cebd857b22d3cdc5ab149124a58cc92adf3fd59e96'
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
  pyinstaller --onefile --clean --strip kipresence.py
}

package() {
    cd "$srcdir"
    install -Dm755 dist/kipresence "$pkgdir/usr/bin/kipresence"
    install -Dm644 kipresence.service $pkgdir/usr/lib/systemd/system/kipresence.service
}
