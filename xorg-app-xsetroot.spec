# $Rev: 3421 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xsetroot application
Summary(pl):	Aplikacja xsetroot
Name:		xorg-app-xsetroot
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xsetroot-%{version}.tar.bz2
# Source0-md5:	66d8db8638c21db7e6bd2d7ed4578f0a
Patch0:		xsetroot-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRequires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/xsetroot-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xsetroot application.

%description -l pl
Aplikacja xsetroot.


%prep
%setup -q -n xsetroot-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
