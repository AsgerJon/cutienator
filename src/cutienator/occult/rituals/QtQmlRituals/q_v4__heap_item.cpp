//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Heap::Base *QV4::HeapItem::operator QV4::Heap::Base *()
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZN3QV48HeapItemcvPNS_4Heap4BaseEEv(
    QV4::HeapItem *self) {
  return self->operator QV4::Heap::Base *();
}

//  Chunk *QV4::HeapItem::chunk() const
extern "C" Q_DECL_EXPORT
QV4::Chunk *ritual_ZNK3QV48HeapItem5chunkEv(const QV4::HeapItem *self) {
  return self->chunk();
}

//  bool QV4::HeapItem::isBlack() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48HeapItem7isBlackEv(const QV4::HeapItem *self) {
  return self->isBlack();
}

//  bool QV4::HeapItem::isInUse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48HeapItem7isInUseEv(const QV4::HeapItem *self) {
  return self->isInUse();
}

//  void QV4::HeapItem::setAllocatedSlots(size_t nSlots)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48HeapItem17setAllocatedSlotsEm(
    QV4::HeapItem *self,
    size_t nSlots) {
  self->setAllocatedSlots(nSlots);
}

//  QV4::HeapItem::~HeapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48HeapItemD1Ev(QV4::HeapItem *self) {
  delete self;
}
