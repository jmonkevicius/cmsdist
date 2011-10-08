### RPM external p5-extutils-makemaker 6.58
## INITENV +PATH PERL5LIB %i/lib/perl5
%define name_mm ExtUtils-MakeMaker
%define name_inst ExtUtils-Install
%define ver_inst 1.54
Source0: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/%{name_mm}-%{realversion}.tar.gz
Source1: http://search.cpan.org/CPAN/authors/id/Y/YV/YVES/%{name_inst}-%{ver_inst}.tar.gz

%prep
%setup -T -b 0 -n %{name_mm}-%{realversion}
%setup -D -T -b 1 -n %{name_inst}-%{ver_inst}

%build
for pkg in %{name_mm}-%{realversion} %{name_inst}-%{ver_inst}; do
  cd ../$pkg
  LC_ALL=C; export LC_ALL
  perl Makefile.PL INSTALL_BASE=%i
  make
done

%install
for pkg in %{name_mm}-%{realversion} %{name_inst}-%{ver_inst}; do
  cd ../$pkg
  make install
done

%define drop_files %i/man
