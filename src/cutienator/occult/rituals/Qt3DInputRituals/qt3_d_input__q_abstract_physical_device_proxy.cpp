//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *Qt3DInput::QAbstractPhysicalDeviceProxy::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy10metaObjectEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAbstractPhysicalDeviceProxy::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy11qt_metacastEPKc(
    Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      Qt3DInput::QAbstractPhysicalDeviceProxy::qt_metacall(QMetaObject::Cal
//      l a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QString Qt3DInput::QAbstractPhysicalDeviceProxy::deviceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy10deviceNameEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return new QString(self->deviceName());
}

//  DeviceStatus Qt3DInput::QAbstractPhysicalDeviceProxy::status() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceProxy::DeviceStatus ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy6statusEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->status();
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::axisCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy9axisCountEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->axisCount();
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy11buttonCountEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return self->buttonCount();
}

//  QStringList Qt3DInput::QAbstractPhysicalDeviceProxy::axisNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy9axisNamesEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return new QList<QString>(self->axisNames());
}

//  QStringList Qt3DInput::QAbstractPhysicalDeviceProxy::buttonNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy11buttonNamesEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self) {
  return new QList<QString>(self->buttonNames());
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::axisIdentifier(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy14axisIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    const QString *name) {
  return self->axisIdentifier(*name);
}

//  int Qt3DInput::QAbstractPhysicalDeviceProxy::buttonIdentifier(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput28QAbstractPhysicalDeviceProxy16buttonIdentifierERK7QString(
    const Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    const QString *name) {
  return self->buttonIdentifier(*name);
}

//  void Qt3DInput::QAbstractPhysicalDeviceProxy::statusChanged(QAbstractPhys
//      icalDeviceProxy::DeviceStatus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxy13statusChangedENS0_12DeviceStatusE(
    Qt3DInput::QAbstractPhysicalDeviceProxy *self,
    Qt3DInput::QAbstractPhysicalDeviceProxy::DeviceStatus status) {
  self->statusChanged(status);
}

//  Qt3DInput::QAbstractPhysicalDeviceProxy::QAbstractPhysicalDeviceProxy(QAb
//      stractPhysicalDeviceProxyPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceProxy *ritual_ZN9Qt3DInput28QAbstractPhysicalDeviceProxyC1ERNS_35QAbstractPhysicalDeviceProxyPrivateEPN8Qt3DCore5QNodeE(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new Qt3DInput::QAbstractPhysicalDeviceProxy(*dd, parent);
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
