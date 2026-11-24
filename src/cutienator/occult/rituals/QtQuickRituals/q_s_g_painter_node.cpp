//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QSGPainterNode that Python can take functions over in. Every QSGPainterNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGPainterNodeCall0)(const void *, int, int *);
typedef void (*CuteQSGPainterNodeCall1)(const void *, const QSize *, int *);
typedef void (*CuteQSGPainterNodeCall2)(const void *, const QRect *, int *);
typedef void (*CuteQSGPainterNodeCall3)(const void *, bool, int *);
typedef void (*CuteQSGPainterNodeCall4)(const void *, bool, int *);
typedef void (*CuteQSGPainterNodeCall5)(const void *, bool, int *);
typedef void (*CuteQSGPainterNodeCall6)(const void *, bool, int *);
typedef void (*CuteQSGPainterNodeCall7)(const void *, const QColor *, int *);
typedef void (*CuteQSGPainterNodeCall8)(const void *, qreal, int *);
typedef void (*CuteQSGPainterNodeCall9)(const void *, bool, int *);
typedef void (*CuteQSGPainterNodeCall10)(const void *, const QSize *, int *);
typedef const QImage * (*CuteQSGPainterNodeCall11)(const void *, int *);
typedef void (*CuteQSGPainterNodeCall12)(const void *, int *);
typedef void * (*CuteQSGPainterNodeCall13)(const void *, int *);
typedef void (*CuteQSGPainterNodeCall14)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGPainterNodeCall15)(const void *, int *);
typedef void (*CuteQSGPainterNodeCall16)(const void *, int *);
class CuteQSGPainterNode : public QSGPainterNode {
public:
  using QSGPainterNode::QSGPainterNode;
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

  //  void QSGPainterNode::setPreferredRenderTarget(QQuickPaintedItem::Rend
  //      erTarget target)
  void setPreferredRenderTarget(
      QQuickPaintedItem::RenderTarget target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGPainterNodeCall0 call = reinterpret_cast<CuteQSGPainterNodeCall0>(taken[0]);
      call(this, static_cast<int>(target), &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setSize(const QSize &size)
  void setSize(const QSize &size) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGPainterNodeCall1 call = reinterpret_cast<CuteQSGPainterNodeCall1>(taken[1]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setDirty(const QRect &dirtyRect)
  void setDirty(const QRect &dirtyRect) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGPainterNodeCall2 call = reinterpret_cast<CuteQSGPainterNodeCall2>(taken[2]);
      call(this, &dirtyRect, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setOpaquePainting(bool opaque)
  void setOpaquePainting(bool opaque) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGPainterNodeCall3 call = reinterpret_cast<CuteQSGPainterNodeCall3>(taken[3]);
      call(this, opaque, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setLinearFiltering(bool linearFiltering)
  void setLinearFiltering(bool linearFiltering) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGPainterNodeCall4 call = reinterpret_cast<CuteQSGPainterNodeCall4>(taken[4]);
      call(this, linearFiltering, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setMipmapping(bool mipmapping)
  void setMipmapping(bool mipmapping) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGPainterNodeCall5 call = reinterpret_cast<CuteQSGPainterNodeCall5>(taken[5]);
      call(this, mipmapping, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setSmoothPainting(bool s)
  void setSmoothPainting(bool s) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGPainterNodeCall6 call = reinterpret_cast<CuteQSGPainterNodeCall6>(taken[6]);
      call(this, s, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setFillColor(const QColor &c)
  void setFillColor(const QColor &c) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGPainterNodeCall7 call = reinterpret_cast<CuteQSGPainterNodeCall7>(taken[7]);
      call(this, &c, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setContentsScale(qreal s)
  void setContentsScale(qreal s) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGPainterNodeCall8 call = reinterpret_cast<CuteQSGPainterNodeCall8>(taken[8]);
      call(this, s, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setFastFBOResizing(bool dynamic)
  void setFastFBOResizing(bool dynamic) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGPainterNodeCall9 call = reinterpret_cast<CuteQSGPainterNodeCall9>(taken[9]);
      call(this, dynamic, &handled);
      if (handled) return;
    }
  }

  //  void QSGPainterNode::setTextureSize(const QSize &size)
  void setTextureSize(const QSize &size) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGPainterNodeCall10 call = reinterpret_cast<CuteQSGPainterNodeCall10>(taken[10]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }

  //  QImage QSGPainterNode::toImage() const
  QImage toImage() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGPainterNodeCall11 call = reinterpret_cast<CuteQSGPainterNodeCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGPainterNode::update()
  void update() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGPainterNodeCall12 call = reinterpret_cast<CuteQSGPainterNodeCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QSGTexture *QSGPainterNode::texture() const
  QSGTexture *texture() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGPainterNodeCall13 call = reinterpret_cast<CuteQSGPainterNodeCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return {};
  }

  //  void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGPainterNodeCall14 call = reinterpret_cast<CuteQSGPainterNodeCall14>(taken[14]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGPainterNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGPainterNodeCall15 call = reinterpret_cast<CuteQSGPainterNodeCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGPainterNodeCall16 call = reinterpret_cast<CuteQSGPainterNodeCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGPainterNode::~QSGPainterNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNodeD1Ev(QSGPainterNode *self) {
  delete self;
}

//  void
//      QSGPainterNode::setPreferredRenderTarget(QQuickPaintedItem::RenderTar
//      get target)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE(
    QSGPainterNode *self,
    QQuickPaintedItem::RenderTarget target) {
  self->setPreferredRenderTarget(target);
}

//  void QSGPainterNode::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode7setSizeERK5QSize(
    QSGPainterNode *self,
    const QSize *size) {
  self->setSize(*size);
}

//  void QSGPainterNode::setDirty(const QRect &dirtyRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode8setDirtyERK5QRect(
    QSGPainterNode *self,
    const QRect *dirtyRect) {
  self->setDirty(*dirtyRect);
}

//  void QSGPainterNode::setOpaquePainting(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode17setOpaquePaintingEb(
    QSGPainterNode *self,
    bool opaque) {
  self->setOpaquePainting(opaque);
}

//  void QSGPainterNode::setLinearFiltering(bool linearFiltering)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode18setLinearFilteringEb(
    QSGPainterNode *self,
    bool linearFiltering) {
  self->setLinearFiltering(linearFiltering);
}

//  void QSGPainterNode::setMipmapping(bool mipmapping)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode13setMipmappingEb(
    QSGPainterNode *self,
    bool mipmapping) {
  self->setMipmapping(mipmapping);
}

//  void QSGPainterNode::setSmoothPainting(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode17setSmoothPaintingEb(
    QSGPainterNode *self,
    bool s) {
  self->setSmoothPainting(s);
}

