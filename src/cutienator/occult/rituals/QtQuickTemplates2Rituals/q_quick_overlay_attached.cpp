//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickOverlayAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickOverlayAttached10metaObjectEv(
    const QQuickOverlayAttached *self) {
  return self->metaObject();
}

//  QString QQuickOverlayAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickOverlayAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickOverlayAttached::tr(s, c, n));
}

//  QQuickOverlayAttached::QQuickOverlayAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickOverlayAttached *ritual_ZN21QQuickOverlayAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickOverlayAttached(parent);
}

//  QQuickOverlay *QQuickOverlayAttached::overlay() const
extern "C" Q_DECL_EXPORT
QQuickOverlay *ritual_ZNK21QQuickOverlayAttached7overlayEv(
    const QQuickOverlayAttached *self) {
  return self->overlay();
}

//  QQmlComponent *QQuickOverlayAttached::modal() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK21QQuickOverlayAttached5modalEv(
    const QQuickOverlayAttached *self) {
  return self->modal();
}

//  void QQuickOverlayAttached::setModal(QQmlComponent *modal)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickOverlayAttached8setModalEP13QQmlComponent(
    QQuickOverlayAttached *self,
    QQmlComponent *modal) {
  self->setModal(modal);
}

//  QQmlComponent *QQuickOverlayAttached::modeless() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK21QQuickOverlayAttached8modelessEv(
    const QQuickOverlayAttached *self) {
  return self->modeless();
}

//  void QQuickOverlayAttached::setModeless(QQmlComponent *modeless)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickOverlayAttached11setModelessEP13QQmlComponent(
    QQuickOverlayAttached *self,
    QQmlComponent *modeless) {
  self->setModeless(modeless);
}
