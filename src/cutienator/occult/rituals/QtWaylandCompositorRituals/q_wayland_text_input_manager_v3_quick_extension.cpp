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

//  const QMetaObject *QWaylandTextInputManagerV3QuickExtension::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK40QWaylandTextInputManagerV3QuickExtension10metaObjectEv(
    const QWaylandTextInputManagerV3QuickExtension *self) {
  return self->metaObject();
}

//  void *QWaylandTextInputManagerV3QuickExtension::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN40QWaylandTextInputManagerV3QuickExtension11qt_metacastEPKc(
    QWaylandTextInputManagerV3QuickExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QWaylandTextInputManagerV3QuickExtension::qt_metacall(QMetaObject::Ca
//      ll a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN40QWaylandTextInputManagerV3QuickExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandTextInputManagerV3QuickExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandTextInputManagerV3QuickExtension::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN40QWaylandTextInputManagerV3QuickExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandTextInputManagerV3QuickExtension::tr(s, c, n));
}

//  QQmlListProperty<QObject>
//      QWaylandTextInputManagerV3QuickExtension::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN40QWaylandTextInputManagerV3QuickExtension4dataEv(
    QWaylandTextInputManagerV3QuickExtension *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  void QWaylandTextInputManagerV3QuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QWaylandTextInputManagerV3QuickExtension10classBeginEv(
    QWaylandTextInputManagerV3QuickExtension *self) {
  self->classBegin();
}

//  void QWaylandTextInputManagerV3QuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN40QWaylandTextInputManagerV3QuickExtension17componentCompleteEv(
    QWaylandTextInputManagerV3QuickExtension *self) {
  self->componentComplete();
}

//  QWaylandTextInputManagerV3QuickExtension as the QQmlParserStatus it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandTextInputManagerV3QuickExtension_QQmlParserStatus(
    QWaylandTextInputManagerV3QuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QWaylandTextInputManagerV3QuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN40QWaylandTextInputManagerV3QuickExtension10classBeginEv(
    QWaylandTextInputManagerV3QuickExtension *self) {
  self->QWaylandTextInputManagerV3QuickExtension::classBegin();
}

//  void QWaylandTextInputManagerV3QuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN40QWaylandTextInputManagerV3QuickExtension17componentCompleteEv(
    QWaylandTextInputManagerV3QuickExtension *self) {
  self->QWaylandTextInputManagerV3QuickExtension::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of
//      QWaylandTextInputManagerV3QuickExtension gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandTextInputManagerV3QuickExtension__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
