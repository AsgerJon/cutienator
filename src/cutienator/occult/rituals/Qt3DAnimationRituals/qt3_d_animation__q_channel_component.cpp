//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qchannelcomponent.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qchannelcomponent.h>
#include <QtCore/qstring.h>
#include <Qt3DAnimation/qkeyframe.h>
#include <Qt3DAnimation/Qt3DAnimation>

//  Qt3DAnimation::QChannelComponent::QChannelComponent()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent *ritual_ZN13Qt3DAnimation17QChannelComponentC1Ev() {
  return new Qt3DAnimation::QChannelComponent();
}

//  Qt3DAnimation::QChannelComponent::QChannelComponent(const QString &name)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent *ritual_ZN13Qt3DAnimation17QChannelComponentC1ERK7QString(
    const QString *name) {
  return new Qt3DAnimation::QChannelComponent(*name);
}

//  Qt3DAnimation::QChannelComponent::QChannelComponent(const
//      QChannelComponent &a0)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent *ritual_ZN13Qt3DAnimation17QChannelComponentC1ERKS0_(
    const Qt3DAnimation::QChannelComponent *a0) {
  return new Qt3DAnimation::QChannelComponent(*a0);
}

//  QChannelComponent &Qt3DAnimation::QChannelComponent::operator=(const
//      QChannelComponent &a0)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent *ritual_ZN13Qt3DAnimation17QChannelComponentaSERKS0_(
    Qt3DAnimation::QChannelComponent *self,
    const Qt3DAnimation::QChannelComponent *a0) {
  return &(self->operator=(*a0));
}

//  Qt3DAnimation::QChannelComponent::~QChannelComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation17QChannelComponentD1Ev(
    Qt3DAnimation::QChannelComponent *self) {
  delete self;
}

//  void Qt3DAnimation::QChannelComponent::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation17QChannelComponent7setNameERK7QString(
    Qt3DAnimation::QChannelComponent *self,
    const QString *name) {
  self->setName(*name);
}

//  QString Qt3DAnimation::QChannelComponent::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation17QChannelComponent4nameEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return new QString(self->name());
}

//  int Qt3DAnimation::QChannelComponent::keyFrameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation17QChannelComponent13keyFrameCountEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return self->keyFrameCount();
}

//  void Qt3DAnimation::QChannelComponent::appendKeyFrame(const QKeyFrame
//      &kf)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation17QChannelComponent14appendKeyFrameERKNS_9QKeyFrameE(
    Qt3DAnimation::QChannelComponent *self,
    const Qt3DAnimation::QKeyFrame *kf) {
  self->appendKeyFrame(*kf);
}

//  void Qt3DAnimation::QChannelComponent::insertKeyFrame(int index, const
//      QKeyFrame &kf)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation17QChannelComponent14insertKeyFrameEiRKNS_9QKeyFrameE(
    Qt3DAnimation::QChannelComponent *self,
    int index,
    const Qt3DAnimation::QKeyFrame *kf) {
  self->insertKeyFrame(index, *kf);
}

//  void Qt3DAnimation::QChannelComponent::removeKeyFrame(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation17QChannelComponent14removeKeyFrameEi(
    Qt3DAnimation::QChannelComponent *self,
    int index) {
  self->removeKeyFrame(index);
}

//  void Qt3DAnimation::QChannelComponent::clearKeyFrames()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation17QChannelComponent14clearKeyFramesEv(
    Qt3DAnimation::QChannelComponent *self) {
  self->clearKeyFrames();
}

//  const_iterator Qt3DAnimation::QChannelComponent::begin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_iterator ritual_ZNK13Qt3DAnimation17QChannelComponent5beginEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return self->begin();
}

//  const_iterator Qt3DAnimation::QChannelComponent::cbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_iterator ritual_ZNK13Qt3DAnimation17QChannelComponent6cbeginEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return self->cbegin();
}

//  const_iterator Qt3DAnimation::QChannelComponent::end() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_iterator ritual_ZNK13Qt3DAnimation17QChannelComponent3endEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return self->end();
}

//  const_iterator Qt3DAnimation::QChannelComponent::cend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_iterator ritual_ZNK13Qt3DAnimation17QChannelComponent4cendEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return self->cend();
}

//  const_reverse_iterator Qt3DAnimation::QChannelComponent::rbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_reverse_iterator *ritual_ZNK13Qt3DAnimation17QChannelComponent6rbeginEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return new Qt3DAnimation::QChannelComponent::const_reverse_iterator(
      self->rbegin());
}

//  const_reverse_iterator Qt3DAnimation::QChannelComponent::crbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_reverse_iterator *ritual_ZNK13Qt3DAnimation17QChannelComponent7crbeginEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return new Qt3DAnimation::QChannelComponent::const_reverse_iterator(
      self->crbegin());
}

//  const_reverse_iterator Qt3DAnimation::QChannelComponent::rend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_reverse_iterator *ritual_ZNK13Qt3DAnimation17QChannelComponent4rendEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return new Qt3DAnimation::QChannelComponent::const_reverse_iterator(
      self->rend());
}

//  const_reverse_iterator Qt3DAnimation::QChannelComponent::crend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelComponent::const_reverse_iterator *ritual_ZNK13Qt3DAnimation17QChannelComponent5crendEv(
    const Qt3DAnimation::QChannelComponent *self) {
  return new Qt3DAnimation::QChannelComponent::const_reverse_iterator(
      self->crend());
}

//  bool operator==(const QChannelComponent &a0, const QChannelComponent &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationeqERKNS_17QChannelComponentES2_(
    const Qt3DAnimation::QChannelComponent *a0,
    const Qt3DAnimation::QChannelComponent *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(const QChannelComponent &a0, const QChannelComponent &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationneERKNS_17QChannelComponentES2_(
    const Qt3DAnimation::QChannelComponent *a0,
    const Qt3DAnimation::QChannelComponent *a1) {
  return operator!=(*a0, *a1);
}

//  a Qt3DAnimation::QChannelComponent::const_reverse_iterator a ritual of
//      Qt3DAnimation::QChannelComponent gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QChannelComponent__Qt3DAnimation_QChannelComponent_const_reverse_iterator(
    Qt3DAnimation::QChannelComponent::const_reverse_iterator *self) {
  delete self;
}
