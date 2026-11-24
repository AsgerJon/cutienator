//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QRhiGraphicsPipeline that Python can take functions over in. Every QRhiGraphicsPipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiGraphicsPipelineCall0)(const void *, int *);
typedef bool (*CuteQRhiGraphicsPipelineCall1)(const void *, int *);
typedef void (*CuteQRhiGraphicsPipelineCall2)(const void *, int *);
class CuteQRhiGraphicsPipeline : public QRhiGraphicsPipeline {
public:
  using QRhiGraphicsPipeline::QRhiGraphicsPipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRhiGraphicsPipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiGraphicsPipelineCall0 call = reinterpret_cast<CuteQRhiGraphicsPipelineCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiGraphicsPipeline::resourceType();
  }

  //  bool QRhiGraphicsPipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiGraphicsPipelineCall1 call = reinterpret_cast<CuteQRhiGraphicsPipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiGraphicsPipelineCall2 call = reinterpret_cast<CuteQRhiGraphicsPipelineCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK20QRhiGraphicsPipeline12resourceTypeEv(
    const QRhiGraphicsPipeline *self) {
  return self->resourceType();
}

//  Flags QRhiGraphicsPipeline::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QRhiGraphicsPipeline5flagsEv(
    const QRhiGraphicsPipeline *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QRhiGraphicsPipeline::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline8setFlagsE6QFlagsINS_4FlagEE(
    QRhiGraphicsPipeline *self,
    int f) {
  self->setFlags(QFlags<QRhiGraphicsPipeline::Flag>::fromInt(f));
}

//  Topology QRhiGraphicsPipeline::topology() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::Topology ritual_ZNK20QRhiGraphicsPipeline8topologyEv(
    const QRhiGraphicsPipeline *self) {
  return self->topology();
}

//  void QRhiGraphicsPipeline::setTopology(Topology t)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline11setTopologyENS_8TopologyE(
    QRhiGraphicsPipeline *self,
    QRhiGraphicsPipeline::Topology t) {
  self->setTopology(t);
}

//  CullMode QRhiGraphicsPipeline::cullMode() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::CullMode ritual_ZNK20QRhiGraphicsPipeline8cullModeEv(
    const QRhiGraphicsPipeline *self) {
  return self->cullMode();
}

//  void QRhiGraphicsPipeline::setCullMode(CullMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline11setCullModeENS_8CullModeE(
    QRhiGraphicsPipeline *self,
    QRhiGraphicsPipeline::CullMode mode) {
  self->setCullMode(mode);
}

//  FrontFace QRhiGraphicsPipeline::frontFace() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::FrontFace ritual_ZNK20QRhiGraphicsPipeline9frontFaceEv(
    const QRhiGraphicsPipeline *self) {
  return self->frontFace();
}

//  void QRhiGraphicsPipeline::setFrontFace(FrontFace f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline12setFrontFaceENS_9FrontFaceE(
    QRhiGraphicsPipeline *self,
    QRhiGraphicsPipeline::FrontFace f) {
  self->setFrontFace(f);
}

//  const TargetBlend *QRhiGraphicsPipeline::cbeginTargetBlends() const
extern "C" Q_DECL_EXPORT
const QRhiGraphicsPipeline::TargetBlend *ritual_ZNK20QRhiGraphicsPipeline18cbeginTargetBlendsEv(
    const QRhiGraphicsPipeline *self) {
  return self->cbeginTargetBlends();
}

//  const TargetBlend *QRhiGraphicsPipeline::cendTargetBlends() const
extern "C" Q_DECL_EXPORT
const QRhiGraphicsPipeline::TargetBlend *ritual_ZNK20QRhiGraphicsPipeline16cendTargetBlendsEv(
    const QRhiGraphicsPipeline *self) {
  return self->cendTargetBlends();
}

//  const TargetBlend *QRhiGraphicsPipeline::targetBlendAt(qsizetype index)
//      const
extern "C" Q_DECL_EXPORT
const QRhiGraphicsPipeline::TargetBlend *ritual_ZNK20QRhiGraphicsPipeline13targetBlendAtEx(
    const QRhiGraphicsPipeline *self,
    qsizetype index) {
  return self->targetBlendAt(index);
}

//  qsizetype QRhiGraphicsPipeline::targetBlendCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QRhiGraphicsPipeline16targetBlendCountEv(
    const QRhiGraphicsPipeline *self) {
  return self->targetBlendCount();
}

//  bool QRhiGraphicsPipeline::hasDepthTest() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QRhiGraphicsPipeline12hasDepthTestEv(
    const QRhiGraphicsPipeline *self) {
  return self->hasDepthTest();
}

//  void QRhiGraphicsPipeline::setDepthTest(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline12setDepthTestEb(
    QRhiGraphicsPipeline *self,
    bool enable) {
  self->setDepthTest(enable);
}

//  bool QRhiGraphicsPipeline::hasDepthWrite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QRhiGraphicsPipeline13hasDepthWriteEv(
    const QRhiGraphicsPipeline *self) {
  return self->hasDepthWrite();
}

