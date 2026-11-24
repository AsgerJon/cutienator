//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialPort/qserialport.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialPort/qserialport.h>
#include <QtCore/qstring.h>
#include <QtSerialPort/qserialportinfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSerialPort that Python can take functions over in. Every QSerialPort
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSerialPortCall0)(const void *, int, int *);
typedef void (*CuteQSerialPortCall1)(const void *, int *);
typedef bool (*CuteQSerialPortCall2)(const void *, int *);
typedef qint64 (*CuteQSerialPortCall3)(const void *, int *);
typedef qint64 (*CuteQSerialPortCall4)(const void *, int *);
typedef bool (*CuteQSerialPortCall5)(const void *, int *);
typedef bool (*CuteQSerialPortCall6)(const void *, int, int *);
typedef bool (*CuteQSerialPortCall7)(const void *, int, int *);
typedef qint64 (*CuteQSerialPortCall8)(const void *, int *);
typedef qint64 (*CuteQSerialPortCall9)(const void *, int *);
typedef bool (*CuteQSerialPortCall10)(const void *, qint64, int *);
typedef bool (*CuteQSerialPortCall11)(const void *, int *);
typedef bool (*CuteQSerialPortCall12)(const void *, int *);
typedef qint64 (*CuteQSerialPortCall13)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSerialPortCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSerialPortCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSerialPortCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSerialPortCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSerialPortCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSerialPortCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSerialPortCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSerialPort : public QSerialPort {
public:
  using QSerialPort::QSerialPort;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QSerialPort::open(OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSerialPortCall0 call = reinterpret_cast<CuteQSerialPortCall0>(taken[0]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QSerialPort::open(mode);
  }

  //  void QSerialPort::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSerialPortCall1 call = reinterpret_cast<CuteQSerialPortCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSerialPort::close();
  }

  //  bool QSerialPort::isSequential() const
  bool isSequential() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSerialPortCall2 call = reinterpret_cast<CuteQSerialPortCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSerialPort::isSequential();
  }

  //  qint64 QSerialPort::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSerialPortCall3 call = reinterpret_cast<CuteQSerialPortCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSerialPort::bytesAvailable();
  }

  //  qint64 QSerialPort::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSerialPortCall4 call = reinterpret_cast<CuteQSerialPortCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSerialPort::bytesToWrite();
  }

  //  bool QSerialPort::canReadLine() const
  bool canReadLine() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSerialPortCall5 call = reinterpret_cast<CuteQSerialPortCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSerialPort::canReadLine();
  }

  //  bool QSerialPort::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSerialPortCall6 call = reinterpret_cast<CuteQSerialPortCall6>(taken[6]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QSerialPort::waitForReadyRead(msecs);
  }

  //  bool QSerialPort::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSerialPortCall7 call = reinterpret_cast<CuteQSerialPortCall7>(taken[7]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QSerialPort::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSerialPortCall8 call = reinterpret_cast<CuteQSerialPortCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSerialPortCall9 call = reinterpret_cast<CuteQSerialPortCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSerialPortCall10 call = reinterpret_cast<CuteQSerialPortCall10>(taken[10]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSerialPortCall11 call = reinterpret_cast<CuteQSerialPortCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSerialPortCall12 call = reinterpret_cast<CuteQSerialPortCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSerialPortCall13 call = reinterpret_cast<CuteQSerialPortCall13>(taken[13]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSerialPortCall14 call = reinterpret_cast<CuteQSerialPortCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSerialPortCall15 call = reinterpret_cast<CuteQSerialPortCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSerialPortCall16 call = reinterpret_cast<CuteQSerialPortCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSerialPortCall17 call = reinterpret_cast<CuteQSerialPortCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSerialPortCall18 call = reinterpret_cast<CuteQSerialPortCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSerialPortCall19 call = reinterpret_cast<CuteQSerialPortCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSerialPortCall20 call = reinterpret_cast<CuteQSerialPortCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSerialPort::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QSerialPort10metaObjectEv(
    const QSerialPort *self) {
  return self->metaObject();
}

//  QString QSerialPort::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QSerialPort2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSerialPort::tr(s, c, n));
}

//  QSerialPortPrivate *QSerialPort::d_func()
extern "C" Q_DECL_EXPORT
QSerialPortPrivate *ritual_ZN11QSerialPort6d_funcEv(QSerialPort *self) {
  return self->d_func();
}

//  const QSerialPortPrivate *QSerialPort::d_func() const
extern "C" Q_DECL_EXPORT
const QSerialPortPrivate *ritual_ZNK11QSerialPort6d_funcEv(
    const QSerialPort *self) {
  return self->d_func();
}

