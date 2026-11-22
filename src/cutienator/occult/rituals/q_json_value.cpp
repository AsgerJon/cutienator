//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonvalue.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qdebug.h>

//  QJsonValue::QJsonValue(Type a0)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1ENS_4TypeE(QJsonValue::Type a0) {
  return new QJsonValue(a0);
}

//  QJsonValue::QJsonValue(bool b)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1Eb(bool b) {
  return new QJsonValue(b);
}

//  QJsonValue::QJsonValue(double n)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1Ed(double n) {
  return new QJsonValue(n);
}

//  QJsonValue::QJsonValue(int n)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1Ei(int n) {
  return new QJsonValue(n);
}

//  QJsonValue::QJsonValue(qint64 v)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1Ex(qint64 v) {
  return new QJsonValue(v);
}

//  QJsonValue::QJsonValue(const QString &s)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1ERK7QString(const QString *s) {
  return new QJsonValue(*s);
}

//  QJsonValue::QJsonValue(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1E13QLatin1String(const QLatin1String *s) {
  return new QJsonValue(*s);
}

//  QJsonValue::QJsonValue(const char *s)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1EPKc(const char *s) {
  return new QJsonValue(s);
}

//  QJsonValue::QJsonValue(const QJsonArray &a)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1ERK10QJsonArray(const QJsonArray *a) {
  return new QJsonValue(*a);
}

//  QJsonValue::QJsonValue(const QJsonObject &o)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1ERK11QJsonObject(const QJsonObject *o) {
  return new QJsonValue(*o);
}

//  QJsonValue::~QJsonValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QJsonValueD1Ev(QJsonValue *self) {
  delete self;
}

//  QJsonValue::QJsonValue(const QJsonValue &other)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValueC1ERKS_(const QJsonValue *other) {
  return new QJsonValue(*other);
}

//  QJsonValue QJsonValue::fromVariant(const QVariant &variant)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValue11fromVariantERK8QVariant(
    const QVariant *variant) {
  return new QJsonValue(QJsonValue::fromVariant(*variant));
}

//  QVariant QJsonValue::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QJsonValue9toVariantEv(const QJsonValue *self) {
  return new QVariant(self->toVariant());
}

//  QJsonValue QJsonValue::fromJson(QByteArrayView json, QJsonParseError
//      *error)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN10QJsonValue8fromJsonE14QByteArrayViewP15QJsonParseError(
    const QByteArrayView *json,
    QJsonParseError *error) {
  return new QJsonValue(QJsonValue::fromJson(*json, error));
}

//  QByteArray QJsonValue::toJson(JsonFormat format) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QJsonValue6toJsonEN13QJsonDocument10JsonFormatE(
    const QJsonValue *self,
    QJsonValue::JsonFormat format) {
  return new QByteArray(self->toJson(format));
}

//  Type QJsonValue::type() const
extern "C" Q_DECL_EXPORT
QJsonValue::Type ritual_ZNK10QJsonValue4typeEv(const QJsonValue *self) {
  return self->type();
}

//  bool QJsonValue::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue6isNullEv(const QJsonValue *self) {
  return self->isNull();
}

//  bool QJsonValue::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue6isBoolEv(const QJsonValue *self) {
  return self->isBool();
}

//  bool QJsonValue::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue8isDoubleEv(const QJsonValue *self) {
  return self->isDouble();
}

//  bool QJsonValue::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue8isStringEv(const QJsonValue *self) {
  return self->isString();
}

//  bool QJsonValue::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue7isArrayEv(const QJsonValue *self) {
  return self->isArray();
}

//  bool QJsonValue::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue8isObjectEv(const QJsonValue *self) {
  return self->isObject();
}

//  bool QJsonValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue11isUndefinedEv(const QJsonValue *self) {
  return self->isUndefined();
}

//  bool QJsonValue::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QJsonValue6toBoolEb(
    const QJsonValue *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}

//  int QJsonValue::toInt(int defaultValue) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QJsonValue5toIntEi(
    const QJsonValue *self,
    int defaultValue) {
  return self->toInt(defaultValue);
}

//  qint64 QJsonValue::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QJsonValue9toIntegerEx(
    const QJsonValue *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}

//  double QJsonValue::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QJsonValue8toDoubleEd(
    const QJsonValue *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}

//  QString QJsonValue::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QJsonValue8toStringEv(const QJsonValue *self) {
  return new QString(self->toString());
}

//  QString QJsonValue::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QJsonValue8toStringERK7QString(
    const QJsonValue *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}

//  QAnyStringView QJsonValue::toStringView(QAnyStringView defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QJsonValue12toStringViewE14QAnyStringView(
    const QJsonValue *self,
    const QString *defaultValue) {
  return new QString(
      self->toStringView(
          QAnyStringView(*defaultValue)).toString());
}

//  QJsonArray QJsonValue::toArray() const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK10QJsonValue7toArrayEv(const QJsonValue *self) {
  return new QJsonArray(self->toArray());
}

//  QJsonArray QJsonValue::toArray(const QJsonArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK10QJsonValue7toArrayERK10QJsonArray(
    const QJsonValue *self,
    const QJsonArray *defaultValue) {
  return new QJsonArray(self->toArray(*defaultValue));
}

//  QJsonObject QJsonValue::toObject() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK10QJsonValue8toObjectEv(const QJsonValue *self) {
  return new QJsonObject(self->toObject());
}

//  QJsonObject QJsonValue::toObject(const QJsonObject &defaultValue) const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK10QJsonValue8toObjectERK11QJsonObject(
    const QJsonValue *self,
    const QJsonObject *defaultValue) {
  return new QJsonObject(self->toObject(*defaultValue));
}

//  const QJsonValue QJsonValue::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonValueixERK7QString(
    const QJsonValue *self,
    const QString *key) {
  return new QJsonValue(self->operator[](*key));
}

//  const QJsonValue QJsonValue::operator[](QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonValueixE11QStringView(
    const QJsonValue *self,
    const QString *key) {
  return new QJsonValue(self->operator[](QStringView(*key)));
}

//  const QJsonValue QJsonValue::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonValueixE13QLatin1String(
    const QJsonValue *self,
    const QLatin1String *key) {
  return new QJsonValue(self->operator[](*key));
}

//  const QJsonValue QJsonValue::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK10QJsonValueixEx(const QJsonValue *self, qsizetype i) {
  return new QJsonValue(self->operator[](i));
}

//  bool operator==(const QJsonValue &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QJsonValueS1_(
    const QJsonValue *lhs,
    const QJsonValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValue &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QJsonValueS1_(
    const QJsonValue *lhs,
    const QJsonValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QDebug operator<<(QDebug a0, const QJsonValue &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK10QJsonValue(
    const QDebug *a0,
    const QJsonValue *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
