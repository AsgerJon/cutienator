//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessfilebackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkaccessfilebackend_p.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QDateTime>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 28, as _ZNK32QNetworkAccessFileBackendFactory6createEN21QNetworkAccessManager9OperationERK15QNetworkRequest
#if defined(Q_OS_LINUX)
inline QNetworkAccessBackend *
QNetworkAccessFileBackendFactory::create(QNetworkAccessManager::Operation op,
                                         const QNetworkRequest &request) const
{
    // is it an operation we know of?
    switch (op) {
    case QNetworkAccessManager::GetOperation:
    case QNetworkAccessManager::PutOperation:
        break;

    default:
        // no, we can't handle this operation
        return nullptr;
    }

    QUrl url = request.url();
    if (url.scheme().compare("qrc"_L1, Qt::CaseInsensitive) == 0
#if defined(Q_OS_ANDROID)
            || url.scheme().compare("assets"_L1, Qt::CaseInsensitive) == 0
#endif
            || url.isLocalFile()) {
        return new QNetworkAccessFileBackend;
    } else if (!url.scheme().isEmpty() && url.authority().isEmpty() && (url.scheme().size() > 1)) {
        // check if QFile could, in theory, open this URL via the file engines
        // it has to be in the format:
        //    prefix:path/to/file
        // or prefix:/path/to/file
        //
        // this construct here must match the one below in open()
        QFileInfo fi(url.toString(QUrl::RemoveAuthority | QUrl::RemoveFragment | QUrl::RemoveQuery));
        if (fi.exists() || (op == QNetworkAccessManager::PutOperation && fi.dir().exists()))
            return new QNetworkAccessFileBackend;
    }

    return nullptr;
}
#endif  // defined(Q_OS_LINUX)

//  from src/network/access/qnetworkaccessfilebackend.cpp, line 67, as _ZN25QNetworkAccessFileBackendC1Ev
inline QNetworkAccessFileBackend::QNetworkAccessFileBackend()
    : QNetworkAccessBackend(QNetworkAccessBackend::TargetType::Local),
      totalBytes(0),
      hasUploadFinished(false)
{
}
//  -----------------------------------------------------------------------

//  A QNetworkAccessFileBackendFactory that Python can take functions over in. Every QNetworkAccessFileBackendFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQNetworkAccessFileBackendFactoryCall0)(const void *, int, const QNetworkRequest *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessFileBackendFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessFileBackendFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessFileBackendFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessFileBackendFactory : public QNetworkAccessFileBackendFactory {
public:
  using QNetworkAccessFileBackendFactory::QNetworkAccessFileBackendFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28QNetworkAccessBackendFactory6createEN21QNetworkAccessManager9OperationERK15QNetworkRequest")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QNetworkAccessBackend *QNetworkAccessFileBackendFactory::create(QNetw
  //      orkAccessManager::Operation op, const QNetworkRequest &request)
  //      const
  QNetworkAccessBackend *create(
      QNetworkAccessManager::Operation op,
      const QNetworkRequest &request) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall0 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall0>(taken[0]);
      void * given = call(this, static_cast<int>(op), &request, &handled);
      if (handled) return static_cast<QNetworkAccessBackend *>(given);
    }
    return QNetworkAccessFileBackendFactory::create(op, request);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall1 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall2 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall3 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall4 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall5 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall6 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessFileBackendFactoryCall7 call = reinterpret_cast<CuteQNetworkAccessFileBackendFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QStringList QNetworkAccessFileBackendFactory::supportedSchemes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QNetworkAccessFileBackendFactory16supportedSchemesEv(
    const QNetworkAccessFileBackendFactory *self) {
  return new QList<QString>(self->supportedSchemes());
}

//  QNetworkAccessBackend *QNetworkAccessFileBackendFactory::create(QNetworkA
//      ccessManager::Operation op, const QNetworkRequest &request) const
extern "C" Q_DECL_EXPORT
QNetworkAccessBackend *ritual_ZNK32QNetworkAccessFileBackendFactory6createEN21QNetworkAccessManager9OperationERK15QNetworkRequest(
    const QNetworkAccessFileBackendFactory *self,
    QNetworkAccessManager::Operation op,
    const QNetworkRequest *request) {
  return self->create(op, *request);
}

//  a Python function taken by a CuteQNetworkAccessFileBackendFactory, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessFileBackendFactory(
    QNetworkAccessFileBackendFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessFileBackendFactory *>(self)->take(key, call);
}
