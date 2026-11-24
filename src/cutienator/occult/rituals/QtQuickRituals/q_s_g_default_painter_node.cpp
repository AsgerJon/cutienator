//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultpainternode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultpainternode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QSGDefaultPainterNode that Python can take functions over in. Every QSGDefaultPainterNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGDefaultPainterNodeCall0)(const void *, int, int *);
typedef void (*CuteQSGDefaultPainterNodeCall1)(const void *, const QSize *, int *);
typedef void (*CuteQSGDefaultPainterNodeCall2)(const void *, const QRect *, int *);
typedef void (*CuteQSGDefaultPainterNodeCall3)(const void *, bool, int *);
typedef void (*CuteQSGDefaultPainterNodeCall4)(const void *, bool, int *);
typedef void (*CuteQSGDefaultPainterNodeCall5)(const void *, bool, int *);
typedef void (*CuteQSGDefaultPainterNodeCall6)(const void *, bool, int *);
typedef void (*CuteQSGDefaultPainterNodeCall7)(const void *, const QColor *, int *);
typedef void (*CuteQSGDefaultPainterNodeCall8)(const void *, qreal, int *);
typedef void (*CuteQSGDefaultPainterNodeCall9)(const void *, bool, int *);
typedef void (*CuteQSGDefaultPainterNodeCall10)(const void *, const QSize *, int *);
typedef const QImage * (*CuteQSGDefaultPainterNodeCall11)(const void *, int *);
typedef void (*CuteQSGDefaultPainterNodeCall12)(const void *, int *);
typedef void * (*CuteQSGDefaultPainterNodeCall13)(const void *, int *);
typedef void (*CuteQSGDefaultPainterNodeCall14)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGDefaultPainterNodeCall15)(const void *, int *);
typedef void (*CuteQSGDefaultPainterNodeCall16)(const void *, int *);
class CuteQSGDefaultPainterNode : public QSGDefaultPainterNode {
public:
  using QSGDefaultPainterNode::QSGDefaultPainterNode;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QSGPainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode7setSizeERK5QSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode8setDirtyERK5QRect")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode17setOpaquePaintingEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode18setLinearFilteringEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode13setMipmappingEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode17setSmoothPaintingEb")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode12setFillColorERK6QColor")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode16setContentsScaleEd")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode18setFastFBOResizingEb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode14setTextureSizeERK5QSize")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QSGPainterNode7toImageEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode6updateEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QSGPainterNode7textureEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[16] = call;
      return true;
    }
    return false;
  }

  //  void QSGDefaultPainterNode::setPreferredRenderTarget(QQuickPaintedIte
  //      m::RenderTarget target)
  void setPreferredRenderTarget(
      QQuickPaintedItem::RenderTarget target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall0 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall0>(taken[0]);
      call(this, static_cast<int>(target), &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setPreferredRenderTarget(target);
  }

  //  void QSGDefaultPainterNode::setSize(const QSize &size)
  void setSize(const QSize &size) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall1 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall1>(taken[1]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setSize(size);
  }

  //  void QSGDefaultPainterNode::setDirty(const QRect &dirtyRect)
  void setDirty(const QRect &dirtyRect) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall2 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall2>(taken[2]);
      call(this, &dirtyRect, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setDirty(dirtyRect);
  }

  //  void QSGDefaultPainterNode::setOpaquePainting(bool opaque)
  void setOpaquePainting(bool opaque) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall3 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall3>(taken[3]);
      call(this, opaque, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setOpaquePainting(opaque);
  }

  //  void QSGDefaultPainterNode::setLinearFiltering(bool linearFiltering)
  void setLinearFiltering(bool linearFiltering) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall4 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall4>(taken[4]);
      call(this, linearFiltering, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setLinearFiltering(linearFiltering);
  }

  //  void QSGDefaultPainterNode::setMipmapping(bool mipmapping)
  void setMipmapping(bool mipmapping) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall5 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall5>(taken[5]);
      call(this, mipmapping, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setMipmapping(mipmapping);
  }

  //  void QSGDefaultPainterNode::setSmoothPainting(bool s)
  void setSmoothPainting(bool s) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall6 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall6>(taken[6]);
      call(this, s, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setSmoothPainting(s);
  }

  //  void QSGDefaultPainterNode::setFillColor(const QColor &c)
  void setFillColor(const QColor &c) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall7 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall7>(taken[7]);
      call(this, &c, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setFillColor(c);
  }

  //  void QSGDefaultPainterNode::setContentsScale(qreal s)
  void setContentsScale(qreal s) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall8 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall8>(taken[8]);
      call(this, s, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setContentsScale(s);
  }

  //  void QSGDefaultPainterNode::setFastFBOResizing(bool fastResizing)
  void setFastFBOResizing(bool fastResizing) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall9 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall9>(taken[9]);
      call(this, fastResizing, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setFastFBOResizing(fastResizing);
  }

  //  void QSGDefaultPainterNode::setTextureSize(const QSize &textureSize)
  void setTextureSize(const QSize &textureSize) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall10 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall10>(taken[10]);
      call(this, &textureSize, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::setTextureSize(textureSize);
  }

  //  QImage QSGDefaultPainterNode::toImage() const
  QImage toImage() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall11 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGDefaultPainterNode::toImage();
  }

  //  void QSGDefaultPainterNode::update()
  void update() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall12 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultPainterNode::update();
  }

  //  QSGTexture *QSGDefaultPainterNode::texture() const
  QSGTexture *texture() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall13 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGDefaultPainterNode::texture();
  }

  //  void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall14 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall14>(taken[14]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGPainterNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall15 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGDefaultPainterNodeCall16 call = reinterpret_cast<CuteQSGDefaultPainterNodeCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGDefaultPainterNode::QSGDefaultPainterNode(QQuickPaintedItem *item)
