//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickactiongroup_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickactiongroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickActionGroupAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickActionGroupAttached10metaObjectEv(
    const QQuickActionGroupAttached *self) {
  return self->metaObject();
}

//  QString QQuickActionGroupAttached::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickActionGroupAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickActionGroupAttached::tr(s, c, n));
}

//  QQuickActionGroupAttached::QQuickActionGroupAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickActionGroupAttached *ritual_ZN25QQuickActionGroupAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickActionGroupAttached(parent);
}

//  QQuickActionGroup *QQuickActionGroupAttached::group() const
extern "C" Q_DECL_EXPORT
QQuickActionGroup *ritual_ZNK25QQuickActionGroupAttached5groupEv(
    const QQuickActionGroupAttached *self) {
  return self->group();
}

//  void QQuickActionGroupAttached::setGroup(QQuickActionGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickActionGroupAttached8setGroupEP17QQuickActionGroup(
    QQuickActionGroupAttached *self,
    QQuickActionGroup *group) {
  self->setGroup(group);
}
