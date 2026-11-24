//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  const QMetaObject *QV4::Heap::QMetaObjectWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV44Heap18QMetaObjectWrapper10metaObjectEv(
    const QV4::Heap::QMetaObjectWrapper *self) {
  return self->metaObject();
}

//  QMetaType QV4::Heap::QMetaObjectWrapper::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap18QMetaObjectWrapper8metaTypeEv(
    const QV4::Heap::QMetaObjectWrapper *self) {
  return new QMetaType(self->metaType());
}
