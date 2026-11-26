//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qrestreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(http)
#include <QtNetwork/qrestreply.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <optional>
#include <QtCore/QJsonDocument>

//  QRestReply::QRestReply(QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
QRestReply *ritual_ZN10QRestReplyC1EP13QNetworkReply(QNetworkReply *reply) {
  return new QRestReply(reply);
}

//  QRestReply::~QRestReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRestReplyD1Ev(QRestReply *self) {
  delete self;
}

//  QRestReply::QRestReply(QRestReply &&other)
extern "C" Q_DECL_EXPORT
QRestReply *ritual_ZN10QRestReplyC1EOS_(QRestReply *other) {
  return new QRestReply(std::move(*other));
}

//  QRestReply &QRestReply::operator=(QRestReply &&other)
extern "C" Q_DECL_EXPORT
QRestReply *ritual_ZN10QRestReplyaSEOS_(
    QRestReply *self,
    QRestReply *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QRestReply::swap(QRestReply &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRestReply4swapERS_(QRestReply *self, QRestReply *other) {
  self->swap(*other);
}

//  QNetworkReply *QRestReply::networkReply() const
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZNK10QRestReply12networkReplyEv(
    const QRestReply *self) {
  return self->networkReply();
}

//  std::optional<QJsonDocument> QRestReply::readJson(QJsonParseError *error)
extern "C" Q_DECL_EXPORT
std::optional<QJsonDocument> *ritual_ZN10QRestReply8readJsonEP15QJsonParseError(
    QRestReply *self,
    QJsonParseError *error) {
  return new std::optional<QJsonDocument>(self->readJson(error));
}

//  QByteArray QRestReply::readBody()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QRestReply8readBodyEv(QRestReply *self) {
  return new QByteArray(self->readBody());
}

//  QString QRestReply::readText()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QRestReply8readTextEv(QRestReply *self) {
  return new QString(self->readText());
}

//  bool QRestReply::isSuccess() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRestReply9isSuccessEv(const QRestReply *self) {
  return self->isSuccess();
}

//  int QRestReply::httpStatus() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QRestReply10httpStatusEv(const QRestReply *self) {
  return self->httpStatus();
}

//  bool QRestReply::isHttpStatusSuccess() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRestReply19isHttpStatusSuccessEv(const QRestReply *self) {
  return self->isHttpStatusSuccess();
}

//  bool QRestReply::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRestReply8hasErrorEv(const QRestReply *self) {
  return self->hasError();
}

//  QNetworkReply::NetworkError QRestReply::error() const
extern "C" Q_DECL_EXPORT
QNetworkReply::NetworkError ritual_ZNK10QRestReply5errorEv(
    const QRestReply *self) {
  return self->error();
}

//  QString QRestReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QRestReply11errorStringEv(const QRestReply *self) {
  return new QString(self->errorString());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QRestReply &reply)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK10QRestReply(
    const QDebug *debug,
    const QRestReply *reply) {
  return new QDebug(operator<<(*debug, *reply));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  a std::optional<QJsonDocument> a ritual of QRestReply gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRestReply__std_optional_QJsonDocument(
    std::optional<QJsonDocument> *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
