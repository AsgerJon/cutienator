//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkreply_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#if QT_CONFIG(http)
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QHttpNetworkReply that Python can take functions over in. Every QHttpNetworkReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef const QUrl * (*CuteQHttpNetworkReplyCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkReplyCall1)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef int (*CuteQHttpNetworkReplyCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef int (*CuteQHttpNetworkReplyCall3)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpNetworkReplyCall4)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkReplyCall5)(const void *, qint64, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef const QHttpHeaders * (*CuteQHttpNetworkReplyCall6)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef const QByteArray * (*CuteQHttpNetworkReplyCall7)(const void *, const QByteArrayView *, const QByteArray *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkReplyCall8)(const void *, const QByteArray *, const QByteArray *, int *);
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpNetworkReplyCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpNetworkReplyCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkReplyCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkReplyCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkReplyCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkReplyCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkReplyCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpNetworkReply : public QHttpNetworkReply {
public:
  using QHttpNetworkReply::QHttpNetworkReply;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader3urlEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader6setUrlERK4QUrl")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader12majorVersionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader12minorVersionEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader13contentLengthEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader16setContentLengthEx")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader6headerEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader11headerFieldE14QByteArrayViewRK10QByteArray")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader14setHeaderFieldERK10QByteArrayS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(http)
  //  QUrl QHttpNetworkReply::url() const
  QUrl url() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall0 call = reinterpret_cast<CuteQHttpNetworkReplyCall0>(taken[0]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHttpNetworkReply::url();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkReply::setUrl(const QUrl &url)
  void setUrl(const QUrl &url) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall1 call = reinterpret_cast<CuteQHttpNetworkReplyCall1>(taken[1]);
      call(this, &url, &handled);
      if (handled) return;
    }
    QHttpNetworkReply::setUrl(url);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  int QHttpNetworkReply::majorVersion() const
  int majorVersion() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall2 call = reinterpret_cast<CuteQHttpNetworkReplyCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpNetworkReply::majorVersion();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  int QHttpNetworkReply::minorVersion() const
  int minorVersion() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall3 call = reinterpret_cast<CuteQHttpNetworkReplyCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpNetworkReply::minorVersion();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpNetworkReply::contentLength() const
  qint64 contentLength() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall4 call = reinterpret_cast<CuteQHttpNetworkReplyCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpNetworkReply::contentLength();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkReply::setContentLength(qint64 length)
  void setContentLength(qint64 length) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall5 call = reinterpret_cast<CuteQHttpNetworkReplyCall5>(taken[5]);
      call(this, length, &handled);
      if (handled) return;
    }
    QHttpNetworkReply::setContentLength(length);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  QHttpHeaders QHttpNetworkReply::header() const
  QHttpHeaders header() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall6 call = reinterpret_cast<CuteQHttpNetworkReplyCall6>(taken[6]);
      const QHttpHeaders * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHttpNetworkReply::header();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  QByteArray QHttpNetworkReply::headerField(QByteArrayView name, const
  //      QByteArray &defaultValue) const
  QByteArray headerField(
      QByteArrayView name,
      const QByteArray &defaultValue) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall7 call = reinterpret_cast<CuteQHttpNetworkReplyCall7>(taken[7]);
      const QByteArray * given = call(this, &name, &defaultValue, &handled);
      if (handled && given) return *given;
    }
    return QHttpNetworkReply::headerField(name, defaultValue);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkReply::setHeaderField(const QByteArray &name, const
  //      QByteArray &data)
  void setHeaderField(
      const QByteArray &name,
      const QByteArray &data) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall8 call = reinterpret_cast<CuteQHttpNetworkReplyCall8>(taken[8]);
      call(this, &name, &data, &handled);
      if (handled) return;
    }
    QHttpNetworkReply::setHeaderField(name, data);
  }
#endif  // QT_CONFIG(http)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall9 call = reinterpret_cast<CuteQHttpNetworkReplyCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall10 call = reinterpret_cast<CuteQHttpNetworkReplyCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall11 call = reinterpret_cast<CuteQHttpNetworkReplyCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall12 call = reinterpret_cast<CuteQHttpNetworkReplyCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall13 call = reinterpret_cast<CuteQHttpNetworkReplyCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall14 call = reinterpret_cast<CuteQHttpNetworkReplyCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHttpNetworkReplyCall15 call = reinterpret_cast<CuteQHttpNetworkReplyCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttpNetworkReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QHttpNetworkReply10metaObjectEv(
    const QHttpNetworkReply *self) {
  return self->metaObject();
}

