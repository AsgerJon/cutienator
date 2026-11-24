//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertydata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qproperty.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmlpropertycache_p.h"
#include <private/qqmlengine_p.h>
#include <private/qqmlbinding_p.h>
#include <private/qqmlvmemetaobject_p.h>
#include <private/qmetaobject_p.h>
#include <private/qmetaobjectbuilder_p.h>
#include <private/qqmlpropertycachemethodarguments_p.h>
#include <private/qqmlsignalnames_p.h>
#include <private/qv4codegen_p.h>
#include <private/qv4value_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/QCryptographicHash>
#include <QtCore/private/qtools_p.h>
#include <limits.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycache.cpp, line 166, as _ZN16QQmlPropertyData16flagsForPropertyERK13QMetaProperty
inline QQmlPropertyData::Flags
QQmlPropertyData::flagsForProperty(const QMetaProperty &p)
{
    QQmlPropertyData::Flags flags;

    flags.setIsConstant(p.isConstant());
    flags.setIsWritable(p.isWritable());
    flags.setIsResettable(p.isResettable());
    flags.setIsFinal(p.isFinal());
    flags.setIsVirtual(p.isVirtual());
    flags.setDoesOverride(p.isOverride());
    flags.setIsRequired(p.isRequired());
    flags.setIsBindable(p.isBindable());


    const QMetaType metaType = p.metaType();
    int propType = metaType.id();
    if (p.isEnumType()) {
        flags.setType(QQmlPropertyData::Flags::EnumType);
    } else if (metaType.flags() & QMetaType::PointerToQObject) {
        flags.setType(QQmlPropertyData::Flags::QObjectDerivedType);
    } else if (propType == QMetaType::QVariant) {
        flags.setType(QQmlPropertyData::Flags::QVariantType);
    } else if (metaType.flags() & QMetaType::IsQmlList) {
        flags.setType(QQmlPropertyData::Flags::QListType);
    }

    return flags;
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycache.cpp, line 196, as _ZN16QQmlPropertyData4loadERK13QMetaProperty
inline void QQmlPropertyData::load(const QMetaProperty &p)
{
    Q_ASSERT(p.revision() <= std::numeric_limits<quint16>::max());
    setCoreIndex(p.propertyIndex());
    setNotifyIndex(QMetaObjectPrivate::signalIndex(p.notifySignal()));
    setFlags(flagsForProperty(p));
    setRevision(QTypeRevision::fromEncodedVersion(p.revision()));
    QMetaType type = p.metaType();
    setPropType(type);
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycache.cpp, line 207, as _ZN16QQmlPropertyData4loadERK11QMetaMethod
inline void QQmlPropertyData::load(const QMetaMethod &m)
{
    setCoreIndex(m.methodIndex());
    m_flags.setType(Flags::FunctionType);

    // We need to set the constructor, signal, constant, arguments, V4Function, cloned flags.
    // These are specific to methods and change with each method.
    // The same QQmlPropertyData may be loaded with multiple methods in sequence.

    switch (m.methodType()) {
    case QMetaMethod::Signal:
        m_flags.setIsSignal(true);
        m_flags.setIsConstructor(false);
        setPropType(m.returnMetaType());
        break;
    case QMetaMethod::Constructor:
        m_flags.setIsSignal(false);
        m_flags.setIsConstructor(true);
        break;
    default:
        m_flags.setIsSignal(false);
        m_flags.setIsConstructor(false);
        setPropType(m.returnMetaType());
        break;
    }

    m_flags.setIsConstant(m.isConst());

    const int paramCount = m.parameterCount();
    if (paramCount) {
        m_flags.setHasArguments(true);
        m_flags.setIsV4Function(
                paramCount == 1 &&
                m.parameterMetaType(0) == QMetaType::fromType<QQmlV4FunctionPtr>());
    } else {
        m_flags.setHasArguments(false);
        m_flags.setIsV4Function(false);
    }

    m_flags.setIsCloned(m.attributes() & QMetaMethod::Cloned);

    Q_ASSERT(m.revision() <= std::numeric_limits<quint16>::max());
    setRevision(QTypeRevision::fromEncodedVersion(m.revision()));
}

//  from ../qtdeclarative/src/qml/qml/qqmlpropertycache.cpp, line 980, as _ZN16QQmlPropertyData16markAsOverrideOfEPS_
inline void QQmlPropertyData::markAsOverrideOf(QQmlPropertyData *predecessor)
{
    Q_ASSERT(predecessor != this);

    if (!predecessor) {
        return;
    }

    setOverrideIndexIsProperty(!predecessor->isFunction());
    setOverrideIndex(predecessor->coreIndex());
    // propagate "virtuality"
    m_flags.setIsVirtual(predecessor->isVirtual());
    predecessor->m_flags.setIsOverridden(true);
    Q_ASSERT(predecessor->isOverridden());
    return;
}
//  -----------------------------------------------------------------------

//  bool QQmlPropertyData::operator==(const QQmlPropertyData &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyDataeqERKS_(
    const QQmlPropertyData *self,
    const QQmlPropertyData *a0) {
  return self->operator==(*a0);
}

//  Flags QQmlPropertyData::flags() const
extern "C" Q_DECL_EXPORT
QQmlPropertyData::Flags *ritual_ZNK16QQmlPropertyData5flagsEv(
    const QQmlPropertyData *self) {
  return new QQmlPropertyData::Flags(self->flags());
}

//  void QQmlPropertyData::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData8setFlagsENS_5FlagsE(
    QQmlPropertyData *self,
    const QQmlPropertyData::Flags *f) {
  self->setFlags(*f);
}

