//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qsize.h>
#include <QtGui/qsurfaceformat.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGContext that Python can take functions over in. Every QSGContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGContextCall0)(const void *, QSGRenderContext *, int *);
typedef void (*CuteQSGContextCall1)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGContextCall2)(const void *, int *);
typedef void * (*CuteQSGContextCall3)(const void *, int *);
typedef void * (*CuteQSGContextCall4)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGContextCall5)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGContextCall6)(const void *, QQuickPaintedItem *, int *);
typedef void * (*CuteQSGContextCall7)(const void *, QSGRenderContext *, int, int *);
typedef void * (*CuteQSGContextCall8)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGContextCall9)(const void *, int *);
typedef void * (*CuteQSGContextCall10)(const void *, QSGRenderContext *, int *);
#if QT_CONFIG(quick_sprite)
typedef void * (*CuteQSGContextCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef void * (*CuteQSGContextCall12)(const void *, QObject *, int *);
typedef float (*CuteQSGContextCall13)(const void *, QAnimationDriver *, int *);
typedef bool (*CuteQSGContextCall14)(const void *, QAnimationDriver *, int *);
typedef const QSize * (*CuteQSGContextCall15)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQSGContextCall16)(const void *, int *);
typedef void * (*CuteQSGContextCall17)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGContextCall18)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGContextCall19)(const void *, int *);
typedef void * (*CuteQSGContextCall20)(const void *, int *);
typedef void * (*CuteQSGContextCall21)(const void *, int *);
typedef int (*CuteQSGContextCall22)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGContextCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGContextCall24)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextCall25)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextCall26)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGContextCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGContext : public QSGContext {
public:
  using QSGContext::QSGContext;
  void *taken[30] = {};

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
    if (!std::strcmp(key, "_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext17createPainterNodeEP17QQuickPaintedItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext11createLayerEP16QSGRenderContext")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext34createGuiThreadShaderEffectManagerEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN10QSGContext16createSpriteNodeEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN10QSGContext21createAnimationDriverEP7QObject")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationDriver")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext14minimumFBOSizeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext20defaultSurfaceFormatEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext14createTextNodeEP16QSGRenderContext")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createRectangleNodeEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext15createImageNodeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createNinePatchNodeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGContext::renderContextInitialized(QSGRenderContext
  //      *renderContext)
  void renderContextInitialized(QSGRenderContext *renderContext) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGContextCall0 call = reinterpret_cast<CuteQSGContextCall0>(taken[0]);
      call(this, renderContext, &handled);
      if (handled) return;
    }
    QSGContext::renderContextInitialized(renderContext);
  }

  //  void QSGContext::renderContextInvalidated(QSGRenderContext
  //      *renderContext)
  void renderContextInvalidated(QSGRenderContext *renderContext) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGContextCall1 call = reinterpret_cast<CuteQSGContextCall1>(taken[1]);
      call(this, renderContext, &handled);
      if (handled) return;
    }
    QSGContext::renderContextInvalidated(renderContext);
  }

  //  QSGRenderContext *QSGContext::createRenderContext()
  QSGRenderContext *createRenderContext() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGContextCall2 call = reinterpret_cast<CuteQSGContextCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return {};
  }

  //  QSGInternalRectangleNode *QSGContext::createInternalRectangleNode()
  QSGInternalRectangleNode *createInternalRectangleNode() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGContextCall3 call = reinterpret_cast<CuteQSGContextCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGInternalRectangleNode *>(given);
    }
    return {};
  }

  //  QSGInternalImageNode
  //      *QSGContext::createInternalImageNode(QSGRenderContext
  //      *renderContext)
  QSGInternalImageNode *createInternalImageNode(
      QSGRenderContext *renderContext) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGContextCall4 call = reinterpret_cast<CuteQSGContextCall4>(taken[4]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalImageNode *>(given);
    }
    return {};
  }

  //  QSGInternalTextNode
  //      *QSGContext::createInternalTextNode(QSGRenderContext
  //      *renderContext)
  QSGInternalTextNode *createInternalTextNode(
      QSGRenderContext *renderContext) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGContextCall5 call = reinterpret_cast<CuteQSGContextCall5>(taken[5]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalTextNode *>(given);
    }
    return QSGContext::createInternalTextNode(renderContext);
  }

  //  QSGPainterNode *QSGContext::createPainterNode(QQuickPaintedItem
  //      *item)
  QSGPainterNode *createPainterNode(QQuickPaintedItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGContextCall6 call = reinterpret_cast<CuteQSGContextCall6>(taken[6]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<QSGPainterNode *>(given);
    }
    return {};
  }

  //  QSGGlyphNode *QSGContext::createGlyphNode(QSGRenderContext *rc,
  //      QSGTextNode::RenderType renderType)
  QSGGlyphNode *createGlyphNode(
      QSGRenderContext *rc,
      QSGTextNode::RenderType renderType) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGContextCall7 call = reinterpret_cast<CuteQSGContextCall7>(taken[7]);
      void * given = call(this, rc, static_cast<int>(renderType), &handled);
      if (handled) return static_cast<QSGGlyphNode *>(given);
    }
    return {};
  }

  //  QSGLayer *QSGContext::createLayer(QSGRenderContext *renderContext)
  QSGLayer *createLayer(QSGRenderContext *renderContext) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGContextCall8 call = reinterpret_cast<CuteQSGContextCall8>(taken[8]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGLayer *>(given);
    }
    return {};
  }

  //  QSGGuiThreadShaderEffectManager
  //      *QSGContext::createGuiThreadShaderEffectManager()
  QSGGuiThreadShaderEffectManager *createGuiThreadShaderEffectManager() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGContextCall9 call = reinterpret_cast<CuteQSGContextCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGGuiThreadShaderEffectManager *>(given);
    }
    return QSGContext::createGuiThreadShaderEffectManager();
  }

  //  QSGShaderEffectNode
  //      *QSGContext::createShaderEffectNode(QSGRenderContext
  //      *renderContext)
  QSGShaderEffectNode *createShaderEffectNode(
      QSGRenderContext *renderContext) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGContextCall10 call = reinterpret_cast<CuteQSGContextCall10>(taken[10]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGShaderEffectNode *>(given);
    }
    return QSGContext::createShaderEffectNode(renderContext);
  }

