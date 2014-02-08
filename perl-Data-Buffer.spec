%define upstream_name    Data-Buffer
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9

Summary:	Read/write buffer class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Data::Buffer implements a low-level binary buffer in which
you can get and put integers, strings, and other data.
Internally the implementation is based on pack and unpack,
such that Data::Buffer is really a layer on top of those
built-in functions.

All of the get_* and put_* methods respect the internal
offset state in the buffer object. This means that you
should read data out of the buffer in the same order that
you put it in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-7mdv2012.0
+ Revision: 765142
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-6
+ Revision: 763656
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-5
+ Revision: 676628
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-4
+ Revision: 676577
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-3
+ Revision: 676524
- rebuild

* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2
+ Revision: 653400
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 406968
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.04-7mdv2009.0
+ Revision: 256407
- rebuild
- fix no-buildroot-tag

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.04-5mdv2008.1
+ Revision: 151443
- rebuild for perl-5.10.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill (multiple!) definitions of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-4mdv2008.0
+ Revision: 86324
- rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:09:49 (58456)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 15:07:25 (58449)
Import perl-Data-Buffer

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-2mdk
- rebuild for new perl

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.04-1mdk
- New package

