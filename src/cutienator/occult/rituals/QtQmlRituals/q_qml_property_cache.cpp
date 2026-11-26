//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  3. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qobjectdefs.h>
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlenumvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QTypeRevision>
#include <QtCore/QString>
#include <QtCore/QMetaType>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlbinding_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtQml/private/qqmlpropertycachemethodarguments_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtQml/private/qv4codegen_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/QCryptographicHash>
#include <QtCore/private/qtools_p.h>
#include <limits.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycache.cpp, line 304, as _ZNK17QQmlPropertyCache4copyERK21QQmlMetaObjectPointeri
inline QQmlPropertyCache::Ptr QQmlPropertyCache::copy(const QQmlMetaObjectPointer &mo, int reserve) const
{
    QQmlPropertyCache::Ptr cache = QQmlPropertyCache::Ptr(
            new QQmlPropertyCache(mo, _handleOverride), QQmlPropertyCache::Ptr::Adopt);
    cache->_parent.reset(this);
    cache->propertyIndexCacheStart = propertyIndexCache.size() + propertyIndexCacheStart;
    cache->methodIndexCacheStart = methodIndexCache.size() + methodIndexCacheStart;
    cache->signalHandlerIndexCacheStart = signalHandlerIndexCache.size() + signalHandlerIndexCacheStart;
    cache->stringCache.linkAndReserve(stringCache, reserve);
    cache->allowedRevisionCache = allowedRevisionCache;
    cache->_defaultPropertyName = _defaultPropertyName;
    cache->_listPropertyAssignBehavior = _listPropertyAssignBehavior;

    return cache;
}
//  -----------------------------------------------------------------------

//  Ptr QQmlPropertyCache::createStandalone(const QMetaObject *a0,
//      QTypeRevision metaObjectRevision)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZN17QQmlPropertyCache16createStandaloneEPK11QMetaObject13QTypeRevision(
    const QMetaObject *a0,
    const QTypeRevision *metaObjectRevision) {
  return new QQmlPropertyCache::Ptr(
      QQmlPropertyCache::createStandalone(
          a0,
          *metaObjectRevision));
}

//  QQmlPropertyCache::QQmlPropertyCache(OverrideSemantics::HandlerRef
//      handleOverride)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache *ritual_ZN17QQmlPropertyCacheC1EN3qxp12function_refIJKFN17OverrideSemantics6StatusER16QQmlPropertyDataPS4_NS2_9CheckModeEEEEE(
    const OverrideSemantics::HandlerRef *handleOverride) {
  return new QQmlPropertyCache(*handleOverride);
}

//  QQmlPropertyCache::~QQmlPropertyCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCacheD1Ev(QQmlPropertyCache *self) {
  delete self;
}

//  void QQmlPropertyCache::update(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache6updateEPK11QMetaObject(
    QQmlPropertyCache *self,
    const QMetaObject *a0) {
  self->update(a0);
}

//  void QQmlPropertyCache::invalidate(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache10invalidateEPK11QMetaObject(
    QQmlPropertyCache *self,
    const QMetaObject *a0) {
  self->invalidate(a0);
}

//  QQmlPropertyCache::Ptr QQmlPropertyCache::copy() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK17QQmlPropertyCache4copyEv(
    const QQmlPropertyCache *self) {
  return new QQmlPropertyCache::Ptr(self->copy());
}

//  QQmlPropertyCache::Ptr QQmlPropertyCache::rebased(const
//      QQmlPropertyCache::ConstPtr &parent) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK17QQmlPropertyCache7rebasedERKNS_8ConstPtrE(
    const QQmlPropertyCache *self,
    const QQmlPropertyCache::ConstPtr *parent) {
  return new QQmlPropertyCache::Ptr(self->rebased(*parent));
}

