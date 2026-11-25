//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qwindowspipereader_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again. A handle of Windows, as 'HANDLE', is passed as an address.
//  Not written: the signals 'winError', 'readyRead' and 'pipeClosed'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qwindowspipereader_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  Only a class built on QWindowsPipeReader may call these functions of
//  it. This one is, and makes them free for the rituals to call.
struct OwnQWindowsPipeReader : QWindowsPipeReader {
  using QWindowsPipeReader::event;
};

//  A QWindowsPipeReader that Python can take functions over in. Every
//  QWindowsPipeReader Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsPipeReaderCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQWindowsPipeReaderCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQWindowsPipeReaderCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWindowsPipeReaderCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQWindowsPipeReaderCall4)(const void *, QEvent *, int *);
typedef void (*CuteQWindowsPipeReaderCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWindowsPipeReaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowsPipeReader : public QWindowsPipeReader {
public:
  using QWindowsPipeReader::QWindowsPipeReader;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWindowsPipeReader::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall0 call = reinterpret_cast<CuteQWindowsPipeReaderCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QWindowsPipeReader::event(e);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall1 call = reinterpret_cast<CuteQWindowsPipeReaderCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall2 call = reinterpret_cast<CuteQWindowsPipeReaderCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall3 call = reinterpret_cast<CuteQWindowsPipeReaderCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall4 call = reinterpret_cast<CuteQWindowsPipeReaderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall5 call = reinterpret_cast<CuteQWindowsPipeReaderCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsPipeReaderCall6 call = reinterpret_cast<CuteQWindowsPipeReaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowsPipeReader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWindowsPipeReader10metaObjectEv(
    const QWindowsPipeReader *self) {
  return self->metaObject();
}

//  QString QWindowsPipeReader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWindowsPipeReader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowsPipeReader::tr(s, c, n));
}

//  QWindowsPipeReader::QWindowsPipeReader(QObject *parent)
extern "C" Q_DECL_EXPORT
QWindowsPipeReader *ritual_ZN18QWindowsPipeReaderC1EP7QObject(
    QObject *parent) {
  return new CuteQWindowsPipeReader(parent);
}

//  QWindowsPipeReader::~QWindowsPipeReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReaderD1Ev(QWindowsPipeReader *self) {
  delete self;
}

//  void QWindowsPipeReader::setHandle(HANDLE hPipeReadEnd)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader9setHandleEPv(
    QWindowsPipeReader *self,
    HANDLE hPipeReadEnd) {
  self->setHandle(hPipeReadEnd);
}

//  void QWindowsPipeReader::startAsyncRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader14startAsyncReadEv(
    QWindowsPipeReader *self) {
  self->startAsyncRead();
}

//  void QWindowsPipeReader::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader4stopEv(QWindowsPipeReader *self) {
  self->stop();
}

//  void QWindowsPipeReader::drainAndStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader12drainAndStopEv(QWindowsPipeReader *self) {
  self->drainAndStop();
}

//  void QWindowsPipeReader::stopAndClear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader12stopAndClearEv(QWindowsPipeReader *self) {
  self->stopAndClear();
}

//  void QWindowsPipeReader::setMaxReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader20setMaxReadBufferSizeEx(
    QWindowsPipeReader *self,
    qint64 size) {
  self->setMaxReadBufferSize(size);
}

//  qint64 QWindowsPipeReader::maxReadBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QWindowsPipeReader17maxReadBufferSizeEv(
    const QWindowsPipeReader *self) {
  return self->maxReadBufferSize();
}

//  bool QWindowsPipeReader::isPipeClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsPipeReader12isPipeClosedEv(
    const QWindowsPipeReader *self) {
  return self->isPipeClosed();
}

//  qint64 QWindowsPipeReader::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QWindowsPipeReader14bytesAvailableEv(
    const QWindowsPipeReader *self) {
  return self->bytesAvailable();
}

//  qint64 QWindowsPipeReader::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN18QWindowsPipeReader4readEPcx(
    QWindowsPipeReader *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  qint64 QWindowsPipeReader::readLine(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN18QWindowsPipeReader8readLineEPcx(
    QWindowsPipeReader *self,
    char *data,
    qint64 maxlen) {
  return self->readLine(data, maxlen);
}

//  qint64 QWindowsPipeReader::skip(qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN18QWindowsPipeReader4skipEx(
    QWindowsPipeReader *self,
    qint64 maxlen) {
  return self->skip(maxlen);
}

