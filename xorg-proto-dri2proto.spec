Summary:	DRI2 extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia DRI2
Name:		xorg-proto-dri2proto
Version:	2.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/dri2proto-%{version}.tar.bz2
# Source0-md5:	0cdeb1e95901813385dc9576be272bd3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRI2 (Direct Rendering Infrastructure 2) extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia DRI2 (Direct Rendering Infrastructure 2).

%package devel
Summary:	DRI2 extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia DRI2
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
DRI2 (Direct Rendering Infrastructure 2) extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia DRI2 (Direct Rendering Infrastructure 2).

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
%doc COPYING ChangeLog README dri2proto.txt
%{_includedir}/X11/extensions/dri2*.h
%{_pkgconfigdir}/dri2proto.pc
