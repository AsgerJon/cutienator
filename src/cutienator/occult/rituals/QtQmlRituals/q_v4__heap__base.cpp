//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4heap_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4heap_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::Base::markObjects(Base *a0, MarkStack *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base11markObjectsEPS1_PNS_9MarkStackE(
    QV4::Heap::Base *a0,
    QV4::MarkStack *a1) {
  QV4::Heap::Base::markObjects(a0, a1);
}

//  ReturnedValue QV4::Heap::Base::asReturnedValue() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV44Heap4Base15asReturnedValueEv(
    const QV4::Heap::Base *self) {
  return self->asReturnedValue();
}

//  void QV4::Heap::Base::mark(QV4::MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base4markEPNS_9MarkStackE(
    QV4::Heap::Base *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
}

//  bool QV4::Heap::Base::isMarked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap4Base8isMarkedEv(const QV4::Heap::Base *self) {
  return self->isMarked();
}

//  void QV4::Heap::Base::setMarkBit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base10setMarkBitEv(QV4::Heap::Base *self) {
  self->setMarkBit();
}

//  bool QV4::Heap::Base::inUse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap4Base5inUseEv(const QV4::Heap::Base *self) {
  return self->inUse();
}

//  void QV4::Heap::Base::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base4initEv(QV4::Heap::Base *self) {
  self->init();
}

//  void QV4::Heap::Base::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base7destroyEv(QV4::Heap::Base *self) {
  self->destroy();
}

#if !(defined(QML_CHECK_INIT_DESTROY_CALLS))
//  void QV4::Heap::Base::_checkIsInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base19_checkIsInitializedEv(QV4::Heap::Base *self) {
  self->_checkIsInitialized();
}
#endif  // !(defined(QML_CHECK_INIT_DESTROY_CALLS))

#if !(defined(QML_CHECK_INIT_DESTROY_CALLS))
//  void QV4::Heap::Base::_checkIsDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base17_checkIsDestroyedEv(QV4::Heap::Base *self) {
  self->_checkIsDestroyed();
}
#endif  // !(defined(QML_CHECK_INIT_DESTROY_CALLS))

#if !(defined(QML_CHECK_INIT_DESTROY_CALLS))
//  void QV4::Heap::Base::_setInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base15_setInitializedEv(QV4::Heap::Base *self) {
  self->_setInitialized();
}
#endif  // !(defined(QML_CHECK_INIT_DESTROY_CALLS))

#if !(defined(QML_CHECK_INIT_DESTROY_CALLS))
//  void QV4::Heap::Base::_setDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap4Base13_setDestroyedEv(QV4::Heap::Base *self) {
  self->_setDestroyed();
}
#endif  // !(defined(QML_CHECK_INIT_DESTROY_CALLS))
