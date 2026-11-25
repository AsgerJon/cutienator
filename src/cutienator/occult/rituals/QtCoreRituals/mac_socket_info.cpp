//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcfsocketnotifier_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcfsocketnotifier_p.h>

//  MacSocketInfo::MacSocketInfo()
extern "C" Q_DECL_EXPORT
MacSocketInfo *ritual_ZN13MacSocketInfoC1Ev() {
  return new MacSocketInfo();
}

//  MacSocketInfo::~MacSocketInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13MacSocketInfoD1Ev(MacSocketInfo *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