//  QSerialPort::QSerialPort(QObject *parent)
extern "C" Q_DECL_EXPORT
QSerialPort *ritual_ZN11QSerialPortC1EP7QObject(QObject *parent) {
  return new CuteQSerialPort(parent);
}

//  QSerialPort::QSerialPort(const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QSerialPort *ritual_ZN11QSerialPortC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new CuteQSerialPort(*name, parent);
}

//  QSerialPort::QSerialPort(const QSerialPortInfo &info, QObject *parent)
extern "C" Q_DECL_EXPORT
QSerialPort *ritual_ZN11QSerialPortC1ERK15QSerialPortInfoP7QObject(
    const QSerialPortInfo *info,
    QObject *parent) {
  return new CuteQSerialPort(*info, parent);
}

//  QSerialPort::~QSerialPort()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPortD1Ev(QSerialPort *self) {
  delete self;
}

//  void QSerialPort::setPortName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort11setPortNameERK7QString(
    QSerialPort *self,
    const QString *name) {
  self->setPortName(*name);
}

//  QString QSerialPort::portName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QSerialPort8portNameEv(const QSerialPort *self) {
  return new QString(self->portName());
}

//  void QSerialPort::setPort(const QSerialPortInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort7setPortERK15QSerialPortInfo(
    QSerialPort *self,
    const QSerialPortInfo *info) {
  self->setPort(*info);
}

//  bool QSerialPort::open(OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSerialPort *self,
    int mode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QSerialPort::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort5closeEv(QSerialPort *self) {
  self->close();
}

//  bool QSerialPort::setBaudRate(qint32 baudRate, Directions directions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort11setBaudRateEi6QFlagsINS_9DirectionEE(
    QSerialPort *self,
    qint32 baudRate,
    int directions) {
  return self->setBaudRate(
      baudRate,
      QFlags<QSerialPort::Direction>::fromInt(directions));
}

//  qint32 QSerialPort::baudRate(Directions directions) const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK11QSerialPort8baudRateE6QFlagsINS_9DirectionEE(
    const QSerialPort *self,
    int directions) {
  return self->baudRate(QFlags<QSerialPort::Direction>::fromInt(directions));
}

//  bool QSerialPort::setDataBits(DataBits dataBits)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort11setDataBitsENS_8DataBitsE(
    QSerialPort *self,
    QSerialPort::DataBits dataBits) {
  return self->setDataBits(dataBits);
}

//  DataBits QSerialPort::dataBits() const
extern "C" Q_DECL_EXPORT
QSerialPort::DataBits ritual_ZNK11QSerialPort8dataBitsEv(
    const QSerialPort *self) {
  return self->dataBits();
}

//  bool QSerialPort::setParity(Parity parity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort9setParityENS_6ParityE(
    QSerialPort *self,
    QSerialPort::Parity parity) {
  return self->setParity(parity);
}

//  Parity QSerialPort::parity() const
extern "C" Q_DECL_EXPORT
QSerialPort::Parity ritual_ZNK11QSerialPort6parityEv(
    const QSerialPort *self) {
  return self->parity();
}

//  bool QSerialPort::setStopBits(StopBits stopBits)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort11setStopBitsENS_8StopBitsE(
    QSerialPort *self,
    QSerialPort::StopBits stopBits) {
  return self->setStopBits(stopBits);
}

//  StopBits QSerialPort::stopBits() const
extern "C" Q_DECL_EXPORT
QSerialPort::StopBits ritual_ZNK11QSerialPort8stopBitsEv(
    const QSerialPort *self) {
  return self->stopBits();
}

//  bool QSerialPort::setFlowControl(FlowControl flowControl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort14setFlowControlENS_11FlowControlE(
    QSerialPort *self,
    QSerialPort::FlowControl flowControl) {
  return self->setFlowControl(flowControl);
}

//  FlowControl QSerialPort::flowControl() const
extern "C" Q_DECL_EXPORT
QSerialPort::FlowControl ritual_ZNK11QSerialPort11flowControlEv(
    const QSerialPort *self) {
  return self->flowControl();
}

//  bool QSerialPort::setDataTerminalReady(bool set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort20setDataTerminalReadyEb(
    QSerialPort *self,
    bool set) {
  return self->setDataTerminalReady(set);
}

//  bool QSerialPort::isDataTerminalReady()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort19isDataTerminalReadyEv(QSerialPort *self) {
  return self->isDataTerminalReady();
}

//  bool QSerialPort::setRequestToSend(bool set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort16setRequestToSendEb(
    QSerialPort *self,
    bool set) {
  return self->setRequestToSend(set);
}

//  bool QSerialPort::isRequestToSend()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort15isRequestToSendEv(QSerialPort *self) {
  return self->isRequestToSend();
}

