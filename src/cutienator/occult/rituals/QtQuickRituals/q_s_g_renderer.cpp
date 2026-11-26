//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtQuick/qsgmaterialshader.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSGRenderer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGRenderer : QSGRenderer {
  using QSGRenderer::prepareInline;
  using QSGRenderer::renderInline;
  using QSGRenderer::preprocess;
};

//  A QSGRenderer that Python can take functions over in. Every QSGRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGRendererCall0)(const void *, int *);
typedef void (*CuteQSGRendererCall1)(const void *, int *);
typedef void (*CuteQSGRendererCall2)(const void *, int *);
typedef void (*CuteQSGRendererCall3)(const void *, QSGNode *, int, int *);
typedef void (*CuteQSGRendererCall4)(const void *, const QByteArray *, int *);
typedef bool (*CuteQSGRendererCall5)(const void *, int *);
typedef void (*CuteQSGRendererCall6)(const void *, int *);
typedef void (*CuteQSGRendererCall7)(const void *, int *);
typedef void (*CuteQSGRendererCall8)(const void *, int *);
typedef void (*CuteQSGRendererCall9)(const void *, int *);
typedef void (*CuteQSGRendererCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRendererCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRendererCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRendererCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRendererCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRendererCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRendererCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRendererCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRenderer : public QSGRenderer {
public:
  using QSGRenderer::QSGRenderer;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11renderSceneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer18prepareSceneInlineEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer17renderSceneInlineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer20setVisualizationModeERK10QByteArray")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer22releaseCachedResourcesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer6renderEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer13prepareInlineEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer12renderInlineEv")) {
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

  //  void QSGRenderer::renderScene()
  void renderScene() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRendererCall0 call = reinterpret_cast<CuteQSGRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderScene();
  }

  //  void QSGRenderer::prepareSceneInline()
  void prepareSceneInline() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRendererCall1 call = reinterpret_cast<CuteQSGRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareSceneInline();
  }

  //  void QSGRenderer::renderSceneInline()
  void renderSceneInline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRendererCall2 call = reinterpret_cast<CuteQSGRendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderSceneInline();
  }

  //  void QSGRenderer::nodeChanged(QSGNode *node, QSGNode::DirtyState
  //      state)
  void nodeChanged(QSGNode *node, QSGNode::DirtyState state) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRendererCall3 call = reinterpret_cast<CuteQSGRendererCall3>(taken[3]);
      call(this, node, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
    QSGRenderer::nodeChanged(node, state);
  }

  //  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
  void setVisualizationMode(const QByteArray &a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRendererCall4 call = reinterpret_cast<CuteQSGRendererCall4>(taken[4]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSGRenderer::setVisualizationMode(a0);
  }

  //  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
  bool hasVisualizationModeWithContinuousUpdate() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRendererCall5 call = reinterpret_cast<CuteQSGRendererCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderer::hasVisualizationModeWithContinuousUpdate();
  }

  //  void QSGRenderer::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRendererCall6 call = reinterpret_cast<CuteQSGRendererCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::releaseCachedResources();
  }

  //  void QSGRenderer::render()
  void render() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRendererCall7 call = reinterpret_cast<CuteQSGRendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderer::prepareInline()
  void prepareInline() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRendererCall8 call = reinterpret_cast<CuteQSGRendererCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareInline();
  }

  //  void QSGRenderer::renderInline()
  void renderInline() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRendererCall9 call = reinterpret_cast<CuteQSGRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderInline();
  }

  //  void QSGRenderer::preprocess()
  void preprocess() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGRendererCall10 call = reinterpret_cast<CuteQSGRendererCall10>(taken[10]);
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
      CuteQSGRendererCall11 call = reinterpret_cast<CuteQSGRendererCall11>(taken[11]);
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
      CuteQSGRendererCall12 call = reinterpret_cast<CuteQSGRendererCall12>(taken[12]);
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
      CuteQSGRendererCall13 call = reinterpret_cast<CuteQSGRendererCall13>(taken[13]);
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
      CuteQSGRendererCall14 call = reinterpret_cast<CuteQSGRendererCall14>(taken[14]);
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
      CuteQSGRendererCall15 call = reinterpret_cast<CuteQSGRendererCall15>(taken[15]);
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
      CuteQSGRendererCall16 call = reinterpret_cast<CuteQSGRendererCall16>(taken[16]);
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
      CuteQSGRendererCall17 call = reinterpret_cast<CuteQSGRendererCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGRenderer::QSGRenderer(QSGRenderContext *context)
