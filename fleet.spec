Summary:	A distributed init system
Name:		fleet
Version:	0.9.0
Release:	0.1
License:	Apache v2.0
Group:		Base
Source0:	https://github.com/coreos/fleet/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7535590f5513d0da0048a0ba5da616ba
URL:		https://github.com/coreos/fleet/
BuildRequires:	golang >= 1.2.1-3
BuildRequires:	systemd-devel
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fleet ties together systemd and etcd into a distributed init system.

Think of it as an extension of systemd that operates at the cluster
level instead of the machine level. This project is very low level and
is designed as a foundation for higher order orchestration.

%prep
%setup -q

%build
sh -x build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name}}
install -p bin/fleetctl $RPM_BUILD_ROOT%{_bindir}
install -p bin/fleetd $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/ examples/ CONTRIBUTING.md DCO LICENSE MAINTAINERS NOTICE README.md
%dir %attr(750,root,root) %{_sysconfdir}/%{name}
%attr(750,root,root) %{_sysconfdir}/%{name}/%{name}.conf
%attr(755,root,root) %{_bindir}/fleetctl
%attr(755,root,root) %{_bindir}/fleetd