//  void QRhiGraphicsPipeline::setDepthWrite(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline13setDepthWriteEb(
    QRhiGraphicsPipeline *self,
    bool enable) {
  self->setDepthWrite(enable);
}

//  bool QRhiGraphicsPipeline::hasDepthClamp() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QRhiGraphicsPipeline13hasDepthClampEv(
    const QRhiGraphicsPipeline *self) {
  return self->hasDepthClamp();
}

//  void QRhiGraphicsPipeline::setDepthClamp(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline13setDepthClampEb(
    QRhiGraphicsPipeline *self,
    bool enable) {
  self->setDepthClamp(enable);
}

//  CompareOp QRhiGraphicsPipeline::depthOp() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::CompareOp ritual_ZNK20QRhiGraphicsPipeline7depthOpEv(
    const QRhiGraphicsPipeline *self) {
  return self->depthOp();
}

//  void QRhiGraphicsPipeline::setDepthOp(CompareOp op)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline10setDepthOpENS_9CompareOpE(
    QRhiGraphicsPipeline *self,
    QRhiGraphicsPipeline::CompareOp op) {
  self->setDepthOp(op);
}

//  bool QRhiGraphicsPipeline::hasStencilTest() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QRhiGraphicsPipeline14hasStencilTestEv(
    const QRhiGraphicsPipeline *self) {
  return self->hasStencilTest();
}

//  void QRhiGraphicsPipeline::setStencilTest(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline14setStencilTestEb(
    QRhiGraphicsPipeline *self,
    bool enable) {
  self->setStencilTest(enable);
}

//  StencilOpState QRhiGraphicsPipeline::stencilFront() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::StencilOpState *ritual_ZNK20QRhiGraphicsPipeline12stencilFrontEv(
    const QRhiGraphicsPipeline *self) {
  return new QRhiGraphicsPipeline::StencilOpState(self->stencilFront());
}

//  void QRhiGraphicsPipeline::setStencilFront(const StencilOpState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline15setStencilFrontERKNS_14StencilOpStateE(
    QRhiGraphicsPipeline *self,
    const QRhiGraphicsPipeline::StencilOpState *state) {
  self->setStencilFront(*state);
}

//  StencilOpState QRhiGraphicsPipeline::stencilBack() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::StencilOpState *ritual_ZNK20QRhiGraphicsPipeline11stencilBackEv(
    const QRhiGraphicsPipeline *self) {
  return new QRhiGraphicsPipeline::StencilOpState(self->stencilBack());
}

//  void QRhiGraphicsPipeline::setStencilBack(const StencilOpState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline14setStencilBackERKNS_14StencilOpStateE(
    QRhiGraphicsPipeline *self,
    const QRhiGraphicsPipeline::StencilOpState *state) {
  self->setStencilBack(*state);
}

//  quint32 QRhiGraphicsPipeline::stencilReadMask() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QRhiGraphicsPipeline15stencilReadMaskEv(
    const QRhiGraphicsPipeline *self) {
  return self->stencilReadMask();
}

//  void QRhiGraphicsPipeline::setStencilReadMask(quint32 mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline18setStencilReadMaskEj(
    QRhiGraphicsPipeline *self,
    quint32 mask) {
  self->setStencilReadMask(mask);
}

//  quint32 QRhiGraphicsPipeline::stencilWriteMask() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QRhiGraphicsPipeline16stencilWriteMaskEv(
    const QRhiGraphicsPipeline *self) {
  return self->stencilWriteMask();
}

//  void QRhiGraphicsPipeline::setStencilWriteMask(quint32 mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline19setStencilWriteMaskEj(
    QRhiGraphicsPipeline *self,
    quint32 mask) {
  self->setStencilWriteMask(mask);
}

//  int QRhiGraphicsPipeline::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QRhiGraphicsPipeline11sampleCountEv(
    const QRhiGraphicsPipeline *self) {
  return self->sampleCount();
}

//  void QRhiGraphicsPipeline::setSampleCount(int s)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline14setSampleCountEi(
    QRhiGraphicsPipeline *self,
    int s) {
  self->setSampleCount(s);
}

//  float QRhiGraphicsPipeline::lineWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QRhiGraphicsPipeline9lineWidthEv(
    const QRhiGraphicsPipeline *self) {
  return self->lineWidth();
}

//  void QRhiGraphicsPipeline::setLineWidth(float width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline12setLineWidthEf(
    QRhiGraphicsPipeline *self,
    float width) {
  self->setLineWidth(width);
}

//  int QRhiGraphicsPipeline::depthBias() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QRhiGraphicsPipeline9depthBiasEv(
    const QRhiGraphicsPipeline *self) {
  return self->depthBias();
}

//  void QRhiGraphicsPipeline::setDepthBias(int bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline12setDepthBiasEi(
    QRhiGraphicsPipeline *self,
    int bias) {
  self->setDepthBias(bias);
}

//  float QRhiGraphicsPipeline::slopeScaledDepthBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK20QRhiGraphicsPipeline20slopeScaledDepthBiasEv(
    const QRhiGraphicsPipeline *self) {
  return self->slopeScaledDepthBias();
}