extern "C" Q_DECL_EXPORT
QSGRenderer *ritual_ZN11QSGRendererC1EP16QSGRenderContext(
    QSGRenderContext *context) {
  return new CuteQSGRenderer(context);
}

//  QSGRenderer::~QSGRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRendererD1Ev(QSGRenderer *self) {
  delete self;
}

//  QMatrix4x4 QSGRenderer::currentProjectionMatrix(int index) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK11QSGRenderer23currentProjectionMatrixEi(
    const QSGRenderer *self,
    int index) {
  return new QMatrix4x4(self->currentProjectionMatrix(index));
}

//  QMatrix4x4 QSGRenderer::currentModelViewMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK11QSGRenderer22currentModelViewMatrixEv(
    const QSGRenderer *self) {
  return new QMatrix4x4(self->currentModelViewMatrix());
}

//  QMatrix4x4 QSGRenderer::currentCombinedMatrix(int index) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK11QSGRenderer21currentCombinedMatrixEi(
    const QSGRenderer *self,
    int index) {
  return new QMatrix4x4(self->currentCombinedMatrix(index));
}

//  qreal QSGRenderer::currentOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QSGRenderer14currentOpacityEv(const QSGRenderer *self) {
  return self->currentOpacity();
}

//  qreal QSGRenderer::determinant() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QSGRenderer11determinantEv(const QSGRenderer *self) {
  return self->determinant();
}

//  void QSGRenderer::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer19setDevicePixelRatioEd(
    QSGRenderer *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  qreal QSGRenderer::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QSGRenderer16devicePixelRatioEv(const QSGRenderer *self) {
  return self->devicePixelRatio();
}

//  QSGRenderContext *QSGRenderer::context() const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZNK11QSGRenderer7contextEv(
    const QSGRenderer *self) {
  return self->context();
}

//  bool QSGRenderer::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSGRenderer10isMirroredEv(const QSGRenderer *self) {
  return self->isMirrored();
}

//  void QSGRenderer::renderScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer11renderSceneEv(QSGRenderer *self) {
  self->renderScene();
}

//  void QSGRenderer::prepareSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer18prepareSceneInlineEv(QSGRenderer *self) {
  self->prepareSceneInline();
}

//  void QSGRenderer::renderSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer17renderSceneInlineEv(QSGRenderer *self) {
  self->renderSceneInline();
}

//  void QSGRenderer::nodeChanged(QSGNode *node, QSGNode::DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE(
    QSGRenderer *self,
    QSGNode *node,
    int state) {
  self->nodeChanged(node, QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  QSGNodeUpdater *QSGRenderer::nodeUpdater() const
extern "C" Q_DECL_EXPORT
QSGNodeUpdater *ritual_ZNK11QSGRenderer11nodeUpdaterEv(
    const QSGRenderer *self) {
  return self->nodeUpdater();
}

//  void QSGRenderer::setNodeUpdater(QSGNodeUpdater *updater)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer14setNodeUpdaterEP14QSGNodeUpdater(
    QSGRenderer *self,
    QSGNodeUpdater *updater) {
  self->setNodeUpdater(updater);
}

//  QSGMaterialShader::RenderState
//      QSGRenderer::state(QSGMaterialShader::RenderState::DirtyStates dirty)
//      const
extern "C" Q_DECL_EXPORT
QSGMaterialShader::RenderState *ritual_ZNK11QSGRenderer5stateE6QFlagsIN17QSGMaterialShader11RenderState10DirtyStateEE(
    const QSGRenderer *self,
    int dirty) {
  return new QSGMaterialShader::RenderState(
      self->state(
          QFlags<QSGMaterialShader::RenderState::DirtyState>::fromInt(dirty)));
}

//  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer20setVisualizationModeERK10QByteArray(
    QSGRenderer *self,
    const QByteArray *a0) {
  self->setVisualizationMode(*a0);
}

//  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv(
    const QSGRenderer *self) {
  return self->hasVisualizationModeWithContinuousUpdate();
}

//  void QSGRenderer::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer22releaseCachedResourcesEv(QSGRenderer *self) {
  self->releaseCachedResources();
}

//  void QSGRenderer::clearChangedFlag()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer16clearChangedFlagEv(QSGRenderer *self) {
  self->clearChangedFlag();
}

//  QByteArray *QSGRenderer::currentUniformData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QSGRenderer18currentUniformDataEv(
    const QSGRenderer *self) {
  return self->currentUniformData();
}

