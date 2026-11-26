//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4engine_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 7. Kept
//  as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4engine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtQml/qqmlerror.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QUrl>
#include <QtCore/QMultiHash>

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

#if QT_CONFIG(qml_network)
//  QNetworkAccessManager *QV4::ExecutionEngine::getNetworkAccessManager()
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZN3QV415ExecutionEngine23getNetworkAccessManagerEv(
    QV4::ExecutionEngine *self) {
  return self->getNetworkAccessManager();
}
#endif  // QT_CONFIG(qml_network)

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

//  QV4::ExecutionEngine::ExecutionEngine(QJSEngine *jsEngine)
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZN3QV415ExecutionEngineC1EP9QJSEngine(
    QJSEngine *jsEngine) {
  return new QV4::ExecutionEngine(jsEngine);
}

//  QV4::ExecutionEngine::~ExecutionEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngineD1Ev(QV4::ExecutionEngine *self) {
  delete self;
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

#if !(!QT_CONFIG(qml_debug))
//  void QV4::ExecutionEngine::setDebugger(Debugging::Debugger *debugger)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine11setDebuggerEPNS_9Debugging8DebuggerE(
    QV4::ExecutionEngine *self,
    QV4::Debugging::Debugger *debugger) {
  self->setDebugger(debugger);
}
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
//  void QV4::ExecutionEngine::setProfiler(Profiling::Profiler *profiler)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine11setProfilerEPNS_9Profiling8ProfilerE(
    QV4::ExecutionEngine *self,
    QV4::Profiling::Profiler *profiler) {
  self->setProfiler(profiler);
}
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
//  void QV4::ExecutionEngine::setPreviewing(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine13setPreviewingEb(bool enabled) {
  QV4::ExecutionEngine::setPreviewing(enabled);
}
#endif  // !(!QT_CONFIG(qml_debug))

//  quintptr QV4::ExecutionEngine::newProtoId()
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN3QV415ExecutionEngine10newProtoIdEv(
    QV4::ExecutionEngine *self) {
  return self->newProtoId();
}

//  Heap::InternalClass *QV4::ExecutionEngine::newInternalClass(const VTable
//      *vtable, Object *prototype)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV415ExecutionEngine16newInternalClassEPKNS_6VTableEPNS_6ObjectE(
    QV4::ExecutionEngine *self,
    const QV4::VTable *vtable,
    QV4::Object *prototype) {
  return self->newInternalClass(vtable, prototype);
}

//  Heap::Object *QV4::ExecutionEngine::newObject()
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine9newObjectEv(
    QV4::ExecutionEngine *self) {
  return self->newObject();
}

//  Heap::Object *QV4::ExecutionEngine::newObject(Heap::InternalClass
//      *internalClass)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine9newObjectEPNS_4Heap13InternalClassE(
    QV4::ExecutionEngine *self,
    QV4::Heap::InternalClass *internalClass) {
  return self->newObject(internalClass);
}

//  Heap::String *QV4::ExecutionEngine::newString(char16_t c)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV415ExecutionEngine9newStringEDs(
    QV4::ExecutionEngine *self,
    char16_t c) {
  return self->newString(c);
}

//  Heap::String *QV4::ExecutionEngine::newString(const QString &s)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV415ExecutionEngine9newStringERK7QString(
    QV4::ExecutionEngine *self,
    const QString *s) {
  return self->newString(*s);
}

//  Heap::String *QV4::ExecutionEngine::newIdentifier(const QString &text)
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV415ExecutionEngine13newIdentifierERK7QString(
    QV4::ExecutionEngine *self,
    const QString *text) {
  return self->newIdentifier(*text);
}

//  Heap::Object *QV4::ExecutionEngine::newStringObject(const String *string)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine15newStringObjectEPKNS_6StringE(
    QV4::ExecutionEngine *self,
    const QV4::String *string) {
  return self->newStringObject(string);
}

//  Heap::Object *QV4::ExecutionEngine::newSymbolObject(const Symbol *symbol)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine15newSymbolObjectEPKNS_6SymbolE(
    QV4::ExecutionEngine *self,
    const QV4::Symbol *symbol) {
  return self->newSymbolObject(symbol);
}

