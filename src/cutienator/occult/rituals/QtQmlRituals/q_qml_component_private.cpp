//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlcomponent.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcomponent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/qqmlerror.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlproperty.h>
#include <QtCore/qvariant.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QQmlComponent *QQmlComponentPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN20QQmlComponentPrivate6q_funcEv(
    QQmlComponentPrivate *self) {
  return self->q_func();
}

//  const QQmlComponent *QQmlComponentPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlComponent *ritual_ZNK20QQmlComponentPrivate6q_funcEv(
    const QQmlComponentPrivate *self) {
  return self->q_func();
}

//  void QQmlComponentPrivate::loadUrl(const QUrl &newUrl,
//      QQmlComponent::CompilationMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate7loadUrlERK4QUrlN13QQmlComponent15CompilationModeE(
    QQmlComponentPrivate *self,
    const QUrl *newUrl,
    QQmlComponent::CompilationMode mode) {
  self->loadUrl(*newUrl, mode);
}

//  QQmlType QQmlComponentPrivate::loadedType() const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK20QQmlComponentPrivate10loadedTypeEv(
    const QQmlComponentPrivate *self) {
  return new QQmlType(self->loadedType());
}

//  QObject
//      *QQmlComponentPrivate::beginCreate(QQmlRefPointer<QQmlContextData>
//      a0)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN20QQmlComponentPrivate11beginCreateE14QQmlRefPointerI15QQmlContextDataE(
    QQmlComponentPrivate *self,
    const QQmlRefPointer<QQmlContextData> *a0) {
  return self->beginCreate(*a0);
}

//  void QQmlComponentPrivate::completeCreate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate14completeCreateEv(
    QQmlComponentPrivate *self) {
  self->completeCreate();
}

//  void QQmlComponentPrivate::initializeObjectWithInitialProperties(QV4::Qml
//      Context *qmlContext, const QV4::Value &valuemap, QObject *toCreate,
//      RequiredProperties *requiredProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate37initializeObjectWithInitialPropertiesEPN3QV410QmlContextERKNS0_5ValueEP7QObjectP18RequiredProperties(
    QQmlComponentPrivate *self,
    QV4::QmlContext *qmlContext,
    const QV4::Value *valuemap,
    QObject *toCreate,
    RequiredProperties *requiredProperties) {
  self->initializeObjectWithInitialProperties(
      qmlContext,
      *valuemap,
      toCreate,
      requiredProperties);
}

//  void QQmlComponentPrivate::setInitialProperties(QV4::ExecutionEngine
//      *engine, QV4::QmlContext *qmlContext, const QV4::Value &o, const
//      QV4::Value &v, RequiredProperties *requiredProperties, QObject
//      *createdComponent, const QQmlObjectCreator *creator)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate20setInitialPropertiesEPN3QV415ExecutionEngineEPNS0_10QmlContextERKNS0_5ValueES7_P18RequiredPropertiesP7QObjectPK17QQmlObjectCreator(
    QV4::ExecutionEngine *engine,
    QV4::QmlContext *qmlContext,
    const QV4::Value *o,
    const QV4::Value *v,
    RequiredProperties *requiredProperties,
    QObject *createdComponent,
    const QQmlObjectCreator *creator) {
  QQmlComponentPrivate::setInitialProperties(
      engine,
      qmlContext,
      *o,
      *v,
      requiredProperties,
      createdComponent,
      creator);
}

//  QQmlError QQmlComponentPrivate::unsetRequiredPropertyToQQmlError(const
//      RequiredPropertyInfo &unsetRequiredProperty)
extern "C" Q_DECL_EXPORT
QQmlError *ritual_ZN20QQmlComponentPrivate32unsetRequiredPropertyToQQmlErrorERK20RequiredPropertyInfo(
    const RequiredPropertyInfo *unsetRequiredProperty) {
  return new QQmlError(
      QQmlComponentPrivate::unsetRequiredPropertyToQQmlError(
          *unsetRequiredProperty));
}

//  void QQmlComponentPrivate::incubateObject(QQmlIncubator *incubationTask,
//      QQmlComponent *component, QQmlEngine *engine, const
//      QQmlRefPointer<QQmlContextData> &context, const
//      QQmlRefPointer<QQmlContextData> &forContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate14incubateObjectEP13QQmlIncubatorP13QQmlComponentP10QQmlEngineRK14QQmlRefPointerI15QQmlContextDataESA_(
    QQmlComponentPrivate *self,
    QQmlIncubator *incubationTask,
    QQmlComponent *component,
    QQmlEngine *engine,
    const QQmlRefPointer<QQmlContextData> *context,
    const QQmlRefPointer<QQmlContextData> *forContext) {
  self->incubateObject(
      incubationTask,
      component,
      engine,
      *context,
      *forContext);
}

//  void QQmlComponentPrivate::ready(QQmlNotifyingBlob *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate5readyEP17QQmlNotifyingBlob(
    QQmlComponentPrivate *self,
    QQmlNotifyingBlob *a0) {
  self->ready(a0);
}

