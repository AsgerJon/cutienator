//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickPathAttribute::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickPathAttribute10metaObjectEv(
    const QQuickPathAttribute *self) {
  return self->metaObject();
}

//  QString QQuickPathAttribute::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickPathAttribute2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPathAttribute::tr(s, c, n));
}

//  QQuickPathAttribute::QQuickPathAttribute(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPathAttribute *ritual_ZN19QQuickPathAttributeC1EP7QObject(
    QObject *parent) {
  return new QQuickPathAttribute(parent);
}

//  QString QQuickPathAttribute::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuickPathAttribute4nameEv(
    const QQuickPathAttribute *self) {
  return new QString(self->name());
}

//  void QQuickPathAttribute::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAttribute7setNameERK7QString(
    QQuickPathAttribute *self,
    const QString *name) {
  self->setName(*name);
}

//  qreal QQuickPathAttribute::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickPathAttribute5valueEv(
    const QQuickPathAttribute *self) {
  return self->value();
}

//  void QQuickPathAttribute::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickPathAttribute8setValueEd(
    QQuickPathAttribute *self,
    qreal value) {
  self->setValue(value);
}

#endif  // QT_CONFIG(quick_path)
