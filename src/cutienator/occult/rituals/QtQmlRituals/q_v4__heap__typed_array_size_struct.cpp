//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4typedarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Heap::TypedArraySizeStruct as the QV4::Heap::TypedArrayOffsetStruct
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArrayOffsetStruct *ritual_cast_QV4_Heap_TypedArraySizeStruct_QV4_Heap_TypedArrayOffsetStruct(
    QV4::Heap::TypedArraySizeStruct *self) {
  return static_cast<QV4::Heap::TypedArrayOffsetStruct *>(self);
}
