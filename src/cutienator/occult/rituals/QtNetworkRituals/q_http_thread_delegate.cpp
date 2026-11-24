//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhttpnetworkrequest_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#include <QtCore/private/qtools_p.h>
#include "qhttpthreaddelegate_p.h"
#include <QThread>
#include <QTimer>
#include <QAuthenticator>
#include <QEventLoop>
#include <QCryptographicHash>
#include <QtCore/qscopedvaluerollback.h>
#include "private/qhttpnetworkreply_p.h"
#include "private/qnetworkaccesscache_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 192, as _ZNK19QHttpNetworkRequest3urlEv
inline QUrl QHttpNetworkRequest::url() const
{
    return d->url;
}

//  from src/network/access/qhttpthreaddelegate.cpp, line 173, as _ZN19QHttpThreadDelegateD1Ev
inline QHttpThreadDelegate::~QHttpThreadDelegate()
{
    if (!notifiedFinished) {
        emit error(QNetworkReply::OperationCanceledError, QStringLiteral("Operation canceled"));
        emit downloadFinished();
    }

    // It could be that the main thread has asked us to shut down, so we need to delete the HTTP reply
    if (httpReply) {
        delete httpReply;
    }

    // Get the object cache that stores our QHttpNetworkConnection objects
    // and release the entry for this QHttpNetworkConnection
    if (connectionCacheExpiryTimeoutSeconds.value_or(0) < 0) {
        delete httpConnection;
    } else if (connections.hasLocalData() && !cacheKey.isEmpty()) {
        connections.localData()->releaseEntry(cacheKey);
    }
}

//  from src/network/access/qhttpthreaddelegate.cpp, line 425, as _ZN19QHttpThreadDelegate12abortRequestEv
inline void QHttpThreadDelegate::abortRequest()
{
#ifdef QHTTPTHREADDELEGATE_DEBUG
    qDebug() << "QHttpThreadDelegate::abortRequest() thread=" << QThread::currentThreadId() << "sync=" << synchronous;
#endif
    if (httpReply) {
        httpReply->abort();
        delete httpReply;
        httpReply = nullptr;
    }

    // Got aborted by the timeout timer
    if (synchronous) {
        incomingErrorCode = QNetworkReply::TimeoutError;
        QMetaObject::invokeMethod(synchronousRequestLoop, "quit", Qt::QueuedConnection);
    } else {
        //only delete this for asynchronous mode or QNetworkAccessHttpBackend will crash - see QNetworkAccessHttpBackend::postRequest()
        this->deleteLater();
    }
}

//  from src/network/access/qhttpthreaddelegate.cpp, line 446, as _ZN19QHttpThreadDelegate21readBufferSizeChangedEx
inline void QHttpThreadDelegate::readBufferSizeChanged(qint64 size)
{
#ifdef QHTTPTHREADDELEGATE_DEBUG
    qDebug() << "QHttpThreadDelegate::readBufferSizeChanged() size " << size;
#endif
    if (httpReply) {
        httpReply->setDownstreamLimited(size > 0);
        httpReply->setReadBufferSize(size);
        readBufferMaxSize = size;
    }
}

//  from src/network/access/qhttpthreaddelegate.cpp, line 458, as _ZN19QHttpThreadDelegate15readBufferFreedEx
inline void QHttpThreadDelegate::readBufferFreed(qint64 size)
{
    if (readBufferMaxSize) {
        bytesEmitted -= size;

        QMetaObject::invokeMethod(this, "readyReadSlot", Qt::QueuedConnection);
    }
}

//  from src/network/access/qhttpthreaddelegate.cpp, line 604, as _ZN19QHttpThreadDelegate32synchronousFinishedWithErrorSlotEN13QNetworkReply12NetworkErrorERK7QString
inline void QHttpThreadDelegate::synchronousFinishedWithErrorSlot(QNetworkReply::NetworkError errorCode, const QString &detail)
{
    if (!httpReply)
        return;

#ifdef QHTTPTHREADDELEGATE_DEBUG
    qDebug() << "QHttpThreadDelegate::synchronousFinishedWithErrorSlot() thread=" << QThread::currentThreadId() << "error=" << errorCode << detail;
#endif
    incomingErrorCode = errorCode;
    incomingErrorDetail = detail;

    synchronousDownloadData = httpReply->readAll();

    notifiedFinished = true;
    QMetaObject::invokeMethod(httpReply, "deleteLater", Qt::QueuedConnection);
    QMetaObject::invokeMethod(synchronousRequestLoop, "quit", Qt::QueuedConnection);
    httpReply = nullptr;
}

