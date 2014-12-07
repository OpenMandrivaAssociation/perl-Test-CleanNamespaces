%define upstream_name Test-CleanNamespaces
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Check for uncleaned imports
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Find::Rule::Perl)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch

%description
Check for uncleaned imports.

%prep
%setup -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml MYMETA.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Aug 31 2014 sander85 <sander85> 0.160.0-1.mga5
+ Revision: 669872
- update to 0.16

* Sat Aug 16 2014 sander85 <sander85> 0.150.0-1.mga5
+ Revision: 664178
- update to 0.15

* Fri Aug 15 2014 sander85 <sander85> 0.140.0-1.mga5
+ Revision: 662769
- imported package perl-Test-CleanNamespaces

