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
#include <cstring>

//  A QSvgCircle that Python can take functions over in. Every QSvgCircle
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgCircleCall0)(const void *, int *);
typedef bool (*CuteQSvgCircleCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgCircleCall2)(const void *, int *);
class CuteQSvgCircle : public QSvgCircle {
public:
  using QSvgCircle::QSvgCircle;
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

  //  Type QSvgCircle::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgCircleCall0 call = reinterpret_cast<CuteQSvgCircleCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgCircle::type();
  }

  //  bool QSvgEllipse::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgCircleCall1 call = reinterpret_cast<CuteQSvgCircleCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgEllipse::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgCircleCall2 call = reinterpret_cast<CuteQSvgCircleCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgCircle::QSvgCircle(QSvgNode *parent, const QRectF &rect)
extern "C" Q_DECL_EXPORT
QSvgCircle *ritual_ZN10QSvgCircleC1EP8QSvgNodeRK6QRectF(
    QSvgNode *parent,
    const QRectF *rect) {
  return new CuteQSvgCircle(parent, *rect);
}

//  QSvgCircle::~QSvgCircle()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSvgCircleD1Ev(QSvgCircle *self) {
  delete self;
}

//  Type QSvgCircle::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK10QSvgCircle4typeEv(const QSvgCircle *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgCircle, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgCircle(QSvgCircle *self, const char *key, void *call) {
  return static_cast<CuteQSvgCircle *>(self)->take(key, call);
}

//  Type QSvgCircle::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK10QSvgCircle4typeEv(const QSvgCircle *self) {
  return self->QSvgCircle::type();
}
