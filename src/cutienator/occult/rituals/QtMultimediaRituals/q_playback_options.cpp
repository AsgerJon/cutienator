//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qplaybackoptions.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qplaybackoptions.h>

//  QPlaybackOptions::QPlaybackOptions()
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZN16QPlaybackOptionsC1Ev() {
  return new QPlaybackOptions();
}

//  QPlaybackOptions::QPlaybackOptions(const QPlaybackOptions &a0)
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZN16QPlaybackOptionsC1ERKS_(
    const QPlaybackOptions *a0) {
  return new QPlaybackOptions(*a0);
}

//  QPlaybackOptions &QPlaybackOptions::operator=(const QPlaybackOptions &a0)
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZN16QPlaybackOptionsaSERKS_(
    QPlaybackOptions *self,
    const QPlaybackOptions *a0) {
  return &(self->operator=(*a0));
}

//  QPlaybackOptions::QPlaybackOptions(QPlaybackOptions &&a0)
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZN16QPlaybackOptionsC1EOS_(QPlaybackOptions *a0) {
  return new QPlaybackOptions(std::move(*a0));
}

//  QPlaybackOptions &QPlaybackOptions::operator=(QPlaybackOptions &&other)
extern "C" Q_DECL_EXPORT
QPlaybackOptions *ritual_ZN16QPlaybackOptionsaSEOS_(
    QPlaybackOptions *self,
    QPlaybackOptions *other) {
  return &(self->operator=(std::move(*other)));
}

//  QPlaybackOptions::~QPlaybackOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptionsD1Ev(QPlaybackOptions *self) {
  delete self;
}

//  void QPlaybackOptions::swap(QPlaybackOptions &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions4swapERS_(
    QPlaybackOptions *self,
    QPlaybackOptions *other) {
  self->swap(*other);
}

//  std::chrono::milliseconds QPlaybackOptions::networkTimeout() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK16QPlaybackOptions14networkTimeoutEv(
    const QPlaybackOptions *self) {
  return static_cast<long long>(self->networkTimeout().count());
}

//  void QPlaybackOptions::setNetworkTimeout(std::chrono::milliseconds
//      timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions17setNetworkTimeoutENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QPlaybackOptions *self,
    long long timeout) {
  self->setNetworkTimeout(std::chrono::milliseconds(timeout));
}

//  void QPlaybackOptions::resetNetworkTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions19resetNetworkTimeoutEv(
    QPlaybackOptions *self) {
  self->resetNetworkTimeout();
}

//  PlaybackIntent QPlaybackOptions::playbackIntent() const
extern "C" Q_DECL_EXPORT
QPlaybackOptions::PlaybackIntent ritual_ZNK16QPlaybackOptions14playbackIntentEv(
    const QPlaybackOptions *self) {
  return self->playbackIntent();
}

//  void QPlaybackOptions::setPlaybackIntent(PlaybackIntent intent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions17setPlaybackIntentENS_14PlaybackIntentE(
    QPlaybackOptions *self,
    QPlaybackOptions::PlaybackIntent intent) {
  self->setPlaybackIntent(intent);
}

//  void QPlaybackOptions::resetPlaybackIntent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions19resetPlaybackIntentEv(
    QPlaybackOptions *self) {
  self->resetPlaybackIntent();
}

//  qsizetype QPlaybackOptions::probeSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QPlaybackOptions9probeSizeEv(
    const QPlaybackOptions *self) {
  return self->probeSize();
}

//  void QPlaybackOptions::setProbeSize(qsizetype probeSizeBytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions12setProbeSizeEx(
    QPlaybackOptions *self,
    qsizetype probeSizeBytes) {
  self->setProbeSize(probeSizeBytes);
}

//  void QPlaybackOptions::resetProbeSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlaybackOptions14resetProbeSizeEv(QPlaybackOptions *self) {
  self->resetProbeSize();
}

//  bool operator==(const QPlaybackOptions &lhs, const QPlaybackOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QPlaybackOptionsS1_(
    const QPlaybackOptions *lhs,
    const QPlaybackOptions *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaybackOptions &lhs, const QPlaybackOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QPlaybackOptionsS1_(
    const QPlaybackOptions *lhs,
    const QPlaybackOptions *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QPlaybackOptions &lhs, const QPlaybackOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK16QPlaybackOptionsS1_(
    const QPlaybackOptions *lhs,
    const QPlaybackOptions *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QPlaybackOptions &lhs, const QPlaybackOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK16QPlaybackOptionsS1_(
    const QPlaybackOptions *lhs,
    const QPlaybackOptions *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QPlaybackOptions &lhs, const QPlaybackOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK16QPlaybackOptionsS1_(
    const QPlaybackOptions *lhs,
    const QPlaybackOptions *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QPlaybackOptions &lhs, const QPlaybackOptions &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK16QPlaybackOptionsS1_(
    const QPlaybackOptions *lhs,
    const QPlaybackOptions *rhs) {
  return operator>=(*lhs, *rhs);
}
