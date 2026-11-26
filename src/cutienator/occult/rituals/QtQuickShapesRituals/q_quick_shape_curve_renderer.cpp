//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapecurverenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapecurverenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquadpath_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qsgcurveabstractnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickShapeCurveRenderer that Python can take functions over in. Every QQuickShapeCurveRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickShapeCurveRendererCall0)(const void *, int, const QPainterPath *, int, int *);
typedef void (*CuteQQuickShapeCurveRendererCall1)(const void *, int, const QColor *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall2)(const void *, int, qreal, int *);
typedef void (*CuteQQuickShapeCurveRendererCall3)(const void *, int, bool, int *);
typedef void (*CuteQQuickShapeCurveRendererCall4)(const void *, int, const QColor *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall5)(const void *, int, int, int *);
typedef void (*CuteQQuickShapeCurveRendererCall6)(const void *, int, int, int, int *);
typedef void (*CuteQQuickShapeCurveRendererCall7)(const void *, int, int, int *);
typedef void (*CuteQQuickShapeCurveRendererCall8)(const void *, int, QQuickShapeGradient *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall9)(const void *, int, QQuickShapeGradient *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall10)(const void *, int, QQuickItem *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall11)(const void *, int, const QSGTransform *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall12)(const void *, bool, int *);
typedef int (*CuteQQuickShapeCurveRendererCall13)(const void *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall14)(const void *, QQuickWindow *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall15)(const void *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall16)(const void *, int, const QQuickPath *, int *);
typedef void (*CuteQQuickShapeCurveRendererCall17)(const void *, int, qreal, int *);
class CuteQQuickShapeCurveRenderer : public QQuickShapeCurveRenderer {
public:
  using QQuickShapeCurveRenderer::QQuickShapeCurveRenderer;
  CuteQQuickShapeCurveRenderer(const QQuickShapeCurveRenderer & other) : QQuickShapeCurveRenderer(other) {}
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer14setStrokeColorEiRK6QColor")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer14setStrokeWidthEid")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17setCosmeticStrokeEib")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer12setFillColorEiRK6QColor")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer15setFillGradientEiP19QQuickShapeGradient")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17setStrokeGradientEiP19QQuickShapeGradient")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer22setFillTextureProviderEiP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer16setFillTransformEiRK12QSGTransform")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7endSyncEb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QQuickAbstractPathRenderer5flagsEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17handleSceneChangeEP12QQuickWindow")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer10updateNodeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickShapeCurveRenderer::setPath(int index, const QPainterPath
  //      &path, QQuickShapePath::PathHints pathHints)
  void setPath(
      int index,
      const QPainterPath &path,
      QQuickShapePath::PathHints pathHints) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall0 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall0>(taken[0]);
      call(this, index, &path, static_cast<int>(pathHints.toInt()), &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setPath(index, path, pathHints);
  }

  //  void QQuickShapeCurveRenderer::setStrokeColor(int index, const QColor
  //      &color)
  void setStrokeColor(int index, const QColor &color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall1 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall1>(taken[1]);
      call(this, index, &color, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setStrokeColor(index, color);
  }

  //  void QQuickShapeCurveRenderer::setStrokeWidth(int index, qreal w)
  void setStrokeWidth(int index, qreal w) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall2 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall2>(taken[2]);
      call(this, index, w, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setStrokeWidth(index, w);
  }

  //  void QQuickShapeCurveRenderer::setCosmeticStroke(int index, bool c)
  void setCosmeticStroke(int index, bool c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall3 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall3>(taken[3]);
      call(this, index, c, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setCosmeticStroke(index, c);
  }

  //  void QQuickShapeCurveRenderer::setFillColor(int index, const QColor
  //      &color)
  void setFillColor(int index, const QColor &color) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall4 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall4>(taken[4]);
      call(this, index, &color, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setFillColor(index, color);
  }

  //  void QQuickShapeCurveRenderer::setFillRule(int index,
  //      QQuickShapePath::FillRule fillRule)
  void setFillRule(int index, QQuickShapePath::FillRule fillRule) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall5 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall5>(taken[5]);
      call(this, index, static_cast<int>(fillRule), &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setFillRule(index, fillRule);
  }

  //  void QQuickShapeCurveRenderer::setJoinStyle(int index,
  //      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
  void setJoinStyle(
      int index,
      QQuickShapePath::JoinStyle joinStyle,
      int miterLimit) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall6 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall6>(taken[6]);
      call(this, index, static_cast<int>(joinStyle), miterLimit, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setJoinStyle(index, joinStyle, miterLimit);
  }

  //  void QQuickShapeCurveRenderer::setCapStyle(int index,
  //      QQuickShapePath::CapStyle capStyle)
  void setCapStyle(int index, QQuickShapePath::CapStyle capStyle) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall7 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall7>(taken[7]);
      call(this, index, static_cast<int>(capStyle), &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setCapStyle(index, capStyle);
  }

  //  void QQuickShapeCurveRenderer::setFillGradient(int index,
  //      QQuickShapeGradient *gradient)
  void setFillGradient(int index, QQuickShapeGradient *gradient) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall8 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall8>(taken[8]);
      call(this, index, gradient, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setFillGradient(index, gradient);
  }

  //  void QQuickShapeCurveRenderer::setStrokeGradient(int index,
  //      QQuickShapeGradient *gradient)
  void setStrokeGradient(int index, QQuickShapeGradient *gradient) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall9 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall9>(taken[9]);
      call(this, index, gradient, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setStrokeGradient(index, gradient);
  }

  //  void QQuickShapeCurveRenderer::setFillTextureProvider(int index,
  //      QQuickItem *textureProviderItem)
  void setFillTextureProvider(
      int index,
      QQuickItem *textureProviderItem) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall10 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall10>(taken[10]);
      call(this, index, textureProviderItem, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setFillTextureProvider(index, textureProviderItem);
  }

  //  void QQuickShapeCurveRenderer::setFillTransform(int index, const
  //      QSGTransform &transform)
  void setFillTransform(int index, const QSGTransform &transform) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall11 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall11>(taken[11]);
      call(this, index, &transform, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::setFillTransform(index, transform);
  }

  //  void QQuickShapeCurveRenderer::endSync(bool async)
  void endSync(bool async) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall12 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall12>(taken[12]);
      call(this, async, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::endSync(async);
  }

  //  Flags QQuickShapeCurveRenderer::flags() const
  QQuickAbstractPathRenderer::Flags flags() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall13 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQuickAbstractPathRenderer::Flag>::fromInt(given);
    }
    return QQuickShapeCurveRenderer::flags();
  }

  //  void QQuickShapeCurveRenderer::handleSceneChange(QQuickWindow
  //      *window)
  void handleSceneChange(QQuickWindow *window) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall14 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall14>(taken[14]);
      call(this, window, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::handleSceneChange(window);
  }

  //  void QQuickShapeCurveRenderer::updateNode()
  void updateNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall15 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRenderer::updateNode();
  }

  //  void QQuickAbstractPathRenderer::setPath(int index, const QQuickPath
  //      *path)
  void setPath(int index, const QQuickPath *path) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall16 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall16>(taken[16]);
      call(this, index, path, &handled);
      if (handled) return;
    }
    QQuickAbstractPathRenderer::setPath(index, path);
  }

  //  void QQuickAbstractPathRenderer::setTriangulationScale(int a0, qreal
  //      a1)
  void setTriangulationScale(int a0, qreal a1) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShapeCurveRendererCall17 call = reinterpret_cast<CuteQQuickShapeCurveRendererCall17>(taken[17]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickAbstractPathRenderer::setTriangulationScale(a0, a1);
  }
};

