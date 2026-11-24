//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qbarriertask.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qbarriertask.h>
#include <QtTaskTree/qtasktree.h>

//  Group operator>>(const When &whenItem, const Do &doItem)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreersERKNS_4WhenERKNS_2DoE(
    const QtTaskTree::When *whenItem,
    const QtTaskTree::Do *doItem) {
  return new QtTaskTree::Group(operator>>(*whenItem, *doItem));
}
