
Summary:	Bluecurve look & feel
Summary(pl):	Wygl±dy Bluecurve
Name:		redhat-artwork
Version:	0.89
Release:	1
Group:		Themes
License:	GPL
Source0:	http://www.kernel.pl/~djurban/pld/%{name}-%{version}.tar.bz2
# Source0-md5:	16dce1391d6761cbaa3dda1ef13d82b0
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-am.patch
##Patch1:		%{name}-kde.patch
URL:		http://www.redhat.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	icon-slicer
%if %{with kde}
BuildRequires:	kdebase-devel >= 3.1.90
%endif
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 3.0
BuildRequires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluecurve look & feel.

%description -l pl
Wygl±dy Bluecurve.

%package -n icons-Bluecurve
Summary:	Bluecurve icons
Summary(pl):	Ikony Bluecurve
Group:		Themes
# contains dir used by icons
Requires:	XFree86-Xcursor-packs-Bluecurve

%description -n icons-Bluecurve
Bluecurve icons for GNOME & KDE.

%description -n icons-Bluecurve -l pl
Ikony Bluecurve dla GNOME i KDE.

%package -n gtk-theme-engine-Bluecurve
Summary:	GTK+ Bluecurve theme
Summary(pl):	Bluecurve dla GTK+
Group:		Themes
Requires:	icons-Bluecurve
Obsoletes:	gtk2-theme-engine-Wonderland
Obsoletes:	metacity-theme-Bluecurve
Obsoletes: 	gnome-theme-Bluecurve < 0.89

%description -n gtk-theme-engine-Bluecurve
GTK+ Bluecurve theme.

%description -n gtk-theme-engine-Bluecurve -l pl
Motyw Bluecurve dla GTK.

%package -n metacity-theme-Bluecurve
Summary:        Metacity Bluecurve theme
Summary(pl):    Bluecurve dla Metacity
Group:          Themes
Requires:       icons-Bluecurve
Obsoletes:      gtk2-theme-engine-Wonderland
Obsoletes:      metacity-theme-Bluecurve
Obsoletes:      gnome-theme-Bluecurve < 0.89

%description -n metacity-theme-Bluecurve
GTK+ Bluecurve Metacity.

%description -n metacity-theme-Bluecurve -l pl
Motyw Bluecurve dla Metacity.


%package -n gnome-theme-Bluecurve
Summary:        GNOME Bluecurve theme
Summary(pl):    Bluecurve dla GNOME
Group:          Themes
Requires:       icons-Bluecurve
Obsoletes:      gtk2-theme-engine-Wonderland
Obsoletes:      metacity-theme-Bluecurve
Requires:	metacity-theme-Bluecurve
Requires:	gtk2-theme-engine-Bluecurve
Requires:       gtk-theme-engine-Bluecurve

%description -n gnome-theme-Bluecurve
GNOME Bluecurve theme (gtk, gtk2, metacity).

%description -n gnome-theme-Bluecurve -l pl
Motyw Bluecurve dla GNOME (gtk, gtk2, metacity).


%package -n gtk2-theme-engine-Bluecurve
Summary:        GTK+2 Bluecurve theme
Summary(pl):    Bluecurve dla GTK+2
Group:          Themes
Requires:       icons-Bluecurve
Obsoletes:      gtk2-theme-engine-Wonderland
Obsoletes:      metacity-theme-Bluecurve
Obsoletes:      gnome-theme-Bluecurve < 0.89

%description -n gtk2-theme-engine-Bluecurve
GTK+2 Bluecurve theme.

%description -n gtk2-theme-engine-Bluecurve -l pl
Motyw Bluecurve dla GTK+2.

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

%package -n kde-theme-Bluecurve
Summary:	Bluecurve KDE theme
Summary(pl):	Motyw Bluecurve dla KDE
Group:		Themes
Requires:	qt-style-Bluecurve

%description -n kde-theme-Bluecurve
Bluecurve KDE theme.

%description -n kde-theme-Bluecurve -l pl
Motyw Bluecurve dla KDE.

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
%patch1 -p1 -b .niedakh


%build
%if %{without kde}
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

# locales for gdm theme
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n icons-Bluecurve
%defattr(644,root,root,755)
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

%files -n metacity-theme-Bluecurve
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

%files -n XFree86-Xcursor-packs-Bluecurve
%defattr(644,root,root,755)
%dir %{_iconsdir}/Bluecurve
%{_iconsdir}/Bluecurve/cursors
%{_iconsdir}/Bluecurve-inverse

%files -n gdm-theme-Bluecurve -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/gdm/themes/Bluecurve
