//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qwindowspipewriter_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again. A handle of Windows, as 'HANDLE', is passed as an address.
//  Not written: the signals 'bytesWritten' and 'writeFailed', and the
//  template 'writeImpl'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qwindowspipewriter_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  Only a class built on QWindowsPipeWriter may call these functions of
//  it. This one is, and makes them free for the rituals to call.
struct OwnQWindowsPipeWriter : QWindowsPipeWriter {
  using QWindowsPipeWriter::event;
};

//  A QWindowsPipeWriter that Python can take functions over in. Every
//  QWindowsPipeWriter Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsPipeWriterCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQWindowsPipeWriterCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQWindowsPipeWriterCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQWindowsPipeWriterCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQWindowsPipeWriterCall4)(const void *, QEvent *, int *);
typedef void (*CuteQWindowsPipeWriterCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQWindowsPipeWriterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowsPipeWriter : public QWindowsPipeWriter {
public:
  using QWindowsPipeWriter::QWindowsPipeWriter;
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
  //  bool QWindowsPipeWriter::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall0 call = reinterpret_cast<CuteQWindowsPipeWriterCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QWindowsPipeWriter::event(e);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall1 call = reinterpret_cast<CuteQWindowsPipeWriterCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall2 call = reinterpret_cast<CuteQWindowsPipeWriterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall3 call = reinterpret_cast<CuteQWindowsPipeWriterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall4 call = reinterpret_cast<CuteQWindowsPipeWriterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall5 call = reinterpret_cast<CuteQWindowsPipeWriterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsPipeWriterCall6 call = reinterpret_cast<CuteQWindowsPipeWriterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowsPipeWriter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWindowsPipeWriter10metaObjectEv(
    const QWindowsPipeWriter *self) {
  return self->metaObject();
}

//  QString QWindowsPipeWriter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWindowsPipeWriter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowsPipeWriter::tr(s, c, n));
}

//  QWindowsPipeWriter::QWindowsPipeWriter(HANDLE pipeWriteEnd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWindowsPipeWriter *ritual_ZN18QWindowsPipeWriterC1EPvP7QObject(
    HANDLE pipeWriteEnd,
    QObject *parent) {
  return new CuteQWindowsPipeWriter(pipeWriteEnd, parent);
}

//  QWindowsPipeWriter::~QWindowsPipeWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriterD1Ev(QWindowsPipeWriter *self) {
  delete self;
}

//  void QWindowsPipeWriter::setHandle(HANDLE hPipeWriteEnd)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter9setHandleEPv(
    QWindowsPipeWriter *self,
    HANDLE hPipeWriteEnd) {
  self->setHandle(hPipeWriteEnd);
}

//  void QWindowsPipeWriter::write(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter5writeERK10QByteArray(
    QWindowsPipeWriter *self,
    const QByteArray *ba) {
  self->write(*ba);
}

//  void QWindowsPipeWriter::write(const char *data, qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter5writeEPKcx(
    QWindowsPipeWriter *self,
    const char *data,
    qint64 size) {
  self->write(data, size);
}

//  void QWindowsPipeWriter::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter4stopEv(QWindowsPipeWriter *self) {
  self->stop();
}

//  bool QWindowsPipeWriter::checkForWrite()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeWriter13checkForWriteEv(QWindowsPipeWriter *self) {
  return self->checkForWrite();
}

//  qint64 QWindowsPipeWriter::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QWindowsPipeWriter12bytesToWriteEv(
    const QWindowsPipeWriter *self) {
  return self->bytesToWrite();
}

//  bool QWindowsPipeWriter::isWriteOperationActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsPipeWriter22isWriteOperationActiveEv(
    const QWindowsPipeWriter *self) {
  return self->isWriteOperationActive();
}

//  HANDLE QWindowsPipeWriter::syncEvent() const
extern "C" Q_DECL_EXPORT
HANDLE ritual_ZNK18QWindowsPipeWriter9syncEventEv(
    const QWindowsPipeWriter *self) {
  return self->syncEvent();
}

//  bool QWindowsPipeWriter::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeWriter5eventEP6QEvent(
    QWindowsPipeWriter *self,
    QEvent *e) {
  return self->event(e);
}

//  void QWindowsPipeWriter::startAsyncWriteHelper(QMutexLocker<QMutex>
//      *locker)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter21startAsyncWriteHelperEP12QMutexLockerI6QMutexE(
    QWindowsPipeWriter *self,
    QMutexLocker<QMutex> *locker) {
  self->startAsyncWriteHelper(locker);
}

//  void QWindowsPipeWriter::startAsyncWriteLocked()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter21startAsyncWriteLockedEv(
    QWindowsPipeWriter *self) {
  self->startAsyncWriteLocked();
}

//  void QWindowsPipeWriter::waitCallback(PTP_CALLBACK_INSTANCE instance,
//      PVOID context, PTP_WAIT wait, TP_WAIT_RESULT waitResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter12waitCallbackEP21_TP_CALLBACK_INSTANCEPvP8_TP_WAITm(
    PTP_CALLBACK_INSTANCE instance,
    PVOID context,
    PTP_WAIT wait,
    TP_WAIT_RESULT waitResult) {
  QWindowsPipeWriter::waitCallback(instance, context, wait, waitResult);
}

//  bool QWindowsPipeWriter::writeCompleted(DWORD errorCode, DWORD
//      numberOfBytesWritten)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeWriter14writeCompletedEmm(
    QWindowsPipeWriter *self,
    DWORD errorCode,
    DWORD numberOfBytesWritten) {
  return self->writeCompleted(errorCode, numberOfBytesWritten);
}

//  void QWindowsPipeWriter::notifyCompleted(QMutexLocker<QMutex> *locker)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsPipeWriter15notifyCompletedEP12QMutexLockerI6QMutexE(
    QWindowsPipeWriter *self,
    QMutexLocker<QMutex> *locker) {
  self->notifyCompleted(locker);
}

//  bool QWindowsPipeWriter::consumePendingAndEmit(bool allowWinActPosting)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWindowsPipeWriter21consumePendingAndEmitEb(
    QWindowsPipeWriter *self,
    bool allowWinActPosting) {
  return self->consumePendingAndEmit(allowWinActPosting);
}

//  a Python function taken by a CuteQWindowsPipeWriter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsPipeWriter(
    QWindowsPipeWriter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsPipeWriter *>(self)->take(key, call);
}

//  bool QWindowsPipeWriter::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QWindowsPipeWriter5eventEP6QEvent(
    QWindowsPipeWriter *self,
    QEvent *e) {
  return static_cast<OwnQWindowsPipeWriter *>(self)->OwnQWindowsPipeWriter::event(
      e);
}

#endif  // defined(Q_OS_WIN)
