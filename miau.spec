Summary:	Small but quite featured IRC-bouncer
Summary(pl.UTF-8):	Mały, ale dobrze wyposażony ircowy bramkarz
Name:		miau
Version:	0.6.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/miau/%{name}-%{version}.tar.bz2
# Source0-md5:	6ee1b23fe55b46988d0714021b0ff76c
URL:		http://miau.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Miau is small but quite featured IRC-bouncer - a service a bit like
HTTP-proxy, but for IRC-networks.

The biggest difference of miau and HTTP-proxy (forgetting the fact
they talk all different protocols) is that when IRC-client disconnects
from bouncer, the connection to the server isn't necessarily lost.
This way your nick can stay online and cannot be taken by the others.
In case bouncer loses the nick because of netsplit or other
disruption, it can try to get it back automatically.

Some people may also like the fact that when using bouncer, your
hostname appearing in IRC is the one of the machine the bouncer is
running at, not the one you are IRCing from.

%description -l pl.UTF-8
Miau jest małym, lecz dobrze wyposażonym ircowym bramkarzem - usługą
podobną do proxy HTTP, ale do sieci IRC.

Największa różnica między proxy HTTP a miau (pomijając fakt, że to
zupełnie inne protokoły) to nietracenie połączenia do serwera po
odłączeniu się klienta od bramkarza. W ten sposób pseudonim dalej
istnieje na serwerze i nie może być zajęty przez inne osoby. W
przypadku stracenia pseudonimu przy netsplicie lub innych
zakłóceniach, miau będzie automatycznie próbował go odzyskać.

Niektórym może się również spodobać, że nazwa hosta pojawiająca się na
ircu nie jest nazwą maszyny z której się łączą, lecz nazwą maszyny na
której uruchomiony został bramkarz.

%prep
%setup -q

%build
%configure \
	--enable-dccbounce \
	--enable-automode \
	--enable-releasenick \
	--enable-ctcp-replies \
	--enable-mkpasswd \
	--enable-uptime \
	--enable-chanlog \
	--enable-privlog \
	--enable-onconnect \
	--enable-empty-awaymsg
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_docdir}/miau/examples/miaurc
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO misc/miaurc
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
%{_mandir}/man1/miau.1*
