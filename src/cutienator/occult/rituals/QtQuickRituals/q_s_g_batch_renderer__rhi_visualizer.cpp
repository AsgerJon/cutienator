//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhivisualizer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhivisualizer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgbatchrenderer_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QElapsedTimer>
#include <QtCore/QtNumeric>
#include <QtGui/QGuiApplication>
#include <QtCore/private/qnumeric_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtQuick/private/qsgrhivisualizer_p.h>
#include <QtQuick/private/qsgnode_p.h>
#include <algorithm>
#include <QtQuick/private/qsgrhivisualizer_p.h>
#include <QtCore/qmath.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 48, as local:qsgbatchrenderer.cpp:SHADOWNODE_TRAVERSE
#define SHADOWNODE_TRAVERSE(NODE) for (Node *child = NODE->firstChild(); child; child = child->sibling())

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 4327, as local:qsgbatchrenderer.cpp:QSGNODE_DIRTY_PARENT
#define QSGNODE_DIRTY_PARENT (QSGNode::DirtyNodeAdded \

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 150, as local:qsgrhivisualizer.cpp:ubufVisibility
namespace QSGBatchRenderer {
const QRhiShaderResourceBinding::StageFlags ubufVisibility =
        QRhiShaderResourceBinding::VertexStage | QRhiShaderResourceBinding::FragmentStage;
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 251, as local:qsgrhivisualizer.cpp:aligned
namespace QSGBatchRenderer {
static inline uint aligned(uint v, uint byteAlign)
{
    return (v + byteAlign - 1) & ~(byteAlign - 1);
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 4317, as _ZN16QSGBatchRenderer10VisualizerC2EPNS_8RendererE
namespace QSGBatchRenderer {
inline Visualizer::Visualizer(Renderer *renderer)
    : m_renderer(renderer),
      m_visualizeMode(VisualizeNothing)
{
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 4323, as _ZN16QSGBatchRenderer10VisualizerD2Ev
namespace QSGBatchRenderer {
inline Visualizer::~Visualizer()
{
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 50, as _ZN16QSGBatchRenderer13RhiVisualizer16prepareVisualizeEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::prepareVisualize()
{
    // Called before the render pass has begun (but after preparing the
    // batches). Now is the time to put resource updates to the renderer's
    // current m_resourceUpdates instance.

    if (m_visualizeMode == VisualizeNothing)
        return;

    if (!m_vs.isValid()) {
        m_vs = QSGMaterialShaderPrivate::loadShader(
                    QLatin1String(":/qt-project.org/scenegraph/shaders_ng/visualization.vert.qsb"));
        m_fs = QSGMaterialShaderPrivate::loadShader(
                    QLatin1String(":/qt-project.org/scenegraph/shaders_ng/visualization.frag.qsb"));
    }

    m_fade.prepare(this, m_renderer->m_rhi, m_renderer->m_resourceUpdates, m_renderer->renderTarget().rpDesc);

    const bool forceUintIndex = m_renderer->m_uint32IndexForRhi;

    switch (m_visualizeMode) {
    case VisualizeBatches:
        m_batchVis.prepare(m_renderer->m_opaqueBatches, m_renderer->m_alphaBatches,
                           this,
                           m_renderer->m_rhi, m_renderer->m_resourceUpdates,
                           forceUintIndex);
        break;
    case VisualizeClipping:
        m_clipVis.prepare(m_renderer->rootNode(), this,
                          m_renderer->m_rhi, m_renderer->m_resourceUpdates);
        break;
    case VisualizeChanges:
        m_changeVis.prepare(m_renderer->m_nodes.value(m_renderer->rootNode()),
                            this,
                            m_renderer->m_rhi, m_renderer->m_resourceUpdates);
        m_visualizeChangeSet.clear();
        break;
    case VisualizeOverdraw:
        m_overdrawVis.prepare(m_renderer->m_nodes.value(m_renderer->rootNode()),
                              this,
                              m_renderer->m_rhi, m_renderer->m_resourceUpdates);
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 38, as _ZN16QSGBatchRenderer13RhiVisualizer16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::releaseResources()
{
    m_pipelines.releaseResources();

    m_fade.releaseResources();

    m_changeVis.releaseResources();
    m_batchVis.releaseResources();
    m_clipVis.releaseResources();
    m_overdrawVis.releaseResources();
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 98, as _ZN16QSGBatchRenderer13RhiVisualizer9visualizeEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::visualize()
{
    if (m_visualizeMode == VisualizeNothing)
        return;

    QRhiCommandBuffer *cb = m_renderer->renderTarget().cb;
    m_fade.render(cb);

    switch (m_visualizeMode) {
    case VisualizeBatches:
        m_batchVis.render(cb);
        break;
    case VisualizeClipping:
        m_clipVis.render(cb);
        break;
    case VisualizeChanges:
        m_changeVis.render(cb);
        break;
    case VisualizeOverdraw:
        m_overdrawVis.render(cb);
        break;
    default:
        Q_UNREACHABLE();
        break;
    }
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 270, as _ZN16QSGBatchRenderer13RhiVisualizer13PipelineCache8pipelineEPS0_P4QRhiP26QRhiShaderResourceBindingsP24QRhiRenderPassDescriptorN20QRhiGraphicsPipeline8TopologyEN24QRhiVertexInputAttribute6FormatEjb
namespace QSGBatchRenderer {
inline QRhiGraphicsPipeline *RhiVisualizer::PipelineCache::pipeline(RhiVisualizer *visualizer,
                                                             QRhi *rhi,
                                                             QRhiShaderResourceBindings *srb,
                                                             QRhiRenderPassDescriptor *rpDesc,
                                                             QRhiGraphicsPipeline::Topology topology,
                                                             QRhiVertexInputAttribute::Format vertexFormat,
                                                             quint32 vertexStride,
                                                             bool blendOneOne)
{
    for (int i = 0, ie = pipelines.size(); i != ie; ++i) {
        const Pipeline &p(pipelines.at(i));
        if (p.topology == topology && p.format == vertexFormat && p.stride == vertexStride)
            return p.ps;
    }

    QRhiGraphicsPipeline *ps = rhi->newGraphicsPipeline();
    ps->setTopology(topology);
    QRhiGraphicsPipeline::TargetBlend blend; // premul alpha
    blend.enable = true;
    if (blendOneOne) {
        // only for visualizing overdraw, other modes use premul alpha
        blend.srcColor = QRhiGraphicsPipeline::One;
        blend.dstColor = QRhiGraphicsPipeline::One;
        blend.srcAlpha = QRhiGraphicsPipeline::One;
        blend.dstAlpha = QRhiGraphicsPipeline::One;
    }
    ps->setTargetBlends({ blend });
    ps->setShaderStages({ { QRhiShaderStage::Vertex, visualizer->m_vs },
                          { QRhiShaderStage::Fragment, visualizer->m_fs } });
    QRhiVertexInputLayout inputLayout;
    inputLayout.setBindings({ { vertexStride } });
    inputLayout.setAttributes({ { 0, 0, vertexFormat, 0 } });
    ps->setVertexInputLayout(inputLayout);
    ps->setShaderResourceBindings(srb);
    ps->setRenderPassDescriptor(rpDesc);
    if (!ps->create())
        return nullptr;

    Pipeline p;
    p.topology = topology;
    p.format = vertexFormat;
    p.stride = vertexStride;
    p.ps = ps;
    pipelines.append(p);

    return ps;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 878, as _ZN16QSGBatchRenderer13RhiVisualizer11OverdrawVis6renderEP17QRhiCommandBuffer
namespace QSGBatchRenderer {
inline void RhiVisualizer::OverdrawVis::render(QRhiCommandBuffer *cb)
{
    cb->setGraphicsPipeline(box.ps);
    cb->setShaderResources();
    QRhiCommandBuffer::VertexInput vb(box.vbuf, 0);
    cb->setVertexInput(0, 1, &vb);
    cb->draw(24);

    visualizer->recordDrawCalls(drawCalls, cb, srb, true);
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 225, as _ZN16QSGBatchRenderer13RhiVisualizer4Fade6renderEP17QRhiCommandBuffer
namespace QSGBatchRenderer {
inline void RhiVisualizer::Fade::render(QRhiCommandBuffer *cb)
{
    cb->setGraphicsPipeline(ps);
    cb->setViewport(visualizer->m_renderer->m_pstate.viewport);
    cb->setShaderResources();
    QRhiCommandBuffer::VertexInput vb(vbuf, 0);
    cb->setVertexInput(0, 1, &vb);
    cb->draw(4);
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 670, as _ZN16QSGBatchRenderer13RhiVisualizer7ClipVis6renderEP17QRhiCommandBuffer
namespace QSGBatchRenderer {
inline void RhiVisualizer::ClipVis::render(QRhiCommandBuffer *cb)
{
    visualizer->recordDrawCalls(drawCalls, cb, srb);
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 570, as _ZN16QSGBatchRenderer13RhiVisualizer8BatchVis6renderEP17QRhiCommandBuffer
namespace QSGBatchRenderer {
inline void RhiVisualizer::BatchVis::render(QRhiCommandBuffer *cb)
{
    visualizer->recordDrawCalls(drawCalls, cb, srb);
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 439, as _ZN16QSGBatchRenderer13RhiVisualizer9ChangeVis6renderEP17QRhiCommandBuffer
namespace QSGBatchRenderer {
inline void RhiVisualizer::ChangeVis::render(QRhiCommandBuffer *cb)
{
    visualizer->recordDrawCalls(drawCalls, cb, srb);
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 851, as _ZN16QSGBatchRenderer13RhiVisualizer11OverdrawVis16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::OverdrawVis::releaseResources()
{
    delete srb;
    srb = nullptr;

    delete ubuf;
    ubuf = nullptr;

    delete ibuf;
    ibuf = nullptr;

    delete vbuf;
    vbuf = nullptr;

    delete box.ps;
    box.ps = nullptr;

    delete box.srb;
    box.srb = nullptr;

    delete box.ubuf;
    box.ubuf = nullptr;

    delete box.vbuf;
    box.vbuf = nullptr;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 318, as _ZN16QSGBatchRenderer13RhiVisualizer13PipelineCache16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::PipelineCache::releaseResources()
{
    for (int i = 0, ie = pipelines.size(); i != ie; ++i)
        delete pipelines.at(i).ps;

    pipelines.clear();
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 210, as _ZN16QSGBatchRenderer13RhiVisualizer4Fade16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::Fade::releaseResources()
{
    delete ps;
    ps = nullptr;

    delete srb;
    srb = nullptr;

    delete ubuf;
    ubuf = nullptr;

    delete vbuf;
    vbuf = nullptr;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 655, as _ZN16QSGBatchRenderer13RhiVisualizer7ClipVis16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::ClipVis::releaseResources()
{
    delete srb;
    srb = nullptr;

    delete ubuf;
    ubuf = nullptr;

    delete ibuf;
    ibuf = nullptr;

    delete vbuf;
    vbuf = nullptr;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 561, as _ZN16QSGBatchRenderer13RhiVisualizer8BatchVis16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::BatchVis::releaseResources()
{
    delete srb;
    srb = nullptr;

    delete ubuf;
    ubuf = nullptr;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 424, as _ZN16QSGBatchRenderer13RhiVisualizer9ChangeVis16releaseResourcesEv
namespace QSGBatchRenderer {
inline void RhiVisualizer::ChangeVis::releaseResources()
{
    delete srb;
    srb = nullptr;

    delete ubuf;
    ubuf = nullptr;

    delete ibuf;
    ibuf = nullptr;

    delete vbuf;
    vbuf = nullptr;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 33, as _ZN16QSGBatchRenderer13RhiVisualizerD1Ev
namespace QSGBatchRenderer {
inline RhiVisualizer::~RhiVisualizer()
{
    releaseResources();
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgrhivisualizer.cpp, line 125, as _ZN16QSGBatchRenderer13RhiVisualizer15recordDrawCallsERK5QListINS0_8DrawCallEEP17QRhiCommandBufferP26QRhiShaderResourceBindingsb
namespace QSGBatchRenderer {
inline void RhiVisualizer::recordDrawCalls(const QList<DrawCall> &drawCalls,
                                    QRhiCommandBuffer *cb,
                                    QRhiShaderResourceBindings *srb,
                                    bool blendOneOne)
{
    for (const DrawCall &dc : drawCalls) {
        QRhiGraphicsPipeline *ps = m_pipelines.pipeline(this, m_renderer->m_rhi, srb, m_renderer->renderTarget().rpDesc,
                                                        dc.vertex.topology, dc.vertex.format, dc.vertex.stride,
                                                        blendOneOne);
        if (!ps)
            continue;
        cb->setGraphicsPipeline(ps); // no-op if same as the last one
        QRhiCommandBuffer::DynamicOffset dynofs(0, dc.buf.ubufOffset);
        cb->setShaderResources(srb, 1, &dynofs);
        QRhiCommandBuffer::VertexInput vb(dc.buf.vbuf, dc.buf.vbufOffset);
        if (dc.index.count) {
            cb->setVertexInput(0, 1, &vb, dc.buf.ibuf, dc.buf.ibufOffset, dc.index.format);
            cb->drawIndexed(dc.index.count);
        } else {
            cb->setVertexInput(0, 1, &vb);
            cb->draw(dc.vertex.count);
        }
    }
}
}  // namespace QSGBatchRenderer
//  -----------------------------------------------------------------------

//  A QSGBatchRenderer::RhiVisualizer that Python can take functions over in. Every QSGBatchRenderer::RhiVisualizer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall0)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall1)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall2)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RhiVisualizerCall3)(const void *, QSGBatchRenderer::Node *, uint, int *);
class CuteQSGBatchRenderer_RhiVisualizer : public QSGBatchRenderer::RhiVisualizer {
public:
  using QSGBatchRenderer::RhiVisualizer::RhiVisualizer;
  CuteQSGBatchRenderer_RhiVisualizer(const QSGBatchRenderer::RhiVisualizer & other) : QSGBatchRenderer::RhiVisualizer(other) {}
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer16prepareVisualizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer9visualizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer16releaseResourcesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGBatchRenderer10Visualizer23visualizeChangesPrepareEPNS_4NodeEj")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QSGBatchRenderer::RhiVisualizer::prepareVisualize()
  void prepareVisualize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall0 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::RhiVisualizer::prepareVisualize();
  }

  //  void QSGBatchRenderer::RhiVisualizer::visualize()
  void visualize() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall1 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::RhiVisualizer::visualize();
  }

  //  void QSGBatchRenderer::RhiVisualizer::releaseResources()
  void releaseResources() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall2 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::RhiVisualizer::releaseResources();
  }

  //  void QSGBatchRenderer::Visualizer::visualizeChangesPrepare(Node *n,
  //      uint parentChanges)
  void visualizeChangesPrepare(
      QSGBatchRenderer::Node *n,
      uint parentChanges) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGBatchRenderer_RhiVisualizerCall3 call = reinterpret_cast<CuteQSGBatchRenderer_RhiVisualizerCall3>(taken[3]);
      call(this, n, parentChanges, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Visualizer::visualizeChangesPrepare(n, parentChanges);
  }
};

//  QSGBatchRenderer::RhiVisualizer::~RhiVisualizer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13RhiVisualizerD1Ev(
    QSGBatchRenderer::RhiVisualizer *self) {
  delete self;
}

//  void QSGBatchRenderer::RhiVisualizer::prepareVisualize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13RhiVisualizer16prepareVisualizeEv(
    QSGBatchRenderer::RhiVisualizer *self) {
  self->prepareVisualize();
}

//  void QSGBatchRenderer::RhiVisualizer::visualize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13RhiVisualizer9visualizeEv(
    QSGBatchRenderer::RhiVisualizer *self) {
  self->visualize();
}

//  void QSGBatchRenderer::RhiVisualizer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13RhiVisualizer16releaseResourcesEv(
    QSGBatchRenderer::RhiVisualizer *self) {
  self->releaseResources();
}

//  void QSGBatchRenderer::RhiVisualizer::recordDrawCalls(const
//      QList<DrawCall> &drawCalls, QRhiCommandBuffer *cb,
//      QRhiShaderResourceBindings *srb, bool blendOneOne)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer13RhiVisualizer15recordDrawCallsERK5QListINS0_8DrawCallEEP17QRhiCommandBufferP26QRhiShaderResourceBindingsb(
    QSGBatchRenderer::RhiVisualizer *self,
    const QList<QSGBatchRenderer::RhiVisualizer::DrawCall> *drawCalls,
    QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb,
    bool blendOneOne) {
  self->recordDrawCalls(*drawCalls, cb, srb, blendOneOne);
}

//  a Python function taken by a CuteQSGBatchRenderer_RhiVisualizer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBatchRenderer_RhiVisualizer(
    QSGBatchRenderer::RhiVisualizer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBatchRenderer_RhiVisualizer *>(self)->take(key, call);
}

//  void QSGBatchRenderer::RhiVisualizer::visualize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer13RhiVisualizer9visualizeEv(
    QSGBatchRenderer::RhiVisualizer *self) {
  self->QSGBatchRenderer::RhiVisualizer::visualize();
}

//  void QSGBatchRenderer::RhiVisualizer::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer13RhiVisualizer16releaseResourcesEv(
    QSGBatchRenderer::RhiVisualizer *self) {
  self->QSGBatchRenderer::RhiVisualizer::releaseResources();
}
