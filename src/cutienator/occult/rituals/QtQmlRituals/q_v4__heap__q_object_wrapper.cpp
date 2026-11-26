//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::QObjectWrapper::init(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14QObjectWrapper4initEP7QObject(
    QV4::Heap::QObjectWrapper *self,
    QObject *object) {
  self->init(object);
}

//  void QV4::Heap::QObjectWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14QObjectWrapper7destroyEv(
    QV4::Heap::QObjectWrapper *self) {
  self->destroy();
}

//  QObject *QV4::Heap::QObjectWrapper::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV44Heap14QObjectWrapper6objectEv(
    const QV4::Heap::QObjectWrapper *self) {
  return self->object();
}

//  void QV4::Heap::QObjectWrapper::markObjects(Heap::Base *that, MarkStack
//      *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14QObjectWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *that,
    QV4::MarkStack *markStack) {
  QV4::Heap::QObjectWrapper::markObjects(that, markStack);
}
