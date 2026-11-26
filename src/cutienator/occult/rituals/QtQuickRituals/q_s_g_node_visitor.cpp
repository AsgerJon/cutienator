//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <cstring>

//  Only a class built on QSGNodeVisitor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSGNodeVisitor : QSGNodeVisitor {
  using QSGNodeVisitor::enterTransformNode;
  using QSGNodeVisitor::leaveTransformNode;
  using QSGNodeVisitor::enterClipNode;
  using QSGNodeVisitor::leaveClipNode;
  using QSGNodeVisitor::enterGeometryNode;
  using QSGNodeVisitor::leaveGeometryNode;
  using QSGNodeVisitor::enterOpacityNode;
  using QSGNodeVisitor::leaveOpacityNode;
  using QSGNodeVisitor::visitNode;
  using QSGNodeVisitor::visitChildren;
};

//  A QSGNodeVisitor that Python can take functions over in. Every QSGNodeVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGNodeVisitorCall0)(const void *, QSGTransformNode *, int *);
typedef void (*CuteQSGNodeVisitorCall1)(const void *, QSGTransformNode *, int *);
typedef void (*CuteQSGNodeVisitorCall2)(const void *, QSGClipNode *, int *);
typedef void (*CuteQSGNodeVisitorCall3)(const void *, QSGClipNode *, int *);
typedef void (*CuteQSGNodeVisitorCall4)(const void *, QSGGeometryNode *, int *);
typedef void (*CuteQSGNodeVisitorCall5)(const void *, QSGGeometryNode *, int *);
typedef void (*CuteQSGNodeVisitorCall6)(const void *, QSGOpacityNode *, int *);
typedef void (*CuteQSGNodeVisitorCall7)(const void *, QSGOpacityNode *, int *);
typedef void (*CuteQSGNodeVisitorCall8)(const void *, QSGNode *, int *);
typedef void (*CuteQSGNodeVisitorCall9)(const void *, QSGNode *, int *);
class CuteQSGNodeVisitor : public QSGNodeVisitor {
public:
  using QSGNodeVisitor::QSGNodeVisitor;
  CuteQSGNodeVisitor(const QSGNodeVisitor & other) : QSGNodeVisitor(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor18enterTransformNodeEP16QSGTransformNode")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor18leaveTransformNodeEP16QSGTransformNode")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor13enterClipNodeEP11QSGClipNode")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor13leaveClipNodeEP11QSGClipNode")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor17enterGeometryNodeEP15QSGGeometryNode")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor17leaveGeometryNodeEP15QSGGeometryNode")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor16enterOpacityNodeEP14QSGOpacityNode")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor16leaveOpacityNodeEP14QSGOpacityNode")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor9visitNodeEP7QSGNode")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGNodeVisitor13visitChildrenEP7QSGNode")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QSGNodeVisitor::enterTransformNode(QSGTransformNode *a0)
  void enterTransformNode(QSGTransformNode *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGNodeVisitorCall0 call = reinterpret_cast<CuteQSGNodeVisitorCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::enterTransformNode(a0);
  }

  //  void QSGNodeVisitor::leaveTransformNode(QSGTransformNode *a0)
  void leaveTransformNode(QSGTransformNode *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGNodeVisitorCall1 call = reinterpret_cast<CuteQSGNodeVisitorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::leaveTransformNode(a0);
  }

  //  void QSGNodeVisitor::enterClipNode(QSGClipNode *a0)
  void enterClipNode(QSGClipNode *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGNodeVisitorCall2 call = reinterpret_cast<CuteQSGNodeVisitorCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::enterClipNode(a0);
  }

  //  void QSGNodeVisitor::leaveClipNode(QSGClipNode *a0)
  void leaveClipNode(QSGClipNode *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGNodeVisitorCall3 call = reinterpret_cast<CuteQSGNodeVisitorCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::leaveClipNode(a0);
  }

  //  void QSGNodeVisitor::enterGeometryNode(QSGGeometryNode *a0)
  void enterGeometryNode(QSGGeometryNode *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGNodeVisitorCall4 call = reinterpret_cast<CuteQSGNodeVisitorCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::enterGeometryNode(a0);
  }

  //  void QSGNodeVisitor::leaveGeometryNode(QSGGeometryNode *a0)
  void leaveGeometryNode(QSGGeometryNode *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGNodeVisitorCall5 call = reinterpret_cast<CuteQSGNodeVisitorCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::leaveGeometryNode(a0);
  }

  //  void QSGNodeVisitor::enterOpacityNode(QSGOpacityNode *a0)
  void enterOpacityNode(QSGOpacityNode *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGNodeVisitorCall6 call = reinterpret_cast<CuteQSGNodeVisitorCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::enterOpacityNode(a0);
  }

  //  void QSGNodeVisitor::leaveOpacityNode(QSGOpacityNode *a0)
  void leaveOpacityNode(QSGOpacityNode *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGNodeVisitorCall7 call = reinterpret_cast<CuteQSGNodeVisitorCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::leaveOpacityNode(a0);
  }

  //  void QSGNodeVisitor::visitNode(QSGNode *n)
  void visitNode(QSGNode *n) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGNodeVisitorCall8 call = reinterpret_cast<CuteQSGNodeVisitorCall8>(taken[8]);
      call(this, n, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::visitNode(n);
  }

  //  void QSGNodeVisitor::visitChildren(QSGNode *n)
  void visitChildren(QSGNode *n) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGNodeVisitorCall9 call = reinterpret_cast<CuteQSGNodeVisitorCall9>(taken[9]);
      call(this, n, &handled);
      if (handled) return;
    }
    QSGNodeVisitor::visitChildren(n);
  }
};

