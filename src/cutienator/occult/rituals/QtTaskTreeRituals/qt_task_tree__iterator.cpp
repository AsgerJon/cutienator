//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::Iterator::Iterator(const Iterator &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Iterator *ritual_ZN10QtTaskTree8IteratorC1ERKS0_(
    const QtTaskTree::Iterator *other) {
  return new QtTaskTree::Iterator(*other);
}

//  QtTaskTree::Iterator::Iterator(Iterator &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::Iterator *ritual_ZN10QtTaskTree8IteratorC1EOS0_(
    QtTaskTree::Iterator *other) {
  return new QtTaskTree::Iterator(std::move(*other));
}

//  void QtTaskTree::Iterator::swap(Iterator &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree8Iterator4swapERS0_(
    QtTaskTree::Iterator *self,
    QtTaskTree::Iterator *other) {
  self->swap(*other);
}

//  qsizetype QtTaskTree::Iterator::iteration() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QtTaskTree8Iterator9iterationEv(
    const QtTaskTree::Iterator *self) {
  return self->iteration();
}

//  QtTaskTree::Iterator::Iterator()
extern "C" Q_DECL_EXPORT
QtTaskTree::Iterator *ritual_ZN10QtTaskTree8IteratorC1Ev() {
  return new QtTaskTree::Iterator();
}

//  QtTaskTree::Iterator::Iterator(qsizetype count, const ValueGetter
//      &valueGetter)
extern "C" Q_DECL_EXPORT
QtTaskTree::Iterator *ritual_ZN10QtTaskTree8IteratorC1ExRKSt8functionIFPKvxEE(
    qsizetype count,
    const QtTaskTree::Iterator::ValueGetter *valueGetter) {
  return new QtTaskTree::Iterator(count, *valueGetter);
}

//  QtTaskTree::Iterator::Iterator(const Condition &condition)
extern "C" Q_DECL_EXPORT
QtTaskTree::Iterator *ritual_ZN10QtTaskTree8IteratorC1ERKSt8functionIFbxEE(
    const QtTaskTree::Iterator::Condition *condition) {
  return new QtTaskTree::Iterator(*condition);
}

//  QtTaskTree::Iterator::Iterator(LazyList &&lazyList)
extern "C" Q_DECL_EXPORT
QtTaskTree::Iterator *ritual_ZN10QtTaskTree8IteratorC1EONS0_8LazyListE(
    QtTaskTree::Iterator::LazyList *lazyList) {
  return new QtTaskTree::Iterator(std::move(*lazyList));
}

//  const void *QtTaskTree::Iterator::valuePtr() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK10QtTaskTree8Iterator8valuePtrEv(
    const QtTaskTree::Iterator *self) {
  return self->valuePtr();
}
