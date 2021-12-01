%define		kdeplasmaver	5.23.4
%define		qtver		5.9.0
%define		kpname		breeze-plymouth

Summary:	breeze-plymouth
Name:		kp5-%{kpname}
Version:	5.23.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	71c20d264f3e55a6b44d7bb999cb2392
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.8.0
BuildRequires:	ninja
BuildRequires:	plymouth-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
breeze-plymouth.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/plymouth/breeze-text.so
%{_datadir}/plymouth/themes/breeze-text
%{_datadir}/plymouth/themes/breeze
