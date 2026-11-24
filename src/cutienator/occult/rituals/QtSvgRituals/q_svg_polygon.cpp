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

//  A QSvgPolygon that Python can take functions over in. Every QSvgPolygon
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgPolygonCall0)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgPolygonCall1)(const void *, int *);
typedef bool (*CuteQSvgPolygonCall2)(const void *, int *);
class CuteQSvgPolygon : public QSvgPolygon {
public:
  using QSvgPolygon::QSvgPolygon;
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

  //  bool QSvgPolygon::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgPolygonCall0 call = reinterpret_cast<CuteQSvgPolygonCall0>(taken[0]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgPolygon::separateFillStroke(a0, a1);
  }

  //  Type QSvgPolygon::type() const
  QSvgNode::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgPolygonCall1 call = reinterpret_cast<CuteQSvgPolygonCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgPolygon::type();
  }

  //  bool QSvgPolygon::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgPolygonCall2 call = reinterpret_cast<CuteQSvgPolygonCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgPolygon::requiresGroupRendering();
  }
};

//  QSvgPolygon::QSvgPolygon(QSvgNode *parent, const QPolygonF &poly)
extern "C" Q_DECL_EXPORT
QSvgPolygon *ritual_ZN11QSvgPolygonC1EP8QSvgNodeRK9QPolygonF(
    QSvgNode *parent,
    const QPolygonF *poly) {
  return new CuteQSvgPolygon(parent, *poly);
}

//  QSvgPolygon::~QSvgPolygon()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSvgPolygonD1Ev(QSvgPolygon *self) {
  delete self;
}

//  bool QSvgPolygon::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgPolygon18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgPolygon *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  Type QSvgPolygon::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK11QSvgPolygon4typeEv(const QSvgPolygon *self) {
  return self->type();
}

//  bool QSvgPolygon::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSvgPolygon22requiresGroupRenderingEv(
    const QSvgPolygon *self) {
  return self->requiresGroupRendering();
}

//  const QPolygonF &QSvgPolygon::polygon() const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK11QSvgPolygon7polygonEv(const QSvgPolygon *self) {
  return new QPolygonF(self->polygon());
}

//  a Python function taken by a CuteQSvgPolygon, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgPolygon(
    QSvgPolygon *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgPolygon *>(self)->take(key, call);
}

//  bool QSvgPolygon::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSvgPolygon18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgPolygon *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgPolygon::separateFillStroke(a0, *a1);
}

//  Type QSvgPolygon::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK11QSvgPolygon4typeEv(const QSvgPolygon *self) {
  return self->QSvgPolygon::type();
}

//  bool QSvgPolygon::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QSvgPolygon22requiresGroupRenderingEv(
    const QSvgPolygon *self) {
  return self->QSvgPolygon::requiresGroupRendering();
}
