//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qlist.h>

//  const QMetaObject *Qt3DInput::QInputDeviceIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput23QInputDeviceIntegration10metaObjectEv(
    const Qt3DInput::QInputDeviceIntegration *self) {
  return self->metaObject();
}

//  QString Qt3DInput::QInputDeviceIntegration::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput23QInputDeviceIntegration2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QInputDeviceIntegration::tr(s, c, n));
}

//  QAbstractPhysicalDevice
//      *Qt3DInput::QInputDeviceIntegration::createPhysicalDevice(const
//      QString &name)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZN9Qt3DInput23QInputDeviceIntegration20createPhysicalDeviceERK7QString(
    Qt3DInput::QInputDeviceIntegration *self,
    const QString *name) {
  return self->createPhysicalDevice(*name);
}

//  QAbstractPhysicalDeviceBackendNode
//      *Qt3DInput::QInputDeviceIntegration::physicalDevice(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceBackendNode *ritual_ZNK9Qt3DInput23QInputDeviceIntegration14physicalDeviceEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::QInputDeviceIntegration *self,
    const Qt3DCore::QNodeId *id) {
  return self->physicalDevice(*id);
}

//  QStringList Qt3DInput::QInputDeviceIntegration::deviceNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9Qt3DInput23QInputDeviceIntegration11deviceNamesEv(
    const Qt3DInput::QInputDeviceIntegration *self) {
  return new QList<QString>(self->deviceNames());
}

//  void Qt3DInput::QInputDeviceIntegration::onInitialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QInputDeviceIntegration12onInitializeEv(
    Qt3DInput::QInputDeviceIntegration *self) {
  self->onInitialize();
}

//  QInputDeviceIntegrationPrivate
//      *Qt3DInput::QInputDeviceIntegration::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputDeviceIntegrationPrivate *ritual_ZN9Qt3DInput23QInputDeviceIntegration6d_funcEv(
    Qt3DInput::QInputDeviceIntegration *self) {
  return self->d_func();
}

//  const QInputDeviceIntegrationPrivate
//      *Qt3DInput::QInputDeviceIntegration::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputDeviceIntegrationPrivate *ritual_ZNK9Qt3DInput23QInputDeviceIntegration6d_funcEv(
    const Qt3DInput::QInputDeviceIntegration *self) {
  return self->d_func();
}
