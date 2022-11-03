Summary:	xsetroot application - root window parameter setting utility for X
Summary(pl.UTF-8):	Aplikacja xsetroot - narzędzie do zmiany parametrów głównego okna X
Name:		xorg-app-xsetroot
Version:	1.1.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xsetroot-%{version}.tar.xz
# Source0-md5:	fa9a24fe5b1725c52a4566a62dd0a50d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-data-xbitmaps
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xsetroot program allows you to tailor the appearance of the
background ("root") window on a workstation display running X.
Normally, you experiment with xsetroot until you find a personalized
look that you like, then put the xsetroot command that produces it
into your X startup file.

%description -l pl.UTF-8
Program xsetroot pozwala dostroić wygląd tła (głównego okna) ekranu z
działającym X. Zwykle eksperymentuje się z xsetroot do osiągnięcia
lubianego, spersonalizowanego wyglądu, a następnie umieszcza tworzące
go polecenie xsetroot w pliku startowym X.

%prep
%setup -q -n xsetroot-%{version}

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xsetroot
%{_mandir}/man1/xsetroot.1*
