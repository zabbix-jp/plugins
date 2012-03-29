Name:           zabbix-notification-patlite
Version:        1.0
Release:        1%{?dist}
Summary:        Patlite notication plugin for Zabbix

Group:          Applications/Internet
Vendor:         ZABBIX-JP
License:        GPL
URL:            http://www.zabbix.jp
Source0:        patlite

Requires:       rsh
Requires:       zabbix-server

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Patlite notication plugin for Zabbix

%prep
%setup -q -c -T
%build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix/alertscripts/
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/zabbix/alertscripts/

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%post
%preun
%postun
%files
%defattr(-,root,root,-)
/usr/lib/zabbix/alertscripts/patlite

%changelog
* Thu Mar 29 2012 Kodai Terashima <kodai74@gmail.com>
- Initial release