//  QQuickShapeCurveRenderer::QQuickShapeCurveRenderer(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickShapeCurveRenderer *ritual_ZN24QQuickShapeCurveRendererC1EP10QQuickItem(
    QQuickItem *item) {
  return new CuteQQuickShapeCurveRenderer(item);
}

//  QQuickShapeCurveRenderer::~QQuickShapeCurveRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRendererD1Ev(
    QQuickShapeCurveRenderer *self) {
  delete self;
}

//  void QQuickShapeCurveRenderer::beginSync(int totalCount, bool
//      *countChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer9beginSyncEiPb(
    QQuickShapeCurveRenderer *self,
    int totalCount,
    bool *countChanged) {
  self->beginSync(totalCount, countChanged);
}

//  void QQuickShapeCurveRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickShapeCurveRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickShapeCurveRenderer::setStrokeColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer14setStrokeColorEiRK6QColor(
    QQuickShapeCurveRenderer *self,
    int index,
    const QColor *color) {
  self->setStrokeColor(index, *color);
}

//  void QQuickShapeCurveRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer14setStrokeWidthEid(
    QQuickShapeCurveRenderer *self,
    int index,
    qreal w) {
  self->setStrokeWidth(index, w);
}

//  void QQuickShapeCurveRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer17setCosmeticStrokeEib(
    QQuickShapeCurveRenderer *self,
    int index,
    bool c) {
  self->setCosmeticStroke(index, c);
}

