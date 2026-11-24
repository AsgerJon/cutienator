//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultcontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGDefaultContext that Python can take functions over in. Every QSGDefaultContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGDefaultContextCall0)(const void *, QSGRenderContext *, int *);
typedef void (*CuteQSGDefaultContextCall1)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGDefaultContextCall2)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall3)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall4)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGDefaultContextCall5)(const void *, QQuickPaintedItem *, int *);
typedef void * (*CuteQSGDefaultContextCall6)(const void *, QSGRenderContext *, int, int *);
typedef void * (*CuteQSGDefaultContextCall7)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGDefaultContextCall8)(const void *, QSGRenderContext *, int *);
typedef const QSurfaceFormat * (*CuteQSGDefaultContextCall9)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall10)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGDefaultContextCall11)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall12)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall13)(const void *, int *);
#if QT_CONFIG(quick_sprite)
typedef void * (*CuteQSGDefaultContextCall14)(const void *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef void * (*CuteQSGDefaultContextCall15)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall16)(const void *, QSGRenderContext *, int *);
typedef int (*CuteQSGDefaultContextCall17)(const void *, int, int *);
typedef int (*CuteQSGDefaultContextCall18)(const void *, int *);
typedef int (*CuteQSGDefaultContextCall19)(const void *, int *);
typedef int (*CuteQSGDefaultContextCall20)(const void *, int *);
typedef int (*CuteQSGDefaultContextCall21)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall22)(const void *, QObject *, int *);
typedef float (*CuteQSGDefaultContextCall23)(const void *, QAnimationDriver *, int *);
typedef bool (*CuteQSGDefaultContextCall24)(const void *, QAnimationDriver *, int *);
typedef const QSize * (*CuteQSGDefaultContextCall25)(const void *, int *);
typedef void * (*CuteQSGDefaultContextCall26)(const void *, QSGRenderContext *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGDefaultContextCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGDefaultContextCall28)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultContextCall29)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultContextCall30)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultContextCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultContextCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGDefaultContextCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGDefaultContext : public QSGDefaultContext {
public:
  using QSGDefaultContext::QSGDefaultContext;
  void *taken[34] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QSGContext24renderContextInitializedEP16QSGRenderContext")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContext")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createRenderContextEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext27createInternalRectangleNodeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext23createInternalImageNodeEP16QSGRenderContext")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext17createPainterNodeEP17QQuickPaintedItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext11createLayerEP16QSGRenderContext")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext20defaultSurfaceFormatEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createRectangleNodeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext15createImageNodeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createNinePatchNodeEv")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN10QSGContext16createSpriteNodeEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN10QSGContext34createGuiThreadShaderEffectManagerEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface11graphicsApiEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface10shaderTypeEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface21shaderCompilationTypeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface16shaderSourceTypeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext21createAnimationDriverEP7QObject")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationDriver")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext14minimumFBOSizeEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext14createTextNodeEP16QSGRenderContext")) {
      taken[26] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGDefaultContext::renderContextInitialized(QSGRenderContext
  //      *renderContext)
  void renderContextInitialized(QSGRenderContext *renderContext) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDefaultContextCall0 call = reinterpret_cast<CuteQSGDefaultContextCall0>(taken[0]);
      call(this, renderContext, &handled);
      if (handled) return;
    }
    QSGDefaultContext::renderContextInitialized(renderContext);
  }

  //  void QSGDefaultContext::renderContextInvalidated(QSGRenderContext
  //      *a0)
  void renderContextInvalidated(QSGRenderContext *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDefaultContextCall1 call = reinterpret_cast<CuteQSGDefaultContextCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGDefaultContext::renderContextInvalidated(a0);
  }

  //  QSGRenderContext *QSGDefaultContext::createRenderContext()
  QSGRenderContext *createRenderContext() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDefaultContextCall2 call = reinterpret_cast<CuteQSGDefaultContextCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return QSGDefaultContext::createRenderContext();
  }

  //  QSGInternalRectangleNode
  //      *QSGDefaultContext::createInternalRectangleNode()
  QSGInternalRectangleNode *createInternalRectangleNode() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDefaultContextCall3 call = reinterpret_cast<CuteQSGDefaultContextCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGInternalRectangleNode *>(given);
    }
    return QSGDefaultContext::createInternalRectangleNode();
  }

  //  QSGInternalImageNode
  //      *QSGDefaultContext::createInternalImageNode(QSGRenderContext
  //      *renderContext)
  QSGInternalImageNode *createInternalImageNode(
      QSGRenderContext *renderContext) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDefaultContextCall4 call = reinterpret_cast<CuteQSGDefaultContextCall4>(taken[4]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalImageNode *>(given);
    }
    return QSGDefaultContext::createInternalImageNode(renderContext);
  }

  //  QSGPainterNode
  //      *QSGDefaultContext::createPainterNode(QQuickPaintedItem *item)
  QSGPainterNode *createPainterNode(QQuickPaintedItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDefaultContextCall5 call = reinterpret_cast<CuteQSGDefaultContextCall5>(taken[5]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<QSGPainterNode *>(given);
    }
    return QSGDefaultContext::createPainterNode(item);
  }

  //  QSGGlyphNode *QSGDefaultContext::createGlyphNode(QSGRenderContext
  //      *rc, QSGTextNode::RenderType renderType)
  QSGGlyphNode *createGlyphNode(
      QSGRenderContext *rc,
      QSGTextNode::RenderType renderType) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDefaultContextCall6 call = reinterpret_cast<CuteQSGDefaultContextCall6>(taken[6]);
      void * given = call(this, rc, static_cast<int>(renderType), &handled);
      if (handled) return static_cast<QSGGlyphNode *>(given);
    }
    return QSGDefaultContext::createGlyphNode(rc, renderType);
  }

  //  QSGInternalTextNode
  //      *QSGDefaultContext::createInternalTextNode(QSGRenderContext
  //      *renderContext)
  QSGInternalTextNode *createInternalTextNode(
      QSGRenderContext *renderContext) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDefaultContextCall7 call = reinterpret_cast<CuteQSGDefaultContextCall7>(taken[7]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalTextNode *>(given);
    }
    return QSGDefaultContext::createInternalTextNode(renderContext);
  }

  //  QSGLayer *QSGDefaultContext::createLayer(QSGRenderContext
  //      *renderContext)
  QSGLayer *createLayer(QSGRenderContext *renderContext) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGDefaultContextCall8 call = reinterpret_cast<CuteQSGDefaultContextCall8>(taken[8]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGLayer *>(given);
    }
    return QSGDefaultContext::createLayer(renderContext);
  }

  //  QSurfaceFormat QSGDefaultContext::defaultSurfaceFormat() const
  QSurfaceFormat defaultSurfaceFormat() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGDefaultContextCall9 call = reinterpret_cast<CuteQSGDefaultContextCall9>(taken[9]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGDefaultContext::defaultSurfaceFormat();
  }

  //  QSGRendererInterface
  //      *QSGDefaultContext::rendererInterface(QSGRenderContext
  //      *renderContext)
  QSGRendererInterface *rendererInterface(
      QSGRenderContext *renderContext) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDefaultContextCall10 call = reinterpret_cast<CuteQSGDefaultContextCall10>(taken[10]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGRendererInterface *>(given);
    }
    return QSGDefaultContext::rendererInterface(renderContext);
  }

  //  QSGRectangleNode *QSGDefaultContext::createRectangleNode()
  QSGRectangleNode *createRectangleNode() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDefaultContextCall11 call = reinterpret_cast<CuteQSGDefaultContextCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRectangleNode *>(given);
    }
    return QSGDefaultContext::createRectangleNode();
  }

  //  QSGImageNode *QSGDefaultContext::createImageNode()
  QSGImageNode *createImageNode() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDefaultContextCall12 call = reinterpret_cast<CuteQSGDefaultContextCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGImageNode *>(given);
    }
    return QSGDefaultContext::createImageNode();
  }

  //  QSGNinePatchNode *QSGDefaultContext::createNinePatchNode()
  QSGNinePatchNode *createNinePatchNode() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDefaultContextCall13 call = reinterpret_cast<CuteQSGDefaultContextCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGNinePatchNode *>(given);
    }
    return QSGDefaultContext::createNinePatchNode();
  }