//  bool QQmlPropertyData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData7isValidEv(const QQmlPropertyData *self) {
  return self->isValid();
}

//  bool QQmlPropertyData::isConstant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData10isConstantEv(
    const QQmlPropertyData *self) {
  return self->isConstant();
}

//  bool QQmlPropertyData::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData10isWritableEv(
    const QQmlPropertyData *self) {
  return self->isWritable();
}

//  void QQmlPropertyData::setWritable(bool onoff)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData11setWritableEb(
    QQmlPropertyData *self,
    bool onoff) {
  self->setWritable(onoff);
}

//  bool QQmlPropertyData::isResettable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData12isResettableEv(
    const QQmlPropertyData *self) {
  return self->isResettable();
}

//  bool QQmlPropertyData::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData7isAliasEv(const QQmlPropertyData *self) {
  return self->isAlias();
}

//  bool QQmlPropertyData::isFinal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData7isFinalEv(const QQmlPropertyData *self) {
  return self->isFinal();
}

//  bool QQmlPropertyData::isVirtual() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData9isVirtualEv(const QQmlPropertyData *self) {
  return self->isVirtual();
}

//  bool QQmlPropertyData::doesOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData12doesOverrideEv(
    const QQmlPropertyData *self) {
  return self->doesOverride();
}

//  bool QQmlPropertyData::isOverridden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData12isOverriddenEv(
    const QQmlPropertyData *self) {
  return self->isOverridden();
}

//  bool QQmlPropertyData::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData10isRequiredEv(
    const QQmlPropertyData *self) {
  return self->isRequired();
}

//  bool QQmlPropertyData::isFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData10isFunctionEv(
    const QQmlPropertyData *self) {
  return self->isFunction();
}

//  bool QQmlPropertyData::isQObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData9isQObjectEv(const QQmlPropertyData *self) {
  return self->isQObject();
}

//  bool QQmlPropertyData::isEnum() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData6isEnumEv(const QQmlPropertyData *self) {
  return self->isEnum();
}

//  bool QQmlPropertyData::isQList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData7isQListEv(const QQmlPropertyData *self) {
  return self->isQList();
}

