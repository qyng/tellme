Name:       vecl-utils
Version:    1.0
Release:    1
Summary:    vecl utils
License:    GPL
Source:     vecl-utils_1.0.tar.xz
BuildArchitectures: noarch

%description

%prep
%setup

%install
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/sbin
install src/ifreset $RPM_BUILD_ROOT/usr/sbin
install src/tellme $RPM_BUILD_ROOT/usr/bin

%files
%{_sbindir}/ifreset
%{_bindir}/tellme
