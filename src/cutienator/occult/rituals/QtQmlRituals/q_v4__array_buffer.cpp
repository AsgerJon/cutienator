//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::ArrayBuffer::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV411ArrayBuffer12staticVTableEv() {
  return QV4::ArrayBuffer::staticVTable();
}

//  void QV4::ArrayBuffer::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ArrayBuffer10__dataTestEv(QV4::ArrayBuffer *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayBuffer *QV4::ArrayBuffer::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayBuffer *ritual_ZNK3QV411ArrayBuffer11d_uncheckedEv(
    const QV4::ArrayBuffer *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayBuffer *QV4::ArrayBuffer::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayBuffer *ritual_ZNK3QV411ArrayBuffer1dEv(
    const QV4::ArrayBuffer *self) {
  return self->d();
}

//  void QV4::ArrayBuffer::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ArrayBuffer14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ArrayBuffer::virtualDestroy(b);
}

//  QV4::Object *QV4::ArrayBuffer::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV411ArrayBuffer16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ArrayBuffer::defaultPrototype(e);
}

//  uint QV4::ArrayBuffer::arrayDataLength() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV411ArrayBuffer15arrayDataLengthEv(
    const QV4::ArrayBuffer *self) {
  return self->arrayDataLength();
}

//  const char *QV4::ArrayBuffer::constArrayData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK3QV411ArrayBuffer14constArrayDataEv(
    const QV4::ArrayBuffer *self) {
  return self->constArrayData();
}

//  bool QV4::ArrayBuffer::hasSharedArrayData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ArrayBuffer18hasSharedArrayDataEv(
    QV4::ArrayBuffer *self) {
  return self->hasSharedArrayData();
}

//  void QV4::ArrayBuffer::detachArrayData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ArrayBuffer15detachArrayDataEv(QV4::ArrayBuffer *self) {
  self->detachArrayData();
}
