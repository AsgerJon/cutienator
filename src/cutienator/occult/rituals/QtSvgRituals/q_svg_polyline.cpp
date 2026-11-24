//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpolygon.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgPolyline that Python can take functions over in. Every QSvgPolyline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgPolylineCall0)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgPolylineCall1)(const void *, int *);
typedef bool (*CuteQSvgPolylineCall2)(const void *, int *);
class CuteQSvgPolyline : public QSvgPolyline {
public:
  using QSvgPolyline::QSvgPolyline;
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

  //  bool QSvgPolyline::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgPolylineCall0 call = reinterpret_cast<CuteQSvgPolylineCall0>(taken[0]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgPolyline::separateFillStroke(a0, a1);
  }

  //  Type QSvgPolyline::type() const
  QSvgNode::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgPolylineCall1 call = reinterpret_cast<CuteQSvgPolylineCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgPolyline::type();
  }

  //  bool QSvgPolyline::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgPolylineCall2 call = reinterpret_cast<CuteQSvgPolylineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgPolyline::requiresGroupRendering();
  }
};

//  QSvgPolyline::QSvgPolyline(QSvgNode *parent, const QPolygonF &poly)
extern "C" Q_DECL_EXPORT
QSvgPolyline *ritual_ZN12QSvgPolylineC1EP8QSvgNodeRK9QPolygonF(
    QSvgNode *parent,
    const QPolygonF *poly) {
  return new CuteQSvgPolyline(parent, *poly);
}

//  QSvgPolyline::~QSvgPolyline()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSvgPolylineD1Ev(QSvgPolyline *self) {
  delete self;
}

//  bool QSvgPolyline::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgPolyline18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgPolyline *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  Type QSvgPolyline::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK12QSvgPolyline4typeEv(const QSvgPolyline *self) {
  return self->type();
}

//  bool QSvgPolyline::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSvgPolyline22requiresGroupRenderingEv(
    const QSvgPolyline *self) {
  return self->requiresGroupRendering();
}

//  const QPolygonF &QSvgPolyline::polygon() const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK12QSvgPolyline7polygonEv(const QSvgPolyline *self) {
  return new QPolygonF(self->polygon());
}

//  a Python function taken by a CuteQSvgPolyline, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgPolyline(
    QSvgPolyline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgPolyline *>(self)->take(key, call);
}

//  bool QSvgPolyline::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QSvgPolyline18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgPolyline *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgPolyline::separateFillStroke(a0, *a1);
}

//  Type QSvgPolyline::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK12QSvgPolyline4typeEv(
    const QSvgPolyline *self) {
  return self->QSvgPolyline::type();
}

//  bool QSvgPolyline::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QSvgPolyline22requiresGroupRenderingEv(
    const QSvgPolyline *self) {
  return self->QSvgPolyline::requiresGroupRendering();
}