//  QRhiResourceUpdateBatch *QSGRenderer::currentResourceUpdateBatch() const
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZNK11QSGRenderer26currentResourceUpdateBatchEv(
    const QSGRenderer *self) {
  return self->currentResourceUpdateBatch();
}

//  QRhi *QSGRenderer::currentRhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK11QSGRenderer10currentRhiEv(const QSGRenderer *self) {
  return self->currentRhi();
}

//  void QSGRenderer::setRenderTarget(const QSGRenderTarget &rt)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer15setRenderTargetERK15QSGRenderTarget(
    QSGRenderer *self,
    const QSGRenderTarget *rt) {
  self->setRenderTarget(*rt);
}

//  const QSGRenderTarget &QSGRenderer::renderTarget() const
extern "C" Q_DECL_EXPORT
QSGRenderTarget *ritual_ZNK11QSGRenderer12renderTargetEv(
    const QSGRenderer *self) {
  return new QSGRenderTarget(self->renderTarget());
}

//  void QSGRenderer::setRenderPassRecordingCallbacks(QSGRenderContext::Rende
//      rPassCallback start, QSGRenderContext::RenderPassCallback end, void
//      *userData)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer31setRenderPassRecordingCallbacksEPFvPvES2_S0_(
    QSGRenderer *self,
    void *start,
    void *end,
    void *userData) {
  self->setRenderPassRecordingCallbacks(
      reinterpret_cast<QSGRenderContext::RenderPassCallback>(start),
      reinterpret_cast<QSGRenderContext::RenderPassCallback>(end),
      userData);
}

//  void QSGRenderer::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer6renderEv(QSGRenderer *self) {
  self->render();
}

//  void QSGRenderer::prepareInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer13prepareInlineEv(QSGRenderer *self) {
  self->prepareInline();
}

//  void QSGRenderer::renderInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer12renderInlineEv(QSGRenderer *self) {
  self->renderInline();
}

//  void QSGRenderer::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer10preprocessEv(QSGRenderer *self) {
  self->preprocess();
}

//  void QSGRenderer::addNodesToPreprocess(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer20addNodesToPreprocessEP7QSGNode(
    QSGRenderer *self,
    QSGNode *node) {
  self->addNodesToPreprocess(node);
}

//  void QSGRenderer::removeNodesToPreprocess(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRenderer23removeNodesToPreprocessEP7QSGNode(
    QSGRenderer *self,
    QSGNode *node) {
  self->removeNodesToPreprocess(node);
}

//  a Python function taken by a CuteQSGRenderer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRenderer(
    QSGRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRenderer *>(self)->take(key, call);
}

//  void QSGRenderer::renderScene()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer11renderSceneEv(QSGRenderer *self) {
  self->QSGRenderer::renderScene();
}

//  void QSGRenderer::prepareSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer18prepareSceneInlineEv(QSGRenderer *self) {
  self->QSGRenderer::prepareSceneInline();
}

//  void QSGRenderer::renderSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer17renderSceneInlineEv(QSGRenderer *self) {
  self->QSGRenderer::renderSceneInline();
}

//  void QSGRenderer::nodeChanged(QSGNode *node, QSGNode::DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE(
    QSGRenderer *self,
    QSGNode *node,
    int state) {
  self->QSGRenderer::nodeChanged(
      node,
      QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer20setVisualizationModeERK10QByteArray(
    QSGRenderer *self,
    const QByteArray *a0) {
  self->QSGRenderer::setVisualizationMode(*a0);
}

//  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv(
    const QSGRenderer *self) {
  return self->QSGRenderer::hasVisualizationModeWithContinuousUpdate();
}

//  void QSGRenderer::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer22releaseCachedResourcesEv(
    QSGRenderer *self) {
  self->QSGRenderer::releaseCachedResources();
}

//  void QSGRenderer::prepareInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer13prepareInlineEv(QSGRenderer *self) {
  static_cast<OwnQSGRenderer *>(self)->OwnQSGRenderer::prepareInline();
}

//  void QSGRenderer::renderInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer12renderInlineEv(QSGRenderer *self) {
  static_cast<OwnQSGRenderer *>(self)->OwnQSGRenderer::renderInline();
}

//  void QSGRenderer::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSGRenderer10preprocessEv(QSGRenderer *self) {
  static_cast<OwnQSGRenderer *>(self)->OwnQSGRenderer::preprocess();
}
