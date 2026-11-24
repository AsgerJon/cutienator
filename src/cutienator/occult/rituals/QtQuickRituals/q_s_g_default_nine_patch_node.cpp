//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultninepatchnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultninepatchnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGDefaultNinePatchNode that Python can take functions over in. Every QSGDefaultNinePatchNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGDefaultNinePatchNodeCall0)(const void *, QSGTexture *, int *);
typedef void (*CuteQSGDefaultNinePatchNodeCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQSGDefaultNinePatchNodeCall2)(const void *, qreal, int *);
typedef void (*CuteQSGDefaultNinePatchNodeCall3)(const void *, qreal, qreal, qreal, qreal, int *);
typedef void (*CuteQSGDefaultNinePatchNodeCall4)(const void *, int *);
typedef bool (*CuteQSGDefaultNinePatchNodeCall5)(const void *, int *);
typedef void (*CuteQSGDefaultNinePatchNodeCall6)(const void *, int *);
class CuteQSGDefaultNinePatchNode : public QSGDefaultNinePatchNode {
public:
  using QSGDefaultNinePatchNode::QSGDefaultNinePatchNode;
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

  //  void QSGDefaultNinePatchNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall0 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall0>(taken[0]);
      call(this, texture, &handled);
      if (handled) return;
    }
    QSGDefaultNinePatchNode::setTexture(texture);
  }

  //  void QSGDefaultNinePatchNode::setBounds(const QRectF &bounds)
  void setBounds(const QRectF &bounds) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall1 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall1>(taken[1]);
      call(this, &bounds, &handled);
      if (handled) return;
    }
    QSGDefaultNinePatchNode::setBounds(bounds);
  }

  //  void QSGDefaultNinePatchNode::setDevicePixelRatio(qreal ratio)
  void setDevicePixelRatio(qreal ratio) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall2 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall2>(taken[2]);
      call(this, ratio, &handled);
      if (handled) return;
    }
    QSGDefaultNinePatchNode::setDevicePixelRatio(ratio);
  }

  //  void QSGDefaultNinePatchNode::setPadding(qreal left, qreal top, qreal
  //      right, qreal bottom)
  void setPadding(
      qreal left,
      qreal top,
      qreal right,
      qreal bottom) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall3 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall3>(taken[3]);
      call(this, left, top, right, bottom, &handled);
      if (handled) return;
    }
    QSGDefaultNinePatchNode::setPadding(left, top, right, bottom);
  }

  //  void QSGDefaultNinePatchNode::update()
  void update() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall4 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultNinePatchNode::update();
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall5 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDefaultNinePatchNodeCall6 call = reinterpret_cast<CuteQSGDefaultNinePatchNodeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGDefaultNinePatchNode::QSGDefaultNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGDefaultNinePatchNode *ritual_ZN23QSGDefaultNinePatchNodeC1Ev() {
  return new CuteQSGDefaultNinePatchNode();
}

//  QSGDefaultNinePatchNode::~QSGDefaultNinePatchNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultNinePatchNodeD1Ev(QSGDefaultNinePatchNode *self) {
  delete self;
}

//  void QSGDefaultNinePatchNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultNinePatchNode10setTextureEP10QSGTexture(
    QSGDefaultNinePatchNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGDefaultNinePatchNode::setBounds(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultNinePatchNode9setBoundsERK6QRectF(
    QSGDefaultNinePatchNode *self,
    const QRectF *bounds) {
  self->setBounds(*bounds);
}

//  void QSGDefaultNinePatchNode::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultNinePatchNode19setDevicePixelRatioEd(
    QSGDefaultNinePatchNode *self,
    qreal ratio) {
  self->setDevicePixelRatio(ratio);
}

//  void QSGDefaultNinePatchNode::setPadding(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultNinePatchNode10setPaddingEdddd(
    QSGDefaultNinePatchNode *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->setPadding(left, top, right, bottom);
}

//  void QSGDefaultNinePatchNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGDefaultNinePatchNode6updateEv(
    QSGDefaultNinePatchNode *self) {
  self->update();
}

//  a Python function taken by a CuteQSGDefaultNinePatchNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDefaultNinePatchNode(
    QSGDefaultNinePatchNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDefaultNinePatchNode *>(self)->take(key, call);
}

//  void QSGDefaultNinePatchNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultNinePatchNode10setTextureEP10QSGTexture(
    QSGDefaultNinePatchNode *self,
    QSGTexture *texture) {
  self->QSGDefaultNinePatchNode::setTexture(texture);
}

//  void QSGDefaultNinePatchNode::setBounds(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultNinePatchNode9setBoundsERK6QRectF(
    QSGDefaultNinePatchNode *self,
    const QRectF *bounds) {
  self->QSGDefaultNinePatchNode::setBounds(*bounds);
}

//  void QSGDefaultNinePatchNode::setDevicePixelRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultNinePatchNode19setDevicePixelRatioEd(
    QSGDefaultNinePatchNode *self,
    qreal ratio) {
  self->QSGDefaultNinePatchNode::setDevicePixelRatio(ratio);
}

//  void QSGDefaultNinePatchNode::setPadding(qreal left, qreal top, qreal
//      right, qreal bottom)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultNinePatchNode10setPaddingEdddd(
    QSGDefaultNinePatchNode *self,
    qreal left,
    qreal top,
    qreal right,
    qreal bottom) {
  self->QSGDefaultNinePatchNode::setPadding(left, top, right, bottom);
}

//  void QSGDefaultNinePatchNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGDefaultNinePatchNode6updateEv(
    QSGDefaultNinePatchNode *self) {
  self->QSGDefaultNinePatchNode::update();
}
