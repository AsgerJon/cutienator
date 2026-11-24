//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A QSGInternalImageNode that Python can take functions over in. Every QSGInternalImageNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGInternalImageNodeCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQSGInternalImageNodeCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQSGInternalImageNodeCall2)(const void *, const QRectF *, int *);
typedef void (*CuteQSGInternalImageNodeCall3)(const void *, const QRectF *, int *);
typedef void (*CuteQSGInternalImageNodeCall4)(const void *, QSGTexture *, int *);
typedef void (*CuteQSGInternalImageNodeCall5)(const void *, bool, int *);
typedef void (*CuteQSGInternalImageNodeCall6)(const void *, bool, bool, int *);
typedef void (*CuteQSGInternalImageNodeCall7)(const void *, int, int *);
typedef void (*CuteQSGInternalImageNodeCall8)(const void *, int, int *);
typedef void (*CuteQSGInternalImageNodeCall9)(const void *, int, int *);
typedef void (*CuteQSGInternalImageNodeCall10)(const void *, int, int *);
typedef void (*CuteQSGInternalImageNodeCall11)(const void *, int *);
typedef void (*CuteQSGInternalImageNodeCall12)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGInternalImageNodeCall13)(const void *, int *);
typedef void (*CuteQSGInternalImageNodeCall14)(const void *, int *);
class CuteQSGInternalImageNode : public QSGInternalImageNode {
public:
  using QSGInternalImageNode::QSGInternalImageNode;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode13setTargetRectERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode18setInnerTargetRectERK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode18setInnerSourceRectERK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode16setSubSourceRectERK6QRectF")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode10setTextureEP10QSGTexture")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode15setAntialiasingEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode9setMirrorEbb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode6updateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[14] = call;
      return true;
    }
    return false;
  }

  //  void QSGInternalImageNode::setTargetRect(const QRectF &rect)
  void setTargetRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall0 call = reinterpret_cast<CuteQSGInternalImageNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setInnerTargetRect(const QRectF &rect)
  void setInnerTargetRect(const QRectF &rect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall1 call = reinterpret_cast<CuteQSGInternalImageNodeCall1>(taken[1]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setInnerSourceRect(const QRectF &rect)
  void setInnerSourceRect(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall2 call = reinterpret_cast<CuteQSGInternalImageNodeCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setSubSourceRect(const QRectF &rect)
  void setSubSourceRect(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall3 call = reinterpret_cast<CuteQSGInternalImageNodeCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall4 call = reinterpret_cast<CuteQSGInternalImageNodeCall4>(taken[4]);
      call(this, texture, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setAntialiasing(bool antialiasing)
  void setAntialiasing(bool antialiasing) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall5 call = reinterpret_cast<CuteQSGInternalImageNodeCall5>(taken[5]);
      call(this, antialiasing, &handled);
      if (handled) return;
    }
    QSGInternalImageNode::setAntialiasing(antialiasing);
  }

  //  void QSGInternalImageNode::setMirror(bool horizontally, bool
  //      vertically)
  void setMirror(bool horizontally, bool vertically) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall6 call = reinterpret_cast<CuteQSGInternalImageNodeCall6>(taken[6]);
      call(this, horizontally, vertically, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
  //      filtering)
  void setMipmapFiltering(QSGTexture::Filtering filtering) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall7 call = reinterpret_cast<CuteQSGInternalImageNodeCall7>(taken[7]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall8 call = reinterpret_cast<CuteQSGInternalImageNodeCall8>(taken[8]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
  //      wrapMode)
  void setHorizontalWrapMode(QSGTexture::WrapMode wrapMode) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall9 call = reinterpret_cast<CuteQSGInternalImageNodeCall9>(taken[9]);
      call(this, static_cast<int>(wrapMode), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
  //      wrapMode)
  void setVerticalWrapMode(QSGTexture::WrapMode wrapMode) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall10 call = reinterpret_cast<CuteQSGInternalImageNodeCall10>(taken[10]);
      call(this, static_cast<int>(wrapMode), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::update()
  void update() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall11 call = reinterpret_cast<CuteQSGInternalImageNodeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall12 call = reinterpret_cast<CuteQSGInternalImageNodeCall12>(taken[12]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGInternalImageNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall13 call = reinterpret_cast<CuteQSGInternalImageNodeCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGInternalImageNodeCall14 call = reinterpret_cast<CuteQSGInternalImageNodeCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGInternalImageNode::~QSGInternalImageNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNodeD1Ev(QSGInternalImageNode *self) {
  delete self;
}

//  void QSGInternalImageNode::setTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode13setTargetRectERK6QRectF(
    QSGInternalImageNode *self,
    const QRectF *rect) {
  self->setTargetRect(*rect);
}

//  void QSGInternalImageNode::setInnerTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode18setInnerTargetRectERK6QRectF(
    QSGInternalImageNode *self,
    const QRectF *rect) {
  self->setInnerTargetRect(*rect);
}

//  void QSGInternalImageNode::setInnerSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode18setInnerSourceRectERK6QRectF(
    QSGInternalImageNode *self,
    const QRectF *rect) {
  self->setInnerSourceRect(*rect);
}

//  void QSGInternalImageNode::setSubSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode16setSubSourceRectERK6QRectF(
    QSGInternalImageNode *self,
    const QRectF *rect) {
  self->setSubSourceRect(*rect);
}

//  void QSGInternalImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode10setTextureEP10QSGTexture(
    QSGInternalImageNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGInternalImageNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode15setAntialiasingEb(
    QSGInternalImageNode *self,
    bool antialiasing) {
  self->setAntialiasing(antialiasing);
}

//  void QSGInternalImageNode::setMirror(bool horizontally, bool vertically)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode9setMirrorEbb(
    QSGInternalImageNode *self,
    bool horizontally,
    bool vertically) {
  self->setMirror(horizontally, vertically);
}

//  void QSGInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setMipmapFiltering(filtering);
}

//  void QSGInternalImageNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  void QSGInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
//      wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE(
    QSGInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->setHorizontalWrapMode(wrapMode);
}

//  void QSGInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
//      wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE(
    QSGInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->setVerticalWrapMode(wrapMode);
}

//  void QSGInternalImageNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode6updateEv(QSGInternalImageNode *self) {
  self->update();
}

//  void QSGInternalImageNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGInternalImageNode6acceptEP16QSGNodeVisitorEx(
    QSGInternalImageNode *self,
    QSGNodeVisitorEx *visitor) {
  self->accept(visitor);
}

//  a Python function taken by a CuteQSGInternalImageNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGInternalImageNode(
    QSGInternalImageNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGInternalImageNode *>(self)->take(key, call);
}

//  void QSGInternalImageNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGInternalImageNode15setAntialiasingEb(
    QSGInternalImageNode *self,
    bool antialiasing) {
  self->QSGInternalImageNode::setAntialiasing(antialiasing);
}

//  void QSGInternalImageNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGInternalImageNode6acceptEP16QSGNodeVisitorEx(
    QSGInternalImageNode *self,
    QSGNodeVisitorEx *visitor) {
  self->QSGInternalImageNode::accept(visitor);
}
