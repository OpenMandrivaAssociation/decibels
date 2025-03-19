%global rdnn_name org.gnome.Decibels

Name:           decibels
Version:        48.0
Release:        1
Summary:        Audio player for the GNOME desktop
Group:          Audio
License:        GPL-2.0-or-later and GPL-3.0-only
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/%{name}/48/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  appstream-util
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
#BuildRequires:  (npm(typescript) >= 5.7.3 with npm(typescript) < 5.8)
Requires:       hicolor-icon-theme
# Lacking typelib dependency generator, so use package names instead
Requires:       gtk4
Requires:       libadwaita-common
Requires:       gstreamer1.0-plugins-bad
Requires:       gstreamer1.0-plugins-ugly
Requires:       gstreamer1.0-plugins-good
# Bundled gi-typescript-defs
Provides:       bundled(gi-typescript-definitions)
BuildArch:      noarch

%description
%{summary}.
%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{rdnn_name}

%files -f %{rdnn_name}.lang
%license LICENSE
%doc README*
%{_bindir}/%{rdnn_name}
%{_datadir}/%{rdnn_name}/
%{_datadir}/applications/%{rdnn_name}.desktop
%{_datadir}/icons/hicolor/*/*/%{rdnn_name}*
%{_datadir}/dbus-1/services/%{rdnn_name}.service
%{_metainfodir}/%{rdnn_name}.metainfo.xml
