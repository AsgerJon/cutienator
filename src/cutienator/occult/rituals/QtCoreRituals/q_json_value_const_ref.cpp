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

//  bool operator==(const QJsonValueConstRef &lhs, const QJsonValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QJsonValueConstRefS1_(
    const QJsonValueConstRef *lhs,
    const QJsonValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValueConstRef &lhs, const QJsonValueConstRef
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QJsonValueConstRefS1_(
    const QJsonValueConstRef *lhs,
    const QJsonValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonValueConstRef &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QJsonValueConstRefRK10QJsonValue(
    const QJsonValueConstRef *lhs,
    const QJsonValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValueConstRef &lhs, const QJsonValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QJsonValueConstRefRK10QJsonValue(
    const QJsonValueConstRef *lhs,
    const QJsonValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QJsonValue &lhs, const QJsonValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QJsonValueRK18QJsonValueConstRef(
    const QJsonValue *lhs,
    const QJsonValueConstRef *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QJsonValue &lhs, const QJsonValueConstRef &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QJsonValueRK18QJsonValueConstRef(
    const QJsonValue *lhs,
    const QJsonValueConstRef *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QJsonValue::Type QJsonValueConstRef::concreteType(QJsonValueConstRef
//      self_)
extern "C" Q_DECL_EXPORT
QJsonValue::Type ritual_ZN18QJsonValueConstRef12concreteTypeES_(
    const QJsonValueConstRef *self_) {
  return QJsonValueConstRef::concreteType(*self_);
}

//  bool QJsonValueConstRef::concreteBool(QJsonValueConstRef self_, bool
//      defaultValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QJsonValueConstRef12concreteBoolES_b(
    const QJsonValueConstRef *self_,
    bool defaultValue) {
  return QJsonValueConstRef::concreteBool(*self_, defaultValue);
}

//  qint64 QJsonValueConstRef::concreteInt(QJsonValueConstRef self_, qint64
//      defaultValue, bool clamp)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN18QJsonValueConstRef11concreteIntES_xb(
    const QJsonValueConstRef *self_,
    qint64 defaultValue,
    bool clamp) {
  return QJsonValueConstRef::concreteInt(*self_, defaultValue, clamp);
}

//  double QJsonValueConstRef::concreteDouble(QJsonValueConstRef self_,
//      double defaultValue)
extern "C" Q_DECL_EXPORT
double ritual_ZN18QJsonValueConstRef14concreteDoubleES_d(
    const QJsonValueConstRef *self_,
    double defaultValue) {
  return QJsonValueConstRef::concreteDouble(*self_, defaultValue);
}

//  QString QJsonValueConstRef::concreteString(QJsonValueConstRef self_,
//      const QString &defaultValue)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QJsonValueConstRef14concreteStringES_RK7QString(
    const QJsonValueConstRef *self_,
    const QString *defaultValue) {
  return new QString(
      QJsonValueConstRef::concreteString(
          *self_,
          *defaultValue));
}

//  QAnyStringView QJsonValueConstRef::concreteStringView(QJsonValueConstRef
//      self_, QAnyStringView defaultValue)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QJsonValueConstRef18concreteStringViewES_14QAnyStringView(
    const QJsonValueConstRef *self_,
    const QString *defaultValue) {
  return new QString(
      QJsonValueConstRef::concreteStringView(
          *self_,
          QAnyStringView(*defaultValue)).toString());
}

//  QJsonValue QJsonValueConstRef::concrete(QJsonValueConstRef self_)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN18QJsonValueConstRef8concreteES_(
    const QJsonValueConstRef *self_) {
  return new QJsonValue(QJsonValueConstRef::concrete(*self_));
}

//  QString QJsonValueConstRef::objectKey(QJsonValueConstRef self_)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QJsonValueConstRef9objectKeyES_(
    const QJsonValueConstRef *self_) {
  return new QString(QJsonValueConstRef::objectKey(*self_));
}

//  QString QJsonValueConstRef::objectKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QJsonValueConstRef9objectKeyEv(
    const QJsonValueConstRef *self) {
  return new QString(self->objectKey());
}

//  QAnyStringView QJsonValueConstRef::objectKeyView(QJsonValueConstRef
//      self_)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QJsonValueConstRef13objectKeyViewES_(
    const QJsonValueConstRef *self_) {
  return new QString(QJsonValueConstRef::objectKeyView(*self_).toString());
}

//  QAnyStringView QJsonValueConstRef::objectKeyView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QJsonValueConstRef13objectKeyViewEv(
    const QJsonValueConstRef *self) {
  return new QString(self->objectKeyView().toString());
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValueConstRef::QJsonValueConstRef(QJsonArray *array, qsizetype idx)
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZN18QJsonValueConstRefC1EP10QJsonArrayx(
    QJsonArray *array,
    qsizetype idx) {
  return new QJsonValueConstRef(array, idx);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValueConstRef::QJsonValueConstRef(QJsonObject *object, qsizetype
//      idx)
extern "C" Q_DECL_EXPORT
QJsonValueConstRef *ritual_ZN18QJsonValueConstRefC1EP11QJsonObjectx(
    QJsonObject *object,
    qsizetype idx) {
  return new QJsonValueConstRef(object, idx);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  void QJsonValueConstRef::rebind(QJsonValueConstRef other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QJsonValueConstRef6rebindES_(
    QJsonValueConstRef *self,
    const QJsonValueConstRef *other) {
  self->rebind(*other);
}
#endif

//  QJsonValueConstRef::~QJsonValueConstRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QJsonValueConstRefD1Ev(QJsonValueConstRef *self) {
  delete self;
}