//  QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndAppend(const QMetaObject
//      *a0, QTypeRevision typeVersion, QQmlPropertyData::Flags
//      propertyFlags, QQmlPropertyData::Flags methodFlags,
//      QQmlPropertyData::Flags signalFlags) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK17QQmlPropertyCache13copyAndAppendEPK11QMetaObject13QTypeRevisionN16QQmlPropertyData5FlagsES5_S5_(
    const QQmlPropertyCache *self,
    const QMetaObject *a0,
    const QTypeRevision *typeVersion,
    const QQmlPropertyData::Flags *propertyFlags,
    const QQmlPropertyData::Flags *methodFlags,
    const QQmlPropertyData::Flags *signalFlags) {
  return new QQmlPropertyCache::Ptr(
      self->copyAndAppend(
          a0,
          *typeVersion,
          *propertyFlags,
          *methodFlags,
          *signalFlags));
}

//  QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndReserve(int
//      propertyCount, int methodCount, int signalCount, int enumCount) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK17QQmlPropertyCache14copyAndReserveEiiii(
    const QQmlPropertyCache *self,
    int propertyCount,
    int methodCount,
    int signalCount,
    int enumCount) {
  return new QQmlPropertyCache::Ptr(
      self->copyAndReserve(
          propertyCount,
          methodCount,
          signalCount,
          enumCount));
}

//  const QMetaObject *QQmlPropertyCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlPropertyCache10metaObjectEv(
    const QQmlPropertyCache *self) {
  return self->metaObject();
}

//  const QMetaObject *QQmlPropertyCache::createMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlPropertyCache16createMetaObjectEv(
    const QQmlPropertyCache *self) {
  return self->createMetaObject();
}

//  const QMetaObject *QQmlPropertyCache::firstCppMetaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQmlPropertyCache18firstCppMetaObjectEv(
    const QQmlPropertyCache *self) {
  return self->firstCppMetaObject();
}

//  const QQmlPropertyData *QQmlPropertyCache::property(int a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache8propertyEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->property(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::maybeUnresolvedProperty(int
//      a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache23maybeUnresolvedPropertyEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->maybeUnresolvedProperty(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::method(int a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache6methodEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->method(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::signal(int index) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache6signalEi(
    const QQmlPropertyCache *self,
    int index) {
  return self->signal(index);
}

//  QQmlEnumData *QQmlPropertyCache::qmlEnum(int a0) const
extern "C" Q_DECL_EXPORT
QQmlEnumData *ritual_ZNK17QQmlPropertyCache7qmlEnumEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->qmlEnum(a0);
}

//  int QQmlPropertyCache::methodIndexToSignalIndex(int a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache24methodIndexToSignalIndexEi(
    const QQmlPropertyCache *self,
    int a0) {
  return self->methodIndexToSignalIndex(a0);
}

//  QString QQmlPropertyCache::defaultPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlPropertyCache19defaultPropertyNameEv(
    const QQmlPropertyCache *self) {
  return new QString(self->defaultPropertyName());
}

//  const QQmlPropertyData *QQmlPropertyCache::defaultProperty() const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache15defaultPropertyEv(
    const QQmlPropertyCache *self) {
  return self->defaultProperty();
}

//  const QQmlPropertyCache::ConstPtr &QQmlPropertyCache::parent() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK17QQmlPropertyCache6parentEv(
    const QQmlPropertyCache *self) {
  return new QQmlPropertyCache::ConstPtr(self->parent());
}

//  void QQmlPropertyCache::setParent(QQmlPropertyCache::ConstPtr newParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache9setParentENS_8ConstPtrE(
    QQmlPropertyCache *self,
    const QQmlPropertyCache::ConstPtr *newParent) {
  self->setParent(*newParent);
}

//  const QQmlPropertyData *QQmlPropertyCache::overrideData(const
//      QQmlPropertyData *a0) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZNK17QQmlPropertyCache12overrideDataEPK16QQmlPropertyData(
    const QQmlPropertyCache *self,
    const QQmlPropertyData *a0) {
  return self->overrideData(a0);
}

