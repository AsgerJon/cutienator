//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectorgadget_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <utility>
#include <QtCore/QObject>

//  const QV4::VTable *QV4::QObjectMethod::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV413QObjectMethod12staticVTableEv() {
  return QV4::QObjectMethod::staticVTable();
}

//  void QV4::QObjectMethod::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413QObjectMethod10__dataTestEv(QV4::QObjectMethod *self) {
  self->__dataTest();
}

//  QV4::Heap::QObjectMethod *QV4::QObjectMethod::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectMethod *ritual_ZNK3QV413QObjectMethod11d_uncheckedEv(
    const QV4::QObjectMethod *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QObjectMethod *QV4::QObjectMethod::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectMethod *ritual_ZNK3QV413QObjectMethod1dEv(
    const QV4::QObjectMethod *self) {
  return self->d();
}

//  void QV4::QObjectMethod::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413QObjectMethod14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QObjectMethod::virtualDestroy(b);
}

//  ReturnedValue QV4::QObjectMethod::create(ExecutionEngine *engine,
//      Heap::Object *wrapper, int index)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV413QObjectMethod6createEPNS_15ExecutionEngineEPNS_4Heap6ObjectEi(
    QV4::ExecutionEngine *engine,
    QV4::Heap::Object *wrapper,
    int index) {
  return QV4::QObjectMethod::create(engine, wrapper, index);
}

//  ReturnedValue QV4::QObjectMethod::create(ExecutionEngine *engine,
//      Heap::QQmlValueTypeWrapper *valueType, int index)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV413QObjectMethod6createEPNS_15ExecutionEngineEPNS_4Heap20QQmlValueTypeWrapperEi(
    QV4::ExecutionEngine *engine,
    QV4::Heap::QQmlValueTypeWrapper *valueType,
    int index) {
  return QV4::QObjectMethod::create(engine, valueType, index);
}

//  ReturnedValue QV4::QObjectMethod::create(ExecutionEngine *engine,
//      Heap::QObjectMethod *cloneFrom, Heap::Object *wrapper, Heap::Object
//      *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV413QObjectMethod6createEPNS_15ExecutionEngineEPNS_4Heap13QObjectMethodEPNS3_6ObjectES7_(
    QV4::ExecutionEngine *engine,
    QV4::Heap::QObjectMethod *cloneFrom,
    QV4::Heap::Object *wrapper,
    QV4::Heap::Object *object) {
  return QV4::QObjectMethod::create(engine, cloneFrom, wrapper, object);
}

//  int QV4::QObjectMethod::methodIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV413QObjectMethod11methodIndexEv(
    const QV4::QObjectMethod *self) {
  return self->methodIndex();
}

//  QObject *QV4::QObjectMethod::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV413QObjectMethod6objectEv(
    const QV4::QObjectMethod *self) {
  return self->object();
}

//  QV4::ReturnedValue
//      QV4::QObjectMethod::method_toString(QV4::ExecutionEngine *engine,
//      QObject *o) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV413QObjectMethod15method_toStringEPNS_15ExecutionEngineEP7QObject(
    const QV4::QObjectMethod *self,
    QV4::ExecutionEngine *engine,
    QObject *o) {
  return self->method_toString(engine, o);
}

//  QV4::ReturnedValue
//      QV4::QObjectMethod::method_destroy(QV4::ExecutionEngine *ctx, QObject
//      *o, const Value *args, int argc) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV413QObjectMethod14method_destroyEPNS_15ExecutionEngineEP7QObjectPKNS_5ValueEi(
    const QV4::QObjectMethod *self,
    QV4::ExecutionEngine *ctx,
    QObject *o,
    const QV4::Value *args,
    int argc) {
  return self->method_destroy(ctx, o, args, argc);
}

//  bool QV4::QObjectMethod::method_destroy(QV4::ExecutionEngine *engine,
//      QObject *o, int delay) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV413QObjectMethod14method_destroyEPNS_15ExecutionEngineEP7QObjecti(
    const QV4::QObjectMethod *self,
    QV4::ExecutionEngine *engine,
    QObject *o,
    int delay) {
  return self->method_destroy(engine, o, delay);
}

//  ReturnedValue QV4::QObjectMethod::virtualCall(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV413QObjectMethod11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::QObjectMethod::virtualCall(a0, thisObject, argv, argc);
}

