Summary:	A backend data gatherer for cacti
Name:		cacti-cactid
Version:	0.8.6k
Release:	%mkrel 9
License:	GPL
Group:		System/Servers
URL:		http://www.cacti.net/
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