//  bool QQmlPropertyCache::isAllowedInRevision(const QQmlPropertyData *a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyCache19isAllowedInRevisionEPK16QQmlPropertyData(
    const QQmlPropertyCache *self,
    const QQmlPropertyData *a0) {
  return self->isAllowedInRevision(a0);
}

//  const QQmlPropertyData *QQmlPropertyCache::property(QObject *a0,
//      QStringView a1, const QQmlRefPointer<QQmlContextData> &a2,
//      QQmlPropertyData *a3)
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZN17QQmlPropertyCache8propertyEP7QObject11QStringViewRK14QQmlRefPointerI15QQmlContextDataEP16QQmlPropertyData(
    QObject *a0,
    const QString *a1,
    const QQmlRefPointer<QQmlContextData> *a2,
    QQmlPropertyData *a3) {
  return QQmlPropertyCache::property(a0, QStringView(*a1), *a2, a3);
}

//  const QQmlPropertyData *QQmlPropertyCache::property(QObject *a0, const
//      QLatin1String &a1, const QQmlRefPointer<QQmlContextData> &a2,
//      QQmlPropertyData *a3)
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZN17QQmlPropertyCache8propertyEP7QObjectRK13QLatin1StringRK14QQmlRefPointerI15QQmlContextDataEP16QQmlPropertyData(
    QObject *a0,
    const QLatin1String *a1,
    const QQmlRefPointer<QQmlContextData> *a2,
    QQmlPropertyData *a3) {
  return QQmlPropertyCache::property(a0, *a1, *a2, a3);
}

//  const QQmlPropertyData *QQmlPropertyCache::property(QObject *a0, const
//      QV4::String *a1, const QQmlRefPointer<QQmlContextData> &a2,
//      QQmlPropertyData *a3)
extern "C" Q_DECL_EXPORT
const QQmlPropertyData *ritual_ZN17QQmlPropertyCache8propertyEP7QObjectPKN3QV46StringERK14QQmlRefPointerI15QQmlContextDataEP16QQmlPropertyData(
    QObject *a0,
    const QV4::String *a1,
    const QQmlRefPointer<QQmlContextData> *a2,
    QQmlPropertyData *a3) {
  return QQmlPropertyCache::property(a0, a1, *a2, a3);
}

//  int QQmlPropertyCache::originalClone(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache13originalCloneEi(
    const QQmlPropertyCache *self,
    int index) {
  return self->originalClone(index);
}

//  int QQmlPropertyCache::originalClone(const QObject *a0, int index)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQmlPropertyCache13originalCloneEPK7QObjecti(
    const QObject *a0,
    int index) {
  return QQmlPropertyCache::originalClone(a0, index);
}

//  QList<QByteArray> QQmlPropertyCache::signalParameterNames(int index)
//      const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK17QQmlPropertyCache20signalParameterNamesEi(
    const QQmlPropertyCache *self,
    int index) {
  return new QList<QByteArray>(self->signalParameterNames(index));
}

//  QString QQmlPropertyCache::signalParameterStringForJS(const
//      QList<QByteArray> &parameterNameList, QString *errorString)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQmlPropertyCache26signalParameterStringForJSERK5QListI10QByteArrayEP7QString(
    const QList<QByteArray> *parameterNameList,
    QString *errorString) {
  return new QString(
      QQmlPropertyCache::signalParameterStringForJS(
          *parameterNameList,
          errorString));
}

//  const char *QQmlPropertyCache::className() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK17QQmlPropertyCache9classNameEv(
    const QQmlPropertyCache *self) {
  return self->className();
}

//  int QQmlPropertyCache::propertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache13propertyCountEv(
    const QQmlPropertyCache *self) {
  return self->propertyCount();
}

//  int QQmlPropertyCache::ownPropertyCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache16ownPropertyCountEv(
    const QQmlPropertyCache *self) {
  return self->ownPropertyCount();
}

