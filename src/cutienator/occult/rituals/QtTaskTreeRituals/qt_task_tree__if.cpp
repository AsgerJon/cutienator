//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qconditional.h>

//  ThenItem operator>>(const If &ifItem, const Then &thenItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::ThenItem *ritual_ZN10QtTaskTreersERKNS_2IfERKNS_4ThenE(
    const QtTaskTree::If *ifItem,
    const QtTaskTree::Then *thenItem) {
  return new QtTaskTree::ThenItem(operator>>(*ifItem, *thenItem));
}
