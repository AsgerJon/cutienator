//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 2.
//  Kept as it is when the generator runs again. Also added by hand on
//  2026-11-25, rituals for functions the generator leaves out: 2.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4staticvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::StaticValue::StaticValue()
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValueC1Ev() {
  return new QV4::StaticValue();
}

//  QV4::StaticValue::StaticValue(quint64 val)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValueC1Ey(quint64 val) {
  return new QV4::StaticValue(val);
}

//  StaticValue &QV4::StaticValue::operator=(ReturnedValue v)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValueaSEy(
    QV4::StaticValue *self,
    QV4::ReturnedValue v) {
  return &(self->operator=(v));
}

//  quint64 QV4::StaticValue::rawValue() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK3QV411StaticValue8rawValueEv(
    const QV4::StaticValue *self) {
  return self->rawValue();
}

//  void QV4::StaticValue::setRawValue(quint64 raw)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue11setRawValueEy(
    QV4::StaticValue *self,
    quint64 raw) {
  self->setRawValue(raw);
}

#if Q_BYTE_ORDER == Q_LITTLE_ENDIAN
//  int QV4::StaticValue::valueOffset()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV411StaticValue11valueOffsetEv() {
  return QV4::StaticValue::valueOffset();
}
#endif  // Q_BYTE_ORDER == Q_LITTLE_ENDIAN

#if Q_BYTE_ORDER == Q_LITTLE_ENDIAN
//  int QV4::StaticValue::tagOffset()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV411StaticValue9tagOffsetEv() {
  return QV4::StaticValue::tagOffset();
}
#endif  // Q_BYTE_ORDER == Q_LITTLE_ENDIAN

//  quint64 QV4::StaticValue::tagValue(quint32 tag, quint32 value)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN3QV411StaticValue8tagValueEjj(quint32 tag, quint32 value) {
  return QV4::StaticValue::tagValue(tag, value);
}

//  void QV4::StaticValue::setTagValue(quint32 tag, quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue11setTagValueEjj(
    QV4::StaticValue *self,
    quint32 tag,
    quint32 value) {
  self->setTagValue(tag, value);
}

//  quint32 QV4::StaticValue::value() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV411StaticValue5valueEv(const QV4::StaticValue *self) {
  return self->value();
}

//  quint32 QV4::StaticValue::tag() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV411StaticValue3tagEv(const QV4::StaticValue *self) {
  return self->tag();
}

//  void QV4::StaticValue::setTag(quint32 tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue6setTagEj(
    QV4::StaticValue *self,
    quint32 tag) {
  self->setTag(tag);
}

//  int QV4::StaticValue::int_32() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV411StaticValue6int_32Ev(const QV4::StaticValue *self) {
  return self->int_32();
}

//  void QV4::StaticValue::setInt_32(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue9setInt_32Ei(QV4::StaticValue *self, int i) {
  self->setInt_32(i);
}

//  uint QV4::StaticValue::uint_32() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV411StaticValue7uint_32Ev(const QV4::StaticValue *self) {
  return self->uint_32();
}

//  void QV4::StaticValue::setEmpty()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue8setEmptyEv(QV4::StaticValue *self) {
  self->setEmpty();
}

//  quint64 QV4::StaticValue::tagBitMask(TagBit bit)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN3QV411StaticValue10tagBitMaskENS0_6TagBitE(
    QV4::StaticValue::TagBit bit) {
  return QV4::StaticValue::tagBitMask(bit);
}

//  Type QV4::StaticValue::type() const
extern "C" Q_DECL_EXPORT
QV4::StaticValue::Type ritual_ZNK3QV411StaticValue4typeEv(
    const QV4::StaticValue *self) {
  return self->type();
}

//  quint64 QV4::StaticValue::quickType() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK3QV411StaticValue9quickTypeEv(
    const QV4::StaticValue *self) {
  return self->quickType();
}

//  bool QV4::StaticValue::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue7isEmptyEv(const QV4::StaticValue *self) {
  return self->isEmpty();
}

//  bool QV4::StaticValue::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue6isNullEv(const QV4::StaticValue *self) {
  return self->isNull();
}

