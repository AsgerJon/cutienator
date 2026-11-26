//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qvariant.h>
#include <QtQml/qjsprimitivevalue.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QJSValue::QJSValue(SpecialValue value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1ENS_12SpecialValueE(
    QJSValue::SpecialValue value) {
  return new QJSValue(value);
}

//  QJSValue::~QJSValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QJSValueD1Ev(QJSValue *self) {
  delete self;
}

//  QJSValue::QJSValue(const QJSValue &other)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1ERKS_(const QJSValue *other) {
  return new QJSValue(*other);
}

//  QJSValue::QJSValue(QJSValue &&other)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1EOS_(QJSValue *other) {
  return new QJSValue(std::move(*other));
}

//  QJSValue &QJSValue::operator=(QJSValue &&other)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueaSEOS_(QJSValue *self, QJSValue *other) {
  return &(self->operator=(std::move(*other)));
}

//  QJSValue::QJSValue(bool value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1Eb(bool value) {
  return new QJSValue(value);
}

//  QJSValue::QJSValue(int value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1Ei(int value) {
  return new QJSValue(value);
}

//  QJSValue::QJSValue(uint value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1Ej(uint value) {
  return new QJSValue(value);
}

//  QJSValue::QJSValue(double value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1Ed(double value) {
  return new QJSValue(value);
}

//  QJSValue::QJSValue(const QString &value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1ERK7QString(const QString *value) {
  return new QJSValue(*value);
}

//  QJSValue::QJSValue(const QLatin1String &value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1ERK13QLatin1String(
    const QLatin1String *value) {
  return new QJSValue(*value);
}

#if !defined(QT_NO_CAST_FROM_ASCII)
//  QJSValue::QJSValue(const char *str)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1EPKc(const char *str) {
  return new QJSValue(str);
}
#endif  // !defined(QT_NO_CAST_FROM_ASCII)

//  QJSValue &QJSValue::operator=(const QJSValue &other)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueaSERKS_(QJSValue *self, const QJSValue *other) {
  return &(self->operator=(*other));
}

//  QJSValue::QJSValue(QJSPrimitiveValue &&value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1EO17QJSPrimitiveValue(
    QJSPrimitiveValue *value) {
  return new QJSValue(std::move(*value));
}

//  QJSValue::QJSValue(QJSManagedValue &&value)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN8QJSValueC1EO15QJSManagedValue(QJSManagedValue *value) {
  return new QJSValue(std::move(*value));
}

//  bool QJSValue::isBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue6isBoolEv(const QJSValue *self) {
  return self->isBool();
}

//  bool QJSValue::isNumber() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue8isNumberEv(const QJSValue *self) {
  return self->isNumber();
}

//  bool QJSValue::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue6isNullEv(const QJSValue *self) {
  return self->isNull();
}

//  bool QJSValue::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue8isStringEv(const QJSValue *self) {
  return self->isString();
}

//  bool QJSValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue11isUndefinedEv(const QJSValue *self) {
  return self->isUndefined();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  bool QJSValue::isVariant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue9isVariantEv(const QJSValue *self) {
  return self->isVariant();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  bool QJSValue::isQObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue9isQObjectEv(const QJSValue *self) {
  return self->isQObject();
}

//  bool QJSValue::isQMetaObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue13isQMetaObjectEv(const QJSValue *self) {
  return self->isQMetaObject();
}

//  bool QJSValue::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue8isObjectEv(const QJSValue *self) {
  return self->isObject();
}

//  bool QJSValue::isDate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue6isDateEv(const QJSValue *self) {
  return self->isDate();
}

//  bool QJSValue::isRegExp() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue8isRegExpEv(const QJSValue *self) {
  return self->isRegExp();
}

//  bool QJSValue::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue7isArrayEv(const QJSValue *self) {
  return self->isArray();
}

//  bool QJSValue::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue7isErrorEv(const QJSValue *self) {
  return self->isError();
}

//  bool QJSValue::isUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue5isUrlEv(const QJSValue *self) {
  return self->isUrl();
}

//  QString QJSValue::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QJSValue8toStringEv(const QJSValue *self) {
  return new QString(self->toString());
}

//  double QJSValue::toNumber() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK8QJSValue8toNumberEv(const QJSValue *self) {
  return self->toNumber();
}

//  qint32 QJSValue::toInt() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK8QJSValue5toIntEv(const QJSValue *self) {
  return self->toInt();
}

//  quint32 QJSValue::toUInt() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK8QJSValue6toUIntEv(const QJSValue *self) {
  return self->toUInt();
}

//  bool QJSValue::toBool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue6toBoolEv(const QJSValue *self) {
  return self->toBool();
}

//  QVariant QJSValue::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QJSValue9toVariantEv(const QJSValue *self) {
  return new QVariant(self->toVariant());
}

//  QVariant QJSValue::toVariant(ObjectConversionBehavior behavior) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QJSValue9toVariantENS_24ObjectConversionBehaviorE(
    const QJSValue *self,
    QJSValue::ObjectConversionBehavior behavior) {
  return new QVariant(self->toVariant(behavior));
}

//  QJSPrimitiveValue QJSValue::toPrimitive() const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZNK8QJSValue11toPrimitiveEv(const QJSValue *self) {
  return new QJSPrimitiveValue(self->toPrimitive());
}

//  QObject *QJSValue::toQObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK8QJSValue9toQObjectEv(const QJSValue *self) {
  return self->toQObject();
}

//  const QMetaObject *QJSValue::toQMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8QJSValue13toQMetaObjectEv(
    const QJSValue *self) {
  return self->toQMetaObject();
}

