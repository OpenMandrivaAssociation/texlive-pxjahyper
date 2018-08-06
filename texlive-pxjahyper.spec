Name:		texlive-pxjahyper
Version:	0.3d
Release:	1
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
%{_texmfdistdir}/tex/platex/pxjahyper
%doc %{_texmfdistdir}/doc/platex/pxjahyper

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
