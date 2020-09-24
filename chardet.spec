#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : chardet
Version  : 3.0.4
Release  : 46
URL      : http://pypi.debian.net/chardet/chardet-3.0.4.tar.gz
Source0  : http://pypi.debian.net/chardet/chardet-3.0.4.tar.gz
Summary  : Universal encoding detector for Python 2 and 3
Group    : Development/Tools
License  : LGPL-2.1
Requires: chardet-license = %{version}-%{release}
Requires: chardet-python = %{version}-%{release}
Requires: chardet-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

.. image:: https://img.shields.io/travis/chardet/chardet/stable.svg
   :alt: Build status
   :target: https://travis-ci.org/chardet/chardet

.. image:: https://img.shields.io/coveralls/chardet/chardet/stable.svg
   :target: https://coveralls.io/r/chardet/chardet

.. image:: https://img.shields.io/pypi/v/chardet.svg
   :target: https://warehouse.python.org/project/chardet/
   :alt: Latest version on PyPI

.. image:: https://img.shields.io/pypi/l/chardet.svg
   :alt: License


Detects
 - ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
 - Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
 - EUC-JP, SHIFT_JIS, CP932, ISO-2022-JP (Japanese)
 - EUC-KR, ISO-2022-KR (Korean)
 - KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
 - ISO-8859-5, windows-1251 (Bulgarian)
 - ISO-8859-1, windows-1252 (Western European languages)
 - ISO-8859-7, windows-1253 (Greek)
 - ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
 - TIS-620 (Thai)

.. note::
   Our ISO-8859-2 and windows-1250 (Hungarian) probers have been temporarily
   disabled until we can retrain the models.

Requires Python 2.6, 2.7, or 3.3+.

Installation
------------

Install from `PyPI <https://pypi.python.org/pypi/chardet>`_::

    pip install chardet

Documentation
-------------

For users, docs are now available at https://chardet.readthedocs.io/.

Command-line Tool
-----------------

chardet comes with a command-line script which reports on the encodings of one
or more files::

    % chardetect somefile someotherfile
    somefile: windows-1252 with confidence 0.5
    someotherfile: ascii with confidence 1.0

About
-----

This is a continuation of Mark Pilgrim's excellent chardet. Previously, two
versions needed to be maintained: one that supported python 2.x and one that
supported python 3.x.  We've recently merged with `Ian Cordasco <https://github.com/sigmavirus24>`_'s
`charade <https://github.com/sigmavirus24/charade>`_ fork, so now we have one
coherent version that works for Python 2.6+.

:maintainer: Dan Blanchard

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
%setup -q -n chardet-3.0.4
cd %{_builddir}/chardet-3.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582906824
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/chardet
cp %{_builddir}/chardet-3.0.4/LICENSE %{buildroot}/usr/share/package-licenses/chardet/545f380fb332eb41236596500913ff8d582e3ead
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/chardetect

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
