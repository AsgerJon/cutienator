//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSGBatchRenderer::Renderer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGBatchRenderer_Renderer : QSGBatchRenderer::Renderer {
  using QSGBatchRenderer::Renderer::nodeChanged;
  using QSGBatchRenderer::Renderer::render;
  using QSGBatchRenderer::Renderer::prepareInline;
  using QSGBatchRenderer::Renderer::renderInline;
  using QSGBatchRenderer::Renderer::releaseCachedResources;
};

//  A QSGBatchRenderer::Renderer that Python can take functions over in. Every QSGBatchRenderer::Renderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGBatchRenderer_RendererCall0)(const void *, QSGNode *, int, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall1)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall2)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall3)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall4)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall5)(const void *, const QByteArray *, int *);
typedef bool (*CuteQSGBatchRenderer_RendererCall6)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall7)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall8)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall9)(const void *, int *);
typedef void (*CuteQSGBatchRenderer_RendererCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGBatchRenderer_RendererCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGBatchRenderer_RendererCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_RendererCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_RendererCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_RendererCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_RendererCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGBatchRenderer_RendererCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGBatchRenderer_Renderer : public QSGBatchRenderer::Renderer {
public:
  using QSGBatchRenderer::Renderer::Renderer;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer6renderEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer13prepareInlineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer12renderInlineEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer22releaseCachedResourcesEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer20setVisualizationModeERK10QByteArray")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11renderSceneEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer18prepareSceneInlineEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer17renderSceneInlineEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer10preprocessEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGBatchRenderer::Renderer::nodeChanged(QSGNode *node,
  //      QSGNode::DirtyState state)
  void nodeChanged(QSGNode *node, QSGNode::DirtyState state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall0 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall0>(taken[0]);
      call(this, node, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Renderer::nodeChanged(node, state);
  }

  //  void QSGBatchRenderer::Renderer::render()
  void render() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall1 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Renderer::render();
  }

  //  void QSGBatchRenderer::Renderer::prepareInline()
  void prepareInline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall2 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Renderer::prepareInline();
  }

  //  void QSGBatchRenderer::Renderer::renderInline()
  void renderInline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall3 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Renderer::renderInline();
  }

  //  void QSGBatchRenderer::Renderer::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall4 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Renderer::releaseCachedResources();
  }

  //  void QSGBatchRenderer::Renderer::setVisualizationMode(const
  //      QByteArray &mode)
  void setVisualizationMode(const QByteArray &mode) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall5 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall5>(taken[5]);
      call(this, &mode, &handled);
      if (handled) return;
    }
    QSGBatchRenderer::Renderer::setVisualizationMode(mode);
  }

  //  bool QSGBatchRenderer::Renderer::hasVisualizationModeWithContinuousUp
  //      date() const
  bool hasVisualizationModeWithContinuousUpdate() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall6 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGBatchRenderer::Renderer::hasVisualizationModeWithContinuousUpdate();
  }

  //  void QSGRenderer::renderScene()
  void renderScene() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall7 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderScene();
  }

  //  void QSGRenderer::prepareSceneInline()
  void prepareSceneInline() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall8 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareSceneInline();
  }

  //  void QSGRenderer::renderSceneInline()
  void renderSceneInline() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall9 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderSceneInline();
  }

  //  void QSGRenderer::preprocess()
  void preprocess() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall10 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::preprocess();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall11 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall12 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall13 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall14 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall15 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall16 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGBatchRenderer_RendererCall17 call = reinterpret_cast<CuteQSGBatchRenderer_RendererCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGBatchRenderer::Renderer::Renderer(QSGDefaultRenderContext *ctx,
//      QSGRendererInterface::RenderMode renderMode)
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Renderer *ritual_ZN16QSGBatchRenderer8RendererC1EP23QSGDefaultRenderContextN20QSGRendererInterface10RenderModeE(
    QSGDefaultRenderContext *ctx,
    QSGRendererInterface::RenderMode renderMode) {
  return new CuteQSGBatchRenderer_Renderer(ctx, renderMode);
}

//  QSGBatchRenderer::Renderer::~Renderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8RendererD1Ev(
    QSGBatchRenderer::Renderer *self) {
  delete self;
}

