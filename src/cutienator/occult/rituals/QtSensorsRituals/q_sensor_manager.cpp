//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensormanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensormanager.h>
#include <QtCore/qbytearray.h>

//  void QSensorManager::registerBackend(const QByteArray &type, const
//      QByteArray &identifier, QSensorBackendFactory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorManager15registerBackendERK10QByteArrayS2_P21QSensorBackendFactory(
    const QByteArray *type,
    const QByteArray *identifier,
    QSensorBackendFactory *factory) {
  QSensorManager::registerBackend(*type, *identifier, factory);
}

//  void QSensorManager::unregisterBackend(const QByteArray &type, const
//      QByteArray &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorManager17unregisterBackendERK10QByteArrayS2_(
    const QByteArray *type,
    const QByteArray *identifier) {
  QSensorManager::unregisterBackend(*type, *identifier);
}

//  bool QSensorManager::isBackendRegistered(const QByteArray &type, const
//      QByteArray &identifier)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSensorManager19isBackendRegisteredERK10QByteArrayS2_(
    const QByteArray *type,
    const QByteArray *identifier) {
  return QSensorManager::isBackendRegistered(*type, *identifier);
}

//  QSensorBackend *QSensorManager::createBackend(QSensor *sensor)
extern "C" Q_DECL_EXPORT
QSensorBackend *ritual_ZN14QSensorManager13createBackendEP7QSensor(
    QSensor *sensor) {
  return QSensorManager::createBackend(sensor);
}

//  void QSensorManager::setDefaultBackend(const QByteArray &type, const
//      QByteArray &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorManager17setDefaultBackendERK10QByteArrayS2_(
    const QByteArray *type,
    const QByteArray *identifier) {
  QSensorManager::setDefaultBackend(*type, *identifier);
}

//  QSensorManager::~QSensorManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorManagerD1Ev(QSensorManager *self) {
  delete self;
}
