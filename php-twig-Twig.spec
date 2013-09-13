%define		status		stable
%define		pearname	Twig
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Twig is a PHP template engine
Name:		php-twig-Twig
Version:	1.13.2
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.twig-project.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	2832f6b1b6834f3a08e5a082e61297a9
URL:		http://pear.twig-project.org/package/Twig/
BuildRequires:	php-channel(pear.twig-project.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.twig-project.org)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twig is a template language for PHP.

Twig uses a syntax similar to the Django and Jinja template languages
which inspired the Twig runtime environment.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Twig/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Twig
