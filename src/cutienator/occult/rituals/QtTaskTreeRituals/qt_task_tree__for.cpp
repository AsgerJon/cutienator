//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  Group operator>>(const For &forItem, const Do &doItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreersERKNS_3ForERKNS_2DoE(
    const QtTaskTree::For *forItem,
    const QtTaskTree::Do *doItem) {
  return new QtTaskTree::Group(operator>>(*forItem, *doItem));
}
