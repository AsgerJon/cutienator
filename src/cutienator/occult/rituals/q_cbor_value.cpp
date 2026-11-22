//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborvalue.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qcborarray.h>
#include <QtCore/qcbormap.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qurl.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/quuid.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qjsonvalue.h>

//  QCborValue::QCborValue()
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1Ev() {
  return new QCborValue();
}

//  QCborValue::QCborValue(Type t_)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ENS_4TypeE(QCborValue::Type t_) {
  return new QCborValue(t_);
}

//  QCborValue::QCborValue(bool b_)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1Eb(bool b_) {
  return new QCborValue(b_);
}

//  QCborValue::QCborValue(int i)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1Ei(int i) {
  return new QCborValue(i);
}

//  QCborValue::QCborValue(unsigned int u)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1Ej(unsigned int u) {
  return new QCborValue(u);
}

//  QCborValue::QCborValue(qint64 i)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1Ex(qint64 i) {
  return new QCborValue(i);
}

//  QCborValue::QCborValue(double v)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1Ed(double v) {
  return new QCborValue(v);
}

//  QCborValue::QCborValue(QCborSimpleType st)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1E15QCborSimpleType(QCborSimpleType st) {
  return new QCborValue(st);
}

//  QCborValue::QCborValue(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK10QByteArray(const QByteArray *ba) {
  return new QCborValue(*ba);
}

//  QCborValue::QCborValue(const QString &s)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK7QString(const QString *s) {
  return new QCborValue(*s);
}

//  QCborValue::QCborValue(QStringView s)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1E11QStringView(const QString *s) {
  return new QCborValue(QStringView(*s));
}

//  QCborValue::QCborValue(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1E13QLatin1String(const QLatin1String *s) {
  return new QCborValue(*s);
}

//  QCborValue::QCborValue(const char *s)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1EPKc(const char *s) {
  return new QCborValue(s);
}

//  QCborValue::QCborValue(const QCborArray &a)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK10QCborArray(const QCborArray *a) {
  return new QCborValue(*a);
}

//  QCborValue::QCborValue(const QCborMap &m)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK8QCborMap(const QCborMap *m) {
  return new QCborValue(*m);
}

//  QCborValue::QCborValue(QCborTag tag, const QCborValue &taggedValue)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1E8QCborTagRKS_(
    QCborTag tag,
    const QCborValue *taggedValue) {
  return new QCborValue(tag, *taggedValue);
}

//  QCborValue::QCborValue(QCborKnownTags t_, const QCborValue &tv)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1E14QCborKnownTagsRKS_(
    QCborKnownTags t_,
    const QCborValue *tv) {
  return new QCborValue(t_, *tv);
}

//  QCborValue::QCborValue(const QDateTime &dt)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK9QDateTime(const QDateTime *dt) {
  return new QCborValue(*dt);
}

//  QCborValue::QCborValue(const QUrl &url)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK4QUrl(const QUrl *url) {
  return new QCborValue(*url);
}

//  QCborValue::QCborValue(const QRegularExpression &rx)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK18QRegularExpression(
    const QRegularExpression *rx) {
  return new QCborValue(*rx);
}

//  QCborValue::QCborValue(const QUuid &uuid)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERK5QUuid(const QUuid *uuid) {
  return new QCborValue(*uuid);
}

//  QCborValue::~QCborValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborValueD1Ev(QCborValue *self) {
  delete self;
}

//  QCborValue::QCborValue(const QCborValue &other)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValueC1ERKS_(const QCborValue *other) {
  return new QCborValue(*other);
}

//  Type QCborValue::type() const
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZNK10QCborValue4typeEv(const QCborValue *self) {
  return self->type();
}

//  bool QCborValue::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue9isIntegerEv(const QCborValue *self) {
  return self->isInteger();
}

//  bool QCborValue::isByteArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue11isByteArrayEv(const QCborValue *self) {
  return self->isByteArray();
}

//  bool QCborValue::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue8isStringEv(const QCborValue *self) {
  return self->isString();
}

//  bool QCborValue::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue7isArrayEv(const QCborValue *self) {
  return self->isArray();
}

//  bool QCborValue::isMap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue5isMapEv(const QCborValue *self) {
  return self->isMap();
}

//  bool QCborValue::isTag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue5isTagEv(const QCborValue *self) {
  return self->isTag();
}

//  bool QCborValue::isFalse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue7isFalseEv(const QCborValue *self) {
  return self->isFalse();
}

//  bool QCborValue::isTrue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue6isTrueEv(const QCborValue *self) {
  return self->isTrue();
}

