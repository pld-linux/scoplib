#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	SCoPLib - library for polyhedral representation of high level programs
Summary(pl.UTF-8):	SCoPLib - biblioteka do wielościanowej reprezentacji programów w językach wyższego poziomu
Name:		scoplib
Version:	0.2.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://web.cse.ohio-state.edu/~pouchet/software/pocc/download/modules/%{name}-%{version}.tar.gz
# Source0-md5:	611f1ea5f7d5203e02b46c9d242a245b
BuildRequires:	gmp-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCoPLib is a library for polyhedral representation of some parts of
high level programs written in C, C++, C# or Java.

%description -l pl.UTF-8
SCoPLib to biblioteka do wielościanowej reprezentacji wybranych części
programów napisanych w językach wyższego poziomu, takich jak C, C++,
C# lub Java.

%package devel
Summary:	Header files for SCoPLib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SCoPLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel

%description devel
Header files for SCoPLib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SCoPLib.

%package static
Summary:	Static SCoPLib library
Summary(pl.UTF-8):	Statyczna biblioteka SCoPLib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SCoPLib library.

%description static -l pl.UTF-8
Statyczna biblioteka SCoPLib.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# outdated
%{__rm} $RPM_BUILD_ROOT%{_infodir}/clan.info*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/libscoplib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libscoplib.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libscoplib.so
%{_libdir}/libscoplib.la
%{_includedir}/scoplib

%files static
%defattr(644,root,root,755)
%{_libdir}/libscoplib.a
