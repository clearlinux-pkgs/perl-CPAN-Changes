#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CPAN-Changes
Version  : 0.400002
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/CPAN-Changes-0.400002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/CPAN-Changes-0.400002.tar.gz
Summary  : 'Read and write Changes files'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-CPAN-Changes-bin = %{version}-%{release}
Requires: perl-CPAN-Changes-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
CPAN::Changes - Read and write Changes files
SYNOPSIS
# Load from file
my $changes = CPAN::Changes->load( 'Changes' );

%package bin
Summary: bin components for the perl-CPAN-Changes package.
Group: Binaries
Requires: perl-CPAN-Changes-man = %{version}-%{release}

%description bin
bin components for the perl-CPAN-Changes package.


%package dev
Summary: dev components for the perl-CPAN-Changes package.
Group: Development
Requires: perl-CPAN-Changes-bin = %{version}-%{release}
Provides: perl-CPAN-Changes-devel = %{version}-%{release}

%description dev
dev components for the perl-CPAN-Changes package.


%package man
Summary: man components for the perl-CPAN-Changes package.
Group: Default

%description man
man components for the perl-CPAN-Changes package.


%prep
%setup -q -n CPAN-Changes-0.400002

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1CPAN/Changes.pm
/usr/lib/perl5/vendor_perl/5.28.1CPAN/Changes/Group.pm
/usr/lib/perl5/vendor_perl/5.28.1CPAN/Changes/Release.pm
/usr/lib/perl5/vendor_perl/5.28.1CPAN/Changes/Spec.pod
/usr/lib/perl5/vendor_perl/5.28.1Test/CPAN/Changes.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/tidy_changelog

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CPAN::Changes.3
/usr/share/man/man3/CPAN::Changes::Group.3
/usr/share/man/man3/CPAN::Changes::Release.3
/usr/share/man/man3/CPAN::Changes::Spec.3
/usr/share/man/man3/Test::CPAN::Changes.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tidy_changelog.1
