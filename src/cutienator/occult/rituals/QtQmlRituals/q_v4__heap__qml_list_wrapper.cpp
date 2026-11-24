//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

//  QObject *QV4::Heap::QmlListWrapper::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV44Heap14QmlListWrapper6objectEv(
    const QV4::Heap::QmlListWrapper *self) {
  return self->object();
}

//  QMetaType QV4::Heap::QmlListWrapper::propertyType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap14QmlListWrapper12propertyTypeEv(
    const QV4::Heap::QmlListWrapper *self) {
  return new QMetaType(self->propertyType());
}

//  QMetaType QV4::Heap::QmlListWrapper::elementType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap14QmlListWrapper11elementTypeEv(
    const QV4::Heap::QmlListWrapper *self) {
  return new QMetaType(self->elementType());
}
