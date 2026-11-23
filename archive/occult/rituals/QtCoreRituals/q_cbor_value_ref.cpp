//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborvalue.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qurl.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/quuid.h>
#include <QtCore/qcborarray.h>
#include <QtCore/qcbormap.h>
#include <QtCore/qvariant.h>
#include <QtCore/qjsonvalue.h>

//  QCborValueRef::QCborValueRef(const QCborValueRef &a0)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefC1ERKS_(const QCborValueRef *a0) {
  return new QCborValueRef(*a0);
}

//  QCborValueRef QCborValueRef::operator[](qint64 key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefixEx(
    QCborValueRef *self,
    qint64 key) {
  return new QCborValueRef(self->operator[](key));
}

//  QCborValueRef QCborValueRef::operator[](QLatin1StringView key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefixE13QLatin1String(
    QCborValueRef *self,
    const QLatin1String *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  QCborValueRef QCborValueRef::operator[](const QString &key)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefixERK7QString(
    QCborValueRef *self,
    const QString *key) {
  return new QCborValueRef(self->operator[](*key));
}

//  QCborValue QCborValueRef::operator QCborValue() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefcv10QCborValueEv(
    const QCborValueRef *self) {
  return new QCborValue(self->operator QCborValue());
}

//  QCborValue::Type QCborValueRef::type() const
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZNK13QCborValueRef4typeEv(
    const QCborValueRef *self) {
  return self->type();
}

//  bool QCborValueRef::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef9isIntegerEv(const QCborValueRef *self) {
  return self->isInteger();
}

//  bool QCborValueRef::isByteArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef11isByteArrayEv(const QCborValueRef *self) {
  return self->isByteArray();
}

//  bool QCborValueRef::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef8isStringEv(const QCborValueRef *self) {
  return self->isString();
}

//  bool QCborValueRef::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef7isArrayEv(const QCborValueRef *self) {
  return self->isArray();
}

//  bool QCborValueRef::isMap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef5isMapEv(const QCborValueRef *self) {
  return self->isMap();
}

//  bool QCborValueRef::isTag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef5isTagEv(const QCborValueRef *self) {
  return self->isTag();
}

//  bool QCborValueRef::isFalse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef7isFalseEv(const QCborValueRef *self) {
  return self->isFalse();
}

//  bool QCborValueRef::isTrue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isTrueEv(const QCborValueRef *self) {
  return self->isTrue();
}

//  bool QCborValueRef::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isBoolEv(const QCborValueRef *self) {
  return self->isBool();
}

//  bool QCborValueRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isNullEv(const QCborValueRef *self) {
  return self->isNull();
}

//  bool QCborValueRef::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef11isUndefinedEv(const QCborValueRef *self) {
  return self->isUndefined();
}

//  bool QCborValueRef::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef8isDoubleEv(const QCborValueRef *self) {
  return self->isDouble();
}

//  bool QCborValueRef::isDateTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef10isDateTimeEv(const QCborValueRef *self) {
  return self->isDateTime();
}

//  bool QCborValueRef::isUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef5isUrlEv(const QCborValueRef *self) {
  return self->isUrl();
}

//  bool QCborValueRef::isRegularExpression() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef19isRegularExpressionEv(
    const QCborValueRef *self) {
  return self->isRegularExpression();
}

//  bool QCborValueRef::isUuid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isUuidEv(const QCborValueRef *self) {
  return self->isUuid();
}

//  bool QCborValueRef::isInvalid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef9isInvalidEv(const QCborValueRef *self) {
  return self->isInvalid();
}

//  bool QCborValueRef::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef11isContainerEv(const QCborValueRef *self) {
  return self->isContainer();
}

//  bool QCborValueRef::isSimpleType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef12isSimpleTypeEv(const QCborValueRef *self) {
  return self->isSimpleType();
}

//  bool QCborValueRef::isSimpleType(QCborSimpleType st) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef12isSimpleTypeE15QCborSimpleType(
    const QCborValueRef *self,
    QCborSimpleType st) {
  return self->isSimpleType(st);
}

//  QCborSimpleType QCborValueRef::toSimpleType(QCborSimpleType defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QCborSimpleType ritual_ZNK13QCborValueRef12toSimpleTypeE15QCborSimpleType(
    const QCborValueRef *self,
    QCborSimpleType defaultValue) {
  return self->toSimpleType(defaultValue);
}

//  QCborTag QCborValueRef::tag(QCborTag defaultValue) const
extern "C" Q_DECL_EXPORT
QCborTag ritual_ZNK13QCborValueRef3tagE8QCborTag(
    const QCborValueRef *self,
    QCborTag defaultValue) {
  return self->tag(defaultValue);
}

//  QCborValue QCborValueRef::taggedValue(const QCborValue &defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRef11taggedValueERK10QCborValue(
    const QCborValueRef *self,
    const QCborValue *defaultValue) {
  return new QCborValue(self->taggedValue(*defaultValue));
}

//  qint64 QCborValueRef::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QCborValueRef9toIntegerEx(
    const QCborValueRef *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}

//  bool QCborValueRef::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6toBoolEb(
    const QCborValueRef *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}

//  double QCborValueRef::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QCborValueRef8toDoubleEd(
    const QCborValueRef *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}

//  QByteArray QCborValueRef::toByteArray(const QByteArray &defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QCborValueRef11toByteArrayERK10QByteArray(
    const QCborValueRef *self,
    const QByteArray *defaultValue) {
  return new QByteArray(self->toByteArray(*defaultValue));
}

