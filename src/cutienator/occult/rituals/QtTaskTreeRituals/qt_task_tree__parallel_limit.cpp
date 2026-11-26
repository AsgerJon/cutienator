//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::ParallelLimit::ParallelLimit(int limit)
extern "C" Q_DECL_EXPORT
QtTaskTree::ParallelLimit *ritual_ZN10QtTaskTree13ParallelLimitC1Ei(
    int limit) {
  return new QtTaskTree::ParallelLimit(limit);
}

//  QtTaskTree::ParallelLimit::~ParallelLimit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree13ParallelLimitD1Ev(
    QtTaskTree::ParallelLimit *self) {
  delete self;
}
