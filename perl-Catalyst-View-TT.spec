#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	View-TT
Summary:	Catalyst::View::TT - Template View Class
Summary(pl.UTF-8):	Catalyst::View::TT - klasa widoku szablonu
Name:		perl-Catalyst-View-TT
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-View-TT-%{version}.tar.gz
# Source0-md5:	653f58f818a1b0b3d0ad28b62c13241b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.50
BuildRequires:	perl-Template-Toolkit
BuildRequires:	perl-Template-Timer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the view class for Catalyst web framework that uses Template
Toolkit (TT) for output rendering.

%description -l pl.UTF-8
To jest klasa widoku dla szkieletu WWW Catalyst używająca do
renderowania wyjścia pakietu Template Toolkit (TT).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/View/*.pm
%{perl_vendorlib}/Catalyst/Helper/View/*.pm
%{_mandir}/man3/*
