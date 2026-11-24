//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4engine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4engine_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  Value *QV4::ExecutionEngine::jsAlloca(int nValues)
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV415ExecutionEngine8jsAllocaEi(
    QV4::ExecutionEngine *self,
    int nValues) {
  return self->jsAlloca(nValues);
}

//  QJSEngine *QV4::ExecutionEngine::jsEngine() const
extern "C" Q_DECL_EXPORT
QJSEngine *ritual_ZNK3QV415ExecutionEngine8jsEngineEv(
    const QV4::ExecutionEngine *self) {
  return self->jsEngine();
}

//  QQmlEngine *QV4::ExecutionEngine::qmlEngine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK3QV415ExecutionEngine9qmlEngineEv(
    const QV4::ExecutionEngine *self) {
  return self->qmlEngine();
}

//  ExecutionContext *QV4::ExecutionEngine::rootContext() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV415ExecutionEngine11rootContextEv(
    const QV4::ExecutionEngine *self) {
  return self->rootContext();
}

//  ExecutionContext *QV4::ExecutionEngine::scriptContext() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV415ExecutionEngine13scriptContextEv(
    const QV4::ExecutionEngine *self) {
  return self->scriptContext();
}

//  void QV4::ExecutionEngine::setScriptContext(ReturnedValue c)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine16setScriptContextEy(
    QV4::ExecutionEngine *self,
    QV4::ReturnedValue c) {
  self->setScriptContext(c);
}

//  FunctionObject *QV4::ExecutionEngine::objectCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine10objectCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->objectCtor();
}

//  FunctionObject *QV4::ExecutionEngine::stringCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine10stringCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->stringCtor();
}

//  FunctionObject *QV4::ExecutionEngine::symbolCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine10symbolCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->symbolCtor();
}

//  FunctionObject *QV4::ExecutionEngine::numberCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine10numberCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->numberCtor();
}

//  FunctionObject *QV4::ExecutionEngine::booleanCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine11booleanCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->booleanCtor();
}

//  FunctionObject *QV4::ExecutionEngine::arrayCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine9arrayCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->arrayCtor();
}

//  FunctionObject *QV4::ExecutionEngine::functionCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine12functionCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->functionCtor();
}

//  FunctionObject *QV4::ExecutionEngine::generatorFunctionCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine21generatorFunctionCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->generatorFunctionCtor();
}

//  FunctionObject *QV4::ExecutionEngine::dateCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine8dateCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->dateCtor();
}

//  FunctionObject *QV4::ExecutionEngine::regExpCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine10regExpCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->regExpCtor();
}

//  FunctionObject *QV4::ExecutionEngine::errorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine9errorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->errorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::evalErrorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine13evalErrorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->evalErrorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::rangeErrorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine14rangeErrorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->rangeErrorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::referenceErrorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine18referenceErrorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->referenceErrorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::syntaxErrorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine15syntaxErrorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->syntaxErrorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::typeErrorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine13typeErrorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->typeErrorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::uRIErrorCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine12uRIErrorCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->uRIErrorCtor();
}

//  FunctionObject *QV4::ExecutionEngine::sharedArrayBufferCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine21sharedArrayBufferCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->sharedArrayBufferCtor();
}

//  FunctionObject *QV4::ExecutionEngine::promiseCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine11promiseCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->promiseCtor();
}

//  FunctionObject *QV4::ExecutionEngine::arrayBufferCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine15arrayBufferCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->arrayBufferCtor();
}

//  FunctionObject *QV4::ExecutionEngine::dataViewCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine12dataViewCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->dataViewCtor();
}

//  FunctionObject *QV4::ExecutionEngine::weakSetCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine11weakSetCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->weakSetCtor();
}

//  FunctionObject *QV4::ExecutionEngine::setCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine7setCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->setCtor();
}

//  FunctionObject *QV4::ExecutionEngine::weakMapCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine11weakMapCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->weakMapCtor();
}

//  FunctionObject *QV4::ExecutionEngine::mapCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine7mapCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->mapCtor();
}

//  FunctionObject *QV4::ExecutionEngine::intrinsicTypedArrayCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine23intrinsicTypedArrayCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->intrinsicTypedArrayCtor();
}

//  FunctionObject *QV4::ExecutionEngine::urlCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine7urlCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->urlCtor();
}

