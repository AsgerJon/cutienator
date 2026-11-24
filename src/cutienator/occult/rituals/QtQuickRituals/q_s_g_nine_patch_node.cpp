//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgninepatchnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgninepatchnode.h>
#include <QtCore/qrect.h>
#include <QtGui/qvectornd.h>
#include <cstring>

//  A QSGNinePatchNode that Python can take functions over in. Every QSGNinePatchNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGNinePatchNodeCall0)(const void *, QSGTexture *, int *);
typedef void (*CuteQSGNinePatchNodeCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQSGNinePatchNodeCall2)(const void *, qreal, int *);
typedef void (*CuteQSGNinePatchNodeCall3)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteQSGNinePatchNodeCall4)(const void *, int *);
typedef bool (*CuteQSGNinePatchNodeCall5)(const void *, int *);
typedef void (*CuteQSGNinePatchNodeCall6)(const void *, int *);
class CuteQSGNinePatchNode : public QSGNinePatchNode {
public:
  using QSGNinePatchNode::QSGNinePatchNode;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGNinePatchNode10setTextureEP10QSGTexture")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNinePatchNode9setBoundsERK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNinePatchNode19setDevicePixelRatioEd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNinePatchNode10setPaddingEdddd")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGNinePatchNode6updateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QSGNinePatchNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall0 call = reinterpret_cast<CuteQSGNinePatchNodeCall0>(taken[0]);
      call(this, texture, &handled);
      if (handled) return;
    }
  }

  //  void QSGNinePatchNode::setBounds(const QRectF &bounds)
  void setBounds(const QRectF &bounds) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall1 call = reinterpret_cast<CuteQSGNinePatchNodeCall1>(taken[1]);
      call(this, &bounds, &handled);
      if (handled) return;
    }
  }

  //  void QSGNinePatchNode::setDevicePixelRatio(qreal ratio)
  void setDevicePixelRatio(qreal ratio) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall2 call = reinterpret_cast<CuteQSGNinePatchNodeCall2>(taken[2]);
      call(this, ratio, &handled);
      if (handled) return;
    }
  }

  //  void QSGNinePatchNode::setPadding(qreal left, qreal top, qreal right,
  //      qreal bottom)
  void setPadding(
      qreal left,
      qreal top,
      qreal right,
      qreal bottom) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall3 call = reinterpret_cast<CuteQSGNinePatchNodeCall3>(taken[3]);
      call(this, left, top, right, bottom, &handled);
      if (handled) return;
    }
  }

  //  void QSGNinePatchNode::update()
  void update() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall4 call = reinterpret_cast<CuteQSGNinePatchNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall5 call = reinterpret_cast<CuteQSGNinePatchNodeCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGNinePatchNodeCall6 call = reinterpret_cast<CuteQSGNinePatchNodeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGNinePatchNode::~QSGNinePatchNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNodeD1Ev(QSGNinePatchNode *self) {
  delete self;
}

//  void QSGNinePatchNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNode10setTextureEP10QSGTexture(
    QSGNinePatchNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGNinePatchNode::setBounds(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNode9setBoundsERK6QRectF(
    QSGNinePatchNode *self,
    const QRectF *bounds) {
  self->setBounds(*bounds);
}

//  void QSGNinePatchNode::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNode19setDevicePixelRatioEd(
    QSGNinePatchNode *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  void QSGNinePatchNode::setPadding(qreal left, qreal top, qreal right,
//      qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNode10setPaddingEdddd(
    QSGNinePatchNode *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setPadding(left, top, right, bottom);
}

//  void QSGNinePatchNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNode6updateEv(QSGNinePatchNode *self) {
  self->update();
}

//  void QSGNinePatchNode::rebuildGeometry(QSGTexture *texture, QSGGeometry
//      *geometry, const QVector4D &padding, const QRectF &bounds, qreal dpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGNinePatchNode15rebuildGeometryEP10QSGTextureP11QSGGeometryRK9QVector4DRK6QRectFd(
    QSGTexture *texture,
    QSGGeometry *geometry,
    const QVector4D *padding,
    const QRectF *bounds,
    qreal dpr) {
  QSGNinePatchNode::rebuildGeometry(
      texture,
      geometry,
      *padding,
      *bounds,
      dpr);
}

//  a Python function taken by a CuteQSGNinePatchNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGNinePatchNode(
    QSGNinePatchNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGNinePatchNode *>(self)->take(key, call);
}
