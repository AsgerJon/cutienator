//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepainternode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepainternode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsgsoftwarepixmaptexture_p.h"
#include <private/qsgcontext_p.h>
#include "qsgsoftwarepainternode_p.h"
#include "qsgsoftwarepixmaptexture_p.h"
#include <qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 23, as _ZN24QSGSoftwarePixmapTextureC1ERK7QPixmap
inline QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QPixmap &pixmap)
    : m_pixmap(pixmap)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 30, as _ZN22QSGSoftwarePainterNodeD1Ev
inline QSGSoftwarePainterNode::~QSGSoftwarePainterNode()
{
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 35, as _ZN22QSGSoftwarePainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE
inline void QSGSoftwarePainterNode::setPreferredRenderTarget(QQuickPaintedItem::RenderTarget target)
{
    if (m_preferredRenderTarget == target)
        return;

    m_preferredRenderTarget = target;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 43, as _ZN22QSGSoftwarePainterNode7setSizeERK5QSize
inline void QSGSoftwarePainterNode::setSize(const QSize &size)
{
    if (size == m_size)
        return;

    m_size = size;

    m_dirtyGeometry = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 53, as _ZN22QSGSoftwarePainterNode8setDirtyERK5QRect
inline void QSGSoftwarePainterNode::setDirty(const QRect &dirtyRect)
{
    m_dirtyContents = true;
    m_dirtyRect = dirtyRect;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 60, as _ZN22QSGSoftwarePainterNode17setOpaquePaintingEb
inline void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)
{
    if (opaque == m_opaquePainting)
        return;

    m_opaquePainting = opaque;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 68, as _ZN22QSGSoftwarePainterNode18setLinearFilteringEb
inline void QSGSoftwarePainterNode::setLinearFiltering(bool linearFiltering)
{
    if (linearFiltering == m_linear_filtering)
        return;

    m_linear_filtering = linearFiltering;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 76, as _ZN22QSGSoftwarePainterNode13setMipmappingEb
inline void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)
{
    if (mipmapping == m_mipmapping)
        return;

    m_mipmapping = mipmapping;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 84, as _ZN22QSGSoftwarePainterNode17setSmoothPaintingEb
inline void QSGSoftwarePainterNode::setSmoothPainting(bool s)
{
    if (s == m_smoothPainting)
        return;

    m_smoothPainting = s;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 92, as _ZN22QSGSoftwarePainterNode12setFillColorERK6QColor
inline void QSGSoftwarePainterNode::setFillColor(const QColor &c)
{
    if (c == m_fillColor)
        return;

    m_fillColor = c;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 101, as _ZN22QSGSoftwarePainterNode16setContentsScaleEd
inline void QSGSoftwarePainterNode::setContentsScale(qreal s)
{
    if (s == m_contentsScale)
        return;

    m_contentsScale = s;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 110, as _ZN22QSGSoftwarePainterNode18setFastFBOResizingEb
inline void QSGSoftwarePainterNode::setFastFBOResizing(bool dynamic)
{
    m_fastFBOResizing = dynamic;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 115, as _ZNK22QSGSoftwarePainterNode7toImageEv
inline QImage QSGSoftwarePainterNode::toImage() const
{
    return m_pixmap.toImage();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 120, as _ZN22QSGSoftwarePainterNode6updateEv
inline void QSGSoftwarePainterNode::update()
{
    if (m_dirtyGeometry) {
        m_pixmap = QPixmap(m_textureSize);
        if (!m_opaquePainting)
            m_pixmap.fill(Qt::transparent);

        if (m_texture)
            delete m_texture;
        m_texture = new QSGSoftwarePixmapTexture(m_pixmap);
    }

    if (m_dirtyContents)
        paint();

    m_dirtyGeometry = false;
    m_dirtyContents = false;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 139, as _ZN22QSGSoftwarePainterNode5paintEP8QPainter
inline void QSGSoftwarePainterNode::paint(QPainter *painter)
{
    bool before = painter->testRenderHint(QPainter::SmoothPixmapTransform);
    painter->setRenderHint(QPainter::SmoothPixmapTransform, m_linear_filtering);
    painter->drawPixmap(0, 0, m_size.width(), m_size.height(), m_pixmap);
    painter->setRenderHint(QPainter::SmoothPixmapTransform, before);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 147, as _ZN22QSGSoftwarePainterNode5paintEv
inline void QSGSoftwarePainterNode::paint()
{
    QRect dirtyRect = m_dirtyRect.isNull() ? QRect(0, 0, m_size.width(), m_size.height()) : m_dirtyRect;

    QPainter painter;

    painter.begin(&m_pixmap);
    if (m_smoothPainting) {
        painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing | QPainter::SmoothPixmapTransform);
    }

    QRect clipRect;

    if (m_contentsScale == 1) {
        qreal scaleX = m_textureSize.width() / (qreal) m_size.width();
        qreal scaleY = m_textureSize.height() / (qreal) m_size.height();
        painter.scale(scaleX, scaleY);
        clipRect = dirtyRect;
    } else {
        painter.scale(m_contentsScale, m_contentsScale);

        QRect sclip(qFloor(dirtyRect.x()/m_contentsScale),
                    qFloor(dirtyRect.y()/m_contentsScale),
                    qCeil(dirtyRect.width()/m_contentsScale+dirtyRect.x()/m_contentsScale-qFloor(dirtyRect.x()/m_contentsScale)),
                    qCeil(dirtyRect.height()/m_contentsScale+dirtyRect.y()/m_contentsScale-qFloor(dirtyRect.y()/m_contentsScale)));

        clipRect = sclip;
    }

    if (!m_dirtyRect.isNull())
        painter.setClipRect(clipRect);

    painter.setCompositionMode(QPainter::CompositionMode_Source);
    painter.fillRect(clipRect, m_fillColor);
    painter.setCompositionMode(QPainter::CompositionMode_SourceOver);

    m_item->paint(&painter);
    painter.end();

    m_dirtyRect = QRect();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 190, as _ZN22QSGSoftwarePainterNode14setTextureSizeERK5QSize
inline void QSGSoftwarePainterNode::setTextureSize(const QSize &size)
{
    if (size == m_textureSize)
        return;

    m_textureSize = size;
    m_dirtyGeometry = true;
}
//  -----------------------------------------------------------------------

//  A QSGSoftwarePainterNode that Python can take functions over in. Every QSGSoftwarePainterNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwarePainterNodeCall0)(const void *, int, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall1)(const void *, const QSize *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall2)(const void *, const QRect *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall3)(const void *, bool, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall4)(const void *, bool, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall5)(const void *, bool, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall6)(const void *, bool, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall7)(const void *, const QColor *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall8)(const void *, qreal, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall9)(const void *, bool, int *);
typedef const QImage * (*CuteQSGSoftwarePainterNodeCall10)(const void *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall11)(const void *, int *);
typedef void * (*CuteQSGSoftwarePainterNodeCall12)(const void *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall13)(const void *, const QSize *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall14)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGSoftwarePainterNodeCall15)(const void *, int *);
typedef void (*CuteQSGSoftwarePainterNodeCall16)(const void *, int *);
class CuteQSGSoftwarePainterNode : public QSGSoftwarePainterNode {
public:
  using QSGSoftwarePainterNode::QSGSoftwarePainterNode;
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
    if (!std::strcmp(key, "_ZNK14QSGPainterNode7toImageEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode6updateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QSGPainterNode7textureEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSGPainterNode14setTextureSizeERK5QSize")) {
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

  //  void QSGSoftwarePainterNode::setPreferredRenderTarget(QQuickPaintedIt
  //      em::RenderTarget target)
  void setPreferredRenderTarget(
      QQuickPaintedItem::RenderTarget target) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall0 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall0>(taken[0]);
      call(this, static_cast<int>(target), &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setPreferredRenderTarget(target);
  }

  //  void QSGSoftwarePainterNode::setSize(const QSize &size)
  void setSize(const QSize &size) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall1 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall1>(taken[1]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setSize(size);
  }

  //  void QSGSoftwarePainterNode::setDirty(const QRect &dirtyRect)
  void setDirty(const QRect &dirtyRect) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall2 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall2>(taken[2]);
      call(this, &dirtyRect, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setDirty(dirtyRect);
  }

  //  void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)
  void setOpaquePainting(bool opaque) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall3 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall3>(taken[3]);
      call(this, opaque, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setOpaquePainting(opaque);
  }

  //  void QSGSoftwarePainterNode::setLinearFiltering(bool linearFiltering)
  void setLinearFiltering(bool linearFiltering) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall4 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall4>(taken[4]);
      call(this, linearFiltering, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setLinearFiltering(linearFiltering);
  }

  //  void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)
  void setMipmapping(bool mipmapping) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall5 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall5>(taken[5]);
      call(this, mipmapping, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setMipmapping(mipmapping);
  }

  //  void QSGSoftwarePainterNode::setSmoothPainting(bool s)
  void setSmoothPainting(bool s) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall6 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall6>(taken[6]);
      call(this, s, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setSmoothPainting(s);
  }

  //  void QSGSoftwarePainterNode::setFillColor(const QColor &c)
  void setFillColor(const QColor &c) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall7 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall7>(taken[7]);
      call(this, &c, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setFillColor(c);
  }

  //  void QSGSoftwarePainterNode::setContentsScale(qreal s)
  void setContentsScale(qreal s) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall8 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall8>(taken[8]);
      call(this, s, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setContentsScale(s);
  }

  //  void QSGSoftwarePainterNode::setFastFBOResizing(bool dynamic)
  void setFastFBOResizing(bool dynamic) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall9 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall9>(taken[9]);
      call(this, dynamic, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setFastFBOResizing(dynamic);
  }

  //  QImage QSGSoftwarePainterNode::toImage() const
  QImage toImage() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall10 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall10>(taken[10]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwarePainterNode::toImage();
  }

  //  void QSGSoftwarePainterNode::update()
  void update() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall11 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::update();
  }

  //  QSGTexture *QSGSoftwarePainterNode::texture() const
  QSGTexture *texture() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall12 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QSGSoftwarePainterNode::texture();
  }

  //  void QSGSoftwarePainterNode::setTextureSize(const QSize &size)
  void setTextureSize(const QSize &size) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall13 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall13>(taken[13]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGSoftwarePainterNode::setTextureSize(size);
  }

  //  void QSGPainterNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall14 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall14>(taken[14]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGPainterNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall15 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwarePainterNodeCall16 call = reinterpret_cast<CuteQSGSoftwarePainterNodeCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGSoftwarePainterNode::~QSGSoftwarePainterNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNodeD1Ev(QSGSoftwarePainterNode *self) {
  delete self;
}

//  void QSGSoftwarePainterNode::setPreferredRenderTarget(QQuickPaintedItem::
//      RenderTarget target)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE(
    QSGSoftwarePainterNode *self,
    QQuickPaintedItem::RenderTarget target) {
  self->setPreferredRenderTarget(target);
}

//  void QSGSoftwarePainterNode::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode7setSizeERK5QSize(
    QSGSoftwarePainterNode *self,
    const QSize *size) {
  self->setSize(*size);
}

//  QSize QSGSoftwarePainterNode::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QSGSoftwarePainterNode4sizeEv(
    const QSGSoftwarePainterNode *self) {
  return new QSize(self->size());
}

//  void QSGSoftwarePainterNode::setDirty(const QRect &dirtyRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode8setDirtyERK5QRect(
    QSGSoftwarePainterNode *self,
    const QRect *dirtyRect) {
  self->setDirty(*dirtyRect);
}

//  void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode17setOpaquePaintingEb(
    QSGSoftwarePainterNode *self,
    bool opaque) {
  self->setOpaquePainting(opaque);
}

//  bool QSGSoftwarePainterNode::opaquePainting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSGSoftwarePainterNode14opaquePaintingEv(
    const QSGSoftwarePainterNode *self) {
  return self->opaquePainting();
}

//  void QSGSoftwarePainterNode::setLinearFiltering(bool linearFiltering)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode18setLinearFilteringEb(
    QSGSoftwarePainterNode *self,
    bool linearFiltering) {
  self->setLinearFiltering(linearFiltering);
}

//  bool QSGSoftwarePainterNode::linearFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSGSoftwarePainterNode15linearFilteringEv(
    const QSGSoftwarePainterNode *self) {
  return self->linearFiltering();
}

//  void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode13setMipmappingEb(
    QSGSoftwarePainterNode *self,
    bool mipmapping) {
  self->setMipmapping(mipmapping);
}

//  bool QSGSoftwarePainterNode::mipmapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSGSoftwarePainterNode10mipmappingEv(
    const QSGSoftwarePainterNode *self) {
  return self->mipmapping();
}

