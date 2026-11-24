//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshaderresourcemergecon
//  text_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshaderresourcemergecontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  void
//      QSSGShaderResourceMergeContext::registerInput(QSSGShaderGeneratorStag
//      e stage, const QByteArray &type, const QByteArray &name, bool flat)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSSGShaderResourceMergeContext13registerInputE24QSSGShaderGeneratorStageRK10QByteArrayS3_b(
    QSSGShaderResourceMergeContext *self,
    QSSGShaderGeneratorStage stage,
    const QByteArray *type,
    const QByteArray *name,
    bool flat) {
  self->registerInput(stage, *type, *name, flat);
}

//  void
//      QSSGShaderResourceMergeContext::registerOutput(QSSGShaderGeneratorSta
//      ge stage, const QByteArray &type, const QByteArray &name, bool flat)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSSGShaderResourceMergeContext14registerOutputE24QSSGShaderGeneratorStageRK10QByteArrayS3_b(
    QSSGShaderResourceMergeContext *self,
    QSSGShaderGeneratorStage stage,
    const QByteArray *type,
    const QByteArray *name,
    bool flat) {
  self->registerOutput(stage, *type, *name, flat);
}

//  void QSSGShaderResourceMergeContext::registerSampler(const QByteArray
//      &type, const QByteArray &name,
//      QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
//      QByteArray &conditionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSSGShaderResourceMergeContext15registerSamplerERK10QByteArrayS2_N24QSSGRenderShaderMetadata7Uniform9ConditionES2_(
    QSSGShaderResourceMergeContext *self,
    const QByteArray *type,
    const QByteArray *name,
    QSSGRenderShaderMetadata::Uniform::Condition conditionType,
    const QByteArray *conditionName) {
  self->registerSampler(*type, *name, conditionType, *conditionName);
}

//  void QSSGShaderResourceMergeContext::registerImage(const QByteArray
//      &type, const QByteArray &name, const QByteArray &imgtype, const
//      QByteArray &qualifiers, QSSGRenderShaderMetadata::Uniform::Condition
//      conditionType, const QByteArray &conditionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSSGShaderResourceMergeContext13registerImageERK10QByteArrayS2_S2_S2_N24QSSGRenderShaderMetadata7Uniform9ConditionES2_(
    QSSGShaderResourceMergeContext *self,
    const QByteArray *type,
    const QByteArray *name,
    const QByteArray *imgtype,
    const QByteArray *qualifiers,
    QSSGRenderShaderMetadata::Uniform::Condition conditionType,
    const QByteArray *conditionName) {
  self->registerImage(
      *type,
      *name,
      *imgtype,
      *qualifiers,
      conditionType,
      *conditionName);
}

//  void QSSGShaderResourceMergeContext::registerUniformMember(const
//      QByteArray &type, const QByteArray &name,
//      QSSGRenderShaderMetadata::Uniform::Condition conditionType, const
//      QByteArray &conditionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSSGShaderResourceMergeContext21registerUniformMemberERK10QByteArrayS2_N24QSSGRenderShaderMetadata7Uniform9ConditionES2_(
    QSSGShaderResourceMergeContext *self,
    const QByteArray *type,
    const QByteArray *name,
    QSSGRenderShaderMetadata::Uniform::Condition conditionType,
    const QByteArray *conditionName) {
  self->registerUniformMember(*type, *name, conditionType, *conditionName);
}

//  QSSGShaderResourceMergeContext::~QSSGShaderResourceMergeContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QSSGShaderResourceMergeContextD1Ev(
    QSSGShaderResourceMergeContext *self) {
  delete self;
}
