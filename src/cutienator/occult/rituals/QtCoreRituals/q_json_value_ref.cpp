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

//  QJsonValueRef::QJsonValueRef(const QJsonValueRef &a0)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN13QJsonValueRefC1ERKS_(const QJsonValueRef *a0) {
  return new QJsonValueRef(*a0);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValueRef::QJsonValueRef(QJsonArray *array, qsizetype idx)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN13QJsonValueRefC1EP10QJsonArrayx(
    QJsonArray *array,
    qsizetype idx) {
  return new QJsonValueRef(array, idx);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValueRef::QJsonValueRef(QJsonObject *object, qsizetype idx)
extern "C" Q_DECL_EXPORT
QJsonValueRef *ritual_ZN13QJsonValueRefC1EP11QJsonObjectx(
    QJsonObject *object,
    qsizetype idx) {
  return new QJsonValueRef(object, idx);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValue QJsonValueRef::operator QJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonValueRefcv10QJsonValueEv(
    const QJsonValueRef *self) {
  return new QJsonValue(self->operator QJsonValue());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QVariant QJsonValueRef::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QJsonValueRef9toVariantEv(const QJsonValueRef *self) {
  return new QVariant(self->toVariant());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValue::Type QJsonValueRef::type() const
extern "C" Q_DECL_EXPORT
QJsonValue::Type ritual_ZNK13QJsonValueRef4typeEv(
    const QJsonValueRef *self) {
  return self->type();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef6isNullEv(const QJsonValueRef *self) {
  return self->isNull();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef6isBoolEv(const QJsonValueRef *self) {
  return self->isBool();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef8isDoubleEv(const QJsonValueRef *self) {
  return self->isDouble();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef8isStringEv(const QJsonValueRef *self) {
  return self->isString();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef7isArrayEv(const QJsonValueRef *self) {
  return self->isArray();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef8isObjectEv(const QJsonValueRef *self) {
  return self->isObject();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef11isUndefinedEv(const QJsonValueRef *self) {
  return self->isUndefined();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QJsonValueRef::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QJsonValueRef6toBoolEb(
    const QJsonValueRef *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  int QJsonValueRef::toInt(int defaultValue) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QJsonValueRef5toIntEi(
    const QJsonValueRef *self,
    int defaultValue) {
  return self->toInt(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  qint64 QJsonValueRef::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QJsonValueRef9toIntegerEx(
    const QJsonValueRef *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  double QJsonValueRef::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QJsonValueRef8toDoubleEd(
    const QJsonValueRef *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QString QJsonValueRef::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QJsonValueRef8toStringERK7QString(
    const QJsonValueRef *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QAnyStringView QJsonValueRef::toStringView(QAnyStringView defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QJsonValueRef12toStringViewE14QAnyStringView(
    const QJsonValueRef *self,
    const QString *defaultValue) {
  return new QString(
      self->toStringView(
          QAnyStringView(*defaultValue)).toString());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonArray QJsonValueRef::toArray() const
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZNK13QJsonValueRef7toArrayEv(const QJsonValueRef *self) {
  return new QJsonArray(self->toArray());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonObject QJsonValueRef::toObject() const
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZNK13QJsonValueRef8toObjectEv(
    const QJsonValueRef *self) {
  return new QJsonObject(self->toObject());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  const QJsonValue QJsonValueRef::operator[](QStringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonValueRefixE11QStringView(
    const QJsonValueRef *self,
    const QString *key) {
  return new QJsonValue(self->operator[](QStringView(*key)));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  const QJsonValue QJsonValueRef::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonValueRefixE13QLatin1String(
    const QJsonValueRef *self,
    const QLatin1String *key) {
  return new QJsonValue(self->operator[](*key));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  const QJsonValue QJsonValueRef::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonValueRefixEx(
    const QJsonValueRef *self,
    qsizetype i) {
  return new QJsonValue(self->operator[](i));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool operator==(const QJsonValueRef &lhs, const QJsonValueRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QJsonValueRefS1_(
    const QJsonValueRef *lhs,
    const QJsonValueRef *rhs) {
  return operator==(*lhs, *rhs);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool operator!=(const QJsonValueRef &lhs, const QJsonValueRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QJsonValueRefS1_(
    const QJsonValueRef *lhs,
    const QJsonValueRef *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool operator==(const QJsonValueRef &lhs, const QJsonValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QJsonValueRefRK18QJsonValueConstRef(
    const QJsonValueRef *lhs,
    const QJsonValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool operator!=(const QJsonValueRef &lhs, const QJsonValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QJsonValueRefRK18QJsonValueConstRef(
    const QJsonValueRef *lhs,
    const QJsonValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool operator==(const QJsonValueConstRef &lhs, const QJsonValueRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QJsonValueConstRefRK13QJsonValueRef(
    const QJsonValueConstRef *lhs,
    const QJsonValueRef *rhs) {
  return operator==(*lhs, *rhs);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool operator!=(const QJsonValueConstRef &lhs, const QJsonValueRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QJsonValueConstRefRK13QJsonValueRef(
    const QJsonValueConstRef *lhs,
    const QJsonValueRef *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValue QJsonValueRef::toValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QJsonValueRef7toValueEv(const QJsonValueRef *self) {
  return new QJsonValue(self->toValue());
}
#endif

//  void QJsonValueRef::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QJsonValueRef6detachEv(QJsonValueRef *self) {
  self->detach();
}

//  QJsonValueRef::~QJsonValueRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QJsonValueRefD1Ev(QJsonValueRef *self) {
  delete self;
}
