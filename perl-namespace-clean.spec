#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-namespace-clean
Version  : 0.27
Release  : 19
URL      : http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/namespace-clean-0.27.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/namespace-clean-0.27.tar.gz
Summary  : 'Keep imports and functions out of your namespace'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-namespace-clean-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)

%description
No detailed description available

%package dev
Summary: dev components for the perl-namespace-clean package.
Group: Development
Provides: perl-namespace-clean-devel = %{version}-%{release}
Requires: perl-namespace-clean = %{version}-%{release}

%description dev
dev components for the perl-namespace-clean package.


%package perl
Summary: perl components for the perl-namespace-clean package.
Group: Default
Requires: perl-namespace-clean = %{version}-%{release}

%description perl
perl components for the perl-namespace-clean package.


%prep
%setup -q -n namespace-clean-0.27
cd %{_builddir}/namespace-clean-0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/namespace::clean.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/namespace/clean.pm
/usr/lib/perl5/vendor_perl/5.34.0/namespace/clean/_Util.pm
