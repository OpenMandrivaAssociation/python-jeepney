# Created by pyp2rpm-3.3.2
%global pypi_name jeepney

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        2
Summary:        Low-level, pure Python DBus protocol wrapper
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/jeepney
Source0:        https://files.pythonhosted.org/packages/bb/4f/06017fbbe94eeaf1e7852c2dd7a065ca7d813e17b4500f4e842531d72593/jeepney-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
This is a low-level, pure Python DBus protocol client. It has an I/O-free core,
and integration modules for different event loops.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
