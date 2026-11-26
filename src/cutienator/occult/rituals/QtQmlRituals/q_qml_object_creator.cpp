//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/qqmlproperty.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QString QQmlObjectCreator::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlObjectCreator2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQmlObjectCreator::tr(sourceText, disambiguation, n));
}

//  QQmlObjectCreator::QQmlObjectCreator(const
//      QQmlRefPointer<QQmlContextData> &parentContext, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QQmlRefPointer<QQmlContextData> &creationContext, const QString
//      &inlineComponentName, QQmlIncubatorPrivate *incubator)
extern "C" Q_DECL_EXPORT
QQmlObjectCreator *ritual_ZN17QQmlObjectCreatorC1ERK14QQmlRefPointerI15QQmlContextDataERKS0_IN3QV425ExecutableCompilationUnitEES4_RK7QStringP20QQmlIncubatorPrivate(
    const QQmlRefPointer<QQmlContextData> *parentContext,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QQmlRefPointer<QQmlContextData> *creationContext,
    const QString *inlineComponentName,
    QQmlIncubatorPrivate *incubator) {
  return new QQmlObjectCreator(
      *parentContext,
      *compilationUnit,
      *creationContext,
      *inlineComponentName,
      incubator);
}

//  QQmlObjectCreator::~QQmlObjectCreator()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreatorD1Ev(QQmlObjectCreator *self) {
  delete self;
}

//  QObject *QQmlObjectCreator::create(int subComponentIndex, QObject
//      *parent, QQmlInstantiationInterrupt *interrupt, int flags)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator6createEiP7QObjectP26QQmlInstantiationInterrupti(
    QQmlObjectCreator *self,
    int subComponentIndex,
    QObject *parent,
    QQmlInstantiationInterrupt *interrupt,
    int flags) {
  return self->create(subComponentIndex, parent, interrupt, flags);
}

//  bool QQmlObjectCreator::populateDeferredProperties(QObject *instance,
//      const QQmlData::DeferredData *deferredData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlObjectCreator26populateDeferredPropertiesEP7QObjectPKN8QQmlData12DeferredDataE(
    QQmlObjectCreator *self,
    QObject *instance,
    const QQmlData::DeferredData *deferredData) {
  return self->populateDeferredProperties(instance, deferredData);
}

//  void QQmlObjectCreator::beginPopulateDeferred(const
//      QQmlRefPointer<QQmlContextData> &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator21beginPopulateDeferredERK14QQmlRefPointerI15QQmlContextDataE(
    QQmlObjectCreator *self,
    const QQmlRefPointer<QQmlContextData> *context) {
  self->beginPopulateDeferred(*context);
}

//  void QQmlObjectCreator::populateDeferredBinding(const QQmlProperty
//      &qmlProperty, int deferredIndex, const QV4::CompiledData::Binding
//      *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator23populateDeferredBindingERK12QQmlPropertyiPKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    const QQmlProperty *qmlProperty,
    int deferredIndex,
    const QV4::CompiledData::Binding *binding) {
  self->populateDeferredBinding(*qmlProperty, deferredIndex, binding);
}

//  void QQmlObjectCreator::populateDeferredInstance(QObject *outerObject,
//      int deferredIndex, int index, QObject *instance, QObject
//      *bindingTarget, const QQmlPropertyData *valueTypeProperty, const
//      QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator24populateDeferredInstanceEP7QObjectiiS1_S1_PK16QQmlPropertyDataPKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    QObject *outerObject,
    int deferredIndex,
    int index,
    QObject *instance,
    QObject *bindingTarget,
    const QQmlPropertyData *valueTypeProperty,
    const QV4::CompiledData::Binding *binding) {
  self->populateDeferredInstance(
      outerObject,
      deferredIndex,
      index,
      instance,
      bindingTarget,
      valueTypeProperty,
      binding);
}

//  void QQmlObjectCreator::finalizePopulateDeferred()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator24finalizePopulateDeferredEv(
    QQmlObjectCreator *self) {
  self->finalizePopulateDeferred();
}

//  bool QQmlObjectCreator::finalize(QQmlInstantiationInterrupt &interrupt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlObjectCreator8finalizeER26QQmlInstantiationInterrupt(
    QQmlObjectCreator *self,
    QQmlInstantiationInterrupt *interrupt) {
  return self->finalize(*interrupt);
}

//  void QQmlObjectCreator::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator5clearEv(QQmlObjectCreator *self) {
  self->clear();
}

