//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessbackend_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qbytearrayview.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QNetworkAccessBackend that Python can take functions over in. Every QNetworkAccessBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNetworkAccessBackendCall0)(const void *, int *);
typedef void (*CuteQNetworkAccessBackendCall1)(const void *, int *);
typedef void (*CuteQNetworkAccessBackendCall2)(const void *, int *);
#if QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessBackendCall3)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef const QSslConfiguration * (*CuteQNetworkAccessBackendCall4)(const void *, int *);
#endif  // QT_CONFIG(ssl)
typedef void (*CuteQNetworkAccessBackendCall5)(const void *, int *);
typedef qint64 (*CuteQNetworkAccessBackendCall6)(const void *, int *);
typedef const QByteArrayView * (*CuteQNetworkAccessBackendCall7)(const void *, int *);
typedef void (*CuteQNetworkAccessBackendCall8)(const void *, qint64, int *);
typedef bool (*CuteQNetworkAccessBackendCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessBackendCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessBackendCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessBackendCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessBackend : public QNetworkAccessBackend {
public:
  using QNetworkAccessBackend::QNetworkAccessBackend;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5startEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend4openEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend5closeEv")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfiguration")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend16sslConfigurationEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend15ignoreSslErrorsEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QNetworkAccessBackend14bytesAvailableEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend11readPointerEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend18advanceReadPointerEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QNetworkAccessBackend10wantToReadEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QNetworkAccessBackend::start()
  bool start() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall0 call = reinterpret_cast<CuteQNetworkAccessBackendCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::start();
  }

  //  void QNetworkAccessBackend::open()
  void open() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall1 call = reinterpret_cast<CuteQNetworkAccessBackendCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QNetworkAccessBackend::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall2 call = reinterpret_cast<CuteQNetworkAccessBackendCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(ssl)
  //  void QNetworkAccessBackend::setSslConfiguration(const
  //      QSslConfiguration &configuration)
  void setSslConfiguration(const QSslConfiguration &configuration) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall3 call = reinterpret_cast<CuteQNetworkAccessBackendCall3>(taken[3]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::setSslConfiguration(configuration);
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
  QSslConfiguration sslConfiguration() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall4 call = reinterpret_cast<CuteQNetworkAccessBackendCall4>(taken[4]);
      const QSslConfiguration * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::sslConfiguration();
  }
#endif  // QT_CONFIG(ssl)

  //  void QNetworkAccessBackend::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall5 call = reinterpret_cast<CuteQNetworkAccessBackendCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::ignoreSslErrors();
  }

  //  qint64 QNetworkAccessBackend::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall6 call = reinterpret_cast<CuteQNetworkAccessBackendCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QByteArrayView QNetworkAccessBackend::readPointer()
  QByteArrayView readPointer() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall7 call = reinterpret_cast<CuteQNetworkAccessBackendCall7>(taken[7]);
      const QByteArrayView * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNetworkAccessBackend::readPointer();
  }

  //  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
  void advanceReadPointer(qint64 distance) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall8 call = reinterpret_cast<CuteQNetworkAccessBackendCall8>(taken[8]);
      call(this, distance, &handled);
      if (handled) return;
    }
    QNetworkAccessBackend::advanceReadPointer(distance);
  }

  //  bool QNetworkAccessBackend::wantToRead()
  bool wantToRead() override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall9 call = reinterpret_cast<CuteQNetworkAccessBackendCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkAccessBackend::wantToRead();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall10 call = reinterpret_cast<CuteQNetworkAccessBackendCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall11 call = reinterpret_cast<CuteQNetworkAccessBackendCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall12 call = reinterpret_cast<CuteQNetworkAccessBackendCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall13 call = reinterpret_cast<CuteQNetworkAccessBackendCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall14 call = reinterpret_cast<CuteQNetworkAccessBackendCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall15 call = reinterpret_cast<CuteQNetworkAccessBackendCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkAccessBackendCall16 call = reinterpret_cast<CuteQNetworkAccessBackendCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkAccessBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QNetworkAccessBackend10metaObjectEv(
    const QNetworkAccessBackend *self) {
  return self->metaObject();
}

