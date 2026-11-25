//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only its constructor,
//  which its header writes out, is called. Not written: the other
//  constructor and the destructor.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h>
#include <QtCore/qstring.h>

//  QWindowsFontDatabase::FontHandle::FontHandle(const QString &name)
extern "C" Q_DECL_EXPORT
QWindowsFontDatabase::FontHandle *ritual_ZN20QWindowsFontDatabase10FontHandleC1ERK7QString(
    const QString *name) {
  return new QWindowsFontDatabase::FontHandle(*name);
}

#endif  // defined(Q_OS_WIN)
