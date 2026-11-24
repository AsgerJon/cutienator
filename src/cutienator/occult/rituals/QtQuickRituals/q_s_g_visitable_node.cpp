//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGVisitableNode that Python can take functions over in. Every QSGVisitableNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGVisitableNodeCall0)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGVisitableNodeCall1)(const void *, int *);
typedef void (*CuteQSGVisitableNodeCall2)(const void *, int *);
class CuteQSGVisitableNode : public QSGVisitableNode {
public:
  using QSGVisitableNode::QSGVisitableNode;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QSGVisitableNode::accept(QSGNodeVisitorEx *a0)
  void accept(QSGNodeVisitorEx *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGVisitableNodeCall0 call = reinterpret_cast<CuteQSGVisitableNodeCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGVisitableNodeCall1 call = reinterpret_cast<CuteQSGVisitableNodeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGVisitableNodeCall2 call = reinterpret_cast<CuteQSGVisitableNodeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGVisitableNode::~QSGVisitableNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGVisitableNodeD1Ev(QSGVisitableNode *self) {
  delete self;
}

//  void QSGVisitableNode::accept(QSGNodeVisitorEx *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx(
    QSGVisitableNode *self,
    QSGNodeVisitorEx *a0) {
  self->accept(a0);
}

//  a Python function taken by a CuteQSGVisitableNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGVisitableNode(
    QSGVisitableNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGVisitableNode *>(self)->take(key, call);
}
