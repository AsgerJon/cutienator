//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/channelmapping_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/channelmapping_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/channelmapping_p.h>
#include <Qt3DAnimation/qchannelmapping.h>
#include <Qt3DAnimation/qskeletonmapping.h>
#include <Qt3DAnimation/qcallbackmapping.h>
#include <Qt3DAnimation/private/qcallbackmapping_p.h>
#include <Qt3DAnimation/private/qchannelmapping_p.h>
#include <Qt3DAnimation/private/qskeletonmapping_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DCore/qabstractskeleton.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapping.cpp, line 46, as _ZN13Qt3DAnimation9Animation14ChannelMapping16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void ChannelMapping::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAbstractChannelMapping *node = qobject_cast<const QAbstractChannelMapping *>(frontEnd);
    if (!node)
        return;

    const QChannelMapping *channelMapping = qobject_cast<const QChannelMapping *>(frontEnd);
    if (channelMapping) {
        m_mappingType = ChannelMappingType;
        m_channelName = channelMapping->channelName();
        m_targetId = Qt3DCore::qIdForNode(channelMapping->target());

        QChannelMappingPrivate *d = static_cast<QChannelMappingPrivate *>(Qt3DCore::QNodePrivate::get(const_cast<QChannelMapping *>(channelMapping)));
        m_type = d->m_type;
        m_propertyName = d->m_propertyName;
        m_componentCount = d->m_componentCount;
    }

    const QSkeletonMapping *skeletonMapping = qobject_cast<const QSkeletonMapping *>(frontEnd);
    if (skeletonMapping) {
        m_mappingType = SkeletonMappingType;
        m_skeletonId = Qt3DCore::qIdForNode(skeletonMapping->skeleton());
    }

    const QCallbackMapping *callbackMapping = qobject_cast<const QCallbackMapping *>(frontEnd);
    if (callbackMapping) {
        m_mappingType = ChannelMappingType;
        m_channelName = callbackMapping->channelName();

        const QCallbackMappingPrivate *d = static_cast<const QCallbackMappingPrivate *>(Qt3DCore::QNodePrivate::get(callbackMapping));
        m_type = d->m_type;
        m_callback = d->m_callback;
        m_callbackFlags = d->m_callbackFlags;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    Q_UNUSED(firstTime);

    d_ptr->setEnabled(frontEnd->isEnabled());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapping.cpp, line 20, as _ZN13Qt3DAnimation9Animation14ChannelMappingC1Ev
namespace Qt3DAnimation::Animation {
inline ChannelMapping::ChannelMapping()
    : BackendNode(ReadOnly)
    , m_channelName()
    , m_targetId()
    , m_type(static_cast<int>(QMetaType::UnknownType))
    , m_componentCount(0)
    , m_propertyName(nullptr)
    , m_callback(nullptr)
    , m_skeletonId()
    , m_mappingType(MappingType::ChannelMappingType)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapping.cpp, line 33, as _ZN13Qt3DAnimation9Animation14ChannelMapping7cleanupEv
namespace Qt3DAnimation::Animation {
inline void ChannelMapping::cleanup()
{
    setEnabled(false);
    m_channelName.clear();
    m_targetId = Qt3DCore::QNodeId();
    m_type = static_cast<int>(QMetaType::UnknownType);
    m_propertyName = nullptr;
    m_componentCount = 0;
    m_callback = nullptr;
    m_callbackFlags = {};
    m_skeletonId = Qt3DCore::QNodeId();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapping.cpp, line 83, as _ZNK13Qt3DAnimation9Animation14ChannelMapping8skeletonEv
namespace Qt3DAnimation::Animation {
inline Skeleton *ChannelMapping::skeleton() const
{
    return m_handler->skeletonManager()->lookupResource(m_skeletonId);
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::ChannelMapping::ChannelMapping()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelMapping *ritual_ZN13Qt3DAnimation9Animation14ChannelMappingC1Ev() {
  return new Qt3DAnimation::Animation::ChannelMapping();
}

//  void Qt3DAnimation::Animation::ChannelMapping::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping7cleanupEv(
    Qt3DAnimation::Animation::ChannelMapping *self) {
  self->cleanup();
}

//  void Qt3DAnimation::Animation::ChannelMapping::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ChannelMapping *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DAnimation::Animation::ChannelMapping::setChannelName(const
//      QString &channelName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping14setChannelNameERK7QString(
    Qt3DAnimation::Animation::ChannelMapping *self,
    const QString *channelName) {
  self->setChannelName(*channelName);
}

//  QString Qt3DAnimation::Animation::ChannelMapping::channelName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping11channelNameEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return new QString(self->channelName());
}

//  void
//      Qt3DAnimation::Animation::ChannelMapping::setTargetId(Qt3DCore::QNode
//      Id targetId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping11setTargetIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ChannelMapping *self,
    const Qt3DCore::QNodeId *targetId) {
  self->setTargetId(*targetId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ChannelMapping::targetId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping8targetIdEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return new Qt3DCore::QNodeId(self->targetId());
}

//  void Qt3DAnimation::Animation::ChannelMapping::setType(int type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping7setTypeEi(
    Qt3DAnimation::Animation::ChannelMapping *self,
    int type) {
  self->setType(type);
}

//  int Qt3DAnimation::Animation::ChannelMapping::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping4typeEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return self->type();
}

//  void Qt3DAnimation::Animation::ChannelMapping::setPropertyName(const char
//      *propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping15setPropertyNameEPKc(
    Qt3DAnimation::Animation::ChannelMapping *self,
    const char *propertyName) {
  self->setPropertyName(propertyName);
}

