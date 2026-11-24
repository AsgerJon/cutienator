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
