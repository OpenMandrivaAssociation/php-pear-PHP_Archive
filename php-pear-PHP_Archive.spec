%define		_class		PHP
%define		_subclass	Archive
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(phar

Name:		php-pear-%{upstream_name}
Version:	0.11.4
Release:	%mkrel 3
Summary:	Create and use PHP Archive files
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PHP_Archive/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
PHP_Archive allows you to create a single .phar file containing an
entire application. 

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