//  void *QHttpNetworkReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QHttpNetworkReply11qt_metacastEPKc(
    QHttpNetworkReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttpNetworkReply::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QHttpNetworkReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttpNetworkReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHttpNetworkReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QHttpNetworkReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHttpNetworkReply::tr(s, c, n));
}

//  QHttpNetworkReply::QHttpNetworkReply(const QUrl &url, QObject *parent)
extern "C" Q_DECL_EXPORT
QHttpNetworkReply *ritual_ZN17QHttpNetworkReplyC1ERK4QUrlP7QObject(
    const QUrl *url,
    QObject *parent) {
  return new CuteQHttpNetworkReply(*url, parent);
}

//  QHttpNetworkReply::~QHttpNetworkReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReplyD1Ev(QHttpNetworkReply *self) {
  delete self;
}

//  QUrl QHttpNetworkReply::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QHttpNetworkReply3urlEv(const QHttpNetworkReply *self) {
  return new QUrl(self->url());
}

//  void QHttpNetworkReply::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply6setUrlERK4QUrl(
    QHttpNetworkReply *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  int QHttpNetworkReply::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpNetworkReply12majorVersionEv(
    const QHttpNetworkReply *self) {
  return self->majorVersion();
}

//  int QHttpNetworkReply::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpNetworkReply12minorVersionEv(
    const QHttpNetworkReply *self) {
  return self->minorVersion();
}

//  void QHttpNetworkReply::setMajorVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply15setMajorVersionEi(
    QHttpNetworkReply *self,
    int version) {
  self->setMajorVersion(version);
}

//  void QHttpNetworkReply::setMinorVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply15setMinorVersionEi(
    QHttpNetworkReply *self,
    int version) {
  self->setMinorVersion(version);
}

//  qint64 QHttpNetworkReply::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpNetworkReply13contentLengthEv(
    const QHttpNetworkReply *self) {
  return self->contentLength();
}

//  void QHttpNetworkReply::setContentLength(qint64 length)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply16setContentLengthEx(
    QHttpNetworkReply *self,
    qint64 length) {
  self->setContentLength(length);
}

//  QHttpHeaders QHttpNetworkReply::header() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK17QHttpNetworkReply6headerEv(
    const QHttpNetworkReply *self) {
  return new QHttpHeaders(self->header());
}

//  QByteArray QHttpNetworkReply::headerField(QByteArrayView name, const
//      QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QHttpNetworkReply11headerFieldE14QByteArrayViewRK10QByteArray(
    const QHttpNetworkReply *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(self->headerField(*name, *defaultValue));
}

//  void QHttpNetworkReply::setHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply14setHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkReply *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->setHeaderField(*name, *data);
}

//  void QHttpNetworkReply::appendHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply17appendHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkReply *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->appendHeaderField(*name, *data);
}

//  void QHttpNetworkReply::parseHeader(QByteArrayView header)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply11parseHeaderE14QByteArrayView(
    QHttpNetworkReply *self,
    const QByteArrayView *header) {
  self->parseHeader(*header);
}

//  QHttpNetworkRequest QHttpNetworkReply::request() const
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest *ritual_ZNK17QHttpNetworkReply7requestEv(
    const QHttpNetworkReply *self) {
  return new QHttpNetworkRequest(self->request());
}

//  void QHttpNetworkReply::setRequest(const QHttpNetworkRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply10setRequestERK19QHttpNetworkRequest(
    QHttpNetworkReply *self,
    const QHttpNetworkRequest *request) {
  self->setRequest(*request);
}

//  int QHttpNetworkReply::statusCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpNetworkReply10statusCodeEv(
    const QHttpNetworkReply *self) {
  return self->statusCode();
}

//  void QHttpNetworkReply::setStatusCode(int code)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply13setStatusCodeEi(
    QHttpNetworkReply *self,
    int code) {
  self->setStatusCode(code);
}

//  QString QHttpNetworkReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHttpNetworkReply11errorStringEv(
    const QHttpNetworkReply *self) {
  return new QString(self->errorString());
}

//  void QHttpNetworkReply::setErrorString(const QString &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply14setErrorStringERK7QString(
    QHttpNetworkReply *self,
    const QString *error) {
  self->setErrorString(*error);
}

