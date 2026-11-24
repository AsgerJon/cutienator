//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgcurveglyphatlas_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgcurveglyphatlas_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtCore/qpoint.h>

//  QSGCurveGlyphAtlas::QSGCurveGlyphAtlas(const QRawFont &font)
extern "C" Q_DECL_EXPORT
QSGCurveGlyphAtlas *ritual_ZN18QSGCurveGlyphAtlasC1ERK8QRawFont(
    const QRawFont *font) {
  return new QSGCurveGlyphAtlas(*font);
}

//  QSGCurveGlyphAtlas::~QSGCurveGlyphAtlas()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGCurveGlyphAtlasD1Ev(QSGCurveGlyphAtlas *self) {
  delete self;
}

//  void QSGCurveGlyphAtlas::addGlyph(QSGCurveFillNode *node, glyph_t glyph,
//      const QPointF &position, qreal pixelSize) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QSGCurveGlyphAtlas8addGlyphEP16QSGCurveFillNodejRK7QPointFd(
    const QSGCurveGlyphAtlas *self,
    QSGCurveFillNode *node,
    glyph_t glyph,
    const QPointF *position,
    qreal pixelSize) {
  self->addGlyph(node, glyph, *position, pixelSize);
}

//  qreal QSGCurveGlyphAtlas::fontSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QSGCurveGlyphAtlas8fontSizeEv(
    const QSGCurveGlyphAtlas *self) {
  return self->fontSize();
}