//  bool QQmlPropertyData::isVarProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData13isVarPropertyEv(
    const QQmlPropertyData *self) {
  return self->isVarProperty();
}

//  bool QQmlPropertyData::isQVariant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData10isQVariantEv(
    const QQmlPropertyData *self) {
  return self->isQVariant();
}

//  bool QQmlPropertyData::isComponentWrapper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData18isComponentWrapperEv(
    const QQmlPropertyData *self) {
  return self->isComponentWrapper();
}

//  bool QQmlPropertyData::isVMEFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData13isVMEFunctionEv(
    const QQmlPropertyData *self) {
  return self->isVMEFunction();
}

//  bool QQmlPropertyData::hasArguments() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData12hasArgumentsEv(
    const QQmlPropertyData *self) {
  return self->hasArguments();
}

//  bool QQmlPropertyData::isSignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData8isSignalEv(const QQmlPropertyData *self) {
  return self->isSignal();
}

//  bool QQmlPropertyData::isVMESignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData11isVMESignalEv(
    const QQmlPropertyData *self) {
  return self->isVMESignal();
}

//  bool QQmlPropertyData::isV4Function() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData12isV4FunctionEv(
    const QQmlPropertyData *self) {
  return self->isV4Function();
}

//  bool QQmlPropertyData::isSignalHandler() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData15isSignalHandlerEv(
    const QQmlPropertyData *self) {
  return self->isSignalHandler();
}

//  bool QQmlPropertyData::hasMetaObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData13hasMetaObjectEv(
    const QQmlPropertyData *self) {
  return self->hasMetaObject();
}

//  bool QQmlPropertyData::hasStaticMetaCallFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData25hasStaticMetaCallFunctionEv(
    const QQmlPropertyData *self) {
  return self->hasStaticMetaCallFunction();
}

//  bool QQmlPropertyData::isOverridableSignal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData19isOverridableSignalEv(
    const QQmlPropertyData *self) {
  return self->isOverridableSignal();
}

//  bool QQmlPropertyData::isCloned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData8isClonedEv(const QQmlPropertyData *self) {
  return self->isCloned();
}

//  bool QQmlPropertyData::isConstructor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData13isConstructorEv(
    const QQmlPropertyData *self) {
  return self->isConstructor();
}

//  bool QQmlPropertyData::notifiesViaBindable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData19notifiesViaBindableEv(
    const QQmlPropertyData *self) {
  return self->notifiesViaBindable();
}

//  bool QQmlPropertyData::acceptsQBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData15acceptsQBindingEv(
    const QQmlPropertyData *self) {
  return self->acceptsQBinding();
}

//  bool QQmlPropertyData::hasOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData11hasOverrideEv(
    const QQmlPropertyData *self) {
  return self->hasOverride();
}

//  bool QQmlPropertyData::hasRevision() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData11hasRevisionEv(
    const QQmlPropertyData *self) {
  return self->hasRevision();
}

//  QMetaType QQmlPropertyData::propType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK16QQmlPropertyData8propTypeEv(
    const QQmlPropertyData *self) {
  return new QMetaType(self->propType());
}

//  void QQmlPropertyData::setPropType(QMetaType pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData11setPropTypeE9QMetaType(
    QQmlPropertyData *self,
    const QMetaType *pt) {
  self->setPropType(*pt);
}

//  int QQmlPropertyData::notifyIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData11notifyIndexEv(
    const QQmlPropertyData *self) {
  return self->notifyIndex();
}

//  void QQmlPropertyData::setNotifyIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData14setNotifyIndexEi(
    QQmlPropertyData *self,
    int idx) {
  self->setNotifyIndex(idx);
}

//  bool QQmlPropertyData::overrideIndexIsProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData23overrideIndexIsPropertyEv(
    const QQmlPropertyData *self) {
  return self->overrideIndexIsProperty();
}

