//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtCoap/qcoapreply.h>
#include <QtCore/qstring.h>
#include <QtCoap/qcoapmessage.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QCoapReply may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCoapReply : QCoapReply {
  using QCoapReply::readData;
};

//  A QCoapReply that Python can take functions over in. Every QCoapReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQCoapReplyCall0)(const void *, char *, qint64, int *);
typedef bool (*CuteQCoapReplyCall1)(const void *, int *);
typedef bool (*CuteQCoapReplyCall2)(const void *, int, int *);
typedef void (*CuteQCoapReplyCall3)(const void *, int *);
typedef qint64 (*CuteQCoapReplyCall4)(const void *, int *);
typedef qint64 (*CuteQCoapReplyCall5)(const void *, int *);
typedef bool (*CuteQCoapReplyCall6)(const void *, qint64, int *);
typedef bool (*CuteQCoapReplyCall7)(const void *, int *);
typedef bool (*CuteQCoapReplyCall8)(const void *, int *);
typedef qint64 (*CuteQCoapReplyCall9)(const void *, int *);
typedef qint64 (*CuteQCoapReplyCall10)(const void *, int *);
typedef bool (*CuteQCoapReplyCall11)(const void *, int *);
typedef bool (*CuteQCoapReplyCall12)(const void *, int, int *);
typedef bool (*CuteQCoapReplyCall13)(const void *, int, int *);
typedef qint64 (*CuteQCoapReplyCall14)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQCoapReplyCall15)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapReplyCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapReplyCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapReplyCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapReplyCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapReplyCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapReplyCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapReplyCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoapReply : public QCoapReply {
public:
  using QCoapReply::QCoapReply;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
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

  //  qint64 QCoapReply::readData(char *data, qint64 maxSize)
  qint64 readData(char *data, qint64 maxSize) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapReplyCall0 call = reinterpret_cast<CuteQCoapReplyCall0>(taken[0]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QCoapReply::readData(data, maxSize);
  }

  //  bool QIODevice::isSequential() const
  bool isSequential() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoapReplyCall1 call = reinterpret_cast<CuteQCoapReplyCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::isSequential();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoapReplyCall2 call = reinterpret_cast<CuteQCoapReplyCall2>(taken[2]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  void QIODevice::close()
  void close() override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoapReplyCall3 call = reinterpret_cast<CuteQCoapReplyCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QIODevice::close();
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoapReplyCall4 call = reinterpret_cast<CuteQCoapReplyCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQCoapReplyCall5 call = reinterpret_cast<CuteQCoapReplyCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCoapReplyCall6 call = reinterpret_cast<CuteQCoapReplyCall6>(taken[6]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCoapReplyCall7 call = reinterpret_cast<CuteQCoapReplyCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[8]) {
      int handled = 0;
      CuteQCoapReplyCall8 call = reinterpret_cast<CuteQCoapReplyCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCoapReplyCall9 call = reinterpret_cast<CuteQCoapReplyCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQCoapReplyCall10 call = reinterpret_cast<CuteQCoapReplyCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQCoapReplyCall11 call = reinterpret_cast<CuteQCoapReplyCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCoapReplyCall12 call = reinterpret_cast<CuteQCoapReplyCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCoapReplyCall13 call = reinterpret_cast<CuteQCoapReplyCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCoapReplyCall14 call = reinterpret_cast<CuteQCoapReplyCall14>(taken[14]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCoapReplyCall15 call = reinterpret_cast<CuteQCoapReplyCall15>(taken[15]);
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
      CuteQCoapReplyCall16 call = reinterpret_cast<CuteQCoapReplyCall16>(taken[16]);
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
      CuteQCoapReplyCall17 call = reinterpret_cast<CuteQCoapReplyCall17>(taken[17]);
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
      CuteQCoapReplyCall18 call = reinterpret_cast<CuteQCoapReplyCall18>(taken[18]);
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
      CuteQCoapReplyCall19 call = reinterpret_cast<CuteQCoapReplyCall19>(taken[19]);
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
      CuteQCoapReplyCall20 call = reinterpret_cast<CuteQCoapReplyCall20>(taken[20]);
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
      CuteQCoapReplyCall21 call = reinterpret_cast<CuteQCoapReplyCall21>(taken[21]);
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
      CuteQCoapReplyCall22 call = reinterpret_cast<CuteQCoapReplyCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCoapReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QCoapReply10metaObjectEv(
    const QCoapReply *self) {
  return self->metaObject();
}

//  void *QCoapReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QCoapReply11qt_metacastEPKc(
    QCoapReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCoapReply::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QCoapReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QCoapReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCoapReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QCoapReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCoapReply::tr(s, c, n));
}

//  QCoapReply::~QCoapReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCoapReplyD1Ev(QCoapReply *self) {
  delete self;
}

//  QtCoap::ResponseCode QCoapReply::responseCode() const
extern "C" Q_DECL_EXPORT
QtCoap::ResponseCode ritual_ZNK10QCoapReply12responseCodeEv(
    const QCoapReply *self) {
  return self->responseCode();
}

//  QCoapMessage QCoapReply::message() const
extern "C" Q_DECL_EXPORT
QCoapMessage *ritual_ZNK10QCoapReply7messageEv(const QCoapReply *self) {
  return new QCoapMessage(self->message());
}

//  QCoapRequest QCoapReply::request() const
extern "C" Q_DECL_EXPORT
QCoapRequest *ritual_ZNK10QCoapReply7requestEv(const QCoapReply *self) {
  return new QCoapRequest(self->request());
}

//  QUrl QCoapReply::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QCoapReply3urlEv(const QCoapReply *self) {
  return new QUrl(self->url());
}