//  void QSGBatchRenderer::Renderer::nodeChanged(QSGNode *node,
//      QSGNode::DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer11nodeChangedEP7QSGNode6QFlagsINS1_13DirtyStateBitEE(
    QSGBatchRenderer::Renderer *self,
    QSGNode *node,
    int state) {
  self->nodeChanged(node, QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  void QSGBatchRenderer::Renderer::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer6renderEv(
    QSGBatchRenderer::Renderer *self) {
  self->render();
}

//  void QSGBatchRenderer::Renderer::prepareInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer13prepareInlineEv(
    QSGBatchRenderer::Renderer *self) {
  self->prepareInline();
}

//  void QSGBatchRenderer::Renderer::renderInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer12renderInlineEv(
    QSGBatchRenderer::Renderer *self) {
  self->renderInline();
}

//  void QSGBatchRenderer::Renderer::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer22releaseCachedResourcesEv(
    QSGBatchRenderer::Renderer *self) {
  self->releaseCachedResources();
}

//  void QSGBatchRenderer::Renderer::prepareRenderPass(RenderPassContext
//      *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer17prepareRenderPassEPNS0_17RenderPassContextE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Renderer::RenderPassContext *ctx) {
  self->prepareRenderPass(ctx);
}

//  void QSGBatchRenderer::Renderer::beginRenderPass(RenderPassContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer15beginRenderPassEPNS0_17RenderPassContextE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Renderer::RenderPassContext *ctx) {
  self->beginRenderPass(ctx);
}

//  void QSGBatchRenderer::Renderer::recordRenderPass(RenderPassContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer16recordRenderPassEPNS0_17RenderPassContextE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Renderer::RenderPassContext *ctx) {
  self->recordRenderPass(ctx);
}

//  void QSGBatchRenderer::Renderer::endRenderPass(RenderPassContext *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer13endRenderPassEPNS0_17RenderPassContextE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Renderer::RenderPassContext *ctx) {
  self->endRenderPass(ctx);
}

//  void QSGBatchRenderer::Renderer::destroyGraphicsResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer24destroyGraphicsResourcesEv(
    QSGBatchRenderer::Renderer *self) {
  self->destroyGraphicsResources();
}

//  void QSGBatchRenderer::Renderer::map(Buffer *buffer, quint32 byteSize,
//      bool isIndexBuf)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer3mapEPNS_6BufferEjb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Buffer *buffer,
    quint32 byteSize,
    bool isIndexBuf) {
  self->map(buffer, byteSize, isIndexBuf);
}

//  void QSGBatchRenderer::Renderer::unmap(Buffer *buffer, bool isIndexBuf)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer5unmapEPNS_6BufferEb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Buffer *buffer,
    bool isIndexBuf) {
  self->unmap(buffer, isIndexBuf);
}

//  void QSGBatchRenderer::Renderer::buildRenderListsFromScratch()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer27buildRenderListsFromScratchEv(
    QSGBatchRenderer::Renderer *self) {
  self->buildRenderListsFromScratch();
}

//  void QSGBatchRenderer::Renderer::buildRenderListsForTaggedRoots()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer30buildRenderListsForTaggedRootsEv(
    QSGBatchRenderer::Renderer *self) {
  self->buildRenderListsForTaggedRoots();
}

//  void QSGBatchRenderer::Renderer::tagSubRoots(Node *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer11tagSubRootsEPNS_4NodeE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node) {
  self->tagSubRoots(node);
}

//  void QSGBatchRenderer::Renderer::buildRenderLists(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer16buildRenderListsEP7QSGNode(
    QSGBatchRenderer::Renderer *self,
    QSGNode *node) {
  self->buildRenderLists(node);
}

//  void QSGBatchRenderer::Renderer::deleteRemovedElements()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer21deleteRemovedElementsEv(
    QSGBatchRenderer::Renderer *self) {
  self->deleteRemovedElements();
}

//  void QSGBatchRenderer::Renderer::cleanupBatches(QDataBuffer<Batch *>
//      *batches)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer14cleanupBatchesEP11QDataBufferIPNS_5BatchEE(
    QSGBatchRenderer::Renderer *self,
    QDataBuffer<QSGBatchRenderer::Batch *> *batches) {
  self->cleanupBatches(batches);
}

