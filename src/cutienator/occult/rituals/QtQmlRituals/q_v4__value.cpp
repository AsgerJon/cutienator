//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4value_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 10. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Value QV4::Value::fromStaticValue(StaticValue staticValue)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value15fromStaticValueENS_11StaticValueE(
    const QV4::StaticValue *staticValue) {
  return new QV4::Value(QV4::Value::fromStaticValue(*staticValue));
}

//  Value QV4::Value::undefined()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value9undefinedEv() {
  return new QV4::Value(QV4::Value::undefined());
}

//  bool QV4::Value::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value8isStringEv(const QV4::Value *self) {
  return self->isString();
}

//  bool QV4::Value::isStringOrSymbol() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value16isStringOrSymbolEv(const QV4::Value *self) {
  return self->isStringOrSymbol();
}

//  bool QV4::Value::isSymbol() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value8isSymbolEv(const QV4::Value *self) {
  return self->isSymbol();
}

//  bool QV4::Value::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value8isObjectEv(const QV4::Value *self) {
  return self->isObject();
}

//  bool QV4::Value::isFunctionObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value16isFunctionObjectEv(const QV4::Value *self) {
  return self->isFunctionObject();
}

//  String *QV4::Value::stringValue() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV45Value11stringValueEv(const QV4::Value *self) {
  return self->stringValue();
}

//  StringOrSymbol *QV4::Value::stringOrSymbolValue() const
extern "C" Q_DECL_EXPORT
QV4::StringOrSymbol *ritual_ZNK3QV45Value19stringOrSymbolValueEv(
    const QV4::Value *self) {
  return self->stringOrSymbolValue();
}

//  Symbol *QV4::Value::symbolValue() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV45Value11symbolValueEv(const QV4::Value *self) {
  return self->symbolValue();
}

//  Object *QV4::Value::objectValue() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV45Value11objectValueEv(const QV4::Value *self) {
  return self->objectValue();
}

//  ManagedPtr QV4::Value::managed() const
extern "C" Q_DECL_EXPORT
QV4::Value::ManagedPtr ritual_ZNK3QV45Value7managedEv(
    const QV4::Value *self) {
  return self->managed();
}

//  Value QV4::Value::fromHeapObject(HeapBasePtr m)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value14fromHeapObjectEPNS_4Heap4BaseE(
    QV4::StaticValue::HeapBasePtr m) {
  return new QV4::Value(QV4::Value::fromHeapObject(m));
}

//  int QV4::Value::toUInt16() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV45Value8toUInt16Ev(const QV4::Value *self) {
  return self->toUInt16();
}

//  int QV4::Value::toInt32() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV45Value7toInt32Ev(const QV4::Value *self) {
  return self->toInt32();
}

//  unsigned int QV4::Value::toUInt32() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK3QV45Value8toUInt32Ev(const QV4::Value *self) {
  return self->toUInt32();
}

//  qint64 QV4::Value::toLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK3QV45Value8toLengthEv(const QV4::Value *self) {
  return self->toLength();
}

//  qint64 QV4::Value::toIndex() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK3QV45Value7toIndexEv(const QV4::Value *self) {
  return self->toIndex();
}

//  bool QV4::Value::toBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value9toBooleanEv(const QV4::Value *self) {
  return self->toBoolean();
}

//  bool QV4::Value::toBooleanImpl(Value val)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV45Value13toBooleanImplES0_(const QV4::Value *val) {
  return QV4::Value::toBooleanImpl(*val);
}

//  double QV4::Value::toInteger() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV45Value9toIntegerEv(const QV4::Value *self) {
  return self->toInteger();
}

//  ReturnedValue QV4::Value::convertedToNumber() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV45Value17convertedToNumberEv(
    const QV4::Value *self) {
  return self->convertedToNumber();
}

//  double QV4::Value::toNumber() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV45Value8toNumberEv(const QV4::Value *self) {
  return self->toNumber();
}

//  double QV4::Value::toNumberImpl(Value v)
extern "C" Q_DECL_EXPORT
double ritual_ZN3QV45Value12toNumberImplES0_(const QV4::Value *v) {
  return QV4::Value::toNumberImpl(*v);
}

//  double QV4::Value::toNumberImpl() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV45Value12toNumberImplEv(const QV4::Value *self) {
  return self->toNumberImpl();
}

