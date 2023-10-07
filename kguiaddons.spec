%define major 5
%define libname %mklibname KF5GuiAddons %{major}
%define devname %mklibname KF5GuiAddons -d
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Name: kguiaddons
Version:	5.110.0
Release:	2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 GUI Library addons
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5WaylandClient)
BuildRequires: qt5-qtwayland
BuildRequires: pkgconfig(wayland-client)
BuildRequires: cmake(PlasmaWaylandProtocols) >= 1.7.0
Obsoletes: python-%{name} < %{EVRD}
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 GUI Library addons.

%package -n %{libname}
Summary: The KDE Frameworks 5 GUI Library addons
Group: System/Libraries
# It's recommended to use the KF6 geo scheme handler even for KF5,
# even before KF6 is released.
# https://community.kde.org/Plasma/Plasma_6#Packaging_notes
Requires: kde-geo-scheme-handler
Obsoletes: %{name} < %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 GUI Library addons.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5 \
	-DBUILD_GEO_SCHEME_HANDLER:BOOL=OFF

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}
%{_datadir}/qlogging-categories5/kguiaddons.categories

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5GuiAddons
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
