//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qanimationclipdata.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DAnimation/qanimationclipdata.h>
#include <QtCore/qstring.h>
#include <Qt3DAnimation/qchannel.h>
#include <Qt3DAnimation/Qt3DAnimation>

//  Qt3DAnimation::QAnimationClipData::QAnimationClipData()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData *ritual_ZN13Qt3DAnimation18QAnimationClipDataC1Ev() {
  return new Qt3DAnimation::QAnimationClipData();
}

//  Qt3DAnimation::QAnimationClipData::QAnimationClipData(const
//      QAnimationClipData &a0)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData *ritual_ZN13Qt3DAnimation18QAnimationClipDataC1ERKS0_(
    const Qt3DAnimation::QAnimationClipData *a0) {
  return new Qt3DAnimation::QAnimationClipData(*a0);
}

//  QAnimationClipData &Qt3DAnimation::QAnimationClipData::operator=(const
//      QAnimationClipData &a0)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData *ritual_ZN13Qt3DAnimation18QAnimationClipDataaSERKS0_(
    Qt3DAnimation::QAnimationClipData *self,
    const Qt3DAnimation::QAnimationClipData *a0) {
  return &(self->operator=(*a0));
}

//  Qt3DAnimation::QAnimationClipData::~QAnimationClipData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationClipDataD1Ev(
    Qt3DAnimation::QAnimationClipData *self) {
  delete self;
}

//  void Qt3DAnimation::QAnimationClipData::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationClipData7setNameERK7QString(
    Qt3DAnimation::QAnimationClipData *self,
    const QString *name) {
  self->setName(*name);
}

//  QString Qt3DAnimation::QAnimationClipData::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation18QAnimationClipData4nameEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return new QString(self->name());
}

//  int Qt3DAnimation::QAnimationClipData::channelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation18QAnimationClipData12channelCountEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return self->channelCount();
}

//  void Qt3DAnimation::QAnimationClipData::appendChannel(const QChannel &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationClipData13appendChannelERKNS_8QChannelE(
    Qt3DAnimation::QAnimationClipData *self,
    const Qt3DAnimation::QChannel *c) {
  self->appendChannel(*c);
}

//  void Qt3DAnimation::QAnimationClipData::insertChannel(int index, const
//      QChannel &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationClipData13insertChannelEiRKNS_8QChannelE(
    Qt3DAnimation::QAnimationClipData *self,
    int index,
    const Qt3DAnimation::QChannel *c) {
  self->insertChannel(index, *c);
}

//  void Qt3DAnimation::QAnimationClipData::removeChannel(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationClipData13removeChannelEi(
    Qt3DAnimation::QAnimationClipData *self,
    int index) {
  self->removeChannel(index);
}

//  void Qt3DAnimation::QAnimationClipData::clearChannels()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation18QAnimationClipData13clearChannelsEv(
    Qt3DAnimation::QAnimationClipData *self) {
  self->clearChannels();
}

//  bool Qt3DAnimation::QAnimationClipData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation18QAnimationClipData7isValidEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return self->isValid();
}

//  const_iterator Qt3DAnimation::QAnimationClipData::begin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_iterator ritual_ZNK13Qt3DAnimation18QAnimationClipData5beginEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return self->begin();
}

//  const_iterator Qt3DAnimation::QAnimationClipData::cbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_iterator ritual_ZNK13Qt3DAnimation18QAnimationClipData6cbeginEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return self->cbegin();
}

//  const_iterator Qt3DAnimation::QAnimationClipData::end() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_iterator ritual_ZNK13Qt3DAnimation18QAnimationClipData3endEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return self->end();
}

//  const_iterator Qt3DAnimation::QAnimationClipData::cend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_iterator ritual_ZNK13Qt3DAnimation18QAnimationClipData4cendEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return self->cend();
}

//  const_reverse_iterator Qt3DAnimation::QAnimationClipData::rbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_reverse_iterator *ritual_ZNK13Qt3DAnimation18QAnimationClipData6rbeginEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return new Qt3DAnimation::QAnimationClipData::const_reverse_iterator(
      self->rbegin());
}

//  const_reverse_iterator Qt3DAnimation::QAnimationClipData::crbegin() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_reverse_iterator *ritual_ZNK13Qt3DAnimation18QAnimationClipData7crbeginEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return new Qt3DAnimation::QAnimationClipData::const_reverse_iterator(
      self->crbegin());
}

//  const_reverse_iterator Qt3DAnimation::QAnimationClipData::rend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_reverse_iterator *ritual_ZNK13Qt3DAnimation18QAnimationClipData4rendEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return new Qt3DAnimation::QAnimationClipData::const_reverse_iterator(
      self->rend());
}

//  const_reverse_iterator Qt3DAnimation::QAnimationClipData::crend() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipData::const_reverse_iterator *ritual_ZNK13Qt3DAnimation18QAnimationClipData5crendEv(
    const Qt3DAnimation::QAnimationClipData *self) {
  return new Qt3DAnimation::QAnimationClipData::const_reverse_iterator(
      self->crend());
}

//  bool operator==(const QAnimationClipData &a0, const QAnimationClipData
//      &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationeqERKNS_18QAnimationClipDataES2_(
    const Qt3DAnimation::QAnimationClipData *a0,
    const Qt3DAnimation::QAnimationClipData *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(const QAnimationClipData &a0, const QAnimationClipData
//      &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationneERKNS_18QAnimationClipDataES2_(
    const Qt3DAnimation::QAnimationClipData *a0,
    const Qt3DAnimation::QAnimationClipData *a1) {
  return operator!=(*a0, *a1);
}

//  a Qt3DAnimation::QAnimationClipData::const_reverse_iterator a ritual of
//      Qt3DAnimation::QAnimationClipData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_QAnimationClipData__Qt3DAnimation_QAnimationClipData_const_reverse_iterator(
    Qt3DAnimation::QAnimationClipData::const_reverse_iterator *self) {
  delete self;
}
