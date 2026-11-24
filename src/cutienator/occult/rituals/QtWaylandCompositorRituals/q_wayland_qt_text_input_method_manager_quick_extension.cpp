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

//  const QMetaObject
//      *QWaylandQtTextInputMethodManagerQuickExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK46QWaylandQtTextInputMethodManagerQuickExtension10metaObjectEv(
    const QWaylandQtTextInputMethodManagerQuickExtension *self) {
  return self->metaObject();
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

#endif  // QT_CONFIG(wayland_compositor_quick)
