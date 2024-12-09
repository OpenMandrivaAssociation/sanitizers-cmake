%define debug_package %nil
%define date 20170421
Summary:        CMake module to enable sanitizers for binary targets
Name:           sanitizers-cmake
Version:        20241103
Release:        1
License:        MIT
Url:            https://github.com/arsenm/sanitizers-cmake
# git clone https://github.com/arsenm/sanitizers-cmake.git
# git archive --format=tar --prefix sanitizers-cmake-$(date +%Y%m%d)/ HEAD | xz -vf > sanitizers-cmake-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{date}.tar.xz
BuildRequires:	cmake

%description
CMake module to enable sanitizers for binary targets.

%prep
%setup -qn %{name}-%{date}

%build

%install
install -d %{buildroot}/%{_libdir}/cmake/%{name}
cp cmake/*.cmake %{buildroot}/%{_libdir}/cmake/%{name}/

%files
%{_libdir}/cmake/%{name}
