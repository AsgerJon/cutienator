//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderMesh::QSSGRenderMesh(QSSGRenderDrawMode inDrawMode,
//      QSSGRenderWinding inWinding)
extern "C" Q_DECL_EXPORT
QSSGRenderMesh *ritual_ZN14QSSGRenderMeshC1E18QSSGRenderDrawMode17QSSGRenderWinding(
    QSSGRenderDrawMode inDrawMode,
    QSSGRenderWinding inWinding) {
  return new QSSGRenderMesh(inDrawMode, inWinding);
}
