//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickPathPercent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickPathPercent10metaObjectEv(
    const QQuickPathPercent *self) {
  return self->metaObject();
}

//  QString QQuickPathPercent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickPathPercent2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathPercent::tr(s, c, n));
}

//  QQuickPathPercent::QQuickPathPercent(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathPercent *ritual_ZN17QQuickPathPercentC1EP7QObject(
    QObject *parent) {
  return new QQuickPathPercent(parent);
}

//  qreal QQuickPathPercent::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickPathPercent5valueEv(const QQuickPathPercent *self) {
  return self->value();
}

//  void QQuickPathPercent::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickPathPercent8setValueEd(
    QQuickPathPercent *self,
    qreal value) {
  self->setValue(value);
}

#endif  // QT_CONFIG(quick_path)
#endif  // QT_CONFIG(quick_path)
