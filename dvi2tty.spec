Summary:	DVI to ascii converter
Summary(pl):	Konwerter DVI do ascii
Name:		dvi2tty
Version:	5.3
Release:	2
License:	non-commercial
Group:		Applications/Text
Source0:	http://www.mesa.nl/pub/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dvi2tty convert TeX dvi output to ascii.

%description -l pl
Dvi2tty konweruje pliki wynikowe TeX dvi do ascii.

%prep
%setup  -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dvi2tty disdvi $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
