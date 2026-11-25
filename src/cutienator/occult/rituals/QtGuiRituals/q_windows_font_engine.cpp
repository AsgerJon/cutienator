//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontengine_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again. Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its header
//  writes out. Not written: the constructor, 'initFontInfo',
//  'selectDesignFont', 'getGlyphIndexes', 'getCMap', 'getOutlineMetrics',
//  'drawGDIGlyph', 'hasCFFTable' and 'hasCMapTable', which Qt's library
//  offers not, and 'fontEngineData', which gives a 'QSharedPointer'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontengine_p.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>

//  QWindowsFontEngine::~QWindowsFontEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsFontEngineD1Ev(QWindowsFontEngine *self) {
  delete self;
}

//  QFixed QWindowsFontEngine::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK18QWindowsFontEngine13lineThicknessEv(
    const QWindowsFontEngine *self) {
  return new QFixed(self->lineThickness());
}

//  Properties QWindowsFontEngine::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_ZNK18QWindowsFontEngine10propertiesEv(
    const QWindowsFontEngine *self) {
  return new QFontEngine::Properties(self->properties());
}

//  void QWindowsFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath
//      *path, glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QWindowsFontEngine *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->getUnscaledGlyph(glyph, path, metrics);
}

//  FaceId QWindowsFontEngine::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_ZNK18QWindowsFontEngine6faceIdEv(
    const QWindowsFontEngine *self) {
  return new QFontEngine::FaceId(self->faceId());
}

//  bool QWindowsFontEngine::getSfntTableData(uint tag, uchar *buffer, uint
//      *length) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsFontEngine16getSfntTableDataEjPhPj(
    const QWindowsFontEngine *self,
    uint tag,
    uchar *buffer,
    uint *length) {
  return self->getSfntTableData(tag, buffer, length);
}

//  int QWindowsFontEngine::synthesized() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWindowsFontEngine11synthesizedEv(
    const QWindowsFontEngine *self) {
  return self->synthesized();
}

//  QFixed QWindowsFontEngine::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK18QWindowsFontEngine12emSquareSizeEv(
    const QWindowsFontEngine *self) {
  return new QFixed(self->emSquareSize());
}

//  glyph_t QWindowsFontEngine::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK18QWindowsFontEngine10glyphIndexEj(
    const QWindowsFontEngine *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  int QWindowsFontEngine::stringToCMap(const QChar *str, int len,
//      QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWindowsFontEngine12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QWindowsFontEngine *self,
    const QChar *str,
    int len,
    QGlyphLayout *glyphs,
    int *nglyphs,
    int flags) {
  return self->stringToCMap(
      str, len, glyphs, nglyphs,
      QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  void QWindowsFontEngine::recalcAdvances(QGlyphLayout *glyphs, ShaperFlags
//      a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QWindowsFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QWindowsFontEngine *self,
    QGlyphLayout *glyphs,
    int a1) {
  self->recalcAdvances(glyphs, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QWindowsFontEngine::addOutlineToPath(qreal x, qreal y, const
//      QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QWindowsFontEngine *self,
    qreal x,
    qreal y,
    const QGlyphLayout *glyphs,
    QPainterPath *path,
    int flags) {
  self->addOutlineToPath(
      x, y, *glyphs, path, QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  void QWindowsFontEngine::addGlyphsToPath(glyph_t *glyphs, QFixedPoint
//      *positions, int nglyphs, QPainterPath *path, QTextItem::RenderFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsFontEngine15addGlyphsToPathEPjP11QFixedPointiP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QWindowsFontEngine *self,
    glyph_t *glyphs,
    QFixedPoint *positions,
    int nglyphs,
    QPainterPath *path,
    int flags) {
  self->addGlyphsToPath(
      glyphs, positions, nglyphs, path,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  glyph_metrics_t QWindowsFontEngine::boundingBox(glyph_t g)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN18QWindowsFontEngine11boundingBoxEj(
    QWindowsFontEngine *self,
    glyph_t g) {
  return new glyph_metrics_t(self->boundingBox(g));
}

//  glyph_metrics_t QWindowsFontEngine::boundingBox(glyph_t g, const
//      QTransform &t)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN18QWindowsFontEngine11boundingBoxEjRK10QTransform(
    QWindowsFontEngine *self,
    glyph_t g,
    const QTransform *t) {
  return new glyph_metrics_t(self->boundingBox(g, *t));
}

//  QFixed QWindowsFontEngine::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK18QWindowsFontEngine7xHeightEv(
    const QWindowsFontEngine *self) {
  return new QFixed(self->xHeight());
}

//  QFixed QWindowsFontEngine::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK18QWindowsFontEngine9capHeightEv(
    const QWindowsFontEngine *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QWindowsFontEngine::averageCharWidth() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK18QWindowsFontEngine16averageCharWidthEv(
    const QWindowsFontEngine *self) {
  return new QFixed(self->averageCharWidth());
}

//  qreal QWindowsFontEngine::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWindowsFontEngine12maxCharWidthEv(
    const QWindowsFontEngine *self) {
  return self->maxCharWidth();
}

//  qreal QWindowsFontEngine::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWindowsFontEngine14minLeftBearingEv(
    const QWindowsFontEngine *self) {
  return self->minLeftBearing();
}

//  qreal QWindowsFontEngine::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWindowsFontEngine15minRightBearingEv(
    const QWindowsFontEngine *self) {
  return self->minRightBearing();
}

//  QImage QWindowsFontEngine::alphaMapForGlyph(glyph_t t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QWindowsFontEngine16alphaMapForGlyphEj(
    QWindowsFontEngine *self,
    glyph_t t) {
  return new QImage(self->alphaMapForGlyph(t));
}

//  QImage QWindowsFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform
//      &xform)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QWindowsFontEngine16alphaMapForGlyphEjRK10QTransform(
    QWindowsFontEngine *self,
    glyph_t a0,
    const QTransform *xform) {
  return new QImage(self->alphaMapForGlyph(a0, *xform));
}

//  QImage QWindowsFontEngine::alphaRGBMapForGlyph(glyph_t t, const
//      QFixedPoint &subPixelPosition, const QTransform &xform)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QWindowsFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QWindowsFontEngine *self,
    glyph_t t,
    const QFixedPoint *subPixelPosition,
    const QTransform *xform) {
  return new QImage(self->alphaRGBMapForGlyph(t, *subPixelPosition, *xform));
}

