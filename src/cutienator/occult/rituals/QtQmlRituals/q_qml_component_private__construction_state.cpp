//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QQmlComponentPrivate::ConstructionState::ConstructionState()
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::ConstructionState *ritual_ZN20QQmlComponentPrivate17ConstructionStateC1Ev() {
  return new QQmlComponentPrivate::ConstructionState();
}

//  QQmlComponentPrivate::ConstructionState::ConstructionState(ConstructionSt
//      ate &&other)
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::ConstructionState *ritual_ZN20QQmlComponentPrivate17ConstructionStateC1EOS0_(
    QQmlComponentPrivate::ConstructionState *other) {
  return new QQmlComponentPrivate::ConstructionState(std::move(*other));
}

//  QQmlComponentPrivate::ConstructionState::~ConstructionState()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionStateD1Ev(
    QQmlComponentPrivate::ConstructionState *self) {
  delete self;
}

//  QQmlComponentPrivate::ConstructionState &QQmlComponentPrivate::Constructi
//      onState::operator=(QQmlComponentPrivate::ConstructionState &&other)
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate::ConstructionState *ritual_ZN20QQmlComponentPrivate17ConstructionStateaSEOS0_(
    QQmlComponentPrivate::ConstructionState *self,
    QQmlComponentPrivate::ConstructionState *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QQmlComponentPrivate::ConstructionState::swap(ConstructionState
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState4swapERS0_(
    QQmlComponentPrivate::ConstructionState *self,
    QQmlComponentPrivate::ConstructionState *other) {
  self->swap(*other);
}

//  void QQmlComponentPrivate::ConstructionState::ensureRequiredPropertyStora
//      ge(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState29ensureRequiredPropertyStorageEP7QObject(
    QQmlComponentPrivate::ConstructionState *self,
    QObject *target) {
  self->ensureRequiredPropertyStorage(target);
}

//  RequiredProperties
//      *QQmlComponentPrivate::ConstructionState::requiredProperties() const
extern "C" Q_DECL_EXPORT
RequiredProperties *ritual_ZNK20QQmlComponentPrivate17ConstructionState18requiredPropertiesEv(
    const QQmlComponentPrivate::ConstructionState *self) {
  return self->requiredProperties();
}

//  void
//      QQmlComponentPrivate::ConstructionState::addPendingRequiredProperty(c
//      onst QObject *object, const QQmlPropertyData *propData, const
//      RequiredPropertyInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState26addPendingRequiredPropertyEPK7QObjectPK16QQmlPropertyDataRK20RequiredPropertyInfo(
    QQmlComponentPrivate::ConstructionState *self,
    const QObject *object,
    const QQmlPropertyData *propData,
    const RequiredPropertyInfo *info) {
  self->addPendingRequiredProperty(object, propData, *info);
}

//  bool
//      QQmlComponentPrivate::ConstructionState::hasUnsetRequiredProperties()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlComponentPrivate17ConstructionState26hasUnsetRequiredPropertiesEv(
    const QQmlComponentPrivate::ConstructionState *self) {
  return self->hasUnsetRequiredProperties();
}

//  void QQmlComponentPrivate::ConstructionState::clearRequiredProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState23clearRequiredPropertiesEv(
    QQmlComponentPrivate::ConstructionState *self) {
  self->clearRequiredProperties();
}

//  void QQmlComponentPrivate::ConstructionState::appendErrors(const
//      QList<QQmlError> &qmlErrors)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState12appendErrorsERK5QListI9QQmlErrorE(
    QQmlComponentPrivate::ConstructionState *self,
    const QList<QQmlError> *qmlErrors) {
  self->appendErrors(*qmlErrors);
}

//  void QQmlComponentPrivate::ConstructionState::appendCreatorErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState19appendCreatorErrorsEv(
    QQmlComponentPrivate::ConstructionState *self) {
  self->appendCreatorErrors();
}

//  QQmlObjectCreator *QQmlComponentPrivate::ConstructionState::creator()
extern "C" Q_DECL_EXPORT
QQmlObjectCreator *ritual_ZN20QQmlComponentPrivate17ConstructionState7creatorEv(
    QQmlComponentPrivate::ConstructionState *self) {
  return self->creator();
}

//  const QQmlObjectCreator
//      *QQmlComponentPrivate::ConstructionState::creator() const
extern "C" Q_DECL_EXPORT
const QQmlObjectCreator *ritual_ZNK20QQmlComponentPrivate17ConstructionState7creatorEv(
    const QQmlComponentPrivate::ConstructionState *self) {
  return self->creator();
}

//  void QQmlComponentPrivate::ConstructionState::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState5clearEv(
    QQmlComponentPrivate::ConstructionState *self) {
  self->clear();
}

//  bool QQmlComponentPrivate::ConstructionState::hasCreator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlComponentPrivate17ConstructionState10hasCreatorEv(
    const QQmlComponentPrivate::ConstructionState *self) {
  return self->hasCreator();
}

//  QQmlObjectCreator
//      *QQmlComponentPrivate::ConstructionState::initCreator(const
//      QQmlRefPointer<QQmlContextData> &parentContext, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QQmlRefPointer<QQmlContextData> &creationContext, const QString
//      &inlineComponentName)
extern "C" Q_DECL_EXPORT
QQmlObjectCreator *ritual_ZN20QQmlComponentPrivate17ConstructionState11initCreatorERK14QQmlRefPointerI15QQmlContextDataERKS1_IN3QV425ExecutableCompilationUnitEES5_RK7QString(
    QQmlComponentPrivate::ConstructionState *self,
    const QQmlRefPointer<QQmlContextData> *parentContext,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QQmlRefPointer<QQmlContextData> *creationContext,
    const QString *inlineComponentName) {
  return self->initCreator(
      *parentContext,
      *compilationUnit,
      *creationContext,
      *inlineComponentName);
}

//  bool QQmlComponentPrivate::ConstructionState::isCompletePending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlComponentPrivate17ConstructionState17isCompletePendingEv(
    const QQmlComponentPrivate::ConstructionState *self) {
  return self->isCompletePending();
}

//  void QQmlComponentPrivate::ConstructionState::setCompletePending(bool
//      isPending)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate17ConstructionState18setCompletePendingEb(
    QQmlComponentPrivate::ConstructionState *self,
    bool isPending) {
  self->setCompletePending(isPending);
}

//  QObject *QQmlComponentPrivate::ConstructionState::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QQmlComponentPrivate17ConstructionState6targetEv(
    const QQmlComponentPrivate::ConstructionState *self) {
  return self->target();
}
