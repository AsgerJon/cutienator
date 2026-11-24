//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcontextdata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcontextdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlContextData::addref() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlContextData6addrefEv(const QQmlContextData *self) {
  self->addref();
}

//  void QQmlContextData::release() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlContextData7releaseEv(const QQmlContextData *self) {
  self->release();
}

//  int QQmlContextData::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlContextData5countEv(const QQmlContextData *self) {
  return self->count();
}

//  int QQmlContextData::refCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlContextData8refCountEv(const QQmlContextData *self) {
  return self->refCount();
}

//  void QQmlContextData::emitDestruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData15emitDestructionEv(QQmlContextData *self) {
  self->emitDestruction();
}

//  void QQmlContextData::clearExpressions()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData16clearExpressionsEv(QQmlContextData *self) {
  self->clearExpressions();
}

//  void QQmlContextData::clearContextRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData23clearContextRecursivelyEv(
    QQmlContextData *self) {
  self->clearContextRecursively();
}

//  void QQmlContextData::clearChildrenAndSiblings()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData24clearChildrenAndSiblingsEv(
    QQmlContextData *self) {
  self->clearChildrenAndSiblings();
}

//  void QQmlContextData::clearImportedScripts()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData20clearImportedScriptsEv(
    QQmlContextData *self) {
  self->clearImportedScripts();
}

//  void QQmlContextData::clearOwnedObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData17clearOwnedObjectsEv(QQmlContextData *self) {
  self->clearOwnedObjects();
}

//  void QQmlContextData::clearContextGuards()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData18clearContextGuardsEv(
    QQmlContextData *self) {
  self->clearContextGuards();
}

//  void QQmlContextData::clearIdValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData13clearIdValuesEv(QQmlContextData *self) {
  self->clearIdValues();
}

//  void QQmlContextData::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData10invalidateEv(QQmlContextData *self) {
  self->invalidate();
}

//  bool QQmlContextData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData7isValidEv(const QQmlContextData *self) {
  return self->isValid();
}

//  bool QQmlContextData::isInternal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData10isInternalEv(const QQmlContextData *self) {
  return self->isInternal();
}

//  void QQmlContextData::setInternal(bool isInternal)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData11setInternalEb(
    QQmlContextData *self,
    bool isInternal) {
  self->setInternal(isInternal);
}

//  bool QQmlContextData::isJSContext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData11isJSContextEv(
    const QQmlContextData *self) {
  return self->isJSContext();
}

//  void QQmlContextData::setJSContext(bool isJSContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData12setJSContextEb(
    QQmlContextData *self,
    bool isJSContext) {
  self->setJSContext(isJSContext);
}

//  bool QQmlContextData::isPragmaLibraryContext() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData22isPragmaLibraryContextEv(
    const QQmlContextData *self) {
  return self->isPragmaLibraryContext();
}

//  void QQmlContextData::setPragmaLibraryContext(bool library)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData23setPragmaLibraryContextEb(
    QQmlContextData *self,
    bool library) {
  self->setPragmaLibraryContext(library);
}

//  void QQmlContextData::clearParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData11clearParentEv(QQmlContextData *self) {
  self->clearParent();
}

//  void QQmlContextData::refreshExpressions()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData18refreshExpressionsEv(
    QQmlContextData *self) {
  self->refreshExpressions();
}

//  void QQmlContextData::addOwnedObject(QQmlData *ownedObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData14addOwnedObjectEP8QQmlData(
    QQmlContextData *self,
    QQmlData *ownedObject) {
  self->addOwnedObject(ownedObject);
}

//  QQmlData *QQmlContextData::ownedObjects() const
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZNK15QQmlContextData12ownedObjectsEv(
    const QQmlContextData *self) {
  return self->ownedObjects();
}

//  void QQmlContextData::setOwnedObjects(QQmlData *ownedObjects)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData15setOwnedObjectsEP8QQmlData(
    QQmlContextData *self,
    QQmlData *ownedObjects) {
  self->setOwnedObjects(ownedObjects);
}

//  void QQmlContextData::installContext(QQmlData *ddata, QmlObjectKind kind)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData14installContextEP8QQmlDataNS_13QmlObjectKindE(
    QQmlContextData *self,
    QQmlData *ddata,
    QQmlContextData::QmlObjectKind kind) {
  self->installContext(ddata, kind);
}

//  QUrl QQmlContextData::resolvedUrl(const QUrl &a0) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QQmlContextData11resolvedUrlERK4QUrl(
    const QQmlContextData *self,
    const QUrl *a0) {
  return new QUrl(self->resolvedUrl(*a0));
}

//  QQmlContext *QQmlContextData::asQQmlContext()
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZN15QQmlContextData13asQQmlContextEv(
    QQmlContextData *self) {
  return self->asQQmlContext();
}

