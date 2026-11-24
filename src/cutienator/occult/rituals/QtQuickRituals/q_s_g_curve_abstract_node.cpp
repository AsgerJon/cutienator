//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcurveabstractnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurveabstractnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <cstring>

//  A QSGCurveAbstractNode that Python can take functions over in. Every QSGCurveAbstractNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGCurveAbstractNodeCall0)(const void *, const QColor *, int *);
typedef void (*CuteQSGCurveAbstractNodeCall1)(const void *, int *);
typedef void (*CuteQSGCurveAbstractNodeCall2)(const void *, bool, int *);
typedef bool (*CuteQSGCurveAbstractNodeCall3)(const void *, int *);
typedef void (*CuteQSGCurveAbstractNodeCall4)(const void *, int *);
class CuteQSGCurveAbstractNode : public QSGCurveAbstractNode {
public:
  using QSGCurveAbstractNode::QSGCurveAbstractNode;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QSGCurveAbstractNode8setColorE6QColor")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGCurveAbstractNode12cookGeometryEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGCurveAbstractNode25setUseStandardDerivativesEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QSGCurveAbstractNode::setColor(QColor col)
  void setColor(QColor col) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGCurveAbstractNodeCall0 call = reinterpret_cast<CuteQSGCurveAbstractNodeCall0>(taken[0]);
      call(this, &col, &handled);
      if (handled) return;
    }
  }

  //  void QSGCurveAbstractNode::cookGeometry()
  void cookGeometry() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGCurveAbstractNodeCall1 call = reinterpret_cast<CuteQSGCurveAbstractNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGCurveAbstractNode::setUseStandardDerivatives(bool
  //      useStandardDerivatives)
  void setUseStandardDerivatives(bool useStandardDerivatives) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGCurveAbstractNodeCall2 call = reinterpret_cast<CuteQSGCurveAbstractNodeCall2>(taken[2]);
      call(this, useStandardDerivatives, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGCurveAbstractNodeCall3 call = reinterpret_cast<CuteQSGCurveAbstractNodeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGCurveAbstractNodeCall4 call = reinterpret_cast<CuteQSGCurveAbstractNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  void QSGCurveAbstractNode::setColor(QColor col)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCurveAbstractNode8setColorE6QColor(
    QSGCurveAbstractNode *self,
    const QColor *col) {
  self->setColor(*col);
}

//  void QSGCurveAbstractNode::cookGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCurveAbstractNode12cookGeometryEv(
    QSGCurveAbstractNode *self) {
  self->cookGeometry();
}

//  void QSGCurveAbstractNode::setUseStandardDerivatives(bool
//      useStandardDerivatives)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGCurveAbstractNode25setUseStandardDerivativesEb(
    QSGCurveAbstractNode *self,
    bool useStandardDerivatives) {
  self->setUseStandardDerivatives(useStandardDerivatives);
}

//  a Python function taken by a CuteQSGCurveAbstractNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGCurveAbstractNode(
    QSGCurveAbstractNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGCurveAbstractNode *>(self)->take(key, call);
}
