//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qchannel.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qchannel.h>
#include <QtCore/qstring.h>
#include <Qt3DAnimation/qchannelcomponent.h>
#include <Qt3DAnimation/Qt3DAnimation>

//  Qt3DAnimation::QChannel::QChannel()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel *ritual_ZN13Qt3DAnimation8QChannelC1Ev() {
  return new Qt3DAnimation::QChannel();
}

//  Qt3DAnimation::QChannel::QChannel(const QString &name)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel *ritual_ZN13Qt3DAnimation8QChannelC1ERK7QString(
    const QString *name) {
  return new Qt3DAnimation::QChannel(*name);
}

//  Qt3DAnimation::QChannel::QChannel(const QChannel &a0)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel *ritual_ZN13Qt3DAnimation8QChannelC1ERKS0_(
    const Qt3DAnimation::QChannel *a0) {
  return new Qt3DAnimation::QChannel(*a0);
}

//  QChannel &Qt3DAnimation::QChannel::operator=(const QChannel &a0)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel *ritual_ZN13Qt3DAnimation8QChannelaSERKS0_(
    Qt3DAnimation::QChannel *self,
    const Qt3DAnimation::QChannel *a0) {
  return &(self->operator=(*a0));
}

//  Qt3DAnimation::QChannel::~QChannel()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannelD1Ev(Qt3DAnimation::QChannel *self) {
  delete self;
}

//  void Qt3DAnimation::QChannel::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannel7setNameERK7QString(
    Qt3DAnimation::QChannel *self,
    const QString *name) {
  self->setName(*name);
}

//  QString Qt3DAnimation::QChannel::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation8QChannel4nameEv(
    const Qt3DAnimation::QChannel *self) {
  return new QString(self->name());
}

//  void Qt3DAnimation::QChannel::setJointIndex(int jointIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannel13setJointIndexEi(
    Qt3DAnimation::QChannel *self,
    int jointIndex) {
  self->setJointIndex(jointIndex);
}

//  int Qt3DAnimation::QChannel::jointIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation8QChannel10jointIndexEv(
    const Qt3DAnimation::QChannel *self) {
  return self->jointIndex();
}

//  int Qt3DAnimation::QChannel::channelComponentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation8QChannel21channelComponentCountEv(
    const Qt3DAnimation::QChannel *self) {
  return self->channelComponentCount();
}

//  void Qt3DAnimation::QChannel::appendChannelComponent(const
//      QChannelComponent &component)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannel22appendChannelComponentERKNS_17QChannelComponentE(
    Qt3DAnimation::QChannel *self,
    const Qt3DAnimation::QChannelComponent *component) {
  self->appendChannelComponent(*component);
}

//  void Qt3DAnimation::QChannel::insertChannelComponent(int index, const
//      QChannelComponent &component)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannel22insertChannelComponentEiRKNS_17QChannelComponentE(
    Qt3DAnimation::QChannel *self,
    int index,
    const Qt3DAnimation::QChannelComponent *component) {
  self->insertChannelComponent(index, *component);
}

//  void Qt3DAnimation::QChannel::removeChannelComponent(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannel22removeChannelComponentEi(
    Qt3DAnimation::QChannel *self,
    int index) {
  self->removeChannelComponent(index);
}

//  void Qt3DAnimation::QChannel::clearChannelComponents()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation8QChannel22clearChannelComponentsEv(
    Qt3DAnimation::QChannel *self) {
  self->clearChannelComponents();
}

//  const_iterator Qt3DAnimation::QChannel::begin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_iterator ritual_ZNK13Qt3DAnimation8QChannel5beginEv(
    const Qt3DAnimation::QChannel *self) {
  return self->begin();
}

//  const_iterator Qt3DAnimation::QChannel::cbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_iterator ritual_ZNK13Qt3DAnimation8QChannel6cbeginEv(
    const Qt3DAnimation::QChannel *self) {
  return self->cbegin();
}

//  const_iterator Qt3DAnimation::QChannel::end() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_iterator ritual_ZNK13Qt3DAnimation8QChannel3endEv(
    const Qt3DAnimation::QChannel *self) {
  return self->end();
}

//  const_iterator Qt3DAnimation::QChannel::cend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_iterator ritual_ZNK13Qt3DAnimation8QChannel4cendEv(
    const Qt3DAnimation::QChannel *self) {
  return self->cend();
}

//  const_reverse_iterator Qt3DAnimation::QChannel::rbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_reverse_iterator *ritual_ZNK13Qt3DAnimation8QChannel6rbeginEv(
    const Qt3DAnimation::QChannel *self) {
  return new Qt3DAnimation::QChannel::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator Qt3DAnimation::QChannel::crbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_reverse_iterator *ritual_ZNK13Qt3DAnimation8QChannel7crbeginEv(
    const Qt3DAnimation::QChannel *self) {
  return new Qt3DAnimation::QChannel::const_reverse_iterator(
      self->crbegin());
}

//  const_reverse_iterator Qt3DAnimation::QChannel::rend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_reverse_iterator *ritual_ZNK13Qt3DAnimation8QChannel4rendEv(
    const Qt3DAnimation::QChannel *self) {
  return new Qt3DAnimation::QChannel::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator Qt3DAnimation::QChannel::crend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannel::const_reverse_iterator *ritual_ZNK13Qt3DAnimation8QChannel5crendEv(
    const Qt3DAnimation::QChannel *self) {
  return new Qt3DAnimation::QChannel::const_reverse_iterator(self->crend());
}

//  bool operator==(const QChannel &a0, const QChannel &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationeqERKNS_8QChannelES2_(
    const Qt3DAnimation::QChannel *a0,
    const Qt3DAnimation::QChannel *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(const QChannel &a0, const QChannel &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationneERKNS_8QChannelES2_(
    const Qt3DAnimation::QChannel *a0,
    const Qt3DAnimation::QChannel *a1) {
  return operator!=(*a0, *a1);
}

//  a Qt3DAnimation::QChannel::const_reverse_iterator a ritual of
//      Qt3DAnimation::QChannel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QChannel__Qt3DAnimation_QChannel_const_reverse_iterator(
    Qt3DAnimation::QChannel::const_reverse_iterator *self) {
  delete self;
}
