%global tl_name clock
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Graphical and textual clocks for TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/clock
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clock.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clock.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Features graphical clocks (with a classical 12h dial and two hands) and
text clocks (in 24h format) which can show system time or any time the
user desires. Works with both TeX and LaTeX. The clock faces
(appearances of the dial) are easily expandable; the default uses a
custom Metafont font.

