//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DInput::QAbstractPhysicalDeviceProxy::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy10metaObjectEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->metaObject();
}

//  QString Qt3DInput::QAbstractPhysicalDeviceProxy::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAbstractPhysicalDeviceProxy::tr(s, c, n));
}

//  QAbstractPhysicalDeviceProxyPrivate
//      *Qt3DInput::QAbstractPhysicalDeviceProxy::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy6d_funcEv(
    Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->d_func();
}

//  const QAbstractPhysicalDeviceProxyPrivate
//      *Qt3DInput::QAbstractPhysicalDeviceProxy::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy6d_funcEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->d_func();
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::axisCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy9axisCountEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->Qt3DInput::QAbstractPhysicalDeviceProxy::axisCount();
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy11buttonCountEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->Qt3DInput::QAbstractPhysicalDeviceProxy::buttonCount();
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::axisIdentifier(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy14axisIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    const QString *name) {
  return self->Qt3DInput::QAbstractPhysicalDeviceProxy::axisIdentifier(
      *name);
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonIdentifier(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy16buttonIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    const QString *name) {
  return self->Qt3DInput::QAbstractPhysicalDeviceProxy::buttonIdentifier(
      *name);
}
