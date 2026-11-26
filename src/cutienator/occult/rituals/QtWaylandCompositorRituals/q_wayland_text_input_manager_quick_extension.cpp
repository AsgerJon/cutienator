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

//  const QMetaObject *QWaylandTextInputManagerQuickExtension::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK38QWaylandTextInputManagerQuickExtension10metaObjectEv(
    const QWaylandTextInputManagerQuickExtension *self) {
  return self->metaObject();
}

//  void *QWaylandTextInputManagerQuickExtension::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN38QWaylandTextInputManagerQuickExtension11qt_metacastEPKc(
    QWaylandTextInputManagerQuickExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandTextInputManagerQuickExtension::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN38QWaylandTextInputManagerQuickExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandTextInputManagerQuickExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandTextInputManagerQuickExtension::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN38QWaylandTextInputManagerQuickExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandTextInputManagerQuickExtension::tr(s, c, n));
}

//  QQmlListProperty<QObject> QWaylandTextInputManagerQuickExtension::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN38QWaylandTextInputManagerQuickExtension4dataEv(
    QWaylandTextInputManagerQuickExtension *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  void QWaylandTextInputManagerQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QWaylandTextInputManagerQuickExtension10classBeginEv(
    QWaylandTextInputManagerQuickExtension *self) {
  self->classBegin();
}

//  void QWaylandTextInputManagerQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QWaylandTextInputManagerQuickExtension17componentCompleteEv(
    QWaylandTextInputManagerQuickExtension *self) {
  self->componentComplete();
}

//  QWaylandTextInputManagerQuickExtension as the QQmlParserStatus it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandTextInputManagerQuickExtension_QQmlParserStatus(
    QWaylandTextInputManagerQuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QWaylandTextInputManagerQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QWaylandTextInputManagerQuickExtension10classBeginEv(
    QWaylandTextInputManagerQuickExtension *self) {
  self->QWaylandTextInputManagerQuickExtension::classBegin();
}

//  void QWaylandTextInputManagerQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN38QWaylandTextInputManagerQuickExtension17componentCompleteEv(
    QWaylandTextInputManagerQuickExtension *self) {
  self->QWaylandTextInputManagerQuickExtension::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of
//      QWaylandTextInputManagerQuickExtension gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandTextInputManagerQuickExtension__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