//  bool QV4::StaticValue::isBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue9isBooleanEv(const QV4::StaticValue *self) {
  return self->isBoolean();
}

//  bool QV4::StaticValue::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue9isIntegerEv(const QV4::StaticValue *self) {
  return self->isInteger();
}

//  bool QV4::StaticValue::isNullOrUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue17isNullOrUndefinedEv(
    const QV4::StaticValue *self) {
  return self->isNullOrUndefined();
}

//  bool QV4::StaticValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue11isUndefinedEv(
    const QV4::StaticValue *self) {
  return self->isUndefined();
}

//  bool QV4::StaticValue::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue8isDoubleEv(const QV4::StaticValue *self) {
  return self->isDouble();
}

//  bool QV4::StaticValue::isNumber() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue8isNumberEv(const QV4::StaticValue *self) {
  return self->isNumber();
}

//  bool QV4::StaticValue::isManagedOrUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue20isManagedOrUndefinedEv(
    const QV4::StaticValue *self) {
  return self->isManagedOrUndefined();
}

//  bool QV4::StaticValue::isManaged() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue9isManagedEv(const QV4::StaticValue *self) {
  return self->isManaged();
}

//  bool QV4::StaticValue::isIntOrBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue11isIntOrBoolEv(
    const QV4::StaticValue *self) {
  return self->isIntOrBool();
}

//  bool QV4::StaticValue::integerCompatible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue17integerCompatibleEv(
    const QV4::StaticValue *self) {
  return self->integerCompatible();
}

//  bool QV4::StaticValue::integerCompatible(StaticValue a, StaticValue b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411StaticValue17integerCompatibleES0_S0_(
    const QV4::StaticValue *a,
    const QV4::StaticValue *b) {
  return QV4::StaticValue::integerCompatible(*a, *b);
}

//  bool QV4::StaticValue::bothDouble(StaticValue a, StaticValue b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411StaticValue10bothDoubleES0_S0_(
    const QV4::StaticValue *a,
    const QV4::StaticValue *b) {
  return QV4::StaticValue::bothDouble(*a, *b);
}

//  bool QV4::StaticValue::isNaN() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue5isNaNEv(const QV4::StaticValue *self) {
  return self->isNaN();
}

//  bool QV4::StaticValue::isPositiveInt() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue13isPositiveIntEv(
    const QV4::StaticValue *self) {
  return self->isPositiveInt();
}

//  double QV4::StaticValue::doubleValue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV411StaticValue11doubleValueEv(
    const QV4::StaticValue *self) {
  return self->doubleValue();
}

//  void QV4::StaticValue::setDouble(double d)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue9setDoubleEd(
    QV4::StaticValue *self,
    double d) {
  self->setDouble(d);
}

//  bool QV4::StaticValue::isInt32()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411StaticValue7isInt32Ev(QV4::StaticValue *self) {
  return self->isInt32();
}

//  bool QV4::StaticValue::isInt32(double d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411StaticValue7isInt32Ed(double d) {
  return QV4::StaticValue::isInt32(d);
}

//  double QV4::StaticValue::asDouble() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV411StaticValue8asDoubleEv(const QV4::StaticValue *self) {
  return self->asDouble();
}

//  bool QV4::StaticValue::booleanValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue12booleanValueEv(
    const QV4::StaticValue *self) {
  return self->booleanValue();
}

//  int QV4::StaticValue::integerValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV411StaticValue12integerValueEv(
    const QV4::StaticValue *self) {
  return self->integerValue();
}

//  bool QV4::StaticValue::tryIntegerConversion()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411StaticValue20tryIntegerConversionEv(
    QV4::StaticValue *self) {
  return self->tryIntegerConversion();
}

//  bool QV4::StaticValue::toBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV411StaticValue9toBooleanEv(const QV4::StaticValue *self) {
  return self->toBoolean();
}

//  int QV4::StaticValue::toInt32() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV411StaticValue7toInt32Ev(const QV4::StaticValue *self) {
  return self->toInt32();
}

//  ReturnedValue QV4::StaticValue::asReturnedValue() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV411StaticValue15asReturnedValueEv(
    const QV4::StaticValue *self) {
  return self->asReturnedValue();
}

