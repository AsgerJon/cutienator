//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

//  QtTaskTree::StorageBase::StorageBase(const StorageBase &other)
extern "C" Q_DECL_EXPORT
QtTaskTree::StorageBase *ritual_ZN10QtTaskTree11StorageBaseC1ERKS0_(
    const QtTaskTree::StorageBase *other) {
  return new QtTaskTree::StorageBase(*other);
}

//  QtTaskTree::StorageBase::StorageBase(StorageBase &&other)
extern "C" Q_DECL_EXPORT
QtTaskTree::StorageBase *ritual_ZN10QtTaskTree11StorageBaseC1EOS0_(
    QtTaskTree::StorageBase *other) {
  return new QtTaskTree::StorageBase(std::move(*other));
}

//  void QtTaskTree::StorageBase::swap(StorageBase &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtTaskTree11StorageBase4swapERS0_(
    QtTaskTree::StorageBase *self,
    QtTaskTree::StorageBase *other) {
  self->swap(*other);
}

//  QtTaskTree::StorageBase::StorageBase(const StorageCreator &creator)
extern "C" Q_DECL_EXPORT
QtTaskTree::StorageBase *ritual_ZN10QtTaskTree11StorageBaseC1ERKSt8functionIFSt10shared_ptrIvEvEE(
    const QtTaskTree::StorageBase::StorageCreator *creator) {
  return new QtTaskTree::StorageBase(*creator);
}

//  void *QtTaskTree::StorageBase::activeStorageVoid() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK10QtTaskTree11StorageBase17activeStorageVoidEv(
    const QtTaskTree::StorageBase *self) {
  return self->activeStorageVoid();
}

//  bool operator==(const StorageBase &first, const StorageBase &second)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QtTaskTreeeqERKNS_11StorageBaseES2_(
    const QtTaskTree::StorageBase *first,
    const QtTaskTree::StorageBase *second) {
  return operator==(*first, *second);
}

//  bool operator!=(const StorageBase &first, const StorageBase &second)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QtTaskTreeneERKNS_11StorageBaseES2_(
    const QtTaskTree::StorageBase *first,
    const QtTaskTree::StorageBase *second) {
  return operator!=(*first, *second);
}
