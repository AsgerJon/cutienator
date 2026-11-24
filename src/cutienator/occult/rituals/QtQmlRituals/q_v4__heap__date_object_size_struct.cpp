//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Heap::DateObjectSizeStruct as the QV4::Heap::DateObjectOffsetStruct
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObjectOffsetStruct *ritual_cast_QV4_Heap_DateObjectSizeStruct_QV4_Heap_DateObjectOffsetStruct(
    QV4::Heap::DateObjectSizeStruct *self) {
  return static_cast<QV4::Heap::DateObjectOffsetStruct *>(self);
}
