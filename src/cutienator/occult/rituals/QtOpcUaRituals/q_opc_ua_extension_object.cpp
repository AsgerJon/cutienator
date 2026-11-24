//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaextensionobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaextensionobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>

//  QOpcUaExtensionObject::QOpcUaExtensionObject()
extern "C" Q_DECL_EXPORT
QOpcUaExtensionObject *ritual_ZN21QOpcUaExtensionObjectC1Ev() {
  return new QOpcUaExtensionObject();
}

//  QOpcUaExtensionObject::QOpcUaExtensionObject(const QOpcUaExtensionObject
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaExtensionObject *ritual_ZN21QOpcUaExtensionObjectC1ERKS_(
    const QOpcUaExtensionObject *a0) {
  return new QOpcUaExtensionObject(*a0);
}

//  QOpcUaExtensionObject::QOpcUaExtensionObject(const QString &typeId,
//      Encoding encoding)
extern "C" Q_DECL_EXPORT
QOpcUaExtensionObject *ritual_ZN21QOpcUaExtensionObjectC1ERK7QStringNS_8EncodingE(
    const QString *typeId,
    QOpcUaExtensionObject::Encoding encoding) {
  return new QOpcUaExtensionObject(*typeId, encoding);
}

//  QOpcUaExtensionObject::~QOpcUaExtensionObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaExtensionObjectD1Ev(QOpcUaExtensionObject *self) {
  delete self;
}

//  bool QOpcUaExtensionObject::operator==(const QOpcUaExtensionObject &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpcUaExtensionObjecteqERKS_(
    const QOpcUaExtensionObject *self,
    const QOpcUaExtensionObject *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaExtensionObject::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QOpcUaExtensionObjectcv8QVariantEv(
    const QOpcUaExtensionObject *self) {
  return new QVariant(self->operator QVariant());
}

//  QString QOpcUaExtensionObject::encodingTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QOpcUaExtensionObject14encodingTypeIdEv(
    const QOpcUaExtensionObject *self) {
  return new QString(self->encodingTypeId());
}

//  void QOpcUaExtensionObject::setEncodingTypeId(const QString
//      &encodingTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaExtensionObject17setEncodingTypeIdERK7QString(
    QOpcUaExtensionObject *self,
    const QString *encodingTypeId) {
  self->setEncodingTypeId(*encodingTypeId);
}

//  QByteArray QOpcUaExtensionObject::encodedBody() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK21QOpcUaExtensionObject11encodedBodyEv(
    const QOpcUaExtensionObject *self) {
  return new QByteArray(self->encodedBody());
}

//  void QOpcUaExtensionObject::setEncodedBody(const QByteArray &encodedBody)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaExtensionObject14setEncodedBodyERK10QByteArray(
    QOpcUaExtensionObject *self,
    const QByteArray *encodedBody) {
  self->setEncodedBody(*encodedBody);
}

//  void QOpcUaExtensionObject::setBinaryEncodedBody(const QByteArray
//      &encodedBody, const QString &typeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaExtensionObject20setBinaryEncodedBodyERK10QByteArrayRK7QString(
    QOpcUaExtensionObject *self,
    const QByteArray *encodedBody,
    const QString *typeId) {
  self->setBinaryEncodedBody(*encodedBody, *typeId);
}

//  void QOpcUaExtensionObject::setXmlEncodedBody(const QByteArray
//      &encodedBody, const QString &typeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaExtensionObject17setXmlEncodedBodyERK10QByteArrayRK7QString(
    QOpcUaExtensionObject *self,
    const QByteArray *encodedBody,
    const QString *typeId) {
  self->setXmlEncodedBody(*encodedBody, *typeId);
}

//  QOpcUaExtensionObject::Encoding QOpcUaExtensionObject::encoding() const
extern "C" Q_DECL_EXPORT
QOpcUaExtensionObject::Encoding ritual_ZNK21QOpcUaExtensionObject8encodingEv(
    const QOpcUaExtensionObject *self) {
  return self->encoding();
}

//  void QOpcUaExtensionObject::setEncoding(QOpcUaExtensionObject::Encoding
//      encoding)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaExtensionObject11setEncodingENS_8EncodingE(
    QOpcUaExtensionObject *self,
    QOpcUaExtensionObject::Encoding encoding) {
  self->setEncoding(encoding);
}