//  Heap::Object *QV4::ExecutionEngine::newNumberObject(double value)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine15newNumberObjectEd(
    QV4::ExecutionEngine *self,
    double value) {
  return self->newNumberObject(value);
}

//  Heap::Object *QV4::ExecutionEngine::newBooleanObject(bool b)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine16newBooleanObjectEb(
    QV4::ExecutionEngine *self,
    bool b) {
  return self->newBooleanObject(b);
}

//  Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(int count)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV415ExecutionEngine14newArrayObjectEi(
    QV4::ExecutionEngine *self,
    int count) {
  return self->newArrayObject(count);
}

//  Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(const Value
//      *values, int length)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV415ExecutionEngine14newArrayObjectEPKNS_5ValueEi(
    QV4::ExecutionEngine *self,
    const QV4::Value *values,
    int length) {
  return self->newArrayObject(values, length);
}

//  Heap::ArrayObject *QV4::ExecutionEngine::newArrayObject(const QStringList
//      &list)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV415ExecutionEngine14newArrayObjectERK5QListI7QStringE(
    QV4::ExecutionEngine *self,
    const QList<QString> *list) {
  return self->newArrayObject(*list);
}

//  Heap::ArrayObject
//      *QV4::ExecutionEngine::newArrayObject(Heap::InternalClass *ic)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV415ExecutionEngine14newArrayObjectEPNS_4Heap13InternalClassE(
    QV4::ExecutionEngine *self,
    QV4::Heap::InternalClass *ic) {
  return self->newArrayObject(ic);
}

//  Heap::ArrayBuffer *QV4::ExecutionEngine::newArrayBuffer(const QByteArray
//      &array)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayBuffer *ritual_ZN3QV415ExecutionEngine14newArrayBufferERK10QByteArray(
    QV4::ExecutionEngine *self,
    const QByteArray *array) {
  return self->newArrayBuffer(*array);
}

//  Heap::ArrayBuffer *QV4::ExecutionEngine::newArrayBuffer(size_t length)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayBuffer *ritual_ZN3QV415ExecutionEngine14newArrayBufferEm(
    QV4::ExecutionEngine *self,
    size_t length) {
  return self->newArrayBuffer(length);
}

//  Heap::DateObject *QV4::ExecutionEngine::newDateObject(double dateTime)
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZN3QV415ExecutionEngine13newDateObjectEd(
    QV4::ExecutionEngine *self,
    double dateTime) {
  return self->newDateObject(dateTime);
}

//  Heap::DateObject *QV4::ExecutionEngine::newDateObject(const QDateTime
//      &dateTime)
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZN3QV415ExecutionEngine13newDateObjectERK9QDateTime(
    QV4::ExecutionEngine *self,
    const QDateTime *dateTime) {
  return self->newDateObject(*dateTime);
}

//  Heap::DateObject *QV4::ExecutionEngine::newDateObject(QDate date,
//      Heap::Object *parent, int index, uint flags)
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZN3QV415ExecutionEngine13newDateObjectE5QDatePNS_4Heap6ObjectEij(
    QV4::ExecutionEngine *self,
    const QDate *date,
    QV4::Heap::Object *parent,
    int index,
    uint flags) {
  return self->newDateObject(*date, parent, index, flags);
}

//  Heap::DateObject *QV4::ExecutionEngine::newDateObject(QTime time,
//      Heap::Object *parent, int index, uint flags)
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZN3QV415ExecutionEngine13newDateObjectE5QTimePNS_4Heap6ObjectEij(
    QV4::ExecutionEngine *self,
    const QTime *time,
    QV4::Heap::Object *parent,
    int index,
    uint flags) {
  return self->newDateObject(*time, parent, index, flags);
}

//  Heap::DateObject *QV4::ExecutionEngine::newDateObject(QDateTime dateTime,
//      Heap::Object *parent, int index, uint flags)
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZN3QV415ExecutionEngine13newDateObjectE9QDateTimePNS_4Heap6ObjectEij(
    QV4::ExecutionEngine *self,
    const QDateTime *dateTime,
    QV4::Heap::Object *parent,
    int index,
    uint flags) {
  return self->newDateObject(*dateTime, parent, index, flags);
}

