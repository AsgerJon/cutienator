//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideonode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qsgvideonode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSGVideoNode that Python can take functions over in. Every QSGVideoNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGVideoNodeCall0)(const void *, int *);
typedef void (*CuteQSGVideoNodeCall1)(const void *, int *);
class CuteQSGVideoNode : public QSGVideoNode {
public:
  using QSGVideoNode::QSGVideoNode;
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
      CuteQSGVideoNodeCall0 call = reinterpret_cast<CuteQSGVideoNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGVideoNodeCall1 call = reinterpret_cast<CuteQSGVideoNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGVideoNode::~QSGVideoNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSGVideoNodeD1Ev(QSGVideoNode *self) {
  delete self;
}

//  QVideoFrameFormat::PixelFormat QSGVideoNode::pixelFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZNK12QSGVideoNode11pixelFormatEv(
    const QSGVideoNode *self) {
  return self->pixelFormat();
}

//  a Python function taken by a CuteQSGVideoNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGVideoNode(
    QSGVideoNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGVideoNode *>(self)->take(key, call);
}
