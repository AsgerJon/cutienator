//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Kept as it is when
//  the generator runs again. Qt's library offers nothing of this
//  class by name: only what its header writes out.
//  Not written: the 'qHash' friend.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p_p.h>

//  QQC2::ThemeMapKey::ThemeMapKey()
extern "C" Q_DECL_EXPORT
QQC2::ThemeMapKey *ritual_ZN4QQC211ThemeMapKeyC1Ev() {
  return new QQC2::ThemeMapKey();
}

//  QQC2::ThemeMapKey::ThemeMapKey(const QQC2::XPThemeData &data)
extern "C" Q_DECL_EXPORT
QQC2::ThemeMapKey *ritual_ZN4QQC211ThemeMapKeyC1ERKNS_11XPThemeDataE(
    const QQC2::XPThemeData *data) {
  return new QQC2::ThemeMapKey(*data);
}

//  QQC2::ThemeMapKey::~ThemeMapKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC211ThemeMapKeyD1Ev(QQC2::ThemeMapKey *self) {
  delete self;
}

//  bool QQC2::operator==(const QQC2::ThemeMapKey &k1, const
//      QQC2::ThemeMapKey &k2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QQC2eqERKNS_11ThemeMapKeyES2_(
    const QQC2::ThemeMapKey *k1,
    const QQC2::ThemeMapKey *k2) {
  return QQC2::operator==(*k1, *k2);
}

#endif  // defined(Q_OS_WIN)