//  Heap::RegExpObject *QV4::ExecutionEngine::newRegExpObject(const QString
//      &pattern, int flags)
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpObject *ritual_ZN3QV415ExecutionEngine15newRegExpObjectERK7QStringi(
    QV4::ExecutionEngine *self,
    const QString *pattern,
    int flags) {
  return self->newRegExpObject(*pattern, flags);
}

#if QT_CONFIG(regularexpression)
//  Heap::RegExpObject *QV4::ExecutionEngine::newRegExpObject(const
//      QRegularExpression &re)
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpObject *ritual_ZN3QV415ExecutionEngine15newRegExpObjectERK18QRegularExpression(
    QV4::ExecutionEngine *self,
    const QRegularExpression *re) {
  return self->newRegExpObject(*re);
}
#endif  // QT_CONFIG(regularexpression)

//  Heap::UrlObject *QV4::ExecutionEngine::newUrlObject()
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZN3QV415ExecutionEngine12newUrlObjectEv(
    QV4::ExecutionEngine *self) {
  return self->newUrlObject();
}

//  Heap::UrlObject *QV4::ExecutionEngine::newUrlObject(const QUrl &url)
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlObject *ritual_ZN3QV415ExecutionEngine12newUrlObjectERK4QUrl(
    QV4::ExecutionEngine *self,
    const QUrl *url) {
  return self->newUrlObject(*url);
}

//  Heap::UrlSearchParamsObject
//      *QV4::ExecutionEngine::newUrlSearchParamsObject()
extern "C" Q_DECL_EXPORT
QV4::Heap::UrlSearchParamsObject *ritual_ZN3QV415ExecutionEngine24newUrlSearchParamsObjectEv(
    QV4::ExecutionEngine *self) {
  return self->newUrlSearchParamsObject();
}

//  Heap::Object *QV4::ExecutionEngine::newErrorObject(const Value &value)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine14newErrorObjectERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *value) {
  return self->newErrorObject(*value);
}

//  Heap::Object *QV4::ExecutionEngine::newErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine14newErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newSyntaxErrorObject(const QString
//      &message, const QString &fileName, int line, int column)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine20newSyntaxErrorObjectERK7QStringS3_ii(
    QV4::ExecutionEngine *self,
    const QString *message,
    const QString *fileName,
    int line,
    int column) {
  return self->newSyntaxErrorObject(*message, *fileName, line, column);
}

//  Heap::Object *QV4::ExecutionEngine::newSyntaxErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine20newSyntaxErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newSyntaxErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newReferenceErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine23newReferenceErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newReferenceErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newReferenceErrorObject(const QString
//      &message, const QString &fileName, int line, int column)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine23newReferenceErrorObjectERK7QStringS3_ii(
    QV4::ExecutionEngine *self,
    const QString *message,
    const QString *fileName,
    int line,
    int column) {
  return self->newReferenceErrorObject(*message, *fileName, line, column);
}

//  Heap::Object *QV4::ExecutionEngine::newTypeErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine18newTypeErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newTypeErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newRangeErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine19newRangeErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newRangeErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newURIErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine17newURIErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newURIErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newURIErrorObject(const Value
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine17newURIErrorObjectERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *message) {
  return self->newURIErrorObject(*message);
}

//  Heap::Object *QV4::ExecutionEngine::newEvalErrorObject(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine18newEvalErrorObjectERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->newEvalErrorObject(*message);
}

//  Heap::PromiseObject *QV4::ExecutionEngine::newPromiseObject()
extern "C" Q_DECL_EXPORT
QV4::Heap::PromiseObject *ritual_ZN3QV415ExecutionEngine16newPromiseObjectEv(
    QV4::ExecutionEngine *self) {
  return self->newPromiseObject();
}

//  Heap::Object *QV4::ExecutionEngine::newPromiseObject(const
//      QV4::FunctionObject *thisObject, const QV4::PromiseCapability
//      *capability)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine16newPromiseObjectEPKNS_14FunctionObjectEPKNS_17PromiseCapabilityE(
    QV4::ExecutionEngine *self,
    const QV4::FunctionObject *thisObject,
    const QV4::PromiseCapability *capability) {
  return self->newPromiseObject(thisObject, capability);
}

