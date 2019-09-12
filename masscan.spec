%define	debug_package %{nil}

Name:		masscan
Version:	1.0.5
Release:	1
Summary:	This is the fastest Internet port scanner
License:	BSD
URL:		https://github.com/robertdavidgraham/masscan
Source0:        https://github.com/robertdavidgraham/masscan/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(libpcap)


%description
It is a faster port scan that produces results similar to nmap,
the most famous port scanner. Internally, it operates more like
scanrand, unicornscan, and ZMap, using asynchronous transmission.


%prep
%setup -q
#patch0 -p1 -b .secondary
#patch1 -p1
sed -i 's/\r$//' VULNINFO.md


%build
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"


%install
mkdir -p %{buildroot}%{_bindir}/
install -pm 0755 bin/masscan %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_docdir}/man8
cp -a doc/masscan.8 %{buildroot}%{_docdir}/man8


%files
%license LICENSE
%doc VULNINFO.md README.md
%{_bindir}/masscan
%{_docdir}/man8/masscan.8