//  void QQmlComponentPrivate::progress(QQmlNotifyingBlob *a0, qreal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate8progressEP17QQmlNotifyingBlobd(
    QQmlComponentPrivate *self,
    QQmlNotifyingBlob *a0,
    qreal a1) {
  self->progress(a0, a1);
}

//  void QQmlComponentPrivate::fromTypeData(const
//      QQmlRefPointer<QQmlTypeData> &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate12fromTypeDataERK14QQmlRefPointerI12QQmlTypeDataE(
    QQmlComponentPrivate *self,
    const QQmlRefPointer<QQmlTypeData> *data) {
  self->fromTypeData(*data);
}

//  bool QQmlComponentPrivate::hadTopLevelRequiredProperties() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlComponentPrivate29hadTopLevelRequiredPropertiesEv(
    const QQmlComponentPrivate *self) {
  return self->hadTopLevelRequiredProperties();
}

//  void QQmlComponentPrivate::beginDeferred(QQmlEnginePrivate *enginePriv,
//      QObject *object, DeferredState *deferredState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate13beginDeferredEP17QQmlEnginePrivateP7QObjectPSt6vectorINS_17ConstructionStateESaIS5_EE(
    QQmlEnginePrivate *enginePriv,
    QObject *object,
    QQmlComponentPrivate::DeferredState *deferredState) {
  QQmlComponentPrivate::beginDeferred(enginePriv, object, deferredState);
}

//  void QQmlComponentPrivate::completeDeferred(QQmlEnginePrivate
//      *enginePriv, DeferredState *deferredState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate16completeDeferredEP17QQmlEnginePrivatePSt6vectorINS_17ConstructionStateESaIS3_EE(
    QQmlEnginePrivate *enginePriv,
    QQmlComponentPrivate::DeferredState *deferredState) {
  QQmlComponentPrivate::completeDeferred(enginePriv, deferredState);
}

//  void QQmlComponentPrivate::complete(QQmlEnginePrivate *enginePriv,
//      ConstructionState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate8completeEP17QQmlEnginePrivatePNS_17ConstructionStateE(
    QQmlEnginePrivate *enginePriv,
    QQmlComponentPrivate::ConstructionState *state) {
  QQmlComponentPrivate::complete(enginePriv, state);
}

//  QQmlProperty QQmlComponentPrivate::removePropertyFromRequired(QObject
//      *target, const QString &name, RequiredProperties *requiredProperties,
//      QQmlEngine *engine, bool *wasInRequiredProperties)
extern "C" Q_DECL_EXPORT
QQmlProperty *ritual_ZN20QQmlComponentPrivate26removePropertyFromRequiredEP7QObjectRK7QStringP18RequiredPropertiesP10QQmlEnginePb(
    QObject *target,
    const QString *name,
    RequiredProperties *requiredProperties,
    QQmlEngine *engine,
    bool *wasInRequiredProperties) {
  return new QQmlProperty(
      QQmlComponentPrivate::removePropertyFromRequired(
          target,
          *name,
          requiredProperties,
          engine,
          wasInRequiredProperties));
}

//  void QQmlComponentPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate5clearEv(QQmlComponentPrivate *self) {
  self->clear();
}

//  QQmlComponentPrivate *QQmlComponentPrivate::get(QQmlComponent *c)
extern "C" Q_DECL_EXPORT
QQmlComponentPrivate *ritual_ZN20QQmlComponentPrivate3getEP13QQmlComponent(
    QQmlComponent *c) {
  return QQmlComponentPrivate::get(c);
}

//  QObject *QQmlComponentPrivate::doBeginCreate(QQmlComponent *q,
//      QQmlContext *context)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN20QQmlComponentPrivate13doBeginCreateEP13QQmlComponentP11QQmlContext(
    QQmlComponentPrivate *self,
    QQmlComponent *q,
    QQmlContext *context) {
  return self->doBeginCreate(q, context);
}

//  bool QQmlComponentPrivate::setInitialProperties(QObject *object, const
//      QVariantMap &properties)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlComponentPrivate20setInitialPropertiesEP7QObjectRK4QMapI7QString8QVariantE(
    QQmlComponentPrivate *self,
    QObject *object,
    const QMap<QString, QVariant> *properties) {
  return self->setInitialProperties(object, *properties);
}

//  bool QQmlComponentPrivate::setInitialProperty(QObject *component, const
//      QString &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlComponentPrivate18setInitialPropertyEP7QObjectRK7QStringRK8QVariant(
    QQmlComponentPrivate *self,
    QObject *component,
    const QString *name,
    const QVariant *value) {
  return self->setInitialProperty(component, *name, *value);
}

