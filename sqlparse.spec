#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6DB3F0E3E0B84F81 (albrecht.andi@gmail.com)
#
Name     : sqlparse
Version  : 0.4.2
Release  : 70
URL      : https://files.pythonhosted.org/packages/32/fe/8a8575debfd924c8160295686a7ea661107fc34d831429cce212b6442edb/sqlparse-0.4.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/fe/8a8575debfd924c8160295686a7ea661107fc34d831429cce212b6442edb/sqlparse-0.4.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/32/fe/8a8575debfd924c8160295686a7ea661107fc34d831429cce212b6442edb/sqlparse-0.4.2.tar.gz.asc
Summary  : A non-validating SQL parser.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: sqlparse-bin = %{version}-%{release}
Requires: sqlparse-license = %{version}-%{release}
Requires: sqlparse-python = %{version}-%{release}
Requires: sqlparse-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest

%description
======================================
        
        |buildstatus|_
        |coverage|_
        |docs|_
        
        .. docincludebegin
        
        sqlparse is a non-validating SQL parser for Python.
        It provides support for parsing, splitting and formatting SQL statements.
        
        The module is compatible with Python 3.5+ and released under the terms of the

%package bin
Summary: bin components for the sqlparse package.
Group: Binaries
Requires: sqlparse-license = %{version}-%{release}

%description bin
bin components for the sqlparse package.


%package license
Summary: license components for the sqlparse package.
Group: Default

%description license
license components for the sqlparse package.


%package python
Summary: python components for the sqlparse package.
Group: Default
Requires: sqlparse-python3 = %{version}-%{release}

%description python
python components for the sqlparse package.


%package python3
Summary: python3 components for the sqlparse package.
Group: Default
Requires: python3-core
Provides: pypi(sqlparse)

%description python3
python3 components for the sqlparse package.


%prep
%setup -q -n sqlparse-0.4.2
cd %{_builddir}/sqlparse-0.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631306958
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest -v || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sqlparse
cp %{_builddir}/sqlparse-0.4.2/LICENSE %{buildroot}/usr/share/package-licenses/sqlparse/c4c4e71afeed48a083c414f8b157f11a3676954a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlformat

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sqlparse/c4c4e71afeed48a083c414f8b157f11a3676954a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