#if QT_CONFIG(quick_sprite)
  //  QSGSpriteNode *QSGDefaultContext::createSpriteNode()
  QSGSpriteNode *createSpriteNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGDefaultContextCall14 call = reinterpret_cast<CuteQSGDefaultContextCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGSpriteNode *>(given);
    }
    return QSGDefaultContext::createSpriteNode();
  }
#endif  // QT_CONFIG(quick_sprite)

  //  QSGGuiThreadShaderEffectManager
  //      *QSGDefaultContext::createGuiThreadShaderEffectManager()
  QSGGuiThreadShaderEffectManager *createGuiThreadShaderEffectManager() override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGDefaultContextCall15 call = reinterpret_cast<CuteQSGDefaultContextCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGGuiThreadShaderEffectManager *>(given);
    }
    return QSGDefaultContext::createGuiThreadShaderEffectManager();
  }

  //  QSGShaderEffectNode
  //      *QSGDefaultContext::createShaderEffectNode(QSGRenderContext
  //      *renderContext)
  QSGShaderEffectNode *createShaderEffectNode(
      QSGRenderContext *renderContext) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGDefaultContextCall16 call = reinterpret_cast<CuteQSGDefaultContextCall16>(taken[16]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGShaderEffectNode *>(given);
    }
    return QSGDefaultContext::createShaderEffectNode(renderContext);
  }

  //  QSGTextNode::RenderType
  //      QSGDefaultContext::processTextRenderType(QSGTextNode::RenderType
  //      renderType)
  QSGTextNode::RenderType processTextRenderType(
      QSGTextNode::RenderType renderType) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGDefaultContextCall17 call = reinterpret_cast<CuteQSGDefaultContextCall17>(taken[17]);
      int given = call(this, static_cast<int>(renderType), &handled);
      if (handled) return static_cast<QSGTextNode::RenderType>(given);
    }
    return QSGDefaultContext::processTextRenderType(renderType);
  }

  //  GraphicsApi QSGDefaultContext::graphicsApi() const
  QSGRendererInterface::GraphicsApi graphicsApi() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGDefaultContextCall18 call = reinterpret_cast<CuteQSGDefaultContextCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGRendererInterface::GraphicsApi>(given);
    }
    return QSGDefaultContext::graphicsApi();
  }

  //  ShaderType QSGDefaultContext::shaderType() const
  QSGRendererInterface::ShaderType shaderType() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGDefaultContextCall19 call = reinterpret_cast<CuteQSGDefaultContextCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGRendererInterface::ShaderType>(given);
    }
    return QSGDefaultContext::shaderType();
  }

  //  ShaderCompilationTypes QSGDefaultContext::shaderCompilationType()
  //      const
  QSGRendererInterface::ShaderCompilationTypes shaderCompilationType() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGDefaultContextCall20 call = reinterpret_cast<CuteQSGDefaultContextCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRendererInterface::ShaderCompilationType>::fromInt(given);
    }
    return QSGDefaultContext::shaderCompilationType();
  }

  //  ShaderSourceTypes QSGDefaultContext::shaderSourceType() const
  QSGRendererInterface::ShaderSourceTypes shaderSourceType() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGDefaultContextCall21 call = reinterpret_cast<CuteQSGDefaultContextCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRendererInterface::ShaderSourceType>::fromInt(given);
    }
    return QSGDefaultContext::shaderSourceType();
  }

  //  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
  QAnimationDriver *createAnimationDriver(QObject *parent) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGDefaultContextCall22 call = reinterpret_cast<CuteQSGDefaultContextCall22>(taken[22]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGContext::createAnimationDriver(parent);
  }

  //  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
  //      *driver)
  float vsyncIntervalForAnimationDriver(QAnimationDriver *driver) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGDefaultContextCall23 call = reinterpret_cast<CuteQSGDefaultContextCall23>(taken[23]);
      float given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::vsyncIntervalForAnimationDriver(driver);
  }

  //  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
  bool isVSyncDependent(QAnimationDriver *driver) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGDefaultContextCall24 call = reinterpret_cast<CuteQSGDefaultContextCall24>(taken[24]);
      bool given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::isVSyncDependent(driver);
  }

  //  QSize QSGContext::minimumFBOSize() const
  QSize minimumFBOSize() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGDefaultContextCall25 call = reinterpret_cast<CuteQSGDefaultContextCall25>(taken[25]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGContext::minimumFBOSize();
  }

  //  QSGTextNode *QSGContext::createTextNode(QSGRenderContext
  //      *renderContext)
  QSGTextNode *createTextNode(QSGRenderContext *renderContext) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSGDefaultContextCall26 call = reinterpret_cast<CuteQSGDefaultContextCall26>(taken[26]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGTextNode *>(given);
    }
    return QSGContext::createTextNode(renderContext);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSGDefaultContextCall27 call = reinterpret_cast<CuteQSGDefaultContextCall27>(taken[27]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSGDefaultContextCall28 call = reinterpret_cast<CuteQSGDefaultContextCall28>(taken[28]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSGDefaultContextCall29 call = reinterpret_cast<CuteQSGDefaultContextCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSGDefaultContextCall30 call = reinterpret_cast<CuteQSGDefaultContextCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSGDefaultContextCall31 call = reinterpret_cast<CuteQSGDefaultContextCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSGDefaultContextCall32 call = reinterpret_cast<CuteQSGDefaultContextCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSGDefaultContextCall33 call = reinterpret_cast<CuteQSGDefaultContextCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGDefaultContext::QSGDefaultContext(QObject *parent)
extern "C" Q_DECL_EXPORT
QSGDefaultContext *ritual_ZN17QSGDefaultContextC1EP7QObject(
    QObject *parent) {
  return new CuteQSGDefaultContext(parent);
}

//  QSGDefaultContext::~QSGDefaultContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGDefaultContextD1Ev(QSGDefaultContext *self) {
  delete self;
}

//  void QSGDefaultContext::renderContextInitialized(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGDefaultContext24renderContextInitializedEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  self->renderContextInitialized(renderContext);
}

