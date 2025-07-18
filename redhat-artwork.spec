#
# Conditional build
%bcond_without	kde
#
Summary:	Bluecurve look & feel
Summary(pl.UTF-8):	Wyglądy Bluecurve
Name:		redhat-artwork
Version:	0.117
Release:	6
Group:		Themes
License:	GPL
Source0:	ftp://distfiles.pld-linux.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	91caaefd6629364c282181b34be13b57
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-mouse_position.patch
URL:		http://www.redhat.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel >= 1.2.9
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	icon-slicer
%if %{with kde}
BuildRequires:	kdebase-devel >= 3.1.90
%endif
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 1:3.0
BuildRequires:	xorg-app-xcursorgen
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluecurve look & feel.

%description -l pl.UTF-8
Wyglądy Bluecurve.

%package -n icons-Bluecurve
Summary:	Bluecurve icons
Summary(pl.UTF-8):	Ikony Bluecurve
Group:		Themes
# contains dir used by icons
Requires:	XcursorTheme-Bluecurve

%description -n icons-Bluecurve
Bluecurve icons for GNOME & KDE.

%description -n icons-Bluecurve -l pl.UTF-8
Ikony Bluecurve dla GNOME i KDE.

%package -n gtk-theme-engine-Bluecurve
Summary:	GTK+ Bluecurve theme
Summary(pl.UTF-8):	Bluecurve dla GTK+
Group:		Themes
Requires:	icons-Bluecurve
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes: 	gnome-theme-Bluecurve < 0.89

%description -n gtk-theme-engine-Bluecurve
GTK+ Bluecurve theme.

%description -n gtk-theme-engine-Bluecurve -l pl.UTF-8
Motyw Bluecurve dla GTK.

%package -n metacity-themes-Bluecurve-redhat
Summary:	Metacity Bluecurve theme
Summary(pl.UTF-8):	Bluecurve dla Metacity
Group:		Themes
Requires:	icons-Bluecurve
Requires:	metacity
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes:	metacity-theme-Bluecurve
Obsoletes:	gnome-theme-Bluecurve < 0.89
Obsoletes:	metacity-theme-Bluecurve-redhat
Conflicts:	metacity-themes-Bluecurve

%description -n metacity-themes-Bluecurve-redhat
GTK+ Bluecurve Metacity.

%description -n metacity-themes-Bluecurve-redhat -l pl.UTF-8
Motyw Bluecurve dla Metacity.

%package -n gnome-theme-Bluecurve
Summary:	GNOME Bluecurve theme
Summary(pl.UTF-8):	Bluecurve dla GNOME
Group:		Themes
Requires:	icons-Bluecurve
Requires:	metacity-themes-Bluecurve-redhat
Requires:	gtk2-theme-engine-Bluecurve
Requires:	gtk-theme-engine-Bluecurve
Requires:	nautilus-theme-Bluecurve
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes:	metacity-theme-Bluecurve

%description -n gnome-theme-Bluecurve
GNOME Bluecurve theme (gtk, gtk2, metacity, nautilus).

%description -n gnome-theme-Bluecurve -l pl.UTF-8
Motyw Bluecurve dla GNOME (gtk, gtk2, metacity, nautilus).

%package -n gtk2-theme-engine-Bluecurve
Summary:	GTK+2 Bluecurve theme
Summary(pl.UTF-8):	Bluecurve dla GTK+2
Group:		Themes
Requires:	icons-Bluecurve
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes:	metacity-theme-Bluecurve
Obsoletes:	gnome-theme-Bluecurve < 0.89

%description -n gtk2-theme-engine-Bluecurve
GTK+2 Bluecurve theme.

%description -n gtk2-theme-engine-Bluecurve -l pl.UTF-8
Motyw Bluecurve dla GTK+2.

%package -n nautilus-theme-Bluecurve
Summary:	Nautilus Bluecurve theme
Summary(pl.UTF-8):	Bluecurve dla Nautilusa
Group:		Themes
Requires:	nautilus

%description -n nautilus-theme-Bluecurve
Nautilus Bluecurve theme.

%description -n nautilus-theme-Bluecurve -l pl.UTF-8
Motyw Bluecurve dla Nautilusa.

%package -n xmms-skin-Bluecurve
Summary:	XMMS skin taken from Bluecurve
Summary(pl.UTF-8):	Skórka dla XMMS-a w stylu Bluecurve
Group:		X11/Applications/Multimedia
Requires:	xmms

%description -n xmms-skin-Bluecurve
XMMS skin taken from Bluecurve.

%description -n xmms-skin-Bluecurve -l pl.UTF-8
Skórka dla XMMS-a w stylu Bluecurve.

%package -n qt-style-Bluecurve
Summary:	Bluecurve Qt style
Summary(pl.UTF-8):	Styl Bluecurve dla Qt
Group:		Themes
Requires:	qt >= 3.0

