//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbasicinternalimagenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbasicinternalimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QSGBasicInternalImageNode that Python can take functions over in. Every QSGBasicInternalImageNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGBasicInternalImageNodeCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall2)(const void *, const QRectF *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall3)(const void *, const QRectF *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall4)(const void *, QSGTexture *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall5)(const void *, bool, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall6)(const void *, bool, bool, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall7)(const void *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall8)(const void *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall9)(const void *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall10)(const void *, QSGTexture *, int *);
typedef void * (*CuteQSGBasicInternalImageNodeCall11)(const void *, int *);
typedef bool (*CuteQSGBasicInternalImageNodeCall12)(const void *, int *);
typedef bool (*CuteQSGBasicInternalImageNodeCall13)(const void *, const QSize *, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall14)(const void *, int, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall15)(const void *, int, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall16)(const void *, int, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall17)(const void *, int, int *);
typedef void (*CuteQSGBasicInternalImageNodeCall18)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGBasicInternalImageNodeCall19)(const void *, int *);
class CuteQSGBasicInternalImageNode : public QSGBasicInternalImageNode {
public:
  using QSGBasicInternalImageNode::QSGBasicInternalImageNode;
  void *taken[20] = {};

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
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode6updateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSGBasicInternalImageNode26updateMaterialAntialiasingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSGBasicInternalImageNode18setMaterialTextureEP10QSGTexture")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QSGBasicInternalImageNode15materialTextureEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSGBasicInternalImageNode22updateMaterialBlendingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QSGBasicInternalImageNode12supportsWrapERK5QSize")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QSGInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  void QSGBasicInternalImageNode::setTargetRect(const QRectF &rect)
  void setTargetRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall0 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setTargetRect(rect);
  }

  //  void QSGBasicInternalImageNode::setInnerTargetRect(const QRectF
  //      &rect)
  void setInnerTargetRect(const QRectF &rect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall1 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall1>(taken[1]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setInnerTargetRect(rect);
  }

  //  void QSGBasicInternalImageNode::setInnerSourceRect(const QRectF
  //      &rect)
  void setInnerSourceRect(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall2 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setInnerSourceRect(rect);
  }

  //  void QSGBasicInternalImageNode::setSubSourceRect(const QRectF &rect)
  void setSubSourceRect(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall3 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setSubSourceRect(rect);
  }

  //  void QSGBasicInternalImageNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall4 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall4>(taken[4]);
      call(this, texture, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setTexture(texture);
  }

  //  void QSGBasicInternalImageNode::setAntialiasing(bool antialiasing)
  void setAntialiasing(bool antialiasing) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall5 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall5>(taken[5]);
      call(this, antialiasing, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setAntialiasing(antialiasing);
  }

  //  void QSGBasicInternalImageNode::setMirror(bool mirrorHorizontally,
  //      bool mirrorVertically)
  void setMirror(bool mirrorHorizontally, bool mirrorVertically) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall6 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall6>(taken[6]);
      call(this, mirrorHorizontally, mirrorVertically, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::setMirror(mirrorHorizontally, mirrorVertically);
  }

  //  void QSGBasicInternalImageNode::update()
  void update() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall7 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::update();
  }

  //  void QSGBasicInternalImageNode::preprocess()
  void preprocess() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall8 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGBasicInternalImageNode::preprocess();
  }

  //  void QSGBasicInternalImageNode::updateMaterialAntialiasing()
  void updateMaterialAntialiasing() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall9 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSGBasicInternalImageNode::setMaterialTexture(QSGTexture
  //      *texture)
  void setMaterialTexture(QSGTexture *texture) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall10 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall10>(taken[10]);
      call(this, texture, &handled);
      if (handled) return;
    }
  }

  //  QSGTexture *QSGBasicInternalImageNode::materialTexture() const
  QSGTexture *materialTexture() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall11 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return {};
  }

  //  bool QSGBasicInternalImageNode::updateMaterialBlending()
  bool updateMaterialBlending() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall12 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSGBasicInternalImageNode::supportsWrap(const QSize &size) const
  bool supportsWrap(const QSize &size) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall13 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall13>(taken[13]);
      bool given = call(this, &size, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QSGInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
  //      filtering)
  void setMipmapFiltering(QSGTexture::Filtering filtering) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall14 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall14>(taken[14]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall15 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall15>(taken[15]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
  //      wrapMode)
  void setHorizontalWrapMode(QSGTexture::WrapMode wrapMode) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall16 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall16>(taken[16]);
      call(this, static_cast<int>(wrapMode), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
  //      wrapMode)
  void setVerticalWrapMode(QSGTexture::WrapMode wrapMode) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall17 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall17>(taken[17]);
      call(this, static_cast<int>(wrapMode), &handled);
      if (handled) return;
    }
  }

  //  void QSGInternalImageNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall18 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall18>(taken[18]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGInternalImageNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGBasicInternalImageNodeCall19 call = reinterpret_cast<CuteQSGBasicInternalImageNodeCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }
};

//  QSGBasicInternalImageNode::QSGBasicInternalImageNode()
extern "C" Q_DECL_EXPORT
QSGBasicInternalImageNode *ritual_ZN25QSGBasicInternalImageNodeC1Ev() {
  return new CuteQSGBasicInternalImageNode();
}

//  void QSGBasicInternalImageNode::setTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode13setTargetRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->setTargetRect(*rect);
}

//  void QSGBasicInternalImageNode::setInnerTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode18setInnerTargetRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->setInnerTargetRect(*rect);
}

//  void QSGBasicInternalImageNode::setInnerSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode18setInnerSourceRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->setInnerSourceRect(*rect);
}

