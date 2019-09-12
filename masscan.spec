%define	debug_package %{nil}

Name:		masscan
Version:	1.0.5
Release:	1
Summary:	This is the fastest Internet port scanner
License:	BSD
URL:		https://github.com/robertdavidgraham/masscan
Source0:        https://github.com/robertdavidgraham/masscan/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	clang git
BuildRequires:	pkgconfig(libpcap)


%description
It is a faster port scan that produces results similar to nmap,
the most famous port scanner. Internally, it operates more like
scanrand, unicornscan, and ZMap, using asynchronous transmission.

%prep
%setup -q
sed -i 's/\r$//' VULNINFO.md

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}/
install -pm 0755 bin/masscan %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man8
install -pm 0755 doc/masscan.8 %{buildroot}%{_mandir}/man8/masscan.8

%files
%license LICENSE
%doc VULNINFO.md README.md
%{_bindir}/masscan
%{_mandir}/man8/masscan.*
