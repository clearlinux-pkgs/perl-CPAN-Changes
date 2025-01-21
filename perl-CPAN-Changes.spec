#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v10
# autospec commit: 5905be9
#
Name     : perl-CPAN-Changes
Version  : 0.500004
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/CPAN-Changes-0.500004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/CPAN-Changes-0.500004.tar.gz
Summary  : 'Parser for CPAN style change logs'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-CPAN-Changes-bin = %{version}-%{release}
Requires: perl-CPAN-Changes-license = %{version}-%{release}
Requires: perl-CPAN-Changes-man = %{version}-%{release}
Requires: perl-CPAN-Changes-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Types::Standard)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
CPAN::Changes - Parser for CPAN style change logs
SYNOPSIS
use CPAN::Changes;
my $changes = CPAN::Changes->load('Changes');
$changes->release('0.01');

%package bin
Summary: bin components for the perl-CPAN-Changes package.
Group: Binaries
Requires: perl-CPAN-Changes-license = %{version}-%{release}

%description bin
bin components for the perl-CPAN-Changes package.


%package dev
Summary: dev components for the perl-CPAN-Changes package.
Group: Development
Requires: perl-CPAN-Changes-bin = %{version}-%{release}
Provides: perl-CPAN-Changes-devel = %{version}-%{release}
Requires: perl-CPAN-Changes = %{version}-%{release}

%description dev
dev components for the perl-CPAN-Changes package.


%package license
Summary: license components for the perl-CPAN-Changes package.
Group: Default

%description license
license components for the perl-CPAN-Changes package.


%package man
Summary: man components for the perl-CPAN-Changes package.
Group: Default

%description man
man components for the perl-CPAN-Changes package.


%package perl
Summary: perl components for the perl-CPAN-Changes package.
Group: Default
Requires: perl-CPAN-Changes = %{version}-%{release}

%description perl
perl components for the perl-CPAN-Changes package.


%prep
%setup -q -n CPAN-Changes-0.500004
cd %{_builddir}/CPAN-Changes-0.500004
pushd ..
cp -a CPAN-Changes-0.500004 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CPAN-Changes
cp %{_builddir}/CPAN-Changes-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-CPAN-Changes/4fd50c6ffe3c2145eee93f9e0551cf97fd0dce92 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tidy_changelog

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CPAN::Changes.3
/usr/share/man/man3/CPAN::Changes::Entry.3
/usr/share/man/man3/CPAN::Changes::Group.3
/usr/share/man/man3/CPAN::Changes::Parser.3
/usr/share/man/man3/CPAN::Changes::Release.3
/usr/share/man/man3/CPAN::Changes::Spec.3
/usr/share/man/man3/Test::CPAN::Changes.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CPAN-Changes/4fd50c6ffe3c2145eee93f9e0551cf97fd0dce92

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tidy_changelog.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
