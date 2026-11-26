//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgrendernode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgrendernode.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGRenderNode that Python can take functions over in. Every QSGRenderNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSGRenderNodeCall0)(const void *, int *);
typedef void (*CuteQSGRenderNodeCall1)(const void *, int *);
typedef void (*CuteQSGRenderNodeCall2)(const void *, const QSGRenderNode::RenderState *, int *);
typedef void (*CuteQSGRenderNodeCall3)(const void *, int *);
typedef int (*CuteQSGRenderNodeCall4)(const void *, int *);
typedef const QRectF * (*CuteQSGRenderNodeCall5)(const void *, int *);
typedef bool (*CuteQSGRenderNodeCall6)(const void *, int *);
typedef void (*CuteQSGRenderNodeCall7)(const void *, int *);
class CuteQSGRenderNode : public QSGRenderNode {
public:
  using QSGRenderNode::QSGRenderNode;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QSGRenderNode13changedStatesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderNode7prepareEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderNode6renderEPKNS_11RenderStateE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderNode16releaseResourcesEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode5flagsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode4rectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  StateFlags QSGRenderNode::changedStates() const
  QSGRenderNode::StateFlags changedStates() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRenderNodeCall0 call = reinterpret_cast<CuteQSGRenderNodeCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRenderNode::StateFlag>::fromInt(given);
    }
    return QSGRenderNode::changedStates();
  }

  //  void QSGRenderNode::prepare()
  void prepare() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRenderNodeCall1 call = reinterpret_cast<CuteQSGRenderNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderNode::prepare();
  }

  //  void QSGRenderNode::render(const RenderState *state)
  void render(const QSGRenderNode::RenderState *state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRenderNodeCall2 call = reinterpret_cast<CuteQSGRenderNodeCall2>(taken[2]);
      call(this, state, &handled);
      if (handled) return;
    }
  }

  //  void QSGRenderNode::releaseResources()
  void releaseResources() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRenderNodeCall3 call = reinterpret_cast<CuteQSGRenderNodeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderNode::releaseResources();
  }

  //  RenderingFlags QSGRenderNode::flags() const
  QSGRenderNode::RenderingFlags flags() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRenderNodeCall4 call = reinterpret_cast<CuteQSGRenderNodeCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRenderNode::RenderingFlag>::fromInt(given);
    }
    return QSGRenderNode::flags();
  }

  //  QRectF QSGRenderNode::rect() const
  QRectF rect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRenderNodeCall5 call = reinterpret_cast<CuteQSGRenderNodeCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGRenderNode::rect();
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRenderNodeCall6 call = reinterpret_cast<CuteQSGRenderNodeCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRenderNodeCall7 call = reinterpret_cast<CuteQSGRenderNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGRenderNode::QSGRenderNode()
extern "C" Q_DECL_EXPORT
QSGRenderNode *ritual_ZN13QSGRenderNodeC1Ev() {
  return new CuteQSGRenderNode();
}

//  QSGRenderNode::~QSGRenderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderNodeD1Ev(QSGRenderNode *self) {
  delete self;
}

//  StateFlags QSGRenderNode::changedStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSGRenderNode13changedStatesEv(const QSGRenderNode *self) {
  return static_cast<int>(self->changedStates().toInt());
}

//  void QSGRenderNode::prepare()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderNode7prepareEv(QSGRenderNode *self) {
  self->prepare();
}

//  void QSGRenderNode::render(const RenderState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderNode6renderEPKNS_11RenderStateE(
    QSGRenderNode *self,
    const QSGRenderNode::RenderState *state) {
  self->render(state);
}

//  void QSGRenderNode::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderNode16releaseResourcesEv(QSGRenderNode *self) {
  self->releaseResources();
}

//  RenderingFlags QSGRenderNode::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSGRenderNode5flagsEv(const QSGRenderNode *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QRectF QSGRenderNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QSGRenderNode4rectEv(const QSGRenderNode *self) {
  return new QRectF(self->rect());
}

//  const QMatrix4x4 *QSGRenderNode::projectionMatrix() const
extern "C" Q_DECL_EXPORT
const QMatrix4x4 *ritual_ZNK13QSGRenderNode16projectionMatrixEv(
    const QSGRenderNode *self) {
  return self->projectionMatrix();
}

//  const QMatrix4x4 *QSGRenderNode::projectionMatrix(qsizetype index) const
extern "C" Q_DECL_EXPORT
const QMatrix4x4 *ritual_ZNK13QSGRenderNode16projectionMatrixEx(
    const QSGRenderNode *self,
    qsizetype index) {
  return self->projectionMatrix(index);
}

//  const QMatrix4x4 *QSGRenderNode::matrix() const
extern "C" Q_DECL_EXPORT
const QMatrix4x4 *ritual_ZNK13QSGRenderNode6matrixEv(
    const QSGRenderNode *self) {
  return self->matrix();
}

//  const QSGClipNode *QSGRenderNode::clipList() const
extern "C" Q_DECL_EXPORT
const QSGClipNode *ritual_ZNK13QSGRenderNode8clipListEv(
    const QSGRenderNode *self) {
  return self->clipList();
}

//  qreal QSGRenderNode::inheritedOpacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QSGRenderNode16inheritedOpacityEv(
    const QSGRenderNode *self) {
  return self->inheritedOpacity();
}

//  QRhiRenderTarget *QSGRenderNode::renderTarget() const
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZNK13QSGRenderNode12renderTargetEv(
    const QSGRenderNode *self) {
  return self->renderTarget();
}

//  QRhiCommandBuffer *QSGRenderNode::commandBuffer() const
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZNK13QSGRenderNode13commandBufferEv(
    const QSGRenderNode *self) {
  return self->commandBuffer();
}

//  a Python function taken by a CuteQSGRenderNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRenderNode(
    QSGRenderNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRenderNode *>(self)->take(key, call);
}

//  StateFlags QSGRenderNode::changedStates() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QSGRenderNode13changedStatesEv(
    const QSGRenderNode *self) {
  return static_cast<int>(self->QSGRenderNode::changedStates().toInt());
}

//  void QSGRenderNode::prepare()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGRenderNode7prepareEv(QSGRenderNode *self) {
  self->QSGRenderNode::prepare();
}

//  void QSGRenderNode::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGRenderNode16releaseResourcesEv(QSGRenderNode *self) {
  self->QSGRenderNode::releaseResources();
}

//  RenderingFlags QSGRenderNode::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QSGRenderNode5flagsEv(const QSGRenderNode *self) {
  return static_cast<int>(self->QSGRenderNode::flags().toInt());
}

//  QRectF QSGRenderNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK13QSGRenderNode4rectEv(const QSGRenderNode *self) {
  return new QRectF(self->QSGRenderNode::rect());
}
