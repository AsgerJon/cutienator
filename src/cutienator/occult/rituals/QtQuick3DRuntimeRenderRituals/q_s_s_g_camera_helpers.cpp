//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderhelpers.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtGui/QMatrix4x4>

//  QMatrix4x4 QSSGCameraHelpers::getViewProjectionMatrix(const QSSGCameraId
//      cameraId, const QMatrix4x4 *globalTransform)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN17QSSGCameraHelpers23getViewProjectionMatrixE12QSSGCameraIdPK10QMatrix4x4(
    const QSSGCameraId *cameraId,
    const QMatrix4x4 *globalTransform) {
  return new QMatrix4x4(
      QSSGCameraHelpers::getViewProjectionMatrix(
          *cameraId,
          globalTransform));
}

//  QSSGCameraHelpers::~QSSGCameraHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSSGCameraHelpersD1Ev(QSSGCameraHelpers *self) {
  delete self;
}
