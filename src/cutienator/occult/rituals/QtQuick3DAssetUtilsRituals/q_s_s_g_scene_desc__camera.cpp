//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGSceneDesc::Camera::Camera(RuntimeType rt)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Camera *ritual_ZN13QSSGSceneDesc6CameraC1EN21QSSGRenderGraphObject4TypeE(
    QSSGSceneDesc::Node::RuntimeType rt) {
  return new QSSGSceneDesc::Camera(rt);
}

//  QSSGSceneDesc::Camera::~Camera()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc6CameraD1Ev(QSSGSceneDesc::Camera *self) {
  delete self;
}
