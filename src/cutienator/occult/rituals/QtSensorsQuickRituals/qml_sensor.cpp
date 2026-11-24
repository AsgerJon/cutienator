//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlSensor that Python can take functions over in. Every QmlSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlSensorCall0)(const void *, int *);
typedef void (*CuteQmlSensorCall1)(const void *, int *);
typedef void * (*CuteQmlSensorCall2)(const void *, int *);
typedef void (*CuteQmlSensorCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlSensor : public QmlSensor {
public:
  using QmlSensor::QmlSensor;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QmlSensor6sensorEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QmlSensor13createReadingEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSensor *QmlSensor::sensor() const
  QSensor *sensor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlSensorCall0 call = reinterpret_cast<CuteQmlSensorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensor *>(given);
    }
    return {};
  }

  //  void QmlSensor::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlSensorCall1 call = reinterpret_cast<CuteQmlSensorCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::componentComplete();
  }

  //  QmlSensorReading *QmlSensor::createReading() const
  QmlSensorReading *createReading() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlSensorCall2 call = reinterpret_cast<CuteQmlSensorCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QmlSensorReading *>(given);
    }
    return {};
  }

  //  void QmlSensor::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlSensorCall3 call = reinterpret_cast<CuteQmlSensorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQmlSensorCall4 call = reinterpret_cast<CuteQmlSensorCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQmlSensorCall5 call = reinterpret_cast<CuteQmlSensorCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQmlSensorCall6 call = reinterpret_cast<CuteQmlSensorCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQmlSensorCall7 call = reinterpret_cast<CuteQmlSensorCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQmlSensorCall8 call = reinterpret_cast<CuteQmlSensorCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQmlSensorCall9 call = reinterpret_cast<CuteQmlSensorCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQmlSensorCall10 call = reinterpret_cast<CuteQmlSensorCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QmlSensor10metaObjectEv(
    const QmlSensor *self) {
  return self->metaObject();
}

//  QString QmlSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QmlSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlSensor::tr(s, c, n));
}

//  void QmlSensor::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor24qt_qmlMarker_uncreatableEv(QmlSensor *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlSensor::~QmlSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensorD1Ev(QmlSensor *self) {
  delete self;
}

//  QByteArray QmlSensor::identifier() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QmlSensor10identifierEv(const QmlSensor *self) {
  return new QByteArray(self->identifier());
}

//  void QmlSensor::setIdentifier(const QByteArray &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor13setIdentifierERK10QByteArray(
    QmlSensor *self,
    const QByteArray *identifier) {
  self->setIdentifier(*identifier);
}

//  QByteArray QmlSensor::type() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QmlSensor4typeEv(const QmlSensor *self) {
  return new QByteArray(self->type());
}

//  bool QmlSensor::isConnectedToBackend() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QmlSensor20isConnectedToBackendEv(const QmlSensor *self) {
  return self->isConnectedToBackend();
}

//  bool QmlSensor::isBusy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QmlSensor6isBusyEv(const QmlSensor *self) {
  return self->isBusy();
}

//  void QmlSensor::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor9setActiveEb(QmlSensor *self, bool active) {
  self->setActive(active);
}

//  bool QmlSensor::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QmlSensor8isActiveEv(const QmlSensor *self) {
  return self->isActive();
}

//  bool QmlSensor::isAlwaysOn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QmlSensor10isAlwaysOnEv(const QmlSensor *self) {
  return self->isAlwaysOn();
}

//  void QmlSensor::setAlwaysOn(bool alwaysOn)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor11setAlwaysOnEb(QmlSensor *self, bool alwaysOn) {
  self->setAlwaysOn(alwaysOn);
}

//  bool QmlSensor::skipDuplicates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QmlSensor14skipDuplicatesEv(const QmlSensor *self) {
  return self->skipDuplicates();
}

//  void QmlSensor::setSkipDuplicates(bool skipDuplicates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor17setSkipDuplicatesEb(
    QmlSensor *self,
    bool skipDuplicates) {
  self->setSkipDuplicates(skipDuplicates);
}

