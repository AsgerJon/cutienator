//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorquickextension
//  s_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorquickextensions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  const QMetaObject *QWaylandQtWindowManagerQuickExtension::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QWaylandQtWindowManagerQuickExtension10metaObjectEv(
    const QWaylandQtWindowManagerQuickExtension *self) {
  return self->metaObject();
}

//  void *QWaylandQtWindowManagerQuickExtension::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN37QWaylandQtWindowManagerQuickExtension11qt_metacastEPKc(
    QWaylandQtWindowManagerQuickExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQtWindowManagerQuickExtension::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN37QWaylandQtWindowManagerQuickExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQtWindowManagerQuickExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQtWindowManagerQuickExtension::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN37QWaylandQtWindowManagerQuickExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQtWindowManagerQuickExtension::tr(s, c, n));
}

//  QQmlListProperty<QObject> QWaylandQtWindowManagerQuickExtension::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN37QWaylandQtWindowManagerQuickExtension4dataEv(
    QWaylandQtWindowManagerQuickExtension *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  void QWaylandQtWindowManagerQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QWaylandQtWindowManagerQuickExtension10classBeginEv(
    QWaylandQtWindowManagerQuickExtension *self) {
  self->classBegin();
}

//  void QWaylandQtWindowManagerQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QWaylandQtWindowManagerQuickExtension17componentCompleteEv(
    QWaylandQtWindowManagerQuickExtension *self) {
  self->componentComplete();
}

//  QWaylandQtWindowManagerQuickExtension as the QQmlParserStatus it is built
//      on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandQtWindowManagerQuickExtension_QQmlParserStatus(
    QWaylandQtWindowManagerQuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QWaylandQtWindowManagerQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QWaylandQtWindowManagerQuickExtension10classBeginEv(
    QWaylandQtWindowManagerQuickExtension *self) {
  self->QWaylandQtWindowManagerQuickExtension::classBegin();
}

//  void QWaylandQtWindowManagerQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN37QWaylandQtWindowManagerQuickExtension17componentCompleteEv(
    QWaylandQtWindowManagerQuickExtension *self) {
  self->QWaylandQtWindowManagerQuickExtension::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of
//      QWaylandQtWindowManagerQuickExtension gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandQtWindowManagerQuickExtension__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
