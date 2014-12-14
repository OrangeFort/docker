# No debugging packages, please!
%global debug_package %{nil}

Name:           docker
Version:        1.3.3
Release:        2%{?repo}%{?dist}
Summary:        Automates deployment of containerized applications
License:        ASL 2.0
Group:          System Environment/Daemons
URL:            http://www.docker.io
BuildRoot:      %{_tmpdir}/%{name}-%{version}-%{release}
# only x86_64 for now: https://github.com/docker/docker/issues/136
# Also, RHEL7/CentOS 7 is x86_64 only, so, you know, deal with it.
ExclusiveArch:  x86_64
# No real libraries to fish versions out of, so don't bother trying
AutoReqProv:    0


Requires:         iptables, procps, systemd, xz
BuildRequires:    systemd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

Provides:  lxc-docker = %{version}
Provides:  docker

Source0:   https://get.docker.io/builds/Linux/x86_64/docker-%{version}
Source1:   docker.service
Source2:   docker.socket
Source3:   docker.sysconfig
Source5:   docker.1.gz
Source6:   docker.bash
Source7:   docker.zsh
Source8:   docker.rules
# Not even going to pretend I'm not considering just making
# this pile of man pages into a tarball and decompressing it
# during the 'install' phase.
Source10:  docker-attach.1.gz
Source11:  docker-build.1.gz
Source12:  docker-commit.1.gz
Source13:  docker-cp.1.gz
Source14:  docker-diff.1.gz
Source15:  docker-events.1.gz
Source16:  docker-export.1.gz
Source17:  docker-history.1.gz
Source18:  docker-images.1.gz
Source19:  docker-import.1.gz
Source20:  docker-info.1.gz
Source21:  docker-inspect.1.gz
Source22:  docker-kill.1.gz
Source23:  docker-load.1.gz
Source24:  docker-login.1.gz
Source25:  docker-logout.1.gz
Source26:  docker-logs.1.gz
Source27:  docker-pause.1.gz
Source28:  docker-port.1.gz
Source29:  docker-ps.1.gz
Source30:  docker-pull.1.gz
Source31:  docker-push.1.gz
Source32:  docker-restart.1.gz
Source33:  docker-rm.1.gz
Source34:  docker-rmi.1.gz
Source35:  docker-run.1.gz
Source36:  docker-save.1.gz
Source37:  docker-search.1.gz
Source38:  docker-start.1.gz
Source39:  docker-stop.1.gz
Source40:  docker-tag.1.gz
Source41:  docker-top.1.gz
Source42:  docker-unpause.1.gz
Source43:  docker-version.1.gz
Source44:  docker-wait.1.gz
Source45:  Dockerfile.5.gz
# The various and sundry Docker docs
Source60:  docker-AUTHORS
Source61:  docker-CHANGELOG.md
Source62:  docker-CONTRIBUTING.md
Source63:  docker-MAINTAINERS
Source64:  docker-NOTICE
Source65:  docker-LICENSE
Source66:  docker-README.md


%description
Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on
and between virtually any server. The same container that a developer builds
and tests on a laptop will run at scale, in production, on VMs, bare-metal
servers, OpenStack clusters, public instances, or combinations of the above.


# Break {bash,zsh}-completion scripts into seperate packages
%package -n %{name}-bash-completion
Summary:     bash completion files for Docker
BuildArch:   noarch
Requires:    bash-completion
Requires:    %{name} = %{version}-%{release}
AutoReqProv: 0

%description -n %{name}-bash-completion
This package contains the bash completion files for Docker

%package -n %{name}-zsh-completion
Summary:     zsh completion files for Docker
BuildArch:   noarch
Requires:    zsh
Requires:    %{name} = %{version}-%{release}
AutoReqProv: 0

%description -n %{name}-zsh-completion
This package contains the zsh completion files for Docker


%prep
%setup -q -c -n docker-%{version} -T
# Nothing to see here!

