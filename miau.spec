Summary:	Small but quite featured IRC-bouncer
Summary(pl):	Ma�y, ale dobrze wyposa�ony ircowy bramkarz
Name:		miau
Version:	0.5.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/miau/%{name}-%{version}.tar.bz2
# Source0-md5:	4f4f74e3e271d51d184c21871b09600f
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

%description -l pl
Miau jest ma�ym, lecz dobrze wyposa�onym ircowym bramkarzem - us�ug�
podobn� do proxy HTTP, ale do sieci IRC.

Najwi�ksza r�nica mi�dzy proxy HTTP a miau (pomijaj�c fakt, �e to
zupe�nie inne protoko�y) to nietracenie po��czenia do serwera po
od��czeniu si� klienta od bramkarza. W ten spos�b pseudonim dalej
istnieje na serwerze i nie mo�e by� zaj�ty przez inne osoby. W
przypadku stracenia pseudonimu przy netsplicie lub innych
zak��ceniach, miau b�dzie automatycznie pr�bowa� go odzyska�.

Niekt�rym mo�e si� r�wnie� spodoba�, �e nazwa hosta pojawiaj�ca si� na
ircu nie jest nazw� maszyny z kt�rej si� ��cz�, lecz nazw� maszyny na
kt�rej uruchomiony zosta� bramkarz.

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
%{_mandir}/man1/miau.1.gz
