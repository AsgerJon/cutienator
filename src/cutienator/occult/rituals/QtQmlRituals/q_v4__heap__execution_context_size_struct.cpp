//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Heap::ExecutionContextSizeStruct as the
//      QV4::Heap::ExecutionContextOffsetStruct it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContextOffsetStruct *ritual_cast_QV4_Heap_ExecutionContextSizeStruct_QV4_Heap_ExecutionContextOffsetStruct(
    QV4::Heap::ExecutionContextSizeStruct *self) {
  return static_cast<QV4::Heap::ExecutionContextOffsetStruct *>(self);
}
