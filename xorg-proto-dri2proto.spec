Summary:	DRI2 extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia DRI2
Name:		xorg-proto-dri2proto
Version:	2.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/dri2proto-%{version}.tar.bz2
# Source0-md5:	5cb7987d29db068153bdc8f23c767c43
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRI2 extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia DRI2.

%package devel
Summary:	DRI2 extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia DRI2
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
DRI2 extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia DRI2.

%prep
%setup -q -n dri2proto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING
%{_includedir}/X11/extensions/dri2*.h
%{_pkgconfigdir}/dri2proto.pc