%description -n qt-style-Bluecurve
Bluecurve Qt style.

%description -n qt-style-Bluecurve -l pl.UTF-8
Styl Bluecurve dla Qt.

%package -n kde-theme-Bluecurve
Summary:	Bluecurve KDE theme
Summary(pl.UTF-8):	Motyw Bluecurve dla KDE
Group:		Themes
Requires:	qt-style-Bluecurve

%description -n kde-theme-Bluecurve
Bluecurve KDE theme.

%description -n kde-theme-Bluecurve -l pl.UTF-8
Motyw Bluecurve dla KDE.

%package -n XcursorTheme-Bluecurve
Summary:	Bluecurve cursor pack
Summary(pl.UTF-8):	Motyw kursorów Bluecurve
Group:		Themes
Obsoletes:	XFree86-Xcursor-packs-Bluecurve

%description -n XcursorTheme-Bluecurve
Bluecurve cursor pack.

%description -n XcursorTheme-Bluecurve -l pl.UTF-8
Motyw kursorów Bluecurve.

%package -n gdm-theme-Bluecurve
Summary:	Bluecurve GDM theme
Summary(pl.UTF-8):	Motyw Bluecurve dla GDM-a
Group:		Themes
Requires:	gdm >= 2.4

%description -n gdm-theme-Bluecurve
Bluecurve GDM theme.

%description -n gdm-theme-Bluecurve -l pl.UTF-8
Motyw Bluecurve dla GDM-a.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1 -b .niedakh
#%%patch2 -p1

%build
%if !%{with kde}
sed -i -e "s,kde ,," art/Makefile.am
rm -rf art/kde/kwin/Bluecurve/configure.in.in
%endif

export QTDIR=%{_prefix}
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
%{__libtoolize}
## gettextize in pld is too screwed, i have gettexitized it using redhat's autogen.sh instead
##%%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--with-xinerama \
	--disable-rpath 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
export QTDIR=%{_prefix}
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
install -d $RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/styles

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#mv -f $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.so
#sed -e "s,\.0,," $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.la > $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bl.la
#mv -f $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bl.la $RPM_BUILD_ROOT%{_libdir}/kde3/kwin_bluecurve.la
#mv -f $RPM_BUILD_ROOT%{_libdir}/qt-3.1/plugins/styles/bluecurve.so \
#	$RPM_BUILD_ROOT%{_libdir}/qt/plugins-mt/styles/libbluecurve.so
#
#rm -f $RPM_BUILD_ROOT%{_libdir}/gtk*/*/engines/libbluecurve.la \
#	$RPM_BUILD_ROOT%{_libdir}/qt-*/plugins/styles/bluecurve.la

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

# locales for gdm theme
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n icons-Bluecurve
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Bluecurve*
%{_iconsdir}/Bluecurve/16x16
%{_iconsdir}/Bluecurve/20x20
%{_iconsdir}/Bluecurve/24x24
%{_iconsdir}/Bluecurve/32x32
%{_iconsdir}/Bluecurve/36x36
%{_iconsdir}/Bluecurve/48x48
%{_iconsdir}/Bluecurve/64x64
%{_iconsdir}/Bluecurve/96x96
%{_iconsdir}/Bluecurve/index.theme
%{_pixmapsdir}/*.png

%files -n gnome-theme-Bluecurve
%defattr(644,root,root,755)
%{_datadir}/themes/*/index.theme

%files -n gtk2-theme-engine-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/libbluecurve.so
%{_datadir}/themes/Bluecurve*/gtk-2.0/

%files -n gtk-theme-engine-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/libbluecurve.so
%{_datadir}/themes/Bluecurve*/gtk/

%files -n metacity-themes-Bluecurve-redhat
%defattr(644,root,root,755)
%{_datadir}/themes/Bluecurve*/metacity*/

%files -n nautilus-theme-Bluecurve
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/Bluecurve

%files -n xmms-skin-Bluecurve
%defattr(644,root,root,755)
%{_datadir}/xmms/Skins/Bluecurve-xmms.zip

%files -n qt-style-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt/plugins-mt/styles/bluecurve.so

%if %{with kde}
%files -n kde-theme-Bluecurve
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kwin3_bluecurve.so
%{_libdir}/kde3/kwin3_bluecurve.la
%{_datadir}/apps/kdisplay/color-schemes/Bluecurve.kcsrc
%{_datadir}/apps/kstyle/themes/Bluecurve.themerc
%{_datadir}/apps/kwin/bluecurve.desktop
%endif

%files -n XcursorTheme-Bluecurve
%defattr(644,root,root,755)
%dir %{_iconsdir}/Bluecurve
%{_iconsdir}/Bluecurve/cursors
%{_iconsdir}/Bluecurve-inverse

%files -n gdm-theme-Bluecurve -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Bluecurve
