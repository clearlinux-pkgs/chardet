#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chardet
Version  : 3.0.4
Release  : 36
URL      : http://pypi.debian.net/chardet/chardet-3.0.4.tar.gz
Source0  : http://pypi.debian.net/chardet/chardet-3.0.4.tar.gz
Summary  : Universal encoding detector for Python 2 and 3
Group    : Development/Tools
License  : LGPL-2.1
Requires: chardet-bin
Requires: chardet-python3
Requires: chardet-license
Requires: chardet-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
--------------------------------------------------

%package bin
Summary: bin components for the chardet package.
Group: Binaries
Requires: chardet-license

%description bin
bin components for the chardet package.


%package legacypython
Summary: legacypython components for the chardet package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the chardet package.


%package license
Summary: license components for the chardet package.
Group: Default

%description license
license components for the chardet package.


%package python
Summary: python components for the chardet package.
Group: Default
Requires: chardet-python3

%description python
python components for the chardet package.


%package python3
Summary: python3 components for the chardet package.
Group: Default
Requires: python3-core

%description python3
python3 components for the chardet package.


%prep
%setup -q -n chardet-3.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530370720
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530370720
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/chardet
cp LICENSE %{buildroot}/usr/share/doc/chardet/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chardetect

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/chardet/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
