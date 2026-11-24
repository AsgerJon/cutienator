//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlDelegateModelItem::ScriptReference::ScriptReference(QQmlDelegateModel
//      Item *item)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem::ScriptReference *ritual_ZN21QQmlDelegateModelItem15ScriptReferenceC1EPS_(
    QQmlDelegateModelItem *item) {
  return new QQmlDelegateModelItem::ScriptReference(item);
}

//  QQmlDelegateModelItem::ScriptReference::~ScriptReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem15ScriptReferenceD1Ev(
    QQmlDelegateModelItem::ScriptReference *self) {
  delete self;
}

//  QQmlDelegateModelItem *QQmlDelegateModelItem::ScriptReference::data()
//      const
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem *ritual_ZNK21QQmlDelegateModelItem15ScriptReference4dataEv(
    const QQmlDelegateModelItem::ScriptReference *self) {
  return self->data();
}

#endif  // QT_CONFIG(qml_delegate_model)
