//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <cstring>

//  A QSGRootNode that Python can take functions over in. Every QSGRootNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRootNodeCall0)(const void *, int *);
typedef void (*CuteQSGRootNodeCall1)(const void *, int *);
class CuteQSGRootNode : public QSGRootNode {
public:
  using QSGRootNode::QSGRootNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRootNodeCall0 call = reinterpret_cast<CuteQSGRootNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRootNodeCall1 call = reinterpret_cast<CuteQSGRootNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGRootNode::QSGRootNode()
extern "C" Q_DECL_EXPORT
QSGRootNode *ritual_ZN11QSGRootNodeC1Ev() {
  return new CuteQSGRootNode();
}

//  QSGRootNode::~QSGRootNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRootNodeD1Ev(QSGRootNode *self) {
  delete self;
}

//  void QSGRootNode::notifyNodeChange(QSGNode *node, DirtyState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGRootNode16notifyNodeChangeEP7QSGNode6QFlagsINS0_13DirtyStateBitEE(
    QSGRootNode *self,
    QSGNode *node,
    int state) {
  self->notifyNodeChange(
      node,
      QFlags<QSGNode::DirtyStateBit>::fromInt(state));
}

//  a Python function taken by a CuteQSGRootNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRootNode(
    QSGRootNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRootNode *>(self)->take(key, call);
}
