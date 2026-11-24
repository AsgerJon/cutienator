//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr()
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtrC1Ev() {
  return new QtPrivate::SlotObjSharedPtr();
}

//  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(const SlotObjSharedPtr
//      &other)
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtrC1ERKS0_(
    const QtPrivate::SlotObjSharedPtr *other) {
  return new QtPrivate::SlotObjSharedPtr(*other);
}

//  QtPrivate::SlotObjSharedPtr::~SlotObjSharedPtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16SlotObjSharedPtrD1Ev(
    QtPrivate::SlotObjSharedPtr *self) {
  delete self;
}

//  bool QtPrivate::SlotObjSharedPtr::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate16SlotObjSharedPtrcvbEv(
    const QtPrivate::SlotObjSharedPtr *self) {
  return self->operator bool();
}
