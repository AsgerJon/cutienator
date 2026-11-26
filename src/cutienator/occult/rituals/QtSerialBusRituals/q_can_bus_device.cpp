//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbusdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbusdevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtSerialBus/qcanbusframe.h>
#include <QtSerialBus/qcanbusdeviceinfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtSerialBus/QCanBusDevice>

//  A QCanBusDevice that Python can take functions over in. Every QCanBusDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCanBusDeviceCall0)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQCanBusDeviceCall1)(const void *, const QCanBusFrame *, int *);
typedef void (*CuteQCanBusDeviceCall2)(const void *, int *);
typedef bool (*CuteQCanBusDeviceCall3)(const void *, int *);
typedef int (*CuteQCanBusDeviceCall4)(const void *, int *);
typedef bool (*CuteQCanBusDeviceCall5)(const void *, int, int *);
typedef bool (*CuteQCanBusDeviceCall6)(const void *, int, int *);
typedef QString * (*CuteQCanBusDeviceCall7)(const void *, const QCanBusFrame *, int *);
typedef const QCanBusDeviceInfo * (*CuteQCanBusDeviceCall8)(const void *, int *);
typedef bool (*CuteQCanBusDeviceCall9)(const void *, int *);
typedef void (*CuteQCanBusDeviceCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanBusDeviceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCanBusDeviceCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanBusDeviceCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanBusDeviceCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanBusDeviceCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanBusDeviceCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCanBusDeviceCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCanBusDevice : public QCanBusDevice {
public:
  using QCanBusDevice::QCanBusDevice;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QCanBusDevice25setConfigurationParameterENS_16ConfigurationKeyERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice10writeFrameERK12QCanBusFrame")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice15resetControllerEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QCanBusDevice12hasBusStatusEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice9busStatusEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice20waitForFramesWrittenEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice21waitForFramesReceivedEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice19interpretErrorFrameERK12QCanBusFrame")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QCanBusDevice10deviceInfoEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice4openEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QCanBusDevice5closeEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QCanBusDevice::setConfigurationParameter(ConfigurationKey key,
  //      const QVariant &value)
  void setConfigurationParameter(
      QCanBusDevice::ConfigurationKey key,
      const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanBusDeviceCall0 call = reinterpret_cast<CuteQCanBusDeviceCall0>(taken[0]);
      call(this, static_cast<int>(key), &value, &handled);
      if (handled) return;
    }
    QCanBusDevice::setConfigurationParameter(key, value);
  }

  //  bool QCanBusDevice::writeFrame(const QCanBusFrame &frame)
  bool writeFrame(const QCanBusFrame &frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanBusDeviceCall1 call = reinterpret_cast<CuteQCanBusDeviceCall1>(taken[1]);
      bool given = call(this, &frame, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QCanBusDevice::resetController()
  void resetController() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCanBusDeviceCall2 call = reinterpret_cast<CuteQCanBusDeviceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QCanBusDevice::resetController();
  }

  //  bool QCanBusDevice::hasBusStatus() const
  bool hasBusStatus() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQCanBusDeviceCall3 call = reinterpret_cast<CuteQCanBusDeviceCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCanBusDevice::hasBusStatus();
  }

  //  CanBusStatus QCanBusDevice::busStatus()
  QCanBusDevice::CanBusStatus busStatus() override {
    if (taken[4]) {
      int handled = 0;
      CuteQCanBusDeviceCall4 call = reinterpret_cast<CuteQCanBusDeviceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QCanBusDevice::CanBusStatus>(given);
    }
    return QCanBusDevice::busStatus();
  }

  //  bool QCanBusDevice::waitForFramesWritten(int msecs)
  bool waitForFramesWritten(int msecs) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCanBusDeviceCall5 call = reinterpret_cast<CuteQCanBusDeviceCall5>(taken[5]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QCanBusDevice::waitForFramesWritten(msecs);
  }

  //  bool QCanBusDevice::waitForFramesReceived(int msecs)
  bool waitForFramesReceived(int msecs) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCanBusDeviceCall6 call = reinterpret_cast<CuteQCanBusDeviceCall6>(taken[6]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QCanBusDevice::waitForFramesReceived(msecs);
  }

  //  QString QCanBusDevice::interpretErrorFrame(const QCanBusFrame
  //      &errorFrame)
  QString interpretErrorFrame(const QCanBusFrame &errorFrame) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCanBusDeviceCall7 call = reinterpret_cast<CuteQCanBusDeviceCall7>(taken[7]);
      QString * given = call(this, &errorFrame, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QCanBusDeviceInfo QCanBusDevice::deviceInfo() const
  QCanBusDeviceInfo deviceInfo() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCanBusDeviceCall8 call = reinterpret_cast<CuteQCanBusDeviceCall8>(taken[8]);
      const QCanBusDeviceInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QCanBusDevice::deviceInfo();
  }

  //  bool QCanBusDevice::open()
  bool open() override {
    if (taken[9]) {
      int handled = 0;
      CuteQCanBusDeviceCall9 call = reinterpret_cast<CuteQCanBusDeviceCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QCanBusDevice::close()
  void close() override {
    if (taken[10]) {
      int handled = 0;
      CuteQCanBusDeviceCall10 call = reinterpret_cast<CuteQCanBusDeviceCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCanBusDeviceCall11 call = reinterpret_cast<CuteQCanBusDeviceCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCanBusDeviceCall12 call = reinterpret_cast<CuteQCanBusDeviceCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCanBusDeviceCall13 call = reinterpret_cast<CuteQCanBusDeviceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCanBusDeviceCall14 call = reinterpret_cast<CuteQCanBusDeviceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCanBusDeviceCall15 call = reinterpret_cast<CuteQCanBusDeviceCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCanBusDeviceCall16 call = reinterpret_cast<CuteQCanBusDeviceCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCanBusDeviceCall17 call = reinterpret_cast<CuteQCanBusDeviceCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCanBusDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QCanBusDevice10metaObjectEv(
    const QCanBusDevice *self) {
  return self->metaObject();
}

//  void *QCanBusDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QCanBusDevice11qt_metacastEPKc(
    QCanBusDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCanBusDevice::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QCanBusDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    QCanBusDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCanBusDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCanBusDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCanBusDevice::tr(s, c, n));
}

//  QCanBusDevicePrivate *QCanBusDevice::d_func()
extern "C" Q_DECL_EXPORT
QCanBusDevicePrivate *ritual_ZN13QCanBusDevice6d_funcEv(
    QCanBusDevice *self) {
  return self->d_func();
}

//  const QCanBusDevicePrivate *QCanBusDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QCanBusDevicePrivate *ritual_ZNK13QCanBusDevice6d_funcEv(
    const QCanBusDevice *self) {
  return self->d_func();
}

//  QCanBusDevice::QCanBusDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QCanBusDevice *ritual_ZN13QCanBusDeviceC1EP7QObject(QObject *parent) {
  return new CuteQCanBusDevice(parent);
}

//  void QCanBusDevice::setConfigurationParameter(ConfigurationKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice25setConfigurationParameterENS_16ConfigurationKeyERK8QVariant(
    QCanBusDevice *self,
    QCanBusDevice::ConfigurationKey key,
    const QVariant *value) {
  self->setConfigurationParameter(key, *value);
}

