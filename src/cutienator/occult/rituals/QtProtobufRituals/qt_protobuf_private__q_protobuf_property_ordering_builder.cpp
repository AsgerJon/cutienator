//  Written by hand on 2026-11-25 from
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufpropertyorderingbuilder_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  The private pointer of the class, 'QProtobufPropertyOrderingBuilder
//  Private', is named by no function and no ritual.
#include <QtProtobuf/qtprotobufglobal.h>
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufpropertyorderingbuilder_p.h>
#include <QtCore/qbytearray.h>

//  QtProtobufPrivate::QProtobufPropertyOrderingBuilder::QProtobufPropertyOrde
//      ringBuilder(QByteArray packageName)
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufPropertyOrderingBuilder *ritual_ZN17QtProtobufPrivate32QProtobufPropertyOrderingBuilderC1E10QByteArray(
    const QByteArray *packageName) {
  return new QtProtobufPrivate::QProtobufPropertyOrderingBuilder(
      *packageName);
}

//  QtProtobufPrivate::QProtobufPropertyOrderingBuilder::~QProtobufPropertyOr
//      deringBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate32QProtobufPropertyOrderingBuilderD1Ev(
    QtProtobufPrivate::QProtobufPropertyOrderingBuilder *self) {
  delete self;
}

//  void QtProtobufPrivate::QProtobufPropertyOrderingBuilder::addV0Field(
//      QByteArray jsonName, uint fieldNumber, uint propertyIndex,
//      FieldFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate32QProtobufPropertyOrderingBuilder10addV0FieldE10QByteArrayjj6QFlagsINS_9FieldFlagEE(
    QtProtobufPrivate::QProtobufPropertyOrderingBuilder *self,
    const QByteArray *jsonName,
    unsigned int fieldNumber,
    unsigned int propertyIndex,
    int flags) {
  self->addV0Field(
      *jsonName, fieldNumber, propertyIndex,
      QFlags<QtProtobufPrivate::FieldFlag>::fromInt(flags));
}

//  QProtobufPropertyOrdering::Data
//      *QtProtobufPrivate::QProtobufPropertyOrderingBuilder::build() const
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufPropertyOrdering::Data *ritual_ZNK17QtProtobufPrivate32QProtobufPropertyOrderingBuilder5buildEv(
    const QtProtobufPrivate::QProtobufPropertyOrderingBuilder *self) {
  return self->build();
}
