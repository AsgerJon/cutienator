//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGeoCameraCapabilities::QGeoCameraCapabilities()
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZN22QGeoCameraCapabilitiesC1Ev() {
  return new QGeoCameraCapabilities();
}

//  QGeoCameraCapabilities::QGeoCameraCapabilities(const
//      QGeoCameraCapabilities &other)
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZN22QGeoCameraCapabilitiesC1ERKS_(
    const QGeoCameraCapabilities *other) {
  return new QGeoCameraCapabilities(*other);
}

//  QGeoCameraCapabilities::QGeoCameraCapabilities(QGeoCameraCapabilities
//      &&other)
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZN22QGeoCameraCapabilitiesC1EOS_(
    QGeoCameraCapabilities *other) {
  return new QGeoCameraCapabilities(std::move(*other));
}

//  QGeoCameraCapabilities::~QGeoCameraCapabilities()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilitiesD1Ev(QGeoCameraCapabilities *self) {
  delete self;
}

//  QGeoCameraCapabilities &QGeoCameraCapabilities::operator=(const
//      QGeoCameraCapabilities &other)
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZN22QGeoCameraCapabilitiesaSERKS_(
    QGeoCameraCapabilities *self,
    const QGeoCameraCapabilities *other) {
  return &(self->operator=(*other));
}

//  QGeoCameraCapabilities
//      &QGeoCameraCapabilities::operator=(QGeoCameraCapabilities &&other)
extern "C" Q_DECL_EXPORT
QGeoCameraCapabilities *ritual_ZN22QGeoCameraCapabilitiesaSEOS_(
    QGeoCameraCapabilities *self,
    QGeoCameraCapabilities *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QGeoCameraCapabilities::swap(QGeoCameraCapabilities &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities4swapERS_(
    QGeoCameraCapabilities *self,
    QGeoCameraCapabilities *other) {
  self->swap(*other);
}

//  bool operator==(const QGeoCameraCapabilities &lhs, const
//      QGeoCameraCapabilities &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK22QGeoCameraCapabilitiesS1_(
    const QGeoCameraCapabilities *lhs,
    const QGeoCameraCapabilities *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoCameraCapabilities &lhs, const
//      QGeoCameraCapabilities &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK22QGeoCameraCapabilitiesS1_(
    const QGeoCameraCapabilities *lhs,
    const QGeoCameraCapabilities *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QGeoCameraCapabilities::setTileSize(int tileSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities11setTileSizeEi(
    QGeoCameraCapabilities *self,
    int tileSize) {
  self->setTileSize(tileSize);
}

//  int QGeoCameraCapabilities::tileSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QGeoCameraCapabilities8tileSizeEv(
    const QGeoCameraCapabilities *self) {
  return self->tileSize();
}

//  void QGeoCameraCapabilities::setMinimumZoomLevel(double minimumZoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities19setMinimumZoomLevelEd(
    QGeoCameraCapabilities *self,
    double minimumZoomLevel) {
  self->setMinimumZoomLevel(minimumZoomLevel);
}

//  double QGeoCameraCapabilities::minimumZoomLevel() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities16minimumZoomLevelEv(
    const QGeoCameraCapabilities *self) {
  return self->minimumZoomLevel();
}

//  double QGeoCameraCapabilities::minimumZoomLevelAt256() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities21minimumZoomLevelAt256Ev(
    const QGeoCameraCapabilities *self) {
  return self->minimumZoomLevelAt256();
}

//  void QGeoCameraCapabilities::setMaximumZoomLevel(double maximumZoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities19setMaximumZoomLevelEd(
    QGeoCameraCapabilities *self,
    double maximumZoomLevel) {
  self->setMaximumZoomLevel(maximumZoomLevel);
}

//  double QGeoCameraCapabilities::maximumZoomLevel() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities16maximumZoomLevelEv(
    const QGeoCameraCapabilities *self) {
  return self->maximumZoomLevel();
}

//  double QGeoCameraCapabilities::maximumZoomLevelAt256() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities21maximumZoomLevelAt256Ev(
    const QGeoCameraCapabilities *self) {
  return self->maximumZoomLevelAt256();
}