//  QObject *QQmlObjectCreator::createObjectInContext(int objectIndex,
//      QObject *parent, const QQmlRefPointer<QQmlContextData>
//      &existingContext)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator21createObjectInContextEiP7QObjectRK14QQmlRefPointerI15QQmlContextDataE(
    QQmlObjectCreator *self,
    int objectIndex,
    QObject *parent,
    const QQmlRefPointer<QQmlContextData> *existingContext) {
  return self->createObjectInContext(objectIndex, parent, *existingContext);
}

//  QQmlRefPointer<QQmlContextData> QQmlObjectCreator::rootContext() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZNK17QQmlObjectCreator11rootContextEv(
    const QQmlObjectCreator *self) {
  return new QQmlRefPointer<QQmlContextData>(self->rootContext());
}

//  QQmlComponentAttached **QQmlObjectCreator::componentAttachment()
extern "C" Q_DECL_EXPORT
QQmlComponentAttached **ritual_ZN17QQmlObjectCreator19componentAttachmentEv(
    QQmlObjectCreator *self) {
  return self->componentAttachment();
}

//  QQmlRefPointer<QQmlContextData> QQmlObjectCreator::parentContextData()
//      const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZNK17QQmlObjectCreator17parentContextDataEv(
    const QQmlObjectCreator *self) {
  return new QQmlRefPointer<QQmlContextData>(self->parentContextData());
}

//  std::vector<QQmlGuard<QObject>> &QQmlObjectCreator::allCreatedObjects()
extern "C" Q_DECL_EXPORT
std::vector<QQmlGuard<QObject>> *ritual_ZN17QQmlObjectCreator17allCreatedObjectsEv(
    QQmlObjectCreator *self) {
  return &(self->allCreatedObjects());
}

//  RequiredProperties *QQmlObjectCreator::requiredProperties()
extern "C" Q_DECL_EXPORT
RequiredProperties *ritual_ZN17QQmlObjectCreator18requiredPropertiesEv(
    QQmlObjectCreator *self) {
  return self->requiredProperties();
}

//  bool QQmlObjectCreator::componentHadTopLevelRequiredProperties() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlObjectCreator38componentHadTopLevelRequiredPropertiesEv(
    const QQmlObjectCreator *self) {
  return self->componentHadTopLevelRequiredProperties();
}

//  QQmlComponent *QQmlObjectCreator::createComponent(QQmlEngine *engine,
//      QV4::ExecutableCompilationUnit *compilationUnit, int index, QObject
//      *parent, const QQmlRefPointer<QQmlContextData> &context)
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZN17QQmlObjectCreator15createComponentEP10QQmlEnginePN3QV425ExecutableCompilationUnitEiP7QObjectRK14QQmlRefPointerI15QQmlContextDataE(
    QQmlEngine *engine,
    QV4::ExecutableCompilationUnit *compilationUnit,
    int index,
    QObject *parent,
    const QQmlRefPointer<QQmlContextData> *context) {
  return QQmlObjectCreator::createComponent(
      engine,
      compilationUnit,
      index,
      parent,
      *context);
}

//  void QQmlObjectCreator::removePendingBinding(QObject *target, int
//      propertyIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQmlObjectCreator20removePendingBindingEP7QObjecti(
    const QQmlObjectCreator *self,
    QObject *target,
    int propertyIndex) {
  self->removePendingBinding(target, propertyIndex);
}

//  void QQmlObjectCreator::repopulateBindings(int index, QObject *instance,
//      const QQmlRefPointer<QQmlContextData> &instanceContext, InitFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator18repopulateBindingsEiP7QObjectRK14QQmlRefPointerI15QQmlContextDataE6QFlagsINS_8InitFlagEE(
    QQmlObjectCreator *self,
    int index,
    QObject *instance,
    const QQmlRefPointer<QQmlContextData> *instanceContext,
    int flags) {
  self->repopulateBindings(
      index,
      instance,
      *instanceContext,
      QFlags<QQmlObjectCreator::InitFlag>::fromInt(flags));
}

//  QQmlObjectCreator::QQmlObjectCreator(const
//      QQmlRefPointer<QQmlContextData> &contextData, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit,
//      const QString inlineComponentName, QQmlObjectCreatorSharedState
//      *inheritedSharedState, bool isContextObject)
extern "C" Q_DECL_EXPORT
QQmlObjectCreator *ritual_ZN17QQmlObjectCreatorC1ERK14QQmlRefPointerI15QQmlContextDataERKS0_IN3QV425ExecutableCompilationUnitEE7QStringP28QQmlObjectCreatorSharedStateb(
    const QQmlRefPointer<QQmlContextData> *contextData,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit,
    const QString *inlineComponentName,
    QQmlObjectCreatorSharedState *inheritedSharedState,
    bool isContextObject) {
  return new QQmlObjectCreator(
      *contextData,
      *compilationUnit,
      *inlineComponentName,
      inheritedSharedState,
      isContextObject);
}

