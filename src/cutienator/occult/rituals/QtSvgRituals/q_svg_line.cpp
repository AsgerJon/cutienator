//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qline.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgLine that Python can take functions over in. Every QSvgLine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgLineCall0)(const void *, int *);
typedef bool (*CuteQSvgLineCall1)(const void *, int *);
typedef bool (*CuteQSvgLineCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
class CuteQSvgLine : public QSvgLine {
public:
  using QSvgLine::QSvgLine;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSvgNode4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode22requiresGroupRenderingEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSvgNode18separateFillStrokeEPK8QPainterRK15QSvgExtraStates")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgLine::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgLineCall0 call = reinterpret_cast<CuteQSvgLineCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgLine::type();
  }

  //  bool QSvgLine::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgLineCall1 call = reinterpret_cast<CuteQSvgLineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgLine::requiresGroupRendering();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgLineCall2 call = reinterpret_cast<CuteQSvgLineCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }
};

//  QSvgLine::QSvgLine(QSvgNode *parent, const QLineF &line)
extern "C" Q_DECL_EXPORT
QSvgLine *ritual_ZN8QSvgLineC1EP8QSvgNodeRK6QLineF(
    QSvgNode *parent,
    const QLineF *line) {
  return new CuteQSvgLine(parent, *line);
}

//  QSvgLine::~QSvgLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgLineD1Ev(QSvgLine *self) {
  delete self;
}

//  Type QSvgLine::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgLine4typeEv(const QSvgLine *self) {
  return self->type();
}

//  bool QSvgLine::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSvgLine22requiresGroupRenderingEv(const QSvgLine *self) {
  return self->requiresGroupRendering();
}

//  QLineF QSvgLine::line() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK8QSvgLine4lineEv(const QSvgLine *self) {
  return new QLineF(self->line());
}

//  a Python function taken by a CuteQSvgLine, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgLine(QSvgLine *self, const char *key, void *call) {
  return static_cast<CuteQSvgLine *>(self)->take(key, call);
}

//  Type QSvgLine::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgLine4typeEv(const QSvgLine *self) {
  return self->QSvgLine::type();
}

//  bool QSvgLine::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8QSvgLine22requiresGroupRenderingEv(
    const QSvgLine *self) {
  return self->QSvgLine::requiresGroupRendering();
}