//  void QSGBatchRenderer::Renderer::prepareOpaqueBatches()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer20prepareOpaqueBatchesEv(
    QSGBatchRenderer::Renderer *self) {
  self->prepareOpaqueBatches();
}

//  bool QSGBatchRenderer::Renderer::checkOverlap(int first, int last, const
//      Rect &bounds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer8Renderer12checkOverlapEiiRKNS_4RectE(
    QSGBatchRenderer::Renderer *self,
    int first,
    int last,
    const QSGBatchRenderer::Rect *bounds) {
  return self->checkOverlap(first, last, *bounds);
}

//  void QSGBatchRenderer::Renderer::prepareAlphaBatches()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer19prepareAlphaBatchesEv(
    QSGBatchRenderer::Renderer *self) {
  self->prepareAlphaBatches();
}

//  void QSGBatchRenderer::Renderer::invalidateBatchAndOverlappingRenderOrder
//      s(Batch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer41invalidateBatchAndOverlappingRenderOrdersEPNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Batch *batch) {
  self->invalidateBatchAndOverlappingRenderOrders(batch);
}

//  void QSGBatchRenderer::Renderer::uploadBatch(Batch *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer11uploadBatchEPNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Batch *b) {
  self->uploadBatch(b);
}

//  void QSGBatchRenderer::Renderer::uploadMergedElement(Element *e, int
//      vaOffset, char **vertexData, char **zData, char **indexData, void
//      *iBasePtr, int *indexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer19uploadMergedElementEPNS_7ElementEiPPcS4_S4_PvPi(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Element *e,
    int vaOffset,
    char **vertexData,
    char **zData,
    char **indexData,
    void *iBasePtr,
    int *indexCount) {
  self->uploadMergedElement(
      e,
      vaOffset,
      vertexData,
      zData,
      indexData,
      iBasePtr,
      indexCount);
}

//  bool QSGBatchRenderer::Renderer::ensurePipelineState(Element *e, const
//      ShaderManager::Shader *sms, bool depthPostPass)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer8Renderer19ensurePipelineStateEPNS_7ElementEPKNS_19ShaderManagerShaderEb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Element *e,
    const QSGBatchRenderer::ShaderManager::Shader *sms,
    bool depthPostPass) {
  return self->ensurePipelineState(e, sms, depthPostPass);
}

//  QRhiTexture *QSGBatchRenderer::Renderer::dummyTexture()
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN16QSGBatchRenderer8Renderer12dummyTextureEv(
    QSGBatchRenderer::Renderer *self) {
  return self->dummyTexture();
}

//  void QSGBatchRenderer::Renderer::updateMaterialDynamicData(ShaderManager:
//      :Shader *sms, QSGMaterialShader::RenderState &renderState,
//      QSGMaterial *material, const Batch *batch, Element *e, int
//      ubufOffset, char *directUpdatePtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer25updateMaterialDynamicDataEPNS_19ShaderManagerShaderERN17QSGMaterialShader11RenderStateEP11QSGMaterialPKNS_5BatchEPNS_7ElementEiPc(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::ShaderManager::Shader *sms,
    QSGMaterialShader::RenderState *renderState,
    QSGMaterial *material,
    const QSGBatchRenderer::Batch *batch,
    QSGBatchRenderer::Element *e,
    int ubufOffset,
    char *directUpdatePtr) {
  self->updateMaterialDynamicData(
      sms,
      *renderState,
      material,
      batch,
      e,
      ubufOffset,
      directUpdatePtr);
}

//  void QSGBatchRenderer::Renderer::updateMaterialStaticData(ShaderManager::
//      Shader *sms, QSGMaterialShader::RenderState &renderState, QSGMaterial
//      *material, Batch *batch, bool *gstateChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer24updateMaterialStaticDataEPNS_19ShaderManagerShaderERN17QSGMaterialShader11RenderStateEP11QSGMaterialPNS_5BatchEPb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::ShaderManager::Shader *sms,
    QSGMaterialShader::RenderState *renderState,
    QSGMaterial *material,
    QSGBatchRenderer::Batch *batch,
    bool *gstateChanged) {
  self->updateMaterialStaticData(
      sms,
      *renderState,
      material,
      batch,
      gstateChanged);
}

