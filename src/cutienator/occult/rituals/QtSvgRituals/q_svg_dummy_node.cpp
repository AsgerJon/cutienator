//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvggraphics_p.h>
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSvgDummyNode that Python can take functions over in. Every QSvgDummyNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgDummyNodeCall0)(const void *, int *);
typedef bool (*CuteQSvgDummyNodeCall1)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef bool (*CuteQSvgDummyNodeCall2)(const void *, int *);
class CuteQSvgDummyNode : public QSvgDummyNode {
public:
  using QSvgDummyNode::QSvgDummyNode;
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

  //  Type QSvgDummyNode::type() const
  QSvgNode::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgDummyNodeCall0 call = reinterpret_cast<CuteQSvgDummyNodeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return QSvgDummyNode::type();
  }

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgDummyNodeCall1 call = reinterpret_cast<CuteQSvgDummyNodeCall1>(taken[1]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgDummyNodeCall2 call = reinterpret_cast<CuteQSvgDummyNodeCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgDummyNode::~QSvgDummyNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSvgDummyNodeD1Ev(QSvgDummyNode *self) {
  delete self;
}

//  Type QSvgDummyNode::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_ZNK13QSvgDummyNode4typeEv(const QSvgDummyNode *self) {
  return self->type();
}

//  a Python function taken by a CuteQSvgDummyNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgDummyNode(
    QSvgDummyNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgDummyNode *>(self)->take(key, call);
}

//  Type QSvgDummyNode::type() const
extern "C" Q_DECL_EXPORT
QSvgNode::Type ritual_own_ZNK13QSvgDummyNode4typeEv(
    const QSvgDummyNode *self) {
  return self->QSvgDummyNode::type();
}
