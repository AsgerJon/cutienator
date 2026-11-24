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

//  Batch *QSGBatchRenderer::Renderer::newBatch()
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Batch *ritual_ZN16QSGBatchRenderer8Renderer8newBatchEv(
    QSGBatchRenderer::Renderer *self) {
  return self->newBatch();
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
