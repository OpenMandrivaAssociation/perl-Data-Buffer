Name:           perl-Data-Buffer
Version:        0.04
Release:        %mkrel 5
License:        GPL or Artistic

%define realname        Data-Buffer
Group:          Development/Perl
Summary:        Read/write buffer class
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/%{realname}-%{version}.tar.bz2
Url:            http://www.cpan.org
Requires:       perl
BuildArch:      noarch

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
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*

