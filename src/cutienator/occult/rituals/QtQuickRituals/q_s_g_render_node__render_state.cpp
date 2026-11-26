//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgrendernode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgrendernode.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGRenderNode::RenderState that Python can take functions over in. Every QSGRenderNode::RenderState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGRenderNode_RenderStateCall0)(const void *, int *);
typedef const QRect * (*CuteQSGRenderNode_RenderStateCall1)(const void *, int *);
typedef bool (*CuteQSGRenderNode_RenderStateCall2)(const void *, int *);
typedef int (*CuteQSGRenderNode_RenderStateCall3)(const void *, int *);
typedef bool (*CuteQSGRenderNode_RenderStateCall4)(const void *, int *);
typedef void * (*CuteQSGRenderNode_RenderStateCall5)(const void *, int *);
class CuteQSGRenderNode_RenderState : public QSGRenderNode::RenderState {
public:
  using QSGRenderNode::RenderState::RenderState;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QSGRenderNode11RenderState16projectionMatrixEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode11RenderState11scissorRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode11RenderState14scissorEnabledEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode11RenderState12stencilValueEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode11RenderState14stencilEnabledEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderNode11RenderState10clipRegionEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  const QMatrix4x4 *QSGRenderNode::RenderState::projectionMatrix()
  //      const
  const QMatrix4x4 *projectionMatrix() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRenderNode_RenderStateCall0 call = reinterpret_cast<CuteQSGRenderNode_RenderStateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QMatrix4x4 *>(given);
    }
    return {};
  }

  //  QRect QSGRenderNode::RenderState::scissorRect() const
  QRect scissorRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRenderNode_RenderStateCall1 call = reinterpret_cast<CuteQSGRenderNode_RenderStateCall1>(taken[1]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGRenderNode::RenderState::scissorEnabled() const
  bool scissorEnabled() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRenderNode_RenderStateCall2 call = reinterpret_cast<CuteQSGRenderNode_RenderStateCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QSGRenderNode::RenderState::stencilValue() const
  int stencilValue() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRenderNode_RenderStateCall3 call = reinterpret_cast<CuteQSGRenderNode_RenderStateCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGRenderNode::RenderState::stencilEnabled() const
  bool stencilEnabled() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRenderNode_RenderStateCall4 call = reinterpret_cast<CuteQSGRenderNode_RenderStateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  const QRegion *QSGRenderNode::RenderState::clipRegion() const
  const QRegion *clipRegion() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRenderNode_RenderStateCall5 call = reinterpret_cast<CuteQSGRenderNode_RenderStateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRegion *>(given);
    }
    return {};
  }
};

//  QSGRenderNode::RenderState::~RenderState()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRenderNode11RenderStateD1Ev(
    QSGRenderNode::RenderState *self) {
  delete self;
}

//  const QMatrix4x4 *QSGRenderNode::RenderState::projectionMatrix() const
extern "C" Q_DECL_EXPORT
const QMatrix4x4 *ritual_ZNK13QSGRenderNode11RenderState16projectionMatrixEv(
    const QSGRenderNode::RenderState *self) {
  return self->projectionMatrix();
}

//  QRect QSGRenderNode::RenderState::scissorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QSGRenderNode11RenderState11scissorRectEv(
    const QSGRenderNode::RenderState *self) {
  return new QRect(self->scissorRect());
}

//  bool QSGRenderNode::RenderState::scissorEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSGRenderNode11RenderState14scissorEnabledEv(
    const QSGRenderNode::RenderState *self) {
  return self->scissorEnabled();
}

//  int QSGRenderNode::RenderState::stencilValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QSGRenderNode11RenderState12stencilValueEv(
    const QSGRenderNode::RenderState *self) {
  return self->stencilValue();
}

//  bool QSGRenderNode::RenderState::stencilEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSGRenderNode11RenderState14stencilEnabledEv(
    const QSGRenderNode::RenderState *self) {
  return self->stencilEnabled();
}

//  const QRegion *QSGRenderNode::RenderState::clipRegion() const
extern "C" Q_DECL_EXPORT
const QRegion *ritual_ZNK13QSGRenderNode11RenderState10clipRegionEv(
    const QSGRenderNode::RenderState *self) {
  return self->clipRegion();
}

//  void *QSGRenderNode::RenderState::get(const char *state) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK13QSGRenderNode11RenderState3getEPKc(
    const QSGRenderNode::RenderState *self,
    const char *state) {
  return self->get(state);
}

//  a Python function taken by a CuteQSGRenderNode_RenderState, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRenderNode_RenderState(
    QSGRenderNode::RenderState *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRenderNode_RenderState *>(self)->take(key, call);
}