//  QNetworkReply::NetworkError QHttpNetworkReply::errorCode() const
extern "C" Q_DECL_EXPORT
QNetworkReply::NetworkError ritual_ZNK17QHttpNetworkReply9errorCodeEv(
    const QHttpNetworkReply *self) {
  return self->errorCode();
}

//  QString QHttpNetworkReply::reasonPhrase() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHttpNetworkReply12reasonPhraseEv(
    const QHttpNetworkReply *self) {
  return new QString(self->reasonPhrase());
}

//  void QHttpNetworkReply::setReasonPhrase(const QString &reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply15setReasonPhraseERK7QString(
    QHttpNetworkReply *self,
    const QString *reason) {
  self->setReasonPhrase(*reason);
}

//  qint64 QHttpNetworkReply::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpNetworkReply14bytesAvailableEv(
    const QHttpNetworkReply *self) {
  return self->bytesAvailable();
}

//  qint64 QHttpNetworkReply::bytesAvailableNextBlock() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpNetworkReply23bytesAvailableNextBlockEv(
    const QHttpNetworkReply *self) {
  return self->bytesAvailableNextBlock();
}

//  bool QHttpNetworkReply::readAnyAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply16readAnyAvailableEv(
    const QHttpNetworkReply *self) {
  return self->readAnyAvailable();
}

//  QByteArray QHttpNetworkReply::readAny()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QHttpNetworkReply7readAnyEv(QHttpNetworkReply *self) {
  return new QByteArray(self->readAny());
}

//  QByteArray QHttpNetworkReply::readAll()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QHttpNetworkReply7readAllEv(QHttpNetworkReply *self) {
  return new QByteArray(self->readAll());
}

//  QByteArray QHttpNetworkReply::read(qint64 amount)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QHttpNetworkReply4readEx(
    QHttpNetworkReply *self,
    qint64 amount) {
  return new QByteArray(self->read(amount));
}

//  qint64 QHttpNetworkReply::sizeNextBlock()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QHttpNetworkReply13sizeNextBlockEv(
    QHttpNetworkReply *self) {
  return self->sizeNextBlock();
}

//  void QHttpNetworkReply::setDownstreamLimited(bool t)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply20setDownstreamLimitedEb(
    QHttpNetworkReply *self,
    bool t) {
  self->setDownstreamLimited(t);
}

//  void QHttpNetworkReply::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply17setReadBufferSizeEx(
    QHttpNetworkReply *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  bool QHttpNetworkReply::supportsUserProvidedDownloadBuffer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpNetworkReply34supportsUserProvidedDownloadBufferEv(
    QHttpNetworkReply *self) {
  return self->supportsUserProvidedDownloadBuffer();
}

//  void QHttpNetworkReply::setUserProvidedDownloadBuffer(char *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply29setUserProvidedDownloadBufferEPc(
    QHttpNetworkReply *self,
    char *a0) {
  self->setUserProvidedDownloadBuffer(a0);
}

//  char *QHttpNetworkReply::userProvidedDownloadBuffer()
extern "C" Q_DECL_EXPORT
char *ritual_ZN17QHttpNetworkReply26userProvidedDownloadBufferEv(
    QHttpNetworkReply *self) {
  return self->userProvidedDownloadBuffer();
}

//  void QHttpNetworkReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply5abortEv(QHttpNetworkReply *self) {
  self->abort();
}

//  bool QHttpNetworkReply::isAborted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply9isAbortedEv(
    const QHttpNetworkReply *self) {
  return self->isAborted();
}

//  bool QHttpNetworkReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply10isFinishedEv(
    const QHttpNetworkReply *self) {
  return self->isFinished();
}

//  bool QHttpNetworkReply::isPipeliningUsed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply16isPipeliningUsedEv(
    const QHttpNetworkReply *self) {
  return self->isPipeliningUsed();
}

//  bool QHttpNetworkReply::isHttp2Used() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply11isHttp2UsedEv(
    const QHttpNetworkReply *self) {
  return self->isHttp2Used();
}

//  void QHttpNetworkReply::setHttp2WasUsed(bool h2Used)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply15setHttp2WasUsedEb(
    QHttpNetworkReply *self,
    bool h2Used) {
  self->setHttp2WasUsed(h2Used);
}

