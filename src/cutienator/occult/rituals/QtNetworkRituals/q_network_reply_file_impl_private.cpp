//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyfileimpl_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyfileimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include "qnetworkreply.h"
#include "qnetworkreply_p.h"
#include <QtNetwork/qsslconfiguration.h>
#include "qnetworkreplyfileimpl_p.h"
#include "QtCore/qdatetime.h"
#include "qnetworkaccessmanager_p.h"
#include <QtCore/QCoreApplication>
#include <QtCore/QFileInfo>
#include <QtCore/QThread>
#include "qnetworkfile_p.h"
#include "qnetworkrequest.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qnetworkreply.cpp, line 17, as _ZN20QNetworkReplyPrivateC2Ev
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

//  from src/network/access/qnetworkreplyfileimpl.cpp, line 21, as _ZN28QNetworkReplyFileImplPrivateC1Ev
inline QNetworkReplyFileImplPrivate::QNetworkReplyFileImplPrivate()
    : QNetworkReplyPrivate(), managerPrivate(nullptr), realFile(nullptr)
{
    qRegisterMetaType<QNetworkRequest::KnownHeaders>();
    qRegisterMetaType<QNetworkReply::NetworkError>();
}
//  -----------------------------------------------------------------------

//  A QNetworkReplyFileImplPrivate that Python can take functions over in. Every QNetworkReplyFileImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNetworkReplyFileImplPrivateCall0)(const void *, char, int *);
typedef const QByteArray * (*CuteQNetworkReplyFileImplPrivateCall1)(const void *, qint64, int *);
class CuteQNetworkReplyFileImplPrivate : public QNetworkReplyFileImplPrivate {
public:
  using QNetworkReplyFileImplPrivate::QNetworkReplyFileImplPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyFileImplPrivateCall0 call = reinterpret_cast<CuteQNetworkReplyFileImplPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyFileImplPrivateCall1 call = reinterpret_cast<CuteQNetworkReplyFileImplPrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QNetworkReplyFileImplPrivate::QNetworkReplyFileImplPrivate()
extern "C" Q_DECL_EXPORT
QNetworkReplyFileImplPrivate *ritual_ZN28QNetworkReplyFileImplPrivateC1Ev() {
  return new CuteQNetworkReplyFileImplPrivate();
}

//  QNetworkReplyFileImpl *QNetworkReplyFileImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyFileImpl *ritual_ZN28QNetworkReplyFileImplPrivate6q_funcEv(
    QNetworkReplyFileImplPrivate *self) {
  return self->q_func();
}

//  const QNetworkReplyFileImpl *QNetworkReplyFileImplPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyFileImpl *ritual_ZNK28QNetworkReplyFileImplPrivate6q_funcEv(
    const QNetworkReplyFileImplPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQNetworkReplyFileImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyFileImplPrivate(
    QNetworkReplyFileImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyFileImplPrivate *>(self)->take(key, call);
}