//  StaticValue QV4::StaticValue::fromReturnedValue(ReturnedValue val)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue17fromReturnedValueEy(
    QV4::ReturnedValue val) {
  return new QV4::StaticValue(QV4::StaticValue::fromReturnedValue(val));
}

//  StaticValue QV4::StaticValue::emptyValue()
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue10emptyValueEv() {
  return new QV4::StaticValue(QV4::StaticValue::emptyValue());
}

//  StaticValue QV4::StaticValue::fromBoolean(bool b)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue11fromBooleanEb(bool b) {
  return new QV4::StaticValue(QV4::StaticValue::fromBoolean(b));
}

//  StaticValue QV4::StaticValue::fromInt32(int i)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue9fromInt32Ei(int i) {
  return new QV4::StaticValue(QV4::StaticValue::fromInt32(i));
}

//  StaticValue QV4::StaticValue::undefinedValue()
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue14undefinedValueEv() {
  return new QV4::StaticValue(QV4::StaticValue::undefinedValue());
}

//  StaticValue QV4::StaticValue::nullValue()
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue9nullValueEv() {
  return new QV4::StaticValue(QV4::StaticValue::nullValue());
}

//  StaticValue QV4::StaticValue::fromDouble(double d)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue10fromDoubleEd(double d) {
  return new QV4::StaticValue(QV4::StaticValue::fromDouble(d));
}

//  StaticValue QV4::StaticValue::fromUInt32(uint i)
extern "C" Q_DECL_EXPORT
QV4::StaticValue *ritual_ZN3QV411StaticValue10fromUInt32Ej(uint i) {
  return new QV4::StaticValue(QV4::StaticValue::fromUInt32(i));
}

//  double QV4::StaticValue::toInteger(double d)
extern "C" Q_DECL_EXPORT
double ritual_ZN3QV411StaticValue9toIntegerEd(double d) {
  return QV4::StaticValue::toInteger(d);
}

//  int QV4::StaticValue::toInt32(double d)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV411StaticValue7toInt32Ed(double d) {
  return QV4::StaticValue::toInt32(d);
}

//  unsigned int QV4::StaticValue::toUInt32(double d)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN3QV411StaticValue8toUInt32Ed(double d) {
  return QV4::StaticValue::toUInt32(d);
}

#if QT_POINTER_SIZE == 8
//  HeapBasePtr QV4::StaticValue::m() const
extern "C" Q_DECL_EXPORT
QV4::StaticValue::HeapBasePtr ritual_ZNK3QV411StaticValue1mEv(
    const QV4::StaticValue *self) {
  return self->m();
}
#endif  // QT_POINTER_SIZE == 8

#if QT_POINTER_SIZE == 8
//  void QV4::StaticValue::setM(HeapBasePtr b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValue4setMEPNS_4Heap4BaseE(
    QV4::StaticValue *self,
    QV4::StaticValue::HeapBasePtr b) {
  self->setM(b);
}
#endif  // QT_POINTER_SIZE == 8

//  QV4::StaticValue::~StaticValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411StaticValueD1Ev(QV4::StaticValue *self) {
  delete self;
}

//  const QV4::Value &QV4::StaticValue::asValue<QV4::Value>() const
extern "C" Q_DECL_EXPORT
const QV4::Value * ritual_ZNK3QV411StaticValue7asValueINS_5ValueEEERKT_v(
    const QV4::StaticValue *self) {
  return &(self->asValue<QV4::Value>());
}

//  QV4::Value &QV4::StaticValue::asValue<QV4::Value>()
extern "C" Q_DECL_EXPORT
QV4::Value * ritual_ZN3QV411StaticValue7asValueINS_5ValueEEERT_v(
    QV4::StaticValue *self) {
  return &(self->asValue<QV4::Value>());
}

//  ReturnedValue *QV4::StaticValue::data_ptr()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue *ritual_ZN3QV411StaticValue8data_ptrEv(
    QV4::StaticValue *self) {
  return self->data_ptr();
}

//  quint64 &QV4::StaticValue::rawValueRef()
extern "C" Q_DECL_EXPORT
quint64 *ritual_ZN3QV411StaticValue11rawValueRefEv(
    QV4::StaticValue *self) {
  return &(self->rawValueRef());
}
