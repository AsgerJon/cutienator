//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  QQmlMetaObject::QQmlMetaObject()
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN14QQmlMetaObjectC1Ev() {
  return new QQmlMetaObject();
}

//  QQmlMetaObject::QQmlMetaObject(const QObject *a0)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN14QQmlMetaObjectC1EPK7QObject(const QObject *a0) {
  return new QQmlMetaObject(a0);
}

//  QQmlMetaObject::QQmlMetaObject(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN14QQmlMetaObjectC1EPK11QMetaObject(
    const QMetaObject *a0) {
  return new QQmlMetaObject(a0);
}

//  QQmlMetaObject::QQmlMetaObject(const QQmlPropertyCache::ConstPtr &a0)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN14QQmlMetaObjectC1ERKN17QQmlPropertyCache8ConstPtrE(
    const QQmlPropertyCache::ConstPtr *a0) {
  return new QQmlMetaObject(*a0);
}

//  QQmlMetaObject::QQmlMetaObject(const QQmlMetaObject &a0)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN14QQmlMetaObjectC1ERKS_(const QQmlMetaObject *a0) {
  return new QQmlMetaObject(*a0);
}

//  bool QQmlMetaObject::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlMetaObject6isNullEv(const QQmlMetaObject *self) {
  return self->isNull();
}

//  const char *QQmlMetaObject::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK14QQmlMetaObject9classNameEv(
    const QQmlMetaObject *self) {
  return self->className();
}

//  int QQmlMetaObject::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlMetaObject13propertyCountEv(const QQmlMetaObject *self) {
  return self->propertyCount();
}

//  const QMetaObject *QQmlMetaObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlMetaObject10metaObjectEv(
    const QQmlMetaObject *self) {
  return self->metaObject();
}

//  QMetaType QQmlMetaObject::methodReturnType(const QQmlPropertyData &data,
//      QString *unknownTypeError) const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK14QQmlMetaObject16methodReturnTypeERK16QQmlPropertyDataP7QString(
    const QQmlMetaObject *self,
    const QQmlPropertyData *data,
    QString *unknownTypeError) {
  return new QMetaType(self->methodReturnType(*data, unknownTypeError));
}

//  bool QQmlMetaObject::canConvert(const QQmlMetaObject &from, const
//      QQmlMetaObject &to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlMetaObject10canConvertERKS_S1_(
    const QQmlMetaObject *from,
    const QQmlMetaObject *to) {
  return QQmlMetaObject::canConvert(*from, *to);
}

//  QQmlMetaObject::~QQmlMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlMetaObjectD1Ev(QQmlMetaObject *self) {
  delete self;
}