//  void QSGDefaultContext::renderContextInvalidated(QSGRenderContext *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGDefaultContext24renderContextInvalidatedEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *a0) {
  self->renderContextInvalidated(a0);
}

//  QSGRenderContext *QSGDefaultContext::createRenderContext()
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZN17QSGDefaultContext19createRenderContextEv(
    QSGDefaultContext *self) {
  return self->createRenderContext();
}

//  QSGInternalRectangleNode
//      *QSGDefaultContext::createInternalRectangleNode()
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_ZN17QSGDefaultContext27createInternalRectangleNodeEv(
    QSGDefaultContext *self) {
  return self->createInternalRectangleNode();
}

//  QSGInternalImageNode
//      *QSGDefaultContext::createInternalImageNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalImageNode *ritual_ZN17QSGDefaultContext23createInternalImageNodeEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->createInternalImageNode(renderContext);
}

//  QSGPainterNode *QSGDefaultContext::createPainterNode(QQuickPaintedItem
//      *item)
extern "C" Q_DECL_EXPORT
QSGPainterNode *ritual_ZN17QSGDefaultContext17createPainterNodeEP17QQuickPaintedItem(
    QSGDefaultContext *self,
    QQuickPaintedItem *item) {
  return self->createPainterNode(item);
}

//  QSGGlyphNode *QSGDefaultContext::createGlyphNode(QSGRenderContext *rc,
//      QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_ZN17QSGDefaultContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE(
    QSGDefaultContext *self,
    QSGRenderContext *rc,
    QSGTextNode::RenderType renderType) {
  return self->createGlyphNode(rc, renderType);
}

