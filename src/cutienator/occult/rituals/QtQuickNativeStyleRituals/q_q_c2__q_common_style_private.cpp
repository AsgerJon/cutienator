//  Written by dev_tooling.RitualGenerator from the records of QtQuickNativeS
//  tyle/6.12.0/QtQuickNativeStyle/private/qqc2qcommonstyle_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file now stands under
//  the condition Qt builds this module under (macOS and Windows
//  only, as quickcontrols/CMakeLists.txt says), as the module
//  and its global header are not there on Linux. The Cute class
//  and its 'take' ritual are taken out: Qt does not export this
//  class, so no function of it is in Qt's library to fall back on.
//  The include of QtWidgets is taken out: its 'QStyle' would be
//  ambiguous with that of QQC2. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/QtQuickNativeStyle>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qcommonstyle_p_p.h>
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCommonStyle *QQC2::QCommonStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQC2::QCommonStyle *ritual_ZN4QQC219QCommonStylePrivate6q_funcEv(
    QQC2::QCommonStylePrivate *self) {
  return self->q_func();
}

//  const QCommonStyle *QQC2::QCommonStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQC2::QCommonStyle *ritual_ZNK4QQC219QCommonStylePrivate6q_funcEv(
    const QQC2::QCommonStylePrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(quick_itemview)
//  QQC2::QCommonStylePrivate::~QCommonStylePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC219QCommonStylePrivateD1Ev(
    QQC2::QCommonStylePrivate *self) {
  delete self;
}
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
//  bool QQC2::QCommonStylePrivate::isViewItemCached(const
//      QStyleOptionViewItem &option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QQC219QCommonStylePrivate16isViewItemCachedERKNS_20QStyleOptionViewItemE(
    const QQC2::QCommonStylePrivate *self,
    const QQC2::QStyleOptionViewItem *option) {
  return self->isViewItemCached(*option);
}
#endif  // QT_CONFIG(quick_itemview)

//  void QQC2::QCommonStylePrivate::tabLayout(const QStyleOptionTab *opt,
//      QRect *textRect, QRect *pixmapRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK4QQC219QCommonStylePrivate9tabLayoutEPKNS_15QStyleOptionTabEP5QRectS5_(
    const QQC2::QCommonStylePrivate *self,
    const QQC2::QStyleOptionTab *opt,
    QRect *textRect,
    QRect *pixmapRect) {
  self->tabLayout(opt, textRect, pixmapRect);
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