//  void QQmlObjectCreator::init(const QQmlRefPointer<QQmlContextData>
//      &parentContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator4initERK14QQmlRefPointerI15QQmlContextDataE(
    QQmlObjectCreator *self,
    const QQmlRefPointer<QQmlContextData> *parentContext) {
  self->init(*parentContext);
}

//  void QQmlObjectCreator::initializeDData(const QV4::CompiledData::Object
//      *obj, QObject *instance, QQmlData *ddata, InitFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator15initializeDDataEPKN3QV412CompiledData6ObjectEP7QObjectP8QQmlData6QFlagsINS_8InitFlagEE(
    QQmlObjectCreator *self,
    const QV4::CompiledData::Object *obj,
    QObject *instance,
    QQmlData *ddata,
    int flags) {
  self->initializeDData(
      obj,
      instance,
      ddata,
      QFlags<QQmlObjectCreator::InitFlag>::fromInt(flags));
}

//  void QQmlObjectCreator::initializePropertyCache(int index, QQmlData
//      *ddata, const QV4::ResolvedTypeReference *typeRef)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator23initializePropertyCacheEiP8QQmlDataPKN3QV421ResolvedTypeReferenceE(
    QQmlObjectCreator *self,
    int index,
    QQmlData *ddata,
    const QV4::ResolvedTypeReference *typeRef) {
  self->initializePropertyCache(index, ddata, typeRef);
}

//  void QQmlObjectCreator::initializeParent(QObject *instance, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator16initializeParentEP7QObjectS1_(
    QQmlObjectCreator *self,
    QObject *instance,
    QObject *parent) {
  self->initializeParent(instance, parent);
}

//  QObject *QQmlObjectCreator::populateInstanceAndAliasBindings(int index,
//      QObject *instance, InitFlags flags)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator32populateInstanceAndAliasBindingsEiP7QObject6QFlagsINS_8InitFlagEE(
    QQmlObjectCreator *self,
    int index,
    QObject *instance,
    int flags) {
  return self->populateInstanceAndAliasBindings(
      index,
      instance,
      QFlags<QQmlObjectCreator::InitFlag>::fromInt(flags));
}

//  QObject *QQmlObjectCreator::createInstance(int index, QObject *parent,
//      bool isContextObject)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator14createInstanceEiP7QObjectb(
    QQmlObjectCreator *self,
    int index,
    QObject *parent,
    bool isContextObject) {
  return self->createInstance(index, parent, isContextObject);
}

//  QObject *QQmlObjectCreator::initializeComponent(const
//      QV4::CompiledData::Object *obj, QObject *instance, InitFlags flags)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator19initializeComponentEPKN3QV412CompiledData6ObjectEP7QObject6QFlagsINS_8InitFlagEE(
    QQmlObjectCreator *self,
    const QV4::CompiledData::Object *obj,
    QObject *instance,
    int flags) {
  return self->initializeComponent(
      obj,
      instance,
      QFlags<QQmlObjectCreator::InitFlag>::fromInt(flags));
}

//  QObject *QQmlObjectCreator::initializeComposite(int index, const
//      QV4::CompiledData::Object *obj, const QV4::ResolvedTypeReference
//      *typeRef, QObject *instance, QObject *parent, InitFlags flags)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator19initializeCompositeEiPKN3QV412CompiledData6ObjectEPKNS0_21ResolvedTypeReferenceEP7QObjectS9_6QFlagsINS_8InitFlagEE(
    QQmlObjectCreator *self,
    int index,
    const QV4::CompiledData::Object *obj,
    const QV4::ResolvedTypeReference *typeRef,
    QObject *instance,
    QObject *parent,
    int flags) {
  return self->initializeComposite(
      index,
      obj,
      typeRef,
      instance,
      parent,
      QFlags<QQmlObjectCreator::InitFlag>::fromInt(flags));
}

//  QObject *QQmlObjectCreator::initializeNonComposite(int index, const
//      QV4::CompiledData::Object *obj, const QV4::ResolvedTypeReference
//      *typeRef, QObject *instance, QObject *parent, InitFlags flags)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQmlObjectCreator22initializeNonCompositeEiPKN3QV412CompiledData6ObjectEPKNS0_21ResolvedTypeReferenceEP7QObjectS9_6QFlagsINS_8InitFlagEE(
    QQmlObjectCreator *self,
    int index,
    const QV4::CompiledData::Object *obj,
    const QV4::ResolvedTypeReference *typeRef,
    QObject *instance,
    QObject *parent,
    int flags) {
  return self->initializeNonComposite(
      index,
      obj,
      typeRef,
      instance,
      parent,
      QFlags<QQmlObjectCreator::InitFlag>::fromInt(flags));
}

