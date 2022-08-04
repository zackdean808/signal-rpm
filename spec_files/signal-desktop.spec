Name:           signal-desktop 
Version:        2.0 
Release:        1%{?dist}
Summary:        Signal is an encrypted messaging applicaton

License:        MIT
URL:            https://www.signal-desktop.com
Source0: 	data.tar.xz       
Source1:	control.tar.gz  

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Thu Aug 04 2022 z <zack.dean@gmail.com>
- 
