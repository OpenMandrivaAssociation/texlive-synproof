# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/synproof
# catalog-date 2009-07-05 17:22:22 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-synproof
Version:	1.0
Release:	7
Summary:	Easy drawing of syntactic proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/synproof
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synproof.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/synproof.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 756420
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719626
- texlive-synproof
- texlive-synproof
- texlive-synproof
- texlive-synproof

