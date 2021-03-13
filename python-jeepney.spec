# Created by pyp2rpm-3.3.2
%global pypi_name jeepney

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        %mkrel 1
Summary:        Low-level, pure Python DBus protocol wrapper
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/jeepney
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This is a low-level, pure Python DBus protocol client. It has an I/O-free core,
and integration modules for different event loops.

%package -n     python3-%{pypi_name}
Summary:        Low-level, pure Python DBus protocol wrapper
Group:          Development/Python
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This is a low-level, pure Python DBus protocol client. It has an I/O-free core,
and integration modules for different event loops.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
