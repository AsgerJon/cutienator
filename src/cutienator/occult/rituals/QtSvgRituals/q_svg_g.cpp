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

//  A QSvgG that Python can take functions over in. Every QSvgG
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgGCall0)(const void *, int *);
typedef bool (*CuteQSvgGCall1)(const void *, int *);
typedef bool (*CuteQSvgGCall2)(const void *, const QPainter *, const QSvgExtraStates *, int *);
class CuteQSvgG : public QSvgG {
public:
  using QSvgG::QSvgG;
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

  //  Type QSvgG::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgGCall0 call = reinterpret_cast<CuteQSvgGCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgG::type();
  }

  //  bool QSvgG::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgGCall1 call = reinterpret_cast<CuteQSvgGCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgG::requiresGroupRendering();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgGCall2 call = reinterpret_cast<CuteQSvgGCall2>(taken[2]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }
};

//  QSvgG::QSvgG(QSvgNode *parent)
extern "C" Q_DECL_EXPORT
QSvgG *ritual_ZN5QSvgGC1EP8QSvgNode(QSvgNode *parent) {
  return new CuteQSvgG(parent);
}

//  QSvgG::~QSvgG()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSvgGD1Ev(QSvgG *self) {
  delete self;
}

//  Type QSvgG::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK5QSvgG4typeEv(const QSvgG *self) {
  return self->type();
}

//  bool QSvgG::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QSvgG22requiresGroupRenderingEv(const QSvgG *self) {
  return self->requiresGroupRendering();
}

//  a Python function taken by a CuteQSvgG, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgG(QSvgG *self, const char *key, void *call) {
  return static_cast<CuteQSvgG *>(self)->take(key, call);
}

//  Type QSvgG::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK5QSvgG4typeEv(const QSvgG *self) {
  return self->QSvgG::type();
}

//  bool QSvgG::requiresGroupRendering() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK5QSvgG22requiresGroupRenderingEv(const QSvgG *self) {
  return self->QSvgG::requiresGroupRendering();
}
