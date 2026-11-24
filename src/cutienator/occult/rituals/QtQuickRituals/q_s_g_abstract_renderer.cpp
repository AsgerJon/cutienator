//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgabstractrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGAbstractRenderer that Python can take functions over in. Every QSGAbstractRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGAbstractRendererCall0)(const void *, int *);
typedef void (*CuteQSGAbstractRendererCall1)(const void *, int *);
typedef void (*CuteQSGAbstractRendererCall2)(const void *, int *);
typedef void (*CuteQSGAbstractRendererCall3)(const void *, QSGNode *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGAbstractRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGAbstractRendererCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractRendererCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractRendererCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractRendererCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractRendererCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGAbstractRendererCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGAbstractRenderer : public QSGAbstractRenderer {
public:
  using QSGAbstractRenderer::QSGAbstractRenderer;
  void *taken[11] = {};

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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGAbstractRenderer::renderScene()
  void renderScene() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGAbstractRendererCall0 call = reinterpret_cast<CuteQSGAbstractRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGAbstractRenderer::prepareSceneInline()
  void prepareSceneInline() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGAbstractRendererCall1 call = reinterpret_cast<CuteQSGAbstractRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGAbstractRenderer::prepareSceneInline();
  }

  //  void QSGAbstractRenderer::renderSceneInline()
  void renderSceneInline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGAbstractRendererCall2 call = reinterpret_cast<CuteQSGAbstractRendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGAbstractRenderer::renderSceneInline();
  }

  //  void QSGAbstractRenderer::nodeChanged(QSGNode *node,
  //      QSGNode::DirtyState state)
  void nodeChanged(QSGNode *node, QSGNode::DirtyState state) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGAbstractRendererCall3 call = reinterpret_cast<CuteQSGAbstractRendererCall3>(taken[3]);
      call(this, node, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGAbstractRendererCall4 call = reinterpret_cast<CuteQSGAbstractRendererCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGAbstractRendererCall5 call = reinterpret_cast<CuteQSGAbstractRendererCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGAbstractRendererCall6 call = reinterpret_cast<CuteQSGAbstractRendererCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGAbstractRendererCall7 call = reinterpret_cast<CuteQSGAbstractRendererCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGAbstractRendererCall8 call = reinterpret_cast<CuteQSGAbstractRendererCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGAbstractRendererCall9 call = reinterpret_cast<CuteQSGAbstractRendererCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGAbstractRendererCall10 call = reinterpret_cast<CuteQSGAbstractRendererCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGAbstractRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QSGAbstractRenderer10metaObjectEv(
    const QSGAbstractRenderer *self) {
  return self->metaObject();
}

//  QString QSGAbstractRenderer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QSGAbstractRenderer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSGAbstractRenderer::tr(s, c, n));
}

//  QSGAbstractRenderer::~QSGAbstractRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRendererD1Ev(QSGAbstractRenderer *self) {
  delete self;
}

//  void QSGAbstractRenderer::setRootNode(QSGRootNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer11setRootNodeEP11QSGRootNode(
    QSGAbstractRenderer *self,
    QSGRootNode *node) {
  self->setRootNode(node);
}

//  QSGRootNode *QSGAbstractRenderer::rootNode() const
extern "C" Q_DECL_EXPORT
QSGRootNode *ritual_ZNK19QSGAbstractRenderer8rootNodeEv(
    const QSGAbstractRenderer *self) {
  return self->rootNode();
}

//  void QSGAbstractRenderer::setDeviceRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer13setDeviceRectERK5QRect(
    QSGAbstractRenderer *self,
    const QRect *rect) {
  self->setDeviceRect(*rect);
}

//  void QSGAbstractRenderer::setDeviceRect(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer13setDeviceRectERK5QSize(
    QSGAbstractRenderer *self,
    const QSize *size) {
  self->setDeviceRect(*size);
}

//  QRect QSGAbstractRenderer::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QSGAbstractRenderer10deviceRectEv(
    const QSGAbstractRenderer *self) {
  return new QRect(self->deviceRect());
}

//  void QSGAbstractRenderer::setViewportRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer15setViewportRectERK5QRect(
    QSGAbstractRenderer *self,
    const QRect *rect) {
  self->setViewportRect(*rect);
}

//  void QSGAbstractRenderer::setViewportRect(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer15setViewportRectERK5QSize(
    QSGAbstractRenderer *self,
    const QSize *size) {
  self->setViewportRect(*size);
}

//  QRect QSGAbstractRenderer::viewportRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QSGAbstractRenderer12viewportRectEv(
    const QSGAbstractRenderer *self) {
  return new QRect(self->viewportRect());
}

//  void QSGAbstractRenderer::setProjectionMatrixToRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer25setProjectionMatrixToRectERK6QRectF(
    QSGAbstractRenderer *self,
    const QRectF *rect) {
  self->setProjectionMatrixToRect(*rect);
}

//  void QSGAbstractRenderer::setProjectionMatrixToRect(const QRectF &rect,
//      MatrixTransformFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer25setProjectionMatrixToRectERK6QRectF6QFlagsINS_19MatrixTransformFlagEE(
    QSGAbstractRenderer *self,
    const QRectF *rect,
    int flags) {
  self->setProjectionMatrixToRect(
      *rect,
      QFlags<QSGAbstractRenderer::MatrixTransformFlag>::fromInt(flags));
}

