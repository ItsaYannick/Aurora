# Maintainer: Yannick Winkler <JaxterLP@gmail.com>
pkgname=aurora
pkgver=0.1.1
pkgrel=1
pkgdesc="A sassy AI assistant that roasts you about your Arch updates"
arch=('any')
url="https://github.com/ItsaYannick/Aurora"
license=('GPL3')
depends=('python' 'pacman-contrib' 'python-rich')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
    cd "$srcdir/Aurora-$pkgver"   # make sure this matches the actual folder name!

    # Main script
    install -Dm755 Aurora.py "$pkgdir/usr/bin/aurora"

    # Support module
    install -Dm644 responses.py "$pkgdir/usr/lib/aurora/responses.py"

    # License and docs
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
