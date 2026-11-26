//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtime_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtime_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  ReturnedValue QV4::RuntimeHelpers::objectDefaultValue(const Object
//      *object, int typeHint)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414RuntimeHelpers18objectDefaultValueEPKNS_6ObjectEi(
    const QV4::Object *object,
    int typeHint) {
  return QV4::RuntimeHelpers::objectDefaultValue(object, typeHint);
}

//  ReturnedValue QV4::RuntimeHelpers::toPrimitive(const Value &value,
//      TypeHint typeHint)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414RuntimeHelpers11toPrimitiveERKNS_5ValueENS_8TypeHintE(
    const QV4::Value *value,
    QV4::TypeHint typeHint) {
  return QV4::RuntimeHelpers::toPrimitive(*value, typeHint);
}

//  ReturnedValue QV4::RuntimeHelpers::ordinaryToPrimitive(ExecutionEngine
//      *engine, const Object *object, String *typeHint)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414RuntimeHelpers19ordinaryToPrimitiveEPNS_15ExecutionEngineEPKNS_6ObjectEPNS_6StringE(
    QV4::ExecutionEngine *engine,
    const QV4::Object *object,
    QV4::String *typeHint) {
  return QV4::RuntimeHelpers::ordinaryToPrimitive(engine, object, typeHint);
}

//  double QV4::RuntimeHelpers::stringToNumber(const QString &s)
extern "C" Q_DECL_EXPORT
double ritual_ZN3QV414RuntimeHelpers14stringToNumberERK7QString(
    const QString *s) {
  return QV4::RuntimeHelpers::stringToNumber(*s);
}

//  Heap::String *QV4::RuntimeHelpers::stringFromNumber(ExecutionEngine
//      *engine, double number)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV414RuntimeHelpers16stringFromNumberEPNS_15ExecutionEngineEd(
    QV4::ExecutionEngine *engine,
    double number) {
  return QV4::RuntimeHelpers::stringFromNumber(engine, number);
}

//  double QV4::RuntimeHelpers::toNumber(const Value &value)
extern "C" Q_DECL_EXPORT
double ritual_ZN3QV414RuntimeHelpers8toNumberERKNS_5ValueE(
    const QV4::Value *value) {
  return QV4::RuntimeHelpers::toNumber(*value);
}

//  void QV4::RuntimeHelpers::numberToString(QString *result, double num, int
//      radix)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414RuntimeHelpers14numberToStringEP7QStringdi(
    QString *result,
    double num,
    int radix) {
  QV4::RuntimeHelpers::numberToString(result, num, radix);
}

//  Heap::String *QV4::RuntimeHelpers::convertToString(ExecutionEngine
//      *engine, Value value, TypeHint a2)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV414RuntimeHelpers15convertToStringEPNS_15ExecutionEngineENS_5ValueENS_8TypeHintE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *value,
    QV4::TypeHint a2) {
  return QV4::RuntimeHelpers::convertToString(engine, *value, a2);
}

//  Heap::Object *QV4::RuntimeHelpers::convertToObject(ExecutionEngine
//      *engine, const Value &value)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV414RuntimeHelpers15convertToObjectEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *value) {
  return QV4::RuntimeHelpers::convertToObject(engine, *value);
}

//  Bool QV4::RuntimeHelpers::equalHelper(const Value &x, const Value &y)
extern "C" Q_DECL_EXPORT
QV4::Bool ritual_ZN3QV414RuntimeHelpers11equalHelperERKNS_5ValueES3_(
    const QV4::Value *x,
    const QV4::Value *y) {
  return QV4::RuntimeHelpers::equalHelper(*x, *y);
}

//  Bool QV4::RuntimeHelpers::strictEqual(const Value &x, const Value &y)
extern "C" Q_DECL_EXPORT
QV4::Bool ritual_ZN3QV414RuntimeHelpers11strictEqualERKNS_5ValueES3_(
    const QV4::Value *x,
    const QV4::Value *y) {
  return QV4::RuntimeHelpers::strictEqual(*x, *y);
}

//  ReturnedValue QV4::RuntimeHelpers::addHelper(ExecutionEngine *engine,
//      const Value &left, const Value &right)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414RuntimeHelpers9addHelperEPNS_15ExecutionEngineERKNS_5ValueES5_(
    QV4::ExecutionEngine *engine,
    const QV4::Value *left,
    const QV4::Value *right) {
  return QV4::RuntimeHelpers::addHelper(engine, *left, *right);
}

//  QV4::RuntimeHelpers::~RuntimeHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414RuntimeHelpersD1Ev(QV4::RuntimeHelpers *self) {
  delete self;
}
