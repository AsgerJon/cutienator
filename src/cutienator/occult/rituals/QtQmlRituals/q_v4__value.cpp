//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4value_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h>
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

//  Value QV4::Value::fromHeapObject(HeapBasePtr m)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value14fromHeapObjectEPNS_4Heap4BaseE(
    QV4::StaticValue::HeapBasePtr m) {
  return new QV4::Value(QV4::Value::fromHeapObject(m));
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

//  double QV4::Value::toNumberImpl() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV45Value12toNumberImplEv(const QV4::Value *self) {
  return self->toNumberImpl();
}

//  Heap::String *QV4::Value::toString(ExecutionEngine *e) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV45Value8toStringEPNS_15ExecutionEngineE(
    const QV4::Value *self,
    QV4::ExecutionEngine *e) {
  return self->toString(e);
}

//  Heap::Object *QV4::Value::toObject(ExecutionEngine *e) const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV45Value8toObjectEPNS_15ExecutionEngineE(
    const QV4::Value *self,
    QV4::ExecutionEngine *e) {
  return self->toObject(e);
}

//  bool QV4::Value::isPrimitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Value11isPrimitiveEv(const QV4::Value *self) {
  return self->isPrimitive();
}

//  Value QV4::Value::fromReturnedValue(ReturnedValue val)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV45Value17fromReturnedValueEy(
    QV4::ReturnedValue val) {
  return new QV4::Value(QV4::Value::fromReturnedValue(val));
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

//  QV4::Value::~Value()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45ValueD1Ev(QV4::Value *self) {
  delete self;
}
