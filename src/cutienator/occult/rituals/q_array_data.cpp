//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qarraydata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qarraydata.h>

//  qsizetype QArrayData::allocatedCapacity()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN10QArrayData17allocatedCapacityEv(QArrayData *self) {
  return self->allocatedCapacity();
}

//  qsizetype QArrayData::constAllocatedCapacity() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QArrayData22constAllocatedCapacityEv(
    const QArrayData *self) {
  return self->constAllocatedCapacity();
}

//  bool QArrayData::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QArrayData3refEv(QArrayData *self) {
  return self->ref();
}

//  bool QArrayData::deref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QArrayData5derefEv(QArrayData *self) {
  return self->deref();
}

//  bool QArrayData::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QArrayData8isSharedEv(const QArrayData *self) {
  return self->isShared();
}

//  bool QArrayData::needsDetach()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QArrayData11needsDetachEv(QArrayData *self) {
  return self->needsDetach();
}

//  qsizetype QArrayData::detachCapacity(qsizetype newSize) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QArrayData14detachCapacityEx(
    const QArrayData *self,
    qsizetype newSize) {
  return self->detachCapacity(newSize);
}

//  void QArrayData::deallocate(QArrayData *data, qsizetype objectSize,
//      qsizetype alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QArrayData10deallocateEPS_xx(
    QArrayData *data,
    qsizetype objectSize,
    qsizetype alignment) {
  QArrayData::deallocate(data, objectSize, alignment);
}
