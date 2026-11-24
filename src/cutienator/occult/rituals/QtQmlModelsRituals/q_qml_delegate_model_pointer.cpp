//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlDelegateModelPointer::QQmlDelegateModelPointer()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelPointer *ritual_ZN24QQmlDelegateModelPointerC1Ev() {
  return new QQmlDelegateModelPointer();
}

//  QQmlDelegateModelPointer::QQmlDelegateModelPointer(const
//      QQmlDelegateModelPointer &a0)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelPointer *ritual_ZN24QQmlDelegateModelPointerC1ERKS_(
    const QQmlDelegateModelPointer *a0) {
  return new QQmlDelegateModelPointer(*a0);
}

//  QQmlDelegateModelPointer::QQmlDelegateModelPointer(QQmlInstanceModel
//      *model)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelPointer *ritual_ZN24QQmlDelegateModelPointerC1EP17QQmlInstanceModel(
    QQmlInstanceModel *model) {
  return new QQmlDelegateModelPointer(model);
}

//  QQmlDelegateModelPointer::QQmlDelegateModelPointer(QQmlDelegateModel
//      *model)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelPointer *ritual_ZN24QQmlDelegateModelPointerC1EP17QQmlDelegateModel(
    QQmlDelegateModel *model) {
  return new QQmlDelegateModelPointer(model);
}

//  QQmlDelegateModel *QQmlDelegateModelPointer::delegateModel()
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZN24QQmlDelegateModelPointer13delegateModelEv(
    QQmlDelegateModelPointer *self) {
  return self->delegateModel();
}

//  QQmlInstanceModel *QQmlDelegateModelPointer::instanceModel()
extern "C" Q_DECL_EXPORT
QQmlInstanceModel *ritual_ZN24QQmlDelegateModelPointer13instanceModelEv(
    QQmlDelegateModelPointer *self) {
  return self->instanceModel();
}

//  bool QQmlDelegateModelPointer::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlDelegateModelPointercvbEv(
    const QQmlDelegateModelPointer *self) {
  return self->operator bool();
}

//  QQmlDelegateModelPointer::~QQmlDelegateModelPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlDelegateModelPointerD1Ev(
    QQmlDelegateModelPointer *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