//  void QSGBasicInternalImageNode::setSubSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode16setSubSourceRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->setSubSourceRect(*rect);
}

//  void QSGBasicInternalImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode10setTextureEP10QSGTexture(
    QSGBasicInternalImageNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGBasicInternalImageNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode15setAntialiasingEb(
    QSGBasicInternalImageNode *self,
    bool antialiasing) {
  self->setAntialiasing(antialiasing);
}

//  void QSGBasicInternalImageNode::setMirror(bool mirrorHorizontally, bool
//      mirrorVertically)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode9setMirrorEbb(
    QSGBasicInternalImageNode *self,
    bool mirrorHorizontally,
    bool mirrorVertically) {
  self->setMirror(mirrorHorizontally, mirrorVertically);
}

//  void QSGBasicInternalImageNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode6updateEv(
    QSGBasicInternalImageNode *self) {
  self->update();
}

//  void QSGBasicInternalImageNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode10preprocessEv(
    QSGBasicInternalImageNode *self) {
  self->preprocess();
}

//  QSGGeometry *QSGBasicInternalImageNode::updateGeometry(const QRectF
//      &targetRect, const QRectF &innerTargetRect, const QRectF &sourceRect,
//      const QRectF &innerSourceRect, const QRectF &subSourceRect,
//      QSGGeometry *geometry, bool mirrorHorizontally, bool
//      mirrorVertically, bool antialiasing)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN25QSGBasicInternalImageNode14updateGeometryERK6QRectFS2_S2_S2_S2_P11QSGGeometrybbb(
    const QRectF *targetRect,
    const QRectF *innerTargetRect,
    const QRectF *sourceRect,
    const QRectF *innerSourceRect,
    const QRectF *subSourceRect,
    QSGGeometry *geometry,
    bool mirrorHorizontally,
    bool mirrorVertically,
    bool antialiasing) {
  return QSGBasicInternalImageNode::updateGeometry(
      *targetRect,
      *innerTargetRect,
      *sourceRect,
      *innerSourceRect,
      *subSourceRect,
      geometry,
      mirrorHorizontally,
      mirrorVertically,
      antialiasing);
}

//  void QSGBasicInternalImageNode::updateMaterialAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode26updateMaterialAntialiasingEv(
    QSGBasicInternalImageNode *self) {
  self->updateMaterialAntialiasing();
}

//  void QSGBasicInternalImageNode::setMaterialTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode18setMaterialTextureEP10QSGTexture(
    QSGBasicInternalImageNode *self,
    QSGTexture *texture) {
  self->setMaterialTexture(texture);
}

//  QSGTexture *QSGBasicInternalImageNode::materialTexture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK25QSGBasicInternalImageNode15materialTextureEv(
    const QSGBasicInternalImageNode *self) {
  return self->materialTexture();
}

//  bool QSGBasicInternalImageNode::updateMaterialBlending()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSGBasicInternalImageNode22updateMaterialBlendingEv(
    QSGBasicInternalImageNode *self) {
  return self->updateMaterialBlending();
}

//  bool QSGBasicInternalImageNode::supportsWrap(const QSize &size) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QSGBasicInternalImageNode12supportsWrapERK5QSize(
    const QSGBasicInternalImageNode *self,
    const QSize *size) {
  return self->supportsWrap(*size);
}

//  void QSGBasicInternalImageNode::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGBasicInternalImageNode14updateGeometryEv(
    QSGBasicInternalImageNode *self) {
  self->updateGeometry();
}

//  a Python function taken by a CuteQSGBasicInternalImageNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGBasicInternalImageNode(
    QSGBasicInternalImageNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGBasicInternalImageNode *>(self)->take(key, call);
}

//  void QSGBasicInternalImageNode::setTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode13setTargetRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->QSGBasicInternalImageNode::setTargetRect(*rect);
}

//  void QSGBasicInternalImageNode::setInnerTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode18setInnerTargetRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->QSGBasicInternalImageNode::setInnerTargetRect(*rect);
}

//  void QSGBasicInternalImageNode::setInnerSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode18setInnerSourceRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->QSGBasicInternalImageNode::setInnerSourceRect(*rect);
}

//  void QSGBasicInternalImageNode::setSubSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode16setSubSourceRectERK6QRectF(
    QSGBasicInternalImageNode *self,
    const QRectF *rect) {
  self->QSGBasicInternalImageNode::setSubSourceRect(*rect);
}

//  void QSGBasicInternalImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode10setTextureEP10QSGTexture(
    QSGBasicInternalImageNode *self,
    QSGTexture *texture) {
  self->QSGBasicInternalImageNode::setTexture(texture);
}

//  void QSGBasicInternalImageNode::setAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode15setAntialiasingEb(
    QSGBasicInternalImageNode *self,
    bool antialiasing) {
  self->QSGBasicInternalImageNode::setAntialiasing(antialiasing);
}

//  void QSGBasicInternalImageNode::setMirror(bool mirrorHorizontally, bool
//      mirrorVertically)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode9setMirrorEbb(
    QSGBasicInternalImageNode *self,
    bool mirrorHorizontally,
    bool mirrorVertically) {
  self->QSGBasicInternalImageNode::setMirror(
      mirrorHorizontally,
      mirrorVertically);
}

//  void QSGBasicInternalImageNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode6updateEv(
    QSGBasicInternalImageNode *self) {
  self->QSGBasicInternalImageNode::update();
}

//  void QSGBasicInternalImageNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGBasicInternalImageNode10preprocessEv(
    QSGBasicInternalImageNode *self) {
  self->QSGBasicInternalImageNode::preprocess();
}
