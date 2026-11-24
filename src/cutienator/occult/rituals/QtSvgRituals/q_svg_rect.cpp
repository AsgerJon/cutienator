//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A QSvgRect that Python can take functions over in. Every QSvgRect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgRectCall0)(const void *, int *);
typedef bool (*CuteQSvgRectCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgRectCall2)(const void *, int *);
class CuteQSvgRect : public QSvgRect {
public:
  using QSvgRect::QSvgRect;
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

  //  Type QSvgRect::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgRectCall0 call = reinterpret_cast<CuteQSvgRectCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgRect::type();
  }

  //  bool QSvgRect::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgRectCall1 call = reinterpret_cast<CuteQSvgRectCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgRect::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgRectCall2 call = reinterpret_cast<CuteQSvgRectCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgRect::QSvgRect(QSvgNode *paren, const QRectF &rect, qreal rx, qreal
//      ry)
extern "C" Q_DECL_EXPORT
QSvgRect *ritual_ZN8QSvgRectC1EP8QSvgNodeRK6QRectFdd(
    QSvgNode *paren,
    const QRectF *rect,
    qreal rx,
    qreal ry) {
  return new CuteQSvgRect(paren, *rect, rx, ry);
}

//  QSvgRect::~QSvgRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgRectD1Ev(QSvgRect *self) {
  delete self;
}

//  Type QSvgRect::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgRect4typeEv(const QSvgRect *self) {
  return self->type();
}

//  bool QSvgRect::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgRect18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgRect *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  QRectF QSvgRect::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QSvgRect4rectEv(const QSvgRect *self) {
  return new QRectF(self->rect());
}

//  QPointF QSvgRect::radius() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8QSvgRect6radiusEv(const QSvgRect *self) {
  return new QPointF(self->radius());
}

//  a Python function taken by a CuteQSvgRect, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgRect(QSvgRect *self, const char *key, void *call) {
  return static_cast<CuteQSvgRect *>(self)->take(key, call);
}

//  Type QSvgRect::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgRect4typeEv(const QSvgRect *self) {
  return self->QSvgRect::type();
}

//  bool QSvgRect::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgRect18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgRect *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgRect::separateFillStroke(a0, *a1);
}
