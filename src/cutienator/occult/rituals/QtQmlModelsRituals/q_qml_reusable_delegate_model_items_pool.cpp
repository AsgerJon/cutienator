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

//  int QQmlReusableDelegateModelItemsPool::size()
extern "C" Q_DECL_EXPORT
int ritual_ZN34QQmlReusableDelegateModelItemsPool4sizeEv(
    QQmlReusableDelegateModelItemsPool *self) {
  return self->size();
}

//  QQmlReusableDelegateModelItemsPool::~QQmlReusableDelegateModelItemsPool()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQmlReusableDelegateModelItemsPoolD1Ev(
    QQmlReusableDelegateModelItemsPool *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
