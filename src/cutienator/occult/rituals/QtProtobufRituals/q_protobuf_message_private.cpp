//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufmessage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtProtobuf/QtProtobuf>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtProtobuf/6.12.0/QtProtobuf/private/qprotobufmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearrayview.h>
#include <QtProtobuf/qprotobufpropertyordering.h>
#include <optional>
#include <QtCore/QMetaProperty>
#include <QtCore/QAnyStringView>

//  QProtobufMessagePrivate::QProtobufMessagePrivate()
extern "C" Q_DECL_EXPORT
QProtobufMessagePrivate *ritual_ZN23QProtobufMessagePrivateC1Ev() {
  return new QProtobufMessagePrivate();
}

//  QProtobufMessagePrivate::QProtobufMessagePrivate(const QMetaObject
//      *metaObject, const QtProtobufPrivate::QProtobufPropertyOrdering
//      *ordering)
extern "C" Q_DECL_EXPORT
QProtobufMessagePrivate *ritual_ZN23QProtobufMessagePrivateC1EPK11QMetaObjectPKN17QtProtobufPrivate25QProtobufPropertyOrderingE(
    const QMetaObject *metaObject,
    const QtProtobufPrivate::QProtobufPropertyOrdering *ordering) {
  return new QProtobufMessagePrivate(metaObject, ordering);
}

//  QProtobufMessagePrivate::QProtobufMessagePrivate(const
//      QProtobufMessagePrivate &other)
extern "C" Q_DECL_EXPORT
QProtobufMessagePrivate *ritual_ZN23QProtobufMessagePrivateC1ERKS_(
    const QProtobufMessagePrivate *other) {
  return new QProtobufMessagePrivate(*other);
}

//  QProtobufMessagePrivate::~QProtobufMessagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufMessagePrivateD1Ev(QProtobufMessagePrivate *self) {
  delete self;
}

//  int QProtobufMessagePrivate::propertyIndex(QAnyStringView propertyName)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QProtobufMessagePrivate13propertyIndexE14QAnyStringView(
    const QProtobufMessagePrivate *self,
    const QString *propertyName) {
  return self->propertyIndex(QAnyStringView(*propertyName));
}

//  void QProtobufMessagePrivate::storeUnknownEntry(QProtobufMessage
//      *message, QByteArrayView entry, int fieldNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufMessagePrivate17storeUnknownEntryEP16QProtobufMessage14QByteArrayViewi(
    QProtobufMessage *message,
    const QByteArrayView *entry,
    int fieldNumber) {
  QProtobufMessagePrivate::storeUnknownEntry(message, *entry, fieldNumber);
}

//  std::optional<QMetaProperty>
//      QProtobufMessagePrivate::metaProperty(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
std::optional<QMetaProperty> *ritual_ZNK23QProtobufMessagePrivate12metaPropertyE14QAnyStringView(
    const QProtobufMessagePrivate *self,
    const QString *name) {
  return new std::optional<QMetaProperty>(
      self->metaProperty(
          QAnyStringView(*name)));
}

//  std::optional<QMetaProperty> QProtobufMessagePrivate::metaProperty(QtProt
//      obufPrivate::QProtobufFieldInfo ord) const
extern "C" Q_DECL_EXPORT
std::optional<QMetaProperty> *ritual_ZNK23QProtobufMessagePrivate12metaPropertyEN17QtProtobufPrivate18QProtobufFieldInfoE(
    const QProtobufMessagePrivate *self,
    const QtProtobufPrivate::QProtobufFieldInfo *ord) {
  return new std::optional<QMetaProperty>(self->metaProperty(*ord));
}

//  QProtobufMessagePrivate *QProtobufMessagePrivate::get(QProtobufMessage
//      *message)
extern "C" Q_DECL_EXPORT
QProtobufMessagePrivate *ritual_ZN23QProtobufMessagePrivate3getEP16QProtobufMessage(
    QProtobufMessage *message) {
  return QProtobufMessagePrivate::get(message);
}

//  const QProtobufMessagePrivate *QProtobufMessagePrivate::get(const
//      QProtobufMessage *message)
extern "C" Q_DECL_EXPORT
const QProtobufMessagePrivate *ritual_ZN23QProtobufMessagePrivate3getEPK16QProtobufMessage(
    const QProtobufMessage *message) {
  return QProtobufMessagePrivate::get(message);
}

//  a std::optional<QMetaProperty> a ritual of QProtobufMessagePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QProtobufMessagePrivate__std_optional_QMetaProperty(
    std::optional<QMetaProperty> *self) {
  delete self;
}