#if QT_CONFIG(quick_sprite)
  //  QSGSpriteNode *QSGContext::createSpriteNode()
  QSGSpriteNode *createSpriteNode() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGContextCall11 call = reinterpret_cast<CuteQSGContextCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGSpriteNode *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(quick_sprite)

  //  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
  QAnimationDriver *createAnimationDriver(QObject *parent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGContextCall12 call = reinterpret_cast<CuteQSGContextCall12>(taken[12]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGContext::createAnimationDriver(parent);
  }

  //  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
  //      *driver)
  float vsyncIntervalForAnimationDriver(QAnimationDriver *driver) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGContextCall13 call = reinterpret_cast<CuteQSGContextCall13>(taken[13]);
      float given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::vsyncIntervalForAnimationDriver(driver);
  }

  //  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
  bool isVSyncDependent(QAnimationDriver *driver) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGContextCall14 call = reinterpret_cast<CuteQSGContextCall14>(taken[14]);
      bool given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::isVSyncDependent(driver);
  }

  //  QSize QSGContext::minimumFBOSize() const
  QSize minimumFBOSize() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGContextCall15 call = reinterpret_cast<CuteQSGContextCall15>(taken[15]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGContext::minimumFBOSize();
  }

  //  QSurfaceFormat QSGContext::defaultSurfaceFormat() const
  QSurfaceFormat defaultSurfaceFormat() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGContextCall16 call = reinterpret_cast<CuteQSGContextCall16>(taken[16]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QSGRendererInterface *QSGContext::rendererInterface(QSGRenderContext
  //      *renderContext)
  QSGRendererInterface *rendererInterface(
      QSGRenderContext *renderContext) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGContextCall17 call = reinterpret_cast<CuteQSGContextCall17>(taken[17]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGRendererInterface *>(given);
    }
    return QSGContext::rendererInterface(renderContext);
  }

  //  QSGTextNode *QSGContext::createTextNode(QSGRenderContext
  //      *renderContext)
  QSGTextNode *createTextNode(QSGRenderContext *renderContext) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGContextCall18 call = reinterpret_cast<CuteQSGContextCall18>(taken[18]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGTextNode *>(given);
    }
    return QSGContext::createTextNode(renderContext);
  }

  //  QSGRectangleNode *QSGContext::createRectangleNode()
  QSGRectangleNode *createRectangleNode() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGContextCall19 call = reinterpret_cast<CuteQSGContextCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRectangleNode *>(given);
    }
    return {};
  }

  //  QSGImageNode *QSGContext::createImageNode()
  QSGImageNode *createImageNode() override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGContextCall20 call = reinterpret_cast<CuteQSGContextCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGImageNode *>(given);
    }
    return {};
  }

  //  QSGNinePatchNode *QSGContext::createNinePatchNode()
  QSGNinePatchNode *createNinePatchNode() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGContextCall21 call = reinterpret_cast<CuteQSGContextCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGNinePatchNode *>(given);
    }
    return {};
  }

  //  QSGTextNode::RenderType
  //      QSGContext::processTextRenderType(QSGTextNode::RenderType
  //      renderType)
  QSGTextNode::RenderType processTextRenderType(
      QSGTextNode::RenderType renderType) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGContextCall22 call = reinterpret_cast<CuteQSGContextCall22>(taken[22]);
      int given = call(this, static_cast<int>(renderType), &handled);
      if (handled) return static_cast<QSGTextNode::RenderType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGContextCall23 call = reinterpret_cast<CuteQSGContextCall23>(taken[23]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGContextCall24 call = reinterpret_cast<CuteQSGContextCall24>(taken[24]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGContextCall25 call = reinterpret_cast<CuteQSGContextCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSGContextCall26 call = reinterpret_cast<CuteQSGContextCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSGContextCall27 call = reinterpret_cast<CuteQSGContextCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSGContextCall28 call = reinterpret_cast<CuteQSGContextCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSGContextCall29 call = reinterpret_cast<CuteQSGContextCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QSGContext10metaObjectEv(
    const QSGContext *self) {
  return self->metaObject();
}

//  void *QSGContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QSGContext11qt_metacastEPKc(
    QSGContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGContext::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSGContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSGContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSGContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGContext::tr(s, c, n));
}

