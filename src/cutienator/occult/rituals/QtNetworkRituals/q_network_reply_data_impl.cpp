//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplydataimpl_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplydataimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkreplydataimpl_p.h>
#include <QtCore/private/qdataurl_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QMetaObject>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkreplydataimpl.cpp, line 70, as _ZN21QNetworkReplyDataImpl5abortEv
inline void QNetworkReplyDataImpl::abort()
{
    QNetworkReply::close();
}

//  from src/network/access/qnetworkreplydataimpl.cpp, line 65, as _ZN21QNetworkReplyDataImpl5closeEv
inline void QNetworkReplyDataImpl::close()
{
    QNetworkReply::close();
}

//  from src/network/access/qnetworkreplydataimpl.cpp, line 75, as _ZNK21QNetworkReplyDataImpl14bytesAvailableEv
inline qint64 QNetworkReplyDataImpl::bytesAvailable() const
{
    Q_D(const QNetworkReplyDataImpl);
    return QNetworkReply::bytesAvailable() + d->decodedData.bytesAvailable();
}

//  from src/network/access/qnetworkreplydataimpl.cpp, line 81, as _ZNK21QNetworkReplyDataImpl12isSequentialEv
inline bool QNetworkReplyDataImpl::isSequential () const
{
    return true;
}

//  from src/network/access/qnetworkreplydataimpl.cpp, line 21, as _ZN21QNetworkReplyDataImplD1Ev
inline QNetworkReplyDataImpl::~QNetworkReplyDataImpl()
{
}

//  from src/network/access/qnetworkreplydataimpl.cpp, line 86, as _ZNK21QNetworkReplyDataImpl4sizeEv
inline qint64 QNetworkReplyDataImpl::size() const
{
    Q_D(const QNetworkReplyDataImpl);
    return d->decodedData.size();
}
//  -----------------------------------------------------------------------

//  A QNetworkReplyDataImpl that Python can take functions over in. Every QNetworkReplyDataImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkReplyDataImplCall0)(const void *, int *);
typedef void (*CuteQNetworkReplyDataImplCall1)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyDataImplCall2)(const void *, int *);
typedef bool (*CuteQNetworkReplyDataImplCall3)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyDataImplCall4)(const void *, int *);
typedef void (*CuteQNetworkReplyDataImplCall5)(const void *, qint64, int *);
typedef void (*CuteQNetworkReplyDataImplCall6)(const void *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkReplyDataImplCall7)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
typedef bool (*CuteQNetworkReplyDataImplCall8)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyDataImplCall9)(const void *, int *);
typedef bool (*CuteQNetworkReplyDataImplCall10)(const void *, qint64, int *);
typedef bool (*CuteQNetworkReplyDataImplCall11)(const void *, int *);
typedef bool (*CuteQNetworkReplyDataImplCall12)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyDataImplCall13)(const void *, int *);
typedef bool (*CuteQNetworkReplyDataImplCall14)(const void *, int *);
typedef bool (*CuteQNetworkReplyDataImplCall15)(const void *, int, int *);
typedef bool (*CuteQNetworkReplyDataImplCall16)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyDataImplCall17)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyDataImplCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyDataImplCall19)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyDataImplCall20)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyDataImplCall21)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyDataImplCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyDataImplCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyDataImplCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkReplyDataImpl : public QNetworkReplyDataImpl {
public:
  using QNetworkReplyDataImpl::QNetworkReplyDataImpl;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QNetworkReply5abortEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply17setReadBufferSizeEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply15ignoreSslErrorsEv")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
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
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[17] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNetworkReplyDataImpl::abort()
  void abort() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall0 call = reinterpret_cast<CuteQNetworkReplyDataImplCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyDataImpl::abort();
  }

  //  void QNetworkReplyDataImpl::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall1 call = reinterpret_cast<CuteQNetworkReplyDataImplCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyDataImpl::close();
  }

  //  qint64 QNetworkReplyDataImpl::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall2 call = reinterpret_cast<CuteQNetworkReplyDataImplCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyDataImpl::bytesAvailable();
  }

  //  bool QNetworkReplyDataImpl::isSequential() const
  bool isSequential() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall3 call = reinterpret_cast<CuteQNetworkReplyDataImplCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyDataImpl::isSequential();
  }

  //  qint64 QNetworkReplyDataImpl::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall4 call = reinterpret_cast<CuteQNetworkReplyDataImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyDataImpl::size();
  }

  //  void QNetworkReply::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall5 call = reinterpret_cast<CuteQNetworkReplyDataImplCall5>(taken[5]);
      call(this, size, &handled);
      if (handled) return;
    }
    QNetworkReply::setReadBufferSize(size);
  }

  //  void QNetworkReply::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall6 call = reinterpret_cast<CuteQNetworkReplyDataImplCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReply::ignoreSslErrors();
  }