//  QVariant QCanBusDevice::configurationParameter(ConfigurationKey key)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QCanBusDevice22configurationParameterENS_16ConfigurationKeyE(
    const QCanBusDevice *self,
    QCanBusDevice::ConfigurationKey key) {
  return new QVariant(self->configurationParameter(key));
}

//  QList<ConfigurationKey> QCanBusDevice::configurationKeys() const
extern "C" Q_DECL_EXPORT
QList<QCanBusDevice::ConfigurationKey> *ritual_ZNK13QCanBusDevice17configurationKeysEv(
    const QCanBusDevice *self) {
  return new QList<QCanBusDevice::ConfigurationKey>(
      self->configurationKeys());
}

//  bool QCanBusDevice::writeFrame(const QCanBusFrame &frame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QCanBusDevice10writeFrameERK12QCanBusFrame(
    QCanBusDevice *self,
    const QCanBusFrame *frame) {
  return self->writeFrame(*frame);
}

//  QCanBusFrame QCanBusDevice::readFrame()
extern "C" Q_DECL_EXPORT
QCanBusFrame *ritual_ZN13QCanBusDevice9readFrameEv(QCanBusDevice *self) {
  return new QCanBusFrame(self->readFrame());
}

//  QList<QCanBusFrame> QCanBusDevice::readAllFrames()
extern "C" Q_DECL_EXPORT
QList<QCanBusFrame> *ritual_ZN13QCanBusDevice13readAllFramesEv(
    QCanBusDevice *self) {
  return new QList<QCanBusFrame>(self->readAllFrames());
}

//  qint64 QCanBusDevice::framesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QCanBusDevice15framesAvailableEv(
    const QCanBusDevice *self) {
  return self->framesAvailable();
}

//  qint64 QCanBusDevice::framesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QCanBusDevice13framesToWriteEv(
    const QCanBusDevice *self) {
  return self->framesToWrite();
}

//  void QCanBusDevice::resetController()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice15resetControllerEv(QCanBusDevice *self) {
  self->resetController();
}

