Summary:	IBMCA engine for OpenSSL
Summary(pl.UTF-8):	Silnik IBMCA dla OpenSSL-a
Name:		openssl-engine-ibmca
Version:	2.0.0
Release:	1
License:	OpenSSL (Apache-like)
Group:		Libraries
Source0:	https://downloads.sourceforge.net/opencryptoki/openssl-ibmca-%{version}.tar.gz
# Source0-md5:	c790483f33b6a3a69df0a859a4417525
URL:		https://opencryptoki.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.3
BuildRequires:	libica-devel >= 3.3.0
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.1.0
BuildRequires:	pkgconfig
Requires:	libica >= 3.3.0
Requires:	openssl >= 1.1.0
# because of libica-2 usage
ExclusiveArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		enginesdir	%(pkg-config --variable=enginesdir libcrypto)

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
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--libdir=%{enginesdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{enginesdir}/ibmca.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md src/openssl.cnf.sample
%attr(755,root,root) %{enginesdir}/ibmca.so*
%{_mandir}/man5/ibmca.5*
