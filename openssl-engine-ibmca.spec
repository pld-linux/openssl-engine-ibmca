Summary:	IBMCA engine for OpenSSL
Summary(pl.UTF-8):	Silnik IBMCA dla OpenSSL-a
Name:		openssl-engine-ibmca
Version:	1.0.0
Release:	1
License:	OpenSSL (Apache-like)
Group:		Libraries
Source0:	http://dl.sourceforge.net/opencryptoki/openssl-ibmca-%{version}.tar.bz2
# Source0-md5:	403fb0544017ebf6c1c9bd2501015154
URL:		http://opencryptoki.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6.3
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	sed >= 4.0
Requires:	libica = 1.3.8
Requires:	openssl >= 0.9.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a shared object OpenSSL dynamic engine for the
IBM eServer Cryptographic Accelerator (ICA).

%description -l pl.UTF-8
Ten pakiet zawiera dynamiczny moduł silnika OpenSSL dla akceleratora
kryptograficznego IBM eServer Cryptographic Accelerator (ICA).

%prep
%setup -q -n openssl-ibmca-%{version}

sed -i -e 's/"ica"/"libica-1.3.8.so"/' ica_openssl_api.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	ac_cv_lib_ica_icaOpenAdapter=yes \
	--with-engines-dir=%{_libdir}/engines \
	--with-openssl=/usr \
	
%{__make} \
	libibmca_la_LIBADD=-lcrypto \
	libibmca_la_DEPENDENCIES=

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libibmca_la_DEPENDENCIES=

rm -f $RPM_BUILD_ROOT%{_libdir}/engines/libibmca.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/engines
%attr(755,root,root) %{_libdir}/engines/libibmca.so*
