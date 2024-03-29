#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chardet
Version  : 4.0.0
Release  : 62
URL      : https://files.pythonhosted.org/packages/ee/2d/9cdc2b527e127b4c9db64b86647d567985940ac3698eeabc7ffaccb4ea61/chardet-4.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ee/2d/9cdc2b527e127b4c9db64b86647d567985940ac3698eeabc7ffaccb4ea61/chardet-4.0.0.tar.gz
Summary  : Universal encoding detector for Python 2 and 3
Group    : Development/Tools
License  : LGPL-2.1
Requires: chardet-license = %{version}-%{release}
Requires: chardet-python = %{version}-%{release}
Requires: chardet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
--------------------------------------------------

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
Provides: pypi(chardet)

%description python3
python3 components for the chardet package.


%prep
%setup -q -n chardet-4.0.0
cd %{_builddir}/chardet-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635710494
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/chardet
cp %{_builddir}/chardet-4.0.0/LICENSE %{buildroot}/usr/share/package-licenses/chardet/545f380fb332eb41236596500913ff8d582e3ead
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/bin/chardetect

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/chardet/545f380fb332eb41236596500913ff8d582e3ead

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
