//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbuttongroup_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbuttongroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickButtonGroupAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickButtonGroupAttached10metaObjectEv(
    const QQuickButtonGroupAttached *self) {
  return self->metaObject();
}

//  QString QQuickButtonGroupAttached::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickButtonGroupAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickButtonGroupAttached::tr(s, c, n));
}

//  QQuickButtonGroupAttached::QQuickButtonGroupAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickButtonGroupAttached *ritual_ZN25QQuickButtonGroupAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickButtonGroupAttached(parent);
}

//  QQuickButtonGroup *QQuickButtonGroupAttached::group() const
extern "C" Q_DECL_EXPORT
QQuickButtonGroup *ritual_ZNK25QQuickButtonGroupAttached5groupEv(
    const QQuickButtonGroupAttached *self) {
  return self->group();
}

//  void QQuickButtonGroupAttached::setGroup(QQuickButtonGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickButtonGroupAttached8setGroupEP17QQuickButtonGroup(
    QQuickButtonGroupAttached *self,
    QQuickButtonGroup *group) {
  self->setGroup(group);
}
