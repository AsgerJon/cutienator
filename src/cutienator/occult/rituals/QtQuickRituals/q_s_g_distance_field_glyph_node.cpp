//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdistancefieldglyphnode_p.h>
#include <QtQuick/private/qsgdistancefieldglyphnode_p_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 165, as _ZN25QSGDistanceFieldGlyphNode10preprocessEv
inline void QSGDistanceFieldGlyphNode::preprocess()
{
    if (m_dirtyGeometry)
        updateGeometry();

    setFlag(UsePreprocess, false);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 151, as _ZN25QSGDistanceFieldGlyphNode13setStyleColorERK6QColor
inline void QSGDistanceFieldGlyphNode::setStyleColor(const QColor &color)
{
    if (m_styleColor == color)
        return;
    m_styleColor = color;
    m_dirtyMaterial = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 173, as _ZN25QSGDistanceFieldGlyphNode16invalidateGlyphsERK5QListIjE
inline void QSGDistanceFieldGlyphNode::invalidateGlyphs(const QList<quint32> &glyphs)
{
    if (m_dirtyGeometry)
        return;

    for (int i = 0; i < glyphs.size(); ++i) {
        if (m_allGlyphIndexesLookup.contains(glyphs.at(i))) {
            m_dirtyGeometry = true;
            setFlag(UsePreprocess);
            return;
        }
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 88, as _ZN25QSGDistanceFieldGlyphNode20setRenderTypeQualityEi
inline void QSGDistanceFieldGlyphNode::setRenderTypeQuality(int renderTypeQuality)
{
    if (renderTypeQuality == m_renderTypeQuality)
        return;

    m_renderTypeQuality = renderTypeQuality;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 96, as _ZN25QSGDistanceFieldGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE
inline void QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(AntialiasingMode mode)
{
    if (mode == m_antialiasingMode)
        return;
    m_antialiasingMode = mode;
    m_dirtyMaterial = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 159, as _ZN25QSGDistanceFieldGlyphNode6updateEv
inline void QSGDistanceFieldGlyphNode::update()
{
    if (m_dirtyMaterial)
        updateMaterial();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 58, as _ZN25QSGDistanceFieldGlyphNode7recycleEv
inline void QSGDistanceFieldGlyphNode::recycle()
{
    QSGGlyphNode::recycle();

    cleanup();
    m_color = QColor{};
    m_baseLine = QPointF{};
    m_originalPosition = QPointF{};
    m_position = QPointF{};
    m_glyphs = QGlyphRun{};
    m_geometry.allocate(0, 0); // Shrink
    m_style = QQuickText::Normal;
    m_antialiasingMode = GrayAntialiasing;
    m_boundingRect = QRectF{};
    m_renderTypeQuality = -1;
    m_dirtyGeometry = true;
    m_dirtyMaterial = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 77, as _ZN25QSGDistanceFieldGlyphNode8setColorERK6QColor
inline void QSGDistanceFieldGlyphNode::setColor(const QColor &color)
{
    m_color = color;
    if (m_material != nullptr) {
        m_material->setColor(color);
        markDirty(DirtyMaterial);
    } else {
        m_dirtyMaterial = true;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 143, as _ZN25QSGDistanceFieldGlyphNode8setStyleEN10QQuickText9TextStyleE
inline void QSGDistanceFieldGlyphNode::setStyle(QQuickText::TextStyle style)
{
    if (m_style == style)
        return;
    m_style = style;
    m_dirtyMaterial = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 104, as _ZN25QSGDistanceFieldGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun
inline void QSGDistanceFieldGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun &glyphs)
{
    QRawFont font = glyphs.rawFont();
    m_originalPosition = position;
    m_position = QPointF(position.x(), position.y() - font.ascent());
    m_glyphs = glyphs;

    m_dirtyGeometry = true;
    m_dirtyMaterial = true;
    setFlag(UsePreprocess);

    QSGDistanceFieldGlyphCache *oldCache = m_glyph_cache;
    m_glyph_cache = m_context->distanceFieldGlyphCache(m_glyphs.rawFont(), m_renderTypeQuality);

    if (m_glyphNodeType == SubGlyphNode)
        return;

    if (m_glyph_cache != oldCache) {
        if (oldCache)
            oldCache->unregisterGlyphNode(this);

        if (m_glyph_cache)
            m_glyph_cache->registerGlyphNode(this);
    }
    if (m_glyph_cache)
        m_glyph_cache->populate(glyphs.glyphIndexes());

    const QList<quint32> glyphIndexes = m_glyphs.glyphIndexes();
    for (int i = 0; i < glyphIndexes.size(); ++i)
        m_allGlyphIndexesLookup.insert(glyphIndexes.at(i));
    qCDebug(lcSgText, "inserting %" PRIdQSIZETYPE " glyphs, %" PRIdQSIZETYPE " unique",
            glyphIndexes.size(),
            m_allGlyphIndexesLookup.size());
#ifdef QSG_RUNTIME_DESCRIPTION
    qsgnode_set_description(this, QString::number(glyphs.glyphIndexes().count()) + QStringLiteral(" DF glyphs: ") +
                            m_glyphs.rawFont().familyName() + QStringLiteral(" ") + QString::number(m_glyphs.rawFont().pixelSize()));
#endif
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 11, as _Z8lcSgTextv
inline const QLoggingCategory &lcSgText()
{
    static const QLoggingCategory category("qt.scenegraph.text");
    return category;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 37, as _ZN25QSGDistanceFieldGlyphNodeD1Ev
inline QSGDistanceFieldGlyphNode::~QSGDistanceFieldGlyphNode()
{
    cleanup();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 42, as _ZN25QSGDistanceFieldGlyphNode7cleanupEv
inline void QSGDistanceFieldGlyphNode::cleanup()
{
    delete m_material;
    m_material = nullptr;
    m_texture = nullptr;

    if (m_glyphNodeType == SubGlyphNode)
        return;

    if (m_glyph_cache) {
        m_glyph_cache->release(m_glyphs.glyphIndexes());
        m_glyph_cache->unregisterGlyphNode(this);
        m_glyph_cache = nullptr;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdistancefieldglyphnode.cpp, line 360, as _ZN25QSGDistanceFieldGlyphNode14updateMaterialEv
inline void QSGDistanceFieldGlyphNode::updateMaterial()
{
    delete m_material;

    if (m_style == QQuickText::Normal) {
        switch (m_antialiasingMode) {
        case HighQualitySubPixelAntialiasing:
            m_material = new QSGHiQSubPixelDistanceFieldTextMaterial;
            break;
        case LowQualitySubPixelAntialiasing:
            m_material = new QSGLoQSubPixelDistanceFieldTextMaterial;
            break;
        case GrayAntialiasing:
        default:
            m_material = new QSGDistanceFieldTextMaterial;
            break;
        }
    } else {
        QSGDistanceFieldStyledTextMaterial *material;
        if (m_style == QQuickText::Outline) {
            material = new QSGDistanceFieldOutlineTextMaterial;
        } else {
            QSGDistanceFieldShiftedStyleTextMaterial *sMaterial = new QSGDistanceFieldShiftedStyleTextMaterial;
            if (m_style == QQuickText::Raised)
                sMaterial->setShift(QPointF(0.0, 1.0));
            else
                sMaterial->setShift(QPointF(0.0, -1.0));
            material = sMaterial;
        }
        material->setStyleColor(m_styleColor);
        m_material = material;
    }

    m_material->setGlyphCache(m_glyph_cache);
    if (m_glyph_cache)
        m_material->setFontScale(m_glyph_cache->fontScale(m_glyphs.rawFont().pixelSize()));
    m_material->setColor(m_color);
    setMaterial(m_material);
    m_dirtyMaterial = false;
}
//  -----------------------------------------------------------------------

//  A QSGDistanceFieldGlyphNode that Python can take functions over in. Every QSGDistanceFieldGlyphNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPointF * (*CuteQSGDistanceFieldGlyphNodeCall0)(const void *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall1)(const void *, const QPointF *, const QGlyphRun *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall2)(const void *, const QColor *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall3)(const void *, int, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall4)(const void *, int, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall5)(const void *, int, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall6)(const void *, const QColor *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall7)(const void *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall8)(const void *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall9)(const void *, int *);
typedef const QRectF * (*CuteQSGDistanceFieldGlyphNodeCall10)(const void *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall11)(const void *, const QRectF *, int *);
typedef void (*CuteQSGDistanceFieldGlyphNodeCall12)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGDistanceFieldGlyphNodeCall13)(const void *, int *);
class CuteQSGDistanceFieldGlyphNode : public QSGDistanceFieldGlyphNode {
public:
  using QSGDistanceFieldGlyphNode::QSGDistanceFieldGlyphNode;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode8baseLineEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setColorERK6QColor")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16AntialiasingModeE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode20setRenderTypeQualityEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode13setStyleColorERK6QColor")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode6updateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode7recycleEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode12boundingRectEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode15setBoundingRectERK6QRectF")) {
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
    return false;
  }

  //  QPointF QSGDistanceFieldGlyphNode::baseLine() const
  QPointF baseLine() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall0 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall0>(taken[0]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGDistanceFieldGlyphNode::baseLine();
  }

  //  void QSGDistanceFieldGlyphNode::setGlyphs(const QPointF &position,
  //      const QGlyphRun &glyphs)
  void setGlyphs(const QPointF &position, const QGlyphRun &glyphs) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall1 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall1>(taken[1]);
      call(this, &position, &glyphs, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::setGlyphs(position, glyphs);
  }

  //  void QSGDistanceFieldGlyphNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall2 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall2>(taken[2]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::setColor(color);
  }

  //  void QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(Antialia
  //      singMode mode)
  void setPreferredAntialiasingMode(
      QSGGlyphNode::AntialiasingMode mode) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall3 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall3>(taken[3]);
      call(this, static_cast<int>(mode), &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(mode);
  }

  //  void QSGDistanceFieldGlyphNode::setRenderTypeQuality(int
  //      renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall4 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall4>(taken[4]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::setRenderTypeQuality(renderTypeQuality);
  }

  //  void QSGDistanceFieldGlyphNode::setStyle(QQuickText::TextStyle style)
  void setStyle(QQuickText::TextStyle style) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall5 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall5>(taken[5]);
      call(this, static_cast<int>(style), &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::setStyle(style);
  }

  //  void QSGDistanceFieldGlyphNode::setStyleColor(const QColor &color)
  void setStyleColor(const QColor &color) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall6 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall6>(taken[6]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::setStyleColor(color);
  }

  //  void QSGDistanceFieldGlyphNode::update()
  void update() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall7 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::update();
  }

  //  void QSGDistanceFieldGlyphNode::preprocess()
  void preprocess() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall8 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::preprocess();
  }

  //  void QSGDistanceFieldGlyphNode::recycle()
  void recycle() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall9 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDistanceFieldGlyphNode::recycle();
  }

  //  QRectF QSGGlyphNode::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall10 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall10>(taken[10]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGGlyphNode::boundingRect();
  }

  //  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
  void setBoundingRect(const QRectF &bounds) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall11 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall11>(taken[11]);
      call(this, &bounds, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setBoundingRect(bounds);
  }

  //  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall12 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall12>(taken[12]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGGlyphNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDistanceFieldGlyphNodeCall13 call = reinterpret_cast<CuteQSGDistanceFieldGlyphNodeCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }
};

//  QSGDistanceFieldGlyphNode::~QSGDistanceFieldGlyphNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNodeD1Ev(
    QSGDistanceFieldGlyphNode *self) {
  delete self;
}

//  QPointF QSGDistanceFieldGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK25QSGDistanceFieldGlyphNode8baseLineEv(
    const QSGDistanceFieldGlyphNode *self) {
  return new QPointF(self->baseLine());
}

//  void QSGDistanceFieldGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGDistanceFieldGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->setGlyphs(*position, *glyphs);
}

//  void QSGDistanceFieldGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode8setColorERK6QColor(
    QSGDistanceFieldGlyphNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void
//      QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(AntialiasingM
//      ode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGDistanceFieldGlyphNode *self,
    QSGGlyphNode::AntialiasingMode mode) {
  self->setPreferredAntialiasingMode(mode);
}

//  void QSGDistanceFieldGlyphNode::setRenderTypeQuality(int
//      renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode20setRenderTypeQualityEi(
    QSGDistanceFieldGlyphNode *self,
    int renderTypeQuality) {
  self->setRenderTypeQuality(renderTypeQuality);
}

//  void QSGDistanceFieldGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGDistanceFieldGlyphNode *self,
    QQuickText::TextStyle style) {
  self->setStyle(style);
}