//  QString QCborValueRef::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCborValueRef8toStringERK7QString(
    const QCborValueRef *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}

//  QDateTime QCborValueRef::toDateTime(const QDateTime &defaultValue) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QCborValueRef10toDateTimeERK9QDateTime(
    const QCborValueRef *self,
    const QDateTime *defaultValue) {
  return new QDateTime(self->toDateTime(*defaultValue));
}

//  QUrl QCborValueRef::toUrl(const QUrl &defaultValue) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QCborValueRef5toUrlERK4QUrl(
    const QCborValueRef *self,
    const QUrl *defaultValue) {
  return new QUrl(self->toUrl(*defaultValue));
}

//  QRegularExpression QCborValueRef::toRegularExpression(const
//      QRegularExpression &defaultValue) const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK13QCborValueRef19toRegularExpressionERK18QRegularExpression(
    const QCborValueRef *self,
    const QRegularExpression *defaultValue) {
  return new QRegularExpression(self->toRegularExpression(*defaultValue));
}

//  QUuid QCborValueRef::toUuid(const QUuid &defaultValue) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK13QCborValueRef6toUuidERK5QUuid(
    const QCborValueRef *self,
    const QUuid *defaultValue) {
  return new QUuid(self->toUuid(*defaultValue));
}

//  QCborArray QCborValueRef::toArray() const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK13QCborValueRef7toArrayEv(const QCborValueRef *self) {
  return new QCborArray(self->toArray());
}

//  QCborArray QCborValueRef::toArray(const QCborArray &a) const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK13QCborValueRef7toArrayERK10QCborArray(
    const QCborValueRef *self,
    const QCborArray *a) {
  return new QCborArray(self->toArray(*a));
}

//  QCborMap QCborValueRef::toMap() const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK13QCborValueRef5toMapEv(const QCborValueRef *self) {
  return new QCborMap(self->toMap());
}

//  QCborMap QCborValueRef::toMap(const QCborMap &m) const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK13QCborValueRef5toMapERK8QCborMap(
    const QCborValueRef *self,
    const QCborMap *m) {
  return new QCborMap(self->toMap(*m));
}

//  const QCborValue QCborValueRef::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefixERK7QString(
    const QCborValueRef *self,
    const QString *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborValueRef::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefixE13QLatin1String(
    const QCborValueRef *self,
    const QLatin1String *key) {
  return new QCborValue(self->operator[](*key));
}

//  const QCborValue QCborValueRef::operator[](qint64 key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefixEx(
    const QCborValueRef *self,
    qint64 key) {
  return new QCborValue(self->operator[](key));
}

//  int QCborValueRef::compare(const QCborValue &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QCborValueRef7compareERK10QCborValue(
    const QCborValueRef *self,
    const QCborValue *other) {
  return self->compare(*other);
}

//  QVariant QCborValueRef::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QCborValueRef9toVariantEv(const QCborValueRef *self) {
  return new QVariant(self->toVariant());
}

//  QJsonValue QCborValueRef::toJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QCborValueRef11toJsonValueEv(
    const QCborValueRef *self) {
  return new QJsonValue(self->toJsonValue());
}

//  QByteArray QCborValueRef::toCbor(QCborValue::EncodingOptions opt)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN13QCborValueRef6toCborE6QFlagsIN10QCborValue14EncodingOptionEE(
    QCborValueRef *self,
    int opt) {
  return new QByteArray(
      self->toCbor(
          QFlags<QCborValue::EncodingOption>::fromInt(opt)));
}

//  QString
//      QCborValueRef::toDiagnosticNotation(QCborValue::DiagnosticNotationOpt
//      ions opt)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCborValueRef20toDiagnosticNotationE6QFlagsIN10QCborValue24DiagnosticNotationOptionEE(
    QCborValueRef *self,
    int opt) {
  return new QString(
      self->toDiagnosticNotation(
          QFlags<QCborValue::DiagnosticNotationOption>::fromInt(opt)));
}

//  QCborValue QCborValueRef::concrete(QCborValueRef that)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN13QCborValueRef8concreteES_(const QCborValueRef *that) {
  return new QCborValue(QCborValueRef::concrete(*that));
}

//  QCborValue QCborValueRef::concrete() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRef8concreteEv(const QCborValueRef *self) {
  return new QCborValue(self->concrete());
}

//  QCborValue::Type QCborValueRef::concreteType(QCborValueRef self_)
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZN13QCborValueRef12concreteTypeES_(
    const QCborValueRef *self_) {
  return QCborValueRef::concreteType(*self_);
}

//  QCborValue::Type QCborValueRef::concreteType() const
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZNK13QCborValueRef12concreteTypeEv(
    const QCborValueRef *self) {
  return self->concreteType();
}

//  QCborValueRef::QCborValueRef()
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefC1Ev() {
  return new QCborValueRef();
}

//  void QCborValueRef::assign(QCborValueRef that, const QCborValue &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCborValueRef6assignES_RK10QCborValue(
    const QCborValueRef *that,
    const QCborValue *other) {
  QCborValueRef::assign(*that, *other);
}

//  void QCborValueRef::assign(QCborValueRef that, const QCborValueRef other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCborValueRef6assignES_S_(
    const QCborValueRef *that,
    const QCborValueRef *other) {
  QCborValueRef::assign(*that, *other);
}

//  QCborValueRef::~QCborValueRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCborValueRefD1Ev(QCborValueRef *self) {
  delete self;
}
