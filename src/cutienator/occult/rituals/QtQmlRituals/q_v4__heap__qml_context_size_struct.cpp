//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Heap::QmlContextSizeStruct as the QV4::Heap::QmlContextOffsetStruct
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContextOffsetStruct *ritual_cast_QV4_Heap_QmlContextSizeStruct_QV4_Heap_QmlContextOffsetStruct(
    QV4::Heap::QmlContextSizeStruct *self) {
  return static_cast<QV4::Heap::QmlContextOffsetStruct *>(self);
}
