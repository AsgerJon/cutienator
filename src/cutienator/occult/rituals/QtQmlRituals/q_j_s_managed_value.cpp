//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qjsmanagedvalue.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qjsmanagedvalue.h>
#include <QtQml/qjsvalue.h>
#include <QtQml/qjsprimitivevalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>

//  QJSManagedValue::QJSManagedValue()
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN15QJSManagedValueC1Ev() {
  return new QJSManagedValue();
}

//  QJSManagedValue::QJSManagedValue(QJSValue value, QJSEngine *engine)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN15QJSManagedValueC1E8QJSValueP9QJSEngine(
    const QJSValue *value,
    QJSEngine *engine) {
  return new QJSManagedValue(*value, engine);
}

//  QJSManagedValue::QJSManagedValue(const QJSPrimitiveValue &value,
//      QJSEngine *engine)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN15QJSManagedValueC1ERK17QJSPrimitiveValueP9QJSEngine(
    const QJSPrimitiveValue *value,
    QJSEngine *engine) {
  return new QJSManagedValue(*value, engine);
}

//  QJSManagedValue::QJSManagedValue(const QVariant &variant, QJSEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN15QJSManagedValueC1ERK8QVariantP9QJSEngine(
    const QVariant *variant,
    QJSEngine *engine) {
  return new QJSManagedValue(*variant, engine);
}

//  QJSManagedValue::QJSManagedValue(const QString &string, QJSEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN15QJSManagedValueC1ERK7QStringP9QJSEngine(
    const QString *string,
    QJSEngine *engine) {
  return new QJSManagedValue(*string, engine);
}

//  QJSManagedValue::~QJSManagedValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSManagedValueD1Ev(QJSManagedValue *self) {
  delete self;
}

//  QJSEngine *QJSManagedValue::engine() const
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZNK15QJSManagedValue6engineEv(
    const QJSManagedValue *self) {
  return self->engine();
}

//  Type QJSManagedValue::type() const
extern "C" Q_DECL_EXPORT
QJSManagedValue::Type ritual_ZNK15QJSManagedValue4typeEv(
    const QJSManagedValue *self) {
  return self->type();
}

//  bool QJSManagedValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue11isUndefinedEv(
    const QJSManagedValue *self) {
  return self->isUndefined();
}

//  bool QJSManagedValue::isBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue9isBooleanEv(const QJSManagedValue *self) {
  return self->isBoolean();
}

//  bool QJSManagedValue::isNumber() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue8isNumberEv(const QJSManagedValue *self) {
  return self->isNumber();
}

//  bool QJSManagedValue::isString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue8isStringEv(const QJSManagedValue *self) {
  return self->isString();
}

//  bool QJSManagedValue::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue8isObjectEv(const QJSManagedValue *self) {
  return self->isObject();
}

//  bool QJSManagedValue::isSymbol() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue8isSymbolEv(const QJSManagedValue *self) {
  return self->isSymbol();
}

//  bool QJSManagedValue::isFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue10isFunctionEv(const QJSManagedValue *self) {
  return self->isFunction();
}

//  bool QJSManagedValue::isInteger() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue9isIntegerEv(const QJSManagedValue *self) {
  return self->isInteger();
}

//  bool QJSManagedValue::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue6isNullEv(const QJSManagedValue *self) {
  return self->isNull();
}

//  bool QJSManagedValue::isRegularExpression() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue19isRegularExpressionEv(
    const QJSManagedValue *self) {
  return self->isRegularExpression();
}

//  bool QJSManagedValue::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue7isArrayEv(const QJSManagedValue *self) {
  return self->isArray();
}

//  bool QJSManagedValue::isUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue5isUrlEv(const QJSManagedValue *self) {
  return self->isUrl();
}

//  bool QJSManagedValue::isVariant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue9isVariantEv(const QJSManagedValue *self) {
  return self->isVariant();
}

//  bool QJSManagedValue::isQObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue9isQObjectEv(const QJSManagedValue *self) {
  return self->isQObject();
}

//  bool QJSManagedValue::isQMetaObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue13isQMetaObjectEv(
    const QJSManagedValue *self) {
  return self->isQMetaObject();
}

//  bool QJSManagedValue::isDate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue6isDateEv(const QJSManagedValue *self) {
  return self->isDate();
}

//  bool QJSManagedValue::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue7isErrorEv(const QJSManagedValue *self) {
  return self->isError();
}

//  bool QJSManagedValue::isJsMetaType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue12isJsMetaTypeEv(
    const QJSManagedValue *self) {
  return self->isJsMetaType();
}

//  QString QJSManagedValue::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QJSManagedValue8toStringEv(
    const QJSManagedValue *self) {
  return new QString(self->toString());
}

//  double QJSManagedValue::toNumber() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QJSManagedValue8toNumberEv(const QJSManagedValue *self) {
  return self->toNumber();
}

//  bool QJSManagedValue::toBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue9toBooleanEv(const QJSManagedValue *self) {
  return self->toBoolean();
}

//  QJSPrimitiveValue QJSManagedValue::toPrimitive() const
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZNK15QJSManagedValue11toPrimitiveEv(
    const QJSManagedValue *self) {
  return new QJSPrimitiveValue(self->toPrimitive());
}

