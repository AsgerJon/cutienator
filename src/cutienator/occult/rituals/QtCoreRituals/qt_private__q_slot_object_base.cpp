//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  bool QtPrivate::QSlotObjectBase::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QSlotObjectBase3refEv(
    QtPrivate::QSlotObjectBase *self) {
  return self->ref();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QtPrivate::QSlotObjectBase::destroyIfLastRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBase16destroyIfLastRefEv(
    QtPrivate::QSlotObjectBase *self) {
  self->destroyIfLastRef();
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  QtPrivate::QSlotObjectBase::~QSlotObjectBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBaseD1Ev(
    QtPrivate::QSlotObjectBase *self) {
  delete self;
}
