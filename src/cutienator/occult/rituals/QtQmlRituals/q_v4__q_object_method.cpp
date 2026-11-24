//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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