//  QString QV4::Value::toQStringNoThrow() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV45Value16toQStringNoThrowEv(const QV4::Value *self) {
  return new QString(self->toQStringNoThrow());
}

//  QString QV4::Value::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV45Value9toQStringEv(const QV4::Value *self) {
  return new QString(self->toQString());
}

//  QString QV4::Value::toQString(bool *ok) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV45Value9toQStringEPb(
    const QV4::Value *self,
    bool *ok) {
  return new QString(self->toQString(ok));
}

//  Heap::String *QV4::Value::toString(ExecutionEngine *e) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV45Value8toStringEPNS_15ExecutionEngineE(
    const QV4::Value *self,
    QV4::ExecutionEngine *e) {
  return self->toString(e);
}

//  QV4::PropertyKey QV4::Value::toPropertyKey(ExecutionEngine *e) const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV45Value13toPropertyKeyEPNS_15ExecutionEngineE(
    const QV4::Value *self,
    QV4::ExecutionEngine *e) {
  return new QV4::PropertyKey(self->toPropertyKey(e));
}

//  Heap::String *QV4::Value::toString(ExecutionEngine *e, Value val)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV45Value8toStringEPNS_15ExecutionEngineES0_(
    QV4::ExecutionEngine *e,
    const QV4::Value *val) {
  return QV4::Value::toString(e, *val);
}

//  Heap::Object *QV4::Value::toObject(ExecutionEngine *e) const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV45Value8toObjectEPNS_15ExecutionEngineE(
    const QV4::Value *self,
    QV4::ExecutionEngine *e) {
  return self->toObject(e);
}

//  Heap::Object *QV4::Value::toObject(ExecutionEngine *e, Value val)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV45Value8toObjectEPNS_15ExecutionEngineES0_(
    QV4::ExecutionEngine *e,
    const QV4::Value *val) {
  return QV4::Value::toObject(e, *val);
}

//  bool QV4::Value::isPrimitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value11isPrimitiveEv(const QV4::Value *self) {
  return self->isPrimitive();
}

//  uint QV4::Value::asArrayLength(bool *ok) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV45Value13asArrayLengthEPb(
    const QV4::Value *self,
    bool *ok) {
  return self->asArrayLength(ok);
}

//  Value QV4::Value::fromReturnedValue(ReturnedValue val)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value17fromReturnedValueEy(
    QV4::ReturnedValue val) {
  return new QV4::Value(QV4::Value::fromReturnedValue(val));
}

//  bool QV4::Value::sameValue(Value other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value9sameValueES0_(
    const QV4::Value *self,
    const QV4::Value *other) {
  return self->sameValue(*other);
}

//  bool QV4::Value::sameValueZero(Value other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value13sameValueZeroES0_(
    const QV4::Value *self,
    const QV4::Value *other) {
  return self->sameValueZero(*other);
}

//  void QV4::Value::mark(MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45Value4markEPNS_9MarkStackE(
    QV4::Value *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
}

//  double QV4::Value::toInteger(double d)
extern "C" Q_DECL_EXPORT
double ritual_ZN3QV45Value9toIntegerEd(double d) {
  return QV4::Value::toInteger(d);
}

//  int QV4::Value::toInt32(double d)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV45Value7toInt32Ed(double d) {
  return QV4::Value::toInt32(d);
}

//  unsigned int QV4::Value::toUInt32(double d)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN3QV45Value8toUInt32Ed(double d) {
  return QV4::Value::toUInt32(d);
}

//  Value QV4::Value::emptyValue()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value10emptyValueEv() {
  return new QV4::Value(QV4::Value::emptyValue());
}

//  Value QV4::Value::fromBoolean(bool b)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value11fromBooleanEb(bool b) {
  return new QV4::Value(QV4::Value::fromBoolean(b));
}

//  Value QV4::Value::fromInt32(int i)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value9fromInt32Ei(int i) {
  return new QV4::Value(QV4::Value::fromInt32(i));
}

//  Value QV4::Value::undefinedValue()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value14undefinedValueEv() {
  return new QV4::Value(QV4::Value::undefinedValue());
}

//  Value QV4::Value::nullValue()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value9nullValueEv() {
  return new QV4::Value(QV4::Value::nullValue());
}

//  Value QV4::Value::fromDouble(double d)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value10fromDoubleEd(double d) {
  return new QV4::Value(QV4::Value::fromDouble(d));
}

