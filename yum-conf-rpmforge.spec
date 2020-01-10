Name:           yum-conf-rpmforge       
Version:        6
Release:        1
Summary:        RPMforge release file and RPM repository configuration
Group:          System Environment/Base 
License:        GPL 
URL:            http://rpmforge.net/
Requires:       rpmforge-release

%description
This package pulls in rpmforge-release which contains the
apt, yum and smart configuration for the RPMforge RPM Repository, 
as well as the public GPG keys used to sign them.


%files


%changelog
* Thu Jan 13 2011 Troy Dawson <dawson@fnal.gov> - 6-1
- The rpm only pulls in the appropriate release package

