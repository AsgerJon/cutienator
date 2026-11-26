//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderCamera::QSSGRenderCamera(QSSGRenderGraphObject::Type type)
extern "C" Q_DECL_EXPORT
QSSGRenderCamera *ritual_ZN16QSSGRenderCameraC1EN21QSSGRenderGraphObject4TypeE(
    QSSGRenderGraphObject::Type type) {
  return new QSSGRenderCamera(type);
}

//  void QSSGRenderCamera::lookAt(const QVector3D &inCameraPos, const
//      QVector3D &inUpDir, const QVector3D &inTargetPos, const QVector3D
//      &pivot)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera6lookAtERK9QVector3DS2_S2_S2_(
    QSSGRenderCamera *self,
    const QVector3D *inCameraPos,
    const QVector3D *inUpDir,
    const QVector3D *inTargetPos,
    const QVector3D *pivot) {
  self->lookAt(*inCameraPos, *inUpDir, *inTargetPos, *pivot);
}

//  bool QSSGRenderCamera::calculateProjectionInternal(QSSGRenderCamera
//      &camera, const QRectF &inViewport, Configuration config)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSSGRenderCamera27calculateProjectionInternalERS_RK6QRectF29QSSGRenderCameraConfiguration(
    QSSGRenderCamera *camera,
    const QRectF *inViewport,
    const QSSGRenderCameraConfiguration *config) {
  return QSSGRenderCamera::calculateProjectionInternal(
      *camera,
      *inViewport,
      *config);
}

//  bool QSSGRenderCamera::calculateProjection(const QRectF &inViewport,
//      Configuration config)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSSGRenderCamera19calculateProjectionERK6QRectF29QSSGRenderCameraConfiguration(
    QSSGRenderCamera *self,
    const QRectF *inViewport,
    const QSSGRenderCameraConfiguration *config) {
  return self->calculateProjection(*inViewport, *config);
}

//  bool QSSGRenderCamera::computeFrustumOrtho(QRectF inViewport,
//      QSSGRenderCamera::ClipPlanes clipPlanes,
//      QSSGRenderCamera::Magnification magnification, Configuration config,
//      QMatrix4x4 &outProjection)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSSGRenderCamera19computeFrustumOrthoE6QRectFNS_10ClipPlanesENS_13MagnificationE29QSSGRenderCameraConfigurationR10QMatrix4x4(
    const QRectF *inViewport,
    const QSSGRenderCamera::ClipPlanes *clipPlanes,
    const QSSGRenderCamera::Magnification *magnification,
    const QSSGRenderCameraConfiguration *config,
    QMatrix4x4 *outProjection) {
  return QSSGRenderCamera::computeFrustumOrtho(
      *inViewport,
      *clipPlanes,
      *magnification,
      *config,
      *outProjection);
}

//  bool QSSGRenderCamera::computeFrustumPerspective(QRectF inViewport,
//      FieldOfView fov, QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4
//      &outProjection)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSSGRenderCamera25computeFrustumPerspectiveE6QRectF27QSSGRenderCameraFieldOfViewNS_10ClipPlanesER10QMatrix4x4(
    const QRectF *inViewport,
    const QSSGRenderCameraFieldOfView *fov,
    const QSSGRenderCamera::ClipPlanes *clipPlanes,
    QMatrix4x4 *outProjection) {
  return QSSGRenderCamera::computeFrustumPerspective(
      *inViewport,
      *fov,
      *clipPlanes,
      *outProjection);
}

//  bool QSSGRenderCamera::computeCustomFrustum(QSSGRenderCamera::Frustum
//      frustum, QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4
//      &outProjection)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSSGRenderCamera20computeCustomFrustumENS_7FrustumENS_10ClipPlanesER10QMatrix4x4(
    const QSSGRenderCamera::Frustum *frustum,
    const QSSGRenderCamera::ClipPlanes *clipPlanes,
    QMatrix4x4 *outProjection) {
  return QSSGRenderCamera::computeCustomFrustum(
      *frustum,
      *clipPlanes,
      *outProjection);
}

//  void QSSGRenderCamera::calculateViewProjectionMatrix(const QMatrix4x4
//      &globalTransform, const QMatrix4x4 &projection, QMatrix4x4
//      &outMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera29calculateViewProjectionMatrixERK10QMatrix4x4S2_RS0_(
    const QMatrix4x4 *globalTransform,
    const QMatrix4x4 *projection,
    QMatrix4x4 *outMatrix) {
  QSSGRenderCamera::calculateViewProjectionMatrix(
      *globalTransform,
      *projection,
      *outMatrix);
}

//  void QSSGRenderCamera::calculateViewProjectionMatrix(const QMatrix4x4
//      &globalTransform, QMatrix4x4 &outMatrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QSSGRenderCamera29calculateViewProjectionMatrixERK10QMatrix4x4RS0_(
    const QSSGRenderCamera *self,
    const QMatrix4x4 *globalTransform,
    QMatrix4x4 *outMatrix) {
  self->calculateViewProjectionMatrix(*globalTransform, *outMatrix);
}

//  void QSSGRenderCamera::calculateViewProjectionWithoutTranslation(const
//      QMatrix4x4 &globalTransform, float near, float far, QMatrix4x4
//      &outMatrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QSSGRenderCamera41calculateViewProjectionWithoutTranslationERK10QMatrix4x4ffRS0_(
    const QSSGRenderCamera *self,
    const QMatrix4x4 *globalTransform,
    float near,
    float far,
    QMatrix4x4 *outMatrix) {
  self->calculateViewProjectionWithoutTranslation(
      *globalTransform,
      near,
      far,
      *outMatrix);
}

//  QSSGRenderRay QSSGRenderCamera::unproject(const QMatrix4x4
//      &globalTransform, const QVector2D &inLayerRelativeMouseCoords, const
//      QRectF &inViewport) const
extern "C" Q_DECL_EXPORT
QSSGRenderRay *ritual_ZNK16QSSGRenderCamera9unprojectERK10QMatrix4x4RK9QVector2DRK6QRectF(
    const QSSGRenderCamera *self,
    const QMatrix4x4 *globalTransform,
    const QVector2D *inLayerRelativeMouseCoords,
    const QRectF *inViewport) {
  return new QSSGRenderRay(
      self->unproject(
          *globalTransform,
          *inLayerRelativeMouseCoords,
          *inViewport));
}

//  bool QSSGRenderCamera::isDirty(DirtyFlag dirtyFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSSGRenderCamera7isDirtyENS_9DirtyFlagE(
    const QSSGRenderCamera *self,
    QSSGRenderCamera::DirtyFlag dirtyFlag) {
  return self->isDirty(dirtyFlag);
}

//  void QSSGRenderCamera::markDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera9markDirtyENS_9DirtyFlagE(
    QSSGRenderCamera *self,
    QSSGRenderCamera::DirtyFlag dirtyFlag) {
  self->markDirty(dirtyFlag);
}

//  void QSSGRenderCamera::clearDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera10clearDirtyENS_9DirtyFlagE(
    QSSGRenderCamera *self,
    QSSGRenderCamera::DirtyFlag dirtyFlag) {
  self->clearDirty(dirtyFlag);
}

//  float QSSGRenderCamera::getLevelOfDetailMultiplier() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSSGRenderCamera26getLevelOfDetailMultiplierEv(
    const QSSGRenderCamera *self) {
  return self->getLevelOfDetailMultiplier();
}

//  float QSSGRenderCamera::getDpr() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSSGRenderCamera6getDprEv(const QSSGRenderCamera *self) {
  return self->getDpr();
}
