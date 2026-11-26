//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreply_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/private/qnetworkreply_p.h>
#include <QtNetwork/qsslconfiguration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkreply.cpp, line 17, as _ZN20QNetworkReplyPrivateC1Ev
inline QNetworkReplyPrivate::QNetworkReplyPrivate()
    : readBufferMaxSize(0),
      emitAllUploadProgressSignals(false),
      operation(QNetworkAccessManager::UnknownOperation),
      errorCode(QNetworkReply::NoError)
    , isFinished(false)
{
    // set the default attribute values
    attributes.insert(QNetworkRequest::ConnectionEncryptedAttribute, false);
}
//  -----------------------------------------------------------------------

//  A QNetworkReplyPrivate that Python can take functions over in. Every QNetworkReplyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNetworkReplyPrivateCall0)(const void *, char, int *);
typedef qint64 (*CuteQNetworkReplyPrivateCall1)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQNetworkReplyPrivateCall2)(const void *, qint64, int *);
class CuteQNetworkReplyPrivate : public QNetworkReplyPrivate {
public:
  using QNetworkReplyPrivate::QNetworkReplyPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEPcx")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyPrivateCall0 call = reinterpret_cast<CuteQNetworkReplyPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyPrivateCall1 call = reinterpret_cast<CuteQNetworkReplyPrivateCall1>(taken[1]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyPrivateCall2 call = reinterpret_cast<CuteQNetworkReplyPrivateCall2>(taken[2]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QNetworkReplyPrivate::QNetworkReplyPrivate()
extern "C" Q_DECL_EXPORT
QNetworkReplyPrivate *ritual_ZN20QNetworkReplyPrivateC1Ev() {
  return new CuteQNetworkReplyPrivate();
}

//  void QNetworkReplyPrivate::setManager(QNetworkReply *reply,
//      QNetworkAccessManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QNetworkReplyPrivate10setManagerEP13QNetworkReplyP21QNetworkAccessManager(
    QNetworkReply *reply,
    QNetworkAccessManager *manager) {
  QNetworkReplyPrivate::setManager(reply, manager);
}

//  QNetworkReply *QNetworkReplyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN20QNetworkReplyPrivate6q_funcEv(
    QNetworkReplyPrivate *self) {
  return self->q_func();
}

//  const QNetworkReply *QNetworkReplyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReply *ritual_ZNK20QNetworkReplyPrivate6q_funcEv(
    const QNetworkReplyPrivate *self) {
  return self->q_func();
}

//  QNetworkReplyPrivate as the QNetworkHeadersPrivate it is built on
extern "C" Q_DECL_EXPORT
QNetworkHeadersPrivate *ritual_cast_QNetworkReplyPrivate_QNetworkHeadersPrivate(
    QNetworkReplyPrivate *self) {
  return static_cast<QNetworkHeadersPrivate *>(self);
}

//  a Python function taken by a CuteQNetworkReplyPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyPrivate(
    QNetworkReplyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyPrivate *>(self)->take(key, call);
}