//  QSGNodeVisitor::~QSGNodeVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitorD1Ev(QSGNodeVisitor *self) {
  delete self;
}

//  void QSGNodeVisitor::enterTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor18enterTransformNodeEP16QSGTransformNode(
    QSGNodeVisitor *self,
    QSGTransformNode *a0) {
  self->enterTransformNode(a0);
}

//  void QSGNodeVisitor::leaveTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor18leaveTransformNodeEP16QSGTransformNode(
    QSGNodeVisitor *self,
    QSGTransformNode *a0) {
  self->leaveTransformNode(a0);
}

//  void QSGNodeVisitor::enterClipNode(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor13enterClipNodeEP11QSGClipNode(
    QSGNodeVisitor *self,
    QSGClipNode *a0) {
  self->enterClipNode(a0);
}

//  void QSGNodeVisitor::leaveClipNode(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor13leaveClipNodeEP11QSGClipNode(
    QSGNodeVisitor *self,
    QSGClipNode *a0) {
  self->leaveClipNode(a0);
}

//  void QSGNodeVisitor::enterGeometryNode(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor17enterGeometryNodeEP15QSGGeometryNode(
    QSGNodeVisitor *self,
    QSGGeometryNode *a0) {
  self->enterGeometryNode(a0);
}

//  void QSGNodeVisitor::leaveGeometryNode(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor17leaveGeometryNodeEP15QSGGeometryNode(
    QSGNodeVisitor *self,
    QSGGeometryNode *a0) {
  self->leaveGeometryNode(a0);
}

//  void QSGNodeVisitor::enterOpacityNode(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor16enterOpacityNodeEP14QSGOpacityNode(
    QSGNodeVisitor *self,
    QSGOpacityNode *a0) {
  self->enterOpacityNode(a0);
}

//  void QSGNodeVisitor::leaveOpacityNode(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor16leaveOpacityNodeEP14QSGOpacityNode(
    QSGNodeVisitor *self,
    QSGOpacityNode *a0) {
  self->leaveOpacityNode(a0);
}

//  void QSGNodeVisitor::visitNode(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor9visitNodeEP7QSGNode(
    QSGNodeVisitor *self,
    QSGNode *n) {
  self->visitNode(n);
}

//  void QSGNodeVisitor::visitChildren(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGNodeVisitor13visitChildrenEP7QSGNode(
    QSGNodeVisitor *self,
    QSGNode *n) {
  self->visitChildren(n);
}

//  a Python function taken by a CuteQSGNodeVisitor, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGNodeVisitor(
    QSGNodeVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGNodeVisitor *>(self)->take(key, call);
}

//  void QSGNodeVisitor::enterTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor18enterTransformNodeEP16QSGTransformNode(
    QSGNodeVisitor *self,
    QSGTransformNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::enterTransformNode(
      a0);
}

//  void QSGNodeVisitor::leaveTransformNode(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor18leaveTransformNodeEP16QSGTransformNode(
    QSGNodeVisitor *self,
    QSGTransformNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::leaveTransformNode(
      a0);
}

//  void QSGNodeVisitor::enterClipNode(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor13enterClipNodeEP11QSGClipNode(
    QSGNodeVisitor *self,
    QSGClipNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::enterClipNode(
      a0);
}

//  void QSGNodeVisitor::leaveClipNode(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor13leaveClipNodeEP11QSGClipNode(
    QSGNodeVisitor *self,
    QSGClipNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::leaveClipNode(
      a0);
}

//  void QSGNodeVisitor::enterGeometryNode(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor17enterGeometryNodeEP15QSGGeometryNode(
    QSGNodeVisitor *self,
    QSGGeometryNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::enterGeometryNode(
      a0);
}

//  void QSGNodeVisitor::leaveGeometryNode(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor17leaveGeometryNodeEP15QSGGeometryNode(
    QSGNodeVisitor *self,
    QSGGeometryNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::leaveGeometryNode(
      a0);
}

//  void QSGNodeVisitor::enterOpacityNode(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor16enterOpacityNodeEP14QSGOpacityNode(
    QSGNodeVisitor *self,
    QSGOpacityNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::enterOpacityNode(
      a0);
}

//  void QSGNodeVisitor::leaveOpacityNode(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor16leaveOpacityNodeEP14QSGOpacityNode(
    QSGNodeVisitor *self,
    QSGOpacityNode *a0) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::leaveOpacityNode(
      a0);
}

//  void QSGNodeVisitor::visitNode(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor9visitNodeEP7QSGNode(
    QSGNodeVisitor *self,
    QSGNode *n) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::visitNode(n);
}

//  void QSGNodeVisitor::visitChildren(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGNodeVisitor13visitChildrenEP7QSGNode(
    QSGNodeVisitor *self,
    QSGNode *n) {
  static_cast<OwnQSGNodeVisitor *>(self)->OwnQSGNodeVisitor::visitChildren(
      n);
}
