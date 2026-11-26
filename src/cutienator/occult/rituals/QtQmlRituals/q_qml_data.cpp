//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldata_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 1. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlData::QQmlData(Ownership ownership)
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZN8QQmlDataC1ENS_9OwnershipE(
    QQmlData::Ownership ownership) {
  return new QQmlData(ownership);
}

//  QQmlData::~QQmlData()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlDataD1Ev(QQmlData *self) {
  delete self;
}

//  void QQmlData::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData4initEv() {
  QQmlData::init();
}

//  void QQmlData::destroyed(QAbstractDeclarativeData *a0, QObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData9destroyedEP24QAbstractDeclarativeDataP7QObject(
    QAbstractDeclarativeData *a0,
    QObject *a1) {
  QQmlData::destroyed(a0, a1);
}

//  void QQmlData::signalEmitted(QAbstractDeclarativeData *a0, QObject *a1,
//      int a2, void **a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData13signalEmittedEP24QAbstractDeclarativeDataP7QObjectiPPv(
    QAbstractDeclarativeData *a0,
    QObject *a1,
    int a2,
    void **a3) {
  QQmlData::signalEmitted(a0, a1, a2, a3);
}

//  int QQmlData::receivers(QAbstractDeclarativeData *a0, const QObject *a1,
//      int a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QQmlData9receiversEP24QAbstractDeclarativeDataPK7QObjecti(
    QAbstractDeclarativeData *a0,
    const QObject *a1,
    int a2) {
  return QQmlData::receivers(a0, a1, a2);
}

//  bool QQmlData::isSignalConnected(QAbstractDeclarativeData *a0, const
//      QObject *a1, int a2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlData17isSignalConnectedEP24QAbstractDeclarativeDataPK7QObjecti(
    QAbstractDeclarativeData *a0,
    const QObject *a1,
    int a2) {
  return QQmlData::isSignalConnected(a0, a1, a2);
}

//  void QQmlData::destroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData9destroyedEP7QObject(QQmlData *self, QObject *a0) {
  self->destroyed(a0);
}

//  void QQmlData::setImplicitDestructible()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData23setImplicitDestructibleEv(QQmlData *self) {
  self->setImplicitDestructible();
}

//  QQmlNotifierEndpoint *QQmlData::notify(int index) const
extern "C" Q_DECL_EXPORT
QQmlNotifierEndpoint *ritual_ZNK8QQmlData6notifyEi(
    const QQmlData *self,
    int index) {
  return self->notify(index);
}

//  void QQmlData::addNotify(int index, QQmlNotifierEndpoint *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData9addNotifyEiP20QQmlNotifierEndpoint(
    QQmlData *self,
    int index,
    QQmlNotifierEndpoint *a1) {
  self->addNotify(index, a1);
}

//  int QQmlData::endpointCount(int index)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QQmlData13endpointCountEi(QQmlData *self, int index) {
  return self->endpointCount(index);
}

//  bool QQmlData::signalHasEndpoint(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlData17signalHasEndpointEi(
    const QQmlData *self,
    int index) {
  return self->signalHasEndpoint(index);
}

//  void QQmlData::connectEndpoint(QQmlNotifierEndpoint *endPoint, QObject
//      *source, int sourceSignal, QQmlEngine *engine, bool doNotify)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData15connectEndpointEP20QQmlNotifierEndpointP7QObjectiP10QQmlEngineb(
    QQmlNotifierEndpoint *endPoint,
    QObject *source,
    int sourceSignal,
    QQmlEngine *engine,
    bool doNotify) {
  QQmlData::connectEndpoint(
      endPoint,
      source,
      sourceSignal,
      engine,
      doNotify);
}

//  void QQmlData::disconnectNotifiers(DeleteNotifyList doDelete)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData19disconnectNotifiersENS_16DeleteNotifyListE(
    QQmlData *self,
    QQmlData::DeleteNotifyList doDelete) {
  self->disconnectNotifiers(doDelete);
}

//  bool QQmlData::hasBindingBit(int a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlData13hasBindingBitEi(const QQmlData *self, int a0) {
  return self->hasBindingBit(a0);
}

//  void QQmlData::setBindingBit(QObject *obj, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData13setBindingBitEP7QObjecti(
    QQmlData *self,
    QObject *obj,
    int a1) {
  self->setBindingBit(obj, a1);
}

//  void QQmlData::clearBindingBit(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData15clearBindingBitEi(QQmlData *self, int a0) {
  self->clearBindingBit(a0);
}

//  bool QQmlData::hasPendingBindingBit(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlData20hasPendingBindingBitEi(
    const QQmlData *self,
    int index) {
  return self->hasPendingBindingBit(index);
}

//  void QQmlData::setPendingBindingBit(QObject *obj, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData20setPendingBindingBitEP7QObjecti(
    QQmlData *self,
    QObject *obj,
    int a1) {
  self->setPendingBindingBit(obj, a1);
}

//  void QQmlData::clearPendingBindingBit(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData22clearPendingBindingBitEi(QQmlData *self, int a0) {
  self->clearPendingBindingBit(a0);
}

//  void QQmlData::deferData(int objectIndex, const
//      QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const
//      QQmlRefPointer<QQmlContextData> &a2, const QString
//      &inlineComponentName)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData9deferDataEiRK14QQmlRefPointerIN3QV425ExecutableCompilationUnitEERKS0_I15QQmlContextDataERK7QString(
    QQmlData *self,
    int objectIndex,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *a1,
    const QQmlRefPointer<QQmlContextData> *a2,
    const QString *inlineComponentName) {
  self->deferData(objectIndex, *a1, *a2, *inlineComponentName);
}