//  QSGInternalTextNode
//      *QSGDefaultContext::createInternalTextNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_ZN17QSGDefaultContext22createInternalTextNodeEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->createInternalTextNode(renderContext);
}

//  QSGLayer *QSGDefaultContext::createLayer(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGLayer *ritual_ZN17QSGDefaultContext11createLayerEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->createLayer(renderContext);
}

//  QSurfaceFormat QSGDefaultContext::defaultSurfaceFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK17QSGDefaultContext20defaultSurfaceFormatEv(
    const QSGDefaultContext *self) {
  return new QSurfaceFormat(self->defaultSurfaceFormat());
}

//  QSGRendererInterface
//      *QSGDefaultContext::rendererInterface(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_ZN17QSGDefaultContext17rendererInterfaceEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->rendererInterface(renderContext);
}

//  QSGRectangleNode *QSGDefaultContext::createRectangleNode()
extern "C" Q_DECL_EXPORT
QSGRectangleNode *ritual_ZN17QSGDefaultContext19createRectangleNodeEv(
    QSGDefaultContext *self) {
  return self->createRectangleNode();
}

//  QSGImageNode *QSGDefaultContext::createImageNode()
extern "C" Q_DECL_EXPORT
QSGImageNode *ritual_ZN17QSGDefaultContext15createImageNodeEv(
    QSGDefaultContext *self) {
  return self->createImageNode();
}

