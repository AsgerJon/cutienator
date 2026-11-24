//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qconditional.h>

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
