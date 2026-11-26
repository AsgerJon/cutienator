//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 6.
//  Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qvarlengtharray.h>

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

//  QQmlMetaObject &QQmlMetaObject::operator=(const QQmlMetaObject &a0)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN14QQmlMetaObjectaSERKS_(
    QQmlMetaObject *self,
    const QQmlMetaObject *a0) {
  return &(self->operator=(*a0));
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

//  void QQmlMetaObject::resolveGadgetMethodOrPropertyIndex(QMetaObject::Call
//      type, const QMetaObject **metaObject, int *index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlMetaObject34resolveGadgetMethodOrPropertyIndexEN11QMetaObject4CallEPPKS0_Pi(
    QMetaObject::Call type,
    const QMetaObject **metaObject,
    int *index) {
  QQmlMetaObject::resolveGadgetMethodOrPropertyIndex(
      type,
      metaObject,
      index);
}

//  QQmlMetaObject::~QQmlMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlMetaObjectD1Ev(QQmlMetaObject *self) {
  delete self;
}

//  bool QQmlMetaObject::methodParameterTypes<QVarLengthArray<QMetaType, 9>>(
//      const QQmlPropertyData &data, QVarLengthArray<QMetaType, 9>
//      *argStorage, QString *unknownTypeError = nullptr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlMetaObject20methodParameterTypesI15QVarLengthArrayI9QMetaTypeLx9EEEEbRK16QQmlPropertyDataPT_P7QString(
    QQmlMetaObject *self,
    const QQmlPropertyData *data,
    QVarLengthArray<QMetaType, 9> *argStorage,
    QString *unknownTypeError) {
  return self->methodParameterTypes<QVarLengthArray<QMetaType, 9>>(
      *data, argStorage, unknownTypeError);
}

//  static bool QQmlMetaObject::methodParameterTypes<QVarLengthArray<
//      QMetaType, 9>>(const QMetaMethod &method, QVarLengthArray<QMetaType,
//      9> *argStorage, QString *unknownTypeError = nullptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlMetaObject20methodParameterTypesI15QVarLengthArrayI9QMetaTypeLx9EEEEbRK11QMetaMethodPT_P7QString(
    const QMetaMethod *method,
    QVarLengthArray<QMetaType, 9> *argStorage,
    QString *unknownTypeError) {
  return QQmlMetaObject::methodParameterTypes<QVarLengthArray<QMetaType, 9>>(
      *method, argStorage, unknownTypeError);
}

//  bool QQmlMetaObject::methodReturnAndParameterTypes<QVarLengthArray<
//      QMetaType, 10>>(const QQmlPropertyData &data, QVarLengthArray<
//      QMetaType, 10> *argStorage, QString *unknownTypeError = nullptr)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlMetaObject29methodReturnAndParameterTypesI15QVarLengthArrayI9QMetaTypeLx10EEEEbRK16QQmlPropertyDataPT_P7QString(
    QQmlMetaObject *self,
    const QQmlPropertyData *data,
    QVarLengthArray<QMetaType, 10> *argStorage,
    QString *unknownTypeError) {
  return self->methodReturnAndParameterTypes<QVarLengthArray<QMetaType, 10>>(
      *data, argStorage, unknownTypeError);
}

//  bool QQmlMetaObject::methodReturnAndParameterTypes<QVarLengthArray<
//      QMetaType, 10>>(const QQmlPropertyData &data, const QMetaMethod
//      &method, QVarLengthArray<QMetaType, 10> *argStorage, QString
//      *unknownTypeError = nullptr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlMetaObject29methodReturnAndParameterTypesI15QVarLengthArrayI9QMetaTypeLx10EEEEbRK16QQmlPropertyDataRK11QMetaMethodPT_P7QString(
    QQmlMetaObject *self,
    const QQmlPropertyData *data,
    const QMetaMethod *method,
    QVarLengthArray<QMetaType, 10> *argStorage,
    QString *unknownTypeError) {
  return self->methodReturnAndParameterTypes<QVarLengthArray<QMetaType, 10>>(
      *data, *method, argStorage, unknownTypeError);
}

//  bool QQmlMetaObject::constructorParameterTypes<QVarLengthArray<QMetaType,
//      9>>(const QQmlPropertyData &data, QVarLengthArray<QMetaType, 9>
//      *argStorage, QString *unknownTypeError = nullptr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlMetaObject25constructorParameterTypesI15QVarLengthArrayI9QMetaTypeLx9EEEEbRK16QQmlPropertyDataPT_P7QString(
    QQmlMetaObject *self,
    const QQmlPropertyData *data,
    QVarLengthArray<QMetaType, 9> *argStorage,
    QString *unknownTypeError) {
  return self->constructorParameterTypes<QVarLengthArray<QMetaType, 9>>(
      *data, argStorage, unknownTypeError);
}

//  bool QQmlMetaObject::constructorReturnAndParameterTypes<QVarLengthArray<
//      QMetaType, 10>>(const QQmlPropertyData &data, QVarLengthArray<
//      QMetaType, 10> *argStorage, QString *unknownTypeError = nullptr)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlMetaObject34constructorReturnAndParameterTypesI15QVarLengthArrayI9QMetaTypeLx10EEEEbRK16QQmlPropertyDataPT_P7QString(
    QQmlMetaObject *self,
    const QQmlPropertyData *data,
    QVarLengthArray<QMetaType, 10> *argStorage,
    QString *unknownTypeError) {
  return self->constructorReturnAndParameterTypes<QVarLengthArray<QMetaType, 10>>(
      *data, argStorage, unknownTypeError);
}
