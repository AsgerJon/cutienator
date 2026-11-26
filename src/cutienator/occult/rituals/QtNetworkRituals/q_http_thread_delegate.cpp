//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpthreaddelegate_p.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtNetwork/QHttpHeaders>
#include <QtCore/QString>
#include <QtCore/QSharedPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtNetwork/private/qhttpthreaddelegate_p.h>
#include <QtCore/QThread>
#include <QtCore/QTimer>
#include <QtNetwork/QAuthenticator>
#include <QtCore/QEventLoop>
#include <QtCore/QCryptographicHash>
#include <QtCore/qscopedvaluerollback.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtNetwork/private/qnetworkaccesscache_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
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

//  void *QHttpThreadDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QHttpThreadDelegate11qt_metacastEPKc(
    QHttpThreadDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttpThreadDelegate::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QHttpThreadDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttpThreadDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QHttpThreadDelegate::~QHttpThreadDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegateD1Ev(QHttpThreadDelegate *self) {
  delete self;
}

//  void QHttpThreadDelegate::authenticationRequired(const
//      QHttpNetworkRequest &request, QAuthenticator *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate22authenticationRequiredERK19QHttpNetworkRequestP14QAuthenticator(
    QHttpThreadDelegate *self,
    const QHttpNetworkRequest *request,
    QAuthenticator *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "authenticationRequired(const QHttpNetworkRequest &,QAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "authenticationRequired(const QHttpNetworkRequest &,QAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpThreadDelegate::proxyAuthenticationRequired(const QNetworkProxy
//      &a0, QAuthenticator *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QHttpThreadDelegate *self,
    const QNetworkProxy *a0,
    QAuthenticator *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyAuthenticationRequired(const QNetworkProxy &,QAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyAuthenticationRequired(const QNetworkProxy &,QAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::encrypted()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate9encryptedEv(QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "encrypted()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "encrypted()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::sslErrors(const QList<QSslError> &a0, bool *a1,
//      QList<QSslError> *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate9sslErrorsERK5QListI9QSslErrorEPbPS2_(
    QHttpThreadDelegate *self,
    const QList<QSslError> *a0,
    bool *a1,
    QList<QSslError> *a2) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sslErrors(const QList<QSslError> &,bool *,QList<QSslError> *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sslErrors(const QList<QSslError> &,bool *,QList<QSslError> *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
      const_cast<void *>(static_cast<const void *>(&a2)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::sslConfigurationChanged(const QSslConfiguration
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate23sslConfigurationChangedERK17QSslConfiguration(
    QHttpThreadDelegate *self,
    const QSslConfiguration *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sslConfigurationChanged(const QSslConfiguration &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sslConfigurationChanged(const QSslConfiguration &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::preSharedKeyAuthenticationRequired(QSslPreShare
//      dKeyAuthenticator *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate34preSharedKeyAuthenticationRequiredEP29QSslPreSharedKeyAuthenticator(
    QHttpThreadDelegate *self,
    QSslPreSharedKeyAuthenticator *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

//  void QHttpThreadDelegate::socketStartedConnecting()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate23socketStartedConnectingEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "socketStartedConnecting()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "socketStartedConnecting()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::requestSent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate11requestSentEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestSent()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestSent()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::downloadMetaData(const QHttpHeaders &a0, int
//      a1, const QString &a2, bool a3, QSharedPointer<char> a4, qint64 a5,
//      qint64 a6, bool a7, bool a8)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate16downloadMetaDataERK12QHttpHeadersiRK7QStringb14QSharedPointerIcExxbb(
    QHttpThreadDelegate *self,
    const QHttpHeaders *a0,
    int a1,
    const QString *a2,
    bool a3,
    const QSharedPointer<char> *a4,
    qint64 a5,
    qint64 a6,
    bool a7,
    bool a8) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "downloadMetaData(const QHttpHeaders &,int,const QString &,bool,QSharedPointer<char>,qint64,qint64,bool,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "downloadMetaData(const QHttpHeaders &,int,const QString &,bool,QSharedPointer<char>,qint64,qint64,bool,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
      const_cast<void *>(static_cast<const void *>(a2)),
      const_cast<void *>(static_cast<const void *>(&a3)),
      const_cast<void *>(static_cast<const void *>(a4)),
      const_cast<void *>(static_cast<const void *>(&a5)),
      const_cast<void *>(static_cast<const void *>(&a6)),
      const_cast<void *>(static_cast<const void *>(&a7)),
      const_cast<void *>(static_cast<const void *>(&a8)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::downloadProgress(qint64 a0, qint64 a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate16downloadProgressExx(
    QHttpThreadDelegate *self,
    qint64 a0,
    qint64 a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "downloadProgress(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "downloadProgress(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::downloadData(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate12downloadDataERK10QByteArray(
    QHttpThreadDelegate *self,
    const QByteArray *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "downloadData(const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "downloadData(const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::error(QNetworkReply::NetworkError a0, const
//      QString &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate5errorEN13QNetworkReply12NetworkErrorERK7QString(
    QHttpThreadDelegate *self,
    QNetworkReply::NetworkError a0,
    const QString *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "error(QNetworkReply::NetworkError,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "error(QNetworkReply::NetworkError,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::downloadFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate16downloadFinishedEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "downloadFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "downloadFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::redirected(const QUrl &url, int httpStatus, int
//      maxRedirectsRemainig)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate10redirectedERK4QUrlii(
    QHttpThreadDelegate *self,
    const QUrl *url,
    int httpStatus,
    int maxRedirectsRemainig) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "redirected(const QUrl &,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "redirected(const QUrl &,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(url)),
      const_cast<void *>(static_cast<const void *>(&httpStatus)),
      const_cast<void *>(static_cast<const void *>(&maxRedirectsRemainig)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::startRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate12startRequestEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "startRequest()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "startRequest()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::abortRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate12abortRequestEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "abortRequest()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "abortRequest()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::readBufferSizeChanged(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate21readBufferSizeChangedEx(
    QHttpThreadDelegate *self,
    qint64 size) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readBufferSizeChanged(qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readBufferSizeChanged(qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&size)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::readBufferFreed(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate15readBufferFreedEx(
    QHttpThreadDelegate *self,
    qint64 size) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readBufferFreed(qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readBufferFreed(qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&size)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::startRequestSynchronously()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate25startRequestSynchronouslyEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "startRequestSynchronously()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "startRequestSynchronously()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::readyReadSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate13readyReadSlotEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readyReadSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readyReadSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::finishedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate12finishedSlotEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finishedSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finishedSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QHttpThreadDelegate::finishedWithErrorSlot(QNetworkReply::NetworkErro
//      r errorCode, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate21finishedWithErrorSlotEN13QNetworkReply12NetworkErrorERK7QString(
    QHttpThreadDelegate *self,
    QNetworkReply::NetworkError errorCode,
    const QString *detail) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "finishedWithErrorSlot(QNetworkReply::NetworkError,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "finishedWithErrorSlot(QNetworkReply::NetworkError,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&errorCode)),
      const_cast<void *>(static_cast<const void *>(detail)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::synchronousFinishedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate23synchronousFinishedSlotEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "synchronousFinishedSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "synchronousFinishedSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::synchronousFinishedWithErrorSlot(QNetworkReply:
//      :NetworkError errorCode, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate32synchronousFinishedWithErrorSlotEN13QNetworkReply12NetworkErrorERK7QString(
    QHttpThreadDelegate *self,
    QNetworkReply::NetworkError errorCode,
    const QString *detail) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "synchronousFinishedWithErrorSlot(QNetworkReply::NetworkError,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "synchronousFinishedWithErrorSlot(QNetworkReply::NetworkError,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&errorCode)),
      const_cast<void *>(static_cast<const void *>(detail)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::headerChangedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate17headerChangedSlotEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "headerChangedSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "headerChangedSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::synchronousHeaderChangedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate28synchronousHeaderChangedSlotEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "synchronousHeaderChangedSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "synchronousHeaderChangedSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::dataReadProgressSlot(qint64 done, qint64 total)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate20dataReadProgressSlotExx(
    QHttpThreadDelegate *self,
    qint64 done,
    qint64 total) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dataReadProgressSlot(qint64,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dataReadProgressSlot(qint64,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&done)),
      const_cast<void *>(static_cast<const void *>(&total)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpThreadDelegate::cacheCredentialsSlot(const QHttpNetworkRequest
//      &request, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate20cacheCredentialsSlotERK19QHttpNetworkRequestP14QAuthenticator(
    QHttpThreadDelegate *self,
    const QHttpNetworkRequest *request,
    QAuthenticator *authenticator) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cacheCredentialsSlot(const QHttpNetworkRequest &,QAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cacheCredentialsSlot(const QHttpNetworkRequest &,QAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
      const_cast<void *>(static_cast<const void *>(&authenticator)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::encryptedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate13encryptedSlotEv(
    QHttpThreadDelegate *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "encryptedSlot()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "encryptedSlot()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::sslErrorsSlot(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate13sslErrorsSlotERK5QListI9QSslErrorE(
    QHttpThreadDelegate *self,
    const QList<QSslError> *errors) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sslErrorsSlot(const QList<QSslError> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sslErrorsSlot(const QList<QSslError> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(errors)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpThreadDelegate::preSharedKeyAuthenticationRequiredSlot(QSslPreS
//      haredKeyAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate38preSharedKeyAuthenticationRequiredSlotEP29QSslPreSharedKeyAuthenticator(
    QHttpThreadDelegate *self,
    QSslPreSharedKeyAuthenticator *authenticator) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "preSharedKeyAuthenticationRequiredSlot(QSslPreSharedKeyAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "preSharedKeyAuthenticationRequiredSlot(QSslPreSharedKeyAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&authenticator)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SSL)

//  void QHttpThreadDelegate::synchronousAuthenticationRequiredSlot(const
//      QHttpNetworkRequest &request, QAuthenticator *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate37synchronousAuthenticationRequiredSlotERK19QHttpNetworkRequestP14QAuthenticator(
    QHttpThreadDelegate *self,
    const QHttpNetworkRequest *request,
    QAuthenticator *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "synchronousAuthenticationRequiredSlot(const QHttpNetworkRequest &,QAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "synchronousAuthenticationRequiredSlot(const QHttpNetworkRequest &,QAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(request)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void
//      QHttpThreadDelegate::synchronousProxyAuthenticationRequiredSlot(const
//      QNetworkProxy &a0, QAuthenticator *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpThreadDelegate42synchronousProxyAuthenticationRequiredSlotERK13QNetworkProxyP14QAuthenticator(
    QHttpThreadDelegate *self,
    const QNetworkProxy *a0,
    QAuthenticator *a1) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpThreadDelegate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "synchronousProxyAuthenticationRequiredSlot(const QNetworkProxy &,QAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "synchronousProxyAuthenticationRequiredSlot(const QNetworkProxy &,QAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(a0)),
      const_cast<void *>(static_cast<const void *>(&a1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

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
#endif  // QT_CONFIG(http)
