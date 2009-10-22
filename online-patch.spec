### RPM cms online-patch CMSSW_3_3_0_onlpatch2_ONLINE
## IMPORT configurations 
Provides: /bin/zsh
Provides: /bin/ksh
Provides: /bin/sed
Provides: /usr/bin/awk
Provides: /usr/bin/python
Provides: perl(Date::Format)
Provides: perl(Term::ReadKey)
Provides: perl(full)
Provides: perl(LWP::UserAgent)
Provides: perl(Template)
Requires: online-patch-tool-conf

%define cmssw_release   %(perl -e '$_="%v"; s/_ONLINE//; print;')
%define buildsetfile    online_build_set
%define cvsrep          cvs://:pserver:anonymous@cmscvs.cern.ch:2401/cvs_server/repositories/%cvsdir?passwd=AA_:yZZ3e

%define cvsprojuc       %(echo %n | sed -e "s|-...patch.*||"| tr 'a-z' 'A-Z')
%define cvsprojlc       %(echo %cvsprojuc | tr 'A-Z' 'a-z')
%define cvsdir          %cvsprojuc
%define cvssrc          %cvsprojuc
%define cvsserver       cmssw
%define useCmsTC        1

%define ucprojname      %cvsprojuc

%define prebuildtarget  gindices
%define buildtarget     release-build
%define saveDeps        yes

%define isPatch         yes
%define patchsrc2       perl -p -i -e ' s!(<classpath.*/test\\+.*>)!!' config/BuildFile.xml

## IMPORT cms-scram-build
## IMPORT partial-build
## IMPORT partial-build-patch
## IMPORT scramv1-build
