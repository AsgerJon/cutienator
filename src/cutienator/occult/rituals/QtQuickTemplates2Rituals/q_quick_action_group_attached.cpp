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

//  void *QQuickActionGroupAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QQuickActionGroupAttached11qt_metacastEPKc(
    QQuickActionGroupAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickActionGroupAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QQuickActionGroupAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickActionGroupAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQuickActionGroupAttached::groupChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickActionGroupAttached12groupChangedEv(
    QQuickActionGroupAttached *self) {
  self->groupChanged();
}

//  QQuickActionGroupAttachedPrivate *QQuickActionGroupAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickActionGroupAttachedPrivate *ritual_ZN25QQuickActionGroupAttached6d_funcEv(
    QQuickActionGroupAttached *self) {
  return self->d_func();
}

//  const QQuickActionGroupAttachedPrivate
//      *QQuickActionGroupAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickActionGroupAttachedPrivate *ritual_ZNK25QQuickActionGroupAttached6d_funcEv(
    const QQuickActionGroupAttached *self) {
  return self->d_func();
}
