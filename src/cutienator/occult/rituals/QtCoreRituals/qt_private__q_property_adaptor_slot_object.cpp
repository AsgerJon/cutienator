//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>

//  const QPropertyBindingData
//      &QtPrivate::QPropertyAdaptorSlotObject::bindingData() const
extern "C" Q_DECL_EXPORT
const QtPrivate::QPropertyBindingData *ritual_ZNK9QtPrivate26QPropertyAdaptorSlotObject11bindingDataEv(
    const QtPrivate::QPropertyAdaptorSlotObject *self) {
  return &(self->bindingData());
}

//  QPropertyBindingData
//      &QtPrivate::QPropertyAdaptorSlotObject::bindingData()
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZN9QtPrivate26QPropertyAdaptorSlotObject11bindingDataEv(
    QtPrivate::QPropertyAdaptorSlotObject *self) {
  return &(self->bindingData());
}

//  QObject *QtPrivate::QPropertyAdaptorSlotObject::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK9QtPrivate26QPropertyAdaptorSlotObject6objectEv(
    const QtPrivate::QPropertyAdaptorSlotObject *self) {
  return self->object();
}

//  const QMetaProperty
//      &QtPrivate::QPropertyAdaptorSlotObject::metaProperty() const
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZNK9QtPrivate26QPropertyAdaptorSlotObject12metaPropertyEv(
    const QtPrivate::QPropertyAdaptorSlotObject *self) {
  return new QMetaProperty(self->metaProperty());
}

//  QtPrivate::QPropertyAdaptorSlotObject as the QtPrivate::QSlotObjectBase
//      it is built on
extern "C" Q_DECL_EXPORT
QtPrivate::QSlotObjectBase *ritual_cast_QtPrivate_QPropertyAdaptorSlotObject_QtPrivate_QSlotObjectBase(
    QtPrivate::QPropertyAdaptorSlotObject *self) {
  return static_cast<QtPrivate::QSlotObjectBase *>(self);
}
