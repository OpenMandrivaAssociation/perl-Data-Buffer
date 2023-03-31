%define modname	Data-Buffer
%define modver	0.04

Summary:	Read/write buffer class
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	20
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

