//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensorplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensorplugin.h>
#include <cstring>

//  A QSensorPluginInterface that Python can take functions over in. Every QSensorPluginInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSensorPluginInterfaceCall0)(const void *, int *);
class CuteQSensorPluginInterface : public QSensorPluginInterface {
public:
  using QSensorPluginInterface::QSensorPluginInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QSensorPluginInterface15registerSensorsEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSensorPluginInterface::registerSensors()
  void registerSensors() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorPluginInterfaceCall0 call = reinterpret_cast<CuteQSensorPluginInterfaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  void QSensorPluginInterface::registerSensors()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSensorPluginInterface15registerSensorsEv(
    QSensorPluginInterface *self) {
  self->registerSensors();
}

//  QSensorPluginInterface::~QSensorPluginInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSensorPluginInterfaceD1Ev(QSensorPluginInterface *self) {
  delete self;
}

//  a Python function taken by a CuteQSensorPluginInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensorPluginInterface(
    QSensorPluginInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSensorPluginInterface *>(self)->take(key, call);
}