//  FunctionObject *QV4::ExecutionEngine::urlSearchParamsCtor() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine19urlSearchParamsCtorEv(
    const QV4::ExecutionEngine *self) {
  return self->urlSearchParamsCtor();
}

//  FunctionObject *QV4::ExecutionEngine::getSymbolSpecies() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine16getSymbolSpeciesEv(
    const QV4::ExecutionEngine *self) {
  return self->getSymbolSpecies();
}

//  Object *QV4::ExecutionEngine::objectPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine15objectPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->objectPrototype();
}

//  Object *QV4::ExecutionEngine::symbolPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine15symbolPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->symbolPrototype();
}

//  Object *QV4::ExecutionEngine::arrayPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine14arrayPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->arrayPrototype();
}

//  Object *QV4::ExecutionEngine::arrayProtoValues() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine16arrayProtoValuesEv(
    const QV4::ExecutionEngine *self) {
  return self->arrayProtoValues();
}

//  Object *QV4::ExecutionEngine::propertyListPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine21propertyListPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->propertyListPrototype();
}

//  Object *QV4::ExecutionEngine::stringPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine15stringPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->stringPrototype();
}

//  Object *QV4::ExecutionEngine::numberPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine15numberPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->numberPrototype();
}

//  Object *QV4::ExecutionEngine::booleanPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine16booleanPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->booleanPrototype();
}

//  Object *QV4::ExecutionEngine::datePrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine13datePrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->datePrototype();
}

//  Object *QV4::ExecutionEngine::functionPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine17functionPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->functionPrototype();
}

//  Object *QV4::ExecutionEngine::generatorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine18generatorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->generatorPrototype();
}

//  Object *QV4::ExecutionEngine::regExpPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine15regExpPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->regExpPrototype();
}

//  Object *QV4::ExecutionEngine::errorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine14errorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->errorPrototype();
}

//  Object *QV4::ExecutionEngine::evalErrorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine18evalErrorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->evalErrorPrototype();
}

//  Object *QV4::ExecutionEngine::rangeErrorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine19rangeErrorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->rangeErrorPrototype();
}

//  Object *QV4::ExecutionEngine::referenceErrorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine23referenceErrorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->referenceErrorPrototype();
}

//  Object *QV4::ExecutionEngine::syntaxErrorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine20syntaxErrorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->syntaxErrorPrototype();
}

//  Object *QV4::ExecutionEngine::typeErrorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine18typeErrorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->typeErrorPrototype();
}

//  Object *QV4::ExecutionEngine::uRIErrorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine17uRIErrorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->uRIErrorPrototype();
}

//  Object *QV4::ExecutionEngine::promisePrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine16promisePrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->promisePrototype();
}

//  Object *QV4::ExecutionEngine::variantPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine16variantPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->variantPrototype();
}

//  Object *QV4::ExecutionEngine::variantAssociationPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine27variantAssociationPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->variantAssociationPrototype();
}

//  Object *QV4::ExecutionEngine::sequencePrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine17sequencePrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->sequencePrototype();
}

//  Object *QV4::ExecutionEngine::sharedArrayBufferPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine26sharedArrayBufferPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->sharedArrayBufferPrototype();
}

//  Object *QV4::ExecutionEngine::arrayBufferPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine20arrayBufferPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->arrayBufferPrototype();
}

//  Object *QV4::ExecutionEngine::dataViewPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine17dataViewPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->dataViewPrototype();
}

//  Object *QV4::ExecutionEngine::weakSetPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine16weakSetPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->weakSetPrototype();
}

//  Object *QV4::ExecutionEngine::setPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine12setPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->setPrototype();
}

//  Object *QV4::ExecutionEngine::weakMapPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine16weakMapPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->weakMapPrototype();
}

//  Object *QV4::ExecutionEngine::mapPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine12mapPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->mapPrototype();
}

//  Object *QV4::ExecutionEngine::intrinsicTypedArrayPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine28intrinsicTypedArrayPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->intrinsicTypedArrayPrototype();
}

//  Object *QV4::ExecutionEngine::valueTypeWrapperPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine25valueTypeWrapperPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->valueTypeWrapperPrototype();
}

//  Object *QV4::ExecutionEngine::signalHandlerPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine22signalHandlerPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->signalHandlerPrototype();
}

//  Object *QV4::ExecutionEngine::typeWrapperPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine20typeWrapperPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->typeWrapperPrototype();
}

