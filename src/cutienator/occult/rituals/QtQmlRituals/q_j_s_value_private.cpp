//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qjsvalue_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 1. Kept
//  as it is when the generator runs again. Also added by hand on 2026-11-25,
//  rituals for functions the generator leaves out: 1.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qjsvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <QtQml/qjsvalue.h>
#include <QtQml/6.12.0/QtQml/private/qv4managed_p.h>

//  Kind QJSValuePrivate::tag(quint64 raw)
extern "C" Q_DECL_EXPORT
QJSValuePrivate::Kind ritual_ZN15QJSValuePrivate3tagEy(quint64 raw) {
  return QJSValuePrivate::tag(raw);
}

#if !(QT_POINTER_SIZE == 4)
//  void *QJSValuePrivate::pointer(quint64 raw)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QJSValuePrivate7pointerEy(quint64 raw) {
  return QJSValuePrivate::pointer(raw);
}
#endif  // !(QT_POINTER_SIZE == 4)

#if !(QT_POINTER_SIZE == 4)
//  quint64 QJSValuePrivate::encodePointer(void *pointer, Kind tag)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate13encodePointerEPvNS_4KindE(
    void *pointer,
    QJSValuePrivate::Kind tag) {
  return QJSValuePrivate::encodePointer(pointer, tag);
}
#endif  // !(QT_POINTER_SIZE == 4)

//  quint64 QJSValuePrivate::encodeUndefined()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate15encodeUndefinedEv() {
  return QJSValuePrivate::encodeUndefined();
}

//  quint64 QJSValuePrivate::encodeNull()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate10encodeNullEv() {
  return QJSValuePrivate::encodeNull();
}

//  int QJSValuePrivate::intValue(quint64 v)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QJSValuePrivate8intValueEy(quint64 v) {
  return QJSValuePrivate::intValue(v);
}

//  quint64 QJSValuePrivate::encode(int intValue)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeEi(int intValue) {
  return QJSValuePrivate::encode(intValue);
}

//  quint64 QJSValuePrivate::encode(uint uintValue)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeEj(uint uintValue) {
  return QJSValuePrivate::encode(uintValue);
}

//  bool QJSValuePrivate::boolValue(quint64 v)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QJSValuePrivate9boolValueEy(quint64 v) {
  return QJSValuePrivate::boolValue(v);
}

//  quint64 QJSValuePrivate::encode(bool boolValue)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeEb(bool boolValue) {
  return QJSValuePrivate::encode(boolValue);
}

//  quint64 QJSValuePrivate::encode(double doubleValue)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeEd(double doubleValue) {
  return QJSValuePrivate::encode(doubleValue);
}

//  QV4::Value *QJSValuePrivate::qv4ValuePtr(quint64 v)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN15QJSValuePrivate11qv4ValuePtrEy(quint64 v) {
  return QJSValuePrivate::qv4ValuePtr(v);
}

//  quint64 QJSValuePrivate::encode(const QV4::Value &qv4Value)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeERKN3QV45ValueE(
    const QV4::Value *qv4Value) {
  return QJSValuePrivate::encode(*qv4Value);
}

//  QString *QJSValuePrivate::qStringPtr(quint64 v)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QJSValuePrivate10qStringPtrEy(quint64 v) {
  return QJSValuePrivate::qStringPtr(v);
}

//  quint64 QJSValuePrivate::encode(QString stringValue)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeE7QString(
    const QString *stringValue) {
  return QJSValuePrivate::encode(*stringValue);
}

//  quint64 QJSValuePrivate::encode(QLatin1String stringValue)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN15QJSValuePrivate6encodeE13QLatin1String(
    const QLatin1String *stringValue) {
  return QJSValuePrivate::encode(*stringValue);
}

//  QJSValue QJSValuePrivate::fromReturnedValue(QV4::ReturnedValue d)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN15QJSValuePrivate17fromReturnedValueEy(
    QV4::ReturnedValue d) {
  return new QJSValue(QJSValuePrivate::fromReturnedValue(d));
}

//  QV4::Value *QJSValuePrivate::takeManagedValue(QJSValue *jsval)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN15QJSValuePrivate16takeManagedValueEP8QJSValue(
    QJSValue *jsval) {
  return QJSValuePrivate::takeManagedValue(jsval);
}