extern "C" Q_DECL_EXPORT
QSGDefaultPainterNode *ritual_ZN21QSGDefaultPainterNodeC1EP17QQuickPaintedItem(
    QQuickPaintedItem *item) {
  return new CuteQSGDefaultPainterNode(item);
}

//  QSGDefaultPainterNode::~QSGDefaultPainterNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNodeD1Ev(QSGDefaultPainterNode *self) {
  delete self;
}

//  void QSGDefaultPainterNode::setPreferredRenderTarget(QQuickPaintedItem::R
//      enderTarget target)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE(
    QSGDefaultPainterNode *self,
    QQuickPaintedItem::RenderTarget target) {
  self->setPreferredRenderTarget(target);
}

//  void QSGDefaultPainterNode::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode7setSizeERK5QSize(
    QSGDefaultPainterNode *self,
    const QSize *size) {
  self->setSize(*size);
}

//  QSize QSGDefaultPainterNode::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QSGDefaultPainterNode4sizeEv(
    const QSGDefaultPainterNode *self) {
  return new QSize(self->size());
}

//  void QSGDefaultPainterNode::setDirty(const QRect &dirtyRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode8setDirtyERK5QRect(
    QSGDefaultPainterNode *self,
    const QRect *dirtyRect) {
  self->setDirty(*dirtyRect);
}

//  void QSGDefaultPainterNode::setOpaquePainting(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode17setOpaquePaintingEb(
    QSGDefaultPainterNode *self,
    bool opaque) {
  self->setOpaquePainting(opaque);
}

//  bool QSGDefaultPainterNode::opaquePainting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGDefaultPainterNode14opaquePaintingEv(
    const QSGDefaultPainterNode *self) {
  return self->opaquePainting();
}

//  void QSGDefaultPainterNode::setLinearFiltering(bool linearFiltering)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode18setLinearFilteringEb(
    QSGDefaultPainterNode *self,
    bool linearFiltering) {
  self->setLinearFiltering(linearFiltering);
}

