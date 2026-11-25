//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontdatabase_p.h>

//  FontAndStyle::~FontAndStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN12FontAndStyleD1Ev(FontAndStyle *self) {
  delete self;
}

//  bool operator==(const FontAndStyle &lhs, const FontAndStyle &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12FontAndStyleS1_(
    const FontAndStyle *lhs,
    const FontAndStyle *rhs) {
  return *lhs == *rhs;
}

//  bool operator!=(const FontAndStyle &lhs, const FontAndStyle &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12FontAndStyleS1_(
    const FontAndStyle *lhs,
    const FontAndStyle *rhs) {
  return *lhs != *rhs;
}

#endif  // defined(Q_OS_WIN)
