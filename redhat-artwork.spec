Summary:	Bluecurve look & feel
Summary(pl):	Wygl±dy Bluecurve
Name:		redhat-artwork
Version:	0.78
Release:	1
Group:		Themes
License:	GPL
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	ad3507a52b3577fa04fab8bcabdccb6f
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.redhat.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	icon-slicer
BuildRequires:	kdebase-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluecurve look & feel.

%description -l pl
Wygl±dy Bluecurve.

%package -n icons-Bluecurve
Summary:	Bluecurve icons
Summary(pl):	Ikony Bluecurve
Group:		Themes

%description -n icons-Bluecurve
Bluecurve icons for GNOME & KDE.

%description -n icons-Bluecurve -l pl
Ikony Bluecurve dla GNOME i KDE.

%package -n gnome-theme-Bluecurve
Summary:	GNOME Bluecurve theme
Summary(pl):	Bluecurve dla GNOME
Group:		Themes
Requires:	icons-Bluecurve
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes:	metacity-theme-Bluecurve

%description -n gnome-theme-Bluecurve
GNOME Bluecurve theme (gtk, gtk2, metacity, nautilus).

%description -n gnome-theme-Bluecurve -l pl
Motyw Bluecurve dla GNOME (gtk, gtk2, metacity, nautilus).

%package -n nautilus-theme-Bluecurve
Summary:	Nautilus Bluecurve theme
Summary(pl):	Bluecurve dla Nautilusa
Group:		Themes
Requires:	nautilus

%description -n nautilus-theme-Bluecurve
Nautilus Bluecurve theme.

%description -n nautilus-theme-Bluecurve -l pl
Motyw Bluecurve dla Nautilusa.

%package -n xmms-skin-Bluecurve
Summary:	XMMS skin taken from Bluecurve
Summary(pl):	Skórka dla XMMS-a w stylu Bluecurve
Group:		X11/Applications/Multimedia
Requires:	xmms

%description -n xmms-skin-Bluecurve
XMMS skin taken from Bluecurve.

%description -n xmms-skin-Bluecurve -l pl
Skórka dla XMMS-a w stylu Bluecurve.

%package -n qt-style-Bluecurve
Summary:	Bluecurve QT style
Summary(pl):	Styl Bluecurve dla QT
Group:		Themes
Requires:	qt >= 3.0

%description -n qt-style-Bluecurve
Bluecurve QT style.

%description -n qt-style-Bluecurve -l pl
Styl Bluecurve dla QT.

%package -n kde-decoration-Bluecurve
Summary:	Bluecurve KDE style
Summary(pl):	Styl Bluecurve dla KDE
Group:		Themes
Requires:	qt-style-Bluecurve

%description -n kde-decoration-Bluecurve
Bluecurve KDE style.

%description -n kde-decoration-Bluecurve -l pl
Styl Bluecurve dla KDE.

%package -n XFree86-Xcursor-packs-Bluecurve
Summary:	Bluecurve cursor pack
Summary(pl):	Motyw kursorów Bluecurve
Group:		X11/XFree86
Requires:	XFree86

%description -n XFree86-Xcursor-packs-Bluecurve
Bluecurve cursor pack.

%description -n XFree86-Xcursor-packs-Bluecurve -l pl
Motyw kursorów Bluecurve.

%package -n gdm-theme-Bluecurve
Summary:	Bluecurve GDM theme
Summary(pl):	Motyw Bluecurve dla GDM-a
Group:		Themes
Requires:	gdm >= 2.4

%description -n gdm-theme-Bluecurve
Bluecurve GDM theme.

%description -n gdm-theme-Bluecurve -l pl
Motyw Bluecurve dla GDM-a.

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
install -d $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/styles

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.so
mv $RPM_BUILD_ROOT%{_libdir}/qt-3.1/plugins/styles/bluecurve.so $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/styles/libbluecurve.so

rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/libbluecurve.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n icons-Bluecurve
%defattr(644,root,root,755)
%{_iconsdir}/Bluecurve/16x16
%{_iconsdir}/Bluecurve/24x24
%{_iconsdir}/Bluecurve/36x36
%{_iconsdir}/Bluecurve/48x48
%{_iconsdir}/Bluecurve/96x96
%{_iconsdir}/Bluecurve/index.theme
%{_pixmapsdir}/*.png

%files -n gnome-theme-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/libbluecurve.so
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/libbluecurve.so
# TODO: fix (too many dirs)
%{_datadir}/locale
%{_datadir}/themes

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
%attr(755,root,root) %{_libdir}/kde3/kwin_bluecurve.so
%{_libdir}/kde3/kwin_bluecurve.la
# TODO: fix
%{_datadir}/apps

%files -n XFree86-Xcursor-packs-Bluecurve
%defattr(644,root,root,755)
%dir %{_iconsdir}/Bluecurve
%{_iconsdir}/Bluecurve/cursors
%{_iconsdir}/Bluecurve-inverse

%files -n gdm-theme-Bluecurve
%defattr(644,root,root,755)
# TODO: fix
%{_datadir}/gdm