//  Object *QV4::ExecutionEngine::iteratorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine17iteratorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->iteratorPrototype();
}

//  Object *QV4::ExecutionEngine::forInIteratorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine22forInIteratorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->forInIteratorPrototype();
}

//  Object *QV4::ExecutionEngine::setIteratorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine20setIteratorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->setIteratorPrototype();
}

//  Object *QV4::ExecutionEngine::mapIteratorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine20mapIteratorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->mapIteratorPrototype();
}

//  Object *QV4::ExecutionEngine::arrayIteratorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine22arrayIteratorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->arrayIteratorPrototype();
}

//  Object *QV4::ExecutionEngine::stringIteratorPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine23stringIteratorPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->stringIteratorPrototype();
}

//  Object *QV4::ExecutionEngine::urlPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine12urlPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->urlPrototype();
}

//  Object *QV4::ExecutionEngine::urlSearchParamsPrototype() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415ExecutionEngine24urlSearchParamsPrototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->urlSearchParamsPrototype();
}

//  EvalFunction *QV4::ExecutionEngine::evalFunction() const
extern "C" Q_DECL_EXPORT
QV4::EvalFunction *ritual_ZNK3QV415ExecutionEngine12evalFunctionEv(
    const QV4::ExecutionEngine *self) {
  return self->evalFunction();
}

//  FunctionObject *QV4::ExecutionEngine::getStackFunction() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine16getStackFunctionEv(
    const QV4::ExecutionEngine *self) {
  return self->getStackFunction();
}

//  FunctionObject *QV4::ExecutionEngine::thrower() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415ExecutionEngine7throwerEv(
    const QV4::ExecutionEngine *self) {
  return self->thrower();
}

//  String *QV4::ExecutionEngine::id_empty() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_emptyEv(
    const QV4::ExecutionEngine *self) {
  return self->id_empty();
}

//  String *QV4::ExecutionEngine::id_undefined() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine12id_undefinedEv(
    const QV4::ExecutionEngine *self) {
  return self->id_undefined();
}

//  String *QV4::ExecutionEngine::id_null() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_nullEv(
    const QV4::ExecutionEngine *self) {
  return self->id_null();
}

//  String *QV4::ExecutionEngine::id_true() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_trueEv(
    const QV4::ExecutionEngine *self) {
  return self->id_true();
}

//  String *QV4::ExecutionEngine::id_false() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_falseEv(
    const QV4::ExecutionEngine *self) {
  return self->id_false();
}

//  String *QV4::ExecutionEngine::id_boolean() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine10id_booleanEv(
    const QV4::ExecutionEngine *self) {
  return self->id_boolean();
}

//  String *QV4::ExecutionEngine::id_number() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_numberEv(
    const QV4::ExecutionEngine *self) {
  return self->id_number();
}

//  String *QV4::ExecutionEngine::id_string() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_stringEv(
    const QV4::ExecutionEngine *self) {
  return self->id_string();
}

//  String *QV4::ExecutionEngine::id_default() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine10id_defaultEv(
    const QV4::ExecutionEngine *self) {
  return self->id_default();
}

//  String *QV4::ExecutionEngine::id_symbol() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_symbolEv(
    const QV4::ExecutionEngine *self) {
  return self->id_symbol();
}

//  String *QV4::ExecutionEngine::id_object() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_objectEv(
    const QV4::ExecutionEngine *self) {
  return self->id_object();
}

//  String *QV4::ExecutionEngine::id_function() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine11id_functionEv(
    const QV4::ExecutionEngine *self) {
  return self->id_function();
}

//  String *QV4::ExecutionEngine::id_length() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_lengthEv(
    const QV4::ExecutionEngine *self) {
  return self->id_length();
}

//  String *QV4::ExecutionEngine::id_prototype() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine12id_prototypeEv(
    const QV4::ExecutionEngine *self) {
  return self->id_prototype();
}

//  String *QV4::ExecutionEngine::id_constructor() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine14id_constructorEv(
    const QV4::ExecutionEngine *self) {
  return self->id_constructor();
}

//  String *QV4::ExecutionEngine::id_arguments() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine12id_argumentsEv(
    const QV4::ExecutionEngine *self) {
  return self->id_arguments();
}

//  String *QV4::ExecutionEngine::id_caller() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_callerEv(
    const QV4::ExecutionEngine *self) {
  return self->id_caller();
}

