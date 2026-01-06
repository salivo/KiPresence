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
sha256sums=('88939b470933ff55086b229e4214d516d74195c159b72ac27e7dabe079040094'
            '87d3007338106c37adad85d41c8e142f266689c7520d402f015422d1c25aee96'
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
