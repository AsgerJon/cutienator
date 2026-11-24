//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlopenmetaobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlopenmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QQmlOpenMetaObjectType::QQmlOpenMetaObjectType(const QMetaObject *base)
extern "C" Q_DECL_EXPORT
QQmlOpenMetaObjectType *ritual_ZN22QQmlOpenMetaObjectTypeC1EPK11QMetaObject(
    const QMetaObject *base) {
  return new QQmlOpenMetaObjectType(base);
}

//  QQmlOpenMetaObjectType::~QQmlOpenMetaObjectType()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlOpenMetaObjectTypeD1Ev(QQmlOpenMetaObjectType *self) {
  delete self;
}

//  void QQmlOpenMetaObjectType::createProperties(const QList<QByteArray>
//      &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlOpenMetaObjectType16createPropertiesERK5QListI10QByteArrayE(
    QQmlOpenMetaObjectType *self,
    const QList<QByteArray> *names) {
  self->createProperties(*names);
}

//  int QQmlOpenMetaObjectType::createProperty(const QByteArray &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlOpenMetaObjectType14createPropertyERK10QByteArray(
    QQmlOpenMetaObjectType *self,
    const QByteArray *name) {
  return self->createProperty(*name);
}

//  int QQmlOpenMetaObjectType::propertyOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlOpenMetaObjectType14propertyOffsetEv(
    const QQmlOpenMetaObjectType *self) {
  return self->propertyOffset();
}

//  int QQmlOpenMetaObjectType::signalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlOpenMetaObjectType12signalOffsetEv(
    const QQmlOpenMetaObjectType *self) {
  return self->signalOffset();
}

//  int QQmlOpenMetaObjectType::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlOpenMetaObjectType13propertyCountEv(
    const QQmlOpenMetaObjectType *self) {
  return self->propertyCount();
}

//  QByteArray QQmlOpenMetaObjectType::propertyName(int a0) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK22QQmlOpenMetaObjectType12propertyNameEi(
    const QQmlOpenMetaObjectType *self,
    int a0) {
  return new QByteArray(self->propertyName(a0));
}
