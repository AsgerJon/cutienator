//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSensor that Python can take functions over in. Every QSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSensorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSensorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSensor : public QSensor {
public:
  using QSensor::QSensor;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorCall0 call = reinterpret_cast<CuteQSensorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSensorCall1 call = reinterpret_cast<CuteQSensorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSensorCall2 call = reinterpret_cast<CuteQSensorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSensorCall3 call = reinterpret_cast<CuteQSensorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSensorCall4 call = reinterpret_cast<CuteQSensorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSensorCall5 call = reinterpret_cast<CuteQSensorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSensorCall6 call = reinterpret_cast<CuteQSensorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QSensor10metaObjectEv(const QSensor *self) {
  return self->metaObject();
}

//  QString QSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QSensor2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QSensor::tr(s, c, n));
}

//  QSensor::QSensor(const QByteArray &type, QObject *parent)
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZN7QSensorC1ERK10QByteArrayP7QObject(
    const QByteArray *type,
    QObject *parent) {
  return new CuteQSensor(*type, parent);
}

//  QSensor::~QSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensorD1Ev(QSensor *self) {
  delete self;
}

//  QByteArray QSensor::identifier() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QSensor10identifierEv(const QSensor *self) {
  return new QByteArray(self->identifier());
}

//  void QSensor::setIdentifier(const QByteArray &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor13setIdentifierERK10QByteArray(
    QSensor *self,
    const QByteArray *identifier) {
  self->setIdentifier(*identifier);
}

//  QByteArray QSensor::type() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QSensor4typeEv(const QSensor *self) {
  return new QByteArray(self->type());
}

//  bool QSensor::connectToBackend()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QSensor16connectToBackendEv(QSensor *self) {
  return self->connectToBackend();
}

//  bool QSensor::isConnectedToBackend() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSensor20isConnectedToBackendEv(const QSensor *self) {
  return self->isConnectedToBackend();
}

//  bool QSensor::isBusy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSensor6isBusyEv(const QSensor *self) {
  return self->isBusy();
}

//  void QSensor::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor9setActiveEb(QSensor *self, bool active) {
  self->setActive(active);
}

//  bool QSensor::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSensor8isActiveEv(const QSensor *self) {
  return self->isActive();
}

//  bool QSensor::isAlwaysOn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSensor10isAlwaysOnEv(const QSensor *self) {
  return self->isAlwaysOn();
}

//  void QSensor::setAlwaysOn(bool alwaysOn)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor11setAlwaysOnEb(QSensor *self, bool alwaysOn) {
  self->setAlwaysOn(alwaysOn);
}

//  bool QSensor::skipDuplicates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSensor14skipDuplicatesEv(const QSensor *self) {
  return self->skipDuplicates();
}

//  void QSensor::setSkipDuplicates(bool skipDuplicates)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor17setSkipDuplicatesEb(
    QSensor *self,
    bool skipDuplicates) {
  self->setSkipDuplicates(skipDuplicates);
}

//  int QSensor::dataRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor8dataRateEv(const QSensor *self) {
  return self->dataRate();
}

//  void QSensor::setDataRate(int rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor11setDataRateEi(QSensor *self, int rate) {
  self->setDataRate(rate);
}

//  qoutputrangelist QSensor::outputRanges() const
extern "C" Q_DECL_EXPORT
QList<qoutputrange> *ritual_ZNK7QSensor12outputRangesEv(
    const QSensor *self) {
  return new QList<qoutputrange>(self->outputRanges());
}

//  int QSensor::outputRange() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor11outputRangeEv(const QSensor *self) {
  return self->outputRange();
}

//  void QSensor::setOutputRange(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor14setOutputRangeEi(QSensor *self, int index) {
  self->setOutputRange(index);
}

//  QString QSensor::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QSensor11descriptionEv(const QSensor *self) {
  return new QString(self->description());
}

//  int QSensor::error() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor5errorEv(const QSensor *self) {
  return self->error();
}

//  void QSensor::addFilter(QSensorFilter *filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor9addFilterEP13QSensorFilter(
    QSensor *self,
    QSensorFilter *filter) {
  self->addFilter(filter);
}

//  void QSensor::removeFilter(QSensorFilter *filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor12removeFilterEP13QSensorFilter(
    QSensor *self,
    QSensorFilter *filter) {
  self->removeFilter(filter);
}

