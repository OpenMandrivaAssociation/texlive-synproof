Name:		texlive-synproof
Version:	15878
Release:	2
Summary:	Easy drawing of syntactic proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/synproof
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synproof.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synproof.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of macros based on PSTricks that
will enable you to draw syntactic proofs easily (inspired by
the Gamut books). Very few commands are needed, however fine
tuning of the various parameters (dimensions) can still be
achieved through "key=value" pairs.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/synproof/synproof.sty
%doc %{_texmfdistdir}/doc/latex/synproof/README
%doc %{_texmfdistdir}/doc/latex/synproof/synproof-doc.pdf
%doc %{_texmfdistdir}/doc/latex/synproof/synproof-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