//  Promise::ReactionHandler
//      *QV4::ExecutionEngine::getPromiseReactionHandler()
extern "C" Q_DECL_EXPORT
QV4::Promise::ReactionHandler *ritual_ZN3QV415ExecutionEngine25getPromiseReactionHandlerEv(
    QV4::ExecutionEngine *self) {
  return self->getPromiseReactionHandler();
}

//  Heap::Object *QV4::ExecutionEngine::newVariantObject(const QMetaType
//      type, const void *data)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine16newVariantObjectE9QMetaTypePKv(
    QV4::ExecutionEngine *self,
    const QMetaType *type,
    const void *data) {
  return self->newVariantObject(*type, data);
}

//  Heap::Object *QV4::ExecutionEngine::newForInIteratorObject(Object *o)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine22newForInIteratorObjectEPNS_6ObjectE(
    QV4::ExecutionEngine *self,
    QV4::Object *o) {
  return self->newForInIteratorObject(o);
}

//  Heap::Object *QV4::ExecutionEngine::newSetIteratorObject(Object *o)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine20newSetIteratorObjectEPNS_6ObjectE(
    QV4::ExecutionEngine *self,
    QV4::Object *o) {
  return self->newSetIteratorObject(o);
}

//  Heap::Object *QV4::ExecutionEngine::newMapIteratorObject(Object *o)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine20newMapIteratorObjectEPNS_6ObjectE(
    QV4::ExecutionEngine *self,
    QV4::Object *o) {
  return self->newMapIteratorObject(o);
}

//  Heap::Object *QV4::ExecutionEngine::newArrayIteratorObject(Object *o)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV415ExecutionEngine22newArrayIteratorObjectEPNS_6ObjectE(
    QV4::ExecutionEngine *self,
    QV4::Object *o) {
  return self->newArrayIteratorObject(o);
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

//  QObject *QV4::ExecutionEngine::qmlScopeObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV415ExecutionEngine14qmlScopeObjectEv(
    const QV4::ExecutionEngine *self) {
  return self->qmlScopeObject();
}

//  StackTrace QV4::ExecutionEngine::stackTrace(int frameLimit) const
extern "C" Q_DECL_EXPORT
QV4::StackTrace *ritual_ZNK3QV415ExecutionEngine10stackTraceEi(
    const QV4::ExecutionEngine *self,
    int frameLimit) {
  return new QV4::StackTrace(self->stackTrace(frameLimit));
}

//  QUrl QV4::ExecutionEngine::resolvedUrl(const QString &file)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN3QV415ExecutionEngine11resolvedUrlERK7QString(
    QV4::ExecutionEngine *self,
    const QString *file) {
  return new QUrl(self->resolvedUrl(*file));
}

//  void QV4::ExecutionEngine::markObjects(MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine11markObjectsEPNS_9MarkStackE(
    QV4::ExecutionEngine *self,
    QV4::MarkStack *markStack) {
  self->markObjects(markStack);
}

//  void QV4::ExecutionEngine::initRootContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine15initRootContextEv(
    QV4::ExecutionEngine *self) {
  self->initRootContext();
}

//  Heap::InternalClass *QV4::ExecutionEngine::newClass(Heap::InternalClass
//      *other)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV415ExecutionEngine8newClassEPNS_4Heap13InternalClassE(
    QV4::ExecutionEngine *self,
    QV4::Heap::InternalClass *other) {
  return self->newClass(other);
}

//  ReturnedValue QV4::ExecutionEngine::throwError(const Value &value)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine10throwErrorERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *value) {
  return self->throwError(*value);
}

//  ReturnedValue QV4::ExecutionEngine::catchException(StackTrace *trace)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine14catchExceptionEP5QListINS_10StackFrameEE(
    QV4::ExecutionEngine *self,
    QV4::StackTrace *trace) {
  return self->catchException(trace);
}

//  ReturnedValue QV4::ExecutionEngine::throwError(const QString &message)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine10throwErrorERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->throwError(*message);
}

//  ReturnedValue QV4::ExecutionEngine::throwSyntaxError(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine16throwSyntaxErrorERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->throwSyntaxError(*message);
}

//  ReturnedValue QV4::ExecutionEngine::throwSyntaxError(const QString
//      &message, const QString &fileName, int lineNumber, int column)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine16throwSyntaxErrorERK7QStringS3_ii(
    QV4::ExecutionEngine *self,
    const QString *message,
    const QString *fileName,
    int lineNumber,
    int column) {
  return self->throwSyntaxError(*message, *fileName, lineNumber, column);
}

