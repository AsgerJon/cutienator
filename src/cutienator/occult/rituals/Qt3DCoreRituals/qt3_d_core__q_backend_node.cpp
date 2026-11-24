//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qbackendnode.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qbackendnode.h>
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

//  Qt3DCore::QBackendNode::~QBackendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QBackendNodeD1Ev(Qt3DCore::QBackendNode *self) {
  delete self;
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