%build
# Nothing to see here!

%install
rm -rf $RPM_BUILD_ROOT

# install binary
install -d -m0755 $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

# install manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE18} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE19} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE20} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE21} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE23} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE24} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE25} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE26} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE27} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE28} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE29} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE30} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE31} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE32} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE33} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE34} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE35} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE36} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE37} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE38} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE39} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE40} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE41} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE42} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE43} $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 %{SOURCE44} $RPM_BUILD_ROOT%{_mandir}/man1/

install -d $RPM_BUILD_ROOT%{_mandir}/man5
install -p -m 644 %{SOURCE45} $RPM_BUILD_ROOT%{_mandir}/man5/

# install bash completion
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/docker.bash

# install zsh completion
install -d $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions
install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/zsh/site-functions/_%{name}

# install udev rules
install -d $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
install -p -m 755 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/80-%{name}.rules

# install storage dir
install -d -m 700 $RPM_BUILD_ROOT%{_sharedstatedir}/docker

# install systemd/init scripts
install -d $RPM_BUILD_ROOT/%{_unitdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_unitdir}/%{name}.service
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_unitdir}/%{name}.socket

# Use sysconfig for additional args
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/docker

# Make some documentation
install -p -m 644 %{SOURCE60} AUTHORS
install -p -m 644 %{SOURCE61} CHANGELOG.md
install -p -m 644 %{SOURCE62} CONTRIBUTING.md
install -p -m 644 %{SOURCE63} MAINTAINERS
install -p -m 644 %{SOURCE64} NOTICE
install -p -m 644 %{SOURCE65} LICENSE
install -p -m 644 %{SOURCE66} README.md

%clean
rm -rf $RPM_BUILD_ROOT


%pre
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG.md CONTRIBUTING.md LICENSE MAINTAINERS NOTICE README.md
%dir %{_sharedstatedir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_sysconfdir}/sysconfig/%{name}
%{_sysconfdir}/udev/rules.d/80-%{name}.rules
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket

%files -n %{name}-bash-completion
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/%{name}.bash

%files -n %{name}-zsh-completion
%defattr(-,root,root)
%{_datadir}/zsh/site-functions/_%{name}


%changelog
* Sat Dec 13 2014 Ryan McKern <ryan@orangefort.com> - 1.3.3-2orangefort.el7
- Restore missing manpage

* Sat Dec 13 2014 Ryan McKern <ryan@orangefort.com> - 1.3.3-1orangefort.el7
- Bump release to 1.3.3-1
- Update 'CHANGELOG' for 1.3.3 release

* Mon Nov 24 2014 Ryan McKern <ryan@orangefort.com> - 1.3.2-1orangefort.el7
- Bump release to 1.3.2-1
- Update 'CHANGELOG' for 1.3.2 release

* Sun Nov  2 2014 Ryan McKern <ryan@orangefort.com> - 1.3.1-2orangefort.el7
- Bump release to 1.3.1-2
- Update 'CHANGELOG' for 1.3.1 release

* Sun Nov  2 2014 Ryan McKern <ryan@orangefort.com> - 1.3.1-1orangefort.el7
- Bump version to 1.3.1
- Add BuildRequires for SystemD to ensure that RPM macros are populated

* Thu Oct 16 2014 Ryan McKern <ryan@orangefort.com> - 1.3.0-1orangefort.el7
- Bump version to 1.3.0

* Sun Sep 14 2014 Ryan McKern <ryan@orangefort.com> - 1.2.0-3orangefort.el7
- Fix errant provides
- Replace buildroot macro with RPM_BUILD_ROOT variable

* Sun Sep 14 2014 Ryan McKern <ryan@orangefort.com> - 1.2.0-2orangefort.el7
- Split bash & zsh completion into seperate packages

* Sun Sep 14 2014 Ryan McKern <ryan@orangefort.com> - 1.2.0-1orangefort.el7
- Initial packaging of Docker binary and a million man pages