//  void QQmlPropertyData::setOverrideIndexIsProperty(bool onoff)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData26setOverrideIndexIsPropertyEb(
    QQmlPropertyData *self,
    bool onoff) {
  self->setOverrideIndexIsProperty(onoff);
}

//  int QQmlPropertyData::overrideIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData13overrideIndexEv(
    const QQmlPropertyData *self) {
  return self->overrideIndex();
}

//  void QQmlPropertyData::setOverrideIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData16setOverrideIndexEi(
    QQmlPropertyData *self,
    int idx) {
  self->setOverrideIndex(idx);
}

//  int QQmlPropertyData::coreIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData9coreIndexEv(const QQmlPropertyData *self) {
  return self->coreIndex();
}

//  void QQmlPropertyData::setCoreIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData12setCoreIndexEi(
    QQmlPropertyData *self,
    int idx) {
  self->setCoreIndex(idx);
}

//  int QQmlPropertyData::aliasTarget() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData11aliasTargetEv(
    const QQmlPropertyData *self) {
  return self->aliasTarget();
}

//  void QQmlPropertyData::setAliasTarget(int target)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData14setAliasTargetEi(
    QQmlPropertyData *self,
    int target) {
  self->setAliasTarget(target);
}

//  int QQmlPropertyData::aliasTargetObjectId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData19aliasTargetObjectIdEv(
    const QQmlPropertyData *self) {
  return self->aliasTargetObjectId();
}

//  void QQmlPropertyData::setAliasTargetObjectId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData22setAliasTargetObjectIdEi(
    QQmlPropertyData *self,
    int id) {
  self->setAliasTargetObjectId(id);
}

//  int QQmlPropertyData::wrappedObjectIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData18wrappedObjectIndexEv(
    const QQmlPropertyData *self) {
  return self->wrappedObjectIndex();
}

//  void QQmlPropertyData::setWrappedObjectIndex(int wrappedObjectIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData21setWrappedObjectIndexEi(
    QQmlPropertyData *self,
    int wrappedObjectIndex) {
  self->setWrappedObjectIndex(wrappedObjectIndex);
}

//  QTypeRevision QQmlPropertyData::revision() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK16QQmlPropertyData8revisionEv(
    const QQmlPropertyData *self) {
  return new QTypeRevision(self->revision());
}

//  void QQmlPropertyData::setRevision(QTypeRevision revision)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData11setRevisionE13QTypeRevision(
    QQmlPropertyData *self,
    const QTypeRevision *revision) {
  self->setRevision(*revision);
}

//  QTypeRevision QQmlPropertyData::typeVersion() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK16QQmlPropertyData11typeVersionEv(
    const QQmlPropertyData *self) {
  return new QTypeRevision(self->typeVersion());
}

//  void QQmlPropertyData::setTypeVersion(QTypeRevision typeVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData14setTypeVersionE13QTypeRevision(
    QQmlPropertyData *self,
    const QTypeRevision *typeVersion) {
  self->setTypeVersion(*typeVersion);
}

//  QQmlPropertyCacheMethodArguments *QQmlPropertyData::arguments() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheMethodArguments *ritual_ZNK16QQmlPropertyData9argumentsEv(
    const QQmlPropertyData *self) {
  return self->arguments();
}

//  void QQmlPropertyData::setArguments(QQmlPropertyCacheMethodArguments
//      *args)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData12setArgumentsEP32QQmlPropertyCacheMethodArguments(
    QQmlPropertyData *self,
    QQmlPropertyCacheMethodArguments *args) {
  self->setArguments(args);
}

//  const QMetaObject *QQmlPropertyData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlPropertyData10metaObjectEv(
    const QQmlPropertyData *self) {
  return self->metaObject();
}

//  void QQmlPropertyData::setMetaObject(const QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData13setMetaObjectEPK11QMetaObject(
    QQmlPropertyData *self,
    const QMetaObject *metaObject) {
  self->setMetaObject(metaObject);
}

