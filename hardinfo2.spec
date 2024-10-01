#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : hardinfo2
Version  : 2.1.17
Release  : 3
URL      : https://github.com/hardinfo2/hardinfo2/archive/release-2.1.17/hardinfo2-2.1.17.tar.gz
Source0  : https://github.com/hardinfo2/hardinfo2/archive/release-2.1.17/hardinfo2-2.1.17.tar.gz
Summary  : System Information and Benchmark for Linux Systems
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0-or-later LGPL-2.0-or-later LGPL-2.1+ LGPL-2.1-only
Requires: hardinfo2-bin = %{version}-%{release}
Requires: hardinfo2-data = %{version}-%{release}
Requires: hardinfo2-lib = %{version}-%{release}
Requires: hardinfo2-locales = %{version}-%{release}
Requires: hardinfo2-man = %{version}-%{release}
Requires: hardinfo2-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-png)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-export-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(x11)
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Hardinfo2 is based on hardinfo, which have not been released >10 years.
Hardinfo2 is the reboot that was needed.

Hardinfo2 offers System Information and Benchmark for Linux Systems. It is able
to obtain information from both hardware and basic software. It can benchmark
your system and compare to other machines online.

Features include:
- Report generation (in either HTML or plain text)
- Online Benchmarking - compare your machine against other machines

%package bin
Summary: bin components for the hardinfo2 package.
Group: Binaries
Requires: hardinfo2-data = %{version}-%{release}
Requires: hardinfo2-services = %{version}-%{release}

%description bin
bin components for the hardinfo2 package.


%package data
Summary: data components for the hardinfo2 package.
Group: Data

%description data
data components for the hardinfo2 package.


%package lib
Summary: lib components for the hardinfo2 package.
Group: Libraries
Requires: hardinfo2-data = %{version}-%{release}

%description lib
lib components for the hardinfo2 package.


%package locales
Summary: locales components for the hardinfo2 package.
Group: Default

%description locales
locales components for the hardinfo2 package.


%package man
Summary: man components for the hardinfo2 package.
Group: Default

%description man
man components for the hardinfo2 package.


%package services
Summary: services components for the hardinfo2 package.
Group: Systemd services
Requires: systemd

%description services
services components for the hardinfo2 package.


%prep
%setup -q -n hardinfo2-release-2.1.17
cd %{_builddir}/hardinfo2-release-2.1.17

%build
## build_prepend content
sed -i 's|/etc/os-release|/usr/lib/os-release|g' CMakeLists.txt
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727792278
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DCMAKE_BUILD_TYPE=Release  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1727792278
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang hardinfo2

%files
%defattr(-,root,root,-)
/usr/lib64/hardinfo2/modules/qgears2

%files bin
%defattr(-,root,root,-)
/usr/bin/hardinfo2

