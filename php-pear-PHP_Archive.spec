%define		_class		PHP
%define		_subclass	Archive
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.11.4
Release:	8
Summary:	Create and use PHP Archive files
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/PHP_Archive/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
PHP_Archive allows you to create a single .phar file containing an
entire application. 

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-6mdv2012.0
+ Revision: 742230
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-5
+ Revision: 679561
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11.4-4mdv2011.0
+ Revision: 613754
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.11.4-3mdv2010.1
+ Revision: 467950
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.11.4-2mdv2010.0
+ Revision: 441507
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.11.4-1mdv2009.1
+ Revision: 368330
- Update php pear PHP_Archive to 0.11.4 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-3mdv2009.1
+ Revision: 322647
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-2mdv2009.0
+ Revision: 237048
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.11.1-1mdv2008.0
+ Revision: 32715
- 0.11.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-1mdv2008.0
+ Revision: 15738
- 0.10.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdv2007.0
+ Revision: 82513
- Import php-pear-PHP_Archive

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdk
- 0.7.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-1mdk
- initial Mandriva package (PLD import)

