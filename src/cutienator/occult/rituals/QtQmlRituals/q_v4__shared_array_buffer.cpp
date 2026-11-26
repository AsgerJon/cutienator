//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::SharedArrayBuffer::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV417SharedArrayBuffer12staticVTableEv() {
  return QV4::SharedArrayBuffer::staticVTable();
}

//  void QV4::SharedArrayBuffer::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417SharedArrayBuffer10__dataTestEv(
    QV4::SharedArrayBuffer *self) {
  self->__dataTest();
}

//  QV4::Heap::SharedArrayBuffer *QV4::SharedArrayBuffer::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SharedArrayBuffer *ritual_ZNK3QV417SharedArrayBuffer11d_uncheckedEv(
    const QV4::SharedArrayBuffer *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SharedArrayBuffer *QV4::SharedArrayBuffer::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SharedArrayBuffer *ritual_ZNK3QV417SharedArrayBuffer1dEv(
    const QV4::SharedArrayBuffer *self) {
  return self->d();
}

//  void QV4::SharedArrayBuffer::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417SharedArrayBuffer14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::SharedArrayBuffer::virtualDestroy(b);
}

//  QV4::Object
//      *QV4::SharedArrayBuffer::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV417SharedArrayBuffer16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::SharedArrayBuffer::defaultPrototype(e);
}

//  uint QV4::SharedArrayBuffer::arrayDataLength() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV417SharedArrayBuffer15arrayDataLengthEv(
    const QV4::SharedArrayBuffer *self) {
  return self->arrayDataLength();
}

//  char *QV4::SharedArrayBuffer::arrayData()
extern "C" Q_DECL_EXPORT
char *ritual_ZN3QV417SharedArrayBuffer9arrayDataEv(
    QV4::SharedArrayBuffer *self) {
  return self->arrayData();
}

//  const char *QV4::SharedArrayBuffer::constArrayData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK3QV417SharedArrayBuffer14constArrayDataEv(
    const QV4::SharedArrayBuffer *self) {
  return self->constArrayData();
}

//  bool QV4::SharedArrayBuffer::hasSharedArrayData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV417SharedArrayBuffer18hasSharedArrayDataEv(
    QV4::SharedArrayBuffer *self) {
  return self->hasSharedArrayData();
}

//  bool QV4::SharedArrayBuffer::hasDetachedArrayData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417SharedArrayBuffer20hasDetachedArrayDataEv(
    const QV4::SharedArrayBuffer *self) {
  return self->hasDetachedArrayData();
}

//  bool QV4::SharedArrayBuffer::isSharedArrayBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417SharedArrayBuffer19isSharedArrayBufferEv(
    const QV4::SharedArrayBuffer *self) {
  return self->isSharedArrayBuffer();
}