%files data
%defattr(-,root,root,-)
/usr/share/applications/hardinfo2.desktop
/usr/share/hardinfo2/arm.ids
/usr/share/hardinfo2/benchmark.data
/usr/share/hardinfo2/benchmark.json
/usr/share/hardinfo2/blobs-update-version.json
/usr/share/hardinfo2/edid.ids
/usr/share/hardinfo2/ieee_oui.ids
/usr/share/hardinfo2/kernel-module-icons.json
/usr/share/hardinfo2/pci.ids
/usr/share/hardinfo2/pixmaps/about-modules.png
/usr/share/hardinfo2/pixmaps/audio.png
/usr/share/hardinfo2/pixmaps/battery.png
/usr/share/hardinfo2/pixmaps/benchmark.png
/usr/share/hardinfo2/pixmaps/bg1_dark.jpg
/usr/share/hardinfo2/pixmaps/bg1_light.jpg
/usr/share/hardinfo2/pixmaps/bg2_dark.jpg
/usr/share/hardinfo2/pixmaps/bg2_light.jpg
/usr/share/hardinfo2/pixmaps/bg3_dark.jpg
/usr/share/hardinfo2/pixmaps/bg3_light.jpg
/usr/share/hardinfo2/pixmaps/bg4_dark.jpg
/usr/share/hardinfo2/pixmaps/bg4_light.jpg
/usr/share/hardinfo2/pixmaps/bg5_dark.jpg
/usr/share/hardinfo2/pixmaps/bg5_light.jpg
/usr/share/hardinfo2/pixmaps/bg6_dark.jpg
/usr/share/hardinfo2/pixmaps/bg6_light.jpg
/usr/share/hardinfo2/pixmaps/blowfish.png
/usr/share/hardinfo2/pixmaps/bluetooth.png
/usr/share/hardinfo2/pixmaps/bolt.png
/usr/share/hardinfo2/pixmaps/boot.png
/usr/share/hardinfo2/pixmaps/camera-photo.png
/usr/share/hardinfo2/pixmaps/camera-web.png
/usr/share/hardinfo2/pixmaps/cdrom.png
/usr/share/hardinfo2/pixmaps/circle_green_check.svg
/usr/share/hardinfo2/pixmaps/circle_red_x.svg
/usr/share/hardinfo2/pixmaps/circle_yellow_exclaim.svg
/usr/share/hardinfo2/pixmaps/clipboard.png
/usr/share/hardinfo2/pixmaps/close.png
/usr/share/hardinfo2/pixmaps/compress.png
/usr/share/hardinfo2/pixmaps/computer.png
/usr/share/hardinfo2/pixmaps/cryptohash.png
/usr/share/hardinfo2/pixmaps/dev_removable.png
/usr/share/hardinfo2/pixmaps/devel.png
/usr/share/hardinfo2/pixmaps/devices.png
/usr/share/hardinfo2/pixmaps/dialog-error.png
/usr/share/hardinfo2/pixmaps/dialog-information.png
/usr/share/hardinfo2/pixmaps/dialog-warning.png
/usr/share/hardinfo2/pixmaps/distros/almalinux.svg
/usr/share/hardinfo2/pixmaps/distros/arch.svg
/usr/share/hardinfo2/pixmaps/distros/armbian.svg
/usr/share/hardinfo2/pixmaps/distros/bodhi.svg
/usr/share/hardinfo2/pixmaps/distros/centos.svg
/usr/share/hardinfo2/pixmaps/distros/clear-linux-os.svg
/usr/share/hardinfo2/pixmaps/distros/debian.svg
/usr/share/hardinfo2/pixmaps/distros/devuan.svg
/usr/share/hardinfo2/pixmaps/distros/edubuntu.svg
/usr/share/hardinfo2/pixmaps/distros/endeavouros.svg
/usr/share/hardinfo2/pixmaps/distros/fedora.svg
/usr/share/hardinfo2/pixmaps/distros/garuda.svg
/usr/share/hardinfo2/pixmaps/distros/gentoo.svg
/usr/share/hardinfo2/pixmaps/distros/kali.svg
/usr/share/hardinfo2/pixmaps/distros/kubuntu.svg
/usr/share/hardinfo2/pixmaps/distros/linuxmint.svg
/usr/share/hardinfo2/pixmaps/distros/lubuntu.svg
/usr/share/hardinfo2/pixmaps/distros/mageia.svg
/usr/share/hardinfo2/pixmaps/distros/manjaro.svg
/usr/share/hardinfo2/pixmaps/distros/mxlinux.svg
/usr/share/hardinfo2/pixmaps/distros/nixos.svg
/usr/share/hardinfo2/pixmaps/distros/nobara.svg
/usr/share/hardinfo2/pixmaps/distros/ol.svg
/usr/share/hardinfo2/pixmaps/distros/opensuse-tumbleweed.svg
/usr/share/hardinfo2/pixmaps/distros/opensuse.svg
/usr/share/hardinfo2/pixmaps/distros/pclinuxos.svg
/usr/share/hardinfo2/pixmaps/distros/pop.svg
/usr/share/hardinfo2/pixmaps/distros/puppy.svg
/usr/share/hardinfo2/pixmaps/distros/pureos.svg
/usr/share/hardinfo2/pixmaps/distros/raspberry-pi.svg
/usr/share/hardinfo2/pixmaps/distros/raspbian.svg
/usr/share/hardinfo2/pixmaps/distros/rebornos.svg
/usr/share/hardinfo2/pixmaps/distros/rhel.svg
/usr/share/hardinfo2/pixmaps/distros/rocky.svg
/usr/share/hardinfo2/pixmaps/distros/slackware.svg
/usr/share/hardinfo2/pixmaps/distros/slint.svg
/usr/share/hardinfo2/pixmaps/distros/sysrescue.svg
/usr/share/hardinfo2/pixmaps/distros/ubuntu-budgie.svg
/usr/share/hardinfo2/pixmaps/distros/ubuntu-gnome.svg
/usr/share/hardinfo2/pixmaps/distros/ubuntu-kylin.svg
/usr/share/hardinfo2/pixmaps/distros/ubuntu-mate.svg
/usr/share/hardinfo2/pixmaps/distros/ubuntu-studio.svg
/usr/share/hardinfo2/pixmaps/distros/ubuntu.svg
/usr/share/hardinfo2/pixmaps/distros/ultramarine.svg
/usr/share/hardinfo2/pixmaps/distros/void.svg
/usr/share/hardinfo2/pixmaps/distros/xubuntu.svg
/usr/share/hardinfo2/pixmaps/dns.png
/usr/share/hardinfo2/pixmaps/environment.png
/usr/share/hardinfo2/pixmaps/face-grin.png
/usr/share/hardinfo2/pixmaps/fan.png
/usr/share/hardinfo2/pixmaps/fft.png
/usr/share/hardinfo2/pixmaps/file-roller.png
/usr/share/hardinfo2/pixmaps/hardinfo.png
/usr/share/hardinfo2/pixmaps/hardinfo2.png
/usr/share/hardinfo2/pixmaps/hardinfo2.svg
/usr/share/hardinfo2/pixmaps/hdd.png
/usr/share/hardinfo2/pixmaps/home.png
/usr/share/hardinfo2/pixmaps/inputdevices.png
/usr/share/hardinfo2/pixmaps/internet.png
/usr/share/hardinfo2/pixmaps/joystick.png
/usr/share/hardinfo2/pixmaps/keyboard.png
/usr/share/hardinfo2/pixmaps/language.png
/usr/share/hardinfo2/pixmaps/logo.xcf
/usr/share/hardinfo2/pixmaps/media-floppy.png
/usr/share/hardinfo2/pixmaps/media-removable.png
/usr/share/hardinfo2/pixmaps/memory.png
/usr/share/hardinfo2/pixmaps/modem.png
/usr/share/hardinfo2/pixmaps/module.png
/usr/share/hardinfo2/pixmaps/monitor.png
/usr/share/hardinfo2/pixmaps/mouse.png
/usr/share/hardinfo2/pixmaps/nautilus.png
/usr/share/hardinfo2/pixmaps/network-connections.png
/usr/share/hardinfo2/pixmaps/network-interface.png
/usr/share/hardinfo2/pixmaps/network-statistics.png
/usr/share/hardinfo2/pixmaps/network.png
/usr/share/hardinfo2/pixmaps/nqueens.png
/usr/share/hardinfo2/pixmaps/os.png
/usr/share/hardinfo2/pixmaps/pcmcia.png
/usr/share/hardinfo2/pixmaps/printer.png
/usr/share/hardinfo2/pixmaps/processor.png
/usr/share/hardinfo2/pixmaps/raytrace.png
/usr/share/hardinfo2/pixmaps/refresh.png
/usr/share/hardinfo2/pixmaps/report-large.png
/usr/share/hardinfo2/pixmaps/report.png
/usr/share/hardinfo2/pixmaps/resources.png
/usr/share/hardinfo2/pixmaps/security.png
/usr/share/hardinfo2/pixmaps/server-large.png
/usr/share/hardinfo2/pixmaps/server.png
/usr/share/hardinfo2/pixmaps/server_sync.png
/usr/share/hardinfo2/pixmaps/shares.png
/usr/share/hardinfo2/pixmaps/summary.png
/usr/share/hardinfo2/pixmaps/syncmanager-small.png
/usr/share/hardinfo2/pixmaps/syncmanager.png
/usr/share/hardinfo2/pixmaps/therm.png
/usr/share/hardinfo2/pixmaps/usb.png
/usr/share/hardinfo2/pixmaps/usbfldisk.png
/usr/share/hardinfo2/pixmaps/users.png
/usr/share/hardinfo2/pixmaps/wireless.png
/usr/share/hardinfo2/sdcard.ids
/usr/share/hardinfo2/usb.ids
/usr/share/hardinfo2/vendor.ids
/usr/share/icons/hicolor/scalable/apps/hardinfo2.svg
/usr/share/metainfo/org.hardinfo2.hardinfo2.metainfo.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/hardinfo2/modules/benchmark.so
/usr/lib64/hardinfo2/modules/computer.so
/usr/lib64/hardinfo2/modules/devices.so
/usr/lib64/hardinfo2/modules/network.so

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hardinfo2.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/hardinfo2.service

%files locales -f hardinfo2.lang
%defattr(-,root,root,-)

