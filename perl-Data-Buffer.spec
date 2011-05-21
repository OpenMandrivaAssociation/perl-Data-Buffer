%define upstream_name    Data-Buffer
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    Read/write buffer class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://www.cpan.org
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