//  QQmlContextPrivate *QQmlContextData::asQQmlContextPrivate()
extern "C" Q_DECL_EXPORT
QQmlContextPrivate *ritual_ZN15QQmlContextData20asQQmlContextPrivateEv(
    QQmlContextData *self) {
  return self->asQQmlContextPrivate();
}

//  QObject *QQmlContextData::contextObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QQmlContextData13contextObjectEv(
    const QQmlContextData *self) {
  return self->contextObject();
}

//  void QQmlContextData::setContextObject(QObject *contextObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData16setContextObjectEP7QObject(
    QQmlContextData *self,
    QObject *contextObject) {
  self->setContextObject(contextObject);
}

//  void QQmlContextData::deepClearContextObject(QObject *contextObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData22deepClearContextObjectEP7QObject(
    QQmlContextData *self,
    QObject *contextObject) {
  self->deepClearContextObject(contextObject);
}

//  QQmlEngine *QQmlContextData::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK15QQmlContextData6engineEv(
    const QQmlContextData *self) {
  return self->engine();
}

//  void QQmlContextData::setEngine(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData9setEngineEP10QQmlEngine(
    QQmlContextData *self,
    QQmlEngine *engine) {
  self->setEngine(engine);
}

//  QQmlContext *QQmlContextData::publicContext() const
extern "C" Q_DECL_EXPORT
QQmlContext *ritual_ZNK15QQmlContextData13publicContextEv(
    const QQmlContextData *self) {
  return self->publicContext();
}

//  void QQmlContextData::clearPublicContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData18clearPublicContextEv(
    QQmlContextData *self) {
  self->clearPublicContext();
}

//  void QQmlContextData::setExpressions(QQmlJavaScriptExpression
//      *expressions)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData14setExpressionsEP24QQmlJavaScriptExpression(
    QQmlContextData *self,
    QQmlJavaScriptExpression *expressions) {
  self->setExpressions(expressions);
}

//  QQmlJavaScriptExpression *QQmlContextData::expressions() const
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpression *ritual_ZNK15QQmlContextData11expressionsEv(
    const QQmlContextData *self) {
  return self->expressions();
}

//  QQmlJavaScriptExpression *QQmlContextData::takeExpressions()
extern "C" Q_DECL_EXPORT
QQmlJavaScriptExpression *ritual_ZN15QQmlContextData15takeExpressionsEv(
    QQmlContextData *self) {
  return self->takeExpressions();
}

//  int QQmlContextData::numIdValues() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlContextData11numIdValuesEv(const QQmlContextData *self) {
  return self->numIdValues();
}

//  void QQmlContextData::setIdValue(int index, QObject *idValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData10setIdValueEiP7QObject(
    QQmlContextData *self,
    int index,
    QObject *idValue) {
  self->setIdValue(index, idValue);
}

//  bool QQmlContextData::isIdValueSet(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData12isIdValueSetEi(
    const QQmlContextData *self,
    int index) {
  return self->isIdValueSet(index);
}

//  QQmlNotifier *QQmlContextData::idValueBindings(int index) const
extern "C" Q_DECL_EXPORT
QQmlNotifier *ritual_ZNK15QQmlContextData15idValueBindingsEi(
    const QQmlContextData *self,
    int index) {
  return self->idValueBindings(index);
}

//  QObject *QQmlContextData::idValue(int index) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QQmlContextData7idValueEi(
    const QQmlContextData *self,
    int index) {
  return self->idValue(index);
}

//  QString QQmlContextData::findObjectId(const QObject *obj) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlContextData12findObjectIdEPK7QObject(
    const QQmlContextData *self,
    const QObject *obj) {
  return new QString(self->findObjectId(obj));
}

//  QUrl QQmlContextData::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QQmlContextData3urlEv(const QQmlContextData *self) {
  return new QUrl(self->url());
}

//  QString QQmlContextData::urlString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlContextData9urlStringEv(
    const QQmlContextData *self) {
  return new QString(self->urlString());
}

//  void QQmlContextData::setBaseUrlString(const QString &baseUrlString)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData16setBaseUrlStringERK7QString(
    QQmlContextData *self,
    const QString *baseUrlString) {
  self->setBaseUrlString(*baseUrlString);
}

//  QString QQmlContextData::baseUrlString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlContextData13baseUrlStringEv(
    const QQmlContextData *self) {
  return new QString(self->baseUrlString());
}

//  void QQmlContextData::setBaseUrl(const QUrl &baseUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData10setBaseUrlERK4QUrl(
    QQmlContextData *self,
    const QUrl *baseUrl) {
  self->setBaseUrl(*baseUrl);
}

//  QUrl QQmlContextData::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QQmlContextData7baseUrlEv(const QQmlContextData *self) {
  return new QUrl(self->baseUrl());
}

//  QQmlIncubatorPrivate *QQmlContextData::incubator() const
extern "C" Q_DECL_EXPORT
QQmlIncubatorPrivate *ritual_ZNK15QQmlContextData9incubatorEv(
    const QQmlContextData *self) {
  return self->incubator();
}