//  void QRhiGraphicsPipeline::setSlopeScaledDepthBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline23setSlopeScaledDepthBiasEf(
    QRhiGraphicsPipeline *self,
    float bias) {
  self->setSlopeScaledDepthBias(bias);
}

//  const QRhiShaderStage *QRhiGraphicsPipeline::cbeginShaderStages() const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK20QRhiGraphicsPipeline18cbeginShaderStagesEv(
    const QRhiGraphicsPipeline *self) {
  return self->cbeginShaderStages();
}

//  const QRhiShaderStage *QRhiGraphicsPipeline::cendShaderStages() const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK20QRhiGraphicsPipeline16cendShaderStagesEv(
    const QRhiGraphicsPipeline *self) {
  return self->cendShaderStages();
}

//  const QRhiShaderStage *QRhiGraphicsPipeline::shaderStageAt(qsizetype
//      index) const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK20QRhiGraphicsPipeline13shaderStageAtEx(
    const QRhiGraphicsPipeline *self,
    qsizetype index) {
  return self->shaderStageAt(index);
}

//  qsizetype QRhiGraphicsPipeline::shaderStageCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QRhiGraphicsPipeline16shaderStageCountEv(
    const QRhiGraphicsPipeline *self) {
  return self->shaderStageCount();
}

//  QRhiVertexInputLayout QRhiGraphicsPipeline::vertexInputLayout() const
extern "C" Q_DECL_EXPORT
QRhiVertexInputLayout *ritual_ZNK20QRhiGraphicsPipeline17vertexInputLayoutEv(
    const QRhiGraphicsPipeline *self) {
  return new QRhiVertexInputLayout(self->vertexInputLayout());
}

//  void QRhiGraphicsPipeline::setVertexInputLayout(const
//      QRhiVertexInputLayout &layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline20setVertexInputLayoutERK21QRhiVertexInputLayout(
    QRhiGraphicsPipeline *self,
    const QRhiVertexInputLayout *layout) {
  self->setVertexInputLayout(*layout);
}

//  QRhiShaderResourceBindings
//      *QRhiGraphicsPipeline::shaderResourceBindings() const
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZNK20QRhiGraphicsPipeline22shaderResourceBindingsEv(
    const QRhiGraphicsPipeline *self) {
  return self->shaderResourceBindings();
}

//  void QRhiGraphicsPipeline::setShaderResourceBindings(QRhiShaderResourceBi
//      ndings *srb)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline25setShaderResourceBindingsEP26QRhiShaderResourceBindings(
    QRhiGraphicsPipeline *self,
    QRhiShaderResourceBindings *srb) {
  self->setShaderResourceBindings(srb);
}

//  QRhiRenderPassDescriptor *QRhiGraphicsPipeline::renderPassDescriptor()
//      const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK20QRhiGraphicsPipeline20renderPassDescriptorEv(
    const QRhiGraphicsPipeline *self) {
  return self->renderPassDescriptor();
}

//  void
//      QRhiGraphicsPipeline::setRenderPassDescriptor(QRhiRenderPassDescripto
//      r *desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline23setRenderPassDescriptorEP24QRhiRenderPassDescriptor(
    QRhiGraphicsPipeline *self,
    QRhiRenderPassDescriptor *desc) {
  self->setRenderPassDescriptor(desc);
}

//  int QRhiGraphicsPipeline::patchControlPointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QRhiGraphicsPipeline22patchControlPointCountEv(
    const QRhiGraphicsPipeline *self) {
  return self->patchControlPointCount();
}

//  void QRhiGraphicsPipeline::setPatchControlPointCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline25setPatchControlPointCountEi(
    QRhiGraphicsPipeline *self,
    int count) {
  self->setPatchControlPointCount(count);
}

//  PolygonMode QRhiGraphicsPipeline::polygonMode() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::PolygonMode ritual_ZNK20QRhiGraphicsPipeline11polygonModeEv(
    const QRhiGraphicsPipeline *self) {
  return self->polygonMode();
}

//  void QRhiGraphicsPipeline::setPolygonMode(PolygonMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline14setPolygonModeENS_11PolygonModeE(
    QRhiGraphicsPipeline *self,
    QRhiGraphicsPipeline::PolygonMode mode) {
  self->setPolygonMode(mode);
}

//  int QRhiGraphicsPipeline::multiViewCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QRhiGraphicsPipeline14multiViewCountEv(
    const QRhiGraphicsPipeline *self) {
  return self->multiViewCount();
}

//  void QRhiGraphicsPipeline::setMultiViewCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRhiGraphicsPipeline17setMultiViewCountEi(
    QRhiGraphicsPipeline *self,
    int count) {
  self->setMultiViewCount(count);
}

//  bool QRhiGraphicsPipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QRhiGraphicsPipeline6createEv(QRhiGraphicsPipeline *self) {
  return self->create();
}

//  a Python function taken by a CuteQRhiGraphicsPipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiGraphicsPipeline(
    QRhiGraphicsPipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiGraphicsPipeline *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK20QRhiGraphicsPipeline12resourceTypeEv(
    const QRhiGraphicsPipeline *self) {
  return self->QRhiGraphicsPipeline::resourceType();
}
