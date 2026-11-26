//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnection_qnx_qiodevices.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#if defined(Q_OS_QNX)
#include <QtRemoteObjects/QtRemoteObjects>
#include <QtRemoteObjects/qconnection_qnx_qiodevices.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QIOQnxSource may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQIOQnxSource : QIOQnxSource {
  using QIOQnxSource::readData;
  using QIOQnxSource::open;
};

//  A QIOQnxSource that Python can take functions over in. Every QIOQnxSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQIOQnxSourceCall0)(const void *, int *);
typedef qint64 (*CuteQIOQnxSourceCall1)(const void *, int *);
typedef qint64 (*CuteQIOQnxSourceCall2)(const void *, int *);
typedef void (*CuteQIOQnxSourceCall3)(const void *, int *);
typedef bool (*CuteQIOQnxSourceCall4)(const void *, int, int *);
typedef bool (*CuteQIOQnxSourceCall5)(const void *, int, int *);
typedef qint64 (*CuteQIOQnxSourceCall6)(const void *, char *, qint64, int *);
typedef bool (*CuteQIOQnxSourceCall7)(const void *, int, int *);
typedef qint64 (*CuteQIOQnxSourceCall8)(const void *, int *);
typedef qint64 (*CuteQIOQnxSourceCall9)(const void *, int *);
typedef bool (*CuteQIOQnxSourceCall10)(const void *, qint64, int *);
typedef bool (*CuteQIOQnxSourceCall11)(const void *, int *);
typedef bool (*CuteQIOQnxSourceCall12)(const void *, int *);
typedef bool (*CuteQIOQnxSourceCall13)(const void *, int *);
typedef qint64 (*CuteQIOQnxSourceCall14)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQIOQnxSourceCall15)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIOQnxSourceCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIOQnxSourceCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOQnxSourceCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOQnxSourceCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOQnxSourceCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOQnxSourceCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIOQnxSourceCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQIOQnxSource : public QIOQnxSource {
public:
  using QIOQnxSource::QIOQnxSource;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
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
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QIOQnxSource::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIOQnxSourceCall0 call = reinterpret_cast<CuteQIOQnxSourceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIOQnxSource::isSequential();
  }

  //  qint64 QIOQnxSource::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIOQnxSourceCall1 call = reinterpret_cast<CuteQIOQnxSourceCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIOQnxSource::bytesAvailable();
  }

  //  qint64 QIOQnxSource::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQIOQnxSourceCall2 call = reinterpret_cast<CuteQIOQnxSourceCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIOQnxSource::bytesToWrite();
  }

  //  void QIOQnxSource::close()
  void close() override {
    if (taken[3]) {
      int handled = 0;
      CuteQIOQnxSourceCall3 call = reinterpret_cast<CuteQIOQnxSourceCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QIOQnxSource::close();
  }

  //  bool QIOQnxSource::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[4]) {
      int handled = 0;
      CuteQIOQnxSourceCall4 call = reinterpret_cast<CuteQIOQnxSourceCall4>(taken[4]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIOQnxSource::waitForBytesWritten(msecs);
  }

  //  bool QIOQnxSource::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[5]) {
      int handled = 0;
      CuteQIOQnxSourceCall5 call = reinterpret_cast<CuteQIOQnxSourceCall5>(taken[5]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIOQnxSource::waitForReadyRead(msecs);
  }

  //  qint64 QIOQnxSource::readData(char *a0, qint64 a1)
  qint64 readData(char *a0, qint64 a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQIOQnxSourceCall6 call = reinterpret_cast<CuteQIOQnxSourceCall6>(taken[6]);
      qint64 given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QIOQnxSource::readData(a0, a1);
  }

  //  bool QIOQnxSource::open(OpenMode openMode)
  bool open(QIODeviceBase::OpenMode openMode) override {
    if (taken[7]) {
      int handled = 0;
      CuteQIOQnxSourceCall7 call = reinterpret_cast<CuteQIOQnxSourceCall7>(taken[7]);
      bool given = call(this, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return QIOQnxSource::open(openMode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQIOQnxSourceCall8 call = reinterpret_cast<CuteQIOQnxSourceCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQIOQnxSourceCall9 call = reinterpret_cast<CuteQIOQnxSourceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQIOQnxSourceCall10 call = reinterpret_cast<CuteQIOQnxSourceCall10>(taken[10]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQIOQnxSourceCall11 call = reinterpret_cast<CuteQIOQnxSourceCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[12]) {
      int handled = 0;
      CuteQIOQnxSourceCall12 call = reinterpret_cast<CuteQIOQnxSourceCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQIOQnxSourceCall13 call = reinterpret_cast<CuteQIOQnxSourceCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[14]) {
      int handled = 0;
      CuteQIOQnxSourceCall14 call = reinterpret_cast<CuteQIOQnxSourceCall14>(taken[14]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[15]) {
      int handled = 0;
      CuteQIOQnxSourceCall15 call = reinterpret_cast<CuteQIOQnxSourceCall15>(taken[15]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQIOQnxSourceCall16 call = reinterpret_cast<CuteQIOQnxSourceCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQIOQnxSourceCall17 call = reinterpret_cast<CuteQIOQnxSourceCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQIOQnxSourceCall18 call = reinterpret_cast<CuteQIOQnxSourceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQIOQnxSourceCall19 call = reinterpret_cast<CuteQIOQnxSourceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQIOQnxSourceCall20 call = reinterpret_cast<CuteQIOQnxSourceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQIOQnxSourceCall21 call = reinterpret_cast<CuteQIOQnxSourceCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQIOQnxSourceCall22 call = reinterpret_cast<CuteQIOQnxSourceCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QIOQnxSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QIOQnxSource10metaObjectEv(
    const QIOQnxSource *self) {
  return self->metaObject();
}

//  void *QIOQnxSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QIOQnxSource11qt_metacastEPKc(
    QIOQnxSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QIOQnxSource::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QIOQnxSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QIOQnxSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QIOQnxSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QIOQnxSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIOQnxSource::tr(s, c, n));
}

//  QIOQnxSourcePrivate *QIOQnxSource::d_func()
extern "C" Q_DECL_EXPORT
QIOQnxSourcePrivate *ritual_ZN12QIOQnxSource6d_funcEv(QIOQnxSource *self) {
  return self->d_func();
}

//  const QIOQnxSourcePrivate *QIOQnxSource::d_func() const
extern "C" Q_DECL_EXPORT
const QIOQnxSourcePrivate *ritual_ZNK12QIOQnxSource6d_funcEv(
    const QIOQnxSource *self) {
  return self->d_func();
}

//  QIOQnxSource::QIOQnxSource(int rcvid, QObject *parent)
extern "C" Q_DECL_EXPORT
QIOQnxSource *ritual_ZN12QIOQnxSourceC1EiP7QObject(
    int rcvid,
    QObject *parent) {
  return new CuteQIOQnxSource(rcvid, parent);
}

//  QIOQnxSource::~QIOQnxSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOQnxSourceD1Ev(QIOQnxSource *self) {
  delete self;
}

//  bool QIOQnxSource::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QIOQnxSource12isSequentialEv(const QIOQnxSource *self) {
  return self->isSequential();
}

//  qint64 QIOQnxSource::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QIOQnxSource14bytesAvailableEv(const QIOQnxSource *self) {
  return self->bytesAvailable();
}

//  qint64 QIOQnxSource::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QIOQnxSource12bytesToWriteEv(const QIOQnxSource *self) {
  return self->bytesToWrite();
}

//  void QIOQnxSource::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOQnxSource5closeEv(QIOQnxSource *self) {
  self->close();
}

//  QAbstractSocket::SocketState QIOQnxSource::state() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketState ritual_ZNK12QIOQnxSource5stateEv(
    const QIOQnxSource *self) {
  return self->state();
}