//  String *QV4::ExecutionEngine::id_callee() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_calleeEv(
    const QV4::ExecutionEngine *self) {
  return self->id_callee();
}

//  String *QV4::ExecutionEngine::id_this() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_thisEv(
    const QV4::ExecutionEngine *self) {
  return self->id_this();
}

//  String *QV4::ExecutionEngine::id___proto__() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine12id___proto__Ev(
    const QV4::ExecutionEngine *self) {
  return self->id___proto__();
}

//  String *QV4::ExecutionEngine::id_enumerable() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine13id_enumerableEv(
    const QV4::ExecutionEngine *self) {
  return self->id_enumerable();
}

//  String *QV4::ExecutionEngine::id_configurable() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine15id_configurableEv(
    const QV4::ExecutionEngine *self) {
  return self->id_configurable();
}

//  String *QV4::ExecutionEngine::id_writable() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine11id_writableEv(
    const QV4::ExecutionEngine *self) {
  return self->id_writable();
}

//  String *QV4::ExecutionEngine::id_value() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_valueEv(
    const QV4::ExecutionEngine *self) {
  return self->id_value();
}

//  String *QV4::ExecutionEngine::id_get() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine6id_getEv(
    const QV4::ExecutionEngine *self) {
  return self->id_get();
}

//  String *QV4::ExecutionEngine::id_set() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine6id_setEv(
    const QV4::ExecutionEngine *self) {
  return self->id_set();
}

//  String *QV4::ExecutionEngine::id_eval() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_evalEv(
    const QV4::ExecutionEngine *self) {
  return self->id_eval();
}

//  String *QV4::ExecutionEngine::id_uintMax() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine10id_uintMaxEv(
    const QV4::ExecutionEngine *self) {
  return self->id_uintMax();
}

//  String *QV4::ExecutionEngine::id_name() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_nameEv(
    const QV4::ExecutionEngine *self) {
  return self->id_name();
}

//  String *QV4::ExecutionEngine::id_index() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_indexEv(
    const QV4::ExecutionEngine *self) {
  return self->id_index();
}

//  String *QV4::ExecutionEngine::id_input() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_inputEv(
    const QV4::ExecutionEngine *self) {
  return self->id_input();
}

//  String *QV4::ExecutionEngine::id_toString() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine11id_toStringEv(
    const QV4::ExecutionEngine *self) {
  return self->id_toString();
}

//  String *QV4::ExecutionEngine::id_toLocaleString() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine17id_toLocaleStringEv(
    const QV4::ExecutionEngine *self) {
  return self->id_toLocaleString();
}

//  String *QV4::ExecutionEngine::id_destroy() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine10id_destroyEv(
    const QV4::ExecutionEngine *self) {
  return self->id_destroy();
}

//  String *QV4::ExecutionEngine::id_valueOf() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine10id_valueOfEv(
    const QV4::ExecutionEngine *self) {
  return self->id_valueOf();
}

//  String *QV4::ExecutionEngine::id_byteLength() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine13id_byteLengthEv(
    const QV4::ExecutionEngine *self) {
  return self->id_byteLength();
}

//  String *QV4::ExecutionEngine::id_byteOffset() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine13id_byteOffsetEv(
    const QV4::ExecutionEngine *self) {
  return self->id_byteOffset();
}

//  String *QV4::ExecutionEngine::id_buffer() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_bufferEv(
    const QV4::ExecutionEngine *self) {
  return self->id_buffer();
}

//  String *QV4::ExecutionEngine::id_lastIndex() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine12id_lastIndexEv(
    const QV4::ExecutionEngine *self) {
  return self->id_lastIndex();
}

//  String *QV4::ExecutionEngine::id_next() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_nextEv(
    const QV4::ExecutionEngine *self) {
  return self->id_next();
}

//  String *QV4::ExecutionEngine::id_done() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine7id_doneEv(
    const QV4::ExecutionEngine *self) {
  return self->id_done();
}

//  String *QV4::ExecutionEngine::id_return() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_returnEv(
    const QV4::ExecutionEngine *self) {
  return self->id_return();
}

//  String *QV4::ExecutionEngine::id_throw() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_throwEv(
    const QV4::ExecutionEngine *self) {
  return self->id_throw();
}