//  bool QWindowsPipeReader::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsPipeReader11canReadLineEv(
    const QWindowsPipeReader *self) {
  return self->canReadLine();
}

//  DWORD QWindowsPipeReader::checkPipeState()
extern "C" Q_DECL_EXPORT
DWORD ritual_ZN18QWindowsPipeReader14checkPipeStateEv(
    QWindowsPipeReader *self) {
  return self->checkPipeState();
}

//  bool QWindowsPipeReader::checkForReadyRead()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeReader17checkForReadyReadEv(
    QWindowsPipeReader *self) {
  return self->checkForReadyRead();
}

//  bool QWindowsPipeReader::isReadOperationActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsPipeReader21isReadOperationActiveEv(
    const QWindowsPipeReader *self) {
  return self->isReadOperationActive();
}

//  HANDLE QWindowsPipeReader::syncEvent() const
extern "C" Q_DECL_EXPORT
HANDLE ritual_ZNK18QWindowsPipeReader9syncEventEv(
    const QWindowsPipeReader *self) {
  return self->syncEvent();
}

//  bool QWindowsPipeReader::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeReader5eventEP6QEvent(
    QWindowsPipeReader *self,
    QEvent *e) {
  return self->event(e);
}

//  void QWindowsPipeReader::startAsyncReadHelper(QMutexLocker<QMutex>
//      *locker)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader20startAsyncReadHelperEP12QMutexLockerI6QMutexE(
    QWindowsPipeReader *self,
    QMutexLocker<QMutex> *locker) {
  self->startAsyncReadHelper(locker);
}

//  void QWindowsPipeReader::startAsyncReadLocked()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader20startAsyncReadLockedEv(
    QWindowsPipeReader *self) {
  self->startAsyncReadLocked();
}

//  void QWindowsPipeReader::cancelAsyncRead(State newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader15cancelAsyncReadENS_5StateE(
    QWindowsPipeReader *self,
    QWindowsPipeReader::State newState) {
  self->cancelAsyncRead(newState);
}

//  void QWindowsPipeReader::waitCallback(PTP_CALLBACK_INSTANCE instance,
//      PVOID context, PTP_WAIT wait, TP_WAIT_RESULT waitResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeReader12waitCallbackEP21_TP_CALLBACK_INSTANCEPvP8_TP_WAITm(
    PTP_CALLBACK_INSTANCE instance,
    PVOID context,
    PTP_WAIT wait,
    TP_WAIT_RESULT waitResult) {
  QWindowsPipeReader::waitCallback(instance, context, wait, waitResult);
}

//  bool QWindowsPipeReader::readCompleted(DWORD errorCode, DWORD
//      numberOfBytesRead)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeReader13readCompletedEmm(
    QWindowsPipeReader *self,
    DWORD errorCode,
    DWORD numberOfBytesRead) {
  return self->readCompleted(errorCode, numberOfBytesRead);
}

//  bool QWindowsPipeReader::waitForNotification()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeReader19waitForNotificationEv(
    QWindowsPipeReader *self) {
  return self->waitForNotification();
}

//  bool QWindowsPipeReader::consumePendingAndEmit(bool allowWinActPosting)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeReader21consumePendingAndEmitEb(
    QWindowsPipeReader *self,
    bool allowWinActPosting) {
  return self->consumePendingAndEmit(allowWinActPosting);
}

//  bool QWindowsPipeReader::consumePending()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeReader14consumePendingEv(
    QWindowsPipeReader *self) {
  return self->consumePending();
}

//  a Python function taken by a CuteQWindowsPipeReader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsPipeReader(
    QWindowsPipeReader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsPipeReader *>(self)->take(key, call);
}

//  bool QWindowsPipeReader::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QWindowsPipeReader5eventEP6QEvent(
    QWindowsPipeReader *self,
    QEvent *e) {
  return static_cast<OwnQWindowsPipeReader *>(self)->OwnQWindowsPipeReader::event(
      e);
}

#endif  // defined(Q_OS_WIN)