//  Value QV4::Value::fromUInt32(uint i)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value10fromUInt32Ej(uint i) {
  return new QV4::Value(QV4::Value::fromUInt32(i));
}

//  Value &QV4::Value::operator=(const ScopedValue &v)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45ValueaSERKNS_11ScopedValueE(
    QV4::Value *self,
    const QV4::ScopedValue *v) {
  return &(self->operator=(*v));
}

//  Value &QV4::Value::operator=(ReturnedValue v)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45ValueaSEy(QV4::Value *self, QV4::ReturnedValue v) {
  return &(self->operator=(v));
}

//  Value &QV4::Value::operator=(ManagedPtr m)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45ValueaSEPNS_7ManagedE(
    QV4::Value *self,
    QV4::Value::ManagedPtr m) {
  return &(self->operator=(m));
}

//  Value &QV4::Value::operator=(HeapBasePtr o)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45ValueaSEPNS_4Heap4BaseE(
    QV4::Value *self,
    QV4::StaticValue::HeapBasePtr o) {
  return &(self->operator=(o));
}

//  QV4::Value::~Value()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45ValueD1Ev(QV4::Value *self) {
  delete self;
}

//  QV4::Object *QV4::Value::as<QV4::Object>()
extern "C" Q_DECL_EXPORT
QV4::Object * ritual_ZN3QV45Value2asINS_6ObjectEEEPT_v(
    QV4::Value *self) {
  return self->as<QV4::Object>();
}

//  QV4::String *QV4::Value::as<QV4::String>()
extern "C" Q_DECL_EXPORT
QV4::String * ritual_ZN3QV45Value2asINS_6StringEEEPT_v(
    QV4::Value *self) {
  return self->as<QV4::String>();
}

//  QV4::FunctionObject *QV4::Value::as<QV4::FunctionObject>()
extern "C" Q_DECL_EXPORT
QV4::FunctionObject * ritual_ZN3QV45Value2asINS_14FunctionObjectEEEPT_v(
    QV4::Value *self) {
  return self->as<QV4::FunctionObject>();
}

//  QV4::ArrayObject *QV4::Value::as<QV4::ArrayObject>()
extern "C" Q_DECL_EXPORT
QV4::ArrayObject * ritual_ZN3QV45Value2asINS_11ArrayObjectEEEPT_v(
    QV4::Value *self) {
  return self->as<QV4::ArrayObject>();
}

//  QV4::QObjectWrapper *QV4::Value::as<QV4::QObjectWrapper>()
extern "C" Q_DECL_EXPORT
QV4::QObjectWrapper * ritual_ZN3QV45Value2asINS_14QObjectWrapperEEEPT_v(
    QV4::Value *self) {
  return self->as<QV4::QObjectWrapper>();
}

//  QV4::Object *QV4::Value::cast<QV4::Object>()
extern "C" Q_DECL_EXPORT
QV4::Object * ritual_ZN3QV45Value4castINS_6ObjectEEEPT_v(
    QV4::Value *self) {
  return self->cast<QV4::Object>();
}

//  QV4::String *QV4::Value::cast<QV4::String>()
extern "C" Q_DECL_EXPORT
QV4::String * ritual_ZN3QV45Value4castINS_6StringEEEPT_v(
    QV4::Value *self) {
  return self->cast<QV4::String>();
}

//  QV4::FunctionObject *QV4::Value::cast<QV4::FunctionObject>()
extern "C" Q_DECL_EXPORT
QV4::FunctionObject * ritual_ZN3QV45Value4castINS_14FunctionObjectEEEPT_v(
    QV4::Value *self) {
  return self->cast<QV4::FunctionObject>();
}

//  QV4::ArrayObject *QV4::Value::cast<QV4::ArrayObject>()
extern "C" Q_DECL_EXPORT
QV4::ArrayObject * ritual_ZN3QV45Value4castINS_11ArrayObjectEEEPT_v(
    QV4::Value *self) {
  return self->cast<QV4::ArrayObject>();
}

//  QV4::QObjectWrapper *QV4::Value::cast<QV4::QObjectWrapper>()
extern "C" Q_DECL_EXPORT
QV4::QObjectWrapper * ritual_ZN3QV45Value4castINS_14QObjectWrapperEEEPT_v(
    QV4::Value *self) {
  return self->cast<QV4::QObjectWrapper>();
}
