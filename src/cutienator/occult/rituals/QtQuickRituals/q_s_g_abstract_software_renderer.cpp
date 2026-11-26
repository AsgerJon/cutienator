//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgabstractsoftwarerenderer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgabstractsoftwarerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderablenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSGAbstractSoftwareRenderer that Python can take functions over in. Every QSGAbstractSoftwareRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGAbstractSoftwareRendererCall0)(const void *, QSGNode *, int, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall1)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall2)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall3)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall4)(const void *, const QByteArray *, int *);
typedef bool (*CuteQSGAbstractSoftwareRendererCall5)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall6)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall7)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall8)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall9)(const void *, int *);
typedef void (*CuteQSGAbstractSoftwareRendererCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGAbstractSoftwareRendererCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGAbstractSoftwareRendererCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractSoftwareRendererCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractSoftwareRendererCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractSoftwareRendererCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractSoftwareRendererCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractSoftwareRendererCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGAbstractSoftwareRenderer : public QSGAbstractSoftwareRenderer {
public:
  using QSGAbstractSoftwareRenderer::QSGAbstractSoftwareRenderer;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11renderSceneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer18prepareSceneInlineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer17renderSceneInlineEv")) {
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

  //  void QSGAbstractSoftwareRenderer::nodeChanged(QSGNode *node,
  //      QSGNode::DirtyState state)
  void nodeChanged(QSGNode *node, QSGNode::DirtyState state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall0 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall0>(taken[0]);
      call(this, node, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
    QSGAbstractSoftwareRenderer::nodeChanged(node, state);
  }

  //  void QSGRenderer::renderScene()
  void renderScene() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall1 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderScene();
  }

  //  void QSGRenderer::prepareSceneInline()
  void prepareSceneInline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall2 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareSceneInline();
  }

  //  void QSGRenderer::renderSceneInline()
  void renderSceneInline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall3 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderSceneInline();
  }

  //  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
  void setVisualizationMode(const QByteArray &a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall4 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall4>(taken[4]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSGRenderer::setVisualizationMode(a0);
  }

  //  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
  bool hasVisualizationModeWithContinuousUpdate() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall5 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderer::hasVisualizationModeWithContinuousUpdate();
  }

  //  void QSGRenderer::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall6 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::releaseCachedResources();
  }

  //  void QSGRenderer::render()
  void render() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall7 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderer::prepareInline()
  void prepareInline() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall8 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareInline();
  }

  //  void QSGRenderer::renderInline()
  void renderInline() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall9 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderInline();
  }

  //  void QSGRenderer::preprocess()
  void preprocess() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGAbstractSoftwareRendererCall10 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall10>(taken[10]);
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
      CuteQSGAbstractSoftwareRendererCall11 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall11>(taken[11]);
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
      CuteQSGAbstractSoftwareRendererCall12 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall12>(taken[12]);
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
      CuteQSGAbstractSoftwareRendererCall13 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall13>(taken[13]);
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
      CuteQSGAbstractSoftwareRendererCall14 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall14>(taken[14]);
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
      CuteQSGAbstractSoftwareRendererCall15 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall15>(taken[15]);
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
      CuteQSGAbstractSoftwareRendererCall16 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall16>(taken[16]);
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
      CuteQSGAbstractSoftwareRendererCall17 call = reinterpret_cast<CuteQSGAbstractSoftwareRendererCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGAbstractSoftwareRenderer::QSGAbstractSoftwareRenderer(QSGRenderContext
//      *context)
extern "C" Q_DECL_EXPORT
QSGAbstractSoftwareRenderer *ritual_ZN27QSGAbstractSoftwareRendererC1EP16QSGRenderContext(
    QSGRenderContext *context) {
  return new CuteQSGAbstractSoftwareRenderer(context);
}

//  QSGAbstractSoftwareRenderer::~QSGAbstractSoftwareRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRendererD1Ev(
    QSGAbstractSoftwareRenderer *self) {
  delete self;
}

//  QSGSoftwareRenderableNode
//      *QSGAbstractSoftwareRenderer::renderableNode(QSGNode *node) const
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderableNode *ritual_ZNK27QSGAbstractSoftwareRenderer14renderableNodeEP7QSGNode(
    const QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  return self->renderableNode(node);
}

//  void QSGAbstractSoftwareRenderer::addNodeMapping(QSGNode *node,
//      QSGSoftwareRenderableNode *renderableNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer14addNodeMappingEP7QSGNodeP25QSGSoftwareRenderableNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node,
    QSGSoftwareRenderableNode *renderableNode) {
  self->addNodeMapping(node, renderableNode);
}

//  void QSGAbstractSoftwareRenderer::appendRenderableNode(QSGSoftwareRendera
//      bleNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer20appendRenderableNodeEP25QSGSoftwareRenderableNode(
    QSGAbstractSoftwareRenderer *self,
    QSGSoftwareRenderableNode *node) {
  self->appendRenderableNode(node);
}

