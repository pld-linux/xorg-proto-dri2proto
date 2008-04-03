Summary:	DRI2 protocol and ancillary headers
Name:		xorg-proto-dri2proto
Version:	1.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/dri2proto-%{version}.tar.bz2
# Source0-md5:	1d70f0653b0b3a837853262dc5d34da4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DRI2 protocol and ancillary headers.

%package devel
Summary:	DRI2 protocol and ancillary headers
Group:		X11/Development/Libraries
Requires:	libdrm-devel
Requires:	xorg-proto-glproto-devel
Requires:	xorg-proto-xproto-devel

%description devel
DRI2 protocol and ancillary headers.

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
%{_includedir}/X11/extensions/dri2proto.h
%{_pkgconfigdir}/dri2proto.pc
