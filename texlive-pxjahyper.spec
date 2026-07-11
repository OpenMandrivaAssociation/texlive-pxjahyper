%global tl_name pxjahyper
%global tl_revision 79106

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6b
Release:	%{tl_revision}.1
Summary:	Hyperref support for pLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/pxjahyper
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjahyper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxjahyper.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package adjusts the behavior of hyperref on (u)pLaTeX so that
authors can properly create PDF documents that contain document
information in Japanese.