//  void QQuickShapeCurveRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer12setFillColorEiRK6QColor(
    QQuickShapeCurveRenderer *self,
    int index,
    const QColor *color) {
  self->setFillColor(index, *color);
}

//  void QQuickShapeCurveRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(index, fillRule);
}

//  void QQuickShapeCurveRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->setJoinStyle(index, joinStyle, miterLimit);
}

//  void QQuickShapeCurveRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->setCapStyle(index, capStyle);
}

//  void QQuickShapeCurveRenderer::setStrokeStyle(int index,
//      QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
//      QList<qreal> &dashPattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer14setStrokeStyleEiN15QQuickShapePath11StrokeStyleEdRK5QListIdE(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::StrokeStyle strokeStyle,
    qreal dashOffset,
    const QList<qreal> *dashPattern) {
  self->setStrokeStyle(index, strokeStyle, dashOffset, *dashPattern);
}

//  void QQuickShapeCurveRenderer::setFillGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer15setFillGradientEiP19QQuickShapeGradient(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->setFillGradient(index, gradient);
}

//  void QQuickShapeCurveRenderer::setStrokeGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer17setStrokeGradientEiP19QQuickShapeGradient(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->setStrokeGradient(index, gradient);
}

//  void QQuickShapeCurveRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->setFillTextureProvider(index, textureProviderItem);
}

//  void QQuickShapeCurveRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer16setFillTransformEiRK12QSGTransform(
    QQuickShapeCurveRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->setFillTransform(index, *transform);
}

//  void QQuickShapeCurveRenderer::endSync(bool async)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer7endSyncEb(
    QQuickShapeCurveRenderer *self,
    bool async) {
  self->endSync(async);
}

//  void QQuickShapeCurveRenderer::setAsyncCallback(void (*)(void *) a0, void
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer16setAsyncCallbackEPFvPvES0_(
    QQuickShapeCurveRenderer *self,
    void *a0,
    void *a1) {
  self->setAsyncCallback(reinterpret_cast<void (*)(void *)>(a0), a1);
}

//  Flags QQuickShapeCurveRenderer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickShapeCurveRenderer5flagsEv(
    const QQuickShapeCurveRenderer *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QQuickShapeCurveRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickShapeCurveRenderer *self,
    QQuickWindow *window) {
  self->handleSceneChange(window);
}

//  void QQuickShapeCurveRenderer::updateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer10updateNodeEv(
    QQuickShapeCurveRenderer *self) {
  self->updateNode();
}

//  void QQuickShapeCurveRenderer::setRootNode(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer11setRootNodeEP7QSGNode(
    QQuickShapeCurveRenderer *self,
    QSGNode *node) {
  self->setRootNode(node);
}

//  void QQuickShapeCurveRenderer::clearNodeReferences()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer19clearNodeReferencesEv(
    QQuickShapeCurveRenderer *self) {
  self->clearNodeReferences();
}

//  int QQuickShapeCurveRenderer::debugVisualization()
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickShapeCurveRenderer18debugVisualizationEv() {
  return QQuickShapeCurveRenderer::debugVisualization();
}

//  void QQuickShapeCurveRenderer::setDebugVisualization(int options)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer21setDebugVisualizationEi(
    int options) {
  QQuickShapeCurveRenderer::setDebugVisualization(options);
}

//  void QQuickShapeCurveRenderer::setUpRunner(PathData *pathData)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer11setUpRunnerEPNS_8PathDataE(
    QQuickShapeCurveRenderer *self,
    QQuickShapeCurveRenderer::PathData *pathData) {
  self->setUpRunner(pathData);
}

//  void QQuickShapeCurveRenderer::maybeUpdateAsyncItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer20maybeUpdateAsyncItemEv(
    QQuickShapeCurveRenderer *self) {
  self->maybeUpdateAsyncItem();
}

//  void QQuickShapeCurveRenderer::processPath(PathData *pathData)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRenderer11processPathEPNS_8PathDataE(
    QQuickShapeCurveRenderer::PathData *pathData) {
  QQuickShapeCurveRenderer::processPath(pathData);
}

//  NodeList QQuickShapeCurveRenderer::addFillNodes(const QQuadPath &path)
extern "C" Q_DECL_EXPORT
QList<QSGCurveAbstractNode *> *ritual_ZN24QQuickShapeCurveRenderer12addFillNodesERK9QQuadPath(
    const QQuadPath *path) {
  return new QList<QSGCurveAbstractNode *>(
      QQuickShapeCurveRenderer::addFillNodes(
          *path));
}

