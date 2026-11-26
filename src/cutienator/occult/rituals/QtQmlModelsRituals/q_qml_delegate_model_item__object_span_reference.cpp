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
#include <QtCore/QSpan>

//  QQmlDelegateModelItem::ObjectSpanReference::ObjectSpanReference(QSpan<QQm
//      lDelegateModelItem *const> span)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItem::ObjectSpanReference *ritual_ZN21QQmlDelegateModelItem19ObjectSpanReferenceC1E5QSpanIKPS_Lm18446744073709551615EE(
    const QSpan<QQmlDelegateModelItem *const> *span) {
  return new QQmlDelegateModelItem::ObjectSpanReference(*span);
}

//  QQmlDelegateModelItem::ObjectSpanReference::~ObjectSpanReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlDelegateModelItem19ObjectSpanReferenceD1Ev(
    QQmlDelegateModelItem::ObjectSpanReference *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
