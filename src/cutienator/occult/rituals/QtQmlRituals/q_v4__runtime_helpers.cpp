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

//  ReturnedValue QV4::RuntimeHelpers::toPrimitive(const Value &value,
//      TypeHint typeHint)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414RuntimeHelpers11toPrimitiveERKNS_5ValueENS_8TypeHintE(
    const QV4::Value *value,
    QV4::TypeHint typeHint) {
  return QV4::RuntimeHelpers::toPrimitive(*value, typeHint);
}

//  double QV4::RuntimeHelpers::stringToNumber(const QString &s)
extern "C" Q_DECL_EXPORT
double ritual_ZN3QV414RuntimeHelpers14stringToNumberERK7QString(
    const QString *s) {
  return QV4::RuntimeHelpers::stringToNumber(*s);
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

//  Bool QV4::RuntimeHelpers::strictEqual(const Value &x, const Value &y)
extern "C" Q_DECL_EXPORT
QV4::Bool ritual_ZN3QV414RuntimeHelpers11strictEqualERKNS_5ValueES3_(
    const QV4::Value *x,
    const QV4::Value *y) {
  return QV4::RuntimeHelpers::strictEqual(*x, *y);
}

//  QV4::RuntimeHelpers::~RuntimeHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414RuntimeHelpersD1Ev(QV4::RuntimeHelpers *self) {
  delete self;
}
