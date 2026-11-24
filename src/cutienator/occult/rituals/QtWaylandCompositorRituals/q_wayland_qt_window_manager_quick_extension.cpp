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

//  const QMetaObject *QWaylandQtWindowManagerQuickExtension::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QWaylandQtWindowManagerQuickExtension10metaObjectEv(
    const QWaylandQtWindowManagerQuickExtension *self) {
  return self->metaObject();
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

#endif  // QT_CONFIG(wayland_compositor_quick)
