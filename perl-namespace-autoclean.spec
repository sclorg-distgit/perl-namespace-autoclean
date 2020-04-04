%{?scl:%scl_package perl-namespace-autoclean}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_namespace_autoclean_enables_optional_test
%else
%bcond_with perl_namespace_autoclean_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-namespace-autoclean
Version:        0.29
Release:        2%{?dist}
License:        GPL+ or Artistic
Summary:        Keep imports out of your namespace
URL:            https://metacpan.org/release/namespace-autoclean
Source0:        https://cpan.metacpan.org/modules/by-module/namespace/namespace-autoclean-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  %{?scl_prefix}perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(namespace::clean) >= 0.20
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Sub::Identify)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.94
BuildRequires:  %{?scl_prefix}perl(Test::Needs)
%if %{with perl_namespace_autoclean_enables_optional_test}
# Optional Tests
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.120900
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  %{?scl_prefix}perl(Moo) >= 1.004000
%endif
%if ! %{defined perl_bootstrap}
# Break build-cycle: perl-namespace-autoclean → perl-Moose
# → perl-Package-DeprecationManager → perl-namespace-autoclean
# Break build-cycle: perl-namespace-autoclean → perl-Mouse → perl-Moose
# → perl-Package-DeprecationManager → perl-namespace-autoclean
BuildRequires:  %{?scl_prefix}perl(Moose) >= 0.56
BuildRequires:  %{?scl_prefix}perl(Moose::Role)
BuildRequires:  %{?scl_prefix}perl(MooseX::Role::WithOverloading) >= 0.09
BuildRequires:  %{?scl_prefix}perl(Mouse)
%endif
BuildRequires:  %{?scl_prefix}perl(Sub::Install)
BuildRequires:  %{?scl_prefix}perl(Sub::Name)
%endif
# Runtime
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Sub::Identify)

%description
When you import a function into a Perl package, it will naturally also be
available as a method. The 'namespace::autoclean' pragma will remove all
imported symbols at the end of the current package's compile cycle. Functions
called in the package itself will still be bound by their name, but they won't
show up as methods on your class or instances. This module is very similar to
namespace::clean, except it will clean all imported functions, no matter if you
imported them before or after you 'use'd the pragma. It will also not touch
anything that looks like a method.

%prep
%setup -q -n namespace-autoclean-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/namespace/
%{_mandir}/man3/namespace::autoclean.3*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.29-2
- SCL

* Mon Aug 26 2019 Paul Howarth <paul@city-fan.org> - 0.29-1
- Update to 0.29
  - Switch from Test::Requires to Test::Needs
  - Report on the installed versions of more optional modules

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-16
- Perl 5.30 re-rebuild of bootstrapped packages

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-15
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-12
- Perl 5.28 re-rebuild of bootstrapped packages

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-11
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-8
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-5
- Perl 5.24 re-rebuild of bootstrapped packages

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.28-4
- Perl 5.24 rebuild

* Tue Mar 29 2016 Petr Pisar <ppisar@redhat.com> - 0.28-3
- Break build-cycle: perl-namespace-autoclean → perl-Moose
 → perl-Package-DeprecationManager → perl-namespace-autoclean
- Break build-cycle: perl-namespace-autoclean → perl-Mouse → perl-Moose
 → perl-Package-DeprecationManager → perl-namespace-autoclean
- Remove unused direct test dependency on Class::MOP

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Paul Howarth <paul@city-fan.org> - 0.28-1
- Update to 0.28
  - Skip failing tests with old Moo or when Sub::Util is broken
    (CPAN RT#107643)

* Wed Sep  9 2015 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27
  - Package with only ExtUtils::MakeMaker to ease installation on perl 5.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.22 rebuild

* Sun Jun  7 2015 Paul Howarth <paul@city-fan.org> - 0.26-1
- Update to 0.26
  - Mark all Mouse tests as TODO below perl 5.010, to enable installation
    despite apparent instability issues (see CPAN RT#101825)

* Sat Jun  6 2015 Paul Howarth <paul@city-fan.org> - 0.25-1
- Update to 0.25
  - Load Moo::Role earlier in a test, to make a potential misconfiguration more
    visible

* Mon Jan  5 2015 Paul Howarth <paul@city-fan.org> - 0.24-1
- Update to 0.24
  - Be more lenient in optional Mouse tests to handle edge cases in older and
    pure perl versions
- Drop redundant %%{?perl_default_filter}

* Tue Nov  4 2014 Paul Howarth <paul@city-fan.org> - 0.22-1
- Update to 0.22
  - Drop testing of MooseX::MarkAsMethods, now that Moose 2.1400 has better
    overload handling

* Tue Sep 23 2014 Paul Howarth <paul@city-fan.org> - 0.20-1
- Update to 0.20
  - Moose earlier than 2.0300 had a broken ->does method, which called methods
    on a class's meta when it might not be initialized (CPAN RT#98424)

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.20 rebuild

* Fri Aug 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Disable BRs MooseX::MarkAsMethods and MooseX::Role::WithOverloading to
  avoid circular deps when bootstrapping

* Thu Aug 14 2014 Paul Howarth <paul@city-fan.org> - 0.19-1
- Update to 0.19
  - Bump dependency on B::Hooks::EndOfScope, to get the separation of pure-perl
    and XS components (CPAN RT#89245)
  - Repository migrated to the github moose organization
  - Update configure_requires checking in Makefile.PL, add CONTRIBUTING file
  - Changed the code to no longer _require_ Class::MOP; if your class is not a
    Moose class then we don't load Class::MOP, which was particularly
    problematic for Moo classes, as using namespace::autoclean with a Moo class
    "upgraded" it to be a Moose class
  - Using this module just broke overloading in a class (CPAN RT#50938)
  - Add -except to import options; this allows you to explicitly not clean a
    sub.
  - Better method detection for Mouse (GH#4)
  - More comprehensive testing with Moo/Mouse/Moose
  - Fixed cleaning of constants
- This release by ETHER -> update source URL
- Switch to Module::Build::Tiny flow
- Update %%description to remove reference to Class::MOP
- Make %%files list more explicit

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 0.13-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.13-2
- Perl 5.16 rebuild

* Sat Jan 14 2012 Iain Arnell <iarnell@gmail.com> 0.13-1
- update to latest upstream version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.12-3
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.12-2
- Perl mass rebuild

* Sun Mar 13 2011 Iain Arnell <iarnell@gmail.com> 0.12-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.11-2
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-3
- rebuild against perl 5.10.1

* Thu Sep 17 2009 Stepan Kasal <skasal@redhat.com> 0.09-2
- fix the previous changelog entry

* Wed Sep 16 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- add %%perl_default_filter'ing
- auto-update to 0.09 (by cpan-spec-update 0.01)
- added a new req on perl(B::Hooks::EndOfScope) (version 0.07)
- added a new req on perl(Class::MOP) (version 0.80)
- added a new req on perl(List::Util) (version 0)
- added a new req on perl(namespace::clean) (version 0.11)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-1
- submission

* Wed Jul 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.08-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)
