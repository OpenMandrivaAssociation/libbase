%{?_javapackages_macros:%_javapackages_macros}
%if 0%{?fedora}
%else
Epoch: 1
%endif
Name: libbase
Version: 1.1.3
Release: 10.0%{?dist}
Summary: JFree Base Services
License: LGPLv2

#Original source: http://downloads.sourceforge.net/jfreereport/%%{name}-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: https://reporting.pentaho.org/
BuildRequires: ant, ant-contrib, java-devel, jpackage-utils, apache-commons-logging
Requires: java, jpackage-utils, apache-commons-logging
BuildArch: noarch

Patch0: libbase-1.1.2.build.patch

%description
LibBase is a library developed to provide base services like logging,
configuration and initialization to other libraries and applications. The
library is the root library for all Pentaho-Reporting projects.

%package javadoc
Summary: Javadoc for %{name}

%if 0%{?fedora}
Requires: %{name} = %{version}-%{release}
%else
Requires: %{name} = %{EVRD}
%endif
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
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
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Aug 06 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.1.3-10
- Fix bogus date in %%changelog
- ant-nodeps is dropped from ant-1.9.0-2 build in rawhide
- Drop buildroot, %%clean, %%defattr and removal of buildroot in %%install

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 03 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.3-7
- repack source to remove bundled multi-license .jars

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.3-5
- Resolves: rhbz#818487 adapt to jakarta->apache

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> - 1.1.3-3
- Related: rhbz#749103 drop gcj aot

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 03 2009 Caolan McNamara <caolanm@redhat.com> 1.1.3-1
- latest version

* Tue Nov 17 2009 Caolan McNamara <caolanm@redhat.com> 1.1.2-1
- latest version

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-3.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-2.OOo31
- Post released tuned for OpenOffice.org reportbuilder

* Wed Dec 03 2008 Caolan McNamara <caolanm@redhat.com> 1.0.0-1
- initial fedora import
