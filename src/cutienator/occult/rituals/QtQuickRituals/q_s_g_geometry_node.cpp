//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <cstring>

//  A QSGGeometryNode that Python can take functions over in. Every QSGGeometryNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGGeometryNodeCall0)(const void *, int *);
typedef void (*CuteQSGGeometryNodeCall1)(const void *, int *);
class CuteQSGGeometryNode : public QSGGeometryNode {
public:
  using QSGGeometryNode::QSGGeometryNode;
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
      CuteQSGGeometryNodeCall0 call = reinterpret_cast<CuteQSGGeometryNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGGeometryNodeCall1 call = reinterpret_cast<CuteQSGGeometryNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGGeometryNode::QSGGeometryNode()
extern "C" Q_DECL_EXPORT
QSGGeometryNode *ritual_ZN15QSGGeometryNodeC1Ev() {
  return new CuteQSGGeometryNode();
}

//  QSGGeometryNode::~QSGGeometryNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryNodeD1Ev(QSGGeometryNode *self) {
  delete self;
}

//  void QSGGeometryNode::setMaterial(QSGMaterial *material)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryNode11setMaterialEP11QSGMaterial(
    QSGGeometryNode *self,
    QSGMaterial *material) {
  self->setMaterial(material);
}

//  QSGMaterial *QSGGeometryNode::material() const
extern "C" Q_DECL_EXPORT
QSGMaterial *ritual_ZNK15QSGGeometryNode8materialEv(
    const QSGGeometryNode *self) {
  return self->material();
}

//  void QSGGeometryNode::setOpaqueMaterial(QSGMaterial *material)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryNode17setOpaqueMaterialEP11QSGMaterial(
    QSGGeometryNode *self,
    QSGMaterial *material) {
  self->setOpaqueMaterial(material);
}

//  QSGMaterial *QSGGeometryNode::opaqueMaterial() const
extern "C" Q_DECL_EXPORT
QSGMaterial *ritual_ZNK15QSGGeometryNode14opaqueMaterialEv(
    const QSGGeometryNode *self) {
  return self->opaqueMaterial();
}

//  QSGMaterial *QSGGeometryNode::activeMaterial() const
extern "C" Q_DECL_EXPORT
QSGMaterial *ritual_ZNK15QSGGeometryNode14activeMaterialEv(
    const QSGGeometryNode *self) {
  return self->activeMaterial();
}

//  void QSGGeometryNode::setRenderOrder(int order)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryNode14setRenderOrderEi(
    QSGGeometryNode *self,
    int order) {
  self->setRenderOrder(order);
}

//  int QSGGeometryNode::renderOrder() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSGGeometryNode11renderOrderEv(const QSGGeometryNode *self) {
  return self->renderOrder();
}

//  void QSGGeometryNode::setInheritedOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSGGeometryNode19setInheritedOpacityEd(
    QSGGeometryNode *self,
    qreal opacity) {
  self->setInheritedOpacity(opacity);
}

//  qreal QSGGeometryNode::inheritedOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QSGGeometryNode16inheritedOpacityEv(
    const QSGGeometryNode *self) {
  return self->inheritedOpacity();
}

//  QSGGeometryNode::QSGGeometryNode(QSGGeometryNodePrivate &dd)
extern "C" Q_DECL_EXPORT
QSGGeometryNode *ritual_ZN15QSGGeometryNodeC1ER22QSGGeometryNodePrivate(
    QSGGeometryNodePrivate *dd) {
  return new CuteQSGGeometryNode(*dd);
}

//  a Python function taken by a CuteQSGGeometryNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGGeometryNode(
    QSGGeometryNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGGeometryNode *>(self)->take(key, call);
}