//  QJSValue QJSManagedValue::toJSValue() const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QJSManagedValue9toJSValueEv(
    const QJSManagedValue *self) {
  return new QJSValue(self->toJSValue());
}

//  QVariant QJSManagedValue::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QJSManagedValue9toVariantEv(
    const QJSManagedValue *self) {
  return new QVariant(self->toVariant());
}

//  int QJSManagedValue::toInteger() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QJSManagedValue9toIntegerEv(const QJSManagedValue *self) {
  return self->toInteger();
}

//  QRegularExpression QJSManagedValue::toRegularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK15QJSManagedValue19toRegularExpressionEv(
    const QJSManagedValue *self) {
  return new QRegularExpression(self->toRegularExpression());
}

//  QUrl QJSManagedValue::toUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QJSManagedValue5toUrlEv(const QJSManagedValue *self) {
  return new QUrl(self->toUrl());
}

//  QObject *QJSManagedValue::toQObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QJSManagedValue9toQObjectEv(
    const QJSManagedValue *self) {
  return self->toQObject();
}

//  const QMetaObject *QJSManagedValue::toQMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QJSManagedValue13toQMetaObjectEv(
    const QJSManagedValue *self) {
  return self->toQMetaObject();
}

//  QDateTime QJSManagedValue::toDateTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK15QJSManagedValue10toDateTimeEv(
    const QJSManagedValue *self) {
  return new QDateTime(self->toDateTime());
}

//  bool QJSManagedValue::hasProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue11hasPropertyERK7QString(
    const QJSManagedValue *self,
    const QString *name) {
  return self->hasProperty(*name);
}

//  bool QJSManagedValue::hasOwnProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue14hasOwnPropertyERK7QString(
    const QJSManagedValue *self,
    const QString *name) {
  return self->hasOwnProperty(*name);
}

//  QJSValue QJSManagedValue::property(const QString &name) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QJSManagedValue8propertyERK7QString(
    const QJSManagedValue *self,
    const QString *name) {
  return new QJSValue(self->property(*name));
}

//  void QJSManagedValue::setProperty(const QString &name, const QJSValue
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSManagedValue11setPropertyERK7QStringRK8QJSValue(
    QJSManagedValue *self,
    const QString *name,
    const QJSValue *value) {
  self->setProperty(*name, *value);
}

//  bool QJSManagedValue::deleteProperty(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QJSManagedValue14deletePropertyERK7QString(
    QJSManagedValue *self,
    const QString *name) {
  return self->deleteProperty(*name);
}

//  bool QJSManagedValue::hasProperty(quint32 arrayIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue11hasPropertyEj(
    const QJSManagedValue *self,
    quint32 arrayIndex) {
  return self->hasProperty(arrayIndex);
}

//  bool QJSManagedValue::hasOwnProperty(quint32 arrayIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QJSManagedValue14hasOwnPropertyEj(
    const QJSManagedValue *self,
    quint32 arrayIndex) {
  return self->hasOwnProperty(arrayIndex);
}

//  QJSValue QJSManagedValue::property(quint32 arrayIndex) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QJSManagedValue8propertyEj(
    const QJSManagedValue *self,
    quint32 arrayIndex) {
  return new QJSValue(self->property(arrayIndex));
}

//  void QJSManagedValue::setProperty(quint32 arrayIndex, const QJSValue
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSManagedValue11setPropertyEjRK8QJSValue(
    QJSManagedValue *self,
    quint32 arrayIndex,
    const QJSValue *value) {
  self->setProperty(arrayIndex, *value);
}

//  bool QJSManagedValue::deleteProperty(quint32 arrayIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QJSManagedValue14deletePropertyEj(
    QJSManagedValue *self,
    quint32 arrayIndex) {
  return self->deleteProperty(arrayIndex);
}

//  QJSValue QJSManagedValue::call(const QJSValueList &arguments) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QJSManagedValue4callERK5QListI8QJSValueE(
    const QJSManagedValue *self,
    const QList<QJSValue> *arguments) {
  return new QJSValue(self->call(*arguments));
}

//  QJSValue QJSManagedValue::callWithInstance(const QJSValue &instance,
//      const QJSValueList &arguments) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QJSManagedValue16callWithInstanceERK8QJSValueRK5QListIS0_E(
    const QJSManagedValue *self,
    const QJSValue *instance,
    const QList<QJSValue> *arguments) {
  return new QJSValue(self->callWithInstance(*instance, *arguments));
}

//  QJSValue QJSManagedValue::callAsConstructor(const QJSValueList
//      &arguments) const
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZNK15QJSManagedValue17callAsConstructorERK5QListI8QJSValueE(
    const QJSManagedValue *self,
    const QList<QJSValue> *arguments) {
  return new QJSValue(self->callAsConstructor(*arguments));
}

//  QStringList QJSManagedValue::jsMetaMembers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QJSManagedValue13jsMetaMembersEv(
    const QJSManagedValue *self) {
  return new QList<QString>(self->jsMetaMembers());
}

//  QJSManagedValue::QJSManagedValue(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QJSManagedValue *ritual_ZN15QJSManagedValueC1EPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QJSManagedValue(engine);
}
