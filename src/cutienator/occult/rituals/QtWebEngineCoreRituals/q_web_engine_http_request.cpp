//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginehttprequest.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginehttprequest.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QWebEngineHttpRequest::QWebEngineHttpRequest(const QUrl &url, const
//      QWebEngineHttpRequest::Method &method)
extern "C" Q_DECL_EXPORT
QWebEngineHttpRequest *ritual_ZN21QWebEngineHttpRequestC1ERK4QUrlRKNS_6MethodE(
    const QUrl *url,
    const QWebEngineHttpRequest::Method *method) {
  return new QWebEngineHttpRequest(*url, *method);
}

//  QWebEngineHttpRequest::QWebEngineHttpRequest(const QWebEngineHttpRequest
//      &other)
extern "C" Q_DECL_EXPORT
QWebEngineHttpRequest *ritual_ZN21QWebEngineHttpRequestC1ERKS_(
    const QWebEngineHttpRequest *other) {
  return new QWebEngineHttpRequest(*other);
}

//  QWebEngineHttpRequest::~QWebEngineHttpRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequestD1Ev(QWebEngineHttpRequest *self) {
  delete self;
}

#if defined(Q_COMPILER_RVALUE_REFS)
//  QWebEngineHttpRequest
//      &QWebEngineHttpRequest::operator=(QWebEngineHttpRequest &&other)
extern "C" Q_DECL_EXPORT
QWebEngineHttpRequest *ritual_ZN21QWebEngineHttpRequestaSEOS_(
    QWebEngineHttpRequest *self,
    QWebEngineHttpRequest *other) {
  return &(self->operator=(std::move(*other)));
}
#endif  // defined(Q_COMPILER_RVALUE_REFS)

//  QWebEngineHttpRequest &QWebEngineHttpRequest::operator=(const
//      QWebEngineHttpRequest &other)
extern "C" Q_DECL_EXPORT
QWebEngineHttpRequest *ritual_ZN21QWebEngineHttpRequestaSERKS_(
    QWebEngineHttpRequest *self,
    const QWebEngineHttpRequest *other) {
  return &(self->operator=(*other));
}

//  QWebEngineHttpRequest QWebEngineHttpRequest::postRequest(const QUrl &url,
//      const QMap<QString, QString> &postData)
extern "C" Q_DECL_EXPORT
QWebEngineHttpRequest *ritual_ZN21QWebEngineHttpRequest11postRequestERK4QUrlRK4QMapI7QStringS4_E(
    const QUrl *url,
    const QMap<QString, QString> *postData) {
  return new QWebEngineHttpRequest(
      QWebEngineHttpRequest::postRequest(
          *url,
          *postData));
}

//  void QWebEngineHttpRequest::swap(QWebEngineHttpRequest &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequest4swapERS_(
    QWebEngineHttpRequest *self,
    QWebEngineHttpRequest *other) {
  self->swap(*other);
}

//  bool QWebEngineHttpRequest::operator==(const QWebEngineHttpRequest
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineHttpRequesteqERKS_(
    const QWebEngineHttpRequest *self,
    const QWebEngineHttpRequest *other) {
  return self->operator==(*other);
}

//  bool QWebEngineHttpRequest::operator!=(const QWebEngineHttpRequest
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineHttpRequestneERKS_(
    const QWebEngineHttpRequest *self,
    const QWebEngineHttpRequest *other) {
  return self->operator!=(*other);
}

//  Method QWebEngineHttpRequest::method() const
extern "C" Q_DECL_EXPORT
QWebEngineHttpRequest::Method ritual_ZNK21QWebEngineHttpRequest6methodEv(
    const QWebEngineHttpRequest *self) {
  return self->method();
}

//  void QWebEngineHttpRequest::setMethod(QWebEngineHttpRequest::Method
//      method)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequest9setMethodENS_6MethodE(
    QWebEngineHttpRequest *self,
    QWebEngineHttpRequest::Method method) {
  self->setMethod(method);
}

//  QUrl QWebEngineHttpRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QWebEngineHttpRequest3urlEv(
    const QWebEngineHttpRequest *self) {
  return new QUrl(self->url());
}

//  void QWebEngineHttpRequest::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequest6setUrlERK4QUrl(
    QWebEngineHttpRequest *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  QByteArray QWebEngineHttpRequest::postData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QWebEngineHttpRequest8postDataEv(
    const QWebEngineHttpRequest *self) {
  return new QByteArray(self->postData());
}

//  void QWebEngineHttpRequest::setPostData(const QByteArray &postData)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequest11setPostDataERK10QByteArray(
    QWebEngineHttpRequest *self,
    const QByteArray *postData) {
  self->setPostData(*postData);
}

//  bool QWebEngineHttpRequest::hasHeader(const QByteArray &headerName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineHttpRequest9hasHeaderERK10QByteArray(
    const QWebEngineHttpRequest *self,
    const QByteArray *headerName) {
  return self->hasHeader(*headerName);
}

//  QList<QByteArray> QWebEngineHttpRequest::headers() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK21QWebEngineHttpRequest7headersEv(
    const QWebEngineHttpRequest *self) {
  return new QList<QByteArray>(self->headers());
}

//  QByteArray QWebEngineHttpRequest::header(const QByteArray &headerName)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QWebEngineHttpRequest6headerERK10QByteArray(
    const QWebEngineHttpRequest *self,
    const QByteArray *headerName) {
  return new QByteArray(self->header(*headerName));
}

//  void QWebEngineHttpRequest::setHeader(const QByteArray &headerName, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequest9setHeaderERK10QByteArrayS2_(
    QWebEngineHttpRequest *self,
    const QByteArray *headerName,
    const QByteArray *value) {
  self->setHeader(*headerName, *value);
}

//  void QWebEngineHttpRequest::unsetHeader(const QByteArray &headerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineHttpRequest11unsetHeaderERK10QByteArray(
    QWebEngineHttpRequest *self,
    const QByteArray *headerName) {
  self->unsetHeader(*headerName);
}
