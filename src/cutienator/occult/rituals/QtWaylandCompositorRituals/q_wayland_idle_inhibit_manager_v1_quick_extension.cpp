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
//      *QWaylandIdleInhibitManagerV1QuickExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK42QWaylandIdleInhibitManagerV1QuickExtension10metaObjectEv(
    const QWaylandIdleInhibitManagerV1QuickExtension *self) {
  return self->metaObject();
}

//  QString QWaylandIdleInhibitManagerV1QuickExtension::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN42QWaylandIdleInhibitManagerV1QuickExtension2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QWaylandIdleInhibitManagerV1QuickExtension::tr(
          s,
          c,
          n));
}

//  void QWaylandIdleInhibitManagerV1QuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QWaylandIdleInhibitManagerV1QuickExtension10classBeginEv(
    QWaylandIdleInhibitManagerV1QuickExtension *self) {
  self->classBegin();
}

//  void QWaylandIdleInhibitManagerV1QuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QWaylandIdleInhibitManagerV1QuickExtension17componentCompleteEv(
    QWaylandIdleInhibitManagerV1QuickExtension *self) {
  self->componentComplete();
}

//  QWaylandIdleInhibitManagerV1QuickExtension as the QQmlParserStatus it is
//      built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandIdleInhibitManagerV1QuickExtension_QQmlParserStatus(
    QWaylandIdleInhibitManagerV1QuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QWaylandIdleInhibitManagerV1QuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN42QWaylandIdleInhibitManagerV1QuickExtension10classBeginEv(
    QWaylandIdleInhibitManagerV1QuickExtension *self) {
  self->QWaylandIdleInhibitManagerV1QuickExtension::classBegin();
}

//  void QWaylandIdleInhibitManagerV1QuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN42QWaylandIdleInhibitManagerV1QuickExtension17componentCompleteEv(
    QWaylandIdleInhibitManagerV1QuickExtension *self) {
  self->QWaylandIdleInhibitManagerV1QuickExtension::componentComplete();
}

#endif  // QT_CONFIG(wayland_compositor_quick)
