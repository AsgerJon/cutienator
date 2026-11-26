//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/viewportnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/viewportnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  Qt3DRender::Render::ViewportNode::ViewportNode()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ViewportNode *ritual_ZN10Qt3DRender6Render12ViewportNodeC1Ev() {
  return new Qt3DRender::Render::ViewportNode();
}

//  float Qt3DRender::Render::ViewportNode::xMin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render12ViewportNode4xMinEv(
    const Qt3DRender::Render::ViewportNode *self) {
  return self->xMin();
}

//  void Qt3DRender::Render::ViewportNode::setXMin(float xMin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ViewportNode7setXMinEf(
    Qt3DRender::Render::ViewportNode *self,
    float xMin) {
  self->setXMin(xMin);
}

//  float Qt3DRender::Render::ViewportNode::yMin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render12ViewportNode4yMinEv(
    const Qt3DRender::Render::ViewportNode *self) {
  return self->yMin();
}

//  void Qt3DRender::Render::ViewportNode::setYMin(float yMin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ViewportNode7setYMinEf(
    Qt3DRender::Render::ViewportNode *self,
    float yMin) {
  self->setYMin(yMin);
}

//  float Qt3DRender::Render::ViewportNode::xMax() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render12ViewportNode4xMaxEv(
    const Qt3DRender::Render::ViewportNode *self) {
  return self->xMax();
}

//  void Qt3DRender::Render::ViewportNode::setXMax(float xMax)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ViewportNode7setXMaxEf(
    Qt3DRender::Render::ViewportNode *self,
    float xMax) {
  self->setXMax(xMax);
}

//  float Qt3DRender::Render::ViewportNode::yMax() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render12ViewportNode4yMaxEv(
    const Qt3DRender::Render::ViewportNode *self) {
  return self->yMax();
}

//  void Qt3DRender::Render::ViewportNode::setYMax(float yMax)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ViewportNode7setYMaxEf(
    Qt3DRender::Render::ViewportNode *self,
    float yMax) {
  self->setYMax(yMax);
}

//  float Qt3DRender::Render::ViewportNode::gamma() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render12ViewportNode5gammaEv(
    const Qt3DRender::Render::ViewportNode *self) {
  return self->gamma();
}

//  void Qt3DRender::Render::ViewportNode::setGamma(float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ViewportNode8setGammaEf(
    Qt3DRender::Render::ViewportNode *self,
    float gamma) {
  self->setGamma(gamma);
}

//  void Qt3DRender::Render::ViewportNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12ViewportNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ViewportNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QRectF Qt3DRender::Render::ViewportNode::computeViewport(const QRectF
//      &childViewport, const ViewportNode *parentViewport)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN10Qt3DRender6Render12ViewportNode15computeViewportERK6QRectFPKS1_(
    const QRectF *childViewport,
    const Qt3DRender::Render::ViewportNode *parentViewport) {
  return new QRectF(
      Qt3DRender::Render::ViewportNode::computeViewport(
          *childViewport,
          parentViewport));
}

//  void Qt3DRender::Render::ViewportNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12ViewportNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ViewportNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ViewportNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