//  void QSGBatchRenderer::Renderer::checkLineWidth(QSGGeometry *g)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer14checkLineWidthEP11QSGGeometry(
    QSGBatchRenderer::Renderer *self,
    QSGGeometry *g) {
  self->checkLineWidth(g);
}

//  bool QSGBatchRenderer::Renderer::prepareRenderMergedBatch(Batch *batch,
//      PreparedRenderBatch *renderBatch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer8Renderer24prepareRenderMergedBatchEPNS_5BatchEPNS0_19PreparedRenderBatchE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Batch *batch,
    QSGBatchRenderer::Renderer::PreparedRenderBatch *renderBatch) {
  return self->prepareRenderMergedBatch(batch, renderBatch);
}

//  void QSGBatchRenderer::Renderer::renderMergedBatch(PreparedRenderBatch
//      *renderBatch, bool depthPostPass)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer17renderMergedBatchEPNS0_19PreparedRenderBatchEb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Renderer::PreparedRenderBatch *renderBatch,
    bool depthPostPass) {
  self->renderMergedBatch(renderBatch, depthPostPass);
}

//  bool QSGBatchRenderer::Renderer::prepareRenderUnmergedBatch(Batch *batch,
//      PreparedRenderBatch *renderBatch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer8Renderer26prepareRenderUnmergedBatchEPNS_5BatchEPNS0_19PreparedRenderBatchE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Batch *batch,
    QSGBatchRenderer::Renderer::PreparedRenderBatch *renderBatch) {
  return self->prepareRenderUnmergedBatch(batch, renderBatch);
}

//  void QSGBatchRenderer::Renderer::renderUnmergedBatch(PreparedRenderBatch
//      *renderBatch, bool depthPostPass)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer19renderUnmergedBatchEPNS0_19PreparedRenderBatchEb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Renderer::PreparedRenderBatch *renderBatch,
    bool depthPostPass) {
  self->renderUnmergedBatch(renderBatch, depthPostPass);
}

//  void QSGBatchRenderer::Renderer::setViewportAndScissors(QRhiCommandBuffer
//      *cb, const Batch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer22setViewportAndScissorsEP17QRhiCommandBufferPKNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    QRhiCommandBuffer *cb,
    const QSGBatchRenderer::Batch *batch) {
  self->setViewportAndScissors(cb, batch);
}

//  void QSGBatchRenderer::Renderer::setGraphicsPipeline(QRhiCommandBuffer
//      *cb, const Batch *batch, Element *e, bool depthPostPass)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer19setGraphicsPipelineEP17QRhiCommandBufferPKNS_5BatchEPNS_7ElementEb(
    QSGBatchRenderer::Renderer *self,
    QRhiCommandBuffer *cb,
    const QSGBatchRenderer::Batch *batch,
    QSGBatchRenderer::Element *e,
    bool depthPostPass) {
  self->setGraphicsPipeline(cb, batch, e, depthPostPass);
}

//  void QSGBatchRenderer::Renderer::applyClipStateToGraphicsState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer29applyClipStateToGraphicsStateEv(
    QSGBatchRenderer::Renderer *self) {
  self->applyClipStateToGraphicsState();
}

//  QRhiGraphicsPipeline
//      *QSGBatchRenderer::Renderer::buildStencilPipeline(const Batch *batch,
//      bool firstStencilClipInBatch)
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN16QSGBatchRenderer8Renderer20buildStencilPipelineEPKNS_5BatchEb(
    QSGBatchRenderer::Renderer *self,
    const QSGBatchRenderer::Batch *batch,
    bool firstStencilClipInBatch) {
  return self->buildStencilPipeline(batch, firstStencilClipInBatch);
}

//  void QSGBatchRenderer::Renderer::updateClipState(const QSGClipNode
//      *clipList, Batch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer15updateClipStateEPK11QSGClipNodePNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    const QSGClipNode *clipList,
    QSGBatchRenderer::Batch *batch) {
  self->updateClipState(clipList, batch);
}

//  void QSGBatchRenderer::Renderer::enqueueStencilDraw(const Batch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer18enqueueStencilDrawEPKNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    const QSGBatchRenderer::Batch *batch) {
  self->enqueueStencilDraw(batch);
}

