//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 3. Kept as it is when the generator runs again.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qobjectdefs.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qlist.h>
#include <vector>
#include <Qt3DCore/Qt3DCore>
#include <QtCore/QList>
#include <Qt3DCore/qbackendnode.h>
#include <Qt3DInput/qkeyboarddevice.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DInput/qabstractphysicaldevice.h>

//  const QMetaObject *Qt3DInput::QInputDeviceIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput23QInputDeviceIntegration10metaObjectEv(
    const Qt3DInput::QInputDeviceIntegration *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QInputDeviceIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput23QInputDeviceIntegration11qt_metacastEPKc(
    Qt3DInput::QInputDeviceIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QInputDeviceIntegration::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput23QInputDeviceIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QInputDeviceIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void Qt3DInput::QInputDeviceIntegration::registerBackendType(const
//      QMetaObject &metaObject, const Qt3DCore::QBackendNodeMapperPtr
//      &functor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QInputDeviceIntegration19registerBackendTypeERK11QMetaObjectRK14QSharedPointerIN8Qt3DCore18QBackendNodeMapperEE(
    Qt3DInput::QInputDeviceIntegration *self,
    const QMetaObject *metaObject,
    const Qt3DCore::QBackendNodeMapperPtr *functor) {
  self->registerBackendType(*metaObject, *functor);
}

//  void
//      Qt3DInput::QInputDeviceIntegration::initialize(Qt3DInput::QInputAspec
//      t *aspect)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QInputDeviceIntegration10initializeEPNS_12QInputAspectE(
    Qt3DInput::QInputDeviceIntegration *self,
    Qt3DInput::QInputAspect *aspect) {
  self->initialize(aspect);
}

//  std::vector<Qt3DCore::QAspectJobPtr>
//      Qt3DInput::QInputDeviceIntegration::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN9Qt3DInput23QInputDeviceIntegration13jobsToExecuteEx(
    Qt3DInput::QInputDeviceIntegration *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
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

//  QList<Qt3DCore::QNodeId>
//      Qt3DInput::QInputDeviceIntegration::physicalDevices() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput23QInputDeviceIntegration15physicalDevicesEv(
    const Qt3DInput::QInputDeviceIntegration *self) {
  return new QList<Qt3DCore::QNodeId>(self->physicalDevices());
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

//  QInputAspect *Qt3DInput::QInputDeviceIntegration::inputAspect() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputAspect *ritual_ZNK9Qt3DInput23QInputDeviceIntegration11inputAspectEv(
    const Qt3DInput::QInputDeviceIntegration *self) {
  return self->inputAspect();
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

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DInput::QInputDeviceIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QInputDeviceIntegration__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DInput::QInputDeviceIntegration
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QInputDeviceIntegration__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}

//  void
//      Qt3DInput::QInputDeviceIntegration::registerBackendType<Qt3DInput::QKeyboardDevice>(
//      const Qt3DCore::QBackendNodeMapperPtr &functor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QInputDeviceIntegration19registerBackendTypeINS_15QKeyboardDeviceEEEvRK14QSharedPointerIN8Qt3DCore18QBackendNodeMapperEE(
    Qt3DInput::QInputDeviceIntegration *self,
    const QSharedPointer<Qt3DCore::QBackendNodeMapper> *functor) {
  self->registerBackendType<Qt3DInput::QKeyboardDevice>(*functor);
}

//  void
//      Qt3DInput::QInputDeviceIntegration::registerBackendType<Qt3DInput::QMouseDevice>(
//      const Qt3DCore::QBackendNodeMapperPtr &functor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QInputDeviceIntegration19registerBackendTypeINS_12QMouseDeviceEEEvRK14QSharedPointerIN8Qt3DCore18QBackendNodeMapperEE(
    Qt3DInput::QInputDeviceIntegration *self,
    const QSharedPointer<Qt3DCore::QBackendNodeMapper> *functor) {
  self->registerBackendType<Qt3DInput::QMouseDevice>(*functor);
}

//  void
//      Qt3DInput::QInputDeviceIntegration::registerBackendType<Qt3DInput::QAbstractPhysicalDevice>(
//      const Qt3DCore::QBackendNodeMapperPtr &functor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput23QInputDeviceIntegration19registerBackendTypeINS_23QAbstractPhysicalDeviceEEEvRK14QSharedPointerIN8Qt3DCore18QBackendNodeMapperEE(
    Qt3DInput::QInputDeviceIntegration *self,
    const QSharedPointer<Qt3DCore::QBackendNodeMapper> *functor) {
  self->registerBackendType<Qt3DInput::QAbstractPhysicalDevice>(*functor);
}