//  PinoutSignals QSerialPort::pinoutSignals()
extern "C" Q_DECL_EXPORT
int ritual_ZN11QSerialPort13pinoutSignalsEv(QSerialPort *self) {
  return static_cast<int>(self->pinoutSignals().toInt());
}

//  bool QSerialPort::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort5flushEv(QSerialPort *self) {
  return self->flush();
}

//  bool QSerialPort::clear(Directions directions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort5clearE6QFlagsINS_9DirectionEE(
    QSerialPort *self,
    int directions) {
  return self->clear(QFlags<QSerialPort::Direction>::fromInt(directions));
}

//  SerialPortError QSerialPort::error() const
extern "C" Q_DECL_EXPORT
QSerialPort::SerialPortError ritual_ZNK11QSerialPort5errorEv(
    const QSerialPort *self) {
  return self->error();
}

//  void QSerialPort::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort10clearErrorEv(QSerialPort *self) {
  self->clearError();
}

//  qint64 QSerialPort::readBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QSerialPort14readBufferSizeEv(const QSerialPort *self) {
  return self->readBufferSize();
}

//  void QSerialPort::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort17setReadBufferSizeEx(
    QSerialPort *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  qint64 QSerialPort::writeBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QSerialPort15writeBufferSizeEv(const QSerialPort *self) {
  return self->writeBufferSize();
}

//  void QSerialPort::setWriteBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort18setWriteBufferSizeEx(
    QSerialPort *self,
    qint64 size) {
  self->setWriteBufferSize(size);
}

//  bool QSerialPort::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSerialPort12isSequentialEv(const QSerialPort *self) {
  return self->isSequential();
}

//  qint64 QSerialPort::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QSerialPort14bytesAvailableEv(const QSerialPort *self) {
  return self->bytesAvailable();
}

//  qint64 QSerialPort::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QSerialPort12bytesToWriteEv(const QSerialPort *self) {
  return self->bytesToWrite();
}

//  bool QSerialPort::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSerialPort11canReadLineEv(const QSerialPort *self) {
  return self->canReadLine();
}

//  bool QSerialPort::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort16waitForReadyReadEi(
    QSerialPort *self,
    int msecs) {
  return self->waitForReadyRead(msecs);
}

//  bool QSerialPort::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort19waitForBytesWrittenEi(
    QSerialPort *self,
    int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QSerialPort::setBreakEnabled(bool set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSerialPort15setBreakEnabledEb(QSerialPort *self, bool set) {
  return self->setBreakEnabled(set);
}

//  bool QSerialPort::isBreakEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSerialPort14isBreakEnabledEv(const QSerialPort *self) {
  return self->isBreakEnabled();
}

//  bool QSerialPort::settingsRestoredOnClose() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSerialPort23settingsRestoredOnCloseEv(
    const QSerialPort *self) {
  return self->settingsRestoredOnClose();
}

//  void QSerialPort::setSettingsRestoredOnClose(bool restore)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSerialPort26setSettingsRestoredOnCloseEb(
    QSerialPort *self,
    bool restore) {
  self->setSettingsRestoredOnClose(restore);
}

//  Handle QSerialPort::handle() const
extern "C" Q_DECL_EXPORT
QSerialPort::Handle ritual_ZNK11QSerialPort6handleEv(
    const QSerialPort *self) {
  return self->handle();
}

//  qint64 QSerialPort::writeData(const char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QSerialPort9writeDataEPKcx(
    QSerialPort *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  a Python function taken by a CuteQSerialPort, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSerialPort(
    QSerialPort *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSerialPort *>(self)->take(key, call);
}

//  bool QSerialPort::open(OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSerialPort4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSerialPort *self,
    int mode) {
  return self->QSerialPort::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QSerialPort::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSerialPort5closeEv(QSerialPort *self) {
  self->QSerialPort::close();
}

//  bool QSerialPort::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSerialPort12isSequentialEv(const QSerialPort *self) {
  return self->QSerialPort::isSequential();
}

//  qint64 QSerialPort::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK11QSerialPort14bytesAvailableEv(
    const QSerialPort *self) {
  return self->QSerialPort::bytesAvailable();
}

//  qint64 QSerialPort::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK11QSerialPort12bytesToWriteEv(const QSerialPort *self) {
  return self->QSerialPort::bytesToWrite();
}

//  bool QSerialPort::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSerialPort11canReadLineEv(const QSerialPort *self) {
  return self->QSerialPort::canReadLine();
}

//  bool QSerialPort::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSerialPort16waitForReadyReadEi(
    QSerialPort *self,
    int msecs) {
  return self->QSerialPort::waitForReadyRead(msecs);
}

//  bool QSerialPort::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QSerialPort19waitForBytesWrittenEi(
    QSerialPort *self,
    int msecs) {
  return self->QSerialPort::waitForBytesWritten(msecs);
}
