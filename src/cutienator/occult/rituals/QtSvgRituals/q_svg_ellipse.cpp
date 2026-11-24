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

//  A QSvgEllipse that Python can take functions over in. Every QSvgEllipse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgEllipseCall0)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgEllipseCall1)(const void *, int *);
typedef bool (*CuteQSvgEllipseCall2)(const void *, int *);
class CuteQSvgEllipse : public QSvgEllipse {
public:
  using QSvgEllipse::QSvgEllipse;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QSvgEllipse::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgEllipseCall0 call = reinterpret_cast<CuteQSvgEllipseCall0>(taken[0]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgEllipse::separateFillStroke(a0, a1);
  }

  //  Type QSvgEllipse::type() const
  QSvgNode::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgEllipseCall1 call = reinterpret_cast<CuteQSvgEllipseCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgEllipse::type();
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgEllipseCall2 call = reinterpret_cast<CuteQSvgEllipseCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgEllipse::QSvgEllipse(QSvgNode *parent, const QRectF &rect)
extern "C" Q_DECL_EXPORT
QSvgEllipse *ritual_ZN11QSvgEllipseC1EP8QSvgNodeRK6QRectF(
    QSvgNode *parent,
    const QRectF *rect) {
  return new CuteQSvgEllipse(parent, *rect);
}

//  QSvgEllipse::~QSvgEllipse()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgEllipseD1Ev(QSvgEllipse *self) {
  delete self;
}

//  bool QSvgEllipse::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgEllipse18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgEllipse *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  Type QSvgEllipse::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK11QSvgEllipse4typeEv(const QSvgEllipse *self) {
  return self->type();
}

//  QRectF QSvgEllipse::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QSvgEllipse4rectEv(const QSvgEllipse *self) {
  return new QRectF(self->rect());
}

//  a Python function taken by a CuteQSvgEllipse, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgEllipse(
    QSvgEllipse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgEllipse *>(self)->take(key, call);
}

//  bool QSvgEllipse::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSvgEllipse18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgEllipse *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgEllipse::separateFillStroke(a0, *a1);
}

//  Type QSvgEllipse::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK11QSvgEllipse4typeEv(const QSvgEllipse *self) {
  return self->QSvgEllipse::type();
}
