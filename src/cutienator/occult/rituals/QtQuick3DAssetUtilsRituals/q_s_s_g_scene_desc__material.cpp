//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGSceneDesc::Material::Material(Node::RuntimeType rt)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Material *ritual_ZN13QSSGSceneDesc8MaterialC1EN21QSSGRenderGraphObject4TypeE(
    QSSGSceneDesc::Node::RuntimeType rt) {
  return new QSSGSceneDesc::Material(rt);
}

//  QSSGSceneDesc::Material::~Material()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc8MaterialD1Ev(QSSGSceneDesc::Material *self) {
  delete self;
}
