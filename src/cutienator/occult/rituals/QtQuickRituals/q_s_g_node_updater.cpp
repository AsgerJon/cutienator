//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgnodeupdater_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgnodeupdater_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QSGNodeUpdater may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGNodeUpdater : QSGNodeUpdater {
  using QSGNodeUpdater::enterTransformNode;
  using QSGNodeUpdater::leaveTransformNode;
};

//  A QSGNodeUpdater that Python can take functions over in. Every QSGNodeUpdater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGNodeUpdaterCall0)(const void *, QSGNode *, int *);
typedef bool (*CuteQSGNodeUpdaterCall1)(const void *, QSGNode *, QSGNode *, int *);
typedef void (*CuteQSGNodeUpdaterCall2)(const void *, QSGTransformNode *, int *);
typedef void (*CuteQSGNodeUpdaterCall3)(const void *, QSGTransformNode *, int *);
class CuteQSGNodeUpdater : public QSGNodeUpdater {
public:
  using QSGNodeUpdater::QSGNodeUpdater;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QSGNodeUpdater12updateStatesEP7QSGNode")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QSGNodeUpdater13isNodeBlockedEP7QSGNodeS1_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeUpdater18enterTransformNodeEP16QSGTransformNode")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeUpdater18leaveTransformNodeEP16QSGTransformNode")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QSGNodeUpdater::updateStates(QSGNode *n)
  void updateStates(QSGNode *n) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGNodeUpdaterCall0 call = reinterpret_cast<CuteQSGNodeUpdaterCall0>(taken[0]);
      call(this, n, &handled);
      if (handled) return;
    }
    QSGNodeUpdater::updateStates(n);
  }

  //  bool QSGNodeUpdater::isNodeBlocked(QSGNode *n, QSGNode *root) const
  bool isNodeBlocked(QSGNode *n, QSGNode *root) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGNodeUpdaterCall1 call = reinterpret_cast<CuteQSGNodeUpdaterCall1>(taken[1]);
      bool given = call(this, n, root, &handled);
      if (handled) return given;
    }
    return QSGNodeUpdater::isNodeBlocked(n, root);
  }

  //  void QSGNodeUpdater::enterTransformNode(QSGTransformNode *a0)
  void enterTransformNode(QSGTransformNode *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGNodeUpdaterCall2 call = reinterpret_cast<CuteQSGNodeUpdaterCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeUpdater::enterTransformNode(a0);
  }

  //  void QSGNodeUpdater::leaveTransformNode(QSGTransformNode *a0)
  void leaveTransformNode(QSGTransformNode *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGNodeUpdaterCall3 call = reinterpret_cast<CuteQSGNodeUpdaterCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeUpdater::leaveTransformNode(a0);
  }
};

//  QSGNodeUpdater::QSGNodeUpdater()
extern "C" Q_DECL_EXPORT
QSGNodeUpdater *ritual_ZN14QSGNodeUpdaterC1Ev() {
  return new CuteQSGNodeUpdater();
}

//  QSGNodeUpdater::~QSGNodeUpdater()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdaterD1Ev(QSGNodeUpdater *self) {
  delete self;
}

//  void QSGNodeUpdater::updateStates(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater12updateStatesEP7QSGNode(
    QSGNodeUpdater *self,
    QSGNode *n) {
  self->updateStates(n);
}

//  bool QSGNodeUpdater::isNodeBlocked(QSGNode *n, QSGNode *root) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSGNodeUpdater13isNodeBlockedEP7QSGNodeS1_(
    const QSGNodeUpdater *self,
    QSGNode *n,
    QSGNode *root) {
  return self->isNodeBlocked(n, root);
}

//  void QSGNodeUpdater::enterTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater18enterTransformNodeEP16QSGTransformNode(
    QSGNodeUpdater *self,
    QSGTransformNode *a0) {
  self->enterTransformNode(a0);
}

