//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  void QtPrivate::QSlotObjectBase::Deleter::operator()(QSlotObjectBase *p)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate15QSlotObjectBase7DeleterclEPS0_(
    const QtPrivate::QSlotObjectBase::Deleter *self,
    QtPrivate::QSlotObjectBase *p) {
  self->operator()(p);
}

//  void QtPrivate::QSlotObjectBase::Deleter::cleanup(QSlotObjectBase *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBase7Deleter7cleanupEPS0_(
    QtPrivate::QSlotObjectBase *p) {
  QtPrivate::QSlotObjectBase::Deleter::cleanup(p);
}

//  QtPrivate::QSlotObjectBase::Deleter::~Deleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBase7DeleterD1Ev(
    QtPrivate::QSlotObjectBase::Deleter *self) {
  delete self;
}