//  glyph_metrics_t QWindowsFontEngine::alphaMapBoundingBox(glyph_t glyph,
//      const QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN18QWindowsFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformN11QFontEngine11GlyphFormatE(
    QWindowsFontEngine *self,
    glyph_t glyph,
    const QFixedPoint *a1,
    const QTransform *matrix,
    QFontEngine::GlyphFormat a3) {
  return new glyph_metrics_t(
      self->alphaMapBoundingBox(glyph, *a1, *matrix, a3));
}

//  QFontEngine *QWindowsFontEngine::cloneWithSize(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK18QWindowsFontEngine13cloneWithSizeEd(
    const QWindowsFontEngine *self,
    qreal pixelSize) {
  return self->cloneWithSize(pixelSize);
}

//  Qt::HANDLE QWindowsFontEngine::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK18QWindowsFontEngine6handleEv(
    const QWindowsFontEngine *self) {
  return self->handle();
}

//  bool QWindowsFontEngine::supportsTransformation(const QTransform
//      &transform) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsFontEngine22supportsTransformationERK10QTransform(
    const QWindowsFontEngine *self,
    const QTransform *transform) {
  return self->supportsTransformation(*transform);
}

#if !defined(Q_CC_MINGW)
//  void QWindowsFontEngine::getGlyphBearings(glyph_t glyph, qreal
//      *leftBearing, qreal *rightBearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsFontEngine16getGlyphBearingsEjPdS0_(
    QWindowsFontEngine *self,
    glyph_t glyph,
    qreal *leftBearing,
    qreal *rightBearing) {
  self->getGlyphBearings(glyph, leftBearing, rightBearing);
}
#endif  // !defined(Q_CC_MINGW)

//  bool QWindowsFontEngine::hasUnreliableGlyphOutline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWindowsFontEngine25hasUnreliableGlyphOutlineEv(
    const QWindowsFontEngine *self) {
  return self->hasUnreliableGlyphOutline();
}

//  void QWindowsFontEngine::setUniqueFamilyName(const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWindowsFontEngine19setUniqueFamilyNameERK7QString(
    QWindowsFontEngine *self,
    const QString *newName) {
  self->setUniqueFamilyName(*newName);
}

//  void QWindowsFontEngine::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QWindowsFontEngine23initializeHeightMetricsEv(
    const QWindowsFontEngine *self) {
  self->initializeHeightMetrics();
}

#endif  // defined(Q_OS_WIN)
