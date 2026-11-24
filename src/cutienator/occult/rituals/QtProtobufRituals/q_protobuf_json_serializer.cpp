//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufjsonserializer.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtProtobuf/qprotobufjsonserializer.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>

//  QProtobufJsonSerializer::QProtobufJsonSerializer()
extern "C" Q_DECL_EXPORT
QProtobufJsonSerializer *ritual_ZN23QProtobufJsonSerializerC1Ev() {
  return new QProtobufJsonSerializer();
}

//  QProtobufJsonSerializer::~QProtobufJsonSerializer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufJsonSerializerD1Ev(QProtobufJsonSerializer *self) {
  delete self;
}

//  Error QProtobufJsonSerializer::lastError() const
extern "C" Q_DECL_EXPORT
QAbstractProtobufSerializer::Error ritual_ZNK23QProtobufJsonSerializer9lastErrorEv(
    const QProtobufJsonSerializer *self) {
  return self->lastError();
}

//  QString QProtobufJsonSerializer::lastErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QProtobufJsonSerializer15lastErrorStringEv(
    const QProtobufJsonSerializer *self) {
  return new QString(self->lastErrorString());
}

//  QByteArray QProtobufJsonSerializer::serializeMessage(const
//      QProtobufMessage *message) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK23QProtobufJsonSerializer16serializeMessageEPK16QProtobufMessage(
    const QProtobufJsonSerializer *self,
    const QProtobufMessage *message) {
  return new QByteArray(self->serializeMessage(message));
}

//  bool QProtobufJsonSerializer::deserializeMessage(QProtobufMessage
//      *message, QByteArrayView data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QProtobufJsonSerializer18deserializeMessageEP16QProtobufMessage14QByteArrayView(
    const QProtobufJsonSerializer *self,
    QProtobufMessage *message,
    const QByteArrayView *data) {
  return self->deserializeMessage(message, *data);
}