//  bool QSGDefaultPainterNode::linearFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGDefaultPainterNode15linearFilteringEv(
    const QSGDefaultPainterNode *self) {
  return self->linearFiltering();
}

//  void QSGDefaultPainterNode::setMipmapping(bool mipmapping)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode13setMipmappingEb(
    QSGDefaultPainterNode *self,
    bool mipmapping) {
  self->setMipmapping(mipmapping);
}

//  bool QSGDefaultPainterNode::mipmapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGDefaultPainterNode10mipmappingEv(
    const QSGDefaultPainterNode *self) {
  return self->mipmapping();
}

//  void QSGDefaultPainterNode::setSmoothPainting(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode17setSmoothPaintingEb(
    QSGDefaultPainterNode *self,
    bool s) {
  self->setSmoothPainting(s);
}

//  bool QSGDefaultPainterNode::smoothPainting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGDefaultPainterNode14smoothPaintingEv(
    const QSGDefaultPainterNode *self) {
  return self->smoothPainting();
}

//  void QSGDefaultPainterNode::setFillColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode12setFillColorERK6QColor(
    QSGDefaultPainterNode *self,
    const QColor *c) {
  self->setFillColor(*c);
}

//  QColor QSGDefaultPainterNode::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK21QSGDefaultPainterNode9fillColorEv(
    const QSGDefaultPainterNode *self) {
  return new QColor(self->fillColor());
}

//  void QSGDefaultPainterNode::setContentsScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode16setContentsScaleEd(
    QSGDefaultPainterNode *self,
    qreal s) {
  self->setContentsScale(s);
}

//  qreal QSGDefaultPainterNode::contentsScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QSGDefaultPainterNode13contentsScaleEv(
    const QSGDefaultPainterNode *self) {
  return self->contentsScale();
}

//  void QSGDefaultPainterNode::setFastFBOResizing(bool fastResizing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode18setFastFBOResizingEb(
    QSGDefaultPainterNode *self,
    bool fastResizing) {
  self->setFastFBOResizing(fastResizing);
}

//  bool QSGDefaultPainterNode::fastFBOResizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGDefaultPainterNode15fastFBOResizingEv(
    const QSGDefaultPainterNode *self) {
  return self->fastFBOResizing();
}

//  void QSGDefaultPainterNode::setTextureSize(const QSize &textureSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode14setTextureSizeERK5QSize(
    QSGDefaultPainterNode *self,
    const QSize *textureSize) {
  self->setTextureSize(*textureSize);
}

//  QSize QSGDefaultPainterNode::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QSGDefaultPainterNode11textureSizeEv(
    const QSGDefaultPainterNode *self) {
  return new QSize(self->textureSize());
}

//  QImage QSGDefaultPainterNode::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK21QSGDefaultPainterNode7toImageEv(
    const QSGDefaultPainterNode *self) {
  return new QImage(self->toImage());
}

//  void QSGDefaultPainterNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode6updateEv(QSGDefaultPainterNode *self) {
  self->update();
}

//  void QSGDefaultPainterNode::paint()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode5paintEv(QSGDefaultPainterNode *self) {
  self->paint();
}

//  QSGTexture *QSGDefaultPainterNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK21QSGDefaultPainterNode7textureEv(
    const QSGDefaultPainterNode *self) {
  return self->texture();
}

//  void QSGDefaultPainterNode::updateTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode13updateTextureEv(
    QSGDefaultPainterNode *self) {
  self->updateTexture();
}

//  void QSGDefaultPainterNode::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode14updateGeometryEv(
    QSGDefaultPainterNode *self) {
  self->updateGeometry();
}

//  void QSGDefaultPainterNode::updateRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode18updateRenderTargetEv(
    QSGDefaultPainterNode *self) {
  self->updateRenderTarget();
}

