//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensor.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSensorFilter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSensorFilter : QSensorFilter {
  using QSensorFilter::setSensor;
};

//  A QSensorFilter that Python can take functions over in. Every QSensorFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSensorFilterCall0)(const void *, QSensorReading *, int *);
typedef void (*CuteQSensorFilterCall1)(const void *, QSensor *, int *);
class CuteQSensorFilter : public QSensorFilter {
public:
  using QSensorFilter::QSensorFilter;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QSensorFilter6filterEP14QSensorReading")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSensorFilter9setSensorEP7QSensor")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QSensorFilter::filter(QSensorReading *reading)
  bool filter(QSensorReading *reading) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorFilterCall0 call = reinterpret_cast<CuteQSensorFilterCall0>(taken[0]);
      bool given = call(this, reading, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSensorFilter::setSensor(QSensor *sensor)
  void setSensor(QSensor *sensor) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSensorFilterCall1 call = reinterpret_cast<CuteQSensorFilterCall1>(taken[1]);
      call(this, sensor, &handled);
      if (handled) return;
    }
    QSensorFilter::setSensor(sensor);
  }
};

//  bool QSensorFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSensorFilter6filterEP14QSensorReading(
    QSensorFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  QSensorFilter::~QSensorFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSensorFilterD1Ev(QSensorFilter *self) {
  delete self;
}

//  void QSensorFilter::setSensor(QSensor *sensor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSensorFilter9setSensorEP7QSensor(
    QSensorFilter *self,
    QSensor *sensor) {
  self->setSensor(sensor);
}

//  a Python function taken by a CuteQSensorFilter, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensorFilter(
    QSensorFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSensorFilter *>(self)->take(key, call);
}

//  void QSensorFilter::setSensor(QSensor *sensor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSensorFilter9setSensorEP7QSensor(
    QSensorFilter *self,
    QSensor *sensor) {
  static_cast<OwnQSensorFilter *>(self)->OwnQSensorFilter::setSensor(sensor);
}

//  QList<QSensorFilter *>::QList()
extern "C" Q_DECL_EXPORT
QList<QSensorFilter *> *ritual_list_make_QSensorFilter_ptr() {
  return new QList<QSensorFilter *>();
}

//  void QList<QSensorFilter *>::append(const QSensorFilter * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSensorFilter_ptr(
    QList<QSensorFilter *> *self,
    QSensorFilter *element) {
  self->append(element);
}

//  qsizetype QList<QSensorFilter *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSensorFilter_ptr(
    const QList<QSensorFilter *> *self) {
  return self->size();
}

//  const QSensorFilter * &QList<QSensorFilter *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSensorFilter *ritual_list_at_QSensorFilter_ptr(
    const QList<QSensorFilter *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QSensorFilter *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSensorFilter_ptr(QList<QSensorFilter *> *self) {
  delete self;
}