//  int QQmlPropertyCache::propertyOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache14propertyOffsetEv(
    const QQmlPropertyCache *self) {
  return self->propertyOffset();
}

//  int QQmlPropertyCache::methodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache11methodCountEv(
    const QQmlPropertyCache *self) {
  return self->methodCount();
}

//  int QQmlPropertyCache::ownMethodCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache14ownMethodCountEv(
    const QQmlPropertyCache *self) {
  return self->ownMethodCount();
}

//  int QQmlPropertyCache::methodOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache12methodOffsetEv(
    const QQmlPropertyCache *self) {
  return self->methodOffset();
}

//  int QQmlPropertyCache::signalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache11signalCountEv(
    const QQmlPropertyCache *self) {
  return self->signalCount();
}

//  int QQmlPropertyCache::ownSignalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache14ownSignalCountEv(
    const QQmlPropertyCache *self) {
  return self->ownSignalCount();
}

//  int QQmlPropertyCache::signalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache12signalOffsetEv(
    const QQmlPropertyCache *self) {
  return self->signalOffset();
}

//  int QQmlPropertyCache::ownEnumCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlPropertyCache12ownEnumCountEv(
    const QQmlPropertyCache *self) {
  return self->ownEnumCount();
}

//  void QQmlPropertyCache::toMetaObjectBuilder(QMetaObjectBuilder &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQmlPropertyCache19toMetaObjectBuilderER18QMetaObjectBuilder(
    const QQmlPropertyCache *self,
    QMetaObjectBuilder *a0) {
  self->toMetaObjectBuilder(*a0);
}

//  bool QQmlPropertyCache::callJSFactoryMethod(QObject *object, void **args)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyCache19callJSFactoryMethodEP7QObjectPPv(
    const QQmlPropertyCache *self,
    QObject *object,
    void **args) {
  return self->callJSFactoryMethod(object, args);
}

//  bool QQmlPropertyCache::determineMetaObjectSizes(const QMetaObject &mo,
//      int *fieldCount, int *stringCount)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlPropertyCache24determineMetaObjectSizesERK11QMetaObjectPiS3_(
    const QMetaObject *mo,
    int *fieldCount,
    int *stringCount) {
  return QQmlPropertyCache::determineMetaObjectSizes(
      *mo,
      fieldCount,
      stringCount);
}

//  bool QQmlPropertyCache::addToHash(QCryptographicHash &hash, const
//      QMetaObject &mo)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlPropertyCache9addToHashER18QCryptographicHashRK11QMetaObject(
    QCryptographicHash *hash,
    const QMetaObject *mo) {
  return QQmlPropertyCache::addToHash(*hash, *mo);
}

//  QByteArray QQmlPropertyCache::checksum(QHash<quintptr, QByteArray>
//      *checksums, bool *ok) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QQmlPropertyCache8checksumEP5QHashIy10QByteArrayEPb(
    const QQmlPropertyCache *self,
    QHash<quintptr, QByteArray> *checksums,
    bool *ok) {
  return new QByteArray(self->checksum(checksums, ok));
}

//  QTypeRevision QQmlPropertyCache::allowedRevision(int index) const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK17QQmlPropertyCache15allowedRevisionEi(
    const QQmlPropertyCache *self,
    int index) {
  return new QTypeRevision(self->allowedRevision(index));
}

//  void QQmlPropertyCache::setAllowedRevision(int index, QTypeRevision
//      allowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache18setAllowedRevisionEi13QTypeRevision(
    QQmlPropertyCache *self,
    int index,
    const QTypeRevision *allowed) {
  self->setAllowedRevision(index, *allowed);
}

//  bool QQmlPropertyCache::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlPropertyCache11isCompositeEv(
    const QQmlPropertyCache *self) {
  return self->isComposite();
}

