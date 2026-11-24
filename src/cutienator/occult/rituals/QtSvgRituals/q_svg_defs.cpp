//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstructure_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgDefs that Python can take functions over in. Every QSvgDefs
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgDefsCall0)(const void *, int *);
typedef bool (*CuteQSvgDefsCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgDefsCall2)(const void *, int *);
class CuteQSvgDefs : public QSvgDefs {
public:
  using QSvgDefs::QSvgDefs;
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

  //  Type QSvgDefs::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgDefsCall0 call = reinterpret_cast<CuteQSvgDefsCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgDefs::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgDefsCall1 call = reinterpret_cast<CuteQSvgDefsCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgDefsCall2 call = reinterpret_cast<CuteQSvgDefsCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgDefs::QSvgDefs(QSvgNode *parent)
extern "C" Q_DECL_EXPORT
QSvgDefs *ritual_ZN8QSvgDefsC1EP8QSvgNode(QSvgNode *parent) {
  return new CuteQSvgDefs(parent);
}

//  QSvgDefs::~QSvgDefs()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSvgDefsD1Ev(QSvgDefs *self) {
  delete self;
}

//  Type QSvgDefs::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK8QSvgDefs4typeEv(const QSvgDefs *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgDefs, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgDefs(QSvgDefs *self, const char *key, void *call) {
  return static_cast<CuteQSvgDefs *>(self)->take(key, call);
}

//  Type QSvgDefs::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK8QSvgDefs4typeEv(const QSvgDefs *self) {
  return self->QSvgDefs::type();
}
