//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h>

//  WinTimerInfo::~WinTimerInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12WinTimerInfoD1Ev(WinTimerInfo *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
