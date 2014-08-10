%define		pearname	Twig
%define		php_min_version 5.2.4
%include	/usr/lib/rpm/macros.php
Summary:	The flexible, fast, and secure template engine for PHP
Name:		php-twig-%{pearname}
Version:	1.16.0
Release:	1
License:	BSD Style
Group:		Development/Languages/PHP
Source0:	http://pear.twig-project.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	1da4723f6919fb76d51ad986fc4a0c66
URL:		http://twig.sensiolabs.org/
BuildRequires:	php-channel(pear.twig-project.org)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(dom)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.twig-project.org)
Requires:	php-pear
Suggests:	php(xdebug)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twig is a template language for PHP.

Twig uses a syntax similar to the Django and Jinja template languages
which inspired the Twig runtime environment.

- Fast: Twig compiles templates down to plain optimized PHP code. The
  overhead compared to regular PHP code was reduced to the very minimum.
- Secure: Twig has a sandbox mode to evaluate untrusted template code.
  This allows Twig to be used as a template language for applications
  where users may modify the template design.
- Flexible: Twig is powered by a flexible lexer and parser. This
  allows the developer to define its own custom tags and filters, and
  create its own DSL.

%prep
%pear_package_setup

mv docs/Twig/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc README.rst CHANGELOG LICENSE
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Twig
