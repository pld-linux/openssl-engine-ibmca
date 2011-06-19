Summary:	IBMCA engine for OpenSSL
Summary(pl.UTF-8):	Silnik IBMCA dla OpenSSL-a
Name:		openssl-engine-ibmca
Version:	1.2.0
Release:	1
License:	OpenSSL (Apache-like)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/opencryptoki/openssl-ibmca-%{version}.tar.gz
# Source0-md5:	df14df18d276ab3106dffb8b7623896a
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6.3
BuildRequires:	libica-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.8
Requires:	libica >= 2.0
Requires:	openssl >= 0.9.8
# because of libica-2 usage
ExclusiveArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a shared object OpenSSL dynamic engine for the
IBM eServer Cryptographic Accelerator (ICA).

%description -l pl.UTF-8
Ten pakiet zawiera dynamiczny moduł silnika OpenSSL dla akceleratora
kryptograficznego IBM eServer Cryptographic Accelerator (ICA).

%prep
%setup -q -n openssl-ibmca-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{_libdir}/engines
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/engines/libibmca.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README openssl.cnf.sample
%attr(755,root,root) %{_libdir}/engines/libibmca.so
