//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>

//  Qt3DAnimation::Animation::ChannelNameAndType::ChannelNameAndType()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelNameAndType *ritual_ZN13Qt3DAnimation9Animation18ChannelNameAndTypeC1Ev() {
  return new Qt3DAnimation::Animation::ChannelNameAndType();
}

//  Qt3DAnimation::Animation::ChannelNameAndType::ChannelNameAndType(const
//      QString &_name, int _type, int componentCount, Qt3DCore::QNodeId
//      _mappingId, int _jointIndex)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelNameAndType *ritual_ZN13Qt3DAnimation9Animation18ChannelNameAndTypeC1ERK7QStringiiN8Qt3DCore7QNodeIdEi(
    const QString *_name,
    int _type,
    int componentCount,
    const Qt3DCore::QNodeId *_mappingId,
    int _jointIndex) {
  return new Qt3DAnimation::Animation::ChannelNameAndType(
      *_name,
      _type,
      componentCount,
      *_mappingId,
      _jointIndex);
}

//  Qt3DAnimation::Animation::ChannelNameAndType::ChannelNameAndType(const
//      QString &_name, int _type, JointTransformComponent
//      _jointTransformComponent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelNameAndType *ritual_ZN13Qt3DAnimation9Animation18ChannelNameAndTypeC1ERK7QStringiNS0_23JointTransformComponentE(
    const QString *_name,
    int _type,
    Qt3DAnimation::Animation::JointTransformComponent _jointTransformComponent) {
  return new Qt3DAnimation::Animation::ChannelNameAndType(
      *_name,
      _type,
      _jointTransformComponent);
}

//  bool Qt3DAnimation::Animation::ChannelNameAndType::operator==(const
//      ChannelNameAndType &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation18ChannelNameAndTypeeqERKS1_(
    const Qt3DAnimation::Animation::ChannelNameAndType *self,
    const Qt3DAnimation::Animation::ChannelNameAndType *rhs) {
  return self->operator==(*rhs);
}

//  Qt3DAnimation::Animation::ChannelNameAndType::~ChannelNameAndType()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation18ChannelNameAndTypeD1Ev(
    Qt3DAnimation::Animation::ChannelNameAndType *self) {
  delete self;
}
