%define module jeepney

Name:		python-jeepney
Version:	0.9.0
Release:	1
Summary:	Low-level, pure Python DBus protocol wrapper
Group:  	Development/Python
License:	MIT
URL:		https://pypi.org/project/jeepney
Source0:	https://files.pythonhosted.org/packages/source/j/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(flit-core)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{module} is a pure Python implementation of D-Bus messaging.
It has an I/O-free core and integration modules for different event loops.
D-Bus is an inter-process communication system, mainly used in Linux.

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