//  QMetaMethod QQmlPropertyData::metaMethod() const
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZNK16QQmlPropertyData10metaMethodEv(
    const QQmlPropertyData *self) {
  return new QMetaMethod(self->metaMethod());
}

//  int QQmlPropertyData::metaObjectOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlPropertyData16metaObjectOffsetEv(
    const QQmlPropertyData *self) {
  return self->metaObjectOffset();
}

//  void QQmlPropertyData::setMetaObjectOffset(int off)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData19setMetaObjectOffsetEi(
    QQmlPropertyData *self,
    int off) {
  self->setMetaObjectOffset(off);
}

//  quint16 QQmlPropertyData::relativePropertyIndex() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK16QQmlPropertyData21relativePropertyIndexEv(
    const QQmlPropertyData *self) {
  return self->relativePropertyIndex();
}

//  Flags QQmlPropertyData::flagsForProperty(const QMetaProperty &a0)
extern "C" Q_DECL_EXPORT
QQmlPropertyData::Flags *ritual_ZN16QQmlPropertyData16flagsForPropertyERK13QMetaProperty(
    const QMetaProperty *a0) {
  return new QQmlPropertyData::Flags(
      QQmlPropertyData::flagsForProperty(
          *a0));
}

//  void QQmlPropertyData::load(const QMetaProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData4loadERK13QMetaProperty(
    QQmlPropertyData *self,
    const QMetaProperty *a0) {
  self->load(*a0);
}

//  void QQmlPropertyData::load(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData4loadERK11QMetaMethod(
    QQmlPropertyData *self,
    const QMetaMethod *a0) {
  self->load(*a0);
}

//  QString QQmlPropertyData::name(QObject *object) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlPropertyData4nameEP7QObject(
    const QQmlPropertyData *self,
    QObject *object) {
  return new QString(self->name(object));
}

//  QString QQmlPropertyData::name(const QMetaObject *metaObject) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlPropertyData4nameEPK11QMetaObject(
    const QQmlPropertyData *self,
    const QMetaObject *metaObject) {
  return new QString(self->name(metaObject));
}

//  void QQmlPropertyData::markAsOverrideOf(QQmlPropertyData *predecessor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyData16markAsOverrideOfEPS_(
    QQmlPropertyData *self,
    QQmlPropertyData *predecessor) {
  self->markAsOverrideOf(predecessor);
}

//  bool QQmlPropertyData::resetProperty(QObject *target, WriteFlags flags)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQmlPropertyData13resetPropertyEP7QObject6QFlagsINS_9WriteFlagEE(
    const QQmlPropertyData *self,
    QObject *target,
    int flags) {
  return self->resetProperty(
      target,
      QFlags<QQmlPropertyData::WriteFlag>::fromInt(flags));
}

//  QUntypedBindable QQmlPropertyData::propertyBindable(QObject *target)
//      const
extern "C" Q_DECL_EXPORT
QUntypedBindable *ritual_ZNK16QQmlPropertyData16propertyBindableEP7QObject(
    const QQmlPropertyData *self,
    QObject *target) {
  return new QUntypedBindable(self->propertyBindable(target));
}

//  Flags QQmlPropertyData::defaultSignalFlags()
extern "C" Q_DECL_EXPORT
QQmlPropertyData::Flags *ritual_ZN16QQmlPropertyData18defaultSignalFlagsEv() {
  return new QQmlPropertyData::Flags(QQmlPropertyData::defaultSignalFlags());
}

//  Flags QQmlPropertyData::defaultSlotFlags()
extern "C" Q_DECL_EXPORT
QQmlPropertyData::Flags *ritual_ZN16QQmlPropertyData16defaultSlotFlagsEv() {
  return new QQmlPropertyData::Flags(QQmlPropertyData::defaultSlotFlags());
}

//  QQmlPropertyData::~QQmlPropertyData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlPropertyDataD1Ev(QQmlPropertyData *self) {
  delete self;
}
