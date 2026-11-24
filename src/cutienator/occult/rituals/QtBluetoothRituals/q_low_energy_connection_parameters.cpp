//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergyconnectionparameters.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtBluetooth/qlowenergyconnectionparameters.h>

//  QLowEnergyConnectionParameters::QLowEnergyConnectionParameters()
extern "C" Q_DECL_EXPORT
QLowEnergyConnectionParameters *ritual_ZN30QLowEnergyConnectionParametersC1Ev() {
  return new QLowEnergyConnectionParameters();
}

//  QLowEnergyConnectionParameters::QLowEnergyConnectionParameters(const
//      QLowEnergyConnectionParameters &other)
extern "C" Q_DECL_EXPORT
QLowEnergyConnectionParameters *ritual_ZN30QLowEnergyConnectionParametersC1ERKS_(
    const QLowEnergyConnectionParameters *other) {
  return new QLowEnergyConnectionParameters(*other);
}

//  QLowEnergyConnectionParameters::~QLowEnergyConnectionParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QLowEnergyConnectionParametersD1Ev(
    QLowEnergyConnectionParameters *self) {
  delete self;
}

//  bool operator==(const QLowEnergyConnectionParameters &a, const
//      QLowEnergyConnectionParameters &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK30QLowEnergyConnectionParametersS1_(
    const QLowEnergyConnectionParameters *a,
    const QLowEnergyConnectionParameters *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyConnectionParameters &a, const
//      QLowEnergyConnectionParameters &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK30QLowEnergyConnectionParametersS1_(
    const QLowEnergyConnectionParameters *a,
    const QLowEnergyConnectionParameters *b) {
  return operator!=(*a, *b);
}

//  void QLowEnergyConnectionParameters::setIntervalRange(double minimum,
//      double maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QLowEnergyConnectionParameters16setIntervalRangeEdd(
    QLowEnergyConnectionParameters *self,
    double minimum,
    double maximum) {
  self->setIntervalRange(minimum, maximum);
}

//  double QLowEnergyConnectionParameters::minimumInterval() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK30QLowEnergyConnectionParameters15minimumIntervalEv(
    const QLowEnergyConnectionParameters *self) {
  return self->minimumInterval();
}

//  double QLowEnergyConnectionParameters::maximumInterval() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK30QLowEnergyConnectionParameters15maximumIntervalEv(
    const QLowEnergyConnectionParameters *self) {
  return self->maximumInterval();
}

//  void QLowEnergyConnectionParameters::setLatency(int latency)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QLowEnergyConnectionParameters10setLatencyEi(
    QLowEnergyConnectionParameters *self,
    int latency) {
  self->setLatency(latency);
}

//  int QLowEnergyConnectionParameters::latency() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QLowEnergyConnectionParameters7latencyEv(
    const QLowEnergyConnectionParameters *self) {
  return self->latency();
}

//  void QLowEnergyConnectionParameters::setSupervisionTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QLowEnergyConnectionParameters21setSupervisionTimeoutEi(
    QLowEnergyConnectionParameters *self,
    int timeout) {
  self->setSupervisionTimeout(timeout);
}

//  int QLowEnergyConnectionParameters::supervisionTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QLowEnergyConnectionParameters18supervisionTimeoutEv(
    const QLowEnergyConnectionParameters *self) {
  return self->supervisionTimeout();
}

//  bool QLowEnergyConnectionParameters::equals(const
//      QLowEnergyConnectionParameters &a, const
//      QLowEnergyConnectionParameters &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QLowEnergyConnectionParameters6equalsERKS_S1_(
    const QLowEnergyConnectionParameters *a,
    const QLowEnergyConnectionParameters *b) {
  return QLowEnergyConnectionParameters::equals(*a, *b);
}