//  String *QV4::ExecutionEngine::id_global() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_globalEv(
    const QV4::ExecutionEngine *self) {
  return self->id_global();
}

//  String *QV4::ExecutionEngine::id_ignoreCase() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine13id_ignoreCaseEv(
    const QV4::ExecutionEngine *self) {
  return self->id_ignoreCase();
}

//  String *QV4::ExecutionEngine::id_multiline() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine12id_multilineEv(
    const QV4::ExecutionEngine *self) {
  return self->id_multiline();
}

//  String *QV4::ExecutionEngine::id_unicode() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine10id_unicodeEv(
    const QV4::ExecutionEngine *self) {
  return self->id_unicode();
}

//  String *QV4::ExecutionEngine::id_sticky() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_stickyEv(
    const QV4::ExecutionEngine *self) {
  return self->id_sticky();
}

//  String *QV4::ExecutionEngine::id_source() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine9id_sourceEv(
    const QV4::ExecutionEngine *self) {
  return self->id_source();
}

//  String *QV4::ExecutionEngine::id_flags() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415ExecutionEngine8id_flagsEv(
    const QV4::ExecutionEngine *self) {
  return self->id_flags();
}

//  Symbol *QV4::ExecutionEngine::symbol_hasInstance() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine18symbol_hasInstanceEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_hasInstance();
}

//  Symbol *QV4::ExecutionEngine::symbol_isConcatSpreadable() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine25symbol_isConcatSpreadableEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_isConcatSpreadable();
}

//  Symbol *QV4::ExecutionEngine::symbol_iterator() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine15symbol_iteratorEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_iterator();
}

//  Symbol *QV4::ExecutionEngine::symbol_match() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine12symbol_matchEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_match();
}

//  Symbol *QV4::ExecutionEngine::symbol_replace() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine14symbol_replaceEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_replace();
}

//  Symbol *QV4::ExecutionEngine::symbol_search() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine13symbol_searchEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_search();
}

//  Symbol *QV4::ExecutionEngine::symbol_species() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine14symbol_speciesEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_species();
}

//  Symbol *QV4::ExecutionEngine::symbol_split() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine12symbol_splitEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_split();
}

//  Symbol *QV4::ExecutionEngine::symbol_toPrimitive() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine18symbol_toPrimitiveEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_toPrimitive();
}

//  Symbol *QV4::ExecutionEngine::symbol_toStringTag() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine18symbol_toStringTagEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_toStringTag();
}

//  Symbol *QV4::ExecutionEngine::symbol_unscopables() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine18symbol_unscopablesEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_unscopables();
}

//  Symbol *QV4::ExecutionEngine::symbol_revokableProxy() const
extern "C" Q_DECL_EXPORT
QV4::Symbol *ritual_ZNK3QV415ExecutionEngine21symbol_revokableProxyEv(
    const QV4::ExecutionEngine *self) {
  return self->symbol_revokableProxy();
}

#if !(!QT_CONFIG(qml_debug))
//  QV4::Debugging::Debugger *QV4::ExecutionEngine::debugger() const
extern "C" Q_DECL_EXPORT
QV4::Debugging::Debugger *ritual_ZNK3QV415ExecutionEngine8debuggerEv(
    const QV4::ExecutionEngine *self) {
  return self->debugger();
}
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
//  QV4::Profiling::Profiler *QV4::ExecutionEngine::profiler() const
extern "C" Q_DECL_EXPORT
QV4::Profiling::Profiler *ritual_ZNK3QV415ExecutionEngine8profilerEv(
    const QV4::ExecutionEngine *self) {
  return self->profiler();
}
#endif  // !(!QT_CONFIG(qml_debug))

//  quintptr QV4::ExecutionEngine::newProtoId()
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN3QV415ExecutionEngine10newProtoIdEv(
    QV4::ExecutionEngine *self) {
  return self->newProtoId();
}

//  Heap::ExecutionContext
//      *QV4::ExecutionEngine::qmlContext(Heap::ExecutionContext *ctx)
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZN3QV415ExecutionEngine10qmlContextEPNS_4Heap16ExecutionContextE(
    QV4::Heap::ExecutionContext *ctx) {
  return QV4::ExecutionEngine::qmlContext(ctx);
}

