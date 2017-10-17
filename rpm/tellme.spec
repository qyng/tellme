Name:       tellme
Version:    1.1
Release:    1
Summary:    tellme
License:    GPL
Source:     tellme_1.1.tar.xz
BuildArchitectures: noarch

%description

%prep
%setup

%install
install -d $RPM_BUILD_ROOT/usr/bin
install src/tellme $RPM_BUILD_ROOT/usr/bin

%files
%{_bindir}/tellme
