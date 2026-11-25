//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h>

//  QSockFd::QSockFd(long ev, long ma)
extern "C" Q_DECL_EXPORT
QSockFd *ritual_ZN7QSockFdC1Ell(long ev, long ma) {
  return new QSockFd(ev, ma);
}

//  QSockFd::~QSockFd()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSockFdD1Ev(QSockFd *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