//  void QSGDistanceFieldGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode13setStyleColorERK6QColor(
    QSGDistanceFieldGlyphNode *self,
    const QColor *color) {
  self->setStyleColor(*color);
}

//  void QSGDistanceFieldGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode6updateEv(
    QSGDistanceFieldGlyphNode *self) {
  self->update();
}

//  void QSGDistanceFieldGlyphNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode10preprocessEv(
    QSGDistanceFieldGlyphNode *self) {
  self->preprocess();
}

//  void QSGDistanceFieldGlyphNode::invalidateGlyphs(const QList<quint32>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode16invalidateGlyphsERK5QListIjE(
    QSGDistanceFieldGlyphNode *self,
    const QList<quint32> *glyphs) {
  self->invalidateGlyphs(*glyphs);
}

//  void QSGDistanceFieldGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode7recycleEv(
    QSGDistanceFieldGlyphNode *self) {
  self->recycle();
}

//  void QSGDistanceFieldGlyphNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode7cleanupEv(
    QSGDistanceFieldGlyphNode *self) {
  self->cleanup();
}

//  void
//      QSGDistanceFieldGlyphNode::setGlyphNodeType(DistanceFieldGlyphNodeTyp
//      e type)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode16setGlyphNodeTypeENS_26DistanceFieldGlyphNodeTypeE(
    QSGDistanceFieldGlyphNode *self,
    QSGDistanceFieldGlyphNode::DistanceFieldGlyphNodeType type) {
  self->setGlyphNodeType(type);
}

