Name:		texlive-clock
Version:	20080419
Release:	1
Summary:	Graphical and textual clocks for TeX and LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clock
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clock.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clock.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Features graphical clocks (with a classical 12h dial and two
hands) and text clocks (in 24h format) which can show system
time or any time the user desires. Works with both TeX and
LaTeX. The clock faces (appearances of the dial) are easily
expandable; the default uses a custom MetaFont font.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/clock/clock.mf
%{_texmfdistdir}/fonts/tfm/public/clock/clock.tfm
%{_texmfdistdir}/tex/latex/clock/clock.sty
%{_texmfdistdir}/tex/latex/clock/clock.tex
%doc %{_texmfdistdir}/doc/latex/clock/COPYING
%doc %{_texmfdistdir}/doc/latex/clock/EMTEX
%doc %{_texmfdistdir}/doc/latex/clock/HISTORY
%doc %{_texmfdistdir}/doc/latex/clock/INSTALL
%doc %{_texmfdistdir}/doc/latex/clock/MIKTEX
%doc %{_texmfdistdir}/doc/latex/clock/README
%doc %{_texmfdistdir}/doc/latex/clock/clockdoc.pdf
%doc %{_texmfdistdir}/doc/latex/clock/clockdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
