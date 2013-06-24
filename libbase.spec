Summary:	JFree Base Services
Name:		libbase
Version:	1.1.6
Release:	1
License:	LGPLv2+
Group:		System/Libraries 
Url:		http://reporting.pentaho.org/
Source0:	http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Patch0:	libbase-1.1.2-fix-build.patch
BuildArch:	noarch
BuildRequires:	ant 
BuildRequires:	ant-contrib 
BuildRequires:	ant-nodeps 
BuildRequires:	java-devel 
BuildRequires:	jpackage-utils 
BuildRequires:	jakarta-commons-logging
Requires:	java 
Requires:	jpackage-utils 
Requires:	jakarta-commons-logging

%description
LibBase is a library developed to provide base services like logging,
configuration and initialization to other libraries and applications. The
library is the root library for all Pentaho-Reporting projects.


%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

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
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{name}-%{version}.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

