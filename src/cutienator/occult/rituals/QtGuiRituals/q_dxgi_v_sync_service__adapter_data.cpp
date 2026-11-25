//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qdxgivsyncservice_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only what its header
//  writes out is called.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qdxgivsyncservice_p.h>

//  QDxgiVSyncService::AdapterData::~AdapterData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService11AdapterDataD1Ev(
    QDxgiVSyncService::AdapterData *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
