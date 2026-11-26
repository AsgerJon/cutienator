//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborvalue.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qurl.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/quuid.h>
#include <QtCore/qcborarray.h>
#include <QtCore/qcbormap.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qcompare.h>

//  QCborValueConstRef::QCborValueConstRef(const QCborValueConstRef &a0)
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZN18QCborValueConstRefC1ERKS_(
    const QCborValueConstRef *a0) {
  return new QCborValueConstRef(*a0);
}

//  QCborValue QCborValueConstRef::operator QCborValue() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK18QCborValueConstRefcv10QCborValueEv(
    const QCborValueConstRef *self) {
  return new QCborValue(self->operator QCborValue());
}

//  QCborValue::Type QCborValueConstRef::type() const
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZNK18QCborValueConstRef4typeEv(
    const QCborValueConstRef *self) {
  return self->type();
}

//  bool QCborValueConstRef::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef9isIntegerEv(
    const QCborValueConstRef *self) {
  return self->isInteger();
}

//  bool QCborValueConstRef::isByteArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef11isByteArrayEv(
    const QCborValueConstRef *self) {
  return self->isByteArray();
}

//  bool QCborValueConstRef::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef8isStringEv(
    const QCborValueConstRef *self) {
  return self->isString();
}

//  bool QCborValueConstRef::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef7isArrayEv(
    const QCborValueConstRef *self) {
  return self->isArray();
}

//  bool QCborValueConstRef::isMap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef5isMapEv(const QCborValueConstRef *self) {
  return self->isMap();
}

//  bool QCborValueConstRef::isTag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef5isTagEv(const QCborValueConstRef *self) {
  return self->isTag();
}

//  bool QCborValueConstRef::isFalse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef7isFalseEv(
    const QCborValueConstRef *self) {
  return self->isFalse();
}

//  bool QCborValueConstRef::isTrue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef6isTrueEv(
    const QCborValueConstRef *self) {
  return self->isTrue();
}

//  bool QCborValueConstRef::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef6isBoolEv(
    const QCborValueConstRef *self) {
  return self->isBool();
}

//  bool QCborValueConstRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef6isNullEv(
    const QCborValueConstRef *self) {
  return self->isNull();
}

//  bool QCborValueConstRef::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef11isUndefinedEv(
    const QCborValueConstRef *self) {
  return self->isUndefined();
}

//  bool QCborValueConstRef::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef8isDoubleEv(
    const QCborValueConstRef *self) {
  return self->isDouble();
}

//  bool QCborValueConstRef::isDateTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef10isDateTimeEv(
    const QCborValueConstRef *self) {
  return self->isDateTime();
}

//  bool QCborValueConstRef::isUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef5isUrlEv(const QCborValueConstRef *self) {
  return self->isUrl();
}

//  bool QCborValueConstRef::isRegularExpression() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef19isRegularExpressionEv(
    const QCborValueConstRef *self) {
  return self->isRegularExpression();
}

//  bool QCborValueConstRef::isUuid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef6isUuidEv(
    const QCborValueConstRef *self) {
  return self->isUuid();
}

//  bool QCborValueConstRef::isInvalid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef9isInvalidEv(
    const QCborValueConstRef *self) {
  return self->isInvalid();
}

//  bool QCborValueConstRef::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef11isContainerEv(
    const QCborValueConstRef *self) {
  return self->isContainer();
}

//  bool QCborValueConstRef::isSimpleType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef12isSimpleTypeEv(
    const QCborValueConstRef *self) {
  return self->isSimpleType();
}

//  bool QCborValueConstRef::isSimpleType(QCborSimpleType st) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef12isSimpleTypeE15QCborSimpleType(
    const QCborValueConstRef *self,
    QCborSimpleType st) {
  return self->isSimpleType(st);
}

//  QCborSimpleType QCborValueConstRef::toSimpleType(QCborSimpleType
//      defaultValue) const
extern "C" Q_DECL_EXPORT
QCborSimpleType ritual_ZNK18QCborValueConstRef12toSimpleTypeE15QCborSimpleType(
    const QCborValueConstRef *self,
    QCborSimpleType defaultValue) {
  return self->toSimpleType(defaultValue);
}

//  QCborTag QCborValueConstRef::tag(QCborTag defaultValue) const
extern "C" Q_DECL_EXPORT
QCborTag ritual_ZNK18QCborValueConstRef3tagE8QCborTag(
    const QCborValueConstRef *self,
    QCborTag defaultValue) {
  return self->tag(defaultValue);
}

//  QCborValue QCborValueConstRef::taggedValue(const QCborValue
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK18QCborValueConstRef11taggedValueERK10QCborValue(
    const QCborValueConstRef *self,
    const QCborValue *defaultValue) {
  return new QCborValue(self->taggedValue(*defaultValue));
}

//  qint64 QCborValueConstRef::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QCborValueConstRef9toIntegerEx(
    const QCborValueConstRef *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}

//  bool QCborValueConstRef::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCborValueConstRef6toBoolEb(
    const QCborValueConstRef *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}

//  double QCborValueConstRef::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK18QCborValueConstRef8toDoubleEd(
    const QCborValueConstRef *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}

//  QByteArray QCborValueConstRef::toByteArray(const QByteArray
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QCborValueConstRef11toByteArrayERK10QByteArray(
    const QCborValueConstRef *self,
    const QByteArray *defaultValue) {
  return new QByteArray(self->toByteArray(*defaultValue));
}

//  QString QCborValueConstRef::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCborValueConstRef8toStringERK7QString(
    const QCborValueConstRef *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}

//  QAnyStringView QCborValueConstRef::toStringView(QAnyStringView
//      defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCborValueConstRef12toStringViewE14QAnyStringView(
    const QCborValueConstRef *self,
    const QString *defaultValue) {
  return new QString(
      self->toStringView(
          QAnyStringView(*defaultValue)).toString());
}

#if QT_CONFIG(datestring)
//  QDateTime QCborValueConstRef::toDateTime(const QDateTime &defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK18QCborValueConstRef10toDateTimeERK9QDateTime(
    const QCborValueConstRef *self,
    const QDateTime *defaultValue) {
  return new QDateTime(self->toDateTime(*defaultValue));
}
#endif  // QT_CONFIG(datestring)

#if !defined(QT_BOOTSTRAPPED)
//  QUrl QCborValueConstRef::toUrl(const QUrl &defaultValue) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QCborValueConstRef5toUrlERK4QUrl(
    const QCborValueConstRef *self,
    const QUrl *defaultValue) {
  return new QUrl(self->toUrl(*defaultValue));
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
#if QT_CONFIG(regularexpression)
//  QRegularExpression QCborValueConstRef::toRegularExpression(const
//      QRegularExpression &defaultValue) const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK18QCborValueConstRef19toRegularExpressionERK18QRegularExpression(
    const QCborValueConstRef *self,
    const QRegularExpression *defaultValue) {
  return new QRegularExpression(self->toRegularExpression(*defaultValue));
}
#endif  // QT_CONFIG(regularexpression)
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  QUuid QCborValueConstRef::toUuid(const QUuid &defaultValue) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK18QCborValueConstRef6toUuidERK5QUuid(
    const QCborValueConstRef *self,
    const QUuid *defaultValue) {
  return new QUuid(self->toUuid(*defaultValue));
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  QCborArray QCborValueConstRef::toArray() const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK18QCborValueConstRef7toArrayEv(
    const QCborValueConstRef *self) {
  return new QCborArray(self->toArray());
}

//  QCborArray QCborValueConstRef::toArray(const QCborArray &a) const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK18QCborValueConstRef7toArrayERK10QCborArray(
    const QCborValueConstRef *self,
    const QCborArray *a) {
  return new QCborArray(self->toArray(*a));
}

//  QCborMap QCborValueConstRef::toMap() const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK18QCborValueConstRef5toMapEv(
    const QCborValueConstRef *self) {
  return new QCborMap(self->toMap());
}

//  QCborMap QCborValueConstRef::toMap(const QCborMap &m) const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK18QCborValueConstRef5toMapERK8QCborMap(
    const QCborValueConstRef *self,
    const QCborMap *m) {
  return new QCborMap(self->toMap(*m));
}

//  const QCborValue QCborValueConstRef::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK18QCborValueConstRefixERK7QString(
    const QCborValueConstRef *self,
    const QString *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborValueConstRef::operator[](QLatin1StringView key)
//      const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK18QCborValueConstRefixE13QLatin1String(
    const QCborValueConstRef *self,
    const QLatin1String *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborValueConstRef::operator[](qint64 key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK18QCborValueConstRefixEx(
    const QCborValueConstRef *self,
    qint64 key) {
  return new QCborValue(self->operator[](key));
}

//  int QCborValueConstRef::compare(const QCborValue &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QCborValueConstRef7compareERK10QCborValue(
    const QCborValueConstRef *self,
    const QCborValue *other) {
  return self->compare(*other);
}

//  QVariant QCborValueConstRef::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QCborValueConstRef9toVariantEv(
    const QCborValueConstRef *self) {
  return new QVariant(self->toVariant());
}

//  QJsonValue QCborValueConstRef::toJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK18QCborValueConstRef11toJsonValueEv(
    const QCborValueConstRef *self) {
  return new QJsonValue(self->toJsonValue());
}

#if QT_CONFIG(cborstreamwriter)
//  QByteArray QCborValueConstRef::toCbor(QCborValue::EncodingOptions opt)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QCborValueConstRef6toCborE6QFlagsIN10QCborValue14EncodingOptionEE(
    const QCborValueConstRef *self,
    int opt) {
  return new QByteArray(
      self->toCbor(
          QFlags<QCborValue::EncodingOption>::fromInt(opt)));
}
#endif  // QT_CONFIG(cborstreamwriter)

#if QT_CONFIG(cborstreamwriter)
//  void QCborValueConstRef::toCbor(QCborStreamWriter &writer,
//      QCborValue::EncodingOptions opt) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QCborValueConstRef6toCborER17QCborStreamWriter6QFlagsIN10QCborValue14EncodingOptionEE(
    const QCborValueConstRef *self,
    QCborStreamWriter *writer,
    int opt) {
  self->toCbor(*writer, QFlags<QCborValue::EncodingOption>::fromInt(opt));
}
#endif  // QT_CONFIG(cborstreamwriter)

//  QString QCborValueConstRef::toDiagnosticNotation(QCborValue::DiagnosticNo
//      tationOptions opt) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QCborValueConstRef20toDiagnosticNotationE6QFlagsIN10QCborValue24DiagnosticNotationOptionEE(
    const QCborValueConstRef *self,
    int opt) {
  return new QString(
      self->toDiagnosticNotation(
          QFlags<QCborValue::DiagnosticNotationOption>::fromInt(opt)));
}

//  QCborValue QCborValueConstRef::concrete() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK18QCborValueConstRef8concreteEv(
    const QCborValueConstRef *self) {
  return new QCborValue(self->concrete());
}

//  bool QCborValueConstRef::comparesEqual_helper(QCborValueConstRef lhs,
//      QCborValueConstRef rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCborValueConstRef20comparesEqual_helperES_S_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return QCborValueConstRef::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering
//      QCborValueConstRef::compareThreeWay_helper(QCborValueConstRef lhs,
//      QCborValueConstRef rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN18QCborValueConstRef22compareThreeWay_helperES_S_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return new Qt::strong_ordering(
      QCborValueConstRef::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const QCborValueConstRef &lhs, const QCborValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QCborValueConstRefS1_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborValueConstRef &lhs, const QCborValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QCborValueConstRefS1_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborValueConstRef &lhs, const QCborValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK18QCborValueConstRefS1_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborValueConstRef &lhs, const QCborValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK18QCborValueConstRefS1_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborValueConstRef &lhs, const QCborValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK18QCborValueConstRefS1_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborValueConstRef &lhs, const QCborValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK18QCborValueConstRefS1_(
    const QCborValueConstRef *lhs,
    const QCborValueConstRef *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool QCborValueConstRef::comparesEqual_helper(QCborValueConstRef lhs,
//      const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCborValueConstRef20comparesEqual_helperES_RK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return QCborValueConstRef::comparesEqual_helper(*lhs, *rhs);
}

//  Qt::strong_ordering
//      QCborValueConstRef::compareThreeWay_helper(QCborValueConstRef lhs,
//      const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
Qt::strong_ordering *ritual_ZN18QCborValueConstRef22compareThreeWay_helperES_RK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return new Qt::strong_ordering(
      QCborValueConstRef::compareThreeWay_helper(
          *lhs,
          *rhs));
}

//  bool operator==(const QCborValueConstRef &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QCborValueConstRefRK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborValueConstRef &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QCborValueConstRefRK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborValueConstRef &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK18QCborValueConstRefRK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborValueConstRef &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK18QCborValueConstRefRK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborValueConstRef &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK18QCborValueConstRefRK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborValueConstRef &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK18QCborValueConstRefRK10QCborValue(
    const QCborValueConstRef *lhs,
    const QCborValue *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QCborValue &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QCborValueRK18QCborValueConstRef(
    const QCborValue *lhs,
    const QCborValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborValue &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QCborValueRK18QCborValueConstRef(
    const QCborValue *lhs,
    const QCborValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborValue &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QCborValueRK18QCborValueConstRef(
    const QCborValue *lhs,
    const QCborValueConstRef *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborValue &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QCborValueRK18QCborValueConstRef(
    const QCborValue *lhs,
    const QCborValueConstRef *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborValue &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QCborValueRK18QCborValueConstRef(
    const QCborValue *lhs,
    const QCborValueConstRef *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborValue &lhs, const QCborValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QCborValueRK18QCborValueConstRef(
    const QCborValue *lhs,
    const QCborValueConstRef *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QCborValue QCborValueConstRef::concrete(QCborValueConstRef that)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN18QCborValueConstRef8concreteES_(
    const QCborValueConstRef *that) {
  return new QCborValue(QCborValueConstRef::concrete(*that));
}

//  QCborValue::Type QCborValueConstRef::concreteType(QCborValueConstRef
//      that)
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZN18QCborValueConstRef12concreteTypeES_(
    const QCborValueConstRef *that) {
  return QCborValueConstRef::concreteType(*that);
}

//  bool QCborValueConstRef::concreteBoolean(QCborValueConstRef that, bool
//      defaultValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCborValueConstRef15concreteBooleanES_b(
    const QCborValueConstRef *that,
    bool defaultValue) {
  return QCborValueConstRef::concreteBoolean(*that, defaultValue);
}

//  double QCborValueConstRef::concreteDouble(QCborValueConstRef that, double
//      defaultValue)
extern "C" Q_DECL_EXPORT
double ritual_ZN18QCborValueConstRef14concreteDoubleES_d(
    const QCborValueConstRef *that,
    double defaultValue) {
  return QCborValueConstRef::concreteDouble(*that, defaultValue);
}

//  qint64 QCborValueConstRef::concreteIntegral(QCborValueConstRef that,
//      qint64 defaultValue)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN18QCborValueConstRef16concreteIntegralES_x(
    const QCborValueConstRef *that,
    qint64 defaultValue) {
  return QCborValueConstRef::concreteIntegral(*that, defaultValue);
}

//  QByteArray QCborValueConstRef::concreteByteArray(QCborValueConstRef that,
//      const QByteArray &defaultValue)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QCborValueConstRef17concreteByteArrayES_RK10QByteArray(
    const QCborValueConstRef *that,
    const QByteArray *defaultValue) {
  return new QByteArray(
      QCborValueConstRef::concreteByteArray(
          *that,
          *defaultValue));
}

//  QString QCborValueConstRef::concreteString(QCborValueConstRef that, const
//      QString &defaultValue)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCborValueConstRef14concreteStringES_RK7QString(
    const QCborValueConstRef *that,
    const QString *defaultValue) {
  return new QString(
      QCborValueConstRef::concreteString(
          *that,
          *defaultValue));
}

//  QAnyStringView QCborValueConstRef::concreteStringView(QCborValueConstRef
//      that, QAnyStringView defaultValue)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCborValueConstRef18concreteStringViewES_14QAnyStringView(
    const QCborValueConstRef *that,
    const QString *defaultValue) {
  return new QString(
      QCborValueConstRef::concreteStringView(
          *that,
          QAnyStringView(*defaultValue)).toString());
}

//  QCborValueConstRef::QCborValueConstRef()
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZN18QCborValueConstRefC1Ev() {
  return new QCborValueConstRef();
}

//  QCborValueConstRef::QCborValueConstRef(QCborContainerPrivate *dd,
//      qsizetype ii)
extern "C" Q_DECL_EXPORT
QCborValueConstRef *ritual_ZN18QCborValueConstRefC1EP21QCborContainerPrivatex(
    QCborContainerPrivate *dd,
    qsizetype ii) {
  return new QCborValueConstRef(dd, ii);
}

//  QCborValueConstRef::~QCborValueConstRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCborValueConstRefD1Ev(QCborValueConstRef *self) {
  delete self;
}