//  void QSGDistanceFieldGlyphNode::updateMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGDistanceFieldGlyphNode14updateMaterialEv(
    QSGDistanceFieldGlyphNode *self) {
  self->updateMaterial();
}

//  QSGDistanceFieldGlyphNode as the QSGDistanceFieldGlyphConsumer it is
//      built on
extern "C" Q_DECL_EXPORT
QSGDistanceFieldGlyphConsumer *ritual_cast_QSGDistanceFieldGlyphNode_QSGDistanceFieldGlyphConsumer(
    QSGDistanceFieldGlyphNode *self) {
  return static_cast<QSGDistanceFieldGlyphConsumer *>(self);
}

//  a Python function taken by a CuteQSGDistanceFieldGlyphNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDistanceFieldGlyphNode(
    QSGDistanceFieldGlyphNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDistanceFieldGlyphNode *>(self)->take(key, call);
}

//  QPointF QSGDistanceFieldGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK25QSGDistanceFieldGlyphNode8baseLineEv(
    const QSGDistanceFieldGlyphNode *self) {
  return new QPointF(self->QSGDistanceFieldGlyphNode::baseLine());
}

//  void QSGDistanceFieldGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGDistanceFieldGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->QSGDistanceFieldGlyphNode::setGlyphs(*position, *glyphs);
}

