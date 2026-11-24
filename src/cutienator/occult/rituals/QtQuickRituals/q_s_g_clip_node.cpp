//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGClipNode that Python can take functions over in. Every QSGClipNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGClipNodeCall0)(const void *, int *);
typedef void (*CuteQSGClipNodeCall1)(const void *, int *);
class CuteQSGClipNode : public QSGClipNode {
public:
  using QSGClipNode::QSGClipNode;
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
      CuteQSGClipNodeCall0 call = reinterpret_cast<CuteQSGClipNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGClipNodeCall1 call = reinterpret_cast<CuteQSGClipNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGClipNode::QSGClipNode()
extern "C" Q_DECL_EXPORT
QSGClipNode *ritual_ZN11QSGClipNodeC1Ev() {
  return new CuteQSGClipNode();
}

//  QSGClipNode::~QSGClipNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGClipNodeD1Ev(QSGClipNode *self) {
  delete self;
}

//  void QSGClipNode::setIsRectangular(bool rectHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGClipNode16setIsRectangularEb(
    QSGClipNode *self,
    bool rectHint) {
  self->setIsRectangular(rectHint);
}

//  bool QSGClipNode::isRectangular() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSGClipNode13isRectangularEv(const QSGClipNode *self) {
  return self->isRectangular();
}

//  void QSGClipNode::setClipRect(const QRectF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGClipNode11setClipRectERK6QRectF(
    QSGClipNode *self,
    const QRectF *a0) {
  self->setClipRect(*a0);
}

//  QRectF QSGClipNode::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QSGClipNode8clipRectEv(const QSGClipNode *self) {
  return new QRectF(self->clipRect());
}

//  a Python function taken by a CuteQSGClipNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGClipNode(
    QSGClipNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGClipNode *>(self)->take(key, call);
}
