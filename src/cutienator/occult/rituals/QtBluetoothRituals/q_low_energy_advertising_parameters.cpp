//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergyadvertisingparameters.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtBluetooth/qlowenergyadvertisingparameters.h>

//  QLowEnergyAdvertisingParameters::QLowEnergyAdvertisingParameters()
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingParameters *ritual_ZN31QLowEnergyAdvertisingParametersC1Ev() {
  return new QLowEnergyAdvertisingParameters();
}

//  QLowEnergyAdvertisingParameters::QLowEnergyAdvertisingParameters(const
//      QLowEnergyAdvertisingParameters &other)
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingParameters *ritual_ZN31QLowEnergyAdvertisingParametersC1ERKS_(
    const QLowEnergyAdvertisingParameters *other) {
  return new QLowEnergyAdvertisingParameters(*other);
}

//  QLowEnergyAdvertisingParameters::~QLowEnergyAdvertisingParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QLowEnergyAdvertisingParametersD1Ev(
    QLowEnergyAdvertisingParameters *self) {
  delete self;
}

//  bool operator==(const QLowEnergyAdvertisingParameters &a, const
//      QLowEnergyAdvertisingParameters &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK31QLowEnergyAdvertisingParametersS1_(
    const QLowEnergyAdvertisingParameters *a,
    const QLowEnergyAdvertisingParameters *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyAdvertisingParameters &a, const
//      QLowEnergyAdvertisingParameters &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK31QLowEnergyAdvertisingParametersS1_(
    const QLowEnergyAdvertisingParameters *a,
    const QLowEnergyAdvertisingParameters *b) {
  return operator!=(*a, *b);
}

//  void QLowEnergyAdvertisingParameters::setMode(Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QLowEnergyAdvertisingParameters7setModeENS_4ModeE(
    QLowEnergyAdvertisingParameters *self,
    QLowEnergyAdvertisingParameters::Mode mode) {
  self->setMode(mode);
}

//  Mode QLowEnergyAdvertisingParameters::mode() const
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingParameters::Mode ritual_ZNK31QLowEnergyAdvertisingParameters4modeEv(
    const QLowEnergyAdvertisingParameters *self) {
  return self->mode();
}

//  FilterPolicy QLowEnergyAdvertisingParameters::filterPolicy() const
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingParameters::FilterPolicy ritual_ZNK31QLowEnergyAdvertisingParameters12filterPolicyEv(
    const QLowEnergyAdvertisingParameters *self) {
  return self->filterPolicy();
}

//  void QLowEnergyAdvertisingParameters::setInterval(quint16 minimum,
//      quint16 maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QLowEnergyAdvertisingParameters11setIntervalEtt(
    QLowEnergyAdvertisingParameters *self,
    quint16 minimum,
    quint16 maximum) {
  self->setInterval(minimum, maximum);
}

//  int QLowEnergyAdvertisingParameters::minimumInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QLowEnergyAdvertisingParameters15minimumIntervalEv(
    const QLowEnergyAdvertisingParameters *self) {
  return self->minimumInterval();
}

//  int QLowEnergyAdvertisingParameters::maximumInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QLowEnergyAdvertisingParameters15maximumIntervalEv(
    const QLowEnergyAdvertisingParameters *self) {
  return self->maximumInterval();
}

//  bool QLowEnergyAdvertisingParameters::equals(const
//      QLowEnergyAdvertisingParameters &a, const
//      QLowEnergyAdvertisingParameters &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QLowEnergyAdvertisingParameters6equalsERKS_S1_(
    const QLowEnergyAdvertisingParameters *a,
    const QLowEnergyAdvertisingParameters *b) {
  return QLowEnergyAdvertisingParameters::equals(*a, *b);
}
