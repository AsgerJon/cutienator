//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <cstring>

//  A QSGBasicGeometryNode that Python can take functions over in. Every QSGBasicGeometryNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGBasicGeometryNodeCall0)(const void *, int *);
typedef void (*CuteQSGBasicGeometryNodeCall1)(const void *, int *);
class CuteQSGBasicGeometryNode : public QSGBasicGeometryNode {
public:
  using QSGBasicGeometryNode::QSGBasicGeometryNode;
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
      CuteQSGBasicGeometryNodeCall0 call = reinterpret_cast<CuteQSGBasicGeometryNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBasicGeometryNodeCall1 call = reinterpret_cast<CuteQSGBasicGeometryNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGBasicGeometryNode::~QSGBasicGeometryNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGBasicGeometryNodeD1Ev(QSGBasicGeometryNode *self) {
  delete self;
}

//  void QSGBasicGeometryNode::setGeometry(QSGGeometry *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGBasicGeometryNode11setGeometryEP11QSGGeometry(
    QSGBasicGeometryNode *self,
    QSGGeometry *geometry) {
  self->setGeometry(geometry);
}

//  const QSGGeometry *QSGBasicGeometryNode::geometry() const
extern "C" Q_DECL_EXPORT
const QSGGeometry *ritual_ZNK20QSGBasicGeometryNode8geometryEv(
    const QSGBasicGeometryNode *self) {
  return self->geometry();
}

//  QSGGeometry *QSGBasicGeometryNode::geometry()
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN20QSGBasicGeometryNode8geometryEv(
    QSGBasicGeometryNode *self) {
  return self->geometry();
}

//  const QMatrix4x4 *QSGBasicGeometryNode::matrix() const
extern "C" Q_DECL_EXPORT
const QMatrix4x4 *ritual_ZNK20QSGBasicGeometryNode6matrixEv(
    const QSGBasicGeometryNode *self) {
  return self->matrix();
}

//  const QSGClipNode *QSGBasicGeometryNode::clipList() const
extern "C" Q_DECL_EXPORT
const QSGClipNode *ritual_ZNK20QSGBasicGeometryNode8clipListEv(
    const QSGBasicGeometryNode *self) {
  return self->clipList();
}

//  void QSGBasicGeometryNode::setRendererMatrix(const QMatrix4x4 *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGBasicGeometryNode17setRendererMatrixEPK10QMatrix4x4(
    QSGBasicGeometryNode *self,
    const QMatrix4x4 *m) {
  self->setRendererMatrix(m);
}

//  void QSGBasicGeometryNode::setRendererClipList(const QSGClipNode *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGBasicGeometryNode19setRendererClipListEPK11QSGClipNode(
    QSGBasicGeometryNode *self,
    const QSGClipNode *c) {
  self->setRendererClipList(c);
}

//  QSGBasicGeometryNode::QSGBasicGeometryNode(NodeType type)
extern "C" Q_DECL_EXPORT
QSGBasicGeometryNode *ritual_ZN20QSGBasicGeometryNodeC1EN7QSGNode8NodeTypeE(
    QSGNode::NodeType type) {
  return new CuteQSGBasicGeometryNode(type);
}

//  QSGBasicGeometryNode::QSGBasicGeometryNode(QSGBasicGeometryNodePrivate
//      &dd, NodeType type)
extern "C" Q_DECL_EXPORT
QSGBasicGeometryNode *ritual_ZN20QSGBasicGeometryNodeC1ER27QSGBasicGeometryNodePrivateN7QSGNode8NodeTypeE(
    QSGBasicGeometryNodePrivate *dd,
    QSGNode::NodeType type) {
  return new CuteQSGBasicGeometryNode(*dd, type);
}

//  a Python function taken by a CuteQSGBasicGeometryNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBasicGeometryNode(
    QSGBasicGeometryNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBasicGeometryNode *>(self)->take(key, call);
}