//  bool QCanBusDevice::hasBusStatus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCanBusDevice12hasBusStatusEv(const QCanBusDevice *self) {
  return self->hasBusStatus();
}

//  CanBusStatus QCanBusDevice::busStatus()
extern "C" Q_DECL_EXPORT
QCanBusDevice::CanBusStatus ritual_ZN13QCanBusDevice9busStatusEv(
    QCanBusDevice *self) {
  return self->busStatus();
}

//  void QCanBusDevice::clear(Directions direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice5clearE6QFlagsINS_9DirectionEE(
    QCanBusDevice *self,
    int direction) {
  self->clear(QFlags<QCanBusDevice::Direction>::fromInt(direction));
}

//  bool QCanBusDevice::waitForFramesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QCanBusDevice20waitForFramesWrittenEi(
    QCanBusDevice *self,
    int msecs) {
  return self->waitForFramesWritten(msecs);
}

//  bool QCanBusDevice::waitForFramesReceived(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QCanBusDevice21waitForFramesReceivedEi(
    QCanBusDevice *self,
    int msecs) {
  return self->waitForFramesReceived(msecs);
}

//  bool QCanBusDevice::connectDevice()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QCanBusDevice13connectDeviceEv(QCanBusDevice *self) {
  return self->connectDevice();
}

//  void QCanBusDevice::disconnectDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice16disconnectDeviceEv(QCanBusDevice *self) {
  self->disconnectDevice();
}

//  CanBusDeviceState QCanBusDevice::state() const
extern "C" Q_DECL_EXPORT
QCanBusDevice::CanBusDeviceState ritual_ZNK13QCanBusDevice5stateEv(
    const QCanBusDevice *self) {
  return self->state();
}

//  CanBusError QCanBusDevice::error() const
extern "C" Q_DECL_EXPORT
QCanBusDevice::CanBusError ritual_ZNK13QCanBusDevice5errorEv(
    const QCanBusDevice *self) {
  return self->error();
}

//  QString QCanBusDevice::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCanBusDevice11errorStringEv(
    const QCanBusDevice *self) {
  return new QString(self->errorString());
}

//  QString QCanBusDevice::interpretErrorFrame(const QCanBusFrame
//      &errorFrame)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCanBusDevice19interpretErrorFrameERK12QCanBusFrame(
    QCanBusDevice *self,
    const QCanBusFrame *errorFrame) {
  return new QString(self->interpretErrorFrame(*errorFrame));
}

//  QCanBusDeviceInfo QCanBusDevice::deviceInfo() const
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfo *ritual_ZNK13QCanBusDevice10deviceInfoEv(
    const QCanBusDevice *self) {
  return new QCanBusDeviceInfo(self->deviceInfo());
}

//  void QCanBusDevice::errorOccurred(QCanBusDevice::CanBusError a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice13errorOccurredENS_11CanBusErrorE(
    QCanBusDevice *self,
    QCanBusDevice::CanBusError a0) {
  self->errorOccurred(a0);
}

//  void QCanBusDevice::framesReceived()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice14framesReceivedEv(QCanBusDevice *self) {
  self->framesReceived();
}

//  void QCanBusDevice::framesWritten(qint64 framesCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice13framesWrittenEx(
    QCanBusDevice *self,
    qint64 framesCount) {
  self->framesWritten(framesCount);
}

//  void QCanBusDevice::stateChanged(QCanBusDevice::CanBusDeviceState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice12stateChangedENS_17CanBusDeviceStateE(
    QCanBusDevice *self,
    QCanBusDevice::CanBusDeviceState state) {
  self->stateChanged(state);
}

//  void QCanBusDevice::setState(QCanBusDevice::CanBusDeviceState newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice8setStateENS_17CanBusDeviceStateE(
    QCanBusDevice *self,
    QCanBusDevice::CanBusDeviceState newState) {
  self->setState(newState);
}

//  void QCanBusDevice::setError(const QString &errorText,
//      QCanBusDevice::CanBusError a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice8setErrorERK7QStringNS_11CanBusErrorE(
    QCanBusDevice *self,
    const QString *errorText,
    QCanBusDevice::CanBusError a1) {
  self->setError(*errorText, a1);
}

//  void QCanBusDevice::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice10clearErrorEv(QCanBusDevice *self) {
  self->clearError();
}

//  void QCanBusDevice::enqueueReceivedFrames(const QList<QCanBusFrame>
//      &newFrames)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice21enqueueReceivedFramesERK5QListI12QCanBusFrameE(
    QCanBusDevice *self,
    const QList<QCanBusFrame> *newFrames) {
  self->enqueueReceivedFrames(*newFrames);
}

