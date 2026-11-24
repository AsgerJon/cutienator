//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGComputePipelineStateKey QSSGComputePipelineStateKey::create(const
//      QShader &shader, const QRhiShaderResourceBindings *srb)
extern "C" Q_DECL_EXPORT
QSSGComputePipelineStateKey *ritual_ZN27QSSGComputePipelineStateKey6createERK7QShaderPK26QRhiShaderResourceBindings(
    const QShader *shader,
    const QRhiShaderResourceBindings *srb) {
  return new QSSGComputePipelineStateKey(
      QSSGComputePipelineStateKey::create(
          *shader,
          srb));
}

//  QSSGComputePipelineStateKey::~QSSGComputePipelineStateKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGComputePipelineStateKeyD1Ev(
    QSSGComputePipelineStateKey *self) {
  delete self;
}
