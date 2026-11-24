//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  Group operator!(const ExecutableItem &item)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreentERKNS_14ExecutableItemE(
    const QtTaskTree::ExecutableItem *item) {
  return new QtTaskTree::Group(operator!(*item));
}

//  Group operator&&(const ExecutableItem &first, const ExecutableItem
//      &second)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeaaERKNS_14ExecutableItemES2_(
    const QtTaskTree::ExecutableItem *first,
    const QtTaskTree::ExecutableItem *second) {
  return new QtTaskTree::Group(operator&&(*first, *second));
}

//  Group operator||(const ExecutableItem &first, const ExecutableItem
//      &second)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeooERKNS_14ExecutableItemES2_(
    const QtTaskTree::ExecutableItem *first,
    const QtTaskTree::ExecutableItem *second) {
  return new QtTaskTree::Group(operator||(*first, *second));
}

//  Group operator&&(const ExecutableItem &item, DoneResult result)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeaaERKNS_14ExecutableItemENS_10DoneResultE(
    const QtTaskTree::ExecutableItem *item,
    QtTaskTree::DoneResult result) {
  return new QtTaskTree::Group(operator&&(*item, result));
}

//  Group operator||(const ExecutableItem &item, DoneResult result)
extern "C" Q_DECL_EXPORT
QtTaskTree::Group *ritual_ZN10QtTaskTreeooERKNS_14ExecutableItemENS_10DoneResultE(
    const QtTaskTree::ExecutableItem *item,
    QtTaskTree::DoneResult result) {
  return new QtTaskTree::Group(operator||(*item, result));
}

//  QtTaskTree::ExecutableItem::~ExecutableItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree14ExecutableItemD1Ev(
    QtTaskTree::ExecutableItem *self) {
  delete self;
}
