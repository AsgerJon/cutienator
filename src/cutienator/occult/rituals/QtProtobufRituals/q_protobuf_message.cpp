//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtProtobuf/qprotobufmessage.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>

//  QVariant QProtobufMessage::property(QAnyStringView propertyName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QProtobufMessage8propertyE14QAnyStringView(
    const QProtobufMessage *self,
    const QString *propertyName) {
  return new QVariant(self->property(QAnyStringView(*propertyName)));
}

//  bool QProtobufMessage::setProperty(QAnyStringView propertyName, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProtobufMessage11setPropertyE14QAnyStringViewRK8QVariant(
    QProtobufMessage *self,
    const QString *propertyName,
    const QVariant *value) {
  return self->setProperty(QAnyStringView(*propertyName), *value);
}

//  bool QProtobufMessage::setProperty(QAnyStringView propertyName, QVariant
//      &&value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProtobufMessage11setPropertyE14QAnyStringViewO8QVariant(
    QProtobufMessage *self,
    const QString *propertyName,
    QVariant *value) {
  return self->setProperty(QAnyStringView(*propertyName), std::move(*value));
}

//  QList<QByteArray> QProtobufMessage::unknownFieldData(qint32 field) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK16QProtobufMessage16unknownFieldDataEi(
    const QProtobufMessage *self,
    qint32 field) {
  return new QList<QByteArray>(self->unknownFieldData(field));
}

//  QByteArray QProtobufMessage::serialize(QAbstractProtobufSerializer
//      *serializer) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QProtobufMessage9serializeEP27QAbstractProtobufSerializer(
    const QProtobufMessage *self,
    QAbstractProtobufSerializer *serializer) {
  return new QByteArray(self->serialize(serializer));
}

//  bool QProtobufMessage::deserialize(QAbstractProtobufSerializer
//      *serializer, QByteArrayView data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProtobufMessage11deserializeEP27QAbstractProtobufSerializer14QByteArrayView(
    QProtobufMessage *self,
    QAbstractProtobufSerializer *serializer,
    const QByteArrayView *data) {
  return self->deserialize(serializer, *data);
}

//  const QtProtobufPrivate::QProtobufPropertyOrdering
//      *QProtobufMessage::propertyOrdering() const
extern "C" Q_DECL_EXPORT
const QtProtobufPrivate::QProtobufPropertyOrdering *ritual_ZNK16QProtobufMessage16propertyOrderingEv(
    const QProtobufMessage *self) {
  return self->propertyOrdering();
}

//  QProtobufMessage::QProtobufMessage(const QMetaObject *metaObject, const
//      QtProtobufPrivate::QProtobufPropertyOrdering *ordering)
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN16QProtobufMessageC1EPK11QMetaObjectPKN17QtProtobufPrivate25QProtobufPropertyOrderingE(
    const QMetaObject *metaObject,
    const QtProtobufPrivate::QProtobufPropertyOrdering *ordering) {
  return new QProtobufMessage(metaObject, ordering);
}

//  QProtobufMessage::QProtobufMessage(QProtobufMessagePrivate &dd)
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN16QProtobufMessageC1ER23QProtobufMessagePrivate(
    QProtobufMessagePrivate *dd) {
  return new QProtobufMessage(*dd);
}

//  QProtobufMessage::~QProtobufMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QProtobufMessageD1Ev(QProtobufMessage *self) {
  delete self;
}

//  QProtobufMessage::QProtobufMessage(const QProtobufMessage &other)
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN16QProtobufMessageC1ERKS_(
    const QProtobufMessage *other) {
  return new QProtobufMessage(*other);
}

//  QProtobufMessage &QProtobufMessage::operator=(const QProtobufMessage
//      &other)
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN16QProtobufMessageaSERKS_(
    QProtobufMessage *self,
    const QProtobufMessage *other) {
  return &(self->operator=(*other));
}

//  QProtobufMessage::QProtobufMessage(QProtobufMessage &&other)
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN16QProtobufMessageC1EOS_(
    QProtobufMessage *other) {
  return new QProtobufMessage(std::move(*other));
}

//  QProtobufMessage &QProtobufMessage::operator=(QProtobufMessage &&other)
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZN16QProtobufMessageaSEOS_(
    QProtobufMessage *self,
    QProtobufMessage *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QProtobufMessage::swap(QProtobufMessage &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QProtobufMessage4swapERS_(
    QProtobufMessage *self,
    QProtobufMessage *other) {
  self->swap(*other);
}

//  const QMetaObject *QProtobufMessage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QProtobufMessage10metaObjectEv(
    const QProtobufMessage *self) {
  return self->metaObject();
}

//  bool operator==(const QProtobufMessage &lhs, const QProtobufMessage &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QProtobufMessageS1_(
    const QProtobufMessage *lhs,
    const QProtobufMessage *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QProtobufMessage &lhs, const QProtobufMessage &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QProtobufMessageS1_(
    const QProtobufMessage *lhs,
    const QProtobufMessage *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QProtobufMessagePrivate *QProtobufMessage::d_func()
extern "C" Q_DECL_EXPORT
QProtobufMessagePrivate *ritual_ZN16QProtobufMessage6d_funcEv(
    QProtobufMessage *self) {
  return self->d_func();
}

//  const QProtobufMessagePrivate *QProtobufMessage::d_func() const
extern "C" Q_DECL_EXPORT
const QProtobufMessagePrivate *ritual_ZNK16QProtobufMessage6d_funcEv(
    const QProtobufMessage *self) {
  return self->d_func();
}
