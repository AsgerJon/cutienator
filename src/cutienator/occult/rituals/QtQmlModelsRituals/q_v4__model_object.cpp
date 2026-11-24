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

//  void QV4::ModelObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ModelObject10__dataTestEv(QV4::ModelObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ModelObject *QV4::ModelObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ModelObject *ritual_ZNK3QV411ModelObject11d_uncheckedEv(
    const QV4::ModelObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ModelObject *QV4::ModelObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ModelObject *ritual_ZNK3QV411ModelObject1dEv(
    const QV4::ModelObject *self) {
  return self->d();
}

//  void QV4::ModelObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ModelObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ModelObject::virtualDestroy(b);
}

#endif  // QT_CONFIG(qml_list_model)
