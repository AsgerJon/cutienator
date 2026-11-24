//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpheaderparser_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpheaderparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QHttpHeaderParser::QHttpHeaderParser()
extern "C" Q_DECL_EXPORT
QHttpHeaderParser *ritual_ZN17QHttpHeaderParserC1Ev() {
  return new QHttpHeaderParser();
}

//  void QHttpHeaderParser::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser5clearEv(QHttpHeaderParser *self) {
  self->clear();
}

//  bool QHttpHeaderParser::parseHeaders(QByteArrayView headers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpHeaderParser12parseHeadersE14QByteArrayView(
    QHttpHeaderParser *self,
    const QByteArrayView *headers) {
  return self->parseHeaders(*headers);
}

//  bool QHttpHeaderParser::parseStatus(QByteArrayView status)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHttpHeaderParser11parseStatusE14QByteArrayView(
    QHttpHeaderParser *self,
    const QByteArrayView *status) {
  return self->parseStatus(*status);
}

//  const QHttpHeaders &QHttpHeaderParser::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNKR17QHttpHeaderParser7headersEv(
    const QHttpHeaderParser *self) {
  return new QHttpHeaders(self->headers());
}

//  void QHttpHeaderParser::setStatusCode(int code)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser13setStatusCodeEi(
    QHttpHeaderParser *self,
    int code) {
  self->setStatusCode(code);
}

//  int QHttpHeaderParser::getStatusCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpHeaderParser13getStatusCodeEv(
    const QHttpHeaderParser *self) {
  return self->getStatusCode();
}

//  int QHttpHeaderParser::getMajorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpHeaderParser15getMajorVersionEv(
    const QHttpHeaderParser *self) {
  return self->getMajorVersion();
}

//  void QHttpHeaderParser::setMajorVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser15setMajorVersionEi(
    QHttpHeaderParser *self,
    int version) {
  self->setMajorVersion(version);
}

//  int QHttpHeaderParser::getMinorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHttpHeaderParser15getMinorVersionEv(
    const QHttpHeaderParser *self) {
  return self->getMinorVersion();
}

//  void QHttpHeaderParser::setMinorVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser15setMinorVersionEi(
    QHttpHeaderParser *self,
    int version) {
  self->setMinorVersion(version);
}

//  QString QHttpHeaderParser::getReasonPhrase() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHttpHeaderParser15getReasonPhraseEv(
    const QHttpHeaderParser *self) {
  return new QString(self->getReasonPhrase());
}

//  void QHttpHeaderParser::setReasonPhrase(const QString &reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser15setReasonPhraseERK7QString(
    QHttpHeaderParser *self,
    const QString *reason) {
  self->setReasonPhrase(*reason);
}

//  QByteArray QHttpHeaderParser::firstHeaderField(QByteArrayView name, const
//      QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QHttpHeaderParser16firstHeaderFieldE14QByteArrayViewRK10QByteArray(
    const QHttpHeaderParser *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(self->firstHeaderField(*name, *defaultValue));
}

//  QByteArray QHttpHeaderParser::combinedHeaderValue(QByteArrayView name,
//      const QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QHttpHeaderParser19combinedHeaderValueE14QByteArrayViewRK10QByteArray(
    const QHttpHeaderParser *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(self->combinedHeaderValue(*name, *defaultValue));
}

//  QList<QByteArray> QHttpHeaderParser::headerFieldValues(QByteArrayView
//      name) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK17QHttpHeaderParser17headerFieldValuesE14QByteArrayView(
    const QHttpHeaderParser *self,
    const QByteArrayView *name) {
  return new QList<QByteArray>(self->headerFieldValues(*name));
}

//  void QHttpHeaderParser::setHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser14setHeaderFieldERK10QByteArrayS2_(
    QHttpHeaderParser *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->setHeaderField(*name, *data);
}

//  void QHttpHeaderParser::prependHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser18prependHeaderFieldERK10QByteArrayS2_(
    QHttpHeaderParser *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->prependHeaderField(*name, *data);
}

//  void QHttpHeaderParser::appendHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser17appendHeaderFieldERK10QByteArrayS2_(
    QHttpHeaderParser *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->appendHeaderField(*name, *data);
}

//  void QHttpHeaderParser::removeHeaderField(QByteArrayView name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser17removeHeaderFieldE14QByteArrayView(
    QHttpHeaderParser *self,
    const QByteArrayView *name) {
  self->removeHeaderField(*name);
}

//  void QHttpHeaderParser::clearHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser12clearHeadersEv(QHttpHeaderParser *self) {
  self->clearHeaders();
}

//  void QHttpHeaderParser::setMaxHeaderFieldSize(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser21setMaxHeaderFieldSizeEx(
    QHttpHeaderParser *self,
    qsizetype size) {
  self->setMaxHeaderFieldSize(size);
}

//  qsizetype QHttpHeaderParser::maxHeaderFieldSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QHttpHeaderParser18maxHeaderFieldSizeEv(
    const QHttpHeaderParser *self) {
  return self->maxHeaderFieldSize();
}

//  void QHttpHeaderParser::setMaxTotalHeaderSize(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser21setMaxTotalHeaderSizeEx(
    QHttpHeaderParser *self,
    qsizetype size) {
  self->setMaxTotalHeaderSize(size);
}

//  qsizetype QHttpHeaderParser::maxTotalHeaderSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QHttpHeaderParser18maxTotalHeaderSizeEv(
    const QHttpHeaderParser *self) {
  return self->maxTotalHeaderSize();
}

//  void QHttpHeaderParser::setMaxHeaderFields(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParser18setMaxHeaderFieldsEx(
    QHttpHeaderParser *self,
    qsizetype size) {
  self->setMaxHeaderFields(size);
}

//  qsizetype QHttpHeaderParser::maxHeaderFields() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QHttpHeaderParser15maxHeaderFieldsEv(
    const QHttpHeaderParser *self) {
  return self->maxHeaderFields();
}

//  QHttpHeaderParser::~QHttpHeaderParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpHeaderParserD1Ev(QHttpHeaderParser *self) {
  delete self;
}