//  QQmlPropertyCache::QQmlPropertyCache(const QQmlMetaObjectPointer
//      &metaObject, OverrideSemantics::HandlerRef handleOverride)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache *ritual_ZN17QQmlPropertyCacheC1ERK21QQmlMetaObjectPointerN3qxp12function_refIJKFN17OverrideSemantics6StatusER16QQmlPropertyDataPS7_NS5_9CheckModeEEEEE(
    const QQmlMetaObjectPointer *metaObject,
    const OverrideSemantics::HandlerRef *handleOverride) {
  return new QQmlPropertyCache(*metaObject, *handleOverride);
}

//  QQmlPropertyCache::Ptr QQmlPropertyCache::copy(const
//      QQmlMetaObjectPointer &mo, int reserve) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::Ptr *ritual_ZNK17QQmlPropertyCache4copyERK21QQmlMetaObjectPointeri(
    const QQmlPropertyCache *self,
    const QQmlMetaObjectPointer *mo,
    int reserve) {
  return new QQmlPropertyCache::Ptr(self->copy(*mo, reserve));
}

//  void QQmlPropertyCache::append(const QMetaObject *a0, QTypeRevision
//      typeVersion, QQmlPropertyData::Flags propertyFlags,
//      QQmlPropertyData::Flags methodFlags, QQmlPropertyData::Flags
//      signalFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache6appendEPK11QMetaObject13QTypeRevisionN16QQmlPropertyData5FlagsES5_S5_(
    QQmlPropertyCache *self,
    const QMetaObject *a0,
    const QTypeRevision *typeVersion,
    const QQmlPropertyData::Flags *propertyFlags,
    const QQmlPropertyData::Flags *methodFlags,
    const QQmlPropertyData::Flags *signalFlags) {
  self->append(a0, *typeVersion, *propertyFlags, *methodFlags, *signalFlags);
}

//  AppendResult QQmlPropertyCache::appendPropertyAttr(const QString &name,
//      QQmlPropertyData &&data)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::AppendResult *ritual_ZN17QQmlPropertyCache18appendPropertyAttrERK7QStringO16QQmlPropertyData(
    QQmlPropertyCache *self,
    const QString *name,
    QQmlPropertyData *data) {
  return new QQmlPropertyCache::AppendResult(
      self->appendPropertyAttr(
          *name,
          std::move(*data)));
}

//  AppendResult QQmlPropertyCache::appendAlias(const QString &a0,
//      QQmlPropertyData::Flags flags, int coreIndex, QMetaType propType,
//      QTypeRevision version, int notifyIndex, int encodedTargetIndex, int
//      targetObjectId)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::AppendResult *ritual_ZN17QQmlPropertyCache11appendAliasERK7QStringN16QQmlPropertyData5FlagsEi9QMetaType13QTypeRevisioniii(
    QQmlPropertyCache *self,
    const QString *a0,
    const QQmlPropertyData::Flags *flags,
    int coreIndex,
    const QMetaType *propType,
    const QTypeRevision *version,
    int notifyIndex,
    int encodedTargetIndex,
    int targetObjectId) {
  return new QQmlPropertyCache::AppendResult(
      self->appendAlias(
          *a0,
          *flags,
          coreIndex,
          *propType,
          *version,
          notifyIndex,
          encodedTargetIndex,
          targetObjectId));
}

//  AppendResult QQmlPropertyCache::appendComponentWrapper(int coreIndex, int
//      wrappedObjectIndex)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::AppendResult *ritual_ZN17QQmlPropertyCache22appendComponentWrapperEii(
    QQmlPropertyCache *self,
    int coreIndex,
    int wrappedObjectIndex) {
  return new QQmlPropertyCache::AppendResult(
      self->appendComponentWrapper(
          coreIndex,
          wrappedObjectIndex));
}

