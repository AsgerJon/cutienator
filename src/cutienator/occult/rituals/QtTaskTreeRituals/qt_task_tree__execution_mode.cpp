//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::ExecutionMode::ExecutionMode(int limit)
extern "C" Q_DECL_EXPORT
QtTaskTree::ExecutionMode *ritual_ZN10QtTaskTree13ExecutionModeC1Ei(
    int limit) {
  return new QtTaskTree::ExecutionMode(limit);
}

//  QtTaskTree::ExecutionMode::~ExecutionMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree13ExecutionModeD1Ev(
    QtTaskTree::ExecutionMode *self) {
  delete self;
}