//  bool QQmlObjectCreator::populateInstance(int index, QObject *instance,
//      QObject *bindingTarget, const QQmlPropertyData *valueTypeProperty,
//      const QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlObjectCreator16populateInstanceEiP7QObjectS1_PK16QQmlPropertyDataPKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    int index,
    QObject *instance,
    QObject *bindingTarget,
    const QQmlPropertyData *valueTypeProperty,
    const QV4::CompiledData::Binding *binding) {
  return self->populateInstance(
      index,
      instance,
      bindingTarget,
      valueTypeProperty,
      binding);
}

//  void QQmlObjectCreator::populateDeferred(QObject *instance, int
//      deferredIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator16populateDeferredEP7QObjecti(
    QQmlObjectCreator *self,
    QObject *instance,
    int deferredIndex) {
  self->populateDeferred(instance, deferredIndex);
}

//  void QQmlObjectCreator::populateDeferred(QObject *instance, int
//      deferredIndex, const QQmlPropertyPrivate *qmlProperty, const
//      QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator16populateDeferredEP7QObjectiPK19QQmlPropertyPrivatePKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    QObject *instance,
    int deferredIndex,
    const QQmlPropertyPrivate *qmlProperty,
    const QV4::CompiledData::Binding *binding) {
  self->populateDeferred(instance, deferredIndex, qmlProperty, binding);
}

//  void QQmlObjectCreator::setupBindings(BindingSetupFlags mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator13setupBindingsE6QFlagsINS_11BindingModeEE(
    QQmlObjectCreator *self,
    int mode) {
  self->setupBindings(QFlags<QQmlObjectCreator::BindingMode>::fromInt(mode));
}

//  bool QQmlObjectCreator::setPropertyBinding(const QQmlPropertyData
//      *property, const QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlObjectCreator18setPropertyBindingEPK16QQmlPropertyDataPKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    const QQmlPropertyData *property,
    const QV4::CompiledData::Binding *binding) {
  return self->setPropertyBinding(property, binding);
}

//  void QQmlObjectCreator::setPropertyValue(const QQmlPropertyData
//      *property, const QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator16setPropertyValueEPK16QQmlPropertyDataPKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    const QQmlPropertyData *property,
    const QV4::CompiledData::Binding *binding) {
  self->setPropertyValue(property, binding);
}

//  void QQmlObjectCreator::setupFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator14setupFunctionsEv(
    QQmlObjectCreator *self) {
  self->setupFunctions();
}

//  QString QQmlObjectCreator::stringAt(int idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlObjectCreator8stringAtEi(
    const QQmlObjectCreator *self,
    int idx) {
  return new QString(self->stringAt(idx));
}

//  void QQmlObjectCreator::recordError(const QV4::CompiledData::Location
//      &location, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator11recordErrorERKN3QV412CompiledData8LocationERK7QString(
    QQmlObjectCreator *self,
    const QV4::CompiledData::Location *location,
    const QString *description) {
  self->recordError(*location, *description);
}

//  void QQmlObjectCreator::registerObjectWithContextById(const
//      QV4::CompiledData::Object *object, QObject *instance) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQmlObjectCreator29registerObjectWithContextByIdEPKN3QV412CompiledData6ObjectEP7QObject(
    const QQmlObjectCreator *self,
    const QV4::CompiledData::Object *object,
    QObject *instance) {
  self->registerObjectWithContextById(object, instance);
}

//  QV4::QmlContext *QQmlObjectCreator::currentQmlContext()
extern "C" Q_DECL_EXPORT
QV4::QmlContext *ritual_ZN17QQmlObjectCreator17currentQmlContextEv(
    QQmlObjectCreator *self) {
  return self->currentQmlContext();
}

//  QV4::ResolvedTypeReference *QQmlObjectCreator::resolvedType(int id) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK17QQmlObjectCreator12resolvedTypeEi(
    const QQmlObjectCreator *self,
    int id) {
  return self->resolvedType(id);
}

//  void QQmlObjectCreator::registerPostHocRequiredProperties(const
//      QV4::CompiledData::Binding *binding)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlObjectCreator33registerPostHocRequiredPropertiesEPKN3QV412CompiledData7BindingE(
    QQmlObjectCreator *self,
    const QV4::CompiledData::Binding *binding) {
  self->registerPostHocRequiredProperties(binding);
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QQmlObjectCreator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlObjectCreator__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}