//  QSGContext::QSGContext(QObject *parent)
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZN10QSGContextC1EP7QObject(QObject *parent) {
  return new CuteQSGContext(parent);
}

//  QSGContext::~QSGContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGContextD1Ev(QSGContext *self) {
  delete self;
}

//  void QSGContext::renderContextInitialized(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGContext24renderContextInitializedEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  self->renderContextInitialized(renderContext);
}

//  void QSGContext::renderContextInvalidated(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  self->renderContextInvalidated(renderContext);
}

//  QSGRenderContext *QSGContext::createRenderContext()
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZN10QSGContext19createRenderContextEv(
    QSGContext *self) {
  return self->createRenderContext();
}

//  QSGInternalRectangleNode *QSGContext::createInternalRectangleNode(const
//      QRectF &rect, const QColor &c)
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_ZN10QSGContext27createInternalRectangleNodeERK6QRectFRK6QColor(
    QSGContext *self,
    const QRectF *rect,
    const QColor *c) {
  return self->createInternalRectangleNode(*rect, *c);
}

//  QSGInternalRectangleNode *QSGContext::createInternalRectangleNode()
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_ZN10QSGContext27createInternalRectangleNodeEv(
    QSGContext *self) {
  return self->createInternalRectangleNode();
}

//  QSGInternalImageNode
//      *QSGContext::createInternalImageNode(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalImageNode *ritual_ZN10QSGContext23createInternalImageNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->createInternalImageNode(renderContext);
}

//  QSGInternalTextNode *QSGContext::createInternalTextNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->createInternalTextNode(renderContext);
}

//  QSGPainterNode *QSGContext::createPainterNode(QQuickPaintedItem *item)
extern "C" Q_DECL_EXPORT
QSGPainterNode *ritual_ZN10QSGContext17createPainterNodeEP17QQuickPaintedItem(
    QSGContext *self,
    QQuickPaintedItem *item) {
  return self->createPainterNode(item);
}

//  QSGGlyphNode *QSGContext::createGlyphNode(QSGRenderContext *rc,
//      QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_ZN10QSGContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE(
    QSGContext *self,
    QSGRenderContext *rc,
    QSGTextNode::RenderType renderType) {
  return self->createGlyphNode(rc, renderType);
}

//  QSGLayer *QSGContext::createLayer(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGLayer *ritual_ZN10QSGContext11createLayerEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->createLayer(renderContext);
}

//  QSGGuiThreadShaderEffectManager
//      *QSGContext::createGuiThreadShaderEffectManager()
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager *ritual_ZN10QSGContext34createGuiThreadShaderEffectManagerEv(
    QSGContext *self) {
  return self->createGuiThreadShaderEffectManager();
}

//  QSGShaderEffectNode *QSGContext::createShaderEffectNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGShaderEffectNode *ritual_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->createShaderEffectNode(renderContext);
}

#if QT_CONFIG(quick_sprite)
//  QSGSpriteNode *QSGContext::createSpriteNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_ZN10QSGContext16createSpriteNodeEv(QSGContext *self) {
  return self->createSpriteNode();
}
#endif  // QT_CONFIG(quick_sprite)

//  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZN10QSGContext21createAnimationDriverEP7QObject(
    QSGContext *self,
    QObject *parent) {
  return self->createAnimationDriver(parent);
}

//  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
//      *driver)
extern "C" Q_DECL_EXPORT
float ritual_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationDriver(
    QSGContext *self,
    QAnimationDriver *driver) {
  return self->vsyncIntervalForAnimationDriver(driver);
}

//  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver(
    QSGContext *self,
    QAnimationDriver *driver) {
  return self->isVSyncDependent(driver);
}

//  QSize QSGContext::minimumFBOSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QSGContext14minimumFBOSizeEv(const QSGContext *self) {
  return new QSize(self->minimumFBOSize());
}