//  QString QNetworkAccessBackend::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QNetworkAccessBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkAccessBackend::tr(s, c, n));
}

//  QNetworkAccessBackend::~QNetworkAccessBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackendD1Ev(QNetworkAccessBackend *self) {
  delete self;
}

//  SecurityFeatures QNetworkAccessBackend::securityFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QNetworkAccessBackend16securityFeaturesEv(
    const QNetworkAccessBackend *self) {
  return static_cast<int>(self->securityFeatures().toInt());
}

//  TargetTypes QNetworkAccessBackend::targetTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QNetworkAccessBackend11targetTypesEv(
    const QNetworkAccessBackend *self) {
  return static_cast<int>(self->targetTypes().toInt());
}

//  IOFeatures QNetworkAccessBackend::ioFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QNetworkAccessBackend10ioFeaturesEv(
    const QNetworkAccessBackend *self) {
  return static_cast<int>(self->ioFeatures().toInt());
}

//  bool QNetworkAccessBackend::needsResetableUploadData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkAccessBackend24needsResetableUploadDataEv(
    const QNetworkAccessBackend *self) {
  return self->needsResetableUploadData();
}

//  bool QNetworkAccessBackend::start()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QNetworkAccessBackend5startEv(QNetworkAccessBackend *self) {
  return self->start();
}

//  void QNetworkAccessBackend::open()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend4openEv(QNetworkAccessBackend *self) {
  self->open();
}

//  void QNetworkAccessBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend5closeEv(QNetworkAccessBackend *self) {
  self->close();
}

#if QT_CONFIG(ssl)
//  void QNetworkAccessBackend::setSslConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfiguration(
    QNetworkAccessBackend *self,
    const QSslConfiguration *configuration) {
  self->setSslConfiguration(*configuration);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK21QNetworkAccessBackend16sslConfigurationEv(
    const QNetworkAccessBackend *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

//  void QNetworkAccessBackend::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend15ignoreSslErrorsEv(
    QNetworkAccessBackend *self) {
  self->ignoreSslErrors();
}

//  void QNetworkAccessBackend::ignoreSslErrors(const QList<QSslError>
//      &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend15ignoreSslErrorsERK5QListI9QSslErrorE(
    QNetworkAccessBackend *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}

//  qint64 QNetworkAccessBackend::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkAccessBackend14bytesAvailableEv(
    const QNetworkAccessBackend *self) {
  return self->bytesAvailable();
}

//  QByteArrayView QNetworkAccessBackend::readPointer()
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN21QNetworkAccessBackend11readPointerEv(
    QNetworkAccessBackend *self) {
  return new QByteArrayView(self->readPointer());
}

//  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend18advanceReadPointerEx(
    QNetworkAccessBackend *self,
    qint64 distance) {
  self->advanceReadPointer(distance);
}

//  bool QNetworkAccessBackend::wantToRead()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QNetworkAccessBackend10wantToReadEv(
    QNetworkAccessBackend *self) {
  return self->wantToRead();
}

#if QT_CONFIG(networkproxy)
//  QList<QNetworkProxy> QNetworkAccessBackend::proxyList() const
extern "C" Q_DECL_EXPORT
QList<QNetworkProxy> *ritual_ZNK21QNetworkAccessBackend9proxyListEv(
    const QNetworkAccessBackend *self) {
  return new QList<QNetworkProxy>(self->proxyList());
}
#endif  // QT_CONFIG(networkproxy)

//  QUrl QNetworkAccessBackend::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QNetworkAccessBackend3urlEv(
    const QNetworkAccessBackend *self) {
  return new QUrl(self->url());
}

