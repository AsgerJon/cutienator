//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickTumblerAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickTumblerAttached10metaObjectEv(
    const QQuickTumblerAttached *self) {
  return self->metaObject();
}

//  void *QQuickTumblerAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickTumblerAttached11qt_metacastEPKc(
    QQuickTumblerAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTumblerAttached::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickTumblerAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTumblerAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTumblerAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickTumblerAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTumblerAttached::tr(s, c, n));
}

//  QQuickTumblerAttached::QQuickTumblerAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTumblerAttached *ritual_ZN21QQuickTumblerAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickTumblerAttached(parent);
}

//  QQuickTumbler *QQuickTumblerAttached::tumbler() const
extern "C" Q_DECL_EXPORT
QQuickTumbler *ritual_ZNK21QQuickTumblerAttached7tumblerEv(
    const QQuickTumblerAttached *self) {
  return self->tumbler();
}

//  qreal QQuickTumblerAttached::displacement() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTumblerAttached12displacementEv(
    const QQuickTumblerAttached *self) {
  return self->displacement();
}

//  void QQuickTumblerAttached::displacementChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTumblerAttached19displacementChangedEv(
    QQuickTumblerAttached *self) {
  self->displacementChanged();
}

//  QQuickTumblerAttachedPrivate *QQuickTumblerAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickTumblerAttachedPrivate *ritual_ZN21QQuickTumblerAttached6d_funcEv(
    QQuickTumblerAttached *self) {
  return self->d_func();
}

//  const QQuickTumblerAttachedPrivate *QQuickTumblerAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTumblerAttachedPrivate *ritual_ZNK21QQuickTumblerAttached6d_funcEv(
    const QQuickTumblerAttached *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_pathview)