//  void QCanBusDevice::enqueueOutgoingFrame(const QCanBusFrame &newFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice20enqueueOutgoingFrameERK12QCanBusFrame(
    QCanBusDevice *self,
    const QCanBusFrame *newFrame) {
  self->enqueueOutgoingFrame(*newFrame);
}

//  QCanBusFrame QCanBusDevice::dequeueOutgoingFrame()
extern "C" Q_DECL_EXPORT
QCanBusFrame *ritual_ZN13QCanBusDevice20dequeueOutgoingFrameEv(
    QCanBusDevice *self) {
  return new QCanBusFrame(self->dequeueOutgoingFrame());
}

//  bool QCanBusDevice::hasOutgoingFrames() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCanBusDevice17hasOutgoingFramesEv(
    const QCanBusDevice *self) {
  return self->hasOutgoingFrames();
}

//  bool QCanBusDevice::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QCanBusDevice4openEv(QCanBusDevice *self) {
  return self->open();
}

//  void QCanBusDevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCanBusDevice5closeEv(QCanBusDevice *self) {
  self->close();
}

//  QCanBusDeviceInfo QCanBusDevice::createDeviceInfo(const QString &plugin,
//      const QString &name, bool isVirtual, bool isFlexibleDataRateCapable)
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfo *ritual_ZN13QCanBusDevice16createDeviceInfoERK7QStringS2_bb(
    const QString *plugin,
    const QString *name,
    bool isVirtual,
    bool isFlexibleDataRateCapable) {
  return new QCanBusDeviceInfo(
      QCanBusDevice::createDeviceInfo(
          *plugin,
          *name,
          isVirtual,
          isFlexibleDataRateCapable));
}

//  QCanBusDeviceInfo QCanBusDevice::createDeviceInfo(const QString &plugin,
//      const QString &name, const QString &serialNumber, const QString
//      &description, const QString &alias, int channel, bool isVirtual, bool
//      isFlexibleDataRateCapable)
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfo *ritual_ZN13QCanBusDevice16createDeviceInfoERK7QStringS2_S2_S2_S2_ibb(
    const QString *plugin,
    const QString *name,
    const QString *serialNumber,
    const QString *description,
    const QString *alias,
    int channel,
    bool isVirtual,
    bool isFlexibleDataRateCapable) {
  return new QCanBusDeviceInfo(
      QCanBusDevice::createDeviceInfo(
          *plugin,
          *name,
          *serialNumber,
          *description,
          *alias,
          channel,
          isVirtual,
          isFlexibleDataRateCapable));
}

//  a Python function taken by a CuteQCanBusDevice, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanBusDevice(
    QCanBusDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanBusDevice *>(self)->take(key, call);
}

//  void QCanBusDevice::setConfigurationParameter(ConfigurationKey key, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QCanBusDevice25setConfigurationParameterENS_16ConfigurationKeyERK8QVariant(
    QCanBusDevice *self,
    QCanBusDevice::ConfigurationKey key,
    const QVariant *value) {
  self->QCanBusDevice::setConfigurationParameter(key, *value);
}

//  void QCanBusDevice::resetController()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QCanBusDevice15resetControllerEv(QCanBusDevice *self) {
  self->QCanBusDevice::resetController();
}

//  bool QCanBusDevice::hasBusStatus() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QCanBusDevice12hasBusStatusEv(
    const QCanBusDevice *self) {
  return self->QCanBusDevice::hasBusStatus();
}

//  CanBusStatus QCanBusDevice::busStatus()
extern "C" Q_DECL_EXPORT
QCanBusDevice::CanBusStatus ritual_own_ZN13QCanBusDevice9busStatusEv(
    QCanBusDevice *self) {
  return self->QCanBusDevice::busStatus();
}

//  bool QCanBusDevice::waitForFramesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QCanBusDevice20waitForFramesWrittenEi(
    QCanBusDevice *self,
    int msecs) {
  return self->QCanBusDevice::waitForFramesWritten(msecs);
}

//  bool QCanBusDevice::waitForFramesReceived(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QCanBusDevice21waitForFramesReceivedEi(
    QCanBusDevice *self,
    int msecs) {
  return self->QCanBusDevice::waitForFramesReceived(msecs);
}

//  QCanBusDeviceInfo QCanBusDevice::deviceInfo() const
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfo *ritual_own_ZNK13QCanBusDevice10deviceInfoEv(
    const QCanBusDevice *self) {
  return new QCanBusDeviceInfo(self->QCanBusDevice::deviceInfo());
}

//  a QList<QCanBusDevice::ConfigurationKey> a ritual of QCanBusDevice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCanBusDevice__QList_QCanBusDevice_ConfigurationKey(
    QList<QCanBusDevice::ConfigurationKey> *self) {
  delete self;
}
