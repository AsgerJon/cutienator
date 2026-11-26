//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsprimitivevalue.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtQml/QtQml>
#include <QtQml/qjsprimitivevalue.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>

//  Type QJSPrimitiveValue::type() const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue::Type ritual_ZNK17QJSPrimitiveValue4typeEv(
    const QJSPrimitiveValue *self) {
  return self->type();
}

//  QJSPrimitiveValue::QJSPrimitiveValue()
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1Ev() {
  return new QJSPrimitiveValue();
}

//  QJSPrimitiveValue::QJSPrimitiveValue(QJSPrimitiveUndefined undefined)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1E21QJSPrimitiveUndefined(
    const QJSPrimitiveUndefined *undefined) {
  return new QJSPrimitiveValue(*undefined);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(QJSPrimitiveNull null)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1E16QJSPrimitiveNull(
    const QJSPrimitiveNull *null) {
  return new QJSPrimitiveValue(*null);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(bool value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1Eb(bool value) {
  return new QJSPrimitiveValue(value);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(int value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1Ei(int value) {
  return new QJSPrimitiveValue(value);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(double value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1Ed(double value) {
  return new QJSPrimitiveValue(value);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(QString string)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1E7QString(
    const QString *string) {
  return new QJSPrimitiveValue(*string);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(const QMetaType type, const void
//      *value)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1E9QMetaTypePKv(
    const QMetaType *type,
    const void *value) {
  return new QJSPrimitiveValue(*type, value);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(QMetaType type)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1E9QMetaType(
    const QMetaType *type) {
  return new QJSPrimitiveValue(*type);
}

//  QJSPrimitiveValue::QJSPrimitiveValue(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueC1ERK8QVariant(
    const QVariant *variant) {
  return new QJSPrimitiveValue(*variant);
}

//  void *QJSPrimitiveValue::data()
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QJSPrimitiveValue4dataEv(QJSPrimitiveValue *self) {
  return self->data();
}

//  const void *QJSPrimitiveValue::data() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK17QJSPrimitiveValue4dataEv(
    const QJSPrimitiveValue *self) {
  return self->data();
}

//  const void *QJSPrimitiveValue::constData() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK17QJSPrimitiveValue9constDataEv(
    const QJSPrimitiveValue *self) {
  return self->constData();
}

//  bool QJSPrimitiveValue::toBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSPrimitiveValue9toBooleanEv(
    const QJSPrimitiveValue *self) {
  return self->toBoolean();
}

//  int QJSPrimitiveValue::toInteger() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QJSPrimitiveValue9toIntegerEv(
    const QJSPrimitiveValue *self) {
  return self->toInteger();
}

//  double QJSPrimitiveValue::toDouble() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK17QJSPrimitiveValue8toDoubleEv(
    const QJSPrimitiveValue *self) {
  return self->toDouble();
}

//  QString QJSPrimitiveValue::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QJSPrimitiveValue8toStringEv(
    const QJSPrimitiveValue *self) {
  return new QString(self->toString());
}

//  QJSPrimitiveValue operator+(const QJSPrimitiveValue &lhs, const
//      QJSPrimitiveValue &rhs)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZplRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return new QJSPrimitiveValue(operator+(*lhs, *rhs));
}

//  QJSPrimitiveValue operator-(const QJSPrimitiveValue &lhs, const
//      QJSPrimitiveValue &rhs)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZmiRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return new QJSPrimitiveValue(operator-(*lhs, *rhs));
}

//  QJSPrimitiveValue operator*(const QJSPrimitiveValue &lhs, const
//      QJSPrimitiveValue &rhs)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZmlRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return new QJSPrimitiveValue(operator*(*lhs, *rhs));
}

//  QJSPrimitiveValue operator/(const QJSPrimitiveValue &lhs, const
//      QJSPrimitiveValue &rhs)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZdvRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return new QJSPrimitiveValue(operator/(*lhs, *rhs));
}

//  QJSPrimitiveValue operator%(const QJSPrimitiveValue &lhs, const
//      QJSPrimitiveValue &rhs)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZrmRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return new QJSPrimitiveValue(operator%(*lhs, *rhs));
}

//  QJSPrimitiveValue &QJSPrimitiveValue::operator++()
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueppEv(
    QJSPrimitiveValue *self) {
  return &(self->operator++());
}

//  QJSPrimitiveValue QJSPrimitiveValue::operator++(int a0)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValueppEi(
    QJSPrimitiveValue *self,
    int a0) {
  return new QJSPrimitiveValue(self->operator++(a0));
}

//  QJSPrimitiveValue &QJSPrimitiveValue::operator--()
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValuemmEv(
    QJSPrimitiveValue *self) {
  return &(self->operator--());
}

