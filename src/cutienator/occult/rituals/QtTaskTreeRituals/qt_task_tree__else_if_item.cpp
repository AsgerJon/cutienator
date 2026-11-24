//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qconditional.h>

//  ThenItem operator>>(const ElseIfItem &elseIfItem, const Then &thenItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTreersERKNS_10ElseIfItemERKNS_4ThenE(
    const QtTaskTree::ElseIfItem *elseIfItem,
    const QtTaskTree::Then *thenItem) {
  return new QtTaskTree::ThenItem(operator>>(*elseIfItem, *thenItem));
}
