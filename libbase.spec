Name:           libbase
Version:        1.1.6
Release:        %mkrel 2
Summary:        JFree Base Services
License:        LGPLv2+
Group:          System/Libraries 
Source:         http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
URL:            http://reporting.pentaho.org/
BuildRequires:  ant, ant-contrib, ant-nodeps, java-devel, jpackage-utils, jakarta-commons-logging
Requires:       java, jpackage-utils, jakarta-commons-logging
BuildArch:      noarch
Patch0:         libbase-1.1.2-fix-build.patch

%description
LibBase is a library developed to provide base services like logging,
configuration and initialization to other libraries and applications. The
library is the root library for all Pentaho-Reporting projects.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
mkdir -p lib
find . -name "*.jar" -exec rm -f {} \;
build-jar-repository -s -p lib commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib 

%build
ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 1.1.6-2.mga3
+ Revision: 356850
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Oct 14 2012 ennael <ennael> 1.1.6-1.mga3
+ Revision: 305435
- Documentation group

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198929
- new version 1.1.6
- rediff and rename patch to fix-build
- drop the gcj support
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-3.mga1
+ Revision: 74305
- Really build without gcj

* Fri Mar 18 2011 ennael <ennael> 1.1.3-2.mga1
+ Revision: 74279
- build without gcj

* Mon Jan 24 2011 dmorgan <dmorgan> 1.1.3-1.mga1
+ Revision: 35916
- Add back ant-contrib as buildrequire
- Fix buildrequires
- Fix macros
- Adapt for mageia
- imported package libbase