//  QSurfaceFormat QSGContext::defaultSurfaceFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK10QSGContext20defaultSurfaceFormatEv(
    const QSGContext *self) {
  return new QSurfaceFormat(self->defaultSurfaceFormat());
}

//  QSGRendererInterface *QSGContext::rendererInterface(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->rendererInterface(renderContext);
}

//  QSGTextNode *QSGContext::createTextNode(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGTextNode *ritual_ZN10QSGContext14createTextNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->createTextNode(renderContext);
}

//  QSGRectangleNode *QSGContext::createRectangleNode()
extern "C" Q_DECL_EXPORT
QSGRectangleNode *ritual_ZN10QSGContext19createRectangleNodeEv(
    QSGContext *self) {
  return self->createRectangleNode();
}

//  QSGImageNode *QSGContext::createImageNode()
extern "C" Q_DECL_EXPORT
QSGImageNode *ritual_ZN10QSGContext15createImageNodeEv(QSGContext *self) {
  return self->createImageNode();
}

//  QSGNinePatchNode *QSGContext::createNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGNinePatchNode *ritual_ZN10QSGContext19createNinePatchNodeEv(
    QSGContext *self) {
  return self->createNinePatchNode();
}

//  QSGTextNode::RenderType
//      QSGContext::processTextRenderType(QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_ZN10QSGContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGContext *self,
    QSGTextNode::RenderType renderType) {
  return self->processTextRenderType(renderType);
}

//  QSGContext *QSGContext::createDefaultContext()
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZN10QSGContext20createDefaultContextEv() {
  return QSGContext::createDefaultContext();
}

//  QQuickTextureFactory *QSGContext::createTextureFactoryFromImage(const
//      QImage &image)
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZN10QSGContext29createTextureFactoryFromImageERK6QImage(
    const QImage *image) {
  return QSGContext::createTextureFactoryFromImage(*image);
}

//  QSGRenderLoop *QSGContext::createWindowManager()
extern "C" Q_DECL_EXPORT
QSGRenderLoop *ritual_ZN10QSGContext19createWindowManagerEv() {
  return QSGContext::createWindowManager();
}

//  void QSGContext::setBackend(const QString &backend)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSGContext10setBackendERK7QString(const QString *backend) {
  QSGContext::setBackend(*backend);
}

//  QString QSGContext::backend()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSGContext7backendEv() {
  return new QString(QSGContext::backend());
}

//  a Python function taken by a CuteQSGContext, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGContext(QSGContext *self, const char *key, void *call) {
  return static_cast<CuteQSGContext *>(self)->take(key, call);
}

//  void QSGContext::renderContextInitialized(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSGContext24renderContextInitializedEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  self->QSGContext::renderContextInitialized(renderContext);
}

//  void QSGContext::renderContextInvalidated(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  self->QSGContext::renderContextInvalidated(renderContext);
}

//  QSGInternalTextNode *QSGContext::createInternalTextNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_own_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGContext::createInternalTextNode(renderContext);
}

//  QSGGuiThreadShaderEffectManager
//      *QSGContext::createGuiThreadShaderEffectManager()
extern "C" Q_DECL_EXPORT
QSGGuiThreadShaderEffectManager *ritual_own_ZN10QSGContext34createGuiThreadShaderEffectManagerEv(
    QSGContext *self) {
  return self->QSGContext::createGuiThreadShaderEffectManager();
}

//  QSGShaderEffectNode *QSGContext::createShaderEffectNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGShaderEffectNode *ritual_own_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGContext::createShaderEffectNode(renderContext);
}

//  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_own_ZN10QSGContext21createAnimationDriverEP7QObject(
    QSGContext *self,
    QObject *parent) {
  return self->QSGContext::createAnimationDriver(parent);
}

//  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
//      *driver)
extern "C" Q_DECL_EXPORT
float ritual_own_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationDriver(
    QSGContext *self,
    QAnimationDriver *driver) {
  return self->QSGContext::vsyncIntervalForAnimationDriver(driver);
}

//  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver(
    QSGContext *self,
    QAnimationDriver *driver) {
  return self->QSGContext::isVSyncDependent(driver);
}

//  QSize QSGContext::minimumFBOSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QSGContext14minimumFBOSizeEv(const QSGContext *self) {
  return new QSize(self->QSGContext::minimumFBOSize());
}

//  QSGRendererInterface *QSGContext::rendererInterface(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_own_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGContext::rendererInterface(renderContext);
}

//  QSGTextNode *QSGContext::createTextNode(QSGRenderContext *renderContext)
extern "C" Q_DECL_EXPORT
QSGTextNode *ritual_own_ZN10QSGContext14createTextNodeEP16QSGRenderContext(
    QSGContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGContext::createTextNode(renderContext);
}