//  QList<QSensorFilter *> QSensor::filters() const
extern "C" Q_DECL_EXPORT
QList<QSensorFilter *> *ritual_ZNK7QSensor7filtersEv(const QSensor *self) {
  return new QList<QSensorFilter *>(self->filters());
}

//  QSensorReading *QSensor::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK7QSensor7readingEv(const QSensor *self) {
  return self->reading();
}

//  QList<QByteArray> QSensor::sensorTypes()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN7QSensor11sensorTypesEv() {
  return new QList<QByteArray>(QSensor::sensorTypes());
}

//  QList<QByteArray> QSensor::sensorsForType(const QByteArray &type)
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN7QSensor14sensorsForTypeERK10QByteArray(
    const QByteArray *type) {
  return new QList<QByteArray>(QSensor::sensorsForType(*type));
}

//  QByteArray QSensor::defaultSensorForType(const QByteArray &type)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QSensor20defaultSensorForTypeERK10QByteArray(
    const QByteArray *type) {
  return new QByteArray(QSensor::defaultSensorForType(*type));
}

//  bool QSensor::isFeatureSupported(Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSensor18isFeatureSupportedENS_7FeatureE(
    const QSensor *self,
    QSensor::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  AxesOrientationMode QSensor::axesOrientationMode() const
extern "C" Q_DECL_EXPORT
QSensor::AxesOrientationMode ritual_ZNK7QSensor19axesOrientationModeEv(
    const QSensor *self) {
  return self->axesOrientationMode();
}

//  void QSensor::setAxesOrientationMode(AxesOrientationMode
//      axesOrientationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor22setAxesOrientationModeENS_19AxesOrientationModeE(
    QSensor *self,
    QSensor::AxesOrientationMode axesOrientationMode) {
  self->setAxesOrientationMode(axesOrientationMode);
}

//  int QSensor::currentOrientation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor18currentOrientationEv(const QSensor *self) {
  return self->currentOrientation();
}

//  void QSensor::setCurrentOrientation(int currentOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor21setCurrentOrientationEi(
    QSensor *self,
    int currentOrientation) {
  self->setCurrentOrientation(currentOrientation);
}

//  int QSensor::userOrientation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor15userOrientationEv(const QSensor *self) {
  return self->userOrientation();
}

//  void QSensor::setUserOrientation(int userOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor18setUserOrientationEi(
    QSensor *self,
    int userOrientation) {
  self->setUserOrientation(userOrientation);
}

//  int QSensor::maxBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor13maxBufferSizeEv(const QSensor *self) {
  return self->maxBufferSize();
}

//  void QSensor::setMaxBufferSize(int maxBufferSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor16setMaxBufferSizeEi(
    QSensor *self,
    int maxBufferSize) {
  self->setMaxBufferSize(maxBufferSize);
}

//  int QSensor::efficientBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor19efficientBufferSizeEv(const QSensor *self) {
  return self->efficientBufferSize();
}

//  void QSensor::setEfficientBufferSize(int efficientBufferSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor22setEfficientBufferSizeEi(
    QSensor *self,
    int efficientBufferSize) {
  self->setEfficientBufferSize(efficientBufferSize);
}

//  int QSensor::bufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSensor10bufferSizeEv(const QSensor *self) {
  return self->bufferSize();
}

//  void QSensor::setBufferSize(int bufferSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor13setBufferSizeEi(QSensor *self, int bufferSize) {
  self->setBufferSize(bufferSize);
}

//  bool QSensor::start()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QSensor5startEv(QSensor *self) {
  return self->start();
}

//  void QSensor::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor4stopEv(QSensor *self) {
  self->stop();
}

//  QSensorBackend *QSensor::backend() const
extern "C" Q_DECL_EXPORT
QSensorBackend *ritual_ZNK7QSensor7backendEv(const QSensor *self) {
  return self->backend();
}

//  void QSensor::registerInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSensor16registerInstanceEv(QSensor *self) {
  self->registerInstance();
}

//  QSensorPrivate *QSensor::d_func()
extern "C" Q_DECL_EXPORT
QSensorPrivate *ritual_ZN7QSensor6d_funcEv(QSensor *self) {
  return self->d_func();
}

//  const QSensorPrivate *QSensor::d_func() const
extern "C" Q_DECL_EXPORT
const QSensorPrivate *ritual_ZNK7QSensor6d_funcEv(const QSensor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSensor, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensor(QSensor *self, const char *key, void *call) {
  return static_cast<CuteQSensor *>(self)->take(key, call);
}
