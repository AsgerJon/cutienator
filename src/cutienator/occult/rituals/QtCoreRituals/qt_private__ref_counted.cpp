//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpropertyprivate.h>

//  int QtPrivate::RefCounted::refCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QtPrivate10RefCounted8refCountEv(
    const QtPrivate::RefCounted *self) {
  return self->refCount();
}

//  void QtPrivate::RefCounted::addRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate10RefCounted6addRefEv(QtPrivate::RefCounted *self) {
  self->addRef();
}

//  bool QtPrivate::RefCounted::deref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate10RefCounted5derefEv(QtPrivate::RefCounted *self) {
  return self->deref();
}

//  QtPrivate::RefCounted::~RefCounted()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate10RefCountedD1Ev(QtPrivate::RefCounted *self) {
  delete self;
}
