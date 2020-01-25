# TODO:
# - package cli tool
%define		pkgname	jsonlint
%define		php_min_version 5.0.0
Summary:	JSON Lint for PHP
Name:		php-seld-%{pkgname}
Version:	1.5.0
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/Seldaek/jsonlint/archive/%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	9c59f10b97fe4564df8ac91ab2c7ef32
URL:		https://github.com/Seldaek/jsonlint
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON Lint for PHP.

This library is a port of the JavaScript jsonlint library.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Seld
cp -a src/Seld/JsonLint $RPM_BUILD_ROOT%{php_data_dir}/Seld

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.mdown CHANGELOG.mdown LICENSE
%dir %{php_data_dir}/Seld
%dir %{php_data_dir}/Seld/JsonLint
%{php_data_dir}/Seld/JsonLint/*.php
