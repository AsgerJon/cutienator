//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscachebackend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccesscachebackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkaccesscachebackend_p.h>
#include <QtNetwork/qabstractnetworkcache.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qhash.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 27, as _ZN26QNetworkAccessCacheBackend4openEv
inline void QNetworkAccessCacheBackend::open()
{
    if (operation() != QNetworkAccessManager::GetOperation || !sendCacheContents()) {
        QString msg = QCoreApplication::translate("QNetworkAccessCacheBackend", "Error opening %1")
                                                .arg(this->url().toString());
        error(QNetworkReply::ContentNotFoundError, msg);
    } else {
        setAttribute(QNetworkRequest::SourceIsFromCacheAttribute, true);
    }
    finished();
}

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 104, as _ZN26QNetworkAccessCacheBackend4readEPcx
inline qint64 QNetworkAccessCacheBackend::read(char *data, qint64 maxlen)
{
    return device ? device->read(data, maxlen) : qint64(0);
}

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 97, as _ZN26QNetworkAccessCacheBackend5closeEv
inline void QNetworkAccessCacheBackend::close() { }

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 91, as _ZN26QNetworkAccessCacheBackend5startEv
inline bool QNetworkAccessCacheBackend::start()
{
    open();
    return true;
}

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 99, as _ZNK26QNetworkAccessCacheBackend14bytesAvailableEv
inline qint64 QNetworkAccessCacheBackend::bytesAvailable() const
{
    return device ? device->bytesAvailable() : qint64(0);
}

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 18, as _ZN26QNetworkAccessCacheBackendC1Ev
inline QNetworkAccessCacheBackend::QNetworkAccessCacheBackend()
    : QNetworkAccessBackend(QNetworkAccessBackend::TargetType::Local)
{
}

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 23, as _ZN26QNetworkAccessCacheBackendD1Ev
inline QNetworkAccessCacheBackend::~QNetworkAccessCacheBackend()
{
}

//  from src/network/access/qnetworkaccesscachebackend.cpp, line 39, as _ZN26QNetworkAccessCacheBackend17sendCacheContentsEv
inline bool QNetworkAccessCacheBackend::sendCacheContents()
{
    setCachingEnabled(false);
    QAbstractNetworkCache *nc = networkCache();
    if (!nc)
        return false;

    QNetworkCacheMetaData item = nc->metaData(url());
    if (!item.isValid())
        return false;

    QNetworkCacheMetaData::AttributesMap attributes = item.attributes();
    setAttribute(QNetworkRequest::HttpStatusCodeAttribute,
                 attributes.value(QNetworkRequest::HttpStatusCodeAttribute));
    setAttribute(QNetworkRequest::HttpReasonPhraseAttribute,
                 attributes.value(QNetworkRequest::HttpReasonPhraseAttribute));

    // set the headers
    auto headers = item.headers();
    const auto cacheControlValue = QLatin1StringView(
            headers.value(QHttpHeaders::WellKnownHeader::CacheControl));
    // RFC 9111 Section 5.2 Cache Control
    if (cacheControlValue.contains("must-revalidate"_L1, Qt::CaseInsensitive)
        || cacheControlValue.contains("no-cache"_L1, Qt::CaseInsensitive)) {
        return false;
    }
    setHeaders(std::move(headers));

    // handle a possible redirect
    QVariant redirectionTarget = attributes.value(QNetworkRequest::RedirectionTargetAttribute);
    if (redirectionTarget.isValid()) {
        setAttribute(QNetworkRequest::RedirectionTargetAttribute, redirectionTarget);
        redirectionRequested(redirectionTarget.toUrl());
    }

    // signal we're open
    metaDataChanged();

    if (operation() == QNetworkAccessManager::GetOperation) {
        device = nc->data(url());
        if (!device)
            return false;
        device->setParent(this);
        readyRead();
    }

#if defined(QNETWORKACCESSCACHEBACKEND_DEBUG)
    qDebug() << "Successfully sent cache:" << url();
#endif
    return true;
}
//  -----------------------------------------------------------------------

//  A QNetworkAccessCacheBackend that Python can take functions over in. Every QNetworkAccessCacheBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkAccessCacheBackendCall0)(const void *, int *);
typedef void (*CuteQNetworkAccessCacheBackendCall1)(const void *, int *);
typedef bool (*CuteQNetworkAccessCacheBackendCall2)(const void *, int *);
typedef qint64 (*CuteQNetworkAccessCacheBackendCall3)(const void *, int *);
typedef qint64 (*CuteQNetworkAccessCacheBackendCall4)(const void *, char *, qint64, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessCacheBackendCall5)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef const QSslConfiguration * (*CuteQNetworkAccessCacheBackendCall6)(const void *, int *);
#endif  // QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessCacheBackendCall7)(const void *, int *);
typedef const QByteArrayView * (*CuteQNetworkAccessCacheBackendCall8)(const void *, int *);
typedef void (*CuteQNetworkAccessCacheBackendCall9)(const void *, qint64, int *);
typedef bool (*CuteQNetworkAccessCacheBackendCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessCacheBackendCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessCacheBackendCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheBackendCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheBackendCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheBackendCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheBackendCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessCacheBackendCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessCacheBackend : public QNetworkAccessCacheBackend {
public:
  using QNetworkAccessCacheBackend::QNetworkAccessCacheBackend;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend4openEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5startEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend14bytesAvailableEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend4readEPcx")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfiguration")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend16sslConfigurationEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend15ignoreSslErrorsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend11readPointerEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend18advanceReadPointerEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend10wantToReadEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNetworkAccessCacheBackend::open()
  void open() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall0 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessCacheBackend::open();
  }

  //  void QNetworkAccessCacheBackend::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall1 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessCacheBackend::close();
  }

  //  bool QNetworkAccessCacheBackend::start()
  bool start() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall2 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessCacheBackend::start();
  }

  //  qint64 QNetworkAccessCacheBackend::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall3 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessCacheBackend::bytesAvailable();
  }

  //  qint64 QNetworkAccessCacheBackend::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall4 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall4>(taken[4]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QNetworkAccessCacheBackend::read(data, maxlen);
  }