//  void QSGPainterNode::setFillColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode12setFillColorERK6QColor(
    QSGPainterNode *self,
    const QColor *c) {
  self->setFillColor(*c);
}

//  void QSGPainterNode::setContentsScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode16setContentsScaleEd(
    QSGPainterNode *self,
    qreal s) {
  self->setContentsScale(s);
}

//  void QSGPainterNode::setFastFBOResizing(bool dynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode18setFastFBOResizingEb(
    QSGPainterNode *self,
    bool dynamic) {
  self->setFastFBOResizing(dynamic);
}

//  void QSGPainterNode::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode14setTextureSizeERK5QSize(
    QSGPainterNode *self,
    const QSize *size) {
  self->setTextureSize(*size);
}

//  QImage QSGPainterNode::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK14QSGPainterNode7toImageEv(const QSGPainterNode *self) {
  return new QImage(self->toImage());
}

//  void QSGPainterNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode6updateEv(QSGPainterNode *self) {
  self->update();
}

//  QSGTexture *QSGPainterNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK14QSGPainterNode7textureEv(
    const QSGPainterNode *self) {
  return self->texture();
}

//  void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSGPainterNode6acceptEP16QSGNodeVisitorEx(
    QSGPainterNode *self,
    QSGNodeVisitorEx *visitor) {
  self->accept(visitor);
}

//  a Python function taken by a CuteQSGPainterNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGPainterNode(
    QSGPainterNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGPainterNode *>(self)->take(key, call);
}

//  void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSGPainterNode6acceptEP16QSGNodeVisitorEx(
    QSGPainterNode *self,
    QSGNodeVisitorEx *visitor) {
  self->QSGPainterNode::accept(visitor);
}
