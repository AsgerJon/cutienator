//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qarraydata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qarraydata.h>
#include <utility>
#include <QtCore/QArrayData>

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

//  void *QArrayData::allocate(QArrayData **pdata, qsizetype objectSize,
//      qsizetype alignment, qsizetype capacity, AllocationOption option)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QArrayData8allocateEPPS_xxxNS_16AllocationOptionE(
    QArrayData **pdata,
    qsizetype objectSize,
    qsizetype alignment,
    qsizetype capacity,
    QArrayData::AllocationOption option) {
  return QArrayData::allocate(
      pdata,
      objectSize,
      alignment,
      capacity,
      option);
}

//  void *QArrayData::allocate1(QArrayData **pdata, qsizetype capacity,
//      AllocationOption option)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QArrayData9allocate1EPPS_xNS_16AllocationOptionE(
    QArrayData **pdata,
    qsizetype capacity,
    QArrayData::AllocationOption option) {
  return QArrayData::allocate1(pdata, capacity, option);
}

//  void *QArrayData::allocate2(QArrayData **pdata, qsizetype capacity,
//      AllocationOption option)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QArrayData9allocate2EPPS_xNS_16AllocationOptionE(
    QArrayData **pdata,
    qsizetype capacity,
    QArrayData::AllocationOption option) {
  return QArrayData::allocate2(pdata, capacity, option);
}

//  std::pair<QArrayData *, void *>
//      QArrayData::reallocateUnaligned(QArrayData *data, void *dataPointer,
//      qsizetype objectSize, qsizetype newCapacity, AllocationOption option)
extern "C" Q_DECL_EXPORT
std::pair<QArrayData *, void *> *ritual_ZN10QArrayData19reallocateUnalignedEPS_PvxxNS_16AllocationOptionE(
    QArrayData *data,
    void *dataPointer,
    qsizetype objectSize,
    qsizetype newCapacity,
    QArrayData::AllocationOption option) {
  return new std::pair<QArrayData *, void *>(
      QArrayData::reallocateUnaligned(
          data,
          dataPointer,
          objectSize,
          newCapacity,
          option));
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

//  a std::pair<QArrayData *, void *> a ritual of QArrayData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QArrayData__std_pair_QArrayData_void(
    std::pair<QArrayData *, void *> *self) {
  delete self;
}
