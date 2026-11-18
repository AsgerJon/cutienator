//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qbytearray.h>

//  const char *QMetaObject::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK11QMetaObject9classNameEv(const QMetaObject *self) {
  return self->className();
}

//  const QMetaObject *QMetaObject::superClass() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMetaObject10superClassEv(
    const QMetaObject *self) {
  return self->superClass();
}

//  bool QMetaObject::inherits(const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMetaObject8inheritsEPKS_(
    const QMetaObject *self,
    const QMetaObject *metaObject) {
  return self->inherits(metaObject);
}

//  QObject *QMetaObject::cast(QObject *obj) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QMetaObject4castEP7QObject(
    const QMetaObject *self,
    QObject *obj) {
  return self->cast(obj);
}

//  const QObject *QMetaObject::cast(const QObject *obj) const
extern "C" Q_DECL_EXPORT
const QObject *ritual_ZNK11QMetaObject4castEPK7QObject(
    const QMetaObject *self,
    const QObject *obj) {
  return self->cast(obj);
}

//  QString QMetaObject::tr(const char *s, const char *c, int n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMetaObject2trEPKcS1_i(
    const QMetaObject *self,
    const char *s,
    const char *c,
    int n) {
  return new QString(self->tr(s, c, n));
}

//  QMetaType QMetaObject::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK11QMetaObject8metaTypeEv(const QMetaObject *self) {
  return new QMetaType(self->metaType());
}

//  int QMetaObject::methodOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject12methodOffsetEv(const QMetaObject *self) {
  return self->methodOffset();
}

//  int QMetaObject::enumeratorOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject16enumeratorOffsetEv(const QMetaObject *self) {
  return self->enumeratorOffset();
}

//  int QMetaObject::propertyOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject14propertyOffsetEv(const QMetaObject *self) {
  return self->propertyOffset();
}

//  int QMetaObject::classInfoOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject15classInfoOffsetEv(const QMetaObject *self) {
  return self->classInfoOffset();
}

//  int QMetaObject::constructorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject16constructorCountEv(const QMetaObject *self) {
  return self->constructorCount();
}

//  int QMetaObject::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject11methodCountEv(const QMetaObject *self) {
  return self->methodCount();
}

//  int QMetaObject::enumeratorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject15enumeratorCountEv(const QMetaObject *self) {
  return self->enumeratorCount();
}

//  int QMetaObject::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject13propertyCountEv(const QMetaObject *self) {
  return self->propertyCount();
}

//  int QMetaObject::classInfoCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject14classInfoCountEv(const QMetaObject *self) {
  return self->classInfoCount();
}

//  int QMetaObject::indexOfConstructor(const char *constructor) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject18indexOfConstructorEPKc(
    const QMetaObject *self,
    const char *constructor) {
  return self->indexOfConstructor(constructor);
}

//  int QMetaObject::indexOfMethod(const char *method) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject13indexOfMethodEPKc(
    const QMetaObject *self,
    const char *method) {
  return self->indexOfMethod(method);
}

//  int QMetaObject::indexOfSignal(const char *signal) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject13indexOfSignalEPKc(
    const QMetaObject *self,
    const char *signal) {
  return self->indexOfSignal(signal);
}

//  int QMetaObject::indexOfSlot(const char *slot) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject11indexOfSlotEPKc(
    const QMetaObject *self,
    const char *slot) {
  return self->indexOfSlot(slot);
}

//  int QMetaObject::indexOfEnumerator(const char *name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject17indexOfEnumeratorEPKc(
    const QMetaObject *self,
    const char *name) {
  return self->indexOfEnumerator(name);
}

//  int QMetaObject::indexOfProperty(const char *name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject15indexOfPropertyEPKc(
    const QMetaObject *self,
    const char *name) {
  return self->indexOfProperty(name);
}

//  int QMetaObject::indexOfClassInfo(const char *name) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMetaObject16indexOfClassInfoEPKc(
    const QMetaObject *self,
    const char *name) {
  return self->indexOfClassInfo(name);
}

//  QMetaMethod QMetaObject::constructor(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZNK11QMetaObject11constructorEi(
    const QMetaObject *self,
    int index) {
  return new QMetaMethod(self->constructor(index));
}

//  QMetaMethod QMetaObject::method(int index) const
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZNK11QMetaObject6methodEi(
    const QMetaObject *self,
    int index) {
  return new QMetaMethod(self->method(index));
}

//  QMetaEnum QMetaObject::enumerator(int index) const
extern "C" Q_DECL_EXPORT
QMetaEnum *ritual_ZNK11QMetaObject10enumeratorEi(
    const QMetaObject *self,
    int index) {
  return new QMetaEnum(self->enumerator(index));
}

//  QMetaProperty QMetaObject::property(int index) const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK11QMetaObject8propertyEi(
    const QMetaObject *self,
    int index) {
  return new QMetaProperty(self->property(index));
}

//  QMetaClassInfo QMetaObject::classInfo(int index) const
extern "C" Q_DECL_EXPORT
QMetaClassInfo *ritual_ZNK11QMetaObject9classInfoEi(
    const QMetaObject *self,
    int index) {
  return new QMetaClassInfo(self->classInfo(index));
}

//  QMetaProperty QMetaObject::userProperty() const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK11QMetaObject12userPropertyEv(
    const QMetaObject *self) {
  return new QMetaProperty(self->userProperty());
}

