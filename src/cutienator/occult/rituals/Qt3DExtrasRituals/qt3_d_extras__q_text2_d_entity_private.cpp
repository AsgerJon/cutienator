//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtext2dentity_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtext2dentity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qtext2dentity.h>
#include <Qt3DExtras/private/qtext2dentity_p.h>
#include <Qt3DExtras/private/qtext2dmaterial_p.h>
#include <QtGui/qtextlayout.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/private/qdistancefield_p.h>
#include <QtGui/private/qtextureglyphcache_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qdistancefield_p.h>
#include <Qt3DCore/qbuffer.h>
#include <Qt3DCore/qattribute.h>
#include <Qt3DCore/qgeometry.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qgeometryrenderer.h>
#include <Qt3DCore/private/qscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/qdistancefieldglyphcache.cpp, line 20, as local:qdistancefieldglyphcache.cpp:DEFAULT_IMAGE_PADDING
#define DEFAULT_IMAGE_PADDING 1

//  from ../qt3d/src/extras/text/qtext2dentity.cpp, line 27, as local:qtext2dentity.cpp:scaleRectF
namespace {
inline constexpr QRectF scaleRectF(const QRectF &rect, qreal scale)
{
    return QRectF(rect.left() * scale, rect.top() * scale, rect.width() * scale, rect.height() * scale);
}
}  // namespace