//  int QmlSensor::dataRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor8dataRateEv(const QmlSensor *self) {
  return self->dataRate();
}

//  void QmlSensor::setDataRate(int rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor11setDataRateEi(QmlSensor *self, int rate) {
  self->setDataRate(rate);
}

//  int QmlSensor::outputRange() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor11outputRangeEv(const QmlSensor *self) {
  return self->outputRange();
}

//  void QmlSensor::setOutputRange(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor14setOutputRangeEi(QmlSensor *self, int index) {
  self->setOutputRange(index);
}

//  QString QmlSensor::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QmlSensor11descriptionEv(const QmlSensor *self) {
  return new QString(self->description());
}

//  int QmlSensor::error() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor5errorEv(const QmlSensor *self) {
  return self->error();
}

//  QmlSensorReading *QmlSensor::reading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK9QmlSensor7readingEv(const QmlSensor *self) {
  return self->reading();
}

//  bool QmlSensor::isFeatureSupported(Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QmlSensor18isFeatureSupportedENS_7FeatureE(
    const QmlSensor *self,
    QmlSensor::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  AxesOrientationMode QmlSensor::axesOrientationMode() const
extern "C" Q_DECL_EXPORT
QmlSensor::AxesOrientationMode ritual_ZNK9QmlSensor19axesOrientationModeEv(
    const QmlSensor *self) {
  return self->axesOrientationMode();
}

//  void QmlSensor::setAxesOrientationMode(AxesOrientationMode
//      axesOrientationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor22setAxesOrientationModeENS_19AxesOrientationModeE(
    QmlSensor *self,
    QmlSensor::AxesOrientationMode axesOrientationMode) {
  self->setAxesOrientationMode(axesOrientationMode);
}

//  int QmlSensor::currentOrientation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor18currentOrientationEv(const QmlSensor *self) {
  return self->currentOrientation();
}

//  int QmlSensor::userOrientation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor15userOrientationEv(const QmlSensor *self) {
  return self->userOrientation();
}

//  void QmlSensor::setUserOrientation(int userOrientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor18setUserOrientationEi(
    QmlSensor *self,
    int userOrientation) {
  self->setUserOrientation(userOrientation);
}

//  int QmlSensor::maxBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor13maxBufferSizeEv(const QmlSensor *self) {
  return self->maxBufferSize();
}

//  int QmlSensor::efficientBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor19efficientBufferSizeEv(const QmlSensor *self) {
  return self->efficientBufferSize();
}

//  int QmlSensor::bufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QmlSensor10bufferSizeEv(const QmlSensor *self) {
  return self->bufferSize();
}

//  void QmlSensor::setBufferSize(int bufferSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor13setBufferSizeEi(QmlSensor *self, int bufferSize) {
  self->setBufferSize(bufferSize);
}

//  QSensor *QmlSensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK9QmlSensor6sensorEv(const QmlSensor *self) {
  return self->sensor();
}

//  void QmlSensor::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor17componentCompleteEv(QmlSensor *self) {
  self->componentComplete();
}

//  bool QmlSensor::start()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QmlSensor5startEv(QmlSensor *self) {
  return self->start();
}

//  void QmlSensor::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor4stopEv(QmlSensor *self) {
  self->stop();
}

//  QmlSensorReading *QmlSensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK9QmlSensor13createReadingEv(
    const QmlSensor *self) {
  return self->createReading();
}

//  void QmlSensor::updateReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor13updateReadingEv(QmlSensor *self) {
  self->updateReading();
}

//  void QmlSensor::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QmlSensor10classBeginEv(QmlSensor *self) {
  self->classBegin();
}

//  QmlSensor as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QmlSensor_QQmlParserStatus(QmlSensor *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQmlSensor, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlSensor(QmlSensor *self, const char *key, void *call) {
  return static_cast<CuteQmlSensor *>(self)->take(key, call);
}

//  void QmlSensor::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QmlSensor17componentCompleteEv(QmlSensor *self) {
  self->QmlSensor::componentComplete();
}

//  void QmlSensor::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QmlSensor10classBeginEv(QmlSensor *self) {
  self->QmlSensor::classBegin();
}
