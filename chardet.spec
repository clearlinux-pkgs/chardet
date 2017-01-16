#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chardet
Version  : 2.3.0
Release  : 13
URL      : https://pypi.python.org/packages/source/c/chardet/chardet-2.3.0.tar.gz
Source0  : https://pypi.python.org/packages/source/c/chardet/chardet-2.3.0.tar.gz
Summary  : Universal encoding detector for Python 2 and 3
Group    : Development/Tools
License  : LGPL-2.1
Requires: chardet-bin
Requires: chardet-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

%package bin
Summary: bin components for the chardet package.
Group: Binaries

%description bin
bin components for the chardet package.


%package python
Summary: python components for the chardet package.
Group: Default

%description python
python components for the chardet package.


%prep
%setup -q -n chardet-2.3.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484538881
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484538881
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chardetect

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
