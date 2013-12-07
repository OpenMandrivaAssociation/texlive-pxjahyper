# revision 28503
# category Package
# catalog-ctan /language/japanese/pxjahyper
# catalog-date 2012-12-11 14:08:29 +0100
# catalog-license noinfo
# catalog-version 0.3
Name:		texlive-pxjahyper
Version:	0.3
Release:	3
Summary:	Hyperref support for pLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/pxjahyper
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjahyper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjahyper.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pxjahyper package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/platex/pxjahyper/pxjahyper.sty
%doc %{_texmfdistdir}/doc/platex/pxjahyper/LICENSE
%doc %{_texmfdistdir}/doc/platex/pxjahyper/README
%doc %{_texmfdistdir}/doc/platex/pxjahyper/pxjahyper.pdf
%doc %{_texmfdistdir}/doc/platex/pxjahyper/pxjahyper.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