//  void QSGSoftwarePainterNode::setSmoothPainting(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode17setSmoothPaintingEb(
    QSGSoftwarePainterNode *self,
    bool s) {
  self->setSmoothPainting(s);
}

//  bool QSGSoftwarePainterNode::smoothPainting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSGSoftwarePainterNode14smoothPaintingEv(
    const QSGSoftwarePainterNode *self) {
  return self->smoothPainting();
}

//  void QSGSoftwarePainterNode::setFillColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode12setFillColorERK6QColor(
    QSGSoftwarePainterNode *self,
    const QColor *c) {
  self->setFillColor(*c);
}

//  QColor QSGSoftwarePainterNode::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK22QSGSoftwarePainterNode9fillColorEv(
    const QSGSoftwarePainterNode *self) {
  return new QColor(self->fillColor());
}

//  void QSGSoftwarePainterNode::setContentsScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode16setContentsScaleEd(
    QSGSoftwarePainterNode *self,
    qreal s) {
  self->setContentsScale(s);
}

//  qreal QSGSoftwarePainterNode::contentsScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QSGSoftwarePainterNode13contentsScaleEv(
    const QSGSoftwarePainterNode *self) {
  return self->contentsScale();
}

//  void QSGSoftwarePainterNode::setFastFBOResizing(bool dynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode18setFastFBOResizingEb(
    QSGSoftwarePainterNode *self,
    bool dynamic) {
  self->setFastFBOResizing(dynamic);
}

