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
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QQmlDelegateModelItemMetaType::QQmlDelegateModelItemMetaType(QV4::Executi
//      onEngine *engine, QQmlDelegateModel *model, const QStringList
//      &groupNames)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItemMetaType *ritual_ZN29QQmlDelegateModelItemMetaTypeC1EPN3QV415ExecutionEngineEP17QQmlDelegateModelRK5QListI7QStringE(
    QV4::ExecutionEngine *engine,
    QQmlDelegateModel *model,
    const QList<QString> *groupNames) {
  return new QQmlDelegateModelItemMetaType(engine, model, *groupNames);
}

//  QQmlDelegateModelItemMetaType::QQmlDelegateModelItemMetaType(QV4::Executi
//      onEngine *engine, QQmlTableInstanceModel *model)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelItemMetaType *ritual_ZN29QQmlDelegateModelItemMetaTypeC1EPN3QV415ExecutionEngineEP22QQmlTableInstanceModel(
    QV4::ExecutionEngine *engine,
    QQmlTableInstanceModel *model) {
  return new QQmlDelegateModelItemMetaType(engine, model);
}

//  QQmlDelegateModelItemMetaType::~QQmlDelegateModelItemMetaType()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelItemMetaTypeD1Ev(
    QQmlDelegateModelItemMetaType *self) {
  delete self;
}

//  void QQmlDelegateModelItemMetaType::initializeAttachedMetaObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelItemMetaType28initializeAttachedMetaObjectEv(
    QQmlDelegateModelItemMetaType *self) {
  self->initializeAttachedMetaObject();
}

//  void QQmlDelegateModelItemMetaType::initializePrototype()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelItemMetaType19initializePrototypeEv(
    QQmlDelegateModelItemMetaType *self) {
  self->initializePrototype();
}

//  int QQmlDelegateModelItemMetaType::parseGroups(const QStringList
//      &groupNames) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQmlDelegateModelItemMetaType11parseGroupsERK5QListI7QStringE(
    const QQmlDelegateModelItemMetaType *self,
    const QList<QString> *groupNames) {
  return self->parseGroups(*groupNames);
}

//  int QQmlDelegateModelItemMetaType::parseGroups(const QV4::Value
//      &groupNames) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQmlDelegateModelItemMetaType11parseGroupsERKN3QV45ValueE(
    const QQmlDelegateModelItemMetaType *self,
    const QV4::Value *groupNames) {
  return self->parseGroups(*groupNames);
}

//  QQmlDelegateModel *QQmlDelegateModelItemMetaType::delegateModel() const
extern "C" Q_DECL_EXPORT
QQmlDelegateModel *ritual_ZNK29QQmlDelegateModelItemMetaType13delegateModelEv(
    const QQmlDelegateModelItemMetaType *self) {
  return self->delegateModel();
}

//  qsizetype QQmlDelegateModelItemMetaType::groupCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK29QQmlDelegateModelItemMetaType10groupCountEv(
    const QQmlDelegateModelItemMetaType *self) {
  return self->groupCount();
}

//  void QQmlDelegateModelItemMetaType::emitModelChanged() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QQmlDelegateModelItemMetaType16emitModelChangedEv(
    const QQmlDelegateModelItemMetaType *self) {
  self->emitModelChanged();
}

#endif  // QT_CONFIG(qml_delegate_model)
