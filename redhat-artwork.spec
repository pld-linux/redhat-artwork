Summary:	Bluecurve look & feel
Summary(pl):	Wygl±dy Bluecurve
Name:		redhat-artwork
Version:	0.73
Release:	1
Group:		Themes
License:	GPL
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	124b27820d7e34e48b630d82f6a5a1f6
Patch0:		%{name}-makefilefix.patch
URL:		http://www.redhat.com
BuildRequires:	pkgconfig
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	qt-devel >= 3.0
BuildRequires:	kdebase-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _icondir        /usr/share/icons

%description
Bluecurve look & feel.

%description -l pl
Wygl±dy Bluecurve

%package -n icons-Bluecurve
Summary:	Bluecurve icons
Summary(pl):	Ikony Bluecurve
Group:		Themes

%description -n icons-Bluecurve
Bluecurve icons

%description -n icons-Bluecurve -l pl
Ikony Bluecurve

%package -n gnome-theme-Bluecurve
Summary:	GNOME Bluecurve theme
Summary(pl):	Bluecurve dla GNOME
Group:		Themes
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes:	metacity-theme-Bluecurve
Requires:	icons-Bluecurve

%description -n gnome-theme-Bluecurve
GNOME Bluecurve theme (gtk, gtk2, metacity, nautilus)

%description -n gnome-theme-Bluecurve -l pl
Bluecurve dla GNOME (gtk, gtk2, metacity, nautilus)

%package -n nautilus-theme-Bluecurve
Summary:	Nautilus Bluecurve theme
Summary(pl):	Bluecurve dla Nautilusa
Group:		Themes
Requires:	nautilus

%description -n nautilus-theme-Bluecurve
Nautilus Bluecurve theme

%description -n nautilus-theme-Bluecurve -l pl
Bluecurve dla Nautilusa

%package -n xmms-skin-Bluecurve
Summary:	XMMS skin taken from Bluecurve
Summary(pl):	Skórka dla XMMS'a w stylu Bluecurve
Group:		X11/Applications/Multimedia
Requires:	xmms

%description -n xmms-skin-Bluecurve
XMMS skin taken from Bluecurve

%description -n xmms-skin-Bluecurve -l pl
Skórka dla XMMS'a w stylu Bluecurve

%package -n qt-style-Bluecurve
Summary:	Bluecurve QT style
Summary(pl):	Styl Bluecurve dla QT
Group:		Themes
Requires:	qt >= 3.0

%description -n qt-style-Bluecurve
Bluecurve QT style

%description -n qt-style-Bluecurve -l pl
Styl Bluecyrve dla QT

%package -n kde-decoration-Bluecurve
Summary:	Bluecurve KDE style
Summary(pl):	Styl Bluecurve dla KDE
Group:		Themes
Requires:	qt-style-Bluecurve

%description -n kde-decoration-Bluecurve
Bluecurve KDE style

%description -n kde-decoration-Bluecurve -l pl
Styl Bluecurve dla KDE

%package -n XFree86-Xcursor-packs-Bluecurve
Summary:	Bluecurve cursor pack
Summary(pl):	Motyw kursorów Bluecurve
Group:		X11/XFree86
Requires:	XFree86

%description -n XFree86-Xcursor-packs-Bluecurve
Bluecurve cursor pack

%description -n XFree86-Xcursor-packs-Bluecurve
Motyw kursorów Bluecurve

%package -n gdm-theme-Bluecurve
Summary:	Bluecurve GDM theme
Summary(pl):	Temat Bluecurve do GDM'a
Group:		Themes
Requires:	gdm >= 2.4

%description -n gdm-theme-Bluecurve
Bluecurve GDM theme

%description -n gdm-theme-Bluecurve -l pl
Temat Bluecurve do GDM'a

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_icondir}/Bluecurve/cursors
install -d $RPM_BUILD_ROOT%{_icondir}/Bluecurve-inverse/cursors
install art/cursor/Bluecurve/Bluecurve/* $RPM_BUILD_ROOT%{_icondir}/Bluecurve/cursors/
install art/cursor/Bluecurve-inverse/Bluecurve-inverse/* $RPM_BUILD_ROOT%{_icondir}/Bluecurve-inverse/cursors/
mv $RPM_BUILD_ROOT%{_pixmapsdir}/*.png $RPM_BUILD_ROOT%{_datadir}/icons/Bluecurve/48x48/apps/
mv -f $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.so
install -d $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/styles
mv $RPM_BUILD_ROOT%{_libdir}/qt-3.1/plugins/styles/bluecurve.so $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/styles/libbluecurve.so

%clean
rm -rf $RPM_BUILD_ROOT

%files -n icons-Bluecurve
%defattr(644,root,root,755)
%{_icondir}/Bluecurve/16x16
%{_icondir}/Bluecurve/22x22
%{_icondir}/Bluecurve/24x24
%{_icondir}/Bluecurve/32x32
%{_icondir}/Bluecurve/48x48
%{_icondir}/Bluecurve/64x64
%{_icondir}/Bluecurve/72x72
%{_icondir}/Bluecurve/96x96
%{_icondir}/Bluecurve/192x192
%{_icondir}/Bluecurve/index.theme

%files -n gnome-theme-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/libbluecurve.so
%{_libdir}/gtk-2.0/*/engines/libbluecurve.la
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/libbluecurve.so
%{_datadir}/locale
%{_datadir}/themes/Bluecurve

%files -n nautilus-theme-Bluecurve
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/Bluecurve

%files -n xmms-skin-Bluecurve
%defattr(644,root,root,755)
%{_datadir}/xmms/Skins/Bluecurve-xmms.zip

%files -n qt-style-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins-mt/styles/libbluecurve.so

%files -n kde-decoration-Bluecurve
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin_bluecurve.la
%attr(755,root,root) %{_libdir}/kde3/kwin_bluecurve.so
%{_datadir}/apps

%files -n XFree86-Xcursor-packs-Bluecurve
%defattr(644,root,root,755)
%dir %{_icondir}/Bluecurve
%{_icondir}/Bluecurve/cursors
%{_icondir}/Bluecurve-inverse

%files -n gdm-theme-Bluecurve
%defattr(644,root,root,755)
%{_datadir}/gdm
