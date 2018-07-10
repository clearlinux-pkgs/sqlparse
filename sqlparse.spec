#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6DB3F0E3E0B84F81 (albrecht.andi@gmail.com)
#
Name     : sqlparse
Version  : 0.2.4
Release  : 45
URL      : http://pypi.debian.net/sqlparse/sqlparse-0.2.4.tar.gz
Source0  : http://pypi.debian.net/sqlparse/sqlparse-0.2.4.tar.gz
Source99 : http://pypi.debian.net/sqlparse/sqlparse-0.2.4.tar.gz.asc
Summary  : Non-validating SQL parser
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sqlparse-bin
Requires: sqlparse-python3
Requires: sqlparse-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
``sqlparse`` is a non-validating SQL parser module.
        It provides support for parsing, splitting and formatting SQL statements.

%package bin
Summary: bin components for the sqlparse package.
Group: Binaries

%description bin
bin components for the sqlparse package.


%package python
Summary: python components for the sqlparse package.
Group: Default
Requires: sqlparse-python3

%description python
python components for the sqlparse package.


%package python3
Summary: python3 components for the sqlparse package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sqlparse package.


%prep
%setup -q -n sqlparse-0.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523308424
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlformat

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
