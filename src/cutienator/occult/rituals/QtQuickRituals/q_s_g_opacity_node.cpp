//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <cstring>

//  A QSGOpacityNode that Python can take functions over in. Every QSGOpacityNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGOpacityNodeCall0)(const void *, int *);
typedef void (*CuteQSGOpacityNodeCall1)(const void *, int *);
class CuteQSGOpacityNode : public QSGOpacityNode {
public:
  using QSGOpacityNode::QSGOpacityNode;
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

  //  bool QSGOpacityNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGOpacityNodeCall0 call = reinterpret_cast<CuteQSGOpacityNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGOpacityNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGOpacityNodeCall1 call = reinterpret_cast<CuteQSGOpacityNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGOpacityNode::QSGOpacityNode()
extern "C" Q_DECL_EXPORT
QSGOpacityNode *ritual_ZN14QSGOpacityNodeC1Ev() {
  return new CuteQSGOpacityNode();
}

//  QSGOpacityNode::~QSGOpacityNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGOpacityNodeD1Ev(QSGOpacityNode *self) {
  delete self;
}

//  void QSGOpacityNode::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGOpacityNode10setOpacityEd(
    QSGOpacityNode *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  qreal QSGOpacityNode::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QSGOpacityNode7opacityEv(const QSGOpacityNode *self) {
  return self->opacity();
}

//  void QSGOpacityNode::setCombinedOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGOpacityNode18setCombinedOpacityEd(
    QSGOpacityNode *self,
    qreal opacity) {
  self->setCombinedOpacity(opacity);
}

//  qreal QSGOpacityNode::combinedOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QSGOpacityNode15combinedOpacityEv(
    const QSGOpacityNode *self) {
  return self->combinedOpacity();
}

//  bool QSGOpacityNode::isSubtreeBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSGOpacityNode16isSubtreeBlockedEv(
    const QSGOpacityNode *self) {
  return self->isSubtreeBlocked();
}

//  a Python function taken by a CuteQSGOpacityNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGOpacityNode(
    QSGOpacityNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGOpacityNode *>(self)->take(key, call);
}

//  bool QSGOpacityNode::isSubtreeBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QSGOpacityNode16isSubtreeBlockedEv(
    const QSGOpacityNode *self) {
  return self->QSGOpacityNode::isSubtreeBlocked();
}
