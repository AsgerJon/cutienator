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

//  const QMetaObject
//      *QWaylandQtTextInputMethodManagerQuickExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK46QWaylandQtTextInputMethodManagerQuickExtension10metaObjectEv(
    const QWaylandQtTextInputMethodManagerQuickExtension *self) {
  return self->metaObject();
}

//  void *QWaylandQtTextInputMethodManagerQuickExtension::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension11qt_metacastEPKc(
    QWaylandQtTextInputMethodManagerQuickExtension *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQtTextInputMethodManagerQuickExtension::qt_metacall(QMetaObje
//      ct::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQtTextInputMethodManagerQuickExtension *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQtTextInputMethodManagerQuickExtension::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QWaylandQtTextInputMethodManagerQuickExtension::tr(
          s,
          c,
          n));
}

//  QQmlListProperty<QObject>
//      QWaylandQtTextInputMethodManagerQuickExtension::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension4dataEv(
    QWaylandQtTextInputMethodManagerQuickExtension *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  void QWaylandQtTextInputMethodManagerQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension10classBeginEv(
    QWaylandQtTextInputMethodManagerQuickExtension *self) {
  self->classBegin();
}

//  void QWaylandQtTextInputMethodManagerQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN46QWaylandQtTextInputMethodManagerQuickExtension17componentCompleteEv(
    QWaylandQtTextInputMethodManagerQuickExtension *self) {
  self->componentComplete();
}

//  QWaylandQtTextInputMethodManagerQuickExtension as the QQmlParserStatus it
//      is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandQtTextInputMethodManagerQuickExtension_QQmlParserStatus(
    QWaylandQtTextInputMethodManagerQuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QWaylandQtTextInputMethodManagerQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN46QWaylandQtTextInputMethodManagerQuickExtension10classBeginEv(
    QWaylandQtTextInputMethodManagerQuickExtension *self) {
  self->QWaylandQtTextInputMethodManagerQuickExtension::classBegin();
}

//  void QWaylandQtTextInputMethodManagerQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN46QWaylandQtTextInputMethodManagerQuickExtension17componentCompleteEv(
    QWaylandQtTextInputMethodManagerQuickExtension *self) {
  self->QWaylandQtTextInputMethodManagerQuickExtension::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of
//      QWaylandQtTextInputMethodManagerQuickExtension gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandQtTextInputMethodManagerQuickExtension__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
