//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGSceneDesc::Texture::Texture(Node::RuntimeType rt, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Texture *ritual_ZN13QSSGSceneDesc7TextureC1EN21QSSGRenderGraphObject4TypeERK10QByteArray(
    QSSGSceneDesc::Node::RuntimeType rt,
    const QByteArray *name) {
  return new QSSGSceneDesc::Texture(rt, *name);
}

//  QSSGSceneDesc::Texture::~Texture()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc7TextureD1Ev(QSSGSceneDesc::Texture *self) {
  delete self;
}
