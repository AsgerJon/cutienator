//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 4. Kept
//  as it is when the generator runs again.
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

//  size_t QV4::HeapItem::size() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV48HeapItem4sizeEv(const QV4::HeapItem *self) {
  return self->size();
}

//  QV4::HeapItem::~HeapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48HeapItemD1Ev(QV4::HeapItem *self) {
  delete self;
}

#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>

//  QV4::Heap::Object *QV4::HeapItem::as<QV4::Heap::Object>()
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV48HeapItem2asINS_4Heap6ObjectEEEPT_v(
    QV4::HeapItem *self) {
  return self->as<QV4::Heap::Object>();
}

//  QV4::Heap::String *QV4::HeapItem::as<QV4::Heap::String>()
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZN3QV48HeapItem2asINS_4Heap6StringEEEPT_v(
    QV4::HeapItem *self) {
  return self->as<QV4::Heap::String>();
}

//  QV4::Heap::FunctionObject *QV4::HeapItem::as<QV4::Heap::FunctionObject>()
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZN3QV48HeapItem2asINS_4Heap14FunctionObjectEEEPT_v(
    QV4::HeapItem *self) {
  return self->as<QV4::Heap::FunctionObject>();
}

//  QV4::Heap::ArrayObject *QV4::HeapItem::as<QV4::Heap::ArrayObject>()
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV48HeapItem2asINS_4Heap11ArrayObjectEEEPT_v(
    QV4::HeapItem *self) {
  return self->as<QV4::Heap::ArrayObject>();
}