//  ReturnedValue QV4::ExecutionEngine::throwTypeError()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine14throwTypeErrorEv(
    QV4::ExecutionEngine *self) {
  return self->throwTypeError();
}

//  ReturnedValue QV4::ExecutionEngine::throwTypeError(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine14throwTypeErrorERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->throwTypeError(*message);
}

//  ReturnedValue QV4::ExecutionEngine::throwReferenceError(const Value
//      &value)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine19throwReferenceErrorERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *value) {
  return self->throwReferenceError(*value);
}

//  ReturnedValue QV4::ExecutionEngine::throwReferenceError(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine19throwReferenceErrorERK7QString(
    QV4::ExecutionEngine *self,
    const QString *name) {
  return self->throwReferenceError(*name);
}

//  ReturnedValue QV4::ExecutionEngine::throwReferenceError(const QString
//      &value, const QString &fileName, int lineNumber, int column)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine19throwReferenceErrorERK7QStringS3_ii(
    QV4::ExecutionEngine *self,
    const QString *value,
    const QString *fileName,
    int lineNumber,
    int column) {
  return self->throwReferenceError(*value, *fileName, lineNumber, column);
}

//  ReturnedValue QV4::ExecutionEngine::throwRangeError(const Value &value)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine15throwRangeErrorERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *value) {
  return self->throwRangeError(*value);
}

//  ReturnedValue QV4::ExecutionEngine::throwRangeError(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine15throwRangeErrorERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->throwRangeError(*message);
}

//  ReturnedValue QV4::ExecutionEngine::throwURIError(const Value &msg)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine13throwURIErrorERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *msg) {
  return self->throwURIError(*msg);
}

//  ReturnedValue QV4::ExecutionEngine::throwUnimplemented(const QString
//      &message)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine18throwUnimplementedERK7QString(
    QV4::ExecutionEngine *self,
    const QString *message) {
  return self->throwUnimplemented(*message);
}

//  QQmlError QV4::ExecutionEngine::catchExceptionAsQmlError()
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN3QV415ExecutionEngine24catchExceptionAsQmlErrorEv(
    QV4::ExecutionEngine *self) {
  return new QQmlError(self->catchExceptionAsQmlError());
}

//  void QV4::ExecutionEngine::amendException()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine14amendExceptionEv(
    QV4::ExecutionEngine *self) {
  self->amendException();
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

//  bool QV4::ExecutionEngine::metaTypeFromJS(const Value &value, QMetaType
//      type, void *data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415ExecutionEngine14metaTypeFromJSERKNS_5ValueE9QMetaTypePv(
    const QV4::Value *value,
    const QMetaType *type,
    void *data) {
  return QV4::ExecutionEngine::metaTypeFromJS(*value, *type, data);
}

//  QV4::ReturnedValue QV4::ExecutionEngine::metaTypeToJS(QMetaType type,
//      const void *data)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine12metaTypeToJSE9QMetaTypePKv(
    QV4::ExecutionEngine *self,
    const QMetaType *type,
    const void *data) {
  return self->metaTypeToJS(*type, data);
}

//  int QV4::ExecutionEngine::maxJSStackSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV415ExecutionEngine14maxJSStackSizeEv(
    const QV4::ExecutionEngine *self) {
  return self->maxJSStackSize();
}

//  int QV4::ExecutionEngine::maxGCStackSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV415ExecutionEngine14maxGCStackSizeEv(
    const QV4::ExecutionEngine *self) {
  return self->maxGCStackSize();
}

//  int QV4::ExecutionEngine::safeForAllocLength(qint64 len64)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV415ExecutionEngine18safeForAllocLengthEx(
    QV4::ExecutionEngine *self,
    qint64 len64) {
  return self->safeForAllocLength(len64);
}

//  QV4::ReturnedValue QV4::ExecutionEngine::global()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine6globalEv(
    QV4::ExecutionEngine *self) {
  return self->global();
}

//  void QV4::ExecutionEngine::initQmlGlobalObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine19initQmlGlobalObjectEv(
    QV4::ExecutionEngine *self) {
  self->initQmlGlobalObject();
}

