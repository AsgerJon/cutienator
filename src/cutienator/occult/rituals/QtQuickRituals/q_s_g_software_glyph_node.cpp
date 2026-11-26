//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwareglyphnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwareglyphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwareglyphnode_p.h>
#include <QtGui/private/qrawfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 20, as local:qsgsoftwareglyphnode.cpp:calculateBoundingRect
namespace {
inline QRectF calculateBoundingRect(const QPointF &position, const QGlyphRun &glyphs)
{
    QFixed minX;
    QFixed minY;
    QFixed maxX;
    QFixed maxY;

    QRawFontPrivate *rawFontD = QRawFontPrivate::get(glyphs.rawFont());
    QFontEngine *fontEngine = rawFontD->fontEngine;

    QFontEngine::GlyphFormat glyphFormat = fontEngine->glyphFormat != QFontEngine::Format_None ? fontEngine->glyphFormat : QFontEngine::Format_A32;

    int margin = fontEngine->glyphMargin(glyphFormat);

    const QList<uint> glyphIndexes = glyphs.glyphIndexes();
    const QList<QPointF> glyphPositions = glyphs.positions();
    for (int i = 0, n = qMin(glyphIndexes.size(), glyphPositions.size()); i < n; ++i) {
        glyph_metrics_t gm = fontEngine->alphaMapBoundingBox(glyphIndexes.at(i), QFixedPoint(), QTransform(), glyphFormat);

        gm.x += QFixed::fromReal(glyphPositions.at(i).x()) - margin;
        gm.y += QFixed::fromReal(glyphPositions.at(i).y()) - margin;

        if (i == 0) {
            minX = gm.x;
            minY = gm.y;
            maxX = gm.x + gm.width;
            maxY = gm.y + gm.height;
        } else {
            minX = qMin(gm.x, minX);
            minY = qMin(gm.y, minY);
            maxX = qMax(gm.x + gm.width, maxX);
            maxY = qMax(gm.y + gm.height, maxY);
        }
    }

    QRectF boundingRect(QPointF(minX.toReal(), minY.toReal()), QPointF(maxX.toReal(), maxY.toReal()));
    return boundingRect.translated(position - QPointF(0.0, glyphs.rawFont().ascent()));
}
}  // namespace

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 60, as _ZN20QSGSoftwareGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun
inline void QSGSoftwareGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun &glyphs)
{
    m_position = position;
    m_glyphRun = glyphs;
    // Decorations handled by text node
    m_glyphRun.setOverline(false);
    m_glyphRun.setStrikeOut(false);
    m_glyphRun.setUnderline(false);

    recalculateBoundingRect();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 82, as _ZN20QSGSoftwareGlyphNode8setColorERK6QColor
inline void QSGSoftwareGlyphNode::setColor(const QColor &color)
{
    m_color = color;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 87, as _ZN20QSGSoftwareGlyphNode8setStyleEN10QQuickText9TextStyleE
inline void QSGSoftwareGlyphNode::setStyle(QQuickText::TextStyle style)
{
    m_style = style;

    recalculateBoundingRect();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 94, as _ZN20QSGSoftwareGlyphNode13setStyleColorERK6QColor
inline void QSGSoftwareGlyphNode::setStyleColor(const QColor &color)
{
    m_styleColor = color;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 99, as _ZNK20QSGSoftwareGlyphNode8baseLineEv
inline QPointF QSGSoftwareGlyphNode::baseLine() const
{
    return QPointF();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 104, as _ZN20QSGSoftwareGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE
inline void QSGSoftwareGlyphNode::setPreferredAntialiasingMode(QSGGlyphNode::AntialiasingMode)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 108, as _ZN20QSGSoftwareGlyphNode6updateEv
inline void QSGSoftwareGlyphNode::update()
{
    if (m_recycled) {
        markDirty(DirtyGeometry);
        m_recycled = false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 148, as _ZN20QSGSoftwareGlyphNode7recycleEv
inline void QSGSoftwareGlyphNode::recycle()
{
    QSGGlyphNode::recycle();
    m_position = QPointF{};
    m_glyphRun = QGlyphRun{};
    m_color = QColor{};
    m_geometry.allocate(0, 0);
    m_style = QQuickText::Normal;
    m_styleColor = QColor{};
    m_recycled = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 10, as _ZN20QSGSoftwareGlyphNodeC1Ev
inline QSGSoftwareGlyphNode::QSGSoftwareGlyphNode()
    : QSGGlyphNode(QSGTextNode::NativeRendering)
    , m_geometry(QSGGeometry::defaultAttributes_TexturedPoint2D(), 0)
    , m_style(QQuickText::Normal)
{
    setMaterial((QSGMaterial*)1);
    setGeometry(&m_geometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 116, as _ZN20QSGSoftwareGlyphNode5paintEP8QPainter
inline void QSGSoftwareGlyphNode::paint(QPainter *painter)
{
    painter->setBrush(QBrush());
    QPointF pos = m_position - QPointF(0, m_glyphRun.rawFont().ascent());

    qreal offset = 1.0;
    if (painter->device()->devicePixelRatio() > 0.0)
        offset = 1.0 / painter->device()->devicePixelRatio();

    switch (m_style) {
    case QQuickText::Normal: break;
    case QQuickText::Outline:
        painter->setPen(m_styleColor);
        painter->drawGlyphRun(pos + QPointF(0, offset), m_glyphRun);
        painter->drawGlyphRun(pos + QPointF(0, -offset), m_glyphRun);
        painter->drawGlyphRun(pos + QPointF(offset, 0), m_glyphRun);
        painter->drawGlyphRun(pos + QPointF(-offset, 0), m_glyphRun);
        break;
    case QQuickText::Raised:
        painter->setPen(m_styleColor);
        painter->drawGlyphRun(pos + QPointF(0, offset), m_glyphRun);
        break;
    case QQuickText::Sunken:
        painter->setPen(m_styleColor);
        painter->drawGlyphRun(pos + QPointF(0, -offset), m_glyphRun);
        break;
    }

    painter->setPen(m_color);
    painter->drawGlyphRun(pos, m_glyphRun);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 72, as _ZN20QSGSoftwareGlyphNode23recalculateBoundingRectEv
inline void QSGSoftwareGlyphNode::recalculateBoundingRect()
{
    int x1Offset = m_style == QQuickText::Outline ? -1 : 0;
    int x2Offset = m_style == QQuickText::Outline ? 1 : 0;
    int y1Offset = m_style == QQuickText::Outline || m_style == QQuickText::Sunken ? -1 : 0;
    int y2Offset = m_style == QQuickText::Outline || m_style == QQuickText::Raised ? 1 : 0;

    m_bounding_rect = calculateBoundingRect(m_position, m_glyphRun).adjusted(x1Offset, y1Offset, x2Offset, y2Offset);
}
//  -----------------------------------------------------------------------

//  QSGSoftwareGlyphNode::QSGSoftwareGlyphNode()
extern "C" Q_DECL_EXPORT
QSGSoftwareGlyphNode *ritual_ZN20QSGSoftwareGlyphNodeC1Ev() {
  return new QSGSoftwareGlyphNode();
}

//  void QSGSoftwareGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGSoftwareGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->setGlyphs(*position, *glyphs);
}

//  void QSGSoftwareGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode8setColorERK6QColor(
    QSGSoftwareGlyphNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGSoftwareGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGSoftwareGlyphNode *self,
    QQuickText::TextStyle style) {
  self->setStyle(style);
}

//  void QSGSoftwareGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode13setStyleColorERK6QColor(
    QSGSoftwareGlyphNode *self,
    const QColor *color) {
  self->setStyleColor(*color);
}

//  QPointF QSGSoftwareGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK20QSGSoftwareGlyphNode8baseLineEv(
    const QSGSoftwareGlyphNode *self) {
  return new QPointF(self->baseLine());
}

//  void QSGSoftwareGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGSoftwareGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->setPreferredAntialiasingMode(a0);
}

//  void QSGSoftwareGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode6updateEv(QSGSoftwareGlyphNode *self) {
  self->update();
}

//  void QSGSoftwareGlyphNode::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode5paintEP8QPainter(
    QSGSoftwareGlyphNode *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QSGSoftwareGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode7recycleEv(QSGSoftwareGlyphNode *self) {
  self->recycle();
}

//  void QSGSoftwareGlyphNode::recalculateBoundingRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGSoftwareGlyphNode23recalculateBoundingRectEv(
    QSGSoftwareGlyphNode *self) {
  self->recalculateBoundingRect();
}

//  void QSGSoftwareGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGSoftwareGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->QSGSoftwareGlyphNode::setGlyphs(*position, *glyphs);
}

//  void QSGSoftwareGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode8setColorERK6QColor(
    QSGSoftwareGlyphNode *self,
    const QColor *color) {
  self->QSGSoftwareGlyphNode::setColor(*color);
}

//  void QSGSoftwareGlyphNode::setStyle(QQuickText::TextStyle style)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGSoftwareGlyphNode *self,
    QQuickText::TextStyle style) {
  self->QSGSoftwareGlyphNode::setStyle(style);
}

//  void QSGSoftwareGlyphNode::setStyleColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode13setStyleColorERK6QColor(
    QSGSoftwareGlyphNode *self,
    const QColor *color) {
  self->QSGSoftwareGlyphNode::setStyleColor(*color);
}

//  QPointF QSGSoftwareGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK20QSGSoftwareGlyphNode8baseLineEv(
    const QSGSoftwareGlyphNode *self) {
  return new QPointF(self->QSGSoftwareGlyphNode::baseLine());
}

//  void QSGSoftwareGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGSoftwareGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->QSGSoftwareGlyphNode::setPreferredAntialiasingMode(a0);
}

//  void QSGSoftwareGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode6updateEv(
    QSGSoftwareGlyphNode *self) {
  self->QSGSoftwareGlyphNode::update();
}

//  void QSGSoftwareGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGSoftwareGlyphNode7recycleEv(
    QSGSoftwareGlyphNode *self) {
  self->QSGSoftwareGlyphNode::recycle();
}