//  void QQmlPropertyCache::appendSignal(const QString &a0,
//      QQmlPropertyData::Flags a1, int coreIndex, const QMetaType *types,
//      const QList<QByteArray> &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache12appendSignalERK7QStringN16QQmlPropertyData5FlagsEiPK9QMetaTypeRK5QListI10QByteArrayE(
    QQmlPropertyCache *self,
    const QString *a0,
    const QQmlPropertyData::Flags *a1,
    int coreIndex,
    const QMetaType *types,
    const QList<QByteArray> *names) {
  self->appendSignal(*a0, *a1, coreIndex, types, *names);
}

//  void QQmlPropertyCache::appendMethod(const QString &a0,
//      QQmlPropertyData::Flags flags, int coreIndex, QMetaType returnType,
//      const QList<QByteArray> &names, const QList<QMetaType>
//      &parameterTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache12appendMethodERK7QStringN16QQmlPropertyData5FlagsEi9QMetaTypeRK5QListI10QByteArrayERKS6_IS5_E(
    QQmlPropertyCache *self,
    const QString *a0,
    const QQmlPropertyData::Flags *flags,
    int coreIndex,
    const QMetaType *returnType,
    const QList<QByteArray> *names,
    const QList<QMetaType> *parameterTypes) {
  self->appendMethod(
      *a0,
      *flags,
      coreIndex,
      *returnType,
      *names,
      *parameterTypes);
}

//  void QQmlPropertyCache::appendEnum(const QString &a0, const
//      QList<QQmlEnumValue> &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache10appendEnumERK7QStringRK5QListI13QQmlEnumValueE(
    QQmlPropertyCache *self,
    const QString *a0,
    const QList<QQmlEnumValue> *a1) {
  self->appendEnum(*a0, *a1);
}

//  QQmlPropertyCacheMethodArguments
//      *QQmlPropertyCache::createArgumentsObject(int count, const
//      QList<QByteArray> &names)
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheMethodArguments *ritual_ZN17QQmlPropertyCache21createArgumentsObjectEiRK5QListI10QByteArrayE(
    QQmlPropertyCache *self,
    int count,
    const QList<QByteArray> *names) {
  return self->createArgumentsObject(count, *names);
}

//  a QQmlPropertyCache::Ptr a ritual of QQmlPropertyCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlPropertyCache__QQmlPropertyCache_Ptr(
    QQmlPropertyCache::Ptr *self) {
  delete self;
}

//  a QQmlPropertyCache::AppendResult a ritual of QQmlPropertyCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlPropertyCache__QQmlPropertyCache_AppendResult(
    QQmlPropertyCache::AppendResult *self) {
  delete self;
}

//  QQmlPropertyData *QQmlPropertyCache::findNamedProperty<QString>(const
//      QString &key) const
extern "C" Q_DECL_EXPORT
QQmlPropertyData * ritual_ZNK17QQmlPropertyCache17findNamedPropertyI7QStringEEP16QQmlPropertyDataRKT_(
    const QQmlPropertyCache *self,
    const QString *key) {
  return self->findNamedProperty<QString>(*key);
}

//  void QQmlPropertyCache::setNamedProperty<QString>(const QString &key, int
//      index, QQmlPropertyData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlPropertyCache16setNamedPropertyI7QStringEEvRKT_iP16QQmlPropertyData(
    QQmlPropertyCache *self,
    const QString *key,
    int index,
    QQmlPropertyData *data) {
  self->setNamedProperty<QString>(*key, index, data);
}

//  const QQmlPropertyData *QQmlPropertyCache::property<QString>(const
//      QString &key, QObject *object, const QQmlRefPointer<QQmlContextData>
//      &context) const
extern "C" Q_DECL_EXPORT
const QQmlPropertyData * ritual_ZNK17QQmlPropertyCache8propertyI7QStringEEPK16QQmlPropertyDataRKT_P7QObjectRK14QQmlRefPointerI15QQmlContextDataE(
    const QQmlPropertyCache *self,
    const QString *key,
    QObject *object,
    const QQmlRefPointer<QQmlContextData> *context) {
  return self->property<QString>(*key, object, *context);
}
