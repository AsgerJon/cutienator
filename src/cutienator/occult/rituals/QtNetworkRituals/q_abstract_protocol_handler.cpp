//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qabstractprotocolhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qabstractprotocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qabstractprotocolhandler_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qabstractprotocolhandler.cpp, line 18, as _ZN24QAbstractProtocolHandlerD2Ev
inline QAbstractProtocolHandler::~QAbstractProtocolHandler()
{
}

//  from src/network/access/qabstractprotocolhandler.cpp, line 22, as _ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply
inline void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
{
    m_reply = reply;
}
//  -----------------------------------------------------------------------

//  A QAbstractProtocolHandler that Python can take functions over in. Every QAbstractProtocolHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef void (*CuteQAbstractProtocolHandlerCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQAbstractProtocolHandlerCall1)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQAbstractProtocolHandlerCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQAbstractProtocolHandlerCall3)(const void *, QHttpNetworkReply *, int *);
#endif  // QT_CONFIG(http)
class CuteQAbstractProtocolHandler : public QAbstractProtocolHandler {
public:
  using QAbstractProtocolHandler::QAbstractProtocolHandler;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN24QAbstractProtocolHandler15_q_receiveReplyEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN24QAbstractProtocolHandler12_q_readyReadEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN24QAbstractProtocolHandler11sendRequestEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN24QAbstractProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
    return false;
  }

#if QT_CONFIG(http)
  //  void QAbstractProtocolHandler::_q_receiveReply()
  void _q_receiveReply() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractProtocolHandlerCall0 call = reinterpret_cast<CuteQAbstractProtocolHandlerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QAbstractProtocolHandler::_q_readyRead()
  void _q_readyRead() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractProtocolHandlerCall1 call = reinterpret_cast<CuteQAbstractProtocolHandlerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QAbstractProtocolHandler::sendRequest()
  bool sendRequest() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractProtocolHandlerCall2 call = reinterpret_cast<CuteQAbstractProtocolHandlerCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QAbstractProtocolHandler::tryRemoveReply(QHttpNetworkReply
  //      *reply)
  bool tryRemoveReply(QHttpNetworkReply *reply) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractProtocolHandlerCall3 call = reinterpret_cast<CuteQAbstractProtocolHandlerCall3>(taken[3]);
      bool given = call(this, reply, &handled);
      if (handled) return given;
    }
    return QAbstractProtocolHandler::tryRemoveReply(reply);
  }
#endif  // QT_CONFIG(http)
};

//  QAbstractProtocolHandler::~QAbstractProtocolHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractProtocolHandlerD1Ev(
    QAbstractProtocolHandler *self) {
  delete self;
}

//  void QAbstractProtocolHandler::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractProtocolHandler15_q_receiveReplyEv(
    QAbstractProtocolHandler *self) {
  self->_q_receiveReply();
}

//  void QAbstractProtocolHandler::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractProtocolHandler12_q_readyReadEv(
    QAbstractProtocolHandler *self) {
  self->_q_readyRead();
}

//  bool QAbstractProtocolHandler::sendRequest()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractProtocolHandler11sendRequestEv(
    QAbstractProtocolHandler *self) {
  return self->sendRequest();
}

//  bool QAbstractProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply(
    QAbstractProtocolHandler *self,
    QHttpNetworkReply *reply) {
  return self->tryRemoveReply(reply);
}

//  void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply(
    QAbstractProtocolHandler *self,
    QHttpNetworkReply *reply) {
  self->setReply(reply);
}

//  a Python function taken by a CuteQAbstractProtocolHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractProtocolHandler(
    QAbstractProtocolHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractProtocolHandler *>(self)->take(key, call);
}

//  bool QAbstractProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QAbstractProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply(
    QAbstractProtocolHandler *self,
    QHttpNetworkReply *reply) {
  return self->QAbstractProtocolHandler::tryRemoveReply(reply);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