//  void QSGNodeUpdater::leaveTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater18leaveTransformNodeEP16QSGTransformNode(
    QSGNodeUpdater *self,
    QSGTransformNode *a0) {
  self->leaveTransformNode(a0);
}

//  void QSGNodeUpdater::enterClipNode(QSGClipNode *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater13enterClipNodeEP11QSGClipNode(
    QSGNodeUpdater *self,
    QSGClipNode *c) {
  self->enterClipNode(c);
}

//  void QSGNodeUpdater::leaveClipNode(QSGClipNode *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater13leaveClipNodeEP11QSGClipNode(
    QSGNodeUpdater *self,
    QSGClipNode *c) {
  self->leaveClipNode(c);
}

//  void QSGNodeUpdater::enterOpacityNode(QSGOpacityNode *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater16enterOpacityNodeEP14QSGOpacityNode(
    QSGNodeUpdater *self,
    QSGOpacityNode *o) {
  self->enterOpacityNode(o);
}

//  void QSGNodeUpdater::leaveOpacityNode(QSGOpacityNode *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater16leaveOpacityNodeEP14QSGOpacityNode(
    QSGNodeUpdater *self,
    QSGOpacityNode *o) {
  self->leaveOpacityNode(o);
}

//  void QSGNodeUpdater::enterGeometryNode(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater17enterGeometryNodeEP15QSGGeometryNode(
    QSGNodeUpdater *self,
    QSGGeometryNode *a0) {
  self->enterGeometryNode(a0);
}

//  void QSGNodeUpdater::leaveGeometryNode(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater17leaveGeometryNodeEP15QSGGeometryNode(
    QSGNodeUpdater *self,
    QSGGeometryNode *a0) {
  self->leaveGeometryNode(a0);
}

//  void QSGNodeUpdater::enterRenderNode(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater15enterRenderNodeEP13QSGRenderNode(
    QSGNodeUpdater *self,
    QSGRenderNode *a0) {
  self->enterRenderNode(a0);
}

//  void QSGNodeUpdater::leaveRenderNode(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater15leaveRenderNodeEP13QSGRenderNode(
    QSGNodeUpdater *self,
    QSGRenderNode *a0) {
  self->leaveRenderNode(a0);
}

//  void QSGNodeUpdater::visitNode(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater9visitNodeEP7QSGNode(
    QSGNodeUpdater *self,
    QSGNode *n) {
  self->visitNode(n);
}

//  void QSGNodeUpdater::visitChildren(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeUpdater13visitChildrenEP7QSGNode(
    QSGNodeUpdater *self,
    QSGNode *n) {
  self->visitChildren(n);
}

//  a Python function taken by a CuteQSGNodeUpdater, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGNodeUpdater(
    QSGNodeUpdater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGNodeUpdater *>(self)->take(key, call);
}

//  void QSGNodeUpdater::updateStates(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeUpdater12updateStatesEP7QSGNode(
    QSGNodeUpdater *self,
    QSGNode *n) {
  self->QSGNodeUpdater::updateStates(n);
}

//  bool QSGNodeUpdater::isNodeBlocked(QSGNode *n, QSGNode *root) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QSGNodeUpdater13isNodeBlockedEP7QSGNodeS1_(
    const QSGNodeUpdater *self,
    QSGNode *n,
    QSGNode *root) {
  return self->QSGNodeUpdater::isNodeBlocked(n, root);
}

//  void QSGNodeUpdater::enterTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeUpdater18enterTransformNodeEP16QSGTransformNode(
    QSGNodeUpdater *self,
    QSGTransformNode *a0) {
  static_cast<OwnQSGNodeUpdater *>(self)->OwnQSGNodeUpdater::enterTransformNode(
      a0);
}

//  void QSGNodeUpdater::leaveTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeUpdater18leaveTransformNodeEP16QSGTransformNode(
    QSGNodeUpdater *self,
    QSGTransformNode *a0) {
  static_cast<OwnQSGNodeUpdater *>(self)->OwnQSGNodeUpdater::leaveTransformNode(
      a0);
}