//  QJSPrimitiveValue QJSPrimitiveValue::operator--(int a0)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValuemmEi(
    QJSPrimitiveValue *self,
    int a0) {
  return new QJSPrimitiveValue(self->operator--(a0));
}

//  QJSPrimitiveValue QJSPrimitiveValue::operator+()
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValuepsEv(
    QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(self->operator+());
}

//  QJSPrimitiveValue QJSPrimitiveValue::operator-()
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValuengEv(
    QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(self->operator-());
}

//  bool QJSPrimitiveValue::strictlyEquals(const QJSPrimitiveValue &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSPrimitiveValue14strictlyEqualsERKS_(
    const QJSPrimitiveValue *self,
    const QJSPrimitiveValue *other) {
  return self->strictlyEquals(*other);
}

//  bool QJSPrimitiveValue::equals(const QJSPrimitiveValue &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSPrimitiveValue6equalsERKS_(
    const QJSPrimitiveValue *self,
    const QJSPrimitiveValue *other) {
  return self->equals(*other);
}

//  bool operator==(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QJSPrimitiveValue &lhs, const QJSPrimitiveValue
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK17QJSPrimitiveValueS1_(
    const QJSPrimitiveValue *lhs,
    const QJSPrimitiveValue *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool QJSPrimitiveValue::asBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSPrimitiveValue9asBooleanEv(
    const QJSPrimitiveValue *self) {
  return self->asBoolean();
}

//  int QJSPrimitiveValue::asInteger() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QJSPrimitiveValue9asIntegerEv(
    const QJSPrimitiveValue *self) {
  return self->asInteger();
}

//  double QJSPrimitiveValue::asDouble() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK17QJSPrimitiveValue8asDoubleEv(
    const QJSPrimitiveValue *self) {
  return self->asDouble();
}

//  QString QJSPrimitiveValue::asString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QJSPrimitiveValue8asStringEv(
    const QJSPrimitiveValue *self) {
  return new QString(self->asString());
}

//  bool QJSPrimitiveValue::parsedEquals(const QJSPrimitiveValue &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSPrimitiveValue12parsedEqualsERKS_(
    const QJSPrimitiveValue *self,
    const QJSPrimitiveValue *other) {
  return self->parsedEquals(*other);
}

//  QJSPrimitiveValue QJSPrimitiveValue::numberFromString(const QString
//      &string)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN17QJSPrimitiveValue16numberFromStringERK7QString(
    const QString *string) {
  return new QJSPrimitiveValue(QJSPrimitiveValue::numberFromString(*string));
}

//  QString QJSPrimitiveValue::toString(double d)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QJSPrimitiveValue8toStringEd(double d) {
  return new QString(QJSPrimitiveValue::toString(d));
}

//  bool QJSPrimitiveValue::isNanOrUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QJSPrimitiveValue16isNanOrUndefinedEv(
    const QJSPrimitiveValue *self) {
  return self->isNanOrUndefined();
}

//  QJSPrimitiveValue::~QJSPrimitiveValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QJSPrimitiveValueD1Ev(QJSPrimitiveValue *self) {
  delete self;
}

//  QJSPrimitiveValue QJSPrimitiveValue::to<QJSPrimitiveValue::Undefined>()
//      const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZNK17QJSPrimitiveValue2toILNS_4TypeE0EEES_v(
    const QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(
      self->to<QJSPrimitiveValue::Undefined>());
}

//  QJSPrimitiveValue QJSPrimitiveValue::to<QJSPrimitiveValue::Boolean>()
//      const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZNK17QJSPrimitiveValue2toILNS_4TypeE2EEES_v(
    const QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(
      self->to<QJSPrimitiveValue::Boolean>());
}

//  QJSPrimitiveValue QJSPrimitiveValue::to<QJSPrimitiveValue::Integer>()
//      const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZNK17QJSPrimitiveValue2toILNS_4TypeE3EEES_v(
    const QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(
      self->to<QJSPrimitiveValue::Integer>());
}

//  QJSPrimitiveValue QJSPrimitiveValue::to<QJSPrimitiveValue::Double>()
//      const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZNK17QJSPrimitiveValue2toILNS_4TypeE4EEES_v(
    const QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(
      self->to<QJSPrimitiveValue::Double>());
}

//  QJSPrimitiveValue QJSPrimitiveValue::to<QJSPrimitiveValue::String>()
//      const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue * ritual_ZNK17QJSPrimitiveValue2toILNS_4TypeE5EEES_v(
    const QJSPrimitiveValue *self) {
  return new QJSPrimitiveValue(
      self->to<QJSPrimitiveValue::String>());
}
