//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <array>

//  QRhiViewport::QRhiViewport()
extern "C" Q_DECL_EXPORT
QRhiViewport *ritual_ZN12QRhiViewportC1Ev() {
  return new QRhiViewport();
}

//  QRhiViewport::QRhiViewport(float x, float y, float w, float h, float
//      minDepth, float maxDepth)
extern "C" Q_DECL_EXPORT
QRhiViewport *ritual_ZN12QRhiViewportC1Effffff(
    float x,
    float y,
    float w,
    float h,
    float minDepth,
    float maxDepth) {
  return new QRhiViewport(x, y, w, h, minDepth, maxDepth);
}

//  std::array<float, 4> QRhiViewport::viewport() const
extern "C" Q_DECL_EXPORT
std::array<float, 4> *ritual_ZNK12QRhiViewport8viewportEv(
    const QRhiViewport *self) {
  return new std::array<float, 4>(self->viewport());
}

//  void QRhiViewport::setViewport(float x, float y, float w, float h)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiViewport11setViewportEffff(
    QRhiViewport *self,
    float x,
    float y,
    float w,
    float h) {
  self->setViewport(x, y, w, h);
}

//  float QRhiViewport::minDepth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QRhiViewport8minDepthEv(const QRhiViewport *self) {
  return self->minDepth();
}

//  void QRhiViewport::setMinDepth(float minDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiViewport11setMinDepthEf(
    QRhiViewport *self,
    float minDepth) {
  self->setMinDepth(minDepth);
}

//  float QRhiViewport::maxDepth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QRhiViewport8maxDepthEv(const QRhiViewport *self) {
  return self->maxDepth();
}

//  void QRhiViewport::setMaxDepth(float maxDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiViewport11setMaxDepthEf(
    QRhiViewport *self,
    float maxDepth) {
  self->setMaxDepth(maxDepth);
}

//  bool operator==(const QRhiViewport &a, const QRhiViewport &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QRhiViewportS1_(
    const QRhiViewport *a,
    const QRhiViewport *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiViewport &a, const QRhiViewport &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QRhiViewportS1_(
    const QRhiViewport *a,
    const QRhiViewport *b) {
  return operator!=(*a, *b);
}

//  QRhiViewport::~QRhiViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QRhiViewportD1Ev(QRhiViewport *self) {
  delete self;
}

//  a std::array<float, 4> a ritual of QRhiViewport gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRhiViewport__std_array_float_4(
    std::array<float, 4> *self) {
  delete self;
}
