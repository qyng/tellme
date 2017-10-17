# tellme

## deb build
dpkg-buildpackage

## rpm build
tar Jcf tellme_1.0.tar.xz tellme --xform="s/tellme/tellme-1.0/"
rpmbuild -ta tellme_1.0.tar.xz
