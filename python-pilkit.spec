%global srcname pilkit

Name:           python-%{srcname}
Version:        3.0
Release:        2%{?dist}
Summary:        A collection of utilities and processors for the Python Imaging Libary
License:        BSD-3-Clause
URL:            https://github.com/matthewwithanm/pilkit/
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
# post GA fixes
Patch0:         pilkit-3.0-fixes.patch
BuildArch:      noarch

%global _description %{expand:
PILKit is a collection of utilities for working with PIL (the Python Imaging
Library).

One of its main features is a set of **processors** which expose a simple
interface for performing manipulations on PIL images.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# test requirements
BuildRequires:  python3-pillow
BuildRequires:  python3-pytest
BuildRequires:  python3-mock

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Tue May 20 2025 Dan Horák <dan[at]danny.cz> - 3.0-2
- add post GA fixes

* Fri Nov 03 2023 Dan Horák <dan[at]danny.cz> - 3.0-1
- updated to 3.0

* Fri Jun 30 2023 Dan Horák <dan[at]danny.cz> - 2.0-2.git09ffa2a
- rebuild

* Mon Jun 20 2022 Dan Horák <dan[at]danny.cz> - 2.0-1.git09ffa2a
- initial Fedora version
