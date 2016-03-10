#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sqlparse
Version  : 0.1.19
Release  : 17
URL      : https://pypi.python.org/packages/source/s/sqlparse/sqlparse-0.1.19.tar.gz
Source0  : https://pypi.python.org/packages/source/s/sqlparse/sqlparse-0.1.19.tar.gz
Summary  : Non-validating SQL parser
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sqlparse-bin
Requires: sqlparse-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
python-sqlparse - Parse SQL statements
======================================
sqlparse is a non-validating SQL parser module for Python.

%package bin
Summary: bin components for the sqlparse package.
Group: Binaries

%description bin
bin components for the sqlparse package.


%package python
Summary: python components for the sqlparse package.
Group: Default

%description python
python components for the sqlparse package.


%prep
%setup -q -n sqlparse-0.1.19

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlformat

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
