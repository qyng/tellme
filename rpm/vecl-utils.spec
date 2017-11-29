Name:       vecl-utils
Version:    1.1
Release:    1
Summary:    vecl utils
License:    GPL
Source:     vecl-utils_1.1.tar.xz
BuildArchitectures: noarch

%description
 ifreset  reset network interface
 ssh-to   ssh with password automatically
 tellme   describe commands et al

%prep
%setup

%install
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/sbin
install src/ifreset $RPM_BUILD_ROOT/usr/sbin
install src/tellme $RPM_BUILD_ROOT/usr/bin
install src/ssh-expect $RPM_BUILD_ROOT/usr/bin
install src/ssh-to $RPM_BUILD_ROOT/usr/bin

%files
%{_sbindir}/ifreset
%{_bindir}/tellme
# may to libexec
%{_bindir}/ssh-expect
%{_bindir}/ssh-to
