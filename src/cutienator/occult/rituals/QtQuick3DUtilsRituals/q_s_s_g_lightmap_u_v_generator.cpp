//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssglightmapuvgenerator_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssglightmapuvgenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QSSGLightmapUVGeneratorResult QSSGLightmapUVGenerator::run(const
//      QByteArray &positions, const QByteArray &normals, const QByteArray
//      &uv0, const QByteArray &index, QSSGMesh::Mesh::ComponentType
//      indexComponentType, float texelsPerUnit)
extern "C" Q_DECL_EXPORT
QSSGLightmapUVGeneratorResult *ritual_ZN23QSSGLightmapUVGenerator3runERK10QByteArrayS2_S2_S2_23QSSGRenderComponentTypef(
    QSSGLightmapUVGenerator *self,
    const QByteArray *positions,
    const QByteArray *normals,
    const QByteArray *uv0,
    const QByteArray *index,
    QSSGMesh::Mesh::ComponentType indexComponentType,
    float texelsPerUnit) {
  return new QSSGLightmapUVGeneratorResult(
      self->run(
          *positions,
          *normals,
          *uv0,
          *index,
          indexComponentType,
          texelsPerUnit));
}

//  QSSGLightmapUVGenerator::~QSSGLightmapUVGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGLightmapUVGeneratorD1Ev(QSSGLightmapUVGenerator *self) {
  delete self;
}
