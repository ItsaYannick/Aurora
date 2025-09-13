# Maintainer: Yannick Winkler JaxterLP@gmail.com
pkgname=aurora
pkgver=0.1.0
pkgrel=1
pkgdesc="A sassy AI assistant that roasts you about your Arch updates"
arch=('any')
url="https://github.com/ItsaYannick/Aurora"
license=('GPL3')  # Or whatever license you use
depends=('python' 'pacman-contrib' 'python-rich')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')  # Replace with actual checksum if you want

package() {
    cd "$srcdir/Aurora-$pkgver"
    install -Dm755 Aurora.py "$pkgdir/usr/bin/aurora"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