//  QDateTime QJSValue::toDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK8QJSValue10toDateTimeEv(const QJSValue *self) {
  return new QDateTime(self->toDateTime());
}

//  bool QJSValue::equals(const QJSValue &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue6equalsERKS_(
    const QJSValue *self,
    const QJSValue *other) {
  return self->equals(*other);
}

//  bool QJSValue::strictlyEquals(const QJSValue &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue14strictlyEqualsERKS_(
    const QJSValue *self,
    const QJSValue *other) {
  return self->strictlyEquals(*other);
}

//  QJSValue QJSValue::prototype() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QJSValue9prototypeEv(const QJSValue *self) {
  return new QJSValue(self->prototype());
}

//  void QJSValue::setPrototype(const QJSValue &prototype)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QJSValue12setPrototypeERKS_(
    QJSValue *self,
    const QJSValue *prototype) {
  self->setPrototype(*prototype);
}

//  QJSValue QJSValue::property(const QString &name) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QJSValue8propertyERK7QString(
    const QJSValue *self,
    const QString *name) {
  return new QJSValue(self->property(*name));
}

//  void QJSValue::setProperty(const QString &name, const QJSValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QJSValue11setPropertyERK7QStringRKS_(
    QJSValue *self,
    const QString *name,
    const QJSValue *value) {
  self->setProperty(*name, *value);
}

//  bool QJSValue::hasProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue11hasPropertyERK7QString(
    const QJSValue *self,
    const QString *name) {
  return self->hasProperty(*name);
}

//  bool QJSValue::hasOwnProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue14hasOwnPropertyERK7QString(
    const QJSValue *self,
    const QString *name) {
  return self->hasOwnProperty(*name);
}

//  QJSValue QJSValue::property(quint32 arrayIndex) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QJSValue8propertyEj(
    const QJSValue *self,
    quint32 arrayIndex) {
  return new QJSValue(self->property(arrayIndex));
}

//  void QJSValue::setProperty(quint32 arrayIndex, const QJSValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QJSValue11setPropertyEjRKS_(
    QJSValue *self,
    quint32 arrayIndex,
    const QJSValue *value) {
  self->setProperty(arrayIndex, *value);
}

//  bool QJSValue::deleteProperty(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QJSValue14deletePropertyERK7QString(
    QJSValue *self,
    const QString *name) {
  return self->deleteProperty(*name);
}

//  bool QJSValue::isCallable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QJSValue10isCallableEv(const QJSValue *self) {
  return self->isCallable();
}

//  QJSValue QJSValue::call(const QJSValueList &args) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QJSValue4callERK5QListIS_E(
    const QJSValue *self,
    const QList<QJSValue> *args) {
  return new QJSValue(self->call(*args));
}

//  QJSValue QJSValue::callWithInstance(const QJSValue &instance, const
//      QJSValueList &args) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QJSValue16callWithInstanceERKS_RK5QListIS_E(
    const QJSValue *self,
    const QJSValue *instance,
    const QList<QJSValue> *args) {
  return new QJSValue(self->callWithInstance(*instance, *args));
}

//  QJSValue QJSValue::callAsConstructor(const QJSValueList &args) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK8QJSValue17callAsConstructorERK5QListIS_E(
    const QJSValue *self,
    const QList<QJSValue> *args) {
  return new QJSValue(self->callAsConstructor(*args));
}

//  ErrorType QJSValue::errorType() const
extern "C" Q_DECL_EXPORT
QJSValue::ErrorType ritual_ZNK8QJSValue9errorTypeEv(const QJSValue *self) {
  return self->errorType();
}

//  QList<QJSValue>::QList()
extern "C" Q_DECL_EXPORT
QList<QJSValue> *ritual_list_make_QJSValue() {
  return new QList<QJSValue>();
}

//  void QList<QJSValue>::append(const QJSValue &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QJSValue(
    QList<QJSValue> *self,
    const QJSValue *element) {
  self->append(*element);
}

//  qsizetype QList<QJSValue>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QJSValue(const QList<QJSValue> *self) {
  return self->size();
}

//  const QJSValue &QList<QJSValue>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_list_at_QJSValue(
    const QList<QJSValue> *self,
    long long index) {
  return new QJSValue(self->at(index));
}

//  QList<QJSValue>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QJSValue(QList<QJSValue> *self) {
  delete self;
}

//  QHash<QString, QJSValue>: QHash<QString, QJSValue>()
extern "C" Q_DECL_EXPORT
QHash<QString, QJSValue> *ritual_map_make_QHash_QString_QJSValue() {
  return new QHash<QString, QJSValue>();
}

//  QHash<QString, QJSValue>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_QString_QJSValue(
    QHash<QString, QJSValue> *self,
    const QString *key,
    const QJSValue *value) {
  self->insert(*key, *value);
}

//  QHash<QString, QJSValue>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_QString_QJSValue(
    const QHash<QString, QJSValue> *self) {
  return self->size();
}

//  QHash<QString, QJSValue>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QHash_QString_QJSValue(
    const QHash<QString, QJSValue> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QHash<QString, QJSValue>: the value at a place
extern "C" Q_DECL_EXPORT
QJSValue *ritual_map_value_QHash_QString_QJSValue(
    const QHash<QString, QJSValue> *self,
    long long index) {
  return new QJSValue(*std::next(self->constBegin(), index));
}

//  QHash<QString, QJSValue>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_QString_QJSValue(
    const QHash<QString, QJSValue> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QHash<QString, QJSValue>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_map_get_QHash_QString_QJSValue(
    const QHash<QString, QJSValue> *self,
    const QString *key) {
  return new QJSValue(self->value(*key));
}

//  QHash<QString, QJSValue>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_QString_QJSValue(QHash<QString, QJSValue> *self) {
  delete self;
}
