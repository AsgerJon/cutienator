//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::RepeatIterator::RepeatIterator(qsizetype count)
extern "C" Q_DECL_EXPORT
QtTaskTree::RepeatIterator *ritual_ZN10QtTaskTree14RepeatIteratorC1Ex(
    qsizetype count) {
  return new QtTaskTree::RepeatIterator(count);
}

//  QtTaskTree::RepeatIterator::~RepeatIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree14RepeatIteratorD1Ev(
    QtTaskTree::RepeatIterator *self) {
  delete self;
}
