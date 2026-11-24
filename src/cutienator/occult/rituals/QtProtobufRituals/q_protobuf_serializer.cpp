//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufserializer.h, Qt 6.12.0. Changes made here are lost.
#include <QtProtobuf/qprotobufserializer.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>

//  QProtobufSerializer::QProtobufSerializer()
extern "C" Q_DECL_EXPORT
QProtobufSerializer *ritual_ZN19QProtobufSerializerC1Ev() {
  return new QProtobufSerializer();
}

//  QProtobufSerializer::~QProtobufSerializer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProtobufSerializerD1Ev(QProtobufSerializer *self) {
  delete self;
}

//  Error QProtobufSerializer::lastError() const
extern "C" Q_DECL_EXPORT
QAbstractProtobufSerializer::Error ritual_ZNK19QProtobufSerializer9lastErrorEv(
    const QProtobufSerializer *self) {
  return self->lastError();
}

//  QString QProtobufSerializer::lastErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QProtobufSerializer15lastErrorStringEv(
    const QProtobufSerializer *self) {
  return new QString(self->lastErrorString());
}

//  void QProtobufSerializer::shouldPreserveUnknownFields(bool
//      preserveUnknownFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QProtobufSerializer27shouldPreserveUnknownFieldsEb(
    QProtobufSerializer *self,
    bool preserveUnknownFields) {
  self->shouldPreserveUnknownFields(preserveUnknownFields);
}

//  QByteArray QProtobufSerializer::serializeMessage(const QProtobufMessage
//      *message) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QProtobufSerializer16serializeMessageEPK16QProtobufMessage(
    const QProtobufSerializer *self,
    const QProtobufMessage *message) {
  return new QByteArray(self->serializeMessage(message));
}

//  bool QProtobufSerializer::deserializeMessage(QProtobufMessage *message,
//      QByteArrayView data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QProtobufSerializer18deserializeMessageEP16QProtobufMessage14QByteArrayView(
    const QProtobufSerializer *self,
    QProtobufMessage *message,
    const QByteArrayView *data) {
  return self->deserializeMessage(message, *data);
}