//  Heap::QmlContext *QV4::ExecutionEngine::qmlContext() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContext *ritual_ZNK3QV415ExecutionEngine10qmlContextEv(
    const QV4::ExecutionEngine *self) {
  return self->qmlContext();
}

//  QVariant QV4::ExecutionEngine::toVariant(const QV4::Value &value,
//      QMetaType typeHint, bool createJSValueForObjectsAndSymbols)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN3QV415ExecutionEngine9toVariantERKNS_5ValueE9QMetaTypeb(
    const QV4::Value *value,
    const QMetaType *typeHint,
    bool createJSValueForObjectsAndSymbols) {
  return new QVariant(
      QV4::ExecutionEngine::toVariant(
          *value,
          *typeHint,
          createJSValueForObjectsAndSymbols));
}

//  QVariant QV4::ExecutionEngine::toVariantLossy(const QV4::Value &value)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN3QV415ExecutionEngine14toVariantLossyERKNS_5ValueE(
    const QV4::Value *value) {
  return new QVariant(QV4::ExecutionEngine::toVariantLossy(*value));
}

//  QV4::ReturnedValue QV4::ExecutionEngine::fromVariant(const QVariant &a0)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine11fromVariantERK8QVariant(
    QV4::ExecutionEngine *self,
    const QVariant *a0) {
  return self->fromVariant(*a0);
}

//  QV4::ReturnedValue QV4::ExecutionEngine::fromVariant(const QVariant
//      &variant, Heap::Object *parent, int property, uint flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine11fromVariantERK8QVariantPNS_4Heap6ObjectEij(
    QV4::ExecutionEngine *self,
    const QVariant *variant,
    QV4::Heap::Object *parent,
    int property,
    uint flags) {
  return self->fromVariant(*variant, parent, property, flags);
}

//  QVariantMap QV4::ExecutionEngine::variantMapFromJS(const QV4::Object *o)
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN3QV415ExecutionEngine16variantMapFromJSEPKNS_6ObjectE(
    const QV4::Object *o) {
  return new QMap<QString, QVariant>(
      QV4::ExecutionEngine::variantMapFromJS(
          o));
}

//  QVariantHash QV4::ExecutionEngine::variantHashFromJS(const QV4::Object
//      *o)
extern "C" Q_DECL_EXPORT
QHash<QString, QVariant> *ritual_ZN3QV415ExecutionEngine17variantHashFromJSEPKNS_6ObjectE(
    const QV4::Object *o) {
  return new QHash<QString, QVariant>(
      QV4::ExecutionEngine::variantHashFromJS(
          o));
}

//  void QV4::ExecutionEngine::resetQmlEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine14resetQmlEngineEv(
    QV4::ExecutionEngine *self) {
  self->resetQmlEngine();
}

//  QQmlDelayedCallQueue *QV4::ExecutionEngine::delayedCallQueue()
extern "C" Q_DECL_EXPORT
QQmlDelayedCallQueue *ritual_ZN3QV415ExecutionEngine16delayedCallQueueEv(
    QV4::ExecutionEngine *self) {
  return self->delayedCallQueue();
}

//  QMutex *QV4::ExecutionEngine::registrationMutex()
extern "C" Q_DECL_EXPORT
QMutex *ritual_ZN3QV415ExecutionEngine17registrationMutexEv() {
  return QV4::ExecutionEngine::registrationMutex();
}

//  int QV4::ExecutionEngine::registerExtension()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV415ExecutionEngine17registerExtensionEv() {
  return QV4::ExecutionEngine::registerExtension();
}

//  Deletable *QV4::ExecutionEngine::extensionData(int index) const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine::Deletable *ritual_ZNK3QV415ExecutionEngine13extensionDataEi(
    const QV4::ExecutionEngine *self,
    int index) {
  return self->extensionData(index);
}

//  void QV4::ExecutionEngine::setMaxCallDepth(int maxCallDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine15setMaxCallDepthEi(int maxCallDepth) {
  QV4::ExecutionEngine::setMaxCallDepth(maxCallDepth);
}

//  int QV4::ExecutionEngine::maxCallDepth()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV415ExecutionEngine12maxCallDepthEv() {
  return QV4::ExecutionEngine::maxCallDepth();
}

//  bool QV4::ExecutionEngine::hasJsStackOverflow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415ExecutionEngine18hasJsStackOverflowEv(
    const QV4::ExecutionEngine *self) {
  return self->hasJsStackOverflow();
}
