//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslkey_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQmlNetwork/qtqmlnetworkexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(qml_ssl)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlNetwork/QtQmlNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslkey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslkey.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QSslKey QQmlSslKey::getSslKey() const
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZNK10QQmlSslKey9getSslKeyEv(const QQmlSslKey *self) {
  return new QSslKey(self->getSslKey());
}

//  QString QQmlSslKey::keyFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QQmlSslKey7keyFileEv(const QQmlSslKey *self) {
  return new QString(self->keyFile());
}

//  QSsl::KeyAlgorithm QQmlSslKey::keyAlgorithm() const
extern "C" Q_DECL_EXPORT
QSsl::KeyAlgorithm ritual_ZNK10QQmlSslKey12keyAlgorithmEv(
    const QQmlSslKey *self) {
  return self->keyAlgorithm();
}

//  QSsl::EncodingFormat QQmlSslKey::keyFormat() const
extern "C" Q_DECL_EXPORT
QSsl::EncodingFormat ritual_ZNK10QQmlSslKey9keyFormatEv(
    const QQmlSslKey *self) {
  return self->keyFormat();
}

//  QByteArray QQmlSslKey::keyPassPhrase() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QQmlSslKey13keyPassPhraseEv(const QQmlSslKey *self) {
  return new QByteArray(self->keyPassPhrase());
}

//  QSsl::KeyType QQmlSslKey::keyType() const
extern "C" Q_DECL_EXPORT
QSsl::KeyType ritual_ZNK10QQmlSslKey7keyTypeEv(const QQmlSslKey *self) {
  return self->keyType();
}

//  void QQmlSslKey::setKeyFile(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlSslKey10setKeyFileERK7QString(
    QQmlSslKey *self,
    const QString *key) {
  self->setKeyFile(*key);
}

//  void QQmlSslKey::setKeyAlgorithm(QSsl::KeyAlgorithm value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlSslKey15setKeyAlgorithmEN4QSsl12KeyAlgorithmE(
    QQmlSslKey *self,
    QSsl::KeyAlgorithm value) {
  self->setKeyAlgorithm(value);
}

//  void QQmlSslKey::setKeyFormat(QSsl::EncodingFormat value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlSslKey12setKeyFormatEN4QSsl14EncodingFormatE(
    QQmlSslKey *self,
    QSsl::EncodingFormat value) {
  self->setKeyFormat(value);
}

//  void QQmlSslKey::setKeyPassPhrase(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlSslKey16setKeyPassPhraseERK10QByteArray(
    QQmlSslKey *self,
    const QByteArray *value) {
  self->setKeyPassPhrase(*value);
}

//  void QQmlSslKey::setKeyType(QSsl::KeyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlSslKey10setKeyTypeEN4QSsl7KeyTypeE(
    QQmlSslKey *self,
    QSsl::KeyType type) {
  self->setKeyType(type);
}

//  bool operator==(const QQmlSslKey &lvalue, const QQmlSslKey &rvalue)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QQmlSslKeyS1_(
    const QQmlSslKey *lvalue,
    const QQmlSslKey *rvalue) {
  return operator==(*lvalue, *rvalue);
}

//  QQmlSslKey::~QQmlSslKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QQmlSslKeyD1Ev(QQmlSslKey *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_ssl)