#if QT_CONFIG(opengl)
//  void QSGDefaultPainterNode::updateFBOSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGDefaultPainterNode13updateFBOSizeEv(
    QSGDefaultPainterNode *self) {
  self->updateFBOSize();
}
#endif  // QT_CONFIG(opengl)

//  a Python function taken by a CuteQSGDefaultPainterNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDefaultPainterNode(
    QSGDefaultPainterNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDefaultPainterNode *>(self)->take(key, call);
}

//  void QSGDefaultPainterNode::setPreferredRenderTarget(QQuickPaintedItem::R
//      enderTarget target)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE(
    QSGDefaultPainterNode *self,
    QQuickPaintedItem::RenderTarget target) {
  self->QSGDefaultPainterNode::setPreferredRenderTarget(target);
}

//  void QSGDefaultPainterNode::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode7setSizeERK5QSize(
    QSGDefaultPainterNode *self,
    const QSize *size) {
  self->QSGDefaultPainterNode::setSize(*size);
}

//  void QSGDefaultPainterNode::setDirty(const QRect &dirtyRect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode8setDirtyERK5QRect(
    QSGDefaultPainterNode *self,
    const QRect *dirtyRect) {
  self->QSGDefaultPainterNode::setDirty(*dirtyRect);
}

//  void QSGDefaultPainterNode::setOpaquePainting(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode17setOpaquePaintingEb(
    QSGDefaultPainterNode *self,
    bool opaque) {
  self->QSGDefaultPainterNode::setOpaquePainting(opaque);
}

//  void QSGDefaultPainterNode::setLinearFiltering(bool linearFiltering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode18setLinearFilteringEb(
    QSGDefaultPainterNode *self,
    bool linearFiltering) {
  self->QSGDefaultPainterNode::setLinearFiltering(linearFiltering);
}

//  void QSGDefaultPainterNode::setMipmapping(bool mipmapping)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode13setMipmappingEb(
    QSGDefaultPainterNode *self,
    bool mipmapping) {
  self->QSGDefaultPainterNode::setMipmapping(mipmapping);
}

//  void QSGDefaultPainterNode::setSmoothPainting(bool s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode17setSmoothPaintingEb(
    QSGDefaultPainterNode *self,
    bool s) {
  self->QSGDefaultPainterNode::setSmoothPainting(s);
}

//  void QSGDefaultPainterNode::setFillColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode12setFillColorERK6QColor(
    QSGDefaultPainterNode *self,
    const QColor *c) {
  self->QSGDefaultPainterNode::setFillColor(*c);
}

//  void QSGDefaultPainterNode::setContentsScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode16setContentsScaleEd(
    QSGDefaultPainterNode *self,
    qreal s) {
  self->QSGDefaultPainterNode::setContentsScale(s);
}

//  void QSGDefaultPainterNode::setFastFBOResizing(bool fastResizing)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode18setFastFBOResizingEb(
    QSGDefaultPainterNode *self,
    bool fastResizing) {
  self->QSGDefaultPainterNode::setFastFBOResizing(fastResizing);
}

//  void QSGDefaultPainterNode::setTextureSize(const QSize &textureSize)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode14setTextureSizeERK5QSize(
    QSGDefaultPainterNode *self,
    const QSize *textureSize) {
  self->QSGDefaultPainterNode::setTextureSize(*textureSize);
}

//  QImage QSGDefaultPainterNode::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK21QSGDefaultPainterNode7toImageEv(
    const QSGDefaultPainterNode *self) {
  return new QImage(self->QSGDefaultPainterNode::toImage());
}

//  void QSGDefaultPainterNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGDefaultPainterNode6updateEv(
    QSGDefaultPainterNode *self) {
  self->QSGDefaultPainterNode::update();
}

//  QSGTexture *QSGDefaultPainterNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK21QSGDefaultPainterNode7textureEv(
    const QSGDefaultPainterNode *self) {
  return self->QSGDefaultPainterNode::texture();
}