//  void QV4::QObjectMethod::virtualCallWithMetaTypes(const FunctionObject
//      *m, QObject *thisObject, void **argv, const QMetaType *types, int
//      argc)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413QObjectMethod24virtualCallWithMetaTypesEPKNS_14FunctionObjectEP7QObjectPPvPK9QMetaTypei(
    const QV4::FunctionObject *m,
    QObject *thisObject,
    void **argv,
    const QMetaType *types,
    int argc) {
  QV4::QObjectMethod::virtualCallWithMetaTypes(
      m,
      thisObject,
      argv,
      types,
      argc);
}

//  ReturnedValue QV4::QObjectMethod::callInternal(const Value *thisObject,
//      const Value *argv, int argc) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV413QObjectMethod12callInternalEPKNS_5ValueES3_i(
    const QV4::QObjectMethod *self,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return self->callInternal(thisObject, argv, argc);
}

//  void QV4::QObjectMethod::callInternalWithMetaTypes(QObject *thisObject,
//      void **argv, const QMetaType *types, int argc) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV413QObjectMethod25callInternalWithMetaTypesEP7QObjectPPvPK9QMetaTypei(
    const QV4::QObjectMethod *self,
    QObject *thisObject,
    void **argv,
    const QMetaType *types,
    int argc) {
  self->callInternalWithMetaTypes(thisObject, argv, types, argc);
}

//  std::pair<QObject *, int> QV4::QObjectMethod::extractQtMethod(const
//      QV4::FunctionObject *function)
extern "C" Q_DECL_EXPORT
std::pair<QObject *, int> *ritual_ZN3QV413QObjectMethod15extractQtMethodEPKNS_14FunctionObjectE(
    const QV4::FunctionObject *function) {
  return new std::pair<QObject *, int>(
      QV4::QObjectMethod::extractQtMethod(
          function));
}

//  bool QV4::QObjectMethod::isExactMatch(const QMetaMethod &method, void
//      **argv, int argc, const QMetaType *types)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV413QObjectMethod12isExactMatchERK11QMetaMethodPPviPK9QMetaType(
    const QMetaMethod *method,
    void **argv,
    int argc,
    const QMetaType *types) {
  return QV4::QObjectMethod::isExactMatch(*method, argv, argc, types);
}

//  const QQmlPropertyData *QV4::QObjectMethod::resolveOverloaded(const
//      QQmlObjectOrGadget &object, const QQmlPropertyData *methods, int
//      methodCount, ExecutionEngine *engine, CallData *callArgs)
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZN3QV413QObjectMethod17resolveOverloadedERK18QQmlObjectOrGadgetPK16QQmlPropertyDataiPNS_15ExecutionEngineEPNS_8CallDataE(
    const QQmlObjectOrGadget *object,
    const QQmlPropertyData *methods,
    int methodCount,
    QV4::ExecutionEngine *engine,
    QV4::CallData *callArgs) {
  return QV4::QObjectMethod::resolveOverloaded(
      *object,
      methods,
      methodCount,
      engine,
      callArgs);
}

//  const QQmlPropertyData *QV4::QObjectMethod::resolveOverloaded(const
//      QQmlPropertyData *methods, int methodCount, void **argv, int argc,
//      const QMetaType *types)
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZN3QV413QObjectMethod17resolveOverloadedEPK16QQmlPropertyDataiPPviPK9QMetaType(
    const QQmlPropertyData *methods,
    int methodCount,
    void **argv,
    int argc,
    const QMetaType *types) {
  return QV4::QObjectMethod::resolveOverloaded(
      methods,
      methodCount,
      argv,
      argc,
      types);
}

//  ReturnedValue QV4::QObjectMethod::callPrecise(const QQmlObjectOrGadget
//      &object, const QQmlPropertyData &data, ExecutionEngine *engine,
//      CallData *callArgs, QMetaObject::Call callType)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV413QObjectMethod11callPreciseERK18QQmlObjectOrGadgetRK16QQmlPropertyDataPNS_15ExecutionEngineEPNS_8CallDataEN11QMetaObject4CallE(
    const QQmlObjectOrGadget *object,
    const QQmlPropertyData *data,
    QV4::ExecutionEngine *engine,
    QV4::CallData *callArgs,
    QMetaObject::Call callType) {
  return QV4::QObjectMethod::callPrecise(
      *object,
      *data,
      engine,
      callArgs,
      callType);
}

//  a std::pair<QObject *, int> a ritual of QV4::QObjectMethod gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_QObjectMethod__std_pair_QObject_int(
    std::pair<QObject *, int> *self) {
  delete self;
}
