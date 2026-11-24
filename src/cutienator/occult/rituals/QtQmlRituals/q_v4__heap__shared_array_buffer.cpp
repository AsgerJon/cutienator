//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::SharedArrayBuffer::setSharedArrayBuffer(bool shared)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap17SharedArrayBuffer20setSharedArrayBufferEb(
    QV4::Heap::SharedArrayBuffer *self,
    bool shared) {
  self->setSharedArrayBuffer(shared);
}

//  bool QV4::Heap::SharedArrayBuffer::isSharedArrayBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap17SharedArrayBuffer19isSharedArrayBufferEv(
    const QV4::Heap::SharedArrayBuffer *self) {
  return self->isSharedArrayBuffer();
}

//  const char *QV4::Heap::SharedArrayBuffer::constArrayData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK3QV44Heap17SharedArrayBuffer14constArrayDataEv(
    const QV4::Heap::SharedArrayBuffer *self) {
  return self->constArrayData();
}

//  uint QV4::Heap::SharedArrayBuffer::arrayDataLength() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV44Heap17SharedArrayBuffer15arrayDataLengthEv(
    const QV4::Heap::SharedArrayBuffer *self) {
  return self->arrayDataLength();
}

//  bool QV4::Heap::SharedArrayBuffer::hasSharedArrayData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap17SharedArrayBuffer18hasSharedArrayDataEv(
    const QV4::Heap::SharedArrayBuffer *self) {
  return self->hasSharedArrayData();
}

//  bool QV4::Heap::SharedArrayBuffer::hasDetachedArrayData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap17SharedArrayBuffer20hasDetachedArrayDataEv(
    const QV4::Heap::SharedArrayBuffer *self) {
  return self->hasDetachedArrayData();
}

//  void QV4::Heap::SharedArrayBuffer::detachArrayData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap17SharedArrayBuffer15detachArrayDataEv(
    QV4::Heap::SharedArrayBuffer *self) {
  self->detachArrayData();
}

//  bool QV4::Heap::SharedArrayBuffer::arrayDataNeedsDetach() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap17SharedArrayBuffer20arrayDataNeedsDetachEv(
    const QV4::Heap::SharedArrayBuffer *self) {
  return self->arrayDataNeedsDetach();
}
