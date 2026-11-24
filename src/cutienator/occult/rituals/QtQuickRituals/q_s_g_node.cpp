//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <cstring>

//  A QSGNode that Python can take functions over in. Every QSGNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGNodeCall0)(const void *, int *);
typedef void (*CuteQSGNodeCall1)(const void *, int *);
class CuteQSGNode : public QSGNode {
public:
  using QSGNode::QSGNode;
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
      CuteQSGNodeCall0 call = reinterpret_cast<CuteQSGNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGNodeCall1 call = reinterpret_cast<CuteQSGNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGNode::QSGNode()
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN7QSGNodeC1Ev() {
  return new CuteQSGNode();
}

//  QSGNode::~QSGNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNodeD1Ev(QSGNode *self) {
  delete self;
}

//  QSGNode *QSGNode::parent() const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK7QSGNode6parentEv(const QSGNode *self) {
  return self->parent();
}

//  void QSGNode::removeChildNode(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode15removeChildNodeEPS_(QSGNode *self, QSGNode *node) {
  self->removeChildNode(node);
}

//  void QSGNode::removeAllChildNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode19removeAllChildNodesEv(QSGNode *self) {
  self->removeAllChildNodes();
}

//  void QSGNode::prependChildNode(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode16prependChildNodeEPS_(QSGNode *self, QSGNode *node) {
  self->prependChildNode(node);
}

//  void QSGNode::appendChildNode(QSGNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode15appendChildNodeEPS_(QSGNode *self, QSGNode *node) {
  self->appendChildNode(node);
}

//  void QSGNode::insertChildNodeBefore(QSGNode *node, QSGNode *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode21insertChildNodeBeforeEPS_S0_(
    QSGNode *self,
    QSGNode *node,
    QSGNode *before) {
  self->insertChildNodeBefore(node, before);
}

//  void QSGNode::insertChildNodeAfter(QSGNode *node, QSGNode *after)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode20insertChildNodeAfterEPS_S0_(
    QSGNode *self,
    QSGNode *node,
    QSGNode *after) {
  self->insertChildNodeAfter(node, after);
}

//  void QSGNode::reparentChildNodesTo(QSGNode *newParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode20reparentChildNodesToEPS_(
    QSGNode *self,
    QSGNode *newParent) {
  self->reparentChildNodesTo(newParent);
}

//  int QSGNode::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSGNode10childCountEv(const QSGNode *self) {
  return self->childCount();
}

//  QSGNode *QSGNode::childAtIndex(int i) const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK7QSGNode12childAtIndexEi(const QSGNode *self, int i) {
  return self->childAtIndex(i);
}

//  QSGNode *QSGNode::firstChild() const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK7QSGNode10firstChildEv(const QSGNode *self) {
  return self->firstChild();
}

//  QSGNode *QSGNode::lastChild() const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK7QSGNode9lastChildEv(const QSGNode *self) {
  return self->lastChild();
}

//  QSGNode *QSGNode::nextSibling() const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK7QSGNode11nextSiblingEv(const QSGNode *self) {
  return self->nextSibling();
}

//  QSGNode *QSGNode::previousSibling() const
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZNK7QSGNode15previousSiblingEv(const QSGNode *self) {
  return self->previousSibling();
}

//  NodeType QSGNode::type() const
extern "C" Q_DECL_EXPORT
QSGNode::NodeType ritual_ZNK7QSGNode4typeEv(const QSGNode *self) {
  return self->type();
}

//  void QSGNode::clearDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode10clearDirtyEv(QSGNode *self) {
  self->clearDirty();
}

//  void QSGNode::markDirty(DirtyState bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode9markDirtyE6QFlagsINS_13DirtyStateBitEE(
    QSGNode *self,
    int bits) {
  self->markDirty(QFlags<QSGNode::DirtyStateBit>::fromInt(bits));
}

//  DirtyState QSGNode::dirtyState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSGNode10dirtyStateEv(const QSGNode *self) {
  return static_cast<int>(self->dirtyState().toInt());
}

//  bool QSGNode::isSubtreeBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QSGNode16isSubtreeBlockedEv(const QSGNode *self) {
  return self->isSubtreeBlocked();
}

//  Flags QSGNode::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QSGNode5flagsEv(const QSGNode *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QSGNode::setFlag(Flag a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode7setFlagENS_4FlagEb(
    QSGNode *self,
    QSGNode::Flag a0,
    bool a1) {
  self->setFlag(a0, a1);
}

//  void QSGNode::setFlags(Flags a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode8setFlagsE6QFlagsINS_4FlagEEb(
    QSGNode *self,
    int a0,
    bool a1) {
  self->setFlags(QFlags<QSGNode::Flag>::fromInt(a0), a1);
}

//  void QSGNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode10preprocessEv(QSGNode *self) {
  self->preprocess();
}

//  QSGNode::QSGNode(NodeType type)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN7QSGNodeC1ENS_8NodeTypeE(QSGNode::NodeType type) {
  return new CuteQSGNode(type);
}

//  void QSGNode::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode4initEv(QSGNode *self) {
  self->init();
}

//  void QSGNode::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QSGNode7destroyEv(QSGNode *self) {
  self->destroy();
}

//  a Python function taken by a CuteQSGNode, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGNode(QSGNode *self, const char *key, void *call) {
  return static_cast<CuteQSGNode *>(self)->take(key, call);
}

//  bool QSGNode::isSubtreeBlocked() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK7QSGNode16isSubtreeBlockedEv(const QSGNode *self) {
  return self->QSGNode::isSubtreeBlocked();
}

//  void QSGNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QSGNode10preprocessEv(QSGNode *self) {
  self->QSGNode::preprocess();
}