//  NodeList QQuickShapeCurveRenderer::addTriangulatingStrokerNodes(const
//      QQuadPath &path, const QPen &pen)
extern "C" Q_DECL_EXPORT
QList<QSGCurveAbstractNode *> *ritual_ZN24QQuickShapeCurveRenderer28addTriangulatingStrokerNodesERK9QQuadPathRK4QPen(
    const QQuadPath *path,
    const QPen *pen) {
  return new QList<QSGCurveAbstractNode *>(
      QQuickShapeCurveRenderer::addTriangulatingStrokerNodes(
          *path,
          *pen));
}

//  NodeList QQuickShapeCurveRenderer::addCurveStrokeNodes(const QQuadPath
//      &path, const QPen &pen)
extern "C" Q_DECL_EXPORT
QList<QSGCurveAbstractNode *> *ritual_ZN24QQuickShapeCurveRenderer19addCurveStrokeNodesERK9QQuadPathRK4QPen(
    const QQuadPath *path,
    const QPen *pen) {
  return new QList<QSGCurveAbstractNode *>(
      QQuickShapeCurveRenderer::addCurveStrokeNodes(
          *path,
          *pen));
}

//  a Python function taken by a CuteQQuickShapeCurveRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeCurveRenderer(
    QQuickShapeCurveRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeCurveRenderer *>(self)->take(key, call);
}

//  void QQuickShapeCurveRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickShapeCurveRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->QQuickShapeCurveRenderer::setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickShapeCurveRenderer::setStrokeColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer14setStrokeColorEiRK6QColor(
    QQuickShapeCurveRenderer *self,
    int index,
    const QColor *color) {
  self->QQuickShapeCurveRenderer::setStrokeColor(index, *color);
}

//  void QQuickShapeCurveRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer14setStrokeWidthEid(
    QQuickShapeCurveRenderer *self,
    int index,
    qreal w) {
  self->QQuickShapeCurveRenderer::setStrokeWidth(index, w);
}

//  void QQuickShapeCurveRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer17setCosmeticStrokeEib(
    QQuickShapeCurveRenderer *self,
    int index,
    bool c) {
  self->QQuickShapeCurveRenderer::setCosmeticStroke(index, c);
}

//  void QQuickShapeCurveRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer12setFillColorEiRK6QColor(
    QQuickShapeCurveRenderer *self,
    int index,
    const QColor *color) {
  self->QQuickShapeCurveRenderer::setFillColor(index, *color);
}

//  void QQuickShapeCurveRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->QQuickShapeCurveRenderer::setFillRule(index, fillRule);
}

//  void QQuickShapeCurveRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->QQuickShapeCurveRenderer::setJoinStyle(index, joinStyle, miterLimit);
}

//  void QQuickShapeCurveRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->QQuickShapeCurveRenderer::setCapStyle(index, capStyle);
}

//  void QQuickShapeCurveRenderer::setFillGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer15setFillGradientEiP19QQuickShapeGradient(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->QQuickShapeCurveRenderer::setFillGradient(index, gradient);
}

//  void QQuickShapeCurveRenderer::setStrokeGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer17setStrokeGradientEiP19QQuickShapeGradient(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->QQuickShapeCurveRenderer::setStrokeGradient(index, gradient);
}

//  void QQuickShapeCurveRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickShapeCurveRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->QQuickShapeCurveRenderer::setFillTextureProvider(
      index,
      textureProviderItem);
}

//  void QQuickShapeCurveRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer16setFillTransformEiRK12QSGTransform(
    QQuickShapeCurveRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->QQuickShapeCurveRenderer::setFillTransform(index, *transform);
}

//  void QQuickShapeCurveRenderer::endSync(bool async)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer7endSyncEb(
    QQuickShapeCurveRenderer *self,
    bool async) {
  self->QQuickShapeCurveRenderer::endSync(async);
}

//  Flags QQuickShapeCurveRenderer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QQuickShapeCurveRenderer5flagsEv(
    const QQuickShapeCurveRenderer *self) {
  return static_cast<int>(self->QQuickShapeCurveRenderer::flags().toInt());
}

//  void QQuickShapeCurveRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickShapeCurveRenderer *self,
    QQuickWindow *window) {
  self->QQuickShapeCurveRenderer::handleSceneChange(window);
}

//  void QQuickShapeCurveRenderer::updateNode()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickShapeCurveRenderer10updateNodeEv(
    QQuickShapeCurveRenderer *self) {
  self->QQuickShapeCurveRenderer::updateNode();
}
