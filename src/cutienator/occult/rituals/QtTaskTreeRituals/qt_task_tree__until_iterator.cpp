//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::UntilIterator::UntilIterator(const Condition &condition)
extern "C" Q_DECL_EXPORT
QtTaskTree::UntilIterator *ritual_ZN10QtTaskTree13UntilIteratorC1ERKSt8functionIFbxEE(
    const QtTaskTree::Iterator::Condition *condition) {
  return new QtTaskTree::UntilIterator(*condition);
}

//  QtTaskTree::UntilIterator::~UntilIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree13UntilIteratorD1Ev(
    QtTaskTree::UntilIterator *self) {
  delete self;
}