//  from ../qt3d/src/extras/text/qtext2dentity.cpp, line 183, as local:qtext2dentity.cpp:RenderData
namespace Qt3DExtras {
struct RenderData {
    int vertexCount = 0;
    std::vector<float> vertex;
    std::vector<quint16> index;
};
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dentity.cpp, line 125, as _ZN10Qt3DExtras20QText2DEntityPrivate8setSceneEPN8Qt3DCore6QSceneE
namespace Qt3DExtras {
inline void QText2DEntityPrivate::setScene(Qt3DCore::QScene *scene)
{
    if (scene == m_scene)
        return;

    // Unref old glyph cache if it exists
    if (m_scene != nullptr) {
        // Ensure we don't keep reference to glyphs
        // if we are changing the cache
        if (m_glyphCache != nullptr)
            clearCurrentGlyphRuns();

        m_glyphCache = nullptr;

        QText2DEntityPrivate::CacheEntry &entry = QText2DEntityPrivate::m_glyphCacheInstances[m_scene];
        --entry.count;
        if (entry.count == 0 && entry.glyphCache != nullptr) {

            delete entry.glyphCache;
            entry.glyphCache = nullptr;
        }
    }

    QEntityPrivate::setScene(scene);

    // Ref new glyph cache is scene is valid
    if (scene != nullptr) {
        QText2DEntityPrivate::CacheEntry &entry = QText2DEntityPrivate::m_glyphCacheInstances[scene];
        if (entry.glyphCache == nullptr) {
            entry.glyphCache = new QDistanceFieldGlyphCache();
            entry.glyphCache->setRootNode(scene->rootNode());
        }
        m_glyphCache = entry.glyphCache;
        ++entry.count;
        // Update to populate glyphCache if needed
        updateGlyphs();
    }
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dentity.cpp, line 189, as _ZN10Qt3DExtras20QText2DEntityPrivate19setCurrentGlyphRunsERK5QListI9QGlyphRunE
namespace Qt3DExtras {
inline void QText2DEntityPrivate::setCurrentGlyphRuns(const QList<QGlyphRun> &runs)
{
    // For each distinct texture, we need a separate DistanceFieldTextRenderer,
    // for which we need vertex and index data
    QHash<Qt3DRender::QAbstractTexture*, RenderData> renderData;
    const qreal scale = computeActualScale();

    // process glyph runs
    for (const QGlyphRun &run : runs) {
        const auto glyphs = run.glyphIndexes();
        const auto pos = run.positions();

        Q_ASSERT(glyphs.size() == pos.size());

        const bool doubleGlyphResolution = m_glyphCache->doubleGlyphResolution(run.rawFont());

        // faithfully copied from QSGDistanceFieldGlyphNode::updateGeometry()
        const qreal pixelSize = run.rawFont().pixelSize();
        const qreal fontScale = pixelSize / QT_DISTANCEFIELD_BASEFONTSIZE(doubleGlyphResolution);
        const qreal margin = QT_DISTANCEFIELD_RADIUS(doubleGlyphResolution) / QT_DISTANCEFIELD_SCALE(doubleGlyphResolution) * fontScale;

        for (int i = 0; i < glyphs.size(); i++) {
            const QDistanceFieldGlyphCache::Glyph &dfield = m_glyphCache->refGlyph(run.rawFont(), glyphs[i]);

            if (!dfield.texture)
                continue;

            RenderData &data = renderData[dfield.texture];

            // faithfully copied from QSGDistanceFieldGlyphNode::updateGeometry()
            QRectF metrics = scaleRectF(dfield.glyphPathBoundingRect, fontScale);
            metrics.adjust(-margin, margin, margin, 3*margin);

            const qreal top = 0.0;
            const qreal left = 0.0;
            const qreal right = qreal(m_width);
            const qreal bottom = qreal(m_height);

            qreal x1 = left + scale * (pos[i].x() + metrics.left());
            qreal y2 = bottom - scale * (pos[i].y() - metrics.top());
            qreal x2 = x1 + scale * metrics.width();
            qreal y1 = y2 - scale * metrics.height();

            // only draw glyphs that are at least partly visible
            if (y2 < top || x1 > right)
                continue;

            QRectF texCoords = dfield.texCoords;

            // if a glyph is only partly visible within the given rectangle,
            // cut it in half and adjust tex coords
            if (y1 < top) {
                const auto insideRatio = (top - y2) / (y1 - y2);
                y1 = top;
                texCoords.setHeight(texCoords.height() * insideRatio);
            }

            // do the same thing horizontally
            if (x2 > right) {
                const auto insideRatio = (right - x1) / (x2 - x1);
                x2 = right;
                texCoords.setWidth(texCoords.width() * insideRatio);
            }

            for (auto v: std::vector<qreal>{x1, y1, qreal(i), texCoords.left(), texCoords.bottom()})
                data.vertex.push_back(float(v));
            for (auto v: std::vector<qreal>{x1, y2, qreal(i), texCoords.left(), texCoords.top()})
                data.vertex.push_back(float(v));
            for (auto v: std::vector<qreal>{x2, y1, qreal(i), texCoords.right(), texCoords.bottom()})
                data.vertex.push_back(float(v));
            for (auto v: std::vector<qreal>{x2, y2, qreal(i), texCoords.right(), texCoords.top()})
                data.vertex.push_back(float(v));

            for (int i: std::vector<int>{data.vertexCount, data.vertexCount + 3, data.vertexCount + 1})
                data.index.push_back(quint16(i));
            for (int i: std::vector<int>{data.vertexCount, data.vertexCount + 2, data.vertexCount + 3})
                data.index.push_back(quint16(i));

            data.vertexCount += 4;
        }
    }

    // de-ref all glyphs for previous QGlyphRuns
    for (int i = 0; i < m_currentGlyphRuns.size(); i++)
        m_glyphCache->derefGlyphs(m_currentGlyphRuns[i]);
    m_currentGlyphRuns = runs;

    // make sure we have the correct number of DistanceFieldTextRenderers
    // TODO: we might keep one renderer at all times, so we won't delete and
    // re-allocate one every time the text changes from an empty to a non-empty string
    // and vice-versa
    while (m_renderers.size() > renderData.size())
        delete m_renderers.takeLast();

    while (m_renderers.size() < renderData.size()) {
        DistanceFieldTextRenderer *renderer = new DistanceFieldTextRenderer();
        renderer->setColor(m_color);
        renderer->setParent(q_func());
        m_renderers << renderer;
    }

    Q_ASSERT(m_renderers.size() == renderData.size());

    // assign vertex data for all textures to the renderers
    int rendererIdx = 0;
    for (auto it = renderData.begin(); it != renderData.end(); ++it)
        m_renderers[rendererIdx++]->setGlyphData(it.key(), it.value().vertex, it.value().index);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dentity.cpp, line 121, as _ZN10Qt3DExtras20QText2DEntityPrivateD1Ev
namespace Qt3DExtras {
inline QText2DEntityPrivate::~QText2DEntityPrivate()
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtext2dentity.cpp, line 174, as _ZNK10Qt3DExtras20QText2DEntityPrivate18computeActualScaleEv
namespace Qt3DExtras {
inline qreal QText2DEntityPrivate::computeActualScale() const
{
    // scale font based on fontScale property and given QFont
    float scale = 1.0f;
    if (m_font.pointSizeF() > 0)
        scale *= m_font.pointSizeF() / m_scaledFont.pointSizeF();
    return scale;
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QText2DEntityPrivate that Python can take functions over in. Every Qt3DExtras::QText2DEntityPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QText2DEntityPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QText2DEntityPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QText2DEntityPrivate : public Qt3DExtras::QText2DEntityPrivate {
public:
  using Qt3DExtras::QText2DEntityPrivate::QText2DEntityPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DExtras::QText2DEntityPrivate::setScene(Qt3DCore::QScene
  //      *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QText2DEntityPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DExtras::QText2DEntityPrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QText2DEntityPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QText2DEntityPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QText2DEntityPrivate::~QText2DEntityPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras20QText2DEntityPrivateD1Ev(
    Qt3DExtras::QText2DEntityPrivate *self) {
  delete self;
}

//  QText2DEntity *Qt3DExtras::QText2DEntityPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QText2DEntity *ritual_ZN10Qt3DExtras20QText2DEntityPrivate6q_funcEv(
    Qt3DExtras::QText2DEntityPrivate *self) {
  return self->q_func();
}

//  const QText2DEntity *Qt3DExtras::QText2DEntityPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QText2DEntity *ritual_ZNK10Qt3DExtras20QText2DEntityPrivate6q_funcEv(
    const Qt3DExtras::QText2DEntityPrivate *self) {
  return self->q_func();
}

//  void Qt3DExtras::QText2DEntityPrivate::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras20QText2DEntityPrivate8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DExtras::QText2DEntityPrivate *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  qreal Qt3DExtras::QText2DEntityPrivate::computeActualScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10Qt3DExtras20QText2DEntityPrivate18computeActualScaleEv(
    const Qt3DExtras::QText2DEntityPrivate *self) {
  return self->computeActualScale();
}

//  a Python function taken by a CuteQt3DExtras_QText2DEntityPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QText2DEntityPrivate(
    Qt3DExtras::QText2DEntityPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QText2DEntityPrivate *>(self)->take(key, call);
}