//  from src/network/access/qhttpthreaddelegate.cpp, line 669, as _ZN19QHttpThreadDelegate28synchronousHeaderChangedSlotEv
inline void QHttpThreadDelegate::synchronousHeaderChangedSlot()
{
    if (!httpReply)
        return;

#ifdef QHTTPTHREADDELEGATE_DEBUG
    qDebug() << "QHttpThreadDelegate::synchronousHeaderChangedSlot() thread=" << QThread::currentThreadId();
#endif
    // Store the information we need in this object, the QNetworkAccessHttpBackend will later read it
    incomingHeaders = httpReply->header();
    incomingStatusCode = httpReply->statusCode();
    incomingReasonPhrase = httpReply->reasonPhrase();
    isPipeliningUsed = httpReply->isPipeliningUsed();
    isHttp2Used = httpReply->isHttp2Used();
    incomingContentLength = httpReply->contentLength();
}
//  -----------------------------------------------------------------------

//  A QHttpThreadDelegate that Python can take functions over in. Every QHttpThreadDelegate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpThreadDelegateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpThreadDelegateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpThreadDelegateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpThreadDelegateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpThreadDelegateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpThreadDelegateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpThreadDelegateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpThreadDelegate : public QHttpThreadDelegate {
public:
  using QHttpThreadDelegate::QHttpThreadDelegate;
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
      CuteQHttpThreadDelegateCall0 call = reinterpret_cast<CuteQHttpThreadDelegateCall0>(taken[0]);
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
      CuteQHttpThreadDelegateCall1 call = reinterpret_cast<CuteQHttpThreadDelegateCall1>(taken[1]);
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
      CuteQHttpThreadDelegateCall2 call = reinterpret_cast<CuteQHttpThreadDelegateCall2>(taken[2]);
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
      CuteQHttpThreadDelegateCall3 call = reinterpret_cast<CuteQHttpThreadDelegateCall3>(taken[3]);
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
      CuteQHttpThreadDelegateCall4 call = reinterpret_cast<CuteQHttpThreadDelegateCall4>(taken[4]);
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
      CuteQHttpThreadDelegateCall5 call = reinterpret_cast<CuteQHttpThreadDelegateCall5>(taken[5]);
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
      CuteQHttpThreadDelegateCall6 call = reinterpret_cast<CuteQHttpThreadDelegateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttpThreadDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QHttpThreadDelegate10metaObjectEv(
    const QHttpThreadDelegate *self) {
  return self->metaObject();
}

//  QHttpThreadDelegate::~QHttpThreadDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegateD1Ev(QHttpThreadDelegate *self) {
  delete self;
}

//  void QHttpThreadDelegate::abortRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate12abortRequestEv(
    QHttpThreadDelegate *self) {
  self->abortRequest();
}

//  void QHttpThreadDelegate::readBufferSizeChanged(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate21readBufferSizeChangedEx(
    QHttpThreadDelegate *self,
    qint64 size) {
  self->readBufferSizeChanged(size);
}

//  void QHttpThreadDelegate::readBufferFreed(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate15readBufferFreedEx(
    QHttpThreadDelegate *self,
    qint64 size) {
  self->readBufferFreed(size);
}

//  void QHttpThreadDelegate::synchronousFinishedWithErrorSlot(QNetworkReply:
//      :NetworkError errorCode, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate32synchronousFinishedWithErrorSlotEN13QNetworkReply12NetworkErrorERK7QString(
    QHttpThreadDelegate *self,
    QNetworkReply::NetworkError errorCode,
    const QString *detail) {
  self->synchronousFinishedWithErrorSlot(errorCode, *detail);
}

//  void QHttpThreadDelegate::synchronousHeaderChangedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate28synchronousHeaderChangedSlotEv(
    QHttpThreadDelegate *self) {
  self->synchronousHeaderChangedSlot();
}

//  a Python function taken by a CuteQHttpThreadDelegate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpThreadDelegate(
    QHttpThreadDelegate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpThreadDelegate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(http)