//  bool QSGBatchRenderer::Renderer::prepareRhiRenderNode(Batch *batch,
//      PreparedRenderBatch *renderBatch)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer8Renderer20prepareRhiRenderNodeEPNS_5BatchEPNS0_19PreparedRenderBatchE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Batch *batch,
    QSGBatchRenderer::Renderer::PreparedRenderBatch *renderBatch) {
  return self->prepareRhiRenderNode(batch, renderBatch);
}

//  void QSGBatchRenderer::Renderer::renderRhiRenderNode(const Batch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer19renderRhiRenderNodeEPKNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    const QSGBatchRenderer::Batch *batch) {
  self->renderRhiRenderNode(batch);
}

//  void QSGBatchRenderer::Renderer::setActiveRhiShader(QSGMaterialShader
//      *program, ShaderManager::Shader *shader)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer18setActiveRhiShaderEP17QSGMaterialShaderPNS_19ShaderManagerShaderE(
    QSGBatchRenderer::Renderer *self,
    QSGMaterialShader *program,
    QSGBatchRenderer::ShaderManager::Shader *shader) {
  self->setActiveRhiShader(program, shader);
}

//  bool QSGBatchRenderer::Renderer::changeBatchRoot(Node *node, Node
//      *newRoot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer8Renderer15changeBatchRootEPNS_4NodeES2_(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node,
    QSGBatchRenderer::Node *newRoot) {
  return self->changeBatchRoot(node, newRoot);
}

//  void QSGBatchRenderer::Renderer::registerBatchRoot(Node *childRoot, Node
//      *parentRoot)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer17registerBatchRootEPNS_4NodeES2_(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *childRoot,
    QSGBatchRenderer::Node *parentRoot) {
  self->registerBatchRoot(childRoot, parentRoot);
}

//  void QSGBatchRenderer::Renderer::removeBatchRootFromParent(Node
//      *childRoot)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer25removeBatchRootFromParentEPNS_4NodeE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *childRoot) {
  self->removeBatchRootFromParent(childRoot);
}

//  void QSGBatchRenderer::Renderer::nodeChangedBatchRoot(Node *node, Node
//      *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer20nodeChangedBatchRootEPNS_4NodeES2_(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node,
    QSGBatchRenderer::Node *root) {
  self->nodeChangedBatchRoot(node, root);
}

//  void QSGBatchRenderer::Renderer::turnNodeIntoBatchRoot(Node *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer21turnNodeIntoBatchRootEPNS_4NodeE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node) {
  self->turnNodeIntoBatchRoot(node);
}

//  void QSGBatchRenderer::Renderer::nodeWasTransformed(Node *node, int
//      *vertexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer18nodeWasTransformedEPNS_4NodeEPi(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node,
    int *vertexCount) {
  self->nodeWasTransformed(node, vertexCount);
}

//  void QSGBatchRenderer::Renderer::nodeWasRemoved(Node *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer14nodeWasRemovedEPNS_4NodeE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node) {
  self->nodeWasRemoved(node);
}

//  void QSGBatchRenderer::Renderer::nodeWasAdded(QSGNode *node, Node
//      *shadowParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer12nodeWasAddedEP7QSGNodePNS_4NodeE(
    QSGBatchRenderer::Renderer *self,
    QSGNode *node,
    QSGBatchRenderer::Node *shadowParent) {
  self->nodeWasAdded(node, shadowParent);
}

//  BatchRootInfo *QSGBatchRenderer::Renderer::batchRootInfo(Node *node)
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::BatchRootInfo *ritual_ZN16QSGBatchRenderer8Renderer13batchRootInfoEPNS_4NodeE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Node *node) {
  return self->batchRootInfo(node);
}

//  Batch *QSGBatchRenderer::Renderer::newBatch()
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Batch *ritual_ZN16QSGBatchRenderer8Renderer8newBatchEv(
    QSGBatchRenderer::Renderer *self) {
  return self->newBatch();
}

//  void QSGBatchRenderer::Renderer::invalidateAndRecycleBatch(Batch *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer25invalidateAndRecycleBatchEPNS_5BatchE(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Batch *b) {
  self->invalidateAndRecycleBatch(b);
}

