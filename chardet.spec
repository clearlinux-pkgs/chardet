#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chardet
Version  : 3.0.4
Release  : 41
URL      : http://pypi.debian.net/chardet/chardet-3.0.4.tar.gz
Source0  : http://pypi.debian.net/chardet/chardet-3.0.4.tar.gz
Summary  : Universal encoding detector for Python 2 and 3
Group    : Development/Tools
License  : LGPL-2.1
Requires: chardet-bin = %{version}-%{release}
Requires: chardet-license = %{version}-%{release}
Requires: chardet-python = %{version}-%{release}
Requires: chardet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

%package bin
Summary: bin components for the chardet package.
Group: Binaries
Requires: chardet-license = %{version}-%{release}

%description bin
bin components for the chardet package.


%package license
Summary: license components for the chardet package.
Group: Default

%description license
license components for the chardet package.


%package python
Summary: python components for the chardet package.
Group: Default
Requires: chardet-python3 = %{version}-%{release}

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
export SOURCE_DATE_EPOCH=1554311077
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/chardet
cp LICENSE %{buildroot}/usr/share/package-licenses/chardet/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/chardetect

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/chardet/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