//  const char *Qt3DAnimation::Animation::ChannelMapping::propertyName()
//      const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping12propertyNameEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return self->propertyName();
}

//  void Qt3DAnimation::Animation::ChannelMapping::setComponentCount(int
//      componentCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping17setComponentCountEi(
    Qt3DAnimation::Animation::ChannelMapping *self,
    int componentCount) {
  self->setComponentCount(componentCount);
}

//  int Qt3DAnimation::Animation::ChannelMapping::componentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping14componentCountEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return self->componentCount();
}

//  void
//      Qt3DAnimation::Animation::ChannelMapping::setCallback(QAnimationCallb
//      ack *callback)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping11setCallbackEPNS_18QAnimationCallbackE(
    Qt3DAnimation::Animation::ChannelMapping *self,
    Qt3DAnimation::QAnimationCallback *callback) {
  self->setCallback(callback);
}

//  QAnimationCallback *Qt3DAnimation::Animation::ChannelMapping::callback()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationCallback *ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping8callbackEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return self->callback();
}

//  void Qt3DAnimation::Animation::ChannelMapping::setCallbackFlags(QAnimatio
//      nCallback::Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping16setCallbackFlagsE6QFlagsINS_18QAnimationCallback4FlagEE(
    Qt3DAnimation::Animation::ChannelMapping *self,
    int flags) {
  self->setCallbackFlags(
      QFlags<Qt3DAnimation::QAnimationCallback::Flag>::fromInt(flags));
}

//  QAnimationCallback::Flags
//      Qt3DAnimation::Animation::ChannelMapping::callbackFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping13callbackFlagsEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return static_cast<int>(self->callbackFlags().toInt());
}

//  void
//      Qt3DAnimation::Animation::ChannelMapping::setSkeletonId(Qt3DCore::QNo
//      deId skeletonId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping13setSkeletonIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ChannelMapping *self,
    const Qt3DCore::QNodeId *skeletonId) {
  self->setSkeletonId(*skeletonId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ChannelMapping::skeletonId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping10skeletonIdEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return new Qt3DCore::QNodeId(self->skeletonId());
}

//  Skeleton *Qt3DAnimation::Animation::ChannelMapping::skeleton() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Skeleton *ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping8skeletonEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return self->skeleton();
}

//  void Qt3DAnimation::Animation::ChannelMapping::setMappingType(MappingType
//      mappingType)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ChannelMapping14setMappingTypeENS1_11MappingTypeE(
    Qt3DAnimation::Animation::ChannelMapping *self,
    Qt3DAnimation::Animation::ChannelMapping::MappingType mappingType) {
  self->setMappingType(mappingType);
}

//  MappingType Qt3DAnimation::Animation::ChannelMapping::mappingType() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelMapping::MappingType ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping11mappingTypeEv(
    const Qt3DAnimation::Animation::ChannelMapping *self) {
  return self->mappingType();
}

//  void Qt3DAnimation::Animation::ChannelMapping::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation14ChannelMapping16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ChannelMapping *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::ChannelMapping::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
