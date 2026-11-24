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

//  A QSvgStructureNode that Python can take functions over in. Every QSvgStructureNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSvgStructureNodeCall0)(const void *, const QPainter *, const QSvgExtraStates *, int *);
typedef int (*CuteQSvgStructureNodeCall1)(const void *, int *);
typedef bool (*CuteQSvgStructureNodeCall2)(const void *, int *);
class CuteQSvgStructureNode : public QSvgStructureNode {
public:
  using QSvgStructureNode::QSvgStructureNode;
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

  //  bool QSvgNode::separateFillStroke(const QPainter *a0, const
  //      QSvgExtraStates &a1) const
  bool separateFillStroke(
      const QPainter *a0,
      const QSvgExtraStates &a1) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgStructureNodeCall0 call = reinterpret_cast<CuteQSvgStructureNodeCall0>(taken[0]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSvgNode::separateFillStroke(a0, a1);
  }

  //  Type QSvgNode::type() const
  QSvgNode::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSvgStructureNodeCall1 call = reinterpret_cast<CuteQSvgStructureNodeCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgNode::Type>(given);
    }
    return {};
  }

  //  bool QSvgNode::requiresGroupRendering() const
  bool requiresGroupRendering() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSvgStructureNodeCall2 call = reinterpret_cast<CuteQSvgStructureNodeCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSvgNode::requiresGroupRendering();
  }
};

//  QSvgStructureNode::~QSvgStructureNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgStructureNodeD1Ev(QSvgStructureNode *self) {
  delete self;
}

//  QSvgNode *QSvgStructureNode::previousSiblingNode(QSvgNode *n) const
extern "C" Q_DECL_EXPORT
QSvgNode *ritual_ZNK17QSvgStructureNode19previousSiblingNodeEP8QSvgNode(
    const QSvgStructureNode *self,
    QSvgNode *n) {
  return self->previousSiblingNode(n);
}

//  void QSvgStructureNode::releaseDescendants()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgStructureNode18releaseDescendantsEv(
    QSvgStructureNode *self) {
  self->releaseDescendants();
}

//  a Python function taken by a CuteQSvgStructureNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgStructureNode(
    QSvgStructureNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgStructureNode *>(self)->take(key, call);
}
