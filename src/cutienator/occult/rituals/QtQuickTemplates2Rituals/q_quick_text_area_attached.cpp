//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickTextAreaAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickTextAreaAttached10metaObjectEv(
    const QQuickTextAreaAttached *self) {
  return self->metaObject();
}

//  void *QQuickTextAreaAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickTextAreaAttached11qt_metacastEPKc(
    QQuickTextAreaAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextAreaAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickTextAreaAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextAreaAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTextAreaAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickTextAreaAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextAreaAttached::tr(s, c, n));
}

//  QQuickTextAreaAttached::QQuickTextAreaAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickTextAreaAttached *ritual_ZN22QQuickTextAreaAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickTextAreaAttached(parent);
}

//  QQuickTextArea *QQuickTextAreaAttached::flickable() const
extern "C" Q_DECL_EXPORT
QQuickTextArea *ritual_ZNK22QQuickTextAreaAttached9flickableEv(
    const QQuickTextAreaAttached *self) {
  return self->flickable();
}

//  void QQuickTextAreaAttached::setFlickable(QQuickTextArea *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextAreaAttached12setFlickableEP14QQuickTextArea(
    QQuickTextAreaAttached *self,
    QQuickTextArea *control) {
  self->setFlickable(control);
}

//  void QQuickTextAreaAttached::flickableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextAreaAttached16flickableChangedEv(
    QQuickTextAreaAttached *self) {
  self->flickableChanged();
}

//  QQuickTextAreaAttachedPrivate *QQuickTextAreaAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextAreaAttachedPrivate *ritual_ZN22QQuickTextAreaAttached6d_funcEv(
    QQuickTextAreaAttached *self) {
  return self->d_func();
}

//  const QQuickTextAreaAttachedPrivate *QQuickTextAreaAttached::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickTextAreaAttachedPrivate *ritual_ZNK22QQuickTextAreaAttached6d_funcEv(
    const QQuickTextAreaAttached *self) {
  return self->d_func();
}
