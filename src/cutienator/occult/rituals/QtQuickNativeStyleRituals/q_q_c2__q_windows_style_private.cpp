//  Edited by hand on 2026-11-25 from the file the generator wrote from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsstyle_p_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. The generator's
//  include of 'qtquicknativestyleexports.h' stood outside the '#if',
//  and Qt's Linux kit lacks it: it is gone, as are the includes of
//  QtWidgets, which the class does not use. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsstyle_p_p.h>
#include <QtGui/qwindow.h>

//  QWindowsStyle *QQC2::QWindowsStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQC2::QWindowsStyle *ritual_ZN4QQC220QWindowsStylePrivate6q_funcEv(
    QQC2::QWindowsStylePrivate *self) {
  return self->q_func();
}

//  const QWindowsStyle *QQC2::QWindowsStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QWindowsStyle *ritual_ZNK4QQC220QWindowsStylePrivate6q_funcEv(
    const QQC2::QWindowsStylePrivate *self) {
  return self->q_func();
}

//  qreal QQC2::QWindowsStylePrivate::devicePixelRatio(const QStyleOption
//      *option)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN4QQC220QWindowsStylePrivate16devicePixelRatioEPKNS_12QStyleOptionE(
    const QQC2::QStyleOption *option) {
  return QQC2::QWindowsStylePrivate::devicePixelRatio(option);
}

//  qreal QQC2::QWindowsStylePrivate::devicePixelRatio(const QWindow *win)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN4QQC220QWindowsStylePrivate16devicePixelRatioEPK7QWindow(
    const QWindow *win) {
  return QQC2::QWindowsStylePrivate::devicePixelRatio(win);
}

#endif  // defined(Q_OS_WIN)
