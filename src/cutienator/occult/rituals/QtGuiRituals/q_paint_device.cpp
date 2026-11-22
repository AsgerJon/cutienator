//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintdevice.h>

//  QPaintDevice::~QPaintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPaintDeviceD1Ev(QPaintDevice *self) {
  delete self;
}

//  int QPaintDevice::devType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice7devTypeEv(const QPaintDevice *self) {
  return self->devType();
}

//  bool QPaintDevice::paintingActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPaintDevice14paintingActiveEv(const QPaintDevice *self) {
  return self->paintingActive();
}

//  QPaintEngine *QPaintDevice::paintEngine() const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK12QPaintDevice11paintEngineEv(
    const QPaintDevice *self) {
  return self->paintEngine();
}

//  int QPaintDevice::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice5widthEv(const QPaintDevice *self) {
  return self->width();
}

//  int QPaintDevice::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice6heightEv(const QPaintDevice *self) {
  return self->height();
}

//  int QPaintDevice::widthMM() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice7widthMMEv(const QPaintDevice *self) {
  return self->widthMM();
}

//  int QPaintDevice::heightMM() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice8heightMMEv(const QPaintDevice *self) {
  return self->heightMM();
}

//  int QPaintDevice::logicalDpiX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice11logicalDpiXEv(const QPaintDevice *self) {
  return self->logicalDpiX();
}

//  int QPaintDevice::logicalDpiY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice11logicalDpiYEv(const QPaintDevice *self) {
  return self->logicalDpiY();
}

//  int QPaintDevice::physicalDpiX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice12physicalDpiXEv(const QPaintDevice *self) {
  return self->physicalDpiX();
}

//  int QPaintDevice::physicalDpiY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice12physicalDpiYEv(const QPaintDevice *self) {
  return self->physicalDpiY();
}

//  qreal QPaintDevice::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPaintDevice16devicePixelRatioEv(
    const QPaintDevice *self) {
  return self->devicePixelRatio();
}

//  qreal QPaintDevice::devicePixelRatioF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPaintDevice17devicePixelRatioFEv(
    const QPaintDevice *self) {
  return self->devicePixelRatioF();
}

//  int QPaintDevice::colorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice10colorCountEv(const QPaintDevice *self) {
  return self->colorCount();
}

//  int QPaintDevice::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPaintDevice5depthEv(const QPaintDevice *self) {
  return self->depth();
}

//  qreal QPaintDevice::devicePixelRatioFScale()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN12QPaintDevice22devicePixelRatioFScaleEv() {
  return QPaintDevice::devicePixelRatioFScale();
}

//  int QPaintDevice::encodeMetricF(PaintDeviceMetric metric, double value)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QPaintDevice13encodeMetricFENS_17PaintDeviceMetricEd(
    QPaintDevice::PaintDeviceMetric metric,
    double value) {
  return QPaintDevice::encodeMetricF(metric, value);
}
