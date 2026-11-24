//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeresponse_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QTextStream>
#include <QtCore/QByteArray>
#include <QtCore/QStringList>
#include <QtCore/QDateTime>
#include <QtCore/QLocale>
#include <QtCore/QCryptographicHash>
#include <QtCore/QSet>
#include <QtCore/QList>
#include <QtCore/QStringBuilder>   //for more efficient string concatenation
#include <algorithm>
#include <functional>   //for std::greater
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 55, as _ZN27QWebSocketHandshakeResponseD1Ev
inline QWebSocketHandshakeResponse::~QWebSocketHandshakeResponse()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 62, as _ZNK27QWebSocketHandshakeResponse7isValidEv
inline bool QWebSocketHandshakeResponse::isValid() const
{
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 70, as _ZNK27QWebSocketHandshakeResponse10canUpgradeEv
inline bool QWebSocketHandshakeResponse::canUpgrade() const
{
    return m_isValid && m_canUpgrade;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 78, as _ZNK27QWebSocketHandshakeResponse16acceptedProtocolEv
inline QString QWebSocketHandshakeResponse::acceptedProtocol() const
{
    return m_acceptedProtocol;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 260, as _ZNK27QWebSocketHandshakeResponse17acceptedExtensionEv
inline QString QWebSocketHandshakeResponse::acceptedExtension() const
{
    return m_acceptedExtension;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 236, as _ZNK27QWebSocketHandshakeResponse15acceptedVersionEv
inline QWebSocketProtocol::Version QWebSocketHandshakeResponse::acceptedVersion() const
{
    return m_acceptedVersion;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 244, as _ZNK27QWebSocketHandshakeResponse5errorEv
inline QWebSocketProtocol::CloseCode QWebSocketHandshakeResponse::error() const
{
    return m_error;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 252, as _ZNK27QWebSocketHandshakeResponse11errorStringEv
inline QString QWebSocketHandshakeResponse::errorString() const
{
    return m_errorString;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 86, as _ZNK27QWebSocketHandshakeResponse18calculateAcceptKeyERK7QString
inline QString QWebSocketHandshakeResponse::calculateAcceptKey(const QString &key) const
{
    //the UID comes from RFC6455
    const QString tmpKey = key % QStringLiteral("258EAFA5-E914-47DA-95CA-C5AB0DC85B11");
    const QByteArray hash = QCryptographicHash::hash(tmpKey.toLatin1(), QCryptographicHash::Sha1);
    return QString::fromLatin1(hash.toBase64());
}
//  -----------------------------------------------------------------------

//  A QWebSocketHandshakeResponse that Python can take functions over in. Every QWebSocketHandshakeResponse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketHandshakeResponseCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketHandshakeResponseCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketHandshakeResponseCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebSocketHandshakeResponse : public QWebSocketHandshakeResponse {
public:
  using QWebSocketHandshakeResponse::QWebSocketHandshakeResponse;
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
      CuteQWebSocketHandshakeResponseCall0 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall0>(taken[0]);
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
      CuteQWebSocketHandshakeResponseCall1 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall1>(taken[1]);
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
      CuteQWebSocketHandshakeResponseCall2 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall2>(taken[2]);
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
      CuteQWebSocketHandshakeResponseCall3 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall3>(taken[3]);
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
      CuteQWebSocketHandshakeResponseCall4 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall4>(taken[4]);
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
      CuteQWebSocketHandshakeResponseCall5 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall5>(taken[5]);
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
      CuteQWebSocketHandshakeResponseCall6 call = reinterpret_cast<CuteQWebSocketHandshakeResponseCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebSocketHandshakeResponse::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QWebSocketHandshakeResponse10metaObjectEv(
    const QWebSocketHandshakeResponse *self) {
  return self->metaObject();
}

//  QWebSocketHandshakeResponse::~QWebSocketHandshakeResponse()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebSocketHandshakeResponseD1Ev(
    QWebSocketHandshakeResponse *self) {
  delete self;
}

//  bool QWebSocketHandshakeResponse::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebSocketHandshakeResponse7isValidEv(
    const QWebSocketHandshakeResponse *self) {
  return self->isValid();
}

//  bool QWebSocketHandshakeResponse::canUpgrade() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebSocketHandshakeResponse10canUpgradeEv(
    const QWebSocketHandshakeResponse *self) {
  return self->canUpgrade();
}

//  QString QWebSocketHandshakeResponse::acceptedProtocol() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse16acceptedProtocolEv(
    const QWebSocketHandshakeResponse *self) {
  return new QString(self->acceptedProtocol());
}

//  QString QWebSocketHandshakeResponse::acceptedExtension() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse17acceptedExtensionEv(
    const QWebSocketHandshakeResponse *self) {
  return new QString(self->acceptedExtension());
}

//  QWebSocketProtocol::Version
//      QWebSocketHandshakeResponse::acceptedVersion() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::Version ritual_ZNK27QWebSocketHandshakeResponse15acceptedVersionEv(
    const QWebSocketHandshakeResponse *self) {
  return self->acceptedVersion();
}

//  QWebSocketProtocol::CloseCode QWebSocketHandshakeResponse::error() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK27QWebSocketHandshakeResponse5errorEv(
    const QWebSocketHandshakeResponse *self) {
  return self->error();
}

//  QString QWebSocketHandshakeResponse::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse11errorStringEv(
    const QWebSocketHandshakeResponse *self) {
  return new QString(self->errorString());
}

//  QString QWebSocketHandshakeResponse::calculateAcceptKey(const QString
//      &key) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QWebSocketHandshakeResponse18calculateAcceptKeyERK7QString(
    const QWebSocketHandshakeResponse *self,
    const QString *key) {
  return new QString(self->calculateAcceptKey(*key));
}

//  a Python function taken by a CuteQWebSocketHandshakeResponse, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocketHandshakeResponse(
    QWebSocketHandshakeResponse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebSocketHandshakeResponse *>(self)->take(key, call);
}
