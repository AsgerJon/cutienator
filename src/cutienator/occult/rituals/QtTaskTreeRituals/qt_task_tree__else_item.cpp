//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qconditional.h>
#include <QtTaskTree/qtasktree.h>

//  ExecutableItem QtTaskTree::ElseItem::operator ExecutableItem() const
extern "C" Q_DECL_EXPORT
QtTaskTree::ExecutableItem *ritual_ZNK10QtTaskTree8ElseItemcvNS_14ExecutableItemEEv(
    const QtTaskTree::ElseItem *self) {
  return new QtTaskTree::ExecutableItem(
      self->operator QtTaskTree::ExecutableItem());
}

//  QtTaskTree::ElseItem::ElseItem(const ElseItem &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseItem *ritual_ZN10QtTaskTree8ElseItemC1ERKS0_(
    const QtTaskTree::ElseItem *other) {
  return new QtTaskTree::ElseItem(*other);
}

//  QtTaskTree::ElseItem::ElseItem(ElseItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseItem *ritual_ZN10QtTaskTree8ElseItemC1EOS0_(
    QtTaskTree::ElseItem *other) {
  return new QtTaskTree::ElseItem(std::move(*other));
}

//  ElseItem &QtTaskTree::ElseItem::operator=(ElseItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseItem *ritual_ZN10QtTaskTree8ElseItemaSEOS0_(
    QtTaskTree::ElseItem *self,
    QtTaskTree::ElseItem *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QtTaskTree::ElseItem::swap(ElseItem &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree8ElseItem4swapERS0_(
    QtTaskTree::ElseItem *self,
    QtTaskTree::ElseItem *other) {
  self->swap(*other);
}
