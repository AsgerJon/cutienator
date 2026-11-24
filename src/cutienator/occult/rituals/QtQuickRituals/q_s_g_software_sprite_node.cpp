//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarespritenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarespritenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarespritenode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 17, as _ZN21QSGSoftwareSpriteNodeD1Ev
inline QSGSoftwareSpriteNode::~QSGSoftwareSpriteNode()
{
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 22, as _ZN21QSGSoftwareSpriteNode10setTextureEP10QSGTexture
inline void QSGSoftwareSpriteNode::setTexture(QSGTexture *texture)
{
    m_texture = qobject_cast<QSGSoftwarePixmapTexture*>(texture);
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 28, as _ZN21QSGSoftwareSpriteNode7setTimeEf
inline void QSGSoftwareSpriteNode::setTime(float time)
{
    if (m_time != time) {
        m_time = time;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 36, as _ZN21QSGSoftwareSpriteNode10setSourceAERK6QPoint
inline void QSGSoftwareSpriteNode::setSourceA(const QPoint &source)
{
    if (m_sourceA != source) {
        m_sourceA = source;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 44, as _ZN21QSGSoftwareSpriteNode10setSourceBERK6QPoint
inline void QSGSoftwareSpriteNode::setSourceB(const QPoint &source)
{
    if (m_sourceB != source) {
        m_sourceB = source;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 52, as _ZN21QSGSoftwareSpriteNode13setSpriteSizeERK5QSize
inline void QSGSoftwareSpriteNode::setSpriteSize(const QSize &size)
{
    if (m_spriteSize != size) {
        m_spriteSize = size;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 60, as _ZN21QSGSoftwareSpriteNode12setSheetSizeERK5QSize
inline void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)
{
    if (m_sheetSize != size) {
        m_sheetSize = size;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 68, as _ZN21QSGSoftwareSpriteNode7setSizeERK6QSizeF
inline void QSGSoftwareSpriteNode::setSize(const QSizeF &size)
{
    if (m_size != size) {
        m_size = size;
        markDirty(DirtyGeometry);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 76, as _ZN21QSGSoftwareSpriteNode12setFilteringEN10QSGTexture9FilteringE
inline void QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering filtering)
{
    Q_UNUSED(filtering);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 81, as _ZN21QSGSoftwareSpriteNode6updateEv
inline void QSGSoftwareSpriteNode::update()
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 85, as _ZN21QSGSoftwareSpriteNode5paintEP8QPainter
inline void QSGSoftwareSpriteNode::paint(QPainter *painter)
{
    //Get the pixmap handle from the texture
    if (!m_texture)
        return;

    const QPixmap &pixmap = m_texture->pixmap();

    // XXX try to do some kind of interpolation between sourceA and sourceB using time
    painter->drawPixmap(QRectF(0, 0, m_size.width(), m_size.height()),
                        pixmap,
                        QRectF(m_sourceA * pixmap.devicePixelRatio(), m_spriteSize * pixmap.devicePixelRatio()));
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 99, as _ZNK21QSGSoftwareSpriteNode8isOpaqueEv
inline bool QSGSoftwareSpriteNode::isOpaque() const
{
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 104, as _ZNK21QSGSoftwareSpriteNode4rectEv
inline QRectF QSGSoftwareSpriteNode::rect() const
{
    return QRectF(0, 0, m_size.width(), m_size.height());
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareSpriteNode that Python can take functions over in. Every QSGSoftwareSpriteNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall0)(const void *, QSGTexture *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall1)(const void *, float, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall2)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall3)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall4)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall5)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall6)(const void *, const QSizeF *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall7)(const void *, int, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSoftwareSpriteNodeCall9)(const void *, QSGNodeVisitorEx *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef bool (*CuteQSGSoftwareSpriteNodeCall10)(const void *, int *);
typedef void (*CuteQSGSoftwareSpriteNodeCall11)(const void *, int *);
class CuteQSGSoftwareSpriteNode : public QSGSoftwareSpriteNode {
public:
  using QSGSoftwareSpriteNode::QSGSoftwareSpriteNode;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode10setTextureEP10QSGTexture")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode7setTimeEf")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode10setSourceAERK6QPoint")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode10setSourceBERK6QPoint")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode13setSpriteSizeERK5QSize")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode12setSheetSizeERK5QSize")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode7setSizeERK6QSizeF")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode6updateEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall0 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall0>(taken[0]);
      call(this, texture, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setTexture(texture);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setTime(float time)
  void setTime(float time) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall1 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall1>(taken[1]);
      call(this, time, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setTime(time);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setSourceA(const QPoint &source)
  void setSourceA(const QPoint &source) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall2 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall2>(taken[2]);
      call(this, &source, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setSourceA(source);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setSourceB(const QPoint &source)
  void setSourceB(const QPoint &source) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall3 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall3>(taken[3]);
      call(this, &source, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setSourceB(source);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setSpriteSize(const QSize &size)
  void setSpriteSize(const QSize &size) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall4 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall4>(taken[4]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setSpriteSize(size);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)
  void setSheetSize(const QSize &size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall5 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall5>(taken[5]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setSheetSize(size);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall6 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall6>(taken[6]);
      call(this, &size, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setSize(size);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall7 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall7>(taken[7]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::setFiltering(filtering);
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSoftwareSpriteNode::update()
  void update() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall8 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGSoftwareSpriteNode::update();
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall9 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall9>(taken[9]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGSpriteNode::accept(visitor);
  }
#endif  // QT_CONFIG(quick_sprite)

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall10 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareSpriteNodeCall11 call = reinterpret_cast<CuteQSGSoftwareSpriteNodeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGSoftwareSpriteNode::~QSGSoftwareSpriteNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNodeD1Ev(QSGSoftwareSpriteNode *self) {
  delete self;
}

//  void QSGSoftwareSpriteNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode10setTextureEP10QSGTexture(
    QSGSoftwareSpriteNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGSoftwareSpriteNode::setTime(float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode7setTimeEf(
    QSGSoftwareSpriteNode *self,
    float time) {
  self->setTime(time);
}

//  void QSGSoftwareSpriteNode::setSourceA(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode10setSourceAERK6QPoint(
    QSGSoftwareSpriteNode *self,
    const QPoint *source) {
  self->setSourceA(*source);
}

//  void QSGSoftwareSpriteNode::setSourceB(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode10setSourceBERK6QPoint(
    QSGSoftwareSpriteNode *self,
    const QPoint *source) {
  self->setSourceB(*source);
}

//  void QSGSoftwareSpriteNode::setSpriteSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode13setSpriteSizeERK5QSize(
    QSGSoftwareSpriteNode *self,
    const QSize *size) {
  self->setSpriteSize(*size);
}

//  void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode12setSheetSizeERK5QSize(
    QSGSoftwareSpriteNode *self,
    const QSize *size) {
  self->setSheetSize(*size);
}

//  void QSGSoftwareSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode7setSizeERK6QSizeF(
    QSGSoftwareSpriteNode *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  void QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareSpriteNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  void QSGSoftwareSpriteNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode6updateEv(QSGSoftwareSpriteNode *self) {
  self->update();
}

//  void QSGSoftwareSpriteNode::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareSpriteNode5paintEP8QPainter(
    QSGSoftwareSpriteNode *self,
    QPainter *painter) {
  self->paint(painter);
}

//  bool QSGSoftwareSpriteNode::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGSoftwareSpriteNode8isOpaqueEv(
    const QSGSoftwareSpriteNode *self) {
  return self->isOpaque();
}

//  QRectF QSGSoftwareSpriteNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QSGSoftwareSpriteNode4rectEv(
    const QSGSoftwareSpriteNode *self) {
  return new QRectF(self->rect());
}

//  a Python function taken by a CuteQSGSoftwareSpriteNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareSpriteNode(
    QSGSoftwareSpriteNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareSpriteNode *>(self)->take(key, call);
}

//  void QSGSoftwareSpriteNode::setTime(float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode7setTimeEf(
    QSGSoftwareSpriteNode *self,
    float time) {
  self->QSGSoftwareSpriteNode::setTime(time);
}

//  void QSGSoftwareSpriteNode::setSourceA(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode10setSourceAERK6QPoint(
    QSGSoftwareSpriteNode *self,
    const QPoint *source) {
  self->QSGSoftwareSpriteNode::setSourceA(*source);
}

//  void QSGSoftwareSpriteNode::setSourceB(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode10setSourceBERK6QPoint(
    QSGSoftwareSpriteNode *self,
    const QPoint *source) {
  self->QSGSoftwareSpriteNode::setSourceB(*source);
}

//  void QSGSoftwareSpriteNode::setSpriteSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode13setSpriteSizeERK5QSize(
    QSGSoftwareSpriteNode *self,
    const QSize *size) {
  self->QSGSoftwareSpriteNode::setSpriteSize(*size);
}

//  void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode12setSheetSizeERK5QSize(
    QSGSoftwareSpriteNode *self,
    const QSize *size) {
  self->QSGSoftwareSpriteNode::setSheetSize(*size);
}

//  void QSGSoftwareSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode7setSizeERK6QSizeF(
    QSGSoftwareSpriteNode *self,
    const QSizeF *size) {
  self->QSGSoftwareSpriteNode::setSize(*size);
}

//  void QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareSpriteNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGSoftwareSpriteNode::setFiltering(filtering);
}

//  void QSGSoftwareSpriteNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareSpriteNode6updateEv(
    QSGSoftwareSpriteNode *self) {
  self->QSGSoftwareSpriteNode::update();
}

#endif  // QT_CONFIG(quick_sprite)
#endif  // QT_CONFIG(quick_sprite)
