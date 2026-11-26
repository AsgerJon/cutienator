//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qconditional.h>

//  QtTaskTree::ElseIfItem::ElseIfItem(const ElseIfItem &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIfItem *ritual_ZN10QtTaskTree10ElseIfItemC1ERKS0_(
    const QtTaskTree::ElseIfItem *other) {
  return new QtTaskTree::ElseIfItem(*other);
}

//  QtTaskTree::ElseIfItem::ElseIfItem(ElseIfItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIfItem *ritual_ZN10QtTaskTree10ElseIfItemC1EOS0_(
    QtTaskTree::ElseIfItem *other) {
  return new QtTaskTree::ElseIfItem(std::move(*other));
}

//  ElseIfItem &QtTaskTree::ElseIfItem::operator=(ElseIfItem &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::ElseIfItem *ritual_ZN10QtTaskTree10ElseIfItemaSEOS0_(
    QtTaskTree::ElseIfItem *self,
    QtTaskTree::ElseIfItem *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QtTaskTree::ElseIfItem::swap(ElseIfItem &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree10ElseIfItem4swapERS0_(
    QtTaskTree::ElseIfItem *self,
    QtTaskTree::ElseIfItem *other) {
  self->swap(*other);
}

//  ThenItem operator>>(const ElseIfItem &elseIfItem, const Then &thenItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTreersERKNS_10ElseIfItemERKNS_4ThenE(
    const QtTaskTree::ElseIfItem *elseIfItem,
    const QtTaskTree::Then *thenItem) {
  return new QtTaskTree::ThenItem(operator>>(*elseIfItem, *thenItem));
}
