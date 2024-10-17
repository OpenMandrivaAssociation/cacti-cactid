Summary:	A backend data gatherer for cacti
Name:		cacti-cactid
Version:	0.8.6k
Release:	15
License:	GPL
Group:		System/Servers
URL:		https://www.cacti.net/
Source0:	http://www.cacti.net/downloads/cactid/%{name}-%{version}.tar.gz
Patch0:		cacti-cactid-0.8.6k-format_not_a_string_literal_and_no_format_arguments.diff
Requires:	cacti
BuildRequires:	mysql-devel
BuildRequires:	net-snmp-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This code represents the future replacement for cmd.php. As you
can see from the short changelog, development on this code has
only just begun. It has been included in the main release for
*testing* purposes only! Please stick to cmd.php for now.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%serverbuild
# x86_64 fix
export LDFLAGS="-L%{_libdir}"
%configure2_5x
%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_sbindir}

install -m0644 cactid.conf %{buildroot}%{_sysconfdir}/
install -m0755 cactid %{buildroot}%{_sbindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL README LICENSE*
%config(noreplace) %{_sysconfdir}/cactid.conf
%attr(0755,root,root) %{_sbindir}/cactid



%changelog
* Mon Jul 18 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-14mdv2011
+ Revision: 690285
- rebuilt against new net-snmp libs

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-13
+ Revision: 645777
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-12mdv2011.0
+ Revision: 627214
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-11mdv2011.0
+ Revision: 626508
- rebuilt against mysql-5.5.8 libs

* Thu Dec 30 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6k-10mdv2011.0
+ Revision: 626417
- rebuild for latest mysql

* Tue Oct 12 2010 Funda Wang <fwang@mandriva.org> 0.8.6k-9mdv2011.0
+ Revision: 585059
- rebuild for new netsnmp

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-8mdv2010.1
+ Revision: 507519
- rebuild

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-7mdv2010.0
+ Revision: 457700
- fix build
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Dec 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.6k-4mdv2009.1
+ Revision: 312189
- rebuilt against mysql-5.1.30 libs

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.8.6k-3mdv2009.0
+ Revision: 243413
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.8.6k-1mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.6i-1mdv2008.0
+ Revision: 60198
- 0.8.6i


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6f-4mdv2007.0
- Rebuild

* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.6f-3mdk
- rebuilt against new net-snmp with new major (10)

* Wed Dec 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6f-2mdk
- rebuilt against net-snmp that has new major (9)

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6f-1mdk
- 0.8.6f-1

* Tue Jul 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6e-1mdk 
- new release
- used %%mkrel
- spec cleanup
- drop version requirement on cacti dependency

* Tue May 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.6d-1mdk
- 0.8.6d
- use better anti ^M stripper
- drop P0, it's implemented upstream
- fix build on x86_64

* Mon Feb 28 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8.6c-3mdk
- fix #13965
- strip away annoying ^M

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8.6c-2mdk
- rebuilt against MySQL-4.1.x system libs

* Mon Dec 20 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8.6c-1mdk
- 0.8.6c
- fix url

* Fri Oct 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8.6b-1mdk
- initial mandrake package

