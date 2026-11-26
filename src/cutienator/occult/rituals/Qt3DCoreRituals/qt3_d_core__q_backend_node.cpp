//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qbackendnode.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qbackendnode.h>
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DCore::QBackendNode that Python can take functions over in. Every Qt3DCore::QBackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QBackendNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DCore_QBackendNode : public Qt3DCore::QBackendNode {
public:
  using Qt3DCore::QBackendNode::QBackendNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QBackendNode::syncFromFrontEnd(const QNode *frontEnd,
  //      bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodeCall0 call = reinterpret_cast<CuteQt3DCore_QBackendNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DCore::QBackendNode::QBackendNode(Mode mode)
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZN8Qt3DCore12QBackendNodeC1ENS0_4ModeE(
    Qt3DCore::QBackendNode::Mode mode) {
  return new CuteQt3DCore_QBackendNode(mode);
}

//  Qt3DCore::QBackendNode::~QBackendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QBackendNodeD1Ev(Qt3DCore::QBackendNode *self) {
  delete self;
}

//  QNodeId Qt3DCore::QBackendNode::peerId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK8Qt3DCore12QBackendNode6peerIdEv(
    const Qt3DCore::QBackendNode *self) {
  return new Qt3DCore::QNodeId(self->peerId());
}

//  void Qt3DCore::QBackendNode::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QBackendNode10setEnabledEb(
    Qt3DCore::QBackendNode *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool Qt3DCore::QBackendNode::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore12QBackendNode9isEnabledEv(
    const Qt3DCore::QBackendNode *self) {
  return self->isEnabled();
}

//  Mode Qt3DCore::QBackendNode::mode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode::Mode ritual_ZNK8Qt3DCore12QBackendNode4modeEv(
    const Qt3DCore::QBackendNode *self) {
  return self->mode();
}

//  void Qt3DCore::QBackendNode::syncFromFrontEnd(const QNode *frontEnd, bool
//      firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb(
    Qt3DCore::QBackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QBackendNodePrivate *Qt3DCore::QBackendNode::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNodePrivate *ritual_ZN8Qt3DCore12QBackendNode6d_funcEv(
    Qt3DCore::QBackendNode *self) {
  return self->d_func();
}

//  const QBackendNodePrivate *Qt3DCore::QBackendNode::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QBackendNodePrivate *ritual_ZNK8Qt3DCore12QBackendNode6d_funcEv(
    const Qt3DCore::QBackendNode *self) {
  return self->d_func();
}

//  Qt3DCore::QBackendNode::QBackendNode(QBackendNodePrivate &dd)
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZN8Qt3DCore12QBackendNodeC1ERNS_19QBackendNodePrivateE(
    Qt3DCore::QBackendNodePrivate *dd) {
  return new CuteQt3DCore_QBackendNode(*dd);
}

//  void Qt3DCore::QBackendNode::setPeerId(QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QBackendNode9setPeerIdENS_7QNodeIdE(
    Qt3DCore::QBackendNode *self,
    const Qt3DCore::QNodeId *id) {
  self->setPeerId(*id);
}

//  a Python function taken by a CuteQt3DCore_QBackendNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QBackendNode(
    Qt3DCore::QBackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QBackendNode *>(self)->take(key, call);
}

//  void Qt3DCore::QBackendNode::syncFromFrontEnd(const QNode *frontEnd, bool
//      firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb(
    Qt3DCore::QBackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DCore::QBackendNode::syncFromFrontEnd(frontEnd, firstTime);
}