//  QtCoap::Method QCoapReply::method() const
extern "C" Q_DECL_EXPORT
QtCoap::Method ritual_ZNK10QCoapReply6methodEv(const QCoapReply *self) {
  return self->method();
}

//  QtCoap::Error QCoapReply::errorReceived() const
extern "C" Q_DECL_EXPORT
QtCoap::Error ritual_ZNK10QCoapReply13errorReceivedEv(
    const QCoapReply *self) {
  return self->errorReceived();
}

//  bool QCoapReply::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCoapReply9isRunningEv(const QCoapReply *self) {
  return self->isRunning();
}

//  bool QCoapReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCoapReply10isFinishedEv(const QCoapReply *self) {
  return self->isFinished();
}

//  bool QCoapReply::isAborted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCoapReply9isAbortedEv(const QCoapReply *self) {
  return self->isAborted();
}

//  bool QCoapReply::isSuccessful() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCoapReply12isSuccessfulEv(const QCoapReply *self) {
  return self->isSuccessful();
}

//  void QCoapReply::abortRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCoapReply12abortRequestEv(QCoapReply *self) {
  self->abortRequest();
}

//  void QCoapReply::finished(QCoapReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCoapReply8finishedEPS_(
    QCoapReply *self,
    QCoapReply *reply) {
  self->finished(reply);
}

//  void QCoapReply::notified(QCoapReply *reply, const QCoapMessage &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCoapReply8notifiedEPS_RK12QCoapMessage(
    QCoapReply *self,
    QCoapReply *reply,
    const QCoapMessage *message) {
  self->notified(reply, *message);
}

//  void QCoapReply::error(QCoapReply *reply, QtCoap::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCoapReply5errorEPS_N6QtCoap5ErrorE(
    QCoapReply *self,
    QCoapReply *reply,
    QtCoap::Error error) {
  self->error(reply, error);
}

//  void QCoapReply::aborted(const QCoapToken &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCoapReply7abortedERK10QByteArray(
    QCoapReply *self,
    const QByteArray *token) {
  self->aborted(*token);
}

//  qint64 QCoapReply::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN10QCoapReply8readDataEPcx(
    QCoapReply *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
}

//  qint64 QCoapReply::writeData(const char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN10QCoapReply9writeDataEPKcx(
    QCoapReply *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  QCoapReplyPrivate *QCoapReply::d_func()
extern "C" Q_DECL_EXPORT
QCoapReplyPrivate *ritual_ZN10QCoapReply6d_funcEv(QCoapReply *self) {
  return self->d_func();
}

//  const QCoapReplyPrivate *QCoapReply::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapReplyPrivate *ritual_ZNK10QCoapReply6d_funcEv(
    const QCoapReply *self) {
  return self->d_func();
}

//  QCoapReply::QCoapReply(QCoapReplyPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN10QCoapReplyC1ER17QCoapReplyPrivateP7QObject(
    QCoapReplyPrivate *dd,
    QObject *parent) {
  return new CuteQCoapReply(*dd, parent);
}

//  a Python function taken by a CuteQCoapReply, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapReply(QCoapReply *self, const char *key, void *call) {
  return static_cast<CuteQCoapReply *>(self)->take(key, call);
}

//  qint64 QCoapReply::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN10QCoapReply8readDataEPcx(
    QCoapReply *self,
    char *data,
    qint64 maxSize) {
  return static_cast<OwnQCoapReply *>(self)->OwnQCoapReply::readData(
      data,
      maxSize);
}
