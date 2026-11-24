//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensormanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensormanager.h>
#include <cstring>

//  A QSensorBackendFactory that Python can take functions over in. Every QSensorBackendFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSensorBackendFactoryCall0)(const void *, QSensor *, int *);
class CuteQSensorBackendFactory : public QSensorBackendFactory {
public:
  using QSensorBackendFactory::QSensorBackendFactory;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QSensorBackendFactory13createBackendEP7QSensor")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QSensorBackend *QSensorBackendFactory::createBackend(QSensor *sensor)
  QSensorBackend *createBackend(QSensor *sensor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorBackendFactoryCall0 call = reinterpret_cast<CuteQSensorBackendFactoryCall0>(taken[0]);
      void * given = call(this, sensor, &handled);
      if (handled) return static_cast<QSensorBackend *>(given);
    }
    return {};
  }
};

//  QSensorBackend *QSensorBackendFactory::createBackend(QSensor *sensor)
extern "C" Q_DECL_EXPORT
QSensorBackend *ritual_ZN21QSensorBackendFactory13createBackendEP7QSensor(
    QSensorBackendFactory *self,
    QSensor *sensor) {
  return self->createBackend(sensor);
}

//  QSensorBackendFactory::~QSensorBackendFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSensorBackendFactoryD1Ev(QSensorBackendFactory *self) {
  delete self;
}

//  a Python function taken by a CuteQSensorBackendFactory, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensorBackendFactory(
    QSensorBackendFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSensorBackendFactory *>(self)->take(key, call);
}
