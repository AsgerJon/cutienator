//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qjsonvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qjsonvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>

//  QJsonValueConstRef::QJsonValueConstRef(const QJsonValueConstRef &a0)
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZN18QJsonValueConstRefC1ERKS_(
    const QJsonValueConstRef *a0) {
  return new QJsonValueConstRef(*a0);
}

//  QJsonValue QJsonValueConstRef::operator QJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK18QJsonValueConstRefcv10QJsonValueEv(
    const QJsonValueConstRef *self) {
  return new QJsonValue(self->operator QJsonValue());
}

//  QVariant QJsonValueConstRef::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QJsonValueConstRef9toVariantEv(
    const QJsonValueConstRef *self) {
  return new QVariant(self->toVariant());
}

//  QJsonValue::Type QJsonValueConstRef::type() const
extern "C" Q_DECL_EXPORT
QJsonValue::Type ritual_ZNK18QJsonValueConstRef4typeEv(
    const QJsonValueConstRef *self) {
  return self->type();
}

//  bool QJsonValueConstRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef6isNullEv(
    const QJsonValueConstRef *self) {
  return self->isNull();
}

//  bool QJsonValueConstRef::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef6isBoolEv(
    const QJsonValueConstRef *self) {
  return self->isBool();
}

//  bool QJsonValueConstRef::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef8isDoubleEv(
    const QJsonValueConstRef *self) {
  return self->isDouble();
}

//  bool QJsonValueConstRef::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef8isStringEv(
    const QJsonValueConstRef *self) {
  return self->isString();
}

//  bool QJsonValueConstRef::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef7isArrayEv(
    const QJsonValueConstRef *self) {
  return self->isArray();
}

//  bool QJsonValueConstRef::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef8isObjectEv(
    const QJsonValueConstRef *self) {
  return self->isObject();
}

//  bool QJsonValueConstRef::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef11isUndefinedEv(
    const QJsonValueConstRef *self) {
  return self->isUndefined();
}

//  bool QJsonValueConstRef::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QJsonValueConstRef6toBoolEb(
    const QJsonValueConstRef *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}

//  int QJsonValueConstRef::toInt(int defaultValue) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QJsonValueConstRef5toIntEi(
    const QJsonValueConstRef *self,
    int defaultValue) {
  return self->toInt(defaultValue);
}

//  qint64 QJsonValueConstRef::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QJsonValueConstRef9toIntegerEx(
    const QJsonValueConstRef *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}

//  double QJsonValueConstRef::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK18QJsonValueConstRef8toDoubleEd(
    const QJsonValueConstRef *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}

//  QString QJsonValueConstRef::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QJsonValueConstRef8toStringERK7QString(
    const QJsonValueConstRef *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}

//  QAnyStringView QJsonValueConstRef::toStringView(QAnyStringView
//      defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QJsonValueConstRef12toStringViewE14QAnyStringView(
    const QJsonValueConstRef *self,
    const QString *defaultValue) {
  return new QString(
      self->toStringView(
          QAnyStringView(*defaultValue)).toString());
}

//  QJsonArray QJsonValueConstRef::toArray() const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK18QJsonValueConstRef7toArrayEv(
    const QJsonValueConstRef *self) {
  return new QJsonArray(self->toArray());
}

//  QJsonObject QJsonValueConstRef::toObject() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK18QJsonValueConstRef8toObjectEv(
    const QJsonValueConstRef *self) {
  return new QJsonObject(self->toObject());
}

//  const QJsonValue QJsonValueConstRef::operator[](QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK18QJsonValueConstRefixE11QStringView(
    const QJsonValueConstRef *self,
    const QString *key) {
  return new QJsonValue(self->operator[](QStringView(*key)));
}

//  const QJsonValue QJsonValueConstRef::operator[](QLatin1StringView key)
//      const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK18QJsonValueConstRefixE13QLatin1String(
    const QJsonValueConstRef *self,
    const QLatin1String *key) {
  return new QJsonValue(self->operator[](*key));
}

//  const QJsonValue QJsonValueConstRef::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK18QJsonValueConstRefixEx(
    const QJsonValueConstRef *self,
    qsizetype i) {
  return new QJsonValue(self->operator[](i));
}

//  QJsonValueConstRef::~QJsonValueConstRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QJsonValueConstRefD1Ev(QJsonValueConstRef *self) {
  delete self;
}