//  qint64 QHttpNetworkReply::removedContentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QHttpNetworkReply20removedContentLengthEv(
    const QHttpNetworkReply *self) {
  return self->removedContentLength();
}

//  bool QHttpNetworkReply::isRedirecting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply13isRedirectingEv(
    const QHttpNetworkReply *self) {
  return self->isRedirecting();
}

//  QHttpNetworkConnection *QHttpNetworkReply::connection()
extern "C" Q_DECL_EXPORT
QHttpNetworkConnection *ritual_ZN17QHttpNetworkReply10connectionEv(
    QHttpNetworkReply *self) {
  return self->connection();
}

//  QUrl QHttpNetworkReply::redirectUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QHttpNetworkReply11redirectUrlEv(
    const QHttpNetworkReply *self) {
  return new QUrl(self->redirectUrl());
}

//  void QHttpNetworkReply::setRedirectUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply14setRedirectUrlERK4QUrl(
    QHttpNetworkReply *self,
    const QUrl *url) {
  self->setRedirectUrl(*url);
}

//  bool QHttpNetworkReply::isHttpRedirect(int statusCode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpNetworkReply14isHttpRedirectEi(int statusCode) {
  return QHttpNetworkReply::isHttpRedirect(statusCode);
}

//  bool QHttpNetworkReply::isCompressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QHttpNetworkReply12isCompressedEv(
    const QHttpNetworkReply *self) {
  return self->isCompressed();
}

#if !defined(QT_NO_SSL)
//  QSslConfiguration QHttpNetworkReply::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK17QHttpNetworkReply16sslConfigurationEv(
    const QHttpNetworkReply *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkReply::setSslConfiguration(const QSslConfiguration
//      &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply19setSslConfigurationERK17QSslConfiguration(
    QHttpNetworkReply *self,
    const QSslConfiguration *config) {
  self->setSslConfiguration(*config);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkReply::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply15ignoreSslErrorsEv(
    QHttpNetworkReply *self) {
  self->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkReply::ignoreSslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply15ignoreSslErrorsERK5QListI9QSslErrorE(
    QHttpNetworkReply *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkReply::encrypted()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply9encryptedEv(QHttpNetworkReply *self) {
  self->encrypted();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkReply::sslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply9sslErrorsERK5QListI9QSslErrorE(
    QHttpNetworkReply *self,
    const QList<QSslError> *errors) {
  self->sslErrors(*errors);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkReply::preSharedKeyAuthenticationRequired(QSslPreSharedK
//      eyAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply34preSharedKeyAuthenticationRequiredEP29QSslPreSharedKeyAuthenticator(
    QHttpNetworkReply *self,
    QSslPreSharedKeyAuthenticator *authenticator) {
  self->preSharedKeyAuthenticationRequired(authenticator);
}
#endif  // !defined(QT_NO_SSL)

//  void QHttpNetworkReply::socketStartedConnecting()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply23socketStartedConnectingEv(
    QHttpNetworkReply *self) {
  self->socketStartedConnecting();
}

//  void QHttpNetworkReply::requestSent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply11requestSentEv(QHttpNetworkReply *self) {
  self->requestSent();
}

//  void QHttpNetworkReply::readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply9readyReadEv(QHttpNetworkReply *self) {
  self->readyRead();
}

//  void QHttpNetworkReply::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply8finishedEv(QHttpNetworkReply *self) {
  self->finished();
}

//  void QHttpNetworkReply::finishedWithError(QNetworkReply::NetworkError
//      errorCode, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply17finishedWithErrorEN13QNetworkReply12NetworkErrorERK7QString(
    QHttpNetworkReply *self,
    QNetworkReply::NetworkError errorCode,
    const QString *detail) {
  self->finishedWithError(errorCode, *detail);
}

//  void QHttpNetworkReply::headerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply13headerChangedEv(QHttpNetworkReply *self) {
  self->headerChanged();
}

//  void QHttpNetworkReply::dataReadProgress(qint64 done, qint64 total)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply16dataReadProgressExx(
    QHttpNetworkReply *self,
    qint64 done,
    qint64 total) {
  self->dataReadProgress(done, total);
}

//  void QHttpNetworkReply::dataSendProgress(qint64 done, qint64 total)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply16dataSendProgressExx(
    QHttpNetworkReply *self,
    qint64 done,
    qint64 total) {
  self->dataSendProgress(done, total);
}