//  bool QIOQnxSource::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QIOQnxSource19waitForBytesWrittenEi(
    QIOQnxSource *self,
    int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QIOQnxSource::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QIOQnxSource16waitForReadyReadEi(
    QIOQnxSource *self,
    int msecs) {
  return self->waitForReadyRead(msecs);
}

//  void QIOQnxSource::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOQnxSource12disconnectedEv(QIOQnxSource *self) {
  self->disconnected();
}

//  void QIOQnxSource::error(QAbstractSocket::SocketError socketError)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOQnxSource5errorEN15QAbstractSocket11SocketErrorE(
    QIOQnxSource *self,
    QAbstractSocket::SocketError socketError) {
  self->error(socketError);
}

//  void QIOQnxSource::stateChanged(QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOQnxSource12stateChangedEN15QAbstractSocket11SocketStateE(
    QIOQnxSource *self,
    QAbstractSocket::SocketState socketState) {
  self->stateChanged(socketState);
}

//  qint64 QIOQnxSource::readData(char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QIOQnxSource8readDataEPcx(
    QIOQnxSource *self,
    char *a0,
    qint64 a1) {
  return self->readData(a0, a1);
}

//  qint64 QIOQnxSource::writeData(const char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QIOQnxSource9writeDataEPKcx(
    QIOQnxSource *self,
    const char *a0,
    qint64 a1) {
  return self->writeData(a0, a1);
}

//  bool QIOQnxSource::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QIOQnxSource4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QIOQnxSource *self,
    int openMode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QIOQnxSource::onDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIOQnxSource14onDisconnectedEv(QIOQnxSource *self) {
  self->onDisconnected();
}

//  a Python function taken by a CuteQIOQnxSource, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIOQnxSource(
    QIOQnxSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIOQnxSource *>(self)->take(key, call);
}

//  bool QIOQnxSource::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QIOQnxSource12isSequentialEv(const QIOQnxSource *self) {
  return self->QIOQnxSource::isSequential();
}

//  qint64 QIOQnxSource::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QIOQnxSource14bytesAvailableEv(
    const QIOQnxSource *self) {
  return self->QIOQnxSource::bytesAvailable();
}

//  qint64 QIOQnxSource::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QIOQnxSource12bytesToWriteEv(
    const QIOQnxSource *self) {
  return self->QIOQnxSource::bytesToWrite();
}

//  void QIOQnxSource::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QIOQnxSource5closeEv(QIOQnxSource *self) {
  self->QIOQnxSource::close();
}

//  bool QIOQnxSource::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QIOQnxSource19waitForBytesWrittenEi(
    QIOQnxSource *self,
    int msecs) {
  return self->QIOQnxSource::waitForBytesWritten(msecs);
}

//  bool QIOQnxSource::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QIOQnxSource16waitForReadyReadEi(
    QIOQnxSource *self,
    int msecs) {
  return self->QIOQnxSource::waitForReadyRead(msecs);
}

//  qint64 QIOQnxSource::readData(char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN12QIOQnxSource8readDataEPcx(
    QIOQnxSource *self,
    char *a0,
    qint64 a1) {
  return static_cast<OwnQIOQnxSource *>(self)->OwnQIOQnxSource::readData(
      a0,
      a1);
}

//  bool QIOQnxSource::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QIOQnxSource4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QIOQnxSource *self,
    int openMode) {
  return static_cast<OwnQIOQnxSource *>(self)->OwnQIOQnxSource::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

#endif  // defined(Q_OS_QNX)
