//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h>

//  QWindowsFontDatabase::UniqueFontData::~UniqueFontData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsFontDatabase14UniqueFontDataD1Ev(
    QWindowsFontDatabase::UniqueFontData *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
