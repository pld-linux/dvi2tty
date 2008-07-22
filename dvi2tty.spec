Summary:	DVI to ASCII converter
Summary(pl.UTF-8):	Konwerter DVI do ASCII
Name:		dvi2tty
Version:	5.3.1
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.mesa.nl/pub/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	315689466848529c2c7e94e11370a7df
Patch0:		%{name}-ansi-c.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dvi2tty converts TeX DVI output to ASCII.

%description -l pl.UTF-8
Dvi2tty konwertuje pliki wynikowe TeX DVI do ASCII.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
