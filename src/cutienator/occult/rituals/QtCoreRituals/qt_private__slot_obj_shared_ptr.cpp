//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr()
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtrC1Ev() {
  return new QtPrivate::SlotObjSharedPtr();
}

//  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtrC1EDn() {
  return new QtPrivate::SlotObjSharedPtr(nullptr);
}

//  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(const SlotObjSharedPtr
//      &other)
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtrC1ERKS0_(
    const QtPrivate::SlotObjSharedPtr *other) {
  return new QtPrivate::SlotObjSharedPtr(*other);
}

//  SlotObjSharedPtr &QtPrivate::SlotObjSharedPtr::operator=(const
//      SlotObjSharedPtr &other)
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtraSERKS0_(
    QtPrivate::SlotObjSharedPtr *self,
    const QtPrivate::SlotObjSharedPtr *other) {
  return &(self->operator=(*other));
}

//  QtPrivate::SlotObjSharedPtr::SlotObjSharedPtr(SlotObjSharedPtr &&other)
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtrC1EOS0_(
    QtPrivate::SlotObjSharedPtr *other) {
  return new QtPrivate::SlotObjSharedPtr(std::move(*other));
}

//  SlotObjSharedPtr &QtPrivate::SlotObjSharedPtr::operator=(SlotObjSharedPtr
//      &&other)
extern "C" Q_DECL_EXPORT
QtPrivate::SlotObjSharedPtr *ritual_ZN9QtPrivate16SlotObjSharedPtraSEOS0_(
    QtPrivate::SlotObjSharedPtr *self,
    QtPrivate::SlotObjSharedPtr *other) {
  return &(self->operator=(std::move(*other)));
}

//  QtPrivate::SlotObjSharedPtr::~SlotObjSharedPtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16SlotObjSharedPtrD1Ev(
    QtPrivate::SlotObjSharedPtr *self) {
  delete self;
}

//  void QtPrivate::SlotObjSharedPtr::swap(SlotObjSharedPtr &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16SlotObjSharedPtr4swapERS0_(
    QtPrivate::SlotObjSharedPtr *self,
    QtPrivate::SlotObjSharedPtr *other) {
  self->swap(*other);
}

//  bool QtPrivate::SlotObjSharedPtr::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate16SlotObjSharedPtrcvbEv(
    const QtPrivate::SlotObjSharedPtr *self) {
  return self->operator bool();
}