//  void QSGAbstractRenderer::setProjectionMatrixToRect(const QRectF &rect,
//      MatrixTransformFlags flags, bool nativeNDCFlipY)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer25setProjectionMatrixToRectERK6QRectF6QFlagsINS_19MatrixTransformFlagEEb(
    QSGAbstractRenderer *self,
    const QRectF *rect,
    int flags,
    bool nativeNDCFlipY) {
  self->setProjectionMatrixToRect(
      *rect,
      QFlags<QSGAbstractRenderer::MatrixTransformFlag>::fromInt(flags),
      nativeNDCFlipY);
}

//  void QSGAbstractRenderer::setProjectionMatrix(const QMatrix4x4 &matrix,
//      int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer19setProjectionMatrixERK10QMatrix4x4i(
    QSGAbstractRenderer *self,
    const QMatrix4x4 *matrix,
    int index) {
  self->setProjectionMatrix(*matrix, index);
}

//  void QSGAbstractRenderer::setProjectionMatrixWithNativeNDC(const
//      QMatrix4x4 &matrix, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer32setProjectionMatrixWithNativeNDCERK10QMatrix4x4i(
    QSGAbstractRenderer *self,
    const QMatrix4x4 *matrix,
    int index) {
  self->setProjectionMatrixWithNativeNDC(*matrix, index);
}

//  QMatrix4x4 QSGAbstractRenderer::projectionMatrix(int index) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QSGAbstractRenderer16projectionMatrixEi(
    const QSGAbstractRenderer *self,
    int index) {
  return new QMatrix4x4(self->projectionMatrix(index));
}

//  QMatrix4x4 QSGAbstractRenderer::projectionMatrixWithNativeNDC(int index)
//      const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QSGAbstractRenderer29projectionMatrixWithNativeNDCEi(
    const QSGAbstractRenderer *self,
    int index) {
  return new QMatrix4x4(self->projectionMatrixWithNativeNDC(index));
}

//  int QSGAbstractRenderer::projectionMatrixCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSGAbstractRenderer21projectionMatrixCountEv(
    const QSGAbstractRenderer *self) {
  return self->projectionMatrixCount();
}

//  int QSGAbstractRenderer::projectionMatrixWithNativeNDCCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSGAbstractRenderer34projectionMatrixWithNativeNDCCountEv(
    const QSGAbstractRenderer *self) {
  return self->projectionMatrixWithNativeNDCCount();
}

//  void QSGAbstractRenderer::setInvertFrontFace(bool invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer18setInvertFrontFaceEb(
    QSGAbstractRenderer *self,
    bool invert) {
  self->setInvertFrontFace(invert);
}

//  bool QSGAbstractRenderer::invertFrontFace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSGAbstractRenderer15invertFrontFaceEv(
    const QSGAbstractRenderer *self) {
  return self->invertFrontFace();
}

//  void QSGAbstractRenderer::setClearColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer13setClearColorERK6QColor(
    QSGAbstractRenderer *self,
    const QColor *color) {
  self->setClearColor(*color);
}

//  QColor QSGAbstractRenderer::clearColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QSGAbstractRenderer10clearColorEv(
    const QSGAbstractRenderer *self) {
  return new QColor(self->clearColor());
}

//  void QSGAbstractRenderer::renderScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer11renderSceneEv(
    QSGAbstractRenderer *self) {
  self->renderScene();
}

//  void QSGAbstractRenderer::prepareSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer18prepareSceneInlineEv(
    QSGAbstractRenderer *self) {
  self->prepareSceneInline();
}

//  void QSGAbstractRenderer::renderSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer17renderSceneInlineEv(
    QSGAbstractRenderer *self) {
  self->renderSceneInline();
}

//  void QSGAbstractRenderer::nodeChanged(QSGNode *node, QSGNode::DirtyState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE(
    QSGAbstractRenderer *self,
    QSGNode *node,
    int state) {
  self->nodeChanged(node, QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  QSGAbstractRendererPrivate *QSGAbstractRenderer::d_func()
extern "C" Q_DECL_EXPORT
QSGAbstractRendererPrivate *ritual_ZN19QSGAbstractRenderer6d_funcEv(
    QSGAbstractRenderer *self) {
  return self->d_func();
}

//  const QSGAbstractRendererPrivate *QSGAbstractRenderer::d_func() const
extern "C" Q_DECL_EXPORT
const QSGAbstractRendererPrivate *ritual_ZNK19QSGAbstractRenderer6d_funcEv(
    const QSGAbstractRenderer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSGAbstractRenderer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGAbstractRenderer(
    QSGAbstractRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGAbstractRenderer *>(self)->take(key, call);
}

//  void QSGAbstractRenderer::prepareSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGAbstractRenderer18prepareSceneInlineEv(
    QSGAbstractRenderer *self) {
  self->QSGAbstractRenderer::prepareSceneInline();
}

//  void QSGAbstractRenderer::renderSceneInline()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGAbstractRenderer17renderSceneInlineEv(
    QSGAbstractRenderer *self) {
  self->QSGAbstractRenderer::renderSceneInline();
}