//  QV4::ReturnedValue QJSValuePrivate::asPrimitiveType(const QJSValue
//      *jsval)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN15QJSValuePrivate15asPrimitiveTypeEPK8QJSValue(
    const QJSValue *jsval) {
  return QJSValuePrivate::asPrimitiveType(jsval);
}

//  const QString *QJSValuePrivate::asQString(const QJSValue *jsval)
extern "C" Q_DECL_EXPORT
const QString *ritual_ZN15QJSValuePrivate9asQStringEPK8QJSValue(
    const QJSValue *jsval) {
  return QJSValuePrivate::asQString(jsval);
}

//  QV4::ReturnedValue QJSValuePrivate::asReturnedValue(const QJSValue
//      *jsval)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN15QJSValuePrivate15asReturnedValueEPK8QJSValue(
    const QJSValue *jsval) {
  return QJSValuePrivate::asReturnedValue(jsval);
}

//  void QJSValuePrivate::setString(QJSValue *jsval, QString s)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSValuePrivate9setStringEP8QJSValue7QString(
    QJSValue *jsval,
    const QString *s) {
  QJSValuePrivate::setString(jsval, *s);
}

//  void QJSValuePrivate::adoptPersistentValue(QJSValue *jsval, QV4::Value
//      *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSValuePrivate20adoptPersistentValueEP8QJSValuePN3QV45ValueE(
    QJSValue *jsval,
    QV4::Value *v) {
  QJSValuePrivate::adoptPersistentValue(jsval, v);
}

//  void QJSValuePrivate::setValue(QJSValue *jsval, const QV4::Value &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSValuePrivate8setValueEP8QJSValueRKN3QV45ValueE(
    QJSValue *jsval,
    const QV4::Value *v) {
  QJSValuePrivate::setValue(jsval, *v);
}

//  void QJSValuePrivate::manageStringOnV4Heap(QV4::ExecutionEngine *e,
//      QJSValue *jsval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSValuePrivate20manageStringOnV4HeapEPN3QV415ExecutionEngineEP8QJSValue(
    QV4::ExecutionEngine *e,
    QJSValue *jsval) {
  QJSValuePrivate::manageStringOnV4Heap(e, jsval);
}

//  QV4::ReturnedValue
//      QJSValuePrivate::convertToReturnedValue(QV4::ExecutionEngine *e,
//      const QJSValue &jsval)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN15QJSValuePrivate22convertToReturnedValueEPN3QV415ExecutionEngineERK8QJSValue(
    QV4::ExecutionEngine *e,
    const QJSValue *jsval) {
  return QJSValuePrivate::convertToReturnedValue(e, *jsval);
}

//  QV4::ExecutionEngine *QJSValuePrivate::engine(const QJSValue *jsval)
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZN15QJSValuePrivate6engineEPK8QJSValue(
    const QJSValue *jsval) {
  return QJSValuePrivate::engine(jsval);
}

//  bool QJSValuePrivate::checkEngine(QV4::ExecutionEngine *e, const QJSValue
//      &jsval)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QJSValuePrivate11checkEngineEPN3QV415ExecutionEngineERK8QJSValue(
    QV4::ExecutionEngine *e,
    const QJSValue *jsval) {
  return QJSValuePrivate::checkEngine(e, *jsval);
}

//  void QJSValuePrivate::free(QJSValue *jsval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSValuePrivate4freeEP8QJSValue(QJSValue *jsval) {
  QJSValuePrivate::free(jsval);
}

//  QJSValuePrivate::~QJSValuePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QJSValuePrivateD1Ev(QJSValuePrivate *self) {
  delete self;
}

//  static const QV4::Managed
//      *QJSValuePrivate::asManagedType<QV4::Managed>(const QJSValue *jsval)
extern "C" Q_DECL_EXPORT
const QV4::Managed * ritual_ZN15QJSValuePrivate13asManagedTypeIN3QV47ManagedEEEPKT_PK8QJSValue(
    const QJSValue *jsval) {
  return QJSValuePrivate::asManagedType<QV4::Managed>(jsval);
}

//  static double *QJSValuePrivate::doublePtr(quint64 v)
extern "C" Q_DECL_EXPORT
double *ritual_ZN15QJSValuePrivate9doublePtrEy(
    quint64 v) {
  return QJSValuePrivate::doublePtr(v);
}