//  void QQmlContextData::setIncubator(QQmlIncubatorPrivate *incubator)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData12setIncubatorEP20QQmlIncubatorPrivate(
    QQmlContextData *self,
    QQmlIncubatorPrivate *incubator) {
  self->setIncubator(incubator);
}

//  QObject *QQmlContextData::extraObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QQmlContextData11extraObjectEv(
    const QQmlContextData *self) {
  return self->extraObject();
}

//  void QQmlContextData::setExtraObject(QObject *extraObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData14setExtraObjectEP7QObject(
    QQmlContextData *self,
    QObject *extraObject) {
  self->setExtraObject(extraObject);
}

//  bool QQmlContextData::isRootObjectInCreation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData22isRootObjectInCreationEv(
    const QQmlContextData *self) {
  return self->isRootObjectInCreation();
}

//  void QQmlContextData::setRootObjectInCreation(bool rootInCreation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData23setRootObjectInCreationEb(
    QQmlContextData *self,
    bool rootInCreation) {
  self->setRootObjectInCreation(rootInCreation);
}

//  QV4::ReturnedValue QQmlContextData::importedScripts() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK15QQmlContextData15importedScriptsEv(
    const QQmlContextData *self) {
  return self->importedScripts();
}

//  void QQmlContextData::setImportedScripts(QV4::ExecutionEngine *engine,
//      QV4::Value scripts)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData18setImportedScriptsEPN3QV415ExecutionEngineENS0_5ValueE(
    QQmlContextData *self,
    QV4::ExecutionEngine *engine,
    const QV4::Value *scripts) {
  self->setImportedScripts(engine, *scripts);
}

//  void QQmlContextData::setImportedScripts(QV4::ExecutionEngine *engine,
//      QV4::ReturnedValue scripts)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData18setImportedScriptsEPN3QV415ExecutionEngineEy(
    QQmlContextData *self,
    QV4::ExecutionEngine *engine,
    QV4::ReturnedValue scripts) {
  self->setImportedScripts(engine, scripts);
}

//  bool QQmlContextData::hasUnresolvedNames() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData18hasUnresolvedNamesEv(
    const QQmlContextData *self) {
  return self->hasUnresolvedNames();
}

//  void QQmlContextData::setUnresolvedNames(bool hasUnresolvedNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData18setUnresolvedNamesEb(
    QQmlContextData *self,
    bool hasUnresolvedNames) {
  self->setUnresolvedNames(hasUnresolvedNames);
}

//  QQmlComponentAttached *QQmlContextData::componentAttacheds() const
extern "C" Q_DECL_EXPORT
QQmlComponentAttached *ritual_ZNK15QQmlContextData18componentAttachedsEv(
    const QQmlContextData *self) {
  return self->componentAttacheds();
}

//  void QQmlContextData::addComponentAttached(QQmlComponentAttached
//      *attached)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData20addComponentAttachedEP21QQmlComponentAttached(
    QQmlContextData *self,
    QQmlComponentAttached *attached) {
  self->addComponentAttached(attached);
}

//  void QQmlContextData::addExpression(QQmlJavaScriptExpression *expression)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData13addExpressionEP24QQmlJavaScriptExpression(
    QQmlContextData *self,
    QQmlJavaScriptExpression *expression) {
  self->addExpression(expression);
}

//  bool QQmlContextData::valueTypesAreAddressable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData24valueTypesAreAddressableEv(
    const QQmlContextData *self) {
  return self->valueTypesAreAddressable();
}

//  bool QQmlContextData::valueTypesAreAssertable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData23valueTypesAreAssertableEv(
    const QQmlContextData *self) {
  return self->valueTypesAreAssertable();
}

//  QQmlContextData::~QQmlContextData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextDataD1Ev(QQmlContextData *self) {
  delete self;
}

//  bool QQmlContextData::hasExpressionsToRun(bool isGlobalRefresh) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlContextData19hasExpressionsToRunEb(
    const QQmlContextData *self,
    bool isGlobalRefresh) {
  return self->hasExpressionsToRun(isGlobalRefresh);
}

//  void QQmlContextData::refreshExpressionsRecursive(bool isGlobal)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData27refreshExpressionsRecursiveEb(
    QQmlContextData *self,
    bool isGlobal) {
  self->refreshExpressionsRecursive(isGlobal);
}

//  void
//      QQmlContextData::refreshExpressionsRecursive(QQmlJavaScriptExpression
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlContextData27refreshExpressionsRecursiveEP24QQmlJavaScriptExpression(
    QQmlContextData *self,
    QQmlJavaScriptExpression *a0) {
  self->refreshExpressionsRecursive(a0);
}

//  void QQmlContextData::initPropertyNames() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlContextData17initPropertyNamesEv(
    const QQmlContextData *self) {
  self->initPropertyNames();
}

//  void QQmlContextData::ensurePropertyNames() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlContextData19ensurePropertyNamesEv(
    const QQmlContextData *self) {
  self->ensurePropertyNames();
}
