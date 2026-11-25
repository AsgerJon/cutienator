//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Kept as it is when
//  the generator runs again. Qt's library offers nothing of this
//  class by name: only what its header writes out.
//  Not written: 'handle', 'toRECT' and 'isValid', which Qt's
//  library offers not, and 'size', 'margins', 'themeSize' and
//  'themeMargins', which call them and the uxtheme library of
//  Windows.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p_p.h>
#include <QtCore/qrect.h>

//  QQC2::XPThemeData::XPThemeData(const QWindow *w, QPainter *p, int
//      themeIn, int part, int state, const QRect &r)
extern "C" Q_DECL_EXPORT
QQC2::XPThemeData *ritual_ZN4QQC211XPThemeDataC1EPK7QWindowP8QPainteriiiRK5QRect(
    const QWindow *w,
    QPainter *p,
    int themeIn,
    int part,
    int state,
    const QRect *r) {
  return new QQC2::XPThemeData(w, p, themeIn, part, state, *r);
}

//  QQC2::XPThemeData::~XPThemeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC211XPThemeDataD1Ev(QQC2::XPThemeData *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)
