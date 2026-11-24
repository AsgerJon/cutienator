//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGSoftwareRenderer that Python can take functions over in. Every QSGSoftwareRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwareRendererCall0)(const void *, QSGNode *, int, int *);
typedef void (*CuteQSGSoftwareRendererCall1)(const void *, int *);
typedef void (*CuteQSGSoftwareRendererCall2)(const void *, int *);
typedef void (*CuteQSGSoftwareRendererCall3)(const void *, const QByteArray *, int *);
typedef bool (*CuteQSGSoftwareRendererCall4)(const void *, int *);
typedef void (*CuteQSGSoftwareRendererCall5)(const void *, int *);
typedef void (*CuteQSGSoftwareRendererCall6)(const void *, int *);
typedef void (*CuteQSGSoftwareRendererCall7)(const void *, int *);
typedef void (*CuteQSGSoftwareRendererCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareRendererCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareRendererCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRendererCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRendererCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRendererCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRendererCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRendererCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareRenderer : public QSGSoftwareRenderer {
public:
  using QSGSoftwareRenderer::QSGSoftwareRenderer;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE")) {
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
    if (!std::strcmp(key, "_ZN11QSGRenderer20setVisualizationModeERK10QByteArray")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer22releaseCachedResourcesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer13prepareInlineEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer12renderInlineEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer10preprocessEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
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
      CuteQSGSoftwareRendererCall0 call = reinterpret_cast<CuteQSGSoftwareRendererCall0>(taken[0]);
      call(this, node, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
    QSGAbstractSoftwareRenderer::nodeChanged(node, state);
  }

  //  void QSGRenderer::prepareSceneInline()
  void prepareSceneInline() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall1 call = reinterpret_cast<CuteQSGSoftwareRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareSceneInline();
  }

  //  void QSGRenderer::renderSceneInline()
  void renderSceneInline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall2 call = reinterpret_cast<CuteQSGSoftwareRendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderSceneInline();
  }

  //  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
  void setVisualizationMode(const QByteArray &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall3 call = reinterpret_cast<CuteQSGSoftwareRendererCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSGRenderer::setVisualizationMode(a0);
  }

  //  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
  bool hasVisualizationModeWithContinuousUpdate() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall4 call = reinterpret_cast<CuteQSGSoftwareRendererCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderer::hasVisualizationModeWithContinuousUpdate();
  }

  //  void QSGRenderer::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall5 call = reinterpret_cast<CuteQSGSoftwareRendererCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::releaseCachedResources();
  }

  //  void QSGRenderer::prepareInline()
  void prepareInline() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall6 call = reinterpret_cast<CuteQSGSoftwareRendererCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareInline();
  }

  //  void QSGRenderer::renderInline()
  void renderInline() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall7 call = reinterpret_cast<CuteQSGSoftwareRendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderInline();
  }

  //  void QSGRenderer::preprocess()
  void preprocess() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall8 call = reinterpret_cast<CuteQSGSoftwareRendererCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::preprocess();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall9 call = reinterpret_cast<CuteQSGSoftwareRendererCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall10 call = reinterpret_cast<CuteQSGSoftwareRendererCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall11 call = reinterpret_cast<CuteQSGSoftwareRendererCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall12 call = reinterpret_cast<CuteQSGSoftwareRendererCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall13 call = reinterpret_cast<CuteQSGSoftwareRendererCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall14 call = reinterpret_cast<CuteQSGSoftwareRendererCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareRendererCall15 call = reinterpret_cast<CuteQSGSoftwareRendererCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGSoftwareRenderer::QSGSoftwareRenderer(QSGRenderContext *context)
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderer *ritual_ZN19QSGSoftwareRendererC1EP16QSGRenderContext(
    QSGRenderContext *context) {
  return new CuteQSGSoftwareRenderer(context);
}

//  QSGSoftwareRenderer::~QSGSoftwareRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGSoftwareRendererD1Ev(QSGSoftwareRenderer *self) {
  delete self;
}

//  void QSGSoftwareRenderer::setCurrentPaintDevice(QPaintDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGSoftwareRenderer21setCurrentPaintDeviceEP12QPaintDevice(
    QSGSoftwareRenderer *self,
    QPaintDevice *device) {
  self->setCurrentPaintDevice(device);
}

//  QPaintDevice *QSGSoftwareRenderer::currentPaintDevice() const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK19QSGSoftwareRenderer18currentPaintDeviceEv(
    const QSGSoftwareRenderer *self) {
  return self->currentPaintDevice();
}

//  void QSGSoftwareRenderer::setBackingStore(QBackingStore *backingStore)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGSoftwareRenderer15setBackingStoreEP13QBackingStore(
    QSGSoftwareRenderer *self,
    QBackingStore *backingStore) {
  self->setBackingStore(backingStore);
}

//  QRegion QSGSoftwareRenderer::flushRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK19QSGSoftwareRenderer11flushRegionEv(
    const QSGSoftwareRenderer *self) {
  return new QRegion(self->flushRegion());
}

//  void QSGSoftwareRenderer::renderScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGSoftwareRenderer11renderSceneEv(
    QSGSoftwareRenderer *self) {
  self->renderScene();
}

//  void QSGSoftwareRenderer::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGSoftwareRenderer6renderEv(QSGSoftwareRenderer *self) {
  self->render();
}

//  a Python function taken by a CuteQSGSoftwareRenderer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareRenderer(
    QSGSoftwareRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareRenderer *>(self)->take(key, call);
}
