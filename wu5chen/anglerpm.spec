Name: anglerpm
Version: 0.1
Release: 1%{?dist}
Summary: Get your name and show sin and cos value.

Group: Scientific Support
License: GPLv2
URL: http:/playground.openeuler.org/
Source0: anglerpm-0.1.tar.gz

# BuildRequires:

%description 
This package will let you input your name and calculate sin cos value

%prep
%setup -q

%build
./configure
make

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 anglerpm %{buildroot}/usr/local/bin

%files
/usr/local/bin/anglerpm

%changelog
* Tues Septe 20 2022 openEuler Playground playground@openeuler.org - 0.1 - Build the program & Happy Valentine's Day
