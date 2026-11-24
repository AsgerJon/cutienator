//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickShapeGenericNode that Python can take functions over in. Every QQuickShapeGenericNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickShapeGenericNodeCall0)(const void *, int *);
typedef void (*CuteQQuickShapeGenericNodeCall1)(const void *, int *);
class CuteQQuickShapeGenericNode : public QQuickShapeGenericNode {
public:
  using QQuickShapeGenericNode::QQuickShapeGenericNode;
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
      CuteQQuickShapeGenericNodeCall0 call = reinterpret_cast<CuteQQuickShapeGenericNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeGenericNodeCall1 call = reinterpret_cast<CuteQQuickShapeGenericNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  a Python function taken by a CuteQQuickShapeGenericNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeGenericNode(
    QQuickShapeGenericNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeGenericNode *>(self)->take(key, call);
}
