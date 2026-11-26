//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufpropertyordering.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <QtCore/QUtf8StringView>

//  QtProtobufPrivate::QProtobufFieldInfo::QProtobufFieldInfo(QProtobufProper
//      tyOrdering ord, int ind)
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufFieldInfo *ritual_ZN17QtProtobufPrivate18QProtobufFieldInfoC1ENS_25QProtobufPropertyOrderingEi(
    const QtProtobufPrivate::QProtobufPropertyOrdering *ord,
    int ind) {
  return new QtProtobufPrivate::QProtobufFieldInfo(*ord, ind);
}

//  QUtf8StringView QtProtobufPrivate::QProtobufFieldInfo::jsonName() const
extern "C" Q_DECL_EXPORT
QUtf8StringView *ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo8jsonNameEv(
    const QtProtobufPrivate::QProtobufFieldInfo *self) {
  return new QUtf8StringView(self->jsonName());
}

//  int QtProtobufPrivate::QProtobufFieldInfo::fieldNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo11fieldNumberEv(
    const QtProtobufPrivate::QProtobufFieldInfo *self) {
  return self->fieldNumber();
}

//  int QtProtobufPrivate::QProtobufFieldInfo::propertyIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo13propertyIndexEv(
    const QtProtobufPrivate::QProtobufFieldInfo *self) {
  return self->propertyIndex();
}

//  FieldFlags QtProtobufPrivate::QProtobufFieldInfo::fieldFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QtProtobufPrivate18QProtobufFieldInfo10fieldFlagsEv(
    const QtProtobufPrivate::QProtobufFieldInfo *self) {
  return static_cast<int>(self->fieldFlags().toInt());
}

//  QtProtobufPrivate::QProtobufFieldInfo::~QProtobufFieldInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate18QProtobufFieldInfoD1Ev(
    QtProtobufPrivate::QProtobufFieldInfo *self) {
  delete self;
}

//  a QUtf8StringView a ritual of QtProtobufPrivate::QProtobufFieldInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtProtobufPrivate_QProtobufFieldInfo__QUtf8StringView(
    QUtf8StringView *self) {
  delete self;
}