//  void QV4::ExecutionEngine::initializeGlobal()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine16initializeGlobalEv(
    QV4::ExecutionEngine *self) {
  self->initializeGlobal();
}

//  void QV4::ExecutionEngine::createQtObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine14createQtObjectEv(
    QV4::ExecutionEngine *self) {
  self->createQtObject();
}

//  void QV4::ExecutionEngine::freezeObject(const QV4::Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine12freezeObjectERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *value) {
  self->freezeObject(*value);
}

//  void QV4::ExecutionEngine::lockObject(const QV4::Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine10lockObjectERKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QV4::Value *value) {
  self->lockObject(*value);
}

#if QT_CONFIG(qml_xml_http_request)
//  void QV4::ExecutionEngine::setupXmlHttpRequestExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine28setupXmlHttpRequestExtensionEv(
    QV4::ExecutionEngine *self) {
  self->setupXmlHttpRequestExtension();
}
#endif  // QT_CONFIG(qml_xml_http_request)

#if QT_CONFIG(qml_xml_http_request)
//  void *QV4::ExecutionEngine::xmlHttpRequestData() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK3QV415ExecutionEngine18xmlHttpRequestDataEv(
    const QV4::ExecutionEngine *self) {
  return self->xmlHttpRequestData();
}
#endif  // QT_CONFIG(qml_xml_http_request)

//  void QV4::ExecutionEngine::setQmlEngine(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine12setQmlEngineEP10QQmlEngine(
    QV4::ExecutionEngine *self,
    QQmlEngine *engine) {
  self->setQmlEngine(engine);
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

//  void QV4::ExecutionEngine::startTimer(const QString &timerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine10startTimerERK7QString(
    QV4::ExecutionEngine *self,
    const QString *timerName) {
  self->startTimer(*timerName);
}

//  qint64 QV4::ExecutionEngine::stopTimer(const QString &timerName, bool
//      *wasRunning)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN3QV415ExecutionEngine9stopTimerERK7QStringPb(
    QV4::ExecutionEngine *self,
    const QString *timerName,
    bool *wasRunning) {
  return self->stopTimer(*timerName, wasRunning);
}

//  int QV4::ExecutionEngine::consoleCountHelper(const QString &file, quint16
//      line, quint16 column)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV415ExecutionEngine18consoleCountHelperERK7QStringtt(
    QV4::ExecutionEngine *self,
    const QString *file,
    quint16 line,
    quint16 column) {
  return self->consoleCountHelper(*file, line, column);
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

//  void QV4::ExecutionEngine::setExtensionData(int a0, Deletable *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine16setExtensionDataEiPNS0_9DeletableE(
    QV4::ExecutionEngine *self,
    int a0,
    QV4::ExecutionEngine::Deletable *a1) {
  self->setExtensionData(a0, a1);
}

//  Deletable *QV4::ExecutionEngine::extensionData(int index) const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine::Deletable *ritual_ZNK3QV415ExecutionEngine13extensionDataEi(
    const QV4::ExecutionEngine *self,
    int index) {
  return self->extensionData(index);
}

//  QQmlRefPointer<ExecutableCompilationUnit>
//      QV4::ExecutionEngine::compilationUnitForUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZNK3QV415ExecutionEngine21compilationUnitForUrlERK4QUrl(
    const QV4::ExecutionEngine *self,
    const QUrl *url) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      self->compilationUnitForUrl(
          *url));
}

//  QQmlRefPointer<ExecutableCompilationUnit> QV4::ExecutionEngine::executabl
//      eCompilationUnit(QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      &&unit)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZN3QV415ExecutionEngine25executableCompilationUnitEO14QQmlRefPointerINS_12CompiledData15CompilationUnitEE(
    QV4::ExecutionEngine *self,
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *unit) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      self->executableCompilationUnit(
          std::move(*unit)));
}

//  QQmlRefPointer<ExecutableCompilationUnit> QV4::ExecutionEngine::insertCom
//      pilationUnit(QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      &&unit)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZN3QV415ExecutionEngine21insertCompilationUnitEO14QQmlRefPointerINS_12CompiledData15CompilationUnitEE(
    QV4::ExecutionEngine *self,
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *unit) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      self->insertCompilationUnit(
          std::move(*unit)));
}