//  void QHttpNetworkReply::cacheCredentials(const QHttpNetworkRequest
//      &request, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply16cacheCredentialsERK19QHttpNetworkRequestP14QAuthenticator(
    QHttpNetworkReply *self,
    const QHttpNetworkRequest *request,
    QAuthenticator *authenticator) {
  self->cacheCredentials(*request, authenticator);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpNetworkReply::proxyAuthenticationRequired(const QNetworkProxy
//      &proxy, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QHttpNetworkReply *self,
    const QNetworkProxy *proxy,
    QAuthenticator *authenticator) {
  self->proxyAuthenticationRequired(*proxy, authenticator);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QHttpNetworkReply::authenticationRequired(const QHttpNetworkRequest
//      &request, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply22authenticationRequiredERK19QHttpNetworkRequestP14QAuthenticator(
    QHttpNetworkReply *self,
    const QHttpNetworkRequest *request,
    QAuthenticator *authenticator) {
  self->authenticationRequired(*request, authenticator);
}

//  void QHttpNetworkReply::redirected(const QUrl &url, int httpStatus, int
//      maxRedirectsRemaining)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpNetworkReply10redirectedERK4QUrlii(
    QHttpNetworkReply *self,
    const QUrl *url,
    int httpStatus,
    int maxRedirectsRemaining) {
  self->redirected(*url, httpStatus, maxRedirectsRemaining);
}

//  QHttpNetworkReplyPrivate *QHttpNetworkReply::d_func()
extern "C" Q_DECL_EXPORT
QHttpNetworkReplyPrivate *ritual_ZN17QHttpNetworkReply6d_funcEv(
    QHttpNetworkReply *self) {
  return self->d_func();
}

//  const QHttpNetworkReplyPrivate *QHttpNetworkReply::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpNetworkReplyPrivate *ritual_ZNK17QHttpNetworkReply6d_funcEv(
    const QHttpNetworkReply *self) {
  return self->d_func();
}

//  QHttpNetworkReply as the QHttpNetworkHeader it is built on
extern "C" Q_DECL_EXPORT
QHttpNetworkHeader *ritual_cast_QHttpNetworkReply_QHttpNetworkHeader(
    QHttpNetworkReply *self) {
  return static_cast<QHttpNetworkHeader *>(self);
}

//  a Python function taken by a CuteQHttpNetworkReply, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpNetworkReply(
    QHttpNetworkReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpNetworkReply *>(self)->take(key, call);
}

//  QUrl QHttpNetworkReply::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK17QHttpNetworkReply3urlEv(
    const QHttpNetworkReply *self) {
  return new QUrl(self->QHttpNetworkReply::url());
}

//  void QHttpNetworkReply::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QHttpNetworkReply6setUrlERK4QUrl(
    QHttpNetworkReply *self,
    const QUrl *url) {
  self->QHttpNetworkReply::setUrl(*url);
}

//  int QHttpNetworkReply::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QHttpNetworkReply12majorVersionEv(
    const QHttpNetworkReply *self) {
  return self->QHttpNetworkReply::majorVersion();
}

//  int QHttpNetworkReply::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QHttpNetworkReply12minorVersionEv(
    const QHttpNetworkReply *self) {
  return self->QHttpNetworkReply::minorVersion();
}

//  qint64 QHttpNetworkReply::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK17QHttpNetworkReply13contentLengthEv(
    const QHttpNetworkReply *self) {
  return self->QHttpNetworkReply::contentLength();
}

//  void QHttpNetworkReply::setContentLength(qint64 length)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QHttpNetworkReply16setContentLengthEx(
    QHttpNetworkReply *self,
    qint64 length) {
  self->QHttpNetworkReply::setContentLength(length);
}

//  QHttpHeaders QHttpNetworkReply::header() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_own_ZNK17QHttpNetworkReply6headerEv(
    const QHttpNetworkReply *self) {
  return new QHttpHeaders(self->QHttpNetworkReply::header());
}

//  QByteArray QHttpNetworkReply::headerField(QByteArrayView name, const
//      QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK17QHttpNetworkReply11headerFieldE14QByteArrayViewRK10QByteArray(
    const QHttpNetworkReply *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(
      self->QHttpNetworkReply::headerField(
          *name,
          *defaultValue));
}

//  void QHttpNetworkReply::setHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QHttpNetworkReply14setHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkReply *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->QHttpNetworkReply::setHeaderField(*name, *data);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