//  bool QSGSoftwarePainterNode::fastFBOResizing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSGSoftwarePainterNode15fastFBOResizingEv(
    const QSGSoftwarePainterNode *self) {
  return self->fastFBOResizing();
}

//  QImage QSGSoftwarePainterNode::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK22QSGSoftwarePainterNode7toImageEv(
    const QSGSoftwarePainterNode *self) {
  return new QImage(self->toImage());
}

//  void QSGSoftwarePainterNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode6updateEv(
    QSGSoftwarePainterNode *self) {
  self->update();
}

//  QSGTexture *QSGSoftwarePainterNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK22QSGSoftwarePainterNode7textureEv(
    const QSGSoftwarePainterNode *self) {
  return self->texture();
}

//  void QSGSoftwarePainterNode::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode5paintEP8QPainter(
    QSGSoftwarePainterNode *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QSGSoftwarePainterNode::paint()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode5paintEv(
    QSGSoftwarePainterNode *self) {
  self->paint();
}

//  void QSGSoftwarePainterNode::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGSoftwarePainterNode14setTextureSizeERK5QSize(
    QSGSoftwarePainterNode *self,
    const QSize *size) {
  self->setTextureSize(*size);
}

//  QSize QSGSoftwarePainterNode::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QSGSoftwarePainterNode11textureSizeEv(
    const QSGSoftwarePainterNode *self) {
  return new QSize(self->textureSize());
}