//  QMultiHash<QUrl, QQmlRefPointer<ExecutableCompilationUnit>>
//      QV4::ExecutionEngine::compilationUnits() const
extern "C" Q_DECL_EXPORT
QMultiHash<QUrl, QQmlRefPointer<QV4::ExecutableCompilationUnit>> *ritual_ZNK3QV415ExecutionEngine16compilationUnitsEv(
    const QV4::ExecutionEngine *self) {
  return new QMultiHash<QUrl, QQmlRefPointer<QV4::ExecutableCompilationUnit>>(
      self->compilationUnits());
}

//  void QV4::ExecutionEngine::trimCompilationUnits()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine20trimCompilationUnitsEv(
    QV4::ExecutionEngine *self) {
  self->trimCompilationUnits();
}

//  void QV4::ExecutionEngine::trimCompilationUnitsForUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine26trimCompilationUnitsForUrlERK4QUrl(
    QV4::ExecutionEngine *self,
    const QUrl *url) {
  self->trimCompilationUnitsForUrl(*url);
}

//  Module QV4::ExecutionEngine::registerNativeModule(const QUrl &url, const
//      QV4::Value &value)
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine::Module *ritual_ZN3QV415ExecutionEngine20registerNativeModuleERK4QUrlRKNS_5ValueE(
    QV4::ExecutionEngine *self,
    const QUrl *url,
    const QV4::Value *value) {
  return new QV4::ExecutionEngine::Module(
      self->registerNativeModule(
          *url,
          *value));
}

//  Module QV4::ExecutionEngine::moduleForUrl(const QUrl &_url, const
//      ExecutableCompilationUnit *referrer)
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine::Module *ritual_ZN3QV415ExecutionEngine12moduleForUrlERK4QUrlPKNS_25ExecutableCompilationUnitE(
    QV4::ExecutionEngine *self,
    const QUrl *_url,
    const QV4::ExecutableCompilationUnit *referrer) {
  return new QV4::ExecutionEngine::Module(
      self->moduleForUrl(
          *_url,
          referrer));
}

//  DiskCacheOptions QV4::ExecutionEngine::diskCacheOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV415ExecutionEngine16diskCacheOptionsEv(
    const QV4::ExecutionEngine *self) {
  return static_cast<int>(self->diskCacheOptions().toInt());
}

//  void QV4::ExecutionEngine::callInContext(QV4::Function *function, QObject
//      *self_, QV4::ExecutionContext *ctxt, int argc, void **args, QMetaType
//      *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine13callInContextEPNS_8FunctionEP7QObjectPNS_16ExecutionContextEiPPvP9QMetaType(
    QV4::ExecutionEngine *self,
    QV4::Function *function,
    QObject *self_,
    QV4::ExecutionContext *ctxt,
    int argc,
    void **args,
    QMetaType *types) {
  self->callInContext(function, self_, ctxt, argc, args, types);
}

//  QV4::ReturnedValue QV4::ExecutionEngine::callInContext(QV4::Function
//      *function, QObject *self_, QV4::ExecutionContext *ctxt, int argc,
//      const QV4::Value *argv)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine13callInContextEPNS_8FunctionEP7QObjectPNS_16ExecutionContextEiPKNS_5ValueE(
    QV4::ExecutionEngine *self,
    QV4::Function *function,
    QObject *self_,
    QV4::ExecutionContext *ctxt,
    int argc,
    const QV4::Value *argv) {
  return self->callInContext(function, self_, ctxt, argc, argv);
}

//  QV4::ReturnedValue QV4::ExecutionEngine::fromData(QMetaType type, const
//      void *ptr, Heap::Object *parent, int property, uint flags)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ExecutionEngine8fromDataE9QMetaTypePKvPNS_4Heap6ObjectEij(
    QV4::ExecutionEngine *self,
    const QMetaType *type,
    const void *ptr,
    QV4::Heap::Object *parent,
    int property,
    uint flags) {
  return self->fromData(*type, ptr, parent, property, flags);
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

//  void QV4::ExecutionEngine::initializeStaticMembers()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ExecutionEngine23initializeStaticMembersEv() {
  QV4::ExecutionEngine::initializeStaticMembers();
}

//  bool QV4::ExecutionEngine::inStack(const void *current) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415ExecutionEngine7inStackEPKv(
    const QV4::ExecutionEngine *self,
    const void *current) {
  return self->inStack(current);
}

