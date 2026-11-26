//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtGui/QImage>
#include <QtCore/QSize>
#include <utility>

//  A QSvgPattern that Python can take functions over in. Every QSvgPattern
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgPatternCall0)(const void *, int *);
typedef bool (*CuteQSvgPatternCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgPatternCall2)(const void *, int *);
class CuteQSvgPattern : public QSvgPattern {
public:
  using QSvgPattern::QSvgPattern;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgPattern::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgPatternCall0 call = reinterpret_cast<CuteQSvgPatternCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgPattern::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgPatternCall1 call = reinterpret_cast<CuteQSvgPatternCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgPatternCall2 call = reinterpret_cast<CuteQSvgPatternCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgPattern::QSvgPattern(QSvgNode *parent, QSvgRectF bounds, QRectF
//      viewBox, QtSvg::UnitTypes contentUnits, QTransform transform)
extern "C" Q_DECL_EXPORT
QSvgPattern *ritual_ZN11QSvgPatternC1EP8QSvgNode9QSvgRectF6QRectFN5QtSvg9UnitTypesE10QTransform(
    QSvgNode *parent,
    const QSvgRectF *bounds,
    const QRectF *viewBox,
    QtSvg::UnitTypes contentUnits,
    const QTransform *transform) {
  return new CuteQSvgPattern(
      parent,
      *bounds,
      *viewBox,
      contentUnits,
      *transform);
}

//  QSvgPattern::~QSvgPattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgPatternD1Ev(QSvgPattern *self) {
  delete self;
}

//  void QSvgPattern::drawCommand(QPainter *a0, QSvgExtraStates &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgPattern11drawCommandEP8QPainterR15QSvgExtraStates(
    QSvgPattern *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  self->drawCommand(a0, *a1);
}

//  bool QSvgPattern::shouldDrawNode(QPainter *a0, QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgPattern14shouldDrawNodeEP8QPainterR15QSvgExtraStates(
    const QSvgPattern *self,
    QPainter *a0,
    QSvgExtraStates *a1) {
  return self->shouldDrawNode(a0, *a1);
}

//  QImage QSvgPattern::patternImage(QPainter *p, QSvgExtraStates &states,
//      const QSvgNode *patternElement)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QSvgPattern12patternImageEP8QPainterR15QSvgExtraStatesPK8QSvgNode(
    QSvgPattern *self,
    QPainter *p,
    QSvgExtraStates *states,
    const QSvgNode *patternElement) {
  return new QImage(self->patternImage(p, *states, patternElement));
}

//  Type QSvgPattern::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK11QSvgPattern4typeEv(const QSvgPattern *self) {
  return self->type();
}

//  const QTransform &QSvgPattern::appliedTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK11QSvgPattern16appliedTransformEv(
    const QSvgPattern *self) {
  return new QTransform(self->appliedTransform());
}

//  const QTransform &QSvgPattern::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK11QSvgPattern9transformEv(const QSvgPattern *self) {
  return new QTransform(self->transform());
}

//  const QSvgRectF &QSvgPattern::rect() const
extern "C" Q_DECL_EXPORT
QSvgRectF *ritual_ZNK11QSvgPattern4rectEv(const QSvgPattern *self) {
  return new QSvgRectF(self->rect());
}

//  const QRectF &QSvgPattern::viewBox() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QSvgPattern7viewBoxEv(const QSvgPattern *self) {
  return new QRectF(self->viewBox());
}

//  QtSvg::UnitTypes QSvgPattern::contentUnits() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK11QSvgPattern12contentUnitsEv(
    const QSvgPattern *self) {
  return self->contentUnits();
}

//  QImage QSvgPattern::renderPattern(QSize size, std::pair<qreal, qreal>
//      contentScale, const QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN11QSvgPattern13renderPatternE5QSizeSt4pairIddERK15QSvgExtraStates(
    QSvgPattern *self,
    const QSize *size,
    const std::pair<qreal, qreal> *contentScale,
    const QSvgExtraStates *states) {
  return new QImage(self->renderPattern(*size, *contentScale, *states));
}

//  void QSvgPattern::calculateAppliedTransform(QTransform &worldTransform,
//      QRectF peLocalBB, QSize imageSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgPattern25calculateAppliedTransformER10QTransform6QRectF5QSize(
    QSvgPattern *self,
    QTransform *worldTransform,
    const QRectF *peLocalBB,
    const QSize *imageSize) {
  self->calculateAppliedTransform(*worldTransform, *peLocalBB, *imageSize);
}

//  a Python function taken by a CuteQSvgPattern, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgPattern(
    QSvgPattern *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgPattern *>(self)->take(key, call);
}

//  Type QSvgPattern::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK11QSvgPattern4typeEv(const QSvgPattern *self) {
  return self->QSvgPattern::type();
}