//  QSGNinePatchNode *QSGDefaultContext::createNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGNinePatchNode *ritual_ZN17QSGDefaultContext19createNinePatchNodeEv(
    QSGDefaultContext *self) {
  return self->createNinePatchNode();
}

#if QT_CONFIG(quick_sprite)
//  QSGSpriteNode *QSGDefaultContext::createSpriteNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_ZN17QSGDefaultContext16createSpriteNodeEv(
    QSGDefaultContext *self) {
  return self->createSpriteNode();
}
#endif  // QT_CONFIG(quick_sprite)

//  QSGGuiThreadShaderEffectManager
//      *QSGDefaultContext::createGuiThreadShaderEffectManager()
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager *ritual_ZN17QSGDefaultContext34createGuiThreadShaderEffectManagerEv(
    QSGDefaultContext *self) {
  return self->createGuiThreadShaderEffectManager();
}

//  QSGShaderEffectNode
//      *QSGDefaultContext::createShaderEffectNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGShaderEffectNode *ritual_ZN17QSGDefaultContext22createShaderEffectNodeEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->createShaderEffectNode(renderContext);
}

//  void QSGDefaultContext::setDistanceFieldEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGDefaultContext23setDistanceFieldEnabledEb(
    QSGDefaultContext *self,
    bool enabled) {
  self->setDistanceFieldEnabled(enabled);
}

//  bool QSGDefaultContext::isDistanceFieldEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSGDefaultContext22isDistanceFieldEnabledEv(
    const QSGDefaultContext *self) {
  return self->isDistanceFieldEnabled();
}

//  QSGTextNode::RenderType
//      QSGDefaultContext::processTextRenderType(QSGTextNode::RenderType
//      renderType)
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_ZN17QSGDefaultContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGDefaultContext *self,
    QSGTextNode::RenderType renderType) {
  return self->processTextRenderType(renderType);
}

//  GraphicsApi QSGDefaultContext::graphicsApi() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_ZNK17QSGDefaultContext11graphicsApiEv(
    const QSGDefaultContext *self) {
  return self->graphicsApi();
}

//  ShaderType QSGDefaultContext::shaderType() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::ShaderType ritual_ZNK17QSGDefaultContext10shaderTypeEv(
    const QSGDefaultContext *self) {
  return self->shaderType();
}

//  ShaderCompilationTypes QSGDefaultContext::shaderCompilationType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSGDefaultContext21shaderCompilationTypeEv(
    const QSGDefaultContext *self) {
  return static_cast<int>(self->shaderCompilationType().toInt());
}

//  ShaderSourceTypes QSGDefaultContext::shaderSourceType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSGDefaultContext16shaderSourceTypeEv(
    const QSGDefaultContext *self) {
  return static_cast<int>(self->shaderSourceType().toInt());
}

//  QSGDefaultContext as the QSGRendererInterface it is built on
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_cast_QSGDefaultContext_QSGRendererInterface(
    QSGDefaultContext *self) {
  return static_cast<QSGRendererInterface *>(self);
}

//  a Python function taken by a CuteQSGDefaultContext, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDefaultContext(
    QSGDefaultContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDefaultContext *>(self)->take(key, call);
}

//  void QSGDefaultContext::renderContextInitialized(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGDefaultContext24renderContextInitializedEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  self->QSGDefaultContext::renderContextInitialized(renderContext);
}

//  void QSGDefaultContext::renderContextInvalidated(QSGRenderContext *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSGDefaultContext24renderContextInvalidatedEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *a0) {
  self->QSGDefaultContext::renderContextInvalidated(a0);
}

//  QSGRenderContext *QSGDefaultContext::createRenderContext()
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_own_ZN17QSGDefaultContext19createRenderContextEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createRenderContext();
}

//  QSGInternalRectangleNode
//      *QSGDefaultContext::createInternalRectangleNode()
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_own_ZN17QSGDefaultContext27createInternalRectangleNodeEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createInternalRectangleNode();
}

//  QSGInternalImageNode
//      *QSGDefaultContext::createInternalImageNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalImageNode *ritual_own_ZN17QSGDefaultContext23createInternalImageNodeEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGDefaultContext::createInternalImageNode(renderContext);
}

//  QSGPainterNode *QSGDefaultContext::createPainterNode(QQuickPaintedItem
//      *item)
extern "C" Q_DECL_EXPORT
QSGPainterNode *ritual_own_ZN17QSGDefaultContext17createPainterNodeEP17QQuickPaintedItem(
    QSGDefaultContext *self,
    QQuickPaintedItem *item) {
  return self->QSGDefaultContext::createPainterNode(item);
}

