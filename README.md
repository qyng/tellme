# vecl-utils

## deb build
dpkg-buildpackage

## rpm build
tar Jcf vecl-utils_x.y.tar.xz vecl-utils --xform="s/vecl-utils/vecl-utils-x.y/"
rpmbuild -ta vecl-utils_x.y.tar.xz