//  void QGeoCameraCapabilities::setSupportsBearing(bool supportsBearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities18setSupportsBearingEb(
    QGeoCameraCapabilities *self,
    bool supportsBearing) {
  self->setSupportsBearing(supportsBearing);
}

//  bool QGeoCameraCapabilities::supportsBearing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGeoCameraCapabilities15supportsBearingEv(
    const QGeoCameraCapabilities *self) {
  return self->supportsBearing();
}

//  void QGeoCameraCapabilities::setSupportsRolling(bool supportsRolling)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities18setSupportsRollingEb(
    QGeoCameraCapabilities *self,
    bool supportsRolling) {
  self->setSupportsRolling(supportsRolling);
}

//  bool QGeoCameraCapabilities::supportsRolling() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGeoCameraCapabilities15supportsRollingEv(
    const QGeoCameraCapabilities *self) {
  return self->supportsRolling();
}

//  void QGeoCameraCapabilities::setSupportsTilting(bool supportsTilting)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities18setSupportsTiltingEb(
    QGeoCameraCapabilities *self,
    bool supportsTilting) {
  self->setSupportsTilting(supportsTilting);
}

//  bool QGeoCameraCapabilities::supportsTilting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGeoCameraCapabilities15supportsTiltingEv(
    const QGeoCameraCapabilities *self) {
  return self->supportsTilting();
}

//  void QGeoCameraCapabilities::setMinimumTilt(double minimumTilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities14setMinimumTiltEd(
    QGeoCameraCapabilities *self,
    double minimumTilt) {
  self->setMinimumTilt(minimumTilt);
}

//  double QGeoCameraCapabilities::minimumTilt() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities11minimumTiltEv(
    const QGeoCameraCapabilities *self) {
  return self->minimumTilt();
}

//  void QGeoCameraCapabilities::setMaximumTilt(double maximumTilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities14setMaximumTiltEd(
    QGeoCameraCapabilities *self,
    double maximumTilt) {
  self->setMaximumTilt(maximumTilt);
}

//  double QGeoCameraCapabilities::maximumTilt() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities11maximumTiltEv(
    const QGeoCameraCapabilities *self) {
  return self->maximumTilt();
}

//  void QGeoCameraCapabilities::setMinimumFieldOfView(double
//      minimumFieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities21setMinimumFieldOfViewEd(
    QGeoCameraCapabilities *self,
    double minimumFieldOfView) {
  self->setMinimumFieldOfView(minimumFieldOfView);
}

//  double QGeoCameraCapabilities::minimumFieldOfView() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities18minimumFieldOfViewEv(
    const QGeoCameraCapabilities *self) {
  return self->minimumFieldOfView();
}

//  void QGeoCameraCapabilities::setMaximumFieldOfView(double
//      maximumFieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities21setMaximumFieldOfViewEd(
    QGeoCameraCapabilities *self,
    double maximumFieldOfView) {
  self->setMaximumFieldOfView(maximumFieldOfView);
}

//  double QGeoCameraCapabilities::maximumFieldOfView() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK22QGeoCameraCapabilities18maximumFieldOfViewEv(
    const QGeoCameraCapabilities *self) {
  return self->maximumFieldOfView();
}

//  void QGeoCameraCapabilities::setOverzoomEnabled(bool overzoomEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraCapabilities18setOverzoomEnabledEb(
    QGeoCameraCapabilities *self,
    bool overzoomEnabled) {
  self->setOverzoomEnabled(overzoomEnabled);
}

//  bool QGeoCameraCapabilities::overzoomEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGeoCameraCapabilities15overzoomEnabledEv(
    const QGeoCameraCapabilities *self) {
  return self->overzoomEnabled();
}

//  bool QGeoCameraCapabilities::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGeoCameraCapabilities7isValidEv(
    const QGeoCameraCapabilities *self) {
  return self->isValid();
}

//  bool QGeoCameraCapabilities::isEqual(const QGeoCameraCapabilities &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGeoCameraCapabilities7isEqualERKS_(
    const QGeoCameraCapabilities *self,
    const QGeoCameraCapabilities *other) {
  return self->isEqual(*other);
}