//  a Python function taken by a CuteQSGSoftwarePainterNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwarePainterNode(
    QSGSoftwarePainterNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwarePainterNode *>(self)->take(key, call);
}

//  void QSGSoftwarePainterNode::setPreferredRenderTarget(QQuickPaintedItem::
//      RenderTarget target)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE(
    QSGSoftwarePainterNode *self,
    QQuickPaintedItem::RenderTarget target) {
  self->QSGSoftwarePainterNode::setPreferredRenderTarget(target);
}

//  void QSGSoftwarePainterNode::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode7setSizeERK5QSize(
    QSGSoftwarePainterNode *self,
    const QSize *size) {
  self->QSGSoftwarePainterNode::setSize(*size);
}

//  void QSGSoftwarePainterNode::setDirty(const QRect &dirtyRect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode8setDirtyERK5QRect(
    QSGSoftwarePainterNode *self,
    const QRect *dirtyRect) {
  self->QSGSoftwarePainterNode::setDirty(*dirtyRect);
}

//  void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode17setOpaquePaintingEb(
    QSGSoftwarePainterNode *self,
    bool opaque) {
  self->QSGSoftwarePainterNode::setOpaquePainting(opaque);
}

//  void QSGSoftwarePainterNode::setLinearFiltering(bool linearFiltering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode18setLinearFilteringEb(
    QSGSoftwarePainterNode *self,
    bool linearFiltering) {
  self->QSGSoftwarePainterNode::setLinearFiltering(linearFiltering);
}

//  void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode13setMipmappingEb(
    QSGSoftwarePainterNode *self,
    bool mipmapping) {
  self->QSGSoftwarePainterNode::setMipmapping(mipmapping);
}

//  void QSGSoftwarePainterNode::setSmoothPainting(bool s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode17setSmoothPaintingEb(
    QSGSoftwarePainterNode *self,
    bool s) {
  self->QSGSoftwarePainterNode::setSmoothPainting(s);
}

//  void QSGSoftwarePainterNode::setFillColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode12setFillColorERK6QColor(
    QSGSoftwarePainterNode *self,
    const QColor *c) {
  self->QSGSoftwarePainterNode::setFillColor(*c);
}

//  void QSGSoftwarePainterNode::setContentsScale(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode16setContentsScaleEd(
    QSGSoftwarePainterNode *self,
    qreal s) {
  self->QSGSoftwarePainterNode::setContentsScale(s);
}

//  void QSGSoftwarePainterNode::setFastFBOResizing(bool dynamic)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode18setFastFBOResizingEb(
    QSGSoftwarePainterNode *self,
    bool dynamic) {
  self->QSGSoftwarePainterNode::setFastFBOResizing(dynamic);
}

//  QImage QSGSoftwarePainterNode::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK22QSGSoftwarePainterNode7toImageEv(
    const QSGSoftwarePainterNode *self) {
  return new QImage(self->QSGSoftwarePainterNode::toImage());
}

//  QSGTexture *QSGSoftwarePainterNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK22QSGSoftwarePainterNode7textureEv(
    const QSGSoftwarePainterNode *self) {
  return self->QSGSoftwarePainterNode::texture();
}

//  void QSGSoftwarePainterNode::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSGSoftwarePainterNode14setTextureSizeERK5QSize(
    QSGSoftwarePainterNode *self,
    const QSize *size) {
  self->QSGSoftwarePainterNode::setTextureSize(*size);
}
