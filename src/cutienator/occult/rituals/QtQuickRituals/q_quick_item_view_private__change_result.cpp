//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQuickItemViewPrivate::ChangeResult::ChangeResult()
extern "C" Q_DECL_EXPORT
QQuickItemViewPrivate::ChangeResult *ritual_ZN21QQuickItemViewPrivate12ChangeResultC1Ev() {
  return new QQuickItemViewPrivate::ChangeResult();
}

//  QQuickItemViewPrivate::ChangeResult::ChangeResult(const
//      QQmlNullableValue<qreal> &p)
extern "C" Q_DECL_EXPORT
QQuickItemViewPrivate::ChangeResult *ritual_ZN21QQuickItemViewPrivate12ChangeResultC1ERK17QQmlNullableValueIdE(
    const QQmlNullableValue<qreal> *p) {
  return new QQuickItemViewPrivate::ChangeResult(*p);
}

//  ChangeResult &QQuickItemViewPrivate::ChangeResult::operator+=(const
//      ChangeResult &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate12ChangeResultpLERKS0_(
    QQuickItemViewPrivate::ChangeResult *self,
    const QQuickItemViewPrivate::ChangeResult *other) {
  self->operator+=(*other);
}

//  void QQuickItemViewPrivate::ChangeResult::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate12ChangeResult5resetEv(
    QQuickItemViewPrivate::ChangeResult *self) {
  self->reset();
}

//  QQuickItemViewPrivate::ChangeResult::~ChangeResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickItemViewPrivate12ChangeResultD1Ev(
    QQuickItemViewPrivate::ChangeResult *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_itemview)