//  void QNetworkAccessBackend::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend6setUrlERK4QUrl(
    QNetworkAccessBackend *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  QVariant QNetworkAccessBackend::header(QNetworkRequest::KnownHeaders
//      header) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QNetworkAccessBackend6headerEN15QNetworkRequest12KnownHeadersE(
    const QNetworkAccessBackend *self,
    QNetworkRequest::KnownHeaders header) {
  return new QVariant(self->header(header));
}

//  void QNetworkAccessBackend::setHeader(QNetworkRequest::KnownHeaders
//      header, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend9setHeaderEN15QNetworkRequest12KnownHeadersERK8QVariant(
    QNetworkAccessBackend *self,
    QNetworkRequest::KnownHeaders header,
    const QVariant *value) {
  self->setHeader(header, *value);
}

//  QByteArray QNetworkAccessBackend::rawHeader(const QByteArray &header)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QNetworkAccessBackend9rawHeaderERK10QByteArray(
    const QNetworkAccessBackend *self,
    const QByteArray *header) {
  return new QByteArray(self->rawHeader(*header));
}

//  void QNetworkAccessBackend::setRawHeader(const QByteArray &header, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend12setRawHeaderERK10QByteArrayS2_(
    QNetworkAccessBackend *self,
    const QByteArray *header,
    const QByteArray *value) {
  self->setRawHeader(*header, *value);
}

//  QHttpHeaders QNetworkAccessBackend::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK21QNetworkAccessBackend7headersEv(
    const QNetworkAccessBackend *self) {
  return new QHttpHeaders(self->headers());
}

//  void QNetworkAccessBackend::setHeaders(const QHttpHeaders &newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend10setHeadersERK12QHttpHeaders(
    QNetworkAccessBackend *self,
    const QHttpHeaders *newHeaders) {
  self->setHeaders(*newHeaders);
}

//  QNetworkAccessManager::Operation QNetworkAccessBackend::operation() const
extern "C" Q_DECL_EXPORT
QNetworkAccessManager::Operation ritual_ZNK21QNetworkAccessBackend9operationEv(
    const QNetworkAccessBackend *self) {
  return self->operation();
}

//  bool QNetworkAccessBackend::isCachingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkAccessBackend16isCachingEnabledEv(
    const QNetworkAccessBackend *self) {
  return self->isCachingEnabled();
}

//  void QNetworkAccessBackend::setCachingEnabled(bool canCache)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend17setCachingEnabledEb(
    QNetworkAccessBackend *self,
    bool canCache) {
  self->setCachingEnabled(canCache);
}

//  void QNetworkAccessBackend::setAttribute(QNetworkRequest::Attribute
//      attribute, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend12setAttributeEN15QNetworkRequest9AttributeERK8QVariant(
    QNetworkAccessBackend *self,
    QNetworkRequest::Attribute attribute,
    const QVariant *value) {
  self->setAttribute(attribute, *value);
}

//  QIODevice *QNetworkAccessBackend::createUploadByteDevice()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN21QNetworkAccessBackend22createUploadByteDeviceEv(
    QNetworkAccessBackend *self) {
  return self->createUploadByteDevice();
}

//  QIODevice *QNetworkAccessBackend::uploadByteDevice()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN21QNetworkAccessBackend16uploadByteDeviceEv(
    QNetworkAccessBackend *self) {
  return self->uploadByteDevice();
}

//  QAbstractNetworkCache *QNetworkAccessBackend::networkCache() const
extern "C" Q_DECL_EXPORT
QAbstractNetworkCache *ritual_ZNK21QNetworkAccessBackend12networkCacheEv(
    const QNetworkAccessBackend *self) {
  return self->networkCache();
}

//  void QNetworkAccessBackend::readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend9readyReadEv(
    QNetworkAccessBackend *self) {
  self->readyRead();
}

//  void QNetworkAccessBackend::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend8finishedEv(
    QNetworkAccessBackend *self) {
  self->finished();
}

