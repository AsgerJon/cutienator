//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborvalue.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qurl.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
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

//  QCborValueRef::QCborValueRef(QCborValueRef &&a0)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefC1EOS_(QCborValueRef *a0) {
  return new QCborValueRef(std::move(*a0));
}

//  QCborValueRef &QCborValueRef::operator=(const QCborValue &other)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefaSERK10QCborValue(
    QCborValueRef *self,
    const QCborValue *other) {
  return &(self->operator=(*other));
}

//  QCborValueRef &QCborValueRef::operator=(QCborValue &&other)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefaSEO10QCborValue(
    QCborValueRef *self,
    QCborValue *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCborValueRef &QCborValueRef::operator=(const QCborValueRef &other)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefaSERKS_(
    QCborValueRef *self,
    const QCborValueRef *other) {
  return &(self->operator=(*other));
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

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue QCborValueRef::operator QCborValue() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefcv10QCborValueEv(
    const QCborValueRef *self) {
  return new QCborValue(self->operator QCborValue());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue::Type QCborValueRef::type() const
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZNK13QCborValueRef4typeEv(
    const QCborValueRef *self) {
  return self->type();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef9isIntegerEv(const QCborValueRef *self) {
  return self->isInteger();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isByteArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef11isByteArrayEv(const QCborValueRef *self) {
  return self->isByteArray();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef8isStringEv(const QCborValueRef *self) {
  return self->isString();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef7isArrayEv(const QCborValueRef *self) {
  return self->isArray();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isMap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef5isMapEv(const QCborValueRef *self) {
  return self->isMap();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isTag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef5isTagEv(const QCborValueRef *self) {
  return self->isTag();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isFalse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef7isFalseEv(const QCborValueRef *self) {
  return self->isFalse();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isTrue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isTrueEv(const QCborValueRef *self) {
  return self->isTrue();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isBoolEv(const QCborValueRef *self) {
  return self->isBool();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isNullEv(const QCborValueRef *self) {
  return self->isNull();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef11isUndefinedEv(const QCborValueRef *self) {
  return self->isUndefined();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isDouble() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef8isDoubleEv(const QCborValueRef *self) {
  return self->isDouble();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isDateTime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef10isDateTimeEv(const QCborValueRef *self) {
  return self->isDateTime();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef5isUrlEv(const QCborValueRef *self) {
  return self->isUrl();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isRegularExpression() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef19isRegularExpressionEv(
    const QCborValueRef *self) {
  return self->isRegularExpression();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isUuid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6isUuidEv(const QCborValueRef *self) {
  return self->isUuid();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isInvalid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef9isInvalidEv(const QCborValueRef *self) {
  return self->isInvalid();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isContainer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef11isContainerEv(const QCborValueRef *self) {
  return self->isContainer();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isSimpleType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef12isSimpleTypeEv(const QCborValueRef *self) {
  return self->isSimpleType();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::isSimpleType(QCborSimpleType st) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef12isSimpleTypeE15QCborSimpleType(
    const QCborValueRef *self,
    QCborSimpleType st) {
  return self->isSimpleType(st);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborSimpleType QCborValueRef::toSimpleType(QCborSimpleType defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QCborSimpleType ritual_ZNK13QCborValueRef12toSimpleTypeE15QCborSimpleType(
    const QCborValueRef *self,
    QCborSimpleType defaultValue) {
  return self->toSimpleType(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborTag QCborValueRef::tag(QCborTag defaultValue) const
extern "C" Q_DECL_EXPORT
QCborTag ritual_ZNK13QCborValueRef3tagE8QCborTag(
    const QCborValueRef *self,
    QCborTag defaultValue) {
  return self->tag(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue QCborValueRef::taggedValue(const QCborValue &defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRef11taggedValueERK10QCborValue(
    const QCborValueRef *self,
    const QCborValue *defaultValue) {
  return new QCborValue(self->taggedValue(*defaultValue));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  qint64 QCborValueRef::toInteger(qint64 defaultValue) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QCborValueRef9toIntegerEx(
    const QCborValueRef *self,
    qint64 defaultValue) {
  return self->toInteger(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  bool QCborValueRef::toBool(bool defaultValue) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QCborValueRef6toBoolEb(
    const QCborValueRef *self,
    bool defaultValue) {
  return self->toBool(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  double QCborValueRef::toDouble(double defaultValue) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QCborValueRef8toDoubleEd(
    const QCborValueRef *self,
    double defaultValue) {
  return self->toDouble(defaultValue);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QByteArray QCborValueRef::toByteArray(const QByteArray &defaultValue)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QCborValueRef11toByteArrayERK10QByteArray(
    const QCborValueRef *self,
    const QByteArray *defaultValue) {
  return new QByteArray(self->toByteArray(*defaultValue));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QString QCborValueRef::toString(const QString &defaultValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QCborValueRef8toStringERK7QString(
    const QCborValueRef *self,
    const QString *defaultValue) {
  return new QString(self->toString(*defaultValue));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
#if QT_CONFIG(datestring)
//  QDateTime QCborValueRef::toDateTime(const QDateTime &defaultValue) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QCborValueRef10toDateTimeERK9QDateTime(
    const QCborValueRef *self,
    const QDateTime *defaultValue) {
  return new QDateTime(self->toDateTime(*defaultValue));
}
#endif  // QT_CONFIG(datestring)
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
#if !defined(QT_BOOTSTRAPPED)
//  QUrl QCborValueRef::toUrl(const QUrl &defaultValue) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QCborValueRef5toUrlERK4QUrl(
    const QCborValueRef *self,
    const QUrl *defaultValue) {
  return new QUrl(self->toUrl(*defaultValue));
}
#endif  // !defined(QT_BOOTSTRAPPED)
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
#if !defined(QT_BOOTSTRAPPED)
#if QT_CONFIG(regularexpression)
//  QRegularExpression QCborValueRef::toRegularExpression(const
//      QRegularExpression &defaultValue) const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK13QCborValueRef19toRegularExpressionERK18QRegularExpression(
    const QCborValueRef *self,
    const QRegularExpression *defaultValue) {
  return new QRegularExpression(self->toRegularExpression(*defaultValue));
}
#endif  // QT_CONFIG(regularexpression)
#endif  // !defined(QT_BOOTSTRAPPED)
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
#if !defined(QT_BOOTSTRAPPED)
//  QUuid QCborValueRef::toUuid(const QUuid &defaultValue) const
extern "C" Q_DECL_EXPORT
QUuid *ritual_ZNK13QCborValueRef6toUuidERK5QUuid(
    const QCborValueRef *self,
    const QUuid *defaultValue) {
  return new QUuid(self->toUuid(*defaultValue));
}
#endif  // !defined(QT_BOOTSTRAPPED)
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborArray QCborValueRef::toArray() const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK13QCborValueRef7toArrayEv(const QCborValueRef *self) {
  return new QCborArray(self->toArray());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborArray QCborValueRef::toArray(const QCborArray &a) const
extern "C" Q_DECL_EXPORT
QCborArray *ritual_ZNK13QCborValueRef7toArrayERK10QCborArray(
    const QCborValueRef *self,
    const QCborArray *a) {
  return new QCborArray(self->toArray(*a));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborMap QCborValueRef::toMap() const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK13QCborValueRef5toMapEv(const QCborValueRef *self) {
  return new QCborMap(self->toMap());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborMap QCborValueRef::toMap(const QCborMap &m) const
extern "C" Q_DECL_EXPORT
QCborMap *ritual_ZNK13QCborValueRef5toMapERK8QCborMap(
    const QCborValueRef *self,
    const QCborMap *m) {
  return new QCborMap(self->toMap(*m));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  const QCborValue QCborValueRef::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefixERK7QString(
    const QCborValueRef *self,
    const QString *key) {
  return new QCborValue(self->operator[](*key));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  const QCborValue QCborValueRef::operator[](QLatin1StringView key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefixE13QLatin1String(
    const QCborValueRef *self,
    const QLatin1String *key) {
  return new QCborValue(self->operator[](*key));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  const QCborValue QCborValueRef::operator[](qint64 key) const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRefixEx(
    const QCborValueRef *self,
    qint64 key) {
  return new QCborValue(self->operator[](key));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  int QCborValueRef::compare(const QCborValue &other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QCborValueRef7compareERK10QCborValue(
    const QCborValueRef *self,
    const QCborValue *other) {
  return self->compare(*other);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QVariant QCborValueRef::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QCborValueRef9toVariantEv(const QCborValueRef *self) {
  return new QVariant(self->toVariant());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QJsonValue QCborValueRef::toJsonValue() const
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZNK13QCborValueRef11toJsonValueEv(
    const QCborValueRef *self) {
  return new QJsonValue(self->toJsonValue());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
#if QT_CONFIG(cborstreamwriter)
//  QByteArray QCborValueRef::toCbor(QCborValue::EncodingOptions opt)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN13QCborValueRef6toCborE6QFlagsIN10QCborValue14EncodingOptionEE(
    QCborValueRef *self,
    int opt) {
  return new QByteArray(
      self->toCbor(
          QFlags<QCborValue::EncodingOption>::fromInt(opt)));
}
#endif  // QT_CONFIG(cborstreamwriter)
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
#if QT_CONFIG(cborstreamwriter)
//  void QCborValueRef::toCbor(QCborStreamWriter &writer,
//      QCborValue::EncodingOptions opt)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCborValueRef6toCborER17QCborStreamWriter6QFlagsIN10QCborValue14EncodingOptionEE(
    QCborValueRef *self,
    QCborStreamWriter *writer,
    int opt) {
  self->toCbor(*writer, QFlags<QCborValue::EncodingOption>::fromInt(opt));
}
#endif  // QT_CONFIG(cborstreamwriter)
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
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
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue QCborValueRef::concrete(QCborValueRef that)
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZN13QCborValueRef8concreteES_(const QCborValueRef *that) {
  return new QCborValue(QCborValueRef::concrete(*that));
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue QCborValueRef::concrete() const
extern "C" Q_DECL_EXPORT
QCborValue *ritual_ZNK13QCborValueRef8concreteEv(const QCborValueRef *self) {
  return new QCborValue(self->concrete());
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue::Type QCborValueRef::concreteType(QCborValueRef self_)
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZN13QCborValueRef12concreteTypeES_(
    const QCborValueRef *self_) {
  return QCborValueRef::concreteType(*self_);
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValue::Type QCborValueRef::concreteType() const
extern "C" Q_DECL_EXPORT
QCborValue::Type ritual_ZNK13QCborValueRef12concreteTypeEv(
    const QCborValueRef *self) {
  return self->concreteType();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValueRef::QCborValueRef()
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefC1Ev() {
  return new QCborValueRef();
}
#endif

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0) && !defined(QT_BOOTSTRAPPED)
//  QCborValueRef::QCborValueRef(QCborContainerPrivate *dd, qsizetype ii)
extern "C" Q_DECL_EXPORT
QCborValueRef *ritual_ZN13QCborValueRefC1EP21QCborContainerPrivatex(
    QCborContainerPrivate *dd,
    qsizetype ii) {
  return new QCborValueRef(dd, ii);
}
#endif

//  void QCborValueRef::assign(QCborValueRef that, const QCborValue &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCborValueRef6assignES_RK10QCborValue(
    const QCborValueRef *that,
    const QCborValue *other) {
  QCborValueRef::assign(*that, *other);
}

//  void QCborValueRef::assign(QCborValueRef that, QCborValue &&other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCborValueRef6assignES_O10QCborValue(
    const QCborValueRef *that,
    QCborValue *other) {
  QCborValueRef::assign(*that, std::move(*other));
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