//  bool QV4::ExecutionEngine::hasJsStackOverflow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415ExecutionEngine18hasJsStackOverflowEv(
    const QV4::ExecutionEngine *self) {
  return self->hasJsStackOverflow();
}

//  a QV4::StackTrace a ritual of QV4::ExecutionEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ExecutionEngine__QV4_StackTrace(QV4::StackTrace *self) {
  delete self;
}

//  a QQmlRefPointer<QV4::ExecutableCompilationUnit> a ritual of
//      QV4::ExecutionEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ExecutionEngine__QQmlRefPointer_QV4_ExecutableCompilationUnit(
    QQmlRefPointer<QV4::ExecutableCompilationUnit> *self) {
  delete self;
}

//  a QMultiHash<QUrl, QQmlRefPointer<QV4::ExecutableCompilationUnit>> a
//      ritual of QV4::ExecutionEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ExecutionEngine__QMultiHash_QUrl_QQmlRefPointer_QV4_ExecutableCompilationUnit(
    QMultiHash<QUrl, QQmlRefPointer<QV4::ExecutableCompilationUnit>> *self) {
  delete self;
}

//  a QV4::ExecutionEngine::Module a ritual of QV4::ExecutionEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ExecutionEngine__QV4_ExecutionEngine_Module(
    QV4::ExecutionEngine::Module *self) {
  delete self;
}

#include <QtQml/6.12.0/QtQml/private/qv4function_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4stackframe_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>

//  bool QV4::ExecutionEngine::canJIT<QV4::Function>(Function *jittable)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415ExecutionEngine6canJITINS_8FunctionEEEbPT_(
    const QV4::ExecutionEngine *self, QV4::Function *jittable) {
  return self->canJIT<QV4::Function>(jittable);
}

//  static QJSPrimitiveValue QV4::ExecutionEngine::createPrimitive<const
//      QV4::Value *>(const const QV4::Value * &v)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN3QV415ExecutionEngine15createPrimitiveIPKNS_5ValueEEE17QJSPrimitiveValueRKT_(
    const QV4::Value *v) {
  return new QJSPrimitiveValue(
      QV4::ExecutionEngine::createPrimitive<const QV4::Value *>(v));
}

//  static QJSPrimitiveValue QV4::ExecutionEngine::createPrimitive<QV4::Value
//      *>(const QV4::Value * &v)
extern "C" Q_DECL_EXPORT
QJSPrimitiveValue *ritual_ZN3QV415ExecutionEngine15createPrimitiveIPNS_5ValueEEE17QJSPrimitiveValueRKT_(
    QV4::Value *v) {
  return new QJSPrimitiveValue(
      QV4::ExecutionEngine::createPrimitive<QV4::Value *>(v));
}

//  QV4::ExecutionContext *QV4::ExecutionEngine::currentContext<
//      QV4::CppStackFrame>() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV415ExecutionEngine14currentContextINS_13CppStackFrameEEEPNS_16ExecutionContextEv(
    const QV4::ExecutionEngine *self) {
  return self->currentContext<QV4::CppStackFrame>();
}

//  QV4::ExecutionContext *QV4::ExecutionEngine::currentContext<
//      QV4::JSTypesStackFrame>() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV415ExecutionEngine14currentContextINS_17JSTypesStackFrameEEEPNS_16ExecutionContextEv(
    const QV4::ExecutionEngine *self) {
  return self->currentContext<QV4::JSTypesStackFrame>();
}

//  QV4::ExecutionContext *QV4::ExecutionEngine::currentContext<
//      QV4::MetaTypesStackFrame>() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionContext *ritual_ZNK3QV415ExecutionEngine14currentContextINS_19MetaTypesStackFrameEEEPNS_16ExecutionContextEv(
    const QV4::ExecutionEngine *self) {
  return self->currentContext<QV4::MetaTypesStackFrame>();
}

//  QQmlTypeLoader *QV4::ExecutionEngine::typeLoader<QQmlTypeLoader>()
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZN3QV415ExecutionEngine10typeLoaderI14QQmlTypeLoaderEEPT_v(
    QV4::ExecutionEngine *self) {
  return self->typeLoader<QQmlTypeLoader>();
}
