//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyle_p_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25:
//  the whole file stands under macOS and Windows, the systems Qt
//  builds QuickNativeStyle for, and the header is included by its
//  own path, with no module header of QtQuickNativeStyle before it.
//  The include of <QtWidgets/qstyle.h> is gone: it declares the
//  'QStyle' of QtWidgets, which is not the 'QQC2::QStyle' this class
//  holds, and only the one in 'QQC2' is meant here.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyle_p_p.h>

//  QStyle *QQC2::QStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQC2::QStyle *ritual_ZN4QQC213QStylePrivate6q_funcEv(
    QQC2::QStylePrivate *self) {
  return self->q_func();
}

//  const QStyle *QQC2::QStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QStyle *ritual_ZNK4QQC213QStylePrivate6q_funcEv(
    const QQC2::QStylePrivate *self) {
  return self->q_func();
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