//  void QSGAbstractSoftwareRenderer::nodeChanged(QSGNode *node,
//      QSGNode::DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node,
    int state) {
  self->nodeChanged(node, QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  void QSGAbstractSoftwareRenderer::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer9markDirtyEv(
    QSGAbstractSoftwareRenderer *self) {
  self->markDirty();
}

//  void QSGAbstractSoftwareRenderer::setClearColorEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer20setClearColorEnabledEb(
    QSGAbstractSoftwareRenderer *self,
    bool enable) {
  self->setClearColorEnabled(enable);
}

//  bool QSGAbstractSoftwareRenderer::clearColorEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSGAbstractSoftwareRenderer17clearColorEnabledEv(
    const QSGAbstractSoftwareRenderer *self) {
  return self->clearColorEnabled();
}

//  QRegion QSGAbstractSoftwareRenderer::renderNodes(QPainter *painter)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN27QSGAbstractSoftwareRenderer11renderNodesEP8QPainter(
    QSGAbstractSoftwareRenderer *self,
    QPainter *painter) {
  return new QRegion(self->renderNodes(painter));
}

//  void QSGAbstractSoftwareRenderer::buildRenderList()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer15buildRenderListEv(
    QSGAbstractSoftwareRenderer *self) {
  self->buildRenderList();
}

//  QRegion QSGAbstractSoftwareRenderer::optimizeRenderList()
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN27QSGAbstractSoftwareRenderer18optimizeRenderListEv(
    QSGAbstractSoftwareRenderer *self) {
  return new QRegion(self->optimizeRenderList());
}

//  void QSGAbstractSoftwareRenderer::setBackgroundColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer18setBackgroundColorERK6QColor(
    QSGAbstractSoftwareRenderer *self,
    const QColor *color) {
  self->setBackgroundColor(*color);
}

//  void QSGAbstractSoftwareRenderer::setBackgroundRect(const QRect &rect,
//      qreal devicePixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer17setBackgroundRectERK5QRectd(
    QSGAbstractSoftwareRenderer *self,
    const QRect *rect,
    qreal devicePixelRatio) {
  self->setBackgroundRect(*rect, devicePixelRatio);
}

//  QColor QSGAbstractSoftwareRenderer::backgroundColor()
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN27QSGAbstractSoftwareRenderer15backgroundColorEv(
    QSGAbstractSoftwareRenderer *self) {
  return new QColor(self->backgroundColor());
}

//  QRect QSGAbstractSoftwareRenderer::backgroundRect()
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN27QSGAbstractSoftwareRenderer14backgroundRectEv(
    QSGAbstractSoftwareRenderer *self) {
  return new QRect(self->backgroundRect());
}

//  bool QSGAbstractSoftwareRenderer::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSGAbstractSoftwareRenderer8isOpaqueEv(
    const QSGAbstractSoftwareRenderer *self) {
  return self->isOpaque();
}

//  const QList<QSGSoftwareRenderableNode *>
//      &QSGAbstractSoftwareRenderer::renderableNodes() const
extern "C" Q_DECL_EXPORT
QList<QSGSoftwareRenderableNode *> *ritual_ZNK27QSGAbstractSoftwareRenderer15renderableNodesEv(
    const QSGAbstractSoftwareRenderer *self) {
  return new QList<QSGSoftwareRenderableNode *>(self->renderableNodes());
}

//  void QSGAbstractSoftwareRenderer::nodeAdded(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer9nodeAddedEP7QSGNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  self->nodeAdded(node);
}

//  void QSGAbstractSoftwareRenderer::nodeRemoved(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer11nodeRemovedEP7QSGNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  self->nodeRemoved(node);
}

//  void QSGAbstractSoftwareRenderer::nodeGeometryUpdated(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer19nodeGeometryUpdatedEP7QSGNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  self->nodeGeometryUpdated(node);
}

//  void QSGAbstractSoftwareRenderer::nodeMaterialUpdated(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer19nodeMaterialUpdatedEP7QSGNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  self->nodeMaterialUpdated(node);
}

//  void QSGAbstractSoftwareRenderer::nodeMatrixUpdated(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer17nodeMatrixUpdatedEP7QSGNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  self->nodeMatrixUpdated(node);
}

//  void QSGAbstractSoftwareRenderer::nodeOpacityUpdated(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSGAbstractSoftwareRenderer18nodeOpacityUpdatedEP7QSGNode(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node) {
  self->nodeOpacityUpdated(node);
}

//  a Python function taken by a CuteQSGAbstractSoftwareRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGAbstractSoftwareRenderer(
    QSGAbstractSoftwareRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGAbstractSoftwareRenderer *>(self)->take(key, call);
}

//  void QSGAbstractSoftwareRenderer::nodeChanged(QSGNode *node,
//      QSGNode::DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSGAbstractSoftwareRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE(
    QSGAbstractSoftwareRenderer *self,
    QSGNode *node,
    int state) {
  self->QSGAbstractSoftwareRenderer::nodeChanged(
      node,
      QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}
