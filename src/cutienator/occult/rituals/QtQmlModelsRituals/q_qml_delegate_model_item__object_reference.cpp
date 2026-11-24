//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlDelegateModelItem::ObjectReference::ObjectReference(QQmlDelegateModel
//      Item *item)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem::ObjectReference *ritual_ZN21QQmlDelegateModelItem15ObjectReferenceC1EPS_(
    QQmlDelegateModelItem *item) {
  return new QQmlDelegateModelItem::ObjectReference(item);
}

//  QQmlDelegateModelItem::ObjectReference::~ObjectReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem15ObjectReferenceD1Ev(
    QQmlDelegateModelItem::ObjectReference *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