//  void QNetworkAccessBackend::error(QNetworkReply::NetworkError code, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend5errorEN13QNetworkReply12NetworkErrorERK7QString(
    QNetworkAccessBackend *self,
    QNetworkReply::NetworkError code,
    const QString *errorString) {
  self->error(code, *errorString);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QNetworkAccessBackend::proxyAuthenticationRequired(const
//      QNetworkProxy &proxy, QAuthenticator *auth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QNetworkAccessBackend *self,
    const QNetworkProxy *proxy,
    QAuthenticator *auth) {
  self->proxyAuthenticationRequired(*proxy, auth);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QNetworkAccessBackend::authenticationRequired(QAuthenticator *auth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend22authenticationRequiredEP14QAuthenticator(
    QNetworkAccessBackend *self,
    QAuthenticator *auth) {
  self->authenticationRequired(auth);
}

//  void QNetworkAccessBackend::metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend15metaDataChangedEv(
    QNetworkAccessBackend *self) {
  self->metaDataChanged();
}

//  void QNetworkAccessBackend::redirectionRequested(const QUrl &destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend20redirectionRequestedERK4QUrl(
    QNetworkAccessBackend *self,
    const QUrl *destination) {
  self->redirectionRequested(*destination);
}

//  void QNetworkAccessBackend::setReplyPrivate(QNetworkReplyImplPrivate
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend15setReplyPrivateEP24QNetworkReplyImplPrivate(
    QNetworkAccessBackend *self,
    QNetworkReplyImplPrivate *reply) {
  self->setReplyPrivate(reply);
}

//  void
//      QNetworkAccessBackend::setManagerPrivate(QNetworkAccessManagerPrivate
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend17setManagerPrivateEP28QNetworkAccessManagerPrivate(
    QNetworkAccessBackend *self,
    QNetworkAccessManagerPrivate *manager) {
  self->setManagerPrivate(manager);
}

//  bool QNetworkAccessBackend::isSynchronous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkAccessBackend13isSynchronousEv(
    const QNetworkAccessBackend *self) {
  return self->isSynchronous();
}

//  void QNetworkAccessBackend::setSynchronous(bool synchronous)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessBackend14setSynchronousEb(
    QNetworkAccessBackend *self,
    bool synchronous) {
  self->setSynchronous(synchronous);
}

//  a Python function taken by a CuteQNetworkAccessBackend, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessBackend(
    QNetworkAccessBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessBackend *>(self)->take(key, call);
}

//  bool QNetworkAccessBackend::start()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QNetworkAccessBackend5startEv(
    QNetworkAccessBackend *self) {
  return self->QNetworkAccessBackend::start();
}

#if QT_CONFIG(ssl)
//  void QNetworkAccessBackend::setSslConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkAccessBackend19setSslConfigurationERK17QSslConfiguration(
    QNetworkAccessBackend *self,
    const QSslConfiguration *configuration) {
  self->QNetworkAccessBackend::setSslConfiguration(*configuration);
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  QSslConfiguration QNetworkAccessBackend::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_own_ZNK21QNetworkAccessBackend16sslConfigurationEv(
    const QNetworkAccessBackend *self) {
  return new QSslConfiguration(
      self->QNetworkAccessBackend::sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

//  void QNetworkAccessBackend::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkAccessBackend15ignoreSslErrorsEv(
    QNetworkAccessBackend *self) {
  self->QNetworkAccessBackend::ignoreSslErrors();
}

//  QByteArrayView QNetworkAccessBackend::readPointer()
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_own_ZN21QNetworkAccessBackend11readPointerEv(
    QNetworkAccessBackend *self) {
  return new QByteArrayView(self->QNetworkAccessBackend::readPointer());
}

//  void QNetworkAccessBackend::advanceReadPointer(qint64 distance)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkAccessBackend18advanceReadPointerEx(
    QNetworkAccessBackend *self,
    qint64 distance) {
  self->QNetworkAccessBackend::advanceReadPointer(distance);
}

//  bool QNetworkAccessBackend::wantToRead()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QNetworkAccessBackend10wantToReadEv(
    QNetworkAccessBackend *self) {
  return self->QNetworkAccessBackend::wantToRead();
}