//  void QSGBatchRenderer::Renderer::releaseElement(Element *e, bool
//      inDestructor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer14releaseElementEPNS_7ElementEb(
    QSGBatchRenderer::Renderer *self,
    QSGBatchRenderer::Element *e,
    bool inDestructor) {
  self->releaseElement(e, inDestructor);
}

//  void QSGBatchRenderer::Renderer::setVisualizationMode(const QByteArray
//      &mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer20setVisualizationModeERK10QByteArray(
    QSGBatchRenderer::Renderer *self,
    const QByteArray *mode) {
  self->setVisualizationMode(*mode);
}

//  bool
//      QSGBatchRenderer::Renderer::hasVisualizationModeWithContinuousUpdate(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer8Renderer40hasVisualizationModeWithContinuousUpdateEv(
    const QSGBatchRenderer::Renderer *self) {
  return self->hasVisualizationModeWithContinuousUpdate();
}

//  int QSGBatchRenderer::Renderer::mergedIndexElemSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QSGBatchRenderer8Renderer19mergedIndexElemSizeEv(
    const QSGBatchRenderer::Renderer *self) {
  return self->mergedIndexElemSize();
}

//  bool QSGBatchRenderer::Renderer::useDepthBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer8Renderer14useDepthBufferEv(
    const QSGBatchRenderer::Renderer *self) {
  return self->useDepthBuffer();
}

//  void QSGBatchRenderer::Renderer::setStateForDepthPostPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer8Renderer24setStateForDepthPostPassEv(
    QSGBatchRenderer::Renderer *self) {
  self->setStateForDepthPostPass();
}

//  a Python function taken by a CuteQSGBatchRenderer_Renderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBatchRenderer_Renderer(
    QSGBatchRenderer::Renderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBatchRenderer_Renderer *>(self)->take(key, call);
}

//  void QSGBatchRenderer::Renderer::nodeChanged(QSGNode *node,
//      QSGNode::DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer8Renderer11nodeChangedEP7QSGNode6QFlagsINS1_13DirtyStateBitEE(
    QSGBatchRenderer::Renderer *self,
    QSGNode *node,
    int state) {
  static_cast<OwnQSGBatchRenderer_Renderer *>(self)->OwnQSGBatchRenderer_Renderer::nodeChanged(
      node,
      QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  void QSGBatchRenderer::Renderer::render()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer8Renderer6renderEv(
    QSGBatchRenderer::Renderer *self) {
  static_cast<OwnQSGBatchRenderer_Renderer *>(self)->OwnQSGBatchRenderer_Renderer::render();
}

//  void QSGBatchRenderer::Renderer::prepareInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer8Renderer13prepareInlineEv(
    QSGBatchRenderer::Renderer *self) {
  static_cast<OwnQSGBatchRenderer_Renderer *>(self)->OwnQSGBatchRenderer_Renderer::prepareInline();
}

//  void QSGBatchRenderer::Renderer::renderInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer8Renderer12renderInlineEv(
    QSGBatchRenderer::Renderer *self) {
  static_cast<OwnQSGBatchRenderer_Renderer *>(self)->OwnQSGBatchRenderer_Renderer::renderInline();
}

//  void QSGBatchRenderer::Renderer::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer8Renderer22releaseCachedResourcesEv(
    QSGBatchRenderer::Renderer *self) {
  static_cast<OwnQSGBatchRenderer_Renderer *>(self)->OwnQSGBatchRenderer_Renderer::releaseCachedResources();
}

//  void QSGBatchRenderer::Renderer::setVisualizationMode(const QByteArray
//      &mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QSGBatchRenderer8Renderer20setVisualizationModeERK10QByteArray(
    QSGBatchRenderer::Renderer *self,
    const QByteArray *mode) {
  self->QSGBatchRenderer::Renderer::setVisualizationMode(*mode);
}

//  bool
//      QSGBatchRenderer::Renderer::hasVisualizationModeWithContinuousUpdate(
//      ) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QSGBatchRenderer8Renderer40hasVisualizationModeWithContinuousUpdateEv(
    const QSGBatchRenderer::Renderer *self) {
  return self->QSGBatchRenderer::Renderer::hasVisualizationModeWithContinuousUpdate();
}
