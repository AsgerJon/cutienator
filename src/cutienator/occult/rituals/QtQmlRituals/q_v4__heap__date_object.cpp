//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::DateObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::DateObject::markObjects(b, stack);
}

//  void QV4::Heap::DateObject::doSetLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject13doSetLocationEv(
    QV4::Heap::DateObject *self) {
  self->doSetLocation();
}

//  void QV4::Heap::DateObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject4initEv(QV4::Heap::DateObject *self) {
  self->init();
}

//  void QV4::Heap::DateObject::init(Date date)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10DateObject4initENS_4DateE(
    QV4::Heap::DateObject *self,
    const QV4::Date *date) {
  self->init(*date);
}

//  double QV4::Heap::DateObject::date() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV44Heap10DateObject4dateEv(
    const QV4::Heap::DateObject *self) {
  return self->date();
}

//  QV4::Heap::DateObject as the QV4::Heap::DateObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObjectData *ritual_cast_QV4_Heap_DateObject_QV4_Heap_DateObjectData(
    QV4::Heap::DateObject *self) {
  return static_cast<QV4::Heap::DateObjectData *>(self);
}
