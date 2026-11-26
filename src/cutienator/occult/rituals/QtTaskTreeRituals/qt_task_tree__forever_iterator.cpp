//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::ForeverIterator::ForeverIterator()
extern "C" Q_DECL_EXPORT
QtTaskTree::ForeverIterator *ritual_ZN10QtTaskTree15ForeverIteratorC1Ev() {
  return new QtTaskTree::ForeverIterator();
}

//  QtTaskTree::ForeverIterator::~ForeverIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree15ForeverIteratorD1Ev(
    QtTaskTree::ForeverIterator *self) {
  delete self;
}
