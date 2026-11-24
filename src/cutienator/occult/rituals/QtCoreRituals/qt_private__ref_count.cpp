//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrefcount.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrefcount.h>

//  bool QtPrivate::RefCount::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate8RefCount3refEv(QtPrivate::RefCount *self) {
  return self->ref();
}

//  bool QtPrivate::RefCount::deref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate8RefCount5derefEv(QtPrivate::RefCount *self) {
  return self->deref();
}

//  bool QtPrivate::RefCount::isStatic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate8RefCount8isStaticEv(
    const QtPrivate::RefCount *self) {
  return self->isStatic();
}

//  bool QtPrivate::RefCount::isShared() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate8RefCount8isSharedEv(
    const QtPrivate::RefCount *self) {
  return self->isShared();
}

//  void QtPrivate::RefCount::initializeOwned()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate8RefCount15initializeOwnedEv(
    QtPrivate::RefCount *self) {
  self->initializeOwned();
}

//  void QtPrivate::RefCount::initializeUnsharable()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate8RefCount20initializeUnsharableEv(
    QtPrivate::RefCount *self) {
  self->initializeUnsharable();
}
