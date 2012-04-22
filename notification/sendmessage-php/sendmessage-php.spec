Name:           zabbix-notification-sendmessage-php
Version:        1.0
Release:        1%{?dist}
Summary:        E-mail notication plugin using ISO-2022-JP encoding for Zabbix

Group:          Applications/Internet
Vendor:         ZABBIX-JP
License:        GPL
URL:            http://www.zabbix.jp
Source0:        sendmessage-php
Source1:        sendmessage-php.conf

Requires:       php-cli
Requires:       php-mbstring
Requires:       zabbix-server

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
E-mail notification plugin using ISO-2022-JP encoding for Zabbix

%prep
%setup -q -c -T
%build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix/alertscripts/
mkdir -p $RPM_BUILD_ROOT/etc/zabbix/plugins
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/zabbix/alertscripts
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/zabbix/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%post
%preun
%postun
%files
%defattr(-,root,root,-)
/usr/lib/zabbix/alertscripts/sendmessage-php
%config(noreplace) %{_sysconfdir}/zabbix/plugins/sendmessage-php.conf

%changelog
* Sun Apr 22 2012 Kodai Terashima <kodai74@gmail.com>
- Initial release
