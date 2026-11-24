//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickAbstractPathRenderer that Python can take functions over in. Every QQuickAbstractPathRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAbstractPathRendererCall0)(const void *, bool, int *);
typedef int (*CuteQQuickAbstractPathRendererCall1)(const void *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall2)(const void *, int, const QQuickPath *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall3)(const void *, int, const QPainterPath *, int, int *);
typedef void (*CuteQQuickAbstractPathRendererCall4)(const void *, int, const QColor *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall5)(const void *, int, qreal, int *);
typedef void (*CuteQQuickAbstractPathRendererCall6)(const void *, int, bool, int *);
typedef void (*CuteQQuickAbstractPathRendererCall7)(const void *, int, int, int, int *);
typedef void (*CuteQQuickAbstractPathRendererCall8)(const void *, int, int, int *);
typedef void (*CuteQQuickAbstractPathRendererCall9)(const void *, int, const QColor *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall10)(const void *, int, int, int *);
typedef void (*CuteQQuickAbstractPathRendererCall11)(const void *, int, QQuickShapeGradient *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall12)(const void *, int, QQuickShapeGradient *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall13)(const void *, int, QQuickItem *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall14)(const void *, int, const QSGTransform *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall15)(const void *, int, qreal, int *);
typedef void (*CuteQQuickAbstractPathRendererCall16)(const void *, QQuickWindow *, int *);
typedef void (*CuteQQuickAbstractPathRendererCall17)(const void *, int *);
class CuteQQuickAbstractPathRenderer : public QQuickAbstractPathRenderer {
public:
  using QQuickAbstractPathRenderer::QQuickAbstractPathRenderer;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7endSyncEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QQuickAbstractPathRenderer5flagsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer14setStrokeColorEiRK6QColor")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer14setStrokeWidthEid")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17setCosmeticStrokeEib")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer12setFillColorEiRK6QColor")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer15setFillGradientEiP19QQuickShapeGradient")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17setStrokeGradientEiP19QQuickShapeGradient")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer22setFillTextureProviderEiP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer16setFillTransformEiRK12QSGTransform")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17handleSceneChangeEP12QQuickWindow")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer10updateNodeEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickAbstractPathRenderer::endSync(bool async)
  void endSync(bool async) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall0 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall0>(taken[0]);
      call(this, async, &handled);
      if (handled) return;
    }
  }

  //  Flags QQuickAbstractPathRenderer::flags() const
  QQuickAbstractPathRenderer::Flags flags() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall1 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQuickAbstractPathRenderer::Flag>::fromInt(given);
    }
    return QQuickAbstractPathRenderer::flags();
  }

  //  void QQuickAbstractPathRenderer::setPath(int index, const QQuickPath
  //      *path)
  void setPath(int index, const QQuickPath *path) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall2 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall2>(taken[2]);
      call(this, index, path, &handled);
      if (handled) return;
    }
    QQuickAbstractPathRenderer::setPath(index, path);
  }

  //  void QQuickAbstractPathRenderer::setPath(int index, const
  //      QPainterPath &path, QQuickShapePath::PathHints pathHints)
  void setPath(
      int index,
      const QPainterPath &path,
      QQuickShapePath::PathHints pathHints) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall3 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall3>(taken[3]);
      call(this, index, &path, static_cast<int>(pathHints.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setStrokeColor(int index, const
  //      QColor &color)
  void setStrokeColor(int index, const QColor &color) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall4 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall4>(taken[4]);
      call(this, index, &color, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setStrokeWidth(int index, qreal w)
  void setStrokeWidth(int index, qreal w) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall5 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall5>(taken[5]);
      call(this, index, w, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setCosmeticStroke(int index, bool c)
  void setCosmeticStroke(int index, bool c) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall6 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall6>(taken[6]);
      call(this, index, c, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setJoinStyle(int index,
  //      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
  void setJoinStyle(
      int index,
      QQuickShapePath::JoinStyle joinStyle,
      int miterLimit) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall7 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall7>(taken[7]);
      call(this, index, static_cast<int>(joinStyle), miterLimit, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setCapStyle(int index,
  //      QQuickShapePath::CapStyle capStyle)
  void setCapStyle(int index, QQuickShapePath::CapStyle capStyle) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall8 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall8>(taken[8]);
      call(this, index, static_cast<int>(capStyle), &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setFillColor(int index, const QColor
  //      &color)
  void setFillColor(int index, const QColor &color) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall9 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall9>(taken[9]);
      call(this, index, &color, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setFillRule(int index,
  //      QQuickShapePath::FillRule fillRule)
  void setFillRule(int index, QQuickShapePath::FillRule fillRule) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall10 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall10>(taken[10]);
      call(this, index, static_cast<int>(fillRule), &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setFillGradient(int index,
  //      QQuickShapeGradient *gradient)
  void setFillGradient(int index, QQuickShapeGradient *gradient) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall11 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall11>(taken[11]);
      call(this, index, gradient, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setStrokeGradient(int index,
  //      QQuickShapeGradient *gradient)
  void setStrokeGradient(int index, QQuickShapeGradient *gradient) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall12 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall12>(taken[12]);
      call(this, index, gradient, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setFillTextureProvider(int index,
  //      QQuickItem *textureProviderItem)
  void setFillTextureProvider(
      int index,
      QQuickItem *textureProviderItem) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall13 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall13>(taken[13]);
      call(this, index, textureProviderItem, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setFillTransform(int index, const
  //      QSGTransform &transform)
  void setFillTransform(int index, const QSGTransform &transform) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall14 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall14>(taken[14]);
      call(this, index, &transform, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::setTriangulationScale(int a0, qreal
  //      a1)
  void setTriangulationScale(int a0, qreal a1) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall15 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall15>(taken[15]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickAbstractPathRenderer::setTriangulationScale(a0, a1);
  }

  //  void QQuickAbstractPathRenderer::handleSceneChange(QQuickWindow
  //      *window)
  void handleSceneChange(QQuickWindow *window) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall16 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall16>(taken[16]);
      call(this, window, &handled);
      if (handled) return;
    }
  }

  //  void QQuickAbstractPathRenderer::updateNode()
  void updateNode() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickAbstractPathRendererCall17 call = reinterpret_cast<CuteQQuickAbstractPathRendererCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QQuickAbstractPathRenderer::~QQuickAbstractPathRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRendererD1Ev(
    QQuickAbstractPathRenderer *self) {
  delete self;
}

//  void QQuickAbstractPathRenderer::beginSync(int totalCount, bool
//      *countChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer9beginSyncEiPb(
    QQuickAbstractPathRenderer *self,
    int totalCount,
    bool *countChanged) {
  self->beginSync(totalCount, countChanged);
}

//  void QQuickAbstractPathRenderer::endSync(bool async)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer7endSyncEb(
    QQuickAbstractPathRenderer *self,
    bool async) {
  self->endSync(async);
}

//  Flags QQuickAbstractPathRenderer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuickAbstractPathRenderer5flagsEv(
    const QQuickAbstractPathRenderer *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QQuickAbstractPathRenderer::setPath(int index, const QQuickPath
//      *path)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath(
    QQuickAbstractPathRenderer *self,
    int index,
    const QQuickPath *path) {
  self->setPath(index, path);
}

//  void QQuickAbstractPathRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickAbstractPathRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickAbstractPathRenderer::setStrokeColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer14setStrokeColorEiRK6QColor(
    QQuickAbstractPathRenderer *self,
    int index,
    const QColor *color) {
  self->setStrokeColor(index, *color);
}

//  void QQuickAbstractPathRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer14setStrokeWidthEid(
    QQuickAbstractPathRenderer *self,
    int index,
    qreal w) {
  self->setStrokeWidth(index, w);
}

//  void QQuickAbstractPathRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer17setCosmeticStrokeEib(
    QQuickAbstractPathRenderer *self,
    int index,
    bool c) {
  self->setCosmeticStroke(index, c);
}

//  void QQuickAbstractPathRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickAbstractPathRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->setJoinStyle(index, joinStyle, miterLimit);
}

//  void QQuickAbstractPathRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickAbstractPathRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->setCapStyle(index, capStyle);
}

//  void QQuickAbstractPathRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer12setFillColorEiRK6QColor(
    QQuickAbstractPathRenderer *self,
    int index,
    const QColor *color) {
  self->setFillColor(index, *color);
}

//  void QQuickAbstractPathRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickAbstractPathRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(index, fillRule);
}

//  void QQuickAbstractPathRenderer::setFillGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer15setFillGradientEiP19QQuickShapeGradient(
    QQuickAbstractPathRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->setFillGradient(index, gradient);
}

//  void QQuickAbstractPathRenderer::setStrokeGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer17setStrokeGradientEiP19QQuickShapeGradient(
    QQuickAbstractPathRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->setStrokeGradient(index, gradient);
}

//  void QQuickAbstractPathRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickAbstractPathRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->setFillTextureProvider(index, textureProviderItem);
}

//  void QQuickAbstractPathRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer16setFillTransformEiRK12QSGTransform(
    QQuickAbstractPathRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->setFillTransform(index, *transform);
}

//  void QQuickAbstractPathRenderer::setTriangulationScale(int a0, qreal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid(
    QQuickAbstractPathRenderer *self,
    int a0,
    qreal a1) {
  self->setTriangulationScale(a0, a1);
}

//  void QQuickAbstractPathRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickAbstractPathRenderer *self,
    QQuickWindow *window) {
  self->handleSceneChange(window);
}

//  void QQuickAbstractPathRenderer::updateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickAbstractPathRenderer10updateNodeEv(
    QQuickAbstractPathRenderer *self) {
  self->updateNode();
}

//  a Python function taken by a CuteQQuickAbstractPathRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAbstractPathRenderer(
    QQuickAbstractPathRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAbstractPathRenderer *>(self)->take(key, call);
}

//  Flags QQuickAbstractPathRenderer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QQuickAbstractPathRenderer5flagsEv(
    const QQuickAbstractPathRenderer *self) {
  return static_cast<int>(self->QQuickAbstractPathRenderer::flags().toInt());
}

//  void QQuickAbstractPathRenderer::setPath(int index, const QQuickPath
//      *path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath(
    QQuickAbstractPathRenderer *self,
    int index,
    const QQuickPath *path) {
  self->QQuickAbstractPathRenderer::setPath(index, path);
}

//  void QQuickAbstractPathRenderer::setTriangulationScale(int a0, qreal a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid(
    QQuickAbstractPathRenderer *self,
    int a0,
    qreal a1) {
  self->QQuickAbstractPathRenderer::setTriangulationScale(a0, a1);
}