#if QT_CONFIG(ssl)
  //  void QNetworkAccessBackend::setSslConfiguration(const
  //      QSslConfiguration &configuration)
  void setSslConfiguration(const QSslConfiguration &configuration) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall5 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall5>(taken[5]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::setSslConfiguration(configuration);
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
  QSslConfiguration sslConfiguration() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall6 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall6>(taken[6]);
      const QSslConfiguration * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::sslConfiguration();
  }
#endif  // QT_CONFIG(ssl)

  //  void QNetworkAccessBackend::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall7 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::ignoreSslErrors();
  }

  //  QByteArrayView QNetworkAccessBackend::readPointer()
  QByteArrayView readPointer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall8 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall8>(taken[8]);
      const QByteArrayView * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::readPointer();
  }

  //  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
  void advanceReadPointer(qint64 distance) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall9 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall9>(taken[9]);
      call(this, distance, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::advanceReadPointer(distance);
  }

  //  bool QNetworkAccessBackend::wantToRead()
  bool wantToRead() override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall10 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::wantToRead();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall11 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall12 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall13 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall14 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall15 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall16 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkAccessCacheBackendCall17 call = reinterpret_cast<CuteQNetworkAccessCacheBackendCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QNetworkAccessCacheBackend::QNetworkAccessCacheBackend()
extern "C" Q_DECL_EXPORT
QNetworkAccessCacheBackend *ritual_ZN26QNetworkAccessCacheBackendC1Ev() {
  return new CuteQNetworkAccessCacheBackend();
}

//  QNetworkAccessCacheBackend::~QNetworkAccessCacheBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkAccessCacheBackendD1Ev(
    QNetworkAccessCacheBackend *self) {
  delete self;
}

//  void QNetworkAccessCacheBackend::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkAccessCacheBackend4openEv(
    QNetworkAccessCacheBackend *self) {
  self->open();
}

//  void QNetworkAccessCacheBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNetworkAccessCacheBackend5closeEv(
    QNetworkAccessCacheBackend *self) {
  self->close();
}

//  bool QNetworkAccessCacheBackend::start()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QNetworkAccessCacheBackend5startEv(
    QNetworkAccessCacheBackend *self) {
  return self->start();
}

//  qint64 QNetworkAccessCacheBackend::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK26QNetworkAccessCacheBackend14bytesAvailableEv(
    const QNetworkAccessCacheBackend *self) {
  return self->bytesAvailable();
}

//  qint64 QNetworkAccessCacheBackend::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN26QNetworkAccessCacheBackend4readEPcx(
    QNetworkAccessCacheBackend *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  bool QNetworkAccessCacheBackend::sendCacheContents()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QNetworkAccessCacheBackend17sendCacheContentsEv(
    QNetworkAccessCacheBackend *self) {
  return self->sendCacheContents();
}

//  a Python function taken by a CuteQNetworkAccessCacheBackend, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessCacheBackend(
    QNetworkAccessCacheBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessCacheBackend *>(self)->take(key, call);
}

//  void QNetworkAccessCacheBackend::open()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QNetworkAccessCacheBackend4openEv(
    QNetworkAccessCacheBackend *self) {
  self->QNetworkAccessCacheBackend::open();
}

//  void QNetworkAccessCacheBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QNetworkAccessCacheBackend5closeEv(
    QNetworkAccessCacheBackend *self) {
  self->QNetworkAccessCacheBackend::close();
}

//  bool QNetworkAccessCacheBackend::start()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QNetworkAccessCacheBackend5startEv(
    QNetworkAccessCacheBackend *self) {
  return self->QNetworkAccessCacheBackend::start();
}

//  qint64 QNetworkAccessCacheBackend::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK26QNetworkAccessCacheBackend14bytesAvailableEv(
    const QNetworkAccessCacheBackend *self) {
  return self->QNetworkAccessCacheBackend::bytesAvailable();
}

//  qint64 QNetworkAccessCacheBackend::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN26QNetworkAccessCacheBackend4readEPcx(
    QNetworkAccessCacheBackend *self,
    char *data,
    qint64 maxlen) {
  return self->QNetworkAccessCacheBackend::read(data, maxlen);
}
