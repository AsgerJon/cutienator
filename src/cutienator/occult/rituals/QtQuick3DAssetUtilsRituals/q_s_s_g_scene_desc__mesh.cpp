//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qtquick3dassetutilsglobal_p.h>
#include <QtQuick3DAssetUtils/QtQuick3DAssetUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGSceneDesc::Mesh::Mesh(QByteArray name, qsizetype index)
extern "C" Q_DECL_EXPORT
QSSGSceneDesc::Mesh *ritual_ZN13QSSGSceneDesc4MeshC1E10QByteArrayx(
    const QByteArray *name,
    qsizetype index) {
  return new QSSGSceneDesc::Mesh(*name, index);
}

//  QSSGSceneDesc::Mesh::~Mesh()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGSceneDesc4MeshD1Ev(QSSGSceneDesc::Mesh *self) {
  delete self;
}