#if QT_CONFIG(ssl)
  //  void QNetworkReply::setSslConfigurationImplementation(const
  //      QSslConfiguration &a0)
  void setSslConfigurationImplementation(
      const QSslConfiguration &a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall7 call = reinterpret_cast<CuteQNetworkReplyDataImplCall7>(taken[7]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QNetworkReply::setSslConfigurationImplementation(a0);
  }
#endif  // QT_CONFIG(ssl)

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall8 call = reinterpret_cast<CuteQNetworkReplyDataImplCall8>(taken[8]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall9 call = reinterpret_cast<CuteQNetworkReplyDataImplCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall10 call = reinterpret_cast<CuteQNetworkReplyDataImplCall10>(taken[10]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall11 call = reinterpret_cast<CuteQNetworkReplyDataImplCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall12 call = reinterpret_cast<CuteQNetworkReplyDataImplCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall13 call = reinterpret_cast<CuteQNetworkReplyDataImplCall13>(taken[13]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall14 call = reinterpret_cast<CuteQNetworkReplyDataImplCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall15 call = reinterpret_cast<CuteQNetworkReplyDataImplCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall16 call = reinterpret_cast<CuteQNetworkReplyDataImplCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall17 call = reinterpret_cast<CuteQNetworkReplyDataImplCall17>(taken[17]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall18 call = reinterpret_cast<CuteQNetworkReplyDataImplCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall19 call = reinterpret_cast<CuteQNetworkReplyDataImplCall19>(taken[19]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall20 call = reinterpret_cast<CuteQNetworkReplyDataImplCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall21 call = reinterpret_cast<CuteQNetworkReplyDataImplCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall22 call = reinterpret_cast<CuteQNetworkReplyDataImplCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall23 call = reinterpret_cast<CuteQNetworkReplyDataImplCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQNetworkReplyDataImplCall24 call = reinterpret_cast<CuteQNetworkReplyDataImplCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkReplyDataImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QNetworkReplyDataImpl10metaObjectEv(
    const QNetworkReplyDataImpl *self) {
  return self->metaObject();
}

//  QNetworkReplyDataImpl::~QNetworkReplyDataImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyDataImplD1Ev(QNetworkReplyDataImpl *self) {
  delete self;
}

//  void QNetworkReplyDataImpl::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyDataImpl5abortEv(QNetworkReplyDataImpl *self) {
  self->abort();
}

//  void QNetworkReplyDataImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyDataImpl5closeEv(QNetworkReplyDataImpl *self) {
  self->close();
}

//  qint64 QNetworkReplyDataImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkReplyDataImpl14bytesAvailableEv(
    const QNetworkReplyDataImpl *self) {
  return self->bytesAvailable();
}

//  bool QNetworkReplyDataImpl::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkReplyDataImpl12isSequentialEv(
    const QNetworkReplyDataImpl *self) {
  return self->isSequential();
}

//  qint64 QNetworkReplyDataImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkReplyDataImpl4sizeEv(
    const QNetworkReplyDataImpl *self) {
  return self->size();
}

//  QNetworkReplyDataImplPrivate *QNetworkReplyDataImpl::d_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyDataImplPrivate *ritual_ZN21QNetworkReplyDataImpl6d_funcEv(
    QNetworkReplyDataImpl *self) {
  return self->d_func();
}

//  const QNetworkReplyDataImplPrivate *QNetworkReplyDataImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyDataImplPrivate *ritual_ZNK21QNetworkReplyDataImpl6d_funcEv(
    const QNetworkReplyDataImpl *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNetworkReplyDataImpl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyDataImpl(
    QNetworkReplyDataImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyDataImpl *>(self)->take(key, call);
}

//  void QNetworkReplyDataImpl::abort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkReplyDataImpl5abortEv(
    QNetworkReplyDataImpl *self) {
  self->QNetworkReplyDataImpl::abort();
}

//  void QNetworkReplyDataImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkReplyDataImpl5closeEv(
    QNetworkReplyDataImpl *self) {
  self->QNetworkReplyDataImpl::close();
}

//  qint64 QNetworkReplyDataImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK21QNetworkReplyDataImpl14bytesAvailableEv(
    const QNetworkReplyDataImpl *self) {
  return self->QNetworkReplyDataImpl::bytesAvailable();
}

//  bool QNetworkReplyDataImpl::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QNetworkReplyDataImpl12isSequentialEv(
    const QNetworkReplyDataImpl *self) {
  return self->QNetworkReplyDataImpl::isSequential();
}

//  qint64 QNetworkReplyDataImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK21QNetworkReplyDataImpl4sizeEv(
    const QNetworkReplyDataImpl *self) {
  return self->QNetworkReplyDataImpl::size();
}
