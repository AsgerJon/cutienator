//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgnode.h>
#include <QtGui/qmatrix4x4.h>
#include <cstring>

//  A QSGTransformNode that Python can take functions over in. Every QSGTransformNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGTransformNodeCall0)(const void *, int *);
typedef void (*CuteQSGTransformNodeCall1)(const void *, int *);
class CuteQSGTransformNode : public QSGTransformNode {
public:
  using QSGTransformNode::QSGTransformNode;
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
      CuteQSGTransformNodeCall0 call = reinterpret_cast<CuteQSGTransformNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTransformNodeCall1 call = reinterpret_cast<CuteQSGTransformNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGTransformNode::QSGTransformNode()
extern "C" Q_DECL_EXPORT
QSGTransformNode *ritual_ZN16QSGTransformNodeC1Ev() {
  return new CuteQSGTransformNode();
}

//  QSGTransformNode::~QSGTransformNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGTransformNodeD1Ev(QSGTransformNode *self) {
  delete self;
}

//  void QSGTransformNode::setMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGTransformNode9setMatrixERK10QMatrix4x4(
    QSGTransformNode *self,
    const QMatrix4x4 *matrix) {
  self->setMatrix(*matrix);
}

//  const QMatrix4x4 &QSGTransformNode::matrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK16QSGTransformNode6matrixEv(
    const QSGTransformNode *self) {
  return new QMatrix4x4(self->matrix());
}

//  void QSGTransformNode::setCombinedMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGTransformNode17setCombinedMatrixERK10QMatrix4x4(
    QSGTransformNode *self,
    const QMatrix4x4 *matrix) {
  self->setCombinedMatrix(*matrix);
}

//  const QMatrix4x4 &QSGTransformNode::combinedMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK16QSGTransformNode14combinedMatrixEv(
    const QSGTransformNode *self) {
  return new QMatrix4x4(self->combinedMatrix());
}

//  a Python function taken by a CuteQSGTransformNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTransformNode(
    QSGTransformNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTransformNode *>(self)->take(key, call);
}
