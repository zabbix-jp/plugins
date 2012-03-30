Name:           zabbix-plugin-apache
Version:        1.0
Release:        1%{?dist}
Summary:        Apache monitoring plugin for Zabbix

Group:          Applications/Internet
Vendor:         ZABBIX-JP
License:        GPL
URL:            http://www.zabbix.jp
Source0:        apache-status
Source1:        apache_status.conf
Source2:        zabbix_apache_status.conf

Requires:       httpd
Requires:       zabbix-agent

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Apache monitoring plugin for Zabbix

%prep
%setup -q -c -T
%build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts
mkdir -p $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d
mkdir -p $RPM_BUILD_ROOT/etc/httpd/conf.d
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT/etc/httpd/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%post
%preun
%postun
%files
%defattr(-,root,root,-)
/usr/lib/zabbix/externalscripts/apache-status
/etc/zabbix/zabbix_agentd.d/apache_status.conf
/etc/httpd/conf.d/zabbix_apache_status.conf

%changelog
* Thu Mar 30 2012 Kodai Terashima <kodai74@gmail.com>
- Initial release