//  bool QCborValue::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue6isBoolEv(const QCborValue *self) {
  return self->isBool();
}

//  bool QCborValue::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue6isNullEv(const QCborValue *self) {
  return self->isNull();
}

//  bool QCborValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue11isUndefinedEv(const QCborValue *self) {
  return self->isUndefined();
}

//  bool QCborValue::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue8isDoubleEv(const QCborValue *self) {
  return self->isDouble();
}

//  bool QCborValue::isDateTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue10isDateTimeEv(const QCborValue *self) {
  return self->isDateTime();
}

//  bool QCborValue::isUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue5isUrlEv(const QCborValue *self) {
  return self->isUrl();
}

//  bool QCborValue::isRegularExpression() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue19isRegularExpressionEv(const QCborValue *self) {
  return self->isRegularExpression();
}

//  bool QCborValue::isUuid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue6isUuidEv(const QCborValue *self) {
  return self->isUuid();
}

//  bool QCborValue::isInvalid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue9isInvalidEv(const QCborValue *self) {
  return self->isInvalid();
}

//  bool QCborValue::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue11isContainerEv(const QCborValue *self) {
  return self->isContainer();
}

//  bool QCborValue::isSimpleType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue12isSimpleTypeEv(const QCborValue *self) {
  return self->isSimpleType();
}

//  bool QCborValue::isSimpleType(QCborSimpleType st) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue12isSimpleTypeE15QCborSimpleType(
    const QCborValue *self,
    QCborSimpleType st) {
  return self->isSimpleType(st);
}

//  QCborSimpleType QCborValue::toSimpleType(QCborSimpleType defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QCborSimpleType ritual_ZNK10QCborValue12toSimpleTypeE15QCborSimpleType(
    const QCborValue *self,
    QCborSimpleType defaultValue) {
  return self->toSimpleType(defaultValue);
}

//  qint64 QCborValue::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QCborValue9toIntegerEx(
    const QCborValue *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}

//  bool QCborValue::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCborValue6toBoolEb(
    const QCborValue *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}

//  double QCborValue::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QCborValue8toDoubleEd(
    const QCborValue *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}

//  QCborTag QCborValue::tag(QCborTag defaultValue) const
extern "C" Q_DECL_EXPORT
QCborTag ritual_ZNK10QCborValue3tagE8QCborTag(
    const QCborValue *self,
    QCborTag defaultValue) {
  return self->tag(defaultValue);
}

//  QCborValue QCborValue::taggedValue(const QCborValue &defaultValue) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborValue11taggedValueERKS_(
    const QCborValue *self,
    const QCborValue *defaultValue) {
  return new QCborValue(self->taggedValue(*defaultValue));
}

//  QByteArray QCborValue::toByteArray(const QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QCborValue11toByteArrayERK10QByteArray(
    const QCborValue *self,
    const QByteArray *defaultValue) {
  return new QByteArray(self->toByteArray(*defaultValue));
}

//  QString QCborValue::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCborValue8toStringERK7QString(
    const QCborValue *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}

//  QAnyStringView QCborValue::toStringView(QAnyStringView defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCborValue12toStringViewE14QAnyStringView(
    const QCborValue *self,
    const QString *defaultValue) {
  return new QString(
      self->toStringView(
          QAnyStringView(*defaultValue)).toString());
}

//  QDateTime QCborValue::toDateTime(const QDateTime &defaultValue) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK10QCborValue10toDateTimeERK9QDateTime(
    const QCborValue *self,
    const QDateTime *defaultValue) {
  return new QDateTime(self->toDateTime(*defaultValue));
}

//  QUrl QCborValue::toUrl(const QUrl &defaultValue) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QCborValue5toUrlERK4QUrl(
    const QCborValue *self,
    const QUrl *defaultValue) {
  return new QUrl(self->toUrl(*defaultValue));
}

//  QRegularExpression QCborValue::toRegularExpression(const
//      QRegularExpression &defaultValue) const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK10QCborValue19toRegularExpressionERK18QRegularExpression(
    const QCborValue *self,
    const QRegularExpression *defaultValue) {
  return new QRegularExpression(self->toRegularExpression(*defaultValue));
}

//  QUuid QCborValue::toUuid(const QUuid &defaultValue) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK10QCborValue6toUuidERK5QUuid(
    const QCborValue *self,
    const QUuid *defaultValue) {
  return new QUuid(self->toUuid(*defaultValue));
}

//  QCborArray QCborValue::toArray() const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK10QCborValue7toArrayEv(const QCborValue *self) {
  return new QCborArray(self->toArray());
}

//  QCborArray QCborValue::toArray(const QCborArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK10QCborValue7toArrayERK10QCborArray(
    const QCborValue *self,
    const QCborArray *defaultValue) {
  return new QCborArray(self->toArray(*defaultValue));
}

//  QCborMap QCborValue::toMap() const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK10QCborValue5toMapEv(const QCborValue *self) {
  return new QCborMap(self->toMap());
}

//  QCborMap QCborValue::toMap(const QCborMap &defaultValue) const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK10QCborValue5toMapERK8QCborMap(
    const QCborValue *self,
    const QCborMap *defaultValue) {
  return new QCborMap(self->toMap(*defaultValue));
}

//  const QCborValue QCborValue::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborValueixERK7QString(
    const QCborValue *self,
    const QString *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborValue::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborValueixE13QLatin1String(
    const QCborValue *self,
    const QLatin1String *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborValue::operator[](qint64 key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK10QCborValueixEx(const QCborValue *self, qint64 key) {
  return new QCborValue(self->operator[](key));
}

//  QCborValueRef QCborValue::operator[](qint64 key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborValueixEx(QCborValue *self, qint64 key) {
  return new QCborValueRef(self->operator[](key));
}

//  QCborValueRef QCborValue::operator[](QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborValueixE13QLatin1String(
    QCborValue *self,
    const QLatin1String *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  QCborValueRef QCborValue::operator[](const QString &key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN10QCborValueixERK7QString(
    QCborValue *self,
    const QString *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  int QCborValue::compare(const QCborValue &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCborValue7compareERKS_(
    const QCborValue *self,
    const QCborValue *other) {
  return self->compare(*other);
}

//  QCborValue QCborValue::fromVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValue11fromVariantERK8QVariant(
    const QVariant *variant) {
  return new QCborValue(QCborValue::fromVariant(*variant));
}

//  QVariant QCborValue::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QCborValue9toVariantEv(const QCborValue *self) {
  return new QVariant(self->toVariant());
}

//  QCborValue QCborValue::fromJsonValue(const QJsonValue &v)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValue13fromJsonValueERK10QJsonValue(
    const QJsonValue *v) {
  return new QCborValue(QCborValue::fromJsonValue(*v));
}

//  QJsonValue QCborValue::toJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QCborValue11toJsonValueEv(const QCborValue *self) {
  return new QJsonValue(self->toJsonValue());
}

//  QCborValue QCborValue::fromCbor(const QByteArray &ba, QCborParserError
//      *error)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValue8fromCborERK10QByteArrayP16QCborParserError(
    const QByteArray *ba,
    QCborParserError *error) {
  return new QCborValue(QCborValue::fromCbor(*ba, error));
}

//  QCborValue QCborValue::fromCbor(const char *data, qsizetype len,
//      QCborParserError *error)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN10QCborValue8fromCborEPKcxP16QCborParserError(
    const char *data,
    qsizetype len,
    QCborParserError *error) {
  return new QCborValue(QCborValue::fromCbor(data, len, error));
}

//  QByteArray QCborValue::toCbor(EncodingOptions opt) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QCborValue6toCborE6QFlagsINS_14EncodingOptionEE(
    const QCborValue *self,
    int opt) {
  return new QByteArray(
      self->toCbor(
          QFlags<QCborValue::EncodingOption>::fromInt(opt)));
}

//  QString QCborValue::toDiagnosticNotation(DiagnosticNotationOptions opts)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCborValue20toDiagnosticNotationE6QFlagsINS_24DiagnosticNotationOptionEE(
    const QCborValue *self,
    int opts) {
  return new QString(
      self->toDiagnosticNotation(
          QFlags<QCborValue::DiagnosticNotationOption>::fromInt(opts)));
}

//  bool operator==(const QCborValue &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QCborValueS1_(
    const QCborValue *lhs,
    const QCborValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCborValue &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QCborValueS1_(
    const QCborValue *lhs,
    const QCborValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QCborValue &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QCborValueS1_(
    const QCborValue *lhs,
    const QCborValue *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QCborValue &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QCborValueS1_(
    const QCborValue *lhs,
    const QCborValue *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QCborValue &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QCborValueS1_(
    const QCborValue *lhs,
    const QCborValue *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QCborValue &lhs, const QCborValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QCborValueS1_(
    const QCborValue *lhs,
    const QCborValue *rhs) {
  return operator>=(*lhs, *rhs);
}