//  bool QMetaObject::checkConnectArgs(const char *signal, const char
//      *method)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject16checkConnectArgsEPKcS1_(
    const char *signal,
    const char *method) {
  return QMetaObject::checkConnectArgs(signal, method);
}

//  bool QMetaObject::checkConnectArgs(const QMetaMethod &signal, const
//      QMetaMethod &method)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject16checkConnectArgsERK11QMetaMethodS2_(
    const QMetaMethod *signal,
    const QMetaMethod *method) {
  return QMetaObject::checkConnectArgs(*signal, *method);
}

//  QByteArray QMetaObject::normalizedSignature(const char *method)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QMetaObject19normalizedSignatureEPKc(
    const char *method) {
  return new QByteArray(QMetaObject::normalizedSignature(method));
}

//  QByteArray QMetaObject::normalizedType(const char *type)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QMetaObject14normalizedTypeEPKc(const char *type) {
  return new QByteArray(QMetaObject::normalizedType(type));
}

//  bool QMetaObject::disconnect(const QObject *sender, int signal_index,
//      const QObject *receiver, int method_index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject10disconnectEPK7QObjectiS2_i(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    int method_index) {
  return QMetaObject::disconnect(
      sender,
      signal_index,
      receiver,
      method_index);
}

//  bool QMetaObject::disconnectOne(const QObject *sender, int signal_index,
//      const QObject *receiver, int method_index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject13disconnectOneEPK7QObjectiS2_i(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    int method_index) {
  return QMetaObject::disconnectOne(
      sender,
      signal_index,
      receiver,
      method_index);
}

//  void QMetaObject::connectSlotsByName(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaObject18connectSlotsByNameEP7QObject(QObject *o) {
  QMetaObject::connectSlotsByName(o);
}

//  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
//      Qt::ConnectionType a2, QGenericReturnArgument ret, QGenericArgument
//      val0, QGenericArgument val1, QGenericArgument val2, QGenericArgument
//      val3, QGenericArgument val4, QGenericArgument val5, QGenericArgument
//      val6, QGenericArgument val7, QGenericArgument val8, QGenericArgument
//      val9)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKcN2Qt14ConnectionTypeE22QGenericReturnArgument16QGenericArgumentS7_S7_S7_S7_S7_S7_S7_S7_S7_(
    QObject *obj,
    const char *member,
    Qt::ConnectionType a2,
    const QGenericReturnArgument *ret,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return QMetaObject::invokeMethod(
      obj,
      member,
      a2,
      *ret,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}

//  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
//      QGenericReturnArgument ret, QGenericArgument val0, QGenericArgument
//      val1, QGenericArgument val2, QGenericArgument val3, QGenericArgument
//      val4, QGenericArgument val5, QGenericArgument val6, QGenericArgument
//      val7, QGenericArgument val8, QGenericArgument val9)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKc22QGenericReturnArgument16QGenericArgumentS5_S5_S5_S5_S5_S5_S5_S5_S5_(
    QObject *obj,
    const char *member,
    const QGenericReturnArgument *ret,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return QMetaObject::invokeMethod(
      obj,
      member,
      *ret,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}

//  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
//      Qt::ConnectionType type, QGenericArgument val0, QGenericArgument
//      val1, QGenericArgument val2, QGenericArgument val3, QGenericArgument
//      val4, QGenericArgument val5, QGenericArgument val6, QGenericArgument
//      val7, QGenericArgument val8, QGenericArgument val9)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKcN2Qt14ConnectionTypeE16QGenericArgumentS6_S6_S6_S6_S6_S6_S6_S6_S6_(
    QObject *obj,
    const char *member,
    Qt::ConnectionType type,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return QMetaObject::invokeMethod(
      obj,
      member,
      type,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}

//  bool QMetaObject::invokeMethod(QObject *obj, const char *member,
//      QGenericArgument val0, QGenericArgument val1, QGenericArgument val2,
//      QGenericArgument val3, QGenericArgument val4, QGenericArgument val5,
//      QGenericArgument val6, QGenericArgument val7, QGenericArgument val8,
//      QGenericArgument val9)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMetaObject12invokeMethodEP7QObjectPKc16QGenericArgumentS4_S4_S4_S4_S4_S4_S4_S4_S4_(
    QObject *obj,
    const char *member,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return QMetaObject::invokeMethod(
      obj,
      member,
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}

//  QObject *QMetaObject::newInstance(QGenericArgument val0, QGenericArgument
//      val1, QGenericArgument val2, QGenericArgument val3, QGenericArgument
//      val4, QGenericArgument val5, QGenericArgument val6, QGenericArgument
//      val7, QGenericArgument val8, QGenericArgument val9) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK11QMetaObject11newInstanceE16QGenericArgumentS0_S0_S0_S0_S0_S0_S0_S0_S0_(
    const QMetaObject *self,
    const QGenericArgument *val0,
    const QGenericArgument *val1,
    const QGenericArgument *val2,
    const QGenericArgument *val3,
    const QGenericArgument *val4,
    const QGenericArgument *val5,
    const QGenericArgument *val6,
    const QGenericArgument *val7,
    const QGenericArgument *val8,
    const QGenericArgument *val9) {
  return self->newInstance(
      *val0,
      *val1,
      *val2,
      *val3,
      *val4,
      *val5,
      *val6,
      *val7,
      *val8,
      *val9);
}

//  QMetaObject::~QMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMetaObjectD1Ev(QMetaObject *self) {
  delete self;
}
