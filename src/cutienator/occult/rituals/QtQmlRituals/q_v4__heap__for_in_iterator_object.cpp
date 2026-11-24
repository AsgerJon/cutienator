//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ForInIteratorObject::init(QV4::Object *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ForInIteratorObject4initEPNS_6ObjectE(
    QV4::Heap::ForInIteratorObject *self,
    QV4::Object *o) {
  self->init(o);
}

//  QV4::Heap::ForInIteratorObject as the QV4::Heap::ForInIteratorObjectData
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ForInIteratorObjectData *ritual_cast_QV4_Heap_ForInIteratorObject_QV4_Heap_ForInIteratorObjectData(
    QV4::Heap::ForInIteratorObject *self) {
  return static_cast<QV4::Heap::ForInIteratorObjectData *>(self);
}