//  void QSGDistanceFieldGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode8setColorERK6QColor(
    QSGDistanceFieldGlyphNode *self,
    const QColor *color) {
  self->QSGDistanceFieldGlyphNode::setColor(*color);
}

//  void
//      QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(AntialiasingM
//      ode mode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGDistanceFieldGlyphNode *self,
    QSGGlyphNode::AntialiasingMode mode) {
  self->QSGDistanceFieldGlyphNode::setPreferredAntialiasingMode(mode);
}

//  void QSGDistanceFieldGlyphNode::setRenderTypeQuality(int
//      renderTypeQuality)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode20setRenderTypeQualityEi(
    QSGDistanceFieldGlyphNode *self,
    int renderTypeQuality) {
  self->QSGDistanceFieldGlyphNode::setRenderTypeQuality(renderTypeQuality);
}

//  void QSGDistanceFieldGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGDistanceFieldGlyphNode *self,
    QQuickText::TextStyle style) {
  self->QSGDistanceFieldGlyphNode::setStyle(style);
}

//  void QSGDistanceFieldGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode13setStyleColorERK6QColor(
    QSGDistanceFieldGlyphNode *self,
    const QColor *color) {
  self->QSGDistanceFieldGlyphNode::setStyleColor(*color);
}

//  void QSGDistanceFieldGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode6updateEv(
    QSGDistanceFieldGlyphNode *self) {
  self->QSGDistanceFieldGlyphNode::update();
}

//  void QSGDistanceFieldGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSGDistanceFieldGlyphNode7recycleEv(
    QSGDistanceFieldGlyphNode *self) {
  self->QSGDistanceFieldGlyphNode::recycle();
}
