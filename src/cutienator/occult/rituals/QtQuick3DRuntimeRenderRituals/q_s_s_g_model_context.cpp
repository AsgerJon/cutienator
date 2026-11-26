//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterialshadergenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderableobjects.cpp, line 19, as _ZN16QSSGModelContextC1ERK15QSSGRenderModelRK10QMatrix4x4RK14QGenericMatrixILi3ELi3EfERKSt5arrayIS3_Lm2EE
inline QSSGModelContext::QSSGModelContext(const QSSGRenderModel &inModel,
                                   const QMatrix4x4 &inGlobalTransform,
                                   const QMatrix3x3 &inNormalMatrix,
                                   const QSSGRenderMvpArray &inModelViewProjections)
    : model(inModel)
    , globalTransform(inGlobalTransform)
    , normalMatrix(inNormalMatrix)
    , modelViewProjections(inModelViewProjections)
{

}
//  -----------------------------------------------------------------------

//  QSSGModelContext::QSSGModelContext(const QSSGRenderModel &inModel, const
//      QMatrix4x4 &globalTransform, const QMatrix3x3 &inNormalMatrix, const
//      QSSGRenderMvpArray &inModelViewProjections)
extern "C" Q_DECL_EXPORT
QSSGModelContext *ritual_ZN16QSSGModelContextC1ERK15QSSGRenderModelRK10QMatrix4x4RK14QGenericMatrixILi3ELi3EfERKSt5arrayIS3_Lm2EE(
    const QSSGRenderModel *inModel,
    const QMatrix4x4 *globalTransform,
    const QMatrix3x3 *inNormalMatrix,
    const QSSGRenderMvpArray *inModelViewProjections) {
  return new QSSGModelContext(
      *inModel,
      *globalTransform,
      *inNormalMatrix,
      *inModelViewProjections);
}
