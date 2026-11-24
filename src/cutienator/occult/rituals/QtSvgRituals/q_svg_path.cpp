//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgPath that Python can take functions over in. Every QSvgPath
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgPathCall0)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgPathCall1)(const void *, int *);
typedef bool (*CuteQSvgPathCall2)(const void *, int *);
class CuteQSvgPath : public QSvgPath {
public:
  using QSvgPath::QSvgPath;
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

  //  bool QSvgPath::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgPathCall0 call = reinterpret_cast<CuteQSvgPathCall0>(taken[0]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgPath::separateFillStroke(a0, a1);
  }

  //  Type QSvgPath::type() const
  QSvgNode::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgPathCall1 call = reinterpret_cast<CuteQSvgPathCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgPath::type();
  }

  //  bool QSvgPath::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgPathCall2 call = reinterpret_cast<CuteQSvgPathCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgPath::requiresGroupRendering();
  }
};

//  QSvgPath::QSvgPath(QSvgNode *parent, const QPainterPath &qpath)
extern "C" Q_DECL_EXPORT
QSvgPath *ritual_ZN8QSvgPathC1EP8QSvgNodeRK12QPainterPath(
    QSvgNode *parent,
    const QPainterPath *qpath) {
  return new CuteQSvgPath(parent, *qpath);
}

//  QSvgPath::~QSvgPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgPathD1Ev(QSvgPath *self) {
  delete self;
}

//  bool QSvgPath::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgPath18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgPath *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->separateFillStroke(a0, *a1);
}

//  Type QSvgPath::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgPath4typeEv(const QSvgPath *self) {
  return self->type();
}

//  bool QSvgPath::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgPath22requiresGroupRenderingEv(const QSvgPath *self) {
  return self->requiresGroupRendering();
}

//  const QPainterPath &QSvgPath::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK8QSvgPath4pathEv(const QSvgPath *self) {
  return new QPainterPath(self->path());
}

//  a Python function taken by a CuteQSvgPath, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgPath(QSvgPath *self, const char *key, void *call) {
  return static_cast<CuteQSvgPath *>(self)->take(key, call);
}

//  bool QSvgPath::separateFillStroke(const QPainter *a0, const
//      QSvgExtraStates &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgPath18separateFillStrokeEPK8QPainterRK15QSvgExtraStates(
    const QSvgPath *self,
    const QPainter *a0,
    const QSvgExtraStates *a1) {
  return self->QSvgPath::separateFillStroke(a0, *a1);
}

//  Type QSvgPath::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgPath4typeEv(const QSvgPath *self) {
  return self->QSvgPath::type();
}

//  bool QSvgPath::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgPath22requiresGroupRenderingEv(
    const QSvgPath *self) {
  return self->QSvgPath::requiresGroupRendering();
}
