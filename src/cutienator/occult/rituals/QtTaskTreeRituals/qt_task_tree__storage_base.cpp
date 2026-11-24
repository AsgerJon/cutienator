//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>

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
