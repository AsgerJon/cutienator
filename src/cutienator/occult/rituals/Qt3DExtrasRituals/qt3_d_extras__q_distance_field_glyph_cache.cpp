//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qdistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qdistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/private/qrawfont_p.h>
#include <Qt3DExtras/private/qdistancefieldglyphcache_p.h>
#include <Qt3DExtras/private/qtextureatlas_p.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/private/qdistancefield_p.h>
#include <Qt3DCore/private/qnode_p.h>
#include <Qt3DExtras/private/qtextureatlas_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 20, as local:qdistancefieldglyphcache.cpp:DEFAULT_IMAGE_PADDING
#define DEFAULT_IMAGE_PADDING 1

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 28, as local:qdistancefieldglyphcache.cpp:StoredGlyph
namespace Qt3DExtras {
using namespace Qt3DCore;
class StoredGlyph {
public:
    StoredGlyph() = default;
    StoredGlyph(const QRawFont &font, quint32 glyph, bool doubleResolution);

    int refCount() const { return int(m_ref); }
    void ref() { ++m_ref; }
    int deref() { m_ref = std::max(m_ref - 1, quint32(0)); return int(m_ref); }

    bool addToTextureAtlas(QTextureAtlas *atlas);
    void removeFromTextureAtlas();

    QTextureAtlas *atlas() const { return m_atlas; }
    QRectF glyphPathBoundingRect() const { return m_glyphPathBoundingRect; }
    QRectF texCoords() const;

private:
    quint32 m_ref = 0;
    QTextureAtlas *m_atlas = nullptr;
    QTextureAtlas::TextureId m_atlasEntry = QTextureAtlas::InvalidTexture;
    QRectF m_glyphPathBoundingRect;
    QImage m_distanceFieldImage;    // only used until added to texture atlas
};
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 78, as local:qdistancefieldglyphcache.cpp:StoredGlyph::StoredGlyph
namespace Qt3DExtras {
using namespace Qt3DCore;
inline StoredGlyph::StoredGlyph(const QRawFont &font, quint32 glyph, bool doubleResolution)
    : m_ref(1)
    , m_atlas(nullptr)
    , m_atlasEntry(QTextureAtlas::InvalidTexture)
{
    // create new single-channel distance field image for given glyph
    const QPainterPath path = font.pathForGlyph(glyph);
    const QDistanceField dfield(font, glyph, doubleResolution);
    m_distanceFieldImage = dfield.toImage(QImage::Format_Alpha8);

    // scale bounding rect down (as in QSGDistanceFieldGlyphCache::glyphData())
    const QRectF pathBound = path.boundingRect();
    float f = 1.0f / QT_DISTANCEFIELD_SCALE(doubleResolution);
    m_glyphPathBoundingRect = QRectF(pathBound.left() * f, -pathBound.top() * f, pathBound.width() * f, pathBound.height() * f);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 94, as local:qdistancefieldglyphcache.cpp:StoredGlyph::addToTextureAtlas
namespace Qt3DExtras {
using namespace Qt3DCore;
inline bool StoredGlyph::addToTextureAtlas(QTextureAtlas *atlas)
{
    if (m_atlas || m_distanceFieldImage.isNull())
        return false;

    const auto texId = atlas->addImage(m_distanceFieldImage, DEFAULT_IMAGE_PADDING);
    if (texId != QTextureAtlas::InvalidTexture) {
        m_atlas = atlas;
        m_atlasEntry = texId;
        m_distanceFieldImage = QImage();    // free glyph image data
        return true;
    }

    return false;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 110, as local:qdistancefieldglyphcache.cpp:StoredGlyph::removeFromTextureAtlas
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void StoredGlyph::removeFromTextureAtlas()
{
    if (m_atlas) {
        m_atlas->removeImage(m_atlasEntry);
        m_atlas = nullptr;
        m_atlasEntry = QTextureAtlas::InvalidTexture;
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 119, as local:qdistancefieldglyphcache.cpp:StoredGlyph::texCoords
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QRectF StoredGlyph::texCoords() const
{
    return m_atlas ? m_atlas->imageTexCoords(m_atlasEntry) : QRectF();
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 268, as _ZN10Qt3DExtras24QDistanceFieldGlyphCacheC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QDistanceFieldGlyphCache::QDistanceFieldGlyphCache()
    : m_rootNode(nullptr)
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 273, as _ZN10Qt3DExtras24QDistanceFieldGlyphCacheD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QDistanceFieldGlyphCache::~QDistanceFieldGlyphCache()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 277, as _ZN10Qt3DExtras24QDistanceFieldGlyphCache11setRootNodeEPN8Qt3DCore5QNodeE
namespace Qt3DExtras {
using namespace Qt3DCore;
inline void QDistanceFieldGlyphCache::setRootNode(QNode *rootNode)
{
    m_rootNode = rootNode;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 282, as _ZNK10Qt3DExtras24QDistanceFieldGlyphCache8rootNodeEv
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QNode *QDistanceFieldGlyphCache::rootNode() const
{
    return m_rootNode;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 221, as _ZN10Qt3DExtras24QDistanceFieldGlyphCache7fontKeyERK8QRawFont
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QString QDistanceFieldGlyphCache::fontKey(const QRawFont &font)
{
    QFontEngine *fe = QRawFontPrivate::get(font)->fontEngine;
    if (!fe->faceId().filename.isEmpty()) {
        QByteArray keyName = fe->faceId().filename;
        if (font.style() != QFont::StyleNormal)
            keyName += QByteArray(" I");
        if (font.weight() != QFont::Normal)
            keyName += ' ' + QByteArray::number(font.weight());
        keyName += QByteArray(" DF");
        return QString::fromUtf8(keyName);
    } else {
        return QString::fromLatin1("%1_%2_%3_%4")
                  .arg(font.familyName())
                  .arg(font.styleName())
                  .arg(font.weight())
                  .arg(font.style());
    }
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  Qt3DExtras::QDistanceFieldGlyphCache::QDistanceFieldGlyphCache()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDistanceFieldGlyphCache *ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCacheC1Ev() {
  return new Qt3DExtras::QDistanceFieldGlyphCache();
}

//  Qt3DExtras::QDistanceFieldGlyphCache::~QDistanceFieldGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCacheD1Ev(
    Qt3DExtras::QDistanceFieldGlyphCache *self) {
  delete self;
}

//  void Qt3DExtras::QDistanceFieldGlyphCache::setRootNode(Qt3DCore::QNode
//      *rootNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCache11setRootNodeEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QDistanceFieldGlyphCache *self,
    Qt3DCore::QNode *rootNode) {
  self->setRootNode(rootNode);
}

//  Qt3DCore::QNode *Qt3DExtras::QDistanceFieldGlyphCache::rootNode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK10Qt3DExtras24QDistanceFieldGlyphCache8rootNodeEv(
    const Qt3DExtras::QDistanceFieldGlyphCache *self) {
  return self->rootNode();
}

//  QString Qt3DExtras::QDistanceFieldGlyphCache::fontKey(const QRawFont
//      &font)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras24QDistanceFieldGlyphCache7fontKeyERK8QRawFont(
    const QRawFont *font) {
  return new QString(Qt3DExtras::QDistanceFieldGlyphCache::fontKey(*font));
}

//  a QList<Qt3DExtras::QDistanceFieldGlyphCache::Glyph> a ritual of
//      Qt3DExtras::QDistanceFieldGlyphCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DExtras_QDistanceFieldGlyphCache__QList_Qt3DExtras_QDistanceFieldGlyphCache_Glyph(
    QList<Qt3DExtras::QDistanceFieldGlyphCache::Glyph> *self) {
  delete self;
}
