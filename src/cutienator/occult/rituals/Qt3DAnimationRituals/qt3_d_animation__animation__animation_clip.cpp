//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationclip_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationclip_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>

//  void Qt3DAnimation::Animation::AnimationClip::setSource(const QUrl
//      &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip9setSourceERK4QUrl(
    Qt3DAnimation::Animation::AnimationClip *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QUrl Qt3DAnimation::Animation::AnimationClip::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13Qt3DAnimation9Animation13AnimationClip6sourceEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return new QUrl(self->source());
}

//  QAnimationClipLoader::Status
//      Qt3DAnimation::Animation::AnimationClip::status() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipLoader::Status ritual_ZNK13Qt3DAnimation9Animation13AnimationClip6statusEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return self->status();
}

//  QString Qt3DAnimation::Animation::AnimationClip::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation9Animation13AnimationClip4nameEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return new QString(self->name());
}

//  float Qt3DAnimation::Animation::AnimationClip::duration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation13AnimationClip8durationEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return self->duration();
}

//  qsizetype Qt3DAnimation::Animation::AnimationClip::channelCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13Qt3DAnimation9Animation13AnimationClip12channelCountEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return self->channelCount();
}