//  QSGGlyphNode *QSGDefaultContext::createGlyphNode(QSGRenderContext *rc,
//      QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_own_ZN17QSGDefaultContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE(
    QSGDefaultContext *self,
    QSGRenderContext *rc,
    QSGTextNode::RenderType renderType) {
  return self->QSGDefaultContext::createGlyphNode(rc, renderType);
}

//  QSGInternalTextNode
//      *QSGDefaultContext::createInternalTextNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_own_ZN17QSGDefaultContext22createInternalTextNodeEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGDefaultContext::createInternalTextNode(renderContext);
}

//  QSGLayer *QSGDefaultContext::createLayer(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGLayer *ritual_own_ZN17QSGDefaultContext11createLayerEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGDefaultContext::createLayer(renderContext);
}

//  QSurfaceFormat QSGDefaultContext::defaultSurfaceFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_own_ZNK17QSGDefaultContext20defaultSurfaceFormatEv(
    const QSGDefaultContext *self) {
  return new QSurfaceFormat(self->QSGDefaultContext::defaultSurfaceFormat());
}

//  QSGRendererInterface
//      *QSGDefaultContext::rendererInterface(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_own_ZN17QSGDefaultContext17rendererInterfaceEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGDefaultContext::rendererInterface(renderContext);
}

//  QSGRectangleNode *QSGDefaultContext::createRectangleNode()
extern "C" Q_DECL_EXPORT
QSGRectangleNode *ritual_own_ZN17QSGDefaultContext19createRectangleNodeEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createRectangleNode();
}

//  QSGImageNode *QSGDefaultContext::createImageNode()
extern "C" Q_DECL_EXPORT
QSGImageNode *ritual_own_ZN17QSGDefaultContext15createImageNodeEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createImageNode();
}

//  QSGNinePatchNode *QSGDefaultContext::createNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGNinePatchNode *ritual_own_ZN17QSGDefaultContext19createNinePatchNodeEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createNinePatchNode();
}

#if QT_CONFIG(quick_sprite)
//  QSGSpriteNode *QSGDefaultContext::createSpriteNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_own_ZN17QSGDefaultContext16createSpriteNodeEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createSpriteNode();
}
#endif  // QT_CONFIG(quick_sprite)

//  QSGGuiThreadShaderEffectManager
//      *QSGDefaultContext::createGuiThreadShaderEffectManager()
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager *ritual_own_ZN17QSGDefaultContext34createGuiThreadShaderEffectManagerEv(
    QSGDefaultContext *self) {
  return self->QSGDefaultContext::createGuiThreadShaderEffectManager();
}

//  QSGShaderEffectNode
//      *QSGDefaultContext::createShaderEffectNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGShaderEffectNode *ritual_own_ZN17QSGDefaultContext22createShaderEffectNodeEP16QSGRenderContext(
    QSGDefaultContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGDefaultContext::createShaderEffectNode(renderContext);
}

//  QSGTextNode::RenderType
//      QSGDefaultContext::processTextRenderType(QSGTextNode::RenderType
//      renderType)
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_own_ZN17QSGDefaultContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGDefaultContext *self,
    QSGTextNode::RenderType renderType) {
  return self->QSGDefaultContext::processTextRenderType(renderType);
}

//  GraphicsApi QSGDefaultContext::graphicsApi() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_own_ZNK17QSGDefaultContext11graphicsApiEv(
    const QSGDefaultContext *self) {
  return self->QSGDefaultContext::graphicsApi();
}

//  ShaderType QSGDefaultContext::shaderType() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::ShaderType ritual_own_ZNK17QSGDefaultContext10shaderTypeEv(
    const QSGDefaultContext *self) {
  return self->QSGDefaultContext::shaderType();
}

//  ShaderCompilationTypes QSGDefaultContext::shaderCompilationType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QSGDefaultContext21shaderCompilationTypeEv(
    const QSGDefaultContext *self) {
  return static_cast<int>(
      self->QSGDefaultContext::shaderCompilationType().toInt());
}

//  ShaderSourceTypes QSGDefaultContext::shaderSourceType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QSGDefaultContext16shaderSourceTypeEv(
    const QSGDefaultContext *self) {
  return static_cast<int>(
      self->QSGDefaultContext::shaderSourceType().toInt());
}