//  void QQmlData::releaseDeferredData()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData19releaseDeferredDataEv(QQmlData *self) {
  self->releaseDeferredData();
}

//  QQmlData *QQmlData::get(QObjectPrivate *priv, bool create)
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZN8QQmlData3getEP14QObjectPrivateb(
    QObjectPrivate *priv,
    bool create) {
  return QQmlData::get(priv, create);
}

//  QQmlData *QQmlData::get(const QObjectPrivate *priv)
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZN8QQmlData3getEPK14QObjectPrivate(
    const QObjectPrivate *priv) {
  return QQmlData::get(priv);
}

//  QQmlData *QQmlData::get(QObject *object, bool create)
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZN8QQmlData3getEP7QObjectb(QObject *object, bool create) {
  return QQmlData::get(object, create);
}

//  QQmlData *QQmlData::get(const QObject *object)
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZN8QQmlData3getEPK7QObject(const QObject *object) {
  return QQmlData::get(object);
}

//  bool QQmlData::keepAliveDuringGarbageCollection(const QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlData32keepAliveDuringGarbageCollectionEPK7QObject(
    const QObject *object) {
  return QQmlData::keepAliveDuringGarbageCollection(object);
}

//  bool QQmlData::hasExtendedData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlData15hasExtendedDataEv(const QQmlData *self) {
  return self->hasExtendedData();
}

//  QHash<QQmlAttachedPropertiesFunc, QObject *>
//      *QQmlData::attachedProperties() const
extern "C" Q_DECL_EXPORT
QHash<QQmlAttachedPropertiesFunc, QObject *> *ritual_ZNK8QQmlData18attachedPropertiesEv(
    const QQmlData *self) {
  return self->attachedProperties();
}

//  bool QQmlData::wasDeleted(const QObject *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlData10wasDeletedEPK7QObject(const QObject *a0) {
  return QQmlData::wasDeleted(a0);
}

//  bool QQmlData::wasDeleted(const QObjectPrivate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlData10wasDeletedEPK14QObjectPrivate(
    const QObjectPrivate *a0) {
  return QQmlData::wasDeleted(a0);
}

//  void QQmlData::markAsDeleted(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData13markAsDeletedEP7QObject(QObject *a0) {
  QQmlData::markAsDeleted(a0);
}

//  void QQmlData::setQueuedForDeletion(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData20setQueuedForDeletionEP7QObject(QObject *a0) {
  QQmlData::setQueuedForDeletion(a0);
}

//  void QQmlData::flushPendingBinding(QObject *object, int coreIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData19flushPendingBindingEP7QObjecti(
    QObject *object,
    int coreIndex) {
  QQmlData::flushPendingBinding(object, coreIndex);
}

//  void QQmlData::flushPendingBinding(int coreIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData19flushPendingBindingEi(
    QQmlData *self,
    int coreIndex) {
  self->flushPendingBinding(coreIndex);
}

//  QQmlPropertyCache::ConstPtr QQmlData::ensurePropertyCache(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN8QQmlData19ensurePropertyCacheEP7QObject(
    QObject *object) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlData::ensurePropertyCache(
          object));
}

//  uint QQmlData::offsetForBit(int bit)
extern "C" Q_DECL_EXPORT
uint ritual_ZN8QQmlData12offsetForBitEi(int bit) {
  return QQmlData::offsetForBit(bit);
}

//  BindingBitsType QQmlData::bitFlagForBit(int bit)
extern "C" Q_DECL_EXPORT
QQmlData::BindingBitsType ritual_ZN8QQmlData13bitFlagForBitEi(int bit) {
  return QQmlData::bitFlagForBit(bit);
}

//  void QQmlData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData5clearEv(QQmlData *self) {
  self->clear();
}

//  QQmlData *QQmlData::createQQmlData(QObjectPrivate *priv)
extern "C" Q_DECL_EXPORT
QQmlData *ritual_ZN8QQmlData14createQQmlDataEP14QObjectPrivate(
    QObjectPrivate *priv) {
  return QQmlData::createQQmlData(priv);
}

//  QQmlPropertyCache::ConstPtr QQmlData::createPropertyCache(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN8QQmlData19createPropertyCacheEP7QObject(
    QObject *object) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlData::createPropertyCache(
          object));
}

//  void QQmlData::removeFromContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData17removeFromContextEv(QQmlData *self) {
  self->removeFromContext();
}

//  void QQmlData::clearBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData13clearBindingsEv(QQmlData *self) {
  self->clearBindings();
}

//  bool QQmlData::clearSignalHandlers()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlData19clearSignalHandlersEv(QQmlData *self) {
  return self->clearSignalHandlers();
}

//  bool QQmlData::hasBitSet(int bit) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlData9hasBitSetEi(const QQmlData *self, int bit) {
  return self->hasBitSet(bit);
}

//  void QQmlData::clearBit(int bit)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData8clearBitEi(QQmlData *self, int bit) {
  self->clearBit(bit);
}

//  void QQmlData::setBit(QObject *obj, int bit)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData6setBitEP7QObjecti(
    QQmlData *self,
    QObject *obj,
    int bit) {
  self->setBit(obj, bit);
}

//  BindingBitsType *QQmlData::growBits(QObject *obj, int bit)
extern "C" Q_DECL_EXPORT
QQmlData::BindingBitsType *ritual_ZN8QQmlData8growBitsEP7QObjecti(
    QQmlData *self,
    QObject *obj,
    int bit) {
  return self->growBits(obj, bit);
}
