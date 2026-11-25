//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h, Qt 6.12.0, as
//  the Qt of macOS and of Windows install it. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)
#include <QtCore/6.12.0/QtCore/private/qtimezoneprivate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qtimezone.h>

//  QTzTransitionRule::~QTzTransitionRule()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTzTransitionRuleD1Ev(QTzTransitionRule *self) {
  delete self;
}

//  bool operator==(const QTzTransitionRule &lhs, const QTzTransitionRule
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK17QTzTransitionRuleS1_(
    const QTzTransitionRule *lhs,
    const QTzTransitionRule *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QTzTransitionRule &lhs, const QTzTransitionRule
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK17QTzTransitionRuleS1_(
    const QTzTransitionRule *lhs,
    const QTzTransitionRule *rhs) {
  return operator!=(*lhs, *rhs);
}

#endif  // QT_CONFIG(timezone) && !QT_CONFIG(timezone_tzdb) && !defined(Q_OS_DARWIN) && !defined(Q_OS_ANDROID) && defined(Q_OS_UNIX) && !defined(Q_OS_VXWORKS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)
