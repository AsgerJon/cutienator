//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 47, as _ZN3QV410SymbolCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue SymbolCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *, int, const Value *)
{
    return f->engine()->throwTypeError(QStringLiteral("Symbol can't be used together with |new|."));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 52, as _ZN3QV410SymbolCtor10method_forEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue SymbolCtor::method_for(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    ScopedValue k(scope, argc ? argv[0] : Value::undefinedValue());
    ScopedString key(scope, k->toString(scope.engine));
    if (scope.hasException())
        return Encode::undefined();
    QString desc = QLatin1Char('@') + key->toQString();
    return scope.engine->identifierTable->insertSymbol(desc)->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4symbol.cpp, line 63, as _ZN3QV410SymbolCtor13method_keyForEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue SymbolCtor::method_keyFor(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *e = f->engine();
    if (!argc || !argv[0].isSymbol())
        return e->throwTypeError(QLatin1String("Symbol.keyFor: Argument is not a symbol."));
    const Symbol &arg = static_cast<const Symbol &>(argv[0]);
    Heap::Symbol *s = e->identifierTable->symbolForId(arg.propertyKey());
    Q_ASSERT(!s || s == arg.d());
    if (s)
        return e->newString(arg.toQString().mid((1)))->asReturnedValue();
    return Encode::undefined();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::SymbolCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410SymbolCtor10__dataTestEv(QV4::SymbolCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::SymbolCtor *QV4::SymbolCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SymbolCtor *ritual_ZNK3QV410SymbolCtor11d_uncheckedEv(
    const QV4::SymbolCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SymbolCtor *QV4::SymbolCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SymbolCtor *ritual_ZNK3QV410SymbolCtor1dEv(
    const QV4::SymbolCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::SymbolCtor::virtualCallAsConstructor(const
//      FunctionObject *a0, const Value *argv, int argc, const Value
//      *newTarget)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410SymbolCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *a0,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *newTarget) {
  return QV4::SymbolCtor::virtualCallAsConstructor(
      a0,
      argv,
      argc,
      newTarget);
}

//  ReturnedValue QV4::SymbolCtor::method_for(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410SymbolCtor10method_forEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SymbolCtor::method_for(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::SymbolCtor::method_keyFor(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410SymbolCtor13method_keyForEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SymbolCtor::method_keyFor(a0, thisObject, argv, argc);
}
