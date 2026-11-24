//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensorplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensorplugin.h>
#include <cstring>

//  A QSensorChangesInterface that Python can take functions over in. Every QSensorChangesInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSensorChangesInterfaceCall0)(const void *, int *);
class CuteQSensorChangesInterface : public QSensorChangesInterface {
public:
  using QSensorChangesInterface::QSensorChangesInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QSensorChangesInterface14sensorsChangedEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSensorChangesInterface::sensorsChanged()
  void sensorsChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorChangesInterfaceCall0 call = reinterpret_cast<CuteQSensorChangesInterfaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  void QSensorChangesInterface::sensorsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSensorChangesInterface14sensorsChangedEv(
    QSensorChangesInterface *self) {
  self->sensorsChanged();
}

//  QSensorChangesInterface::~QSensorChangesInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSensorChangesInterfaceD1Ev(QSensorChangesInterface *self) {
  delete self;
}

//  a Python function taken by a CuteQSensorChangesInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensorChangesInterface(
    QSensorChangesInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSensorChangesInterface *>(self)->take(key, call);
}
