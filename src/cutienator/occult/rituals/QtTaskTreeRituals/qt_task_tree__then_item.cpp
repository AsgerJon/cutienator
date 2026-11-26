//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qconditional.h>
#include <QtTaskTree/qtasktree.h>

//  ExecutableItem QtTaskTree::ThenItem::operator ExecutableItem() const
extern "C" Q_DECL_EXPORT
QtTaskTree::ExecutableItem *ritual_ZNK10QtTaskTree8ThenItemcvNS_14ExecutableItemEEv(
    const QtTaskTree::ThenItem *self) {
  return new QtTaskTree::ExecutableItem(
      self->operator QtTaskTree::ExecutableItem());
}

//  QtTaskTree::ThenItem::ThenItem(const ThenItem &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTree8ThenItemC1ERKS0_(
    const QtTaskTree::ThenItem *other) {
  return new QtTaskTree::ThenItem(*other);
}

//  QtTaskTree::ThenItem::ThenItem(ThenItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTree8ThenItemC1EOS0_(
    QtTaskTree::ThenItem *other) {
  return new QtTaskTree::ThenItem(std::move(*other));
}

//  ThenItem &QtTaskTree::ThenItem::operator=(ThenItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTree8ThenItemaSEOS0_(
    QtTaskTree::ThenItem *self,
    QtTaskTree::ThenItem *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QtTaskTree::ThenItem::swap(ThenItem &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree8ThenItem4swapERS0_(
    QtTaskTree::ThenItem *self,
    QtTaskTree::ThenItem *other) {
  self->swap(*other);
}

//  ElseItem operator>>(const ThenItem &thenItem, const Else &elseItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseItem *ritual_ZN10QtTaskTreersERKNS_8ThenItemERKNS_4ElseE(
    const QtTaskTree::ThenItem *thenItem,
    const QtTaskTree::Else *elseItem) {
  return new QtTaskTree::ElseItem(operator>>(*thenItem, *elseItem));
}

//  ElseIfItem operator>>(const ThenItem &thenItem, const ElseIf &elseIfItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIfItem *ritual_ZN10QtTaskTreersERKNS_8ThenItemERKNS_6ElseIfE(
    const QtTaskTree::ThenItem *thenItem,
    const QtTaskTree::ElseIf *elseIfItem) {
  return new QtTaskTree::ElseIfItem(operator>>(*thenItem, *elseIfItem));
}
