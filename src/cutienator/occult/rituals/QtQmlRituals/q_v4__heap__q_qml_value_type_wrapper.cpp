//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  void QV4::Heap::QQmlValueTypeWrapper::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QQmlValueTypeWrapper::markObjects(b, stack);
}

//  QMetaType QV4::Heap::QQmlValueTypeWrapper::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper8metaTypeEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return new QMetaType(self->metaType());
}

//  const QMetaObject *QV4::Heap::QQmlValueTypeWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV44Heap20QQmlValueTypeWrapper10metaObjectEv(
    const QV4::Heap::QQmlValueTypeWrapper *self) {
  return self->metaObject();
}

//  void QV4::Heap::QQmlValueTypeWrapper::setMetaObject(const QMetaObject
//      *metaObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper13setMetaObjectEPK11QMetaObject(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const QMetaObject *metaObject) {
  self->setMetaObject(metaObject);
}

//  void QV4::Heap::QQmlValueTypeWrapper::setMetaType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20QQmlValueTypeWrapper11setMetaTypeE9QMetaType(
    QV4::Heap::QQmlValueTypeWrapper *self,
    const QMetaType *metaType) {
  self->setMetaType(*metaType);
}

//  QV4::Heap::QQmlValueTypeWrapper as the
//      QV4::Heap::QQmlValueTypeWrapperData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlValueTypeWrapperData *ritual_cast_QV4_Heap_QQmlValueTypeWrapper_QV4_Heap_QQmlValueTypeWrapperData(
    QV4::Heap::QQmlValueTypeWrapper *self) {
  return static_cast<QV4::Heap::QQmlValueTypeWrapperData *>(self);
}
