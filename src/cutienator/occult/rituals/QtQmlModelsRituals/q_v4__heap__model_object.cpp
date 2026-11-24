//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_list_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmllistmodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ModelObject::init(QObject *object, QQmlListModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ModelObject4initEP7QObjectP13QQmlListModel(
    QV4::Heap::ModelObject *self,
    QObject *object,
    QQmlListModel *model) {
  self->init(object, model);
}

//  void QV4::Heap::ModelObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ModelObject7destroyEv(
    QV4::Heap::ModelObject *self) {
  self->destroy();
}

//  int QV4::Heap::ModelObject::elementIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap11ModelObject12elementIndexEv(
    const QV4::Heap::ModelObject *self) {
  return self->elementIndex();
}

#endif  // QT_CONFIG(qml_list_model)
