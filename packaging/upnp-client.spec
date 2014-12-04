## Basic Descriptions of this package
Name:       upnp-client
Summary:    upnp client
Version:		1.2
Release:    1
Group:      Framework/system
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Source1:    upnp-client.service

# Required packages
# Pkgconfig tool helps to find libraries that have already been installed
BuildRequires:  cmake
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(capi-network-bluetooth)
BuildRequires:  pkgconfig(capi-system-info)
BuildRequires:  pkgconfig(dlog)

## Description string that this package's human users can understand
%description
upnp client framework


## Preprocess script
%prep
# setup: to unpack the original sources / -q: quiet
# patch: to apply patches to the original sources
%setup -q

## Build script
%build
# 'cmake' does all of setting the Makefile, then 'make' builds the binary.
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make %{?jobs:-j%jobs}

## Install script
%install
# make_install: equivalent to... make install DESTDIR="%(?buildroot)"
%make_install

# install license file
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

#install lib files
mkdir -p %{buildroot}/usr/share/web
cp -f web/tizendesc.xml %{buildroot}/usr/share/web/tizendesc.xml
install --directory %{buildroot}/usr/share/web
#install -m 0644 web/tizendesc.xml %{buildroot}/usr/share/web/

# install systemd service
mkdir -p %{buildroot}%{_libdir}/systemd/system/graphical.target.wants
install -m 0644 %SOURCE1 %{buildroot}%{_libdir}/systemd/system/
ln -s ../upnp-client.service %{buildroot}%{_libdir}/systemd/system/graphical.target.wants/upnp-client.service

## Postprocess script
%post 

## Binary Package: File list
%files
%manifest upnp-client.manifest
%{_bindir}/upnp_client
%{_libdir}/systemd/system/upnp-client.service
%{_libdir}/systemd/system/graphical.target.wants/upnp-client.service
/usr/share/license/%{name}
/usr/share/web/tizendesc.xml