//  QObject *QQmlComponentPrivate::createWithProperties(QObject *parent,
//      const QVariantMap &properties, QQmlContext *context, CreateBehavior
//      behavior)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN20QQmlComponentPrivate20createWithPropertiesEP7QObjectRK4QMapI7QString8QVariantEP11QQmlContextNS_14CreateBehaviorE(
    QQmlComponentPrivate *self,
    QObject *parent,
    const QMap<QString, QVariant> *properties,
    QQmlContext *context,
    QQmlComponentPrivate::CreateBehavior behavior) {
  return self->createWithProperties(parent, *properties, context, behavior);
}

//  bool QQmlComponentPrivate::isBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlComponentPrivate7isBoundEv(
    const QQmlComponentPrivate *self) {
  return self->isBound();
}

//  void QQmlComponentPrivate::prepareLoadFromModule(QAnyStringView uri,
//      QAnyStringView typeName, QQmlTypeLoader::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate21prepareLoadFromModuleE14QAnyStringViewS0_N14QQmlTypeLoader4ModeE(
    QQmlComponentPrivate *self,
    const QString *uri,
    const QString *typeName,
    QQmlTypeLoader::Mode mode) {
  self->prepareLoadFromModule(
      QAnyStringView(*uri),
      QAnyStringView(*typeName),
      mode);
}

//  void QQmlComponentPrivate::completeLoadFromModule(QAnyStringView uri,
//      QAnyStringView typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate22completeLoadFromModuleE14QAnyStringViewS0_(
    QQmlComponentPrivate *self,
    const QString *uri,
    const QString *typeName) {
  self->completeLoadFromModule(
      QAnyStringView(*uri),
      QAnyStringView(*typeName));
}

//  void QQmlComponentPrivate::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate11setProgressEd(
    QQmlComponentPrivate *self,
    qreal progress) {
  self->setProgress(progress);
}

//  void
//      QQmlComponentPrivate::setCreationContext(QQmlRefPointer<QQmlContextDa
//      ta> creationContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate18setCreationContextE14QQmlRefPointerI15QQmlContextDataE(
    QQmlComponentPrivate *self,
    const QQmlRefPointer<QQmlContextData> *creationContext) {
  self->setCreationContext(*creationContext);
}

//  QQmlType QQmlComponentPrivate::loadHelperType() const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK20QQmlComponentPrivate14loadHelperTypeEv(
    const QQmlComponentPrivate *self) {
  return new QQmlType(self->loadHelperType());
}

//  bool QQmlComponentPrivate::hasUnsetRequiredProperties() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlComponentPrivate26hasUnsetRequiredPropertiesEv(
    const QQmlComponentPrivate *self) {
  return self->hasUnsetRequiredProperties();
}

//  RequiredProperties *QQmlComponentPrivate::requiredProperties() const
extern "C" Q_DECL_EXPORT
RequiredProperties *ritual_ZNK20QQmlComponentPrivate18requiredPropertiesEv(
    const QQmlComponentPrivate *self) {
  return self->requiredProperties();
}

//  const QQmlObjectCreator *QQmlComponentPrivate::creator() const
extern "C" Q_DECL_EXPORT
const QQmlObjectCreator *ritual_ZNK20QQmlComponentPrivate7creatorEv(
    const QQmlComponentPrivate *self) {
  return self->creator();
}

//  QQmlEngine *QQmlComponentPrivate::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK20QQmlComponentPrivate6engineEv(
    const QQmlComponentPrivate *self) {
  return self->engine();
}

//  QQmlRefPointer<QV4::ExecutableCompilationUnit>
//      QQmlComponentPrivate::compilationUnit() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZNK20QQmlComponentPrivate15compilationUnitEv(
    const QQmlComponentPrivate *self) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      self->compilationUnit());
}

//  void QQmlComponentPrivate::setCompilationUnit(const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate18setCompilationUnitERK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEE(
    QQmlComponentPrivate *self,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *unit) {
  self->setCompilationUnit(*unit);
}

//  void QQmlComponentPrivate::setData(const QByteArray &data, const QUrl
//      &url, QQmlComponent::CompilationMode compilationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlComponentPrivate7setDataERK10QByteArrayRK4QUrlN13QQmlComponent15CompilationModeE(
    QQmlComponentPrivate *self,
    const QByteArray *data,
    const QUrl *url,
    QQmlComponent::CompilationMode compilationMode) {
  self->setData(*data, *url, compilationMode);
}

//  QQmlComponentPrivate as the QQmlNotifyingBlob::Callback it is built on
extern "C" Q_DECL_EXPORT
QQmlNotifyingBlob::Callback *ritual_cast_QQmlComponentPrivate_QQmlNotifyingBlob_Callback(
    QQmlComponentPrivate *self) {
  return static_cast<QQmlNotifyingBlob::Callback *>(self);
}

//  a QQmlRefPointer<QV4::ExecutableCompilationUnit> a ritual of
//      QQmlComponentPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlComponentPrivate__QQmlRefPointer_QV4_ExecutableCompilationUnit(
    QQmlRefPointer<QV4::ExecutableCompilationUnit> *self) {
  delete self;
}
