//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsfontenginedirectwrite_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. DirectWrite's interfaces and structs are passed
//  as addresses, its enums as numbers. Not written: the constructor and
//  'fontEngineData', which pass a 'QSharedPointer'; with no constructor
//  to make one, no Cute class either.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(directwrite)
#include <QtGui/6.12.0/QtGui/private/qwindowsfontenginedirectwrite_p.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#include <QtGui/qfontvariableaxis.h>

//  QWindowsFontEngineDirectWrite::~QWindowsFontEngineDirectWrite()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowsFontEngineDirectWriteD1Ev(
    QWindowsFontEngineDirectWrite *self) {
  delete self;
}

//  void QWindowsFontEngineDirectWrite::initFontInfo(const QFontDef &request,
//      int dpi)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowsFontEngineDirectWrite12initFontInfoERK8QFontDefi(
    QWindowsFontEngineDirectWrite *self,
    const QFontDef *request,
    int dpi) {
  self->initFontInfo(*request, dpi);
}

//  QFixed QWindowsFontEngineDirectWrite::lineThickness() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK29QWindowsFontEngineDirectWrite13lineThicknessEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFixed(self->lineThickness());
}

//  QFixed QWindowsFontEngineDirectWrite::underlinePosition() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK29QWindowsFontEngineDirectWrite17underlinePositionEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFixed(self->underlinePosition());
}

//  bool QWindowsFontEngineDirectWrite::getSfntTableData(uint tag, uchar
//      *buffer, uint *length) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite16getSfntTableDataEjPhPj(
    const QWindowsFontEngineDirectWrite *self,
    uint tag,
    uchar *buffer,
    uint *length) {
  return self->getSfntTableData(tag, buffer, length);
}

//  QFixed QWindowsFontEngineDirectWrite::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK29QWindowsFontEngineDirectWrite12emSquareSizeEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFixed(self->emSquareSize());
}

//  glyph_t QWindowsFontEngineDirectWrite::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK29QWindowsFontEngineDirectWrite10glyphIndexEj(
    const QWindowsFontEngineDirectWrite *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  int QWindowsFontEngineDirectWrite::stringToCMap(const QChar *str, int
//      len, QGlyphLayout *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QWindowsFontEngineDirectWrite12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QWindowsFontEngineDirectWrite *self,
    const QChar *str,
    int len,
    QGlyphLayout *glyphs,
    int *nglyphs,
    int flags) {
  return self->stringToCMap(
      str, len, glyphs, nglyphs,
      QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  void QWindowsFontEngineDirectWrite::recalcAdvances(QGlyphLayout *glyphs,
//      ShaperFlags a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QWindowsFontEngineDirectWrite14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QWindowsFontEngineDirectWrite *self,
    QGlyphLayout *glyphs,
    int a1) {
  self->recalcAdvances(glyphs, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QWindowsFontEngineDirectWrite::addGlyphsToPath(glyph_t *glyphs,
//      QFixedPoint *positions, int nglyphs, QPainterPath *path,
//      QTextItem::RenderFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowsFontEngineDirectWrite15addGlyphsToPathEPjP11QFixedPointiP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QWindowsFontEngineDirectWrite *self,
    glyph_t *glyphs,
    QFixedPoint *positions,
    int nglyphs,
    QPainterPath *path,
    int flags) {
  self->addGlyphsToPath(
      glyphs, positions, nglyphs, path,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  glyph_metrics_t QWindowsFontEngineDirectWrite::boundingBox(const
//      QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN29QWindowsFontEngineDirectWrite11boundingBoxERK12QGlyphLayout(
    QWindowsFontEngineDirectWrite *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->boundingBox(*glyphs));
}

//  glyph_metrics_t QWindowsFontEngineDirectWrite::boundingBox(glyph_t g)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN29QWindowsFontEngineDirectWrite11boundingBoxEj(
    QWindowsFontEngineDirectWrite *self,
    glyph_t g) {
  return new glyph_metrics_t(self->boundingBox(g));
}

//  glyph_metrics_t
//      QWindowsFontEngineDirectWrite::alphaMapBoundingBox(glyph_t glyph,
//      const QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN29QWindowsFontEngineDirectWrite19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformN11QFontEngine11GlyphFormatE(
    QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    const QFixedPoint *a1,
    const QTransform *matrix,
    QFontEngine::GlyphFormat a3) {
  return new glyph_metrics_t(
      self->alphaMapBoundingBox(glyph, *a1, *matrix, a3));
}

//  QFixed QWindowsFontEngineDirectWrite::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK29QWindowsFontEngineDirectWrite9capHeightEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QWindowsFontEngineDirectWrite::xHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK29QWindowsFontEngineDirectWrite7xHeightEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFixed(self->xHeight());
}

//  qreal QWindowsFontEngineDirectWrite::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QWindowsFontEngineDirectWrite12maxCharWidthEv(
    const QWindowsFontEngineDirectWrite *self) {
  return self->maxCharWidth();
}

//  FaceId QWindowsFontEngineDirectWrite::faceId() const
extern "C" Q_DECL_EXPORT
QFontEngine::FaceId *ritual_ZNK29QWindowsFontEngineDirectWrite6faceIdEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFontEngine::FaceId(self->faceId());
}

//  bool QWindowsFontEngineDirectWrite::supportsHorizontalSubPixelPositions()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite35supportsHorizontalSubPixelPositionsEv(
    const QWindowsFontEngineDirectWrite *self) {
  return self->supportsHorizontalSubPixelPositions();
}

//  HFONT QWindowsFontEngineDirectWrite::createHFONT() const
extern "C" Q_DECL_EXPORT
HFONT ritual_ZNK29QWindowsFontEngineDirectWrite11createHFONTEv(
    const QWindowsFontEngineDirectWrite *self) {
  return self->createHFONT();
}

//  QImage QWindowsFontEngineDirectWrite::alphaMapForGlyph(glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN29QWindowsFontEngineDirectWrite16alphaMapForGlyphEjRK11QFixedPoint(
    QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  return new QImage(self->alphaMapForGlyph(glyph, *subPixelPosition));
}

//  QImage QWindowsFontEngineDirectWrite::alphaMapForGlyph(glyph_t glyph,
//      const QFixedPoint &subPixelPosition, const QTransform &t)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN29QWindowsFontEngineDirectWrite16alphaMapForGlyphEjRK11QFixedPointRK10QTransform(
    QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition,
    const QTransform *t) {
  return new QImage(self->alphaMapForGlyph(glyph, *subPixelPosition, *t));
}

//  QImage QWindowsFontEngineDirectWrite::alphaRGBMapForGlyph(glyph_t t,
//      const QFixedPoint &subPixelPosition, const QTransform &xform)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN29QWindowsFontEngineDirectWrite19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform(
    QWindowsFontEngineDirectWrite *self,
    glyph_t t,
    const QFixedPoint *subPixelPosition,
    const QTransform *xform) {
  return new QImage(self->alphaRGBMapForGlyph(t, *subPixelPosition, *xform));
}

//  QImage QWindowsFontEngineDirectWrite::bitmapForGlyph(glyph_t a0, const
//      QFixedPoint &subPixelPosition, const QTransform &t, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN29QWindowsFontEngineDirectWrite14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor(
    QWindowsFontEngineDirectWrite *self,
    glyph_t a0,
    const QFixedPoint *subPixelPosition,
    const QTransform *t,
    const QColor *color) {
  return new QImage(self->bitmapForGlyph(a0, *subPixelPosition, *t, *color));
}

//  QFontEngine *QWindowsFontEngineDirectWrite::cloneWithSize(qreal
//      pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK29QWindowsFontEngineDirectWrite13cloneWithSizeEd(
    const QWindowsFontEngineDirectWrite *self,
    qreal pixelSize) {
  return self->cloneWithSize(pixelSize);
}

//  Qt::HANDLE QWindowsFontEngineDirectWrite::handle() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK29QWindowsFontEngineDirectWrite6handleEv(
    const QWindowsFontEngineDirectWrite *self) {
  return self->handle();
}

//  QString QWindowsFontEngineDirectWrite::fontNameSubstitute(const QString
//      &familyName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QWindowsFontEngineDirectWrite18fontNameSubstituteERK7QString(
    const QString *familyName) {
  return new QString(QWindowsFontEngineDirectWrite::fontNameSubstitute(*familyName));
}

//  IDWriteFontFace *QWindowsFontEngineDirectWrite::directWriteFontFace()
//      const
extern "C" Q_DECL_EXPORT
IDWriteFontFace *ritual_ZNK29QWindowsFontEngineDirectWrite19directWriteFontFaceEv(
    const QWindowsFontEngineDirectWrite *self) {
  return self->directWriteFontFace();
}

//  void QWindowsFontEngineDirectWrite::setUniqueFamilyName(const QString
//      &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowsFontEngineDirectWrite19setUniqueFamilyNameERK7QString(
    QWindowsFontEngineDirectWrite *self,
    const QString *newName) {
  self->setUniqueFamilyName(*newName);
}

//  void QWindowsFontEngineDirectWrite::initializeHeightMetrics() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QWindowsFontEngineDirectWrite23initializeHeightMetricsEv(
    const QWindowsFontEngineDirectWrite *self) {
  self->initializeHeightMetrics();
}

//  Properties QWindowsFontEngineDirectWrite::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_ZNK29QWindowsFontEngineDirectWrite10propertiesEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QFontEngine::Properties(self->properties());
}

//  QPainterPath QWindowsFontEngineDirectWrite::unscaledGlyph(glyph_t glyph)
//      const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK29QWindowsFontEngineDirectWrite13unscaledGlyphEj(
    const QWindowsFontEngineDirectWrite *self,
    glyph_t glyph) {
  return new QPainterPath(self->unscaledGlyph(glyph));
}

//  void QWindowsFontEngineDirectWrite::getUnscaledGlyph(glyph_t glyph,
//      QPainterPath *path, glyph_metrics_t *metrics)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowsFontEngineDirectWrite16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t(
    QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    QPainterPath *path,
    glyph_metrics_t *metrics) {
  self->getUnscaledGlyph(glyph, path, metrics);
}

//  QList<QFontVariableAxis> QWindowsFontEngineDirectWrite::variableAxes()
//      const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK29QWindowsFontEngineDirectWrite12variableAxesEv(
    const QWindowsFontEngineDirectWrite *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  bool QWindowsFontEngineDirectWrite::expectsGammaCorrectedBlending(QFontEn
//      gine::GlyphFormat format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite29expectsGammaCorrectedBlendingEN11QFontEngine11GlyphFormatE(
    const QWindowsFontEngineDirectWrite *self,
    QFontEngine::GlyphFormat format) {
  return self->expectsGammaCorrectedBlending(format);
}

#if QT_CONFIG(directwritecolrv1)
//  bool QWindowsFontEngineDirectWrite::traverseColr1(IDWritePaintReader
//      *paintReader, IDWriteFontFace7 *face7, const DWRITE_PAINT_ELEMENT
//      *paintElement, QColrPaintGraphRenderer *graphRenderer) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite13traverseColr1EP18IDWritePaintReaderP16IDWriteFontFace7PK20DWRITE_PAINT_ELEMENTP23QColrPaintGraphRenderer(
    const QWindowsFontEngineDirectWrite *self,
    IDWritePaintReader *paintReader,
    IDWriteFontFace7 *face7,
    const DWRITE_PAINT_ELEMENT *paintElement,
    QColrPaintGraphRenderer *graphRenderer) {
  return self->traverseColr1(paintReader, face7, paintElement, graphRenderer);
}
#endif  // QT_CONFIG(directwritecolrv1)

#if QT_CONFIG(directwritecolrv1)
//  bool QWindowsFontEngineDirectWrite::renderColr1GlyphRun(QImage *image,
//      const DWRITE_GLYPH_RUN *glyphRun, const DWRITE_MATRIX &transform,
//      QColor color) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite19renderColr1GlyphRunEP6QImagePK16DWRITE_GLYPH_RUNRK13DWRITE_MATRIX6QColor(
    const QWindowsFontEngineDirectWrite *self,
    QImage *image,
    const DWRITE_GLYPH_RUN *glyphRun,
    const DWRITE_MATRIX *transform,
    const QColor *color) {
  return self->renderColr1GlyphRun(image, glyphRun, *transform, *color);
}
#endif  // QT_CONFIG(directwritecolrv1)

//  QRect QWindowsFontEngineDirectWrite::paintGraphBounds(glyph_t glyph,
//      const DWRITE_MATRIX &transform) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK29QWindowsFontEngineDirectWrite16paintGraphBoundsEjRK13DWRITE_MATRIX(
    const QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    const DWRITE_MATRIX *transform) {
  return new QRect(self->paintGraphBounds(glyph, *transform));
}

//  QRect QWindowsFontEngineDirectWrite::alphaTextureBounds(glyph_t glyph,
//      const DWRITE_MATRIX &transform)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN29QWindowsFontEngineDirectWrite18alphaTextureBoundsEjRK13DWRITE_MATRIX(
    QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    const DWRITE_MATRIX *transform) {
  return new QRect(self->alphaTextureBounds(glyph, *transform));
}

//  QRect QWindowsFontEngineDirectWrite::colorBitmapBounds(glyph_t glyph,
//      const DWRITE_MATRIX &transform)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN29QWindowsFontEngineDirectWrite17colorBitmapBoundsEjRK13DWRITE_MATRIX(
    QWindowsFontEngineDirectWrite *self,
    glyph_t glyph,
    const DWRITE_MATRIX *transform) {
  return new QRect(self->colorBitmapBounds(glyph, *transform));
}

//  bool QWindowsFontEngineDirectWrite::renderColr0GlyphRun(QImage *image,
//      const DWRITE_COLOR_GLYPH_RUN *colorGlyphRun, const DWRITE_MATRIX
//      &transform, DWRITE_RENDERING_MODE renderMode, DWRITE_MEASURING_MODE
//      measureMode, DWRITE_GRID_FIT_MODE gridFitMode, QColor color, QRect
//      boundingRect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite19renderColr0GlyphRunEP6QImagePK22DWRITE_COLOR_GLYPH_RUNRK13DWRITE_MATRIX21DWRITE_RENDERING_MODE21DWRITE_MEASURING_MODE20DWRITE_GRID_FIT_MODE6QColor5QRect(
    const QWindowsFontEngineDirectWrite *self,
    QImage *image,
    const DWRITE_COLOR_GLYPH_RUN *colorGlyphRun,
    const DWRITE_MATRIX *transform,
    DWRITE_RENDERING_MODE renderMode,
    DWRITE_MEASURING_MODE measureMode,
    DWRITE_GRID_FIT_MODE gridFitMode,
    const QColor *color,
    const QRect *boundingRect) {
  return self->renderColr0GlyphRun(
      image, colorGlyphRun, *transform, renderMode, measureMode,
      gridFitMode, *color, *boundingRect);
}

//  QImage QWindowsFontEngineDirectWrite::renderColorGlyph(DWRITE_GLYPH_RUN
//      *glyphRun, const DWRITE_MATRIX &transform, DWRITE_RENDERING_MODE
//      renderMode, DWRITE_MEASURING_MODE measureMode, DWRITE_GRID_FIT_MODE
//      gridFitMode, QColor color, QRect boundingRect) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK29QWindowsFontEngineDirectWrite16renderColorGlyphEP16DWRITE_GLYPH_RUNRK13DWRITE_MATRIX21DWRITE_RENDERING_MODE21DWRITE_MEASURING_MODE20DWRITE_GRID_FIT_MODE6QColor5QRect(
    const QWindowsFontEngineDirectWrite *self,
    DWRITE_GLYPH_RUN *glyphRun,
    const DWRITE_MATRIX *transform,
    DWRITE_RENDERING_MODE renderMode,
    DWRITE_MEASURING_MODE measureMode,
    DWRITE_GRID_FIT_MODE gridFitMode,
    const QColor *color,
    const QRect *boundingRect) {
  return new QImage(self->renderColorGlyph(
      glyphRun, *transform, renderMode, measureMode,
      gridFitMode, *color, *boundingRect));
}

//  QImage QWindowsFontEngineDirectWrite::imageForGlyph(glyph_t t, const
//      QFixedPoint &subPixelPosition, int margin, const QTransform &xform,
//      const QColor &color)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN29QWindowsFontEngineDirectWrite13imageForGlyphEjRK11QFixedPointiRK10QTransformRK6QColor(
    QWindowsFontEngineDirectWrite *self,
    glyph_t t,
    const QFixedPoint *subPixelPosition,
    int margin,
    const QTransform *xform,
    const QColor *color) {
  return new QImage(self->imageForGlyph(t, *subPixelPosition, margin, *xform, *color));
}

//  void QWindowsFontEngineDirectWrite::collectMetrics()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowsFontEngineDirectWrite14collectMetricsEv(
    QWindowsFontEngineDirectWrite *self) {
  self->collectMetrics();
}

//  void QWindowsFontEngineDirectWrite::renderGlyphRun(QImage *destination,
//      float r, float g, float b, float a, IDWriteGlyphRunAnalysis
//      *glyphAnalysis, const QRect &boundingRect, DWRITE_RENDERING_MODE
//      renderMode) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QWindowsFontEngineDirectWrite14renderGlyphRunEP6QImageffffP23IDWriteGlyphRunAnalysisRK5QRect21DWRITE_RENDERING_MODE(
    const QWindowsFontEngineDirectWrite *self,
    QImage *destination,
    float r,
    float g,
    float b,
    float a,
    IDWriteGlyphRunAnalysis *glyphAnalysis,
    const QRect *boundingRect,
    DWRITE_RENDERING_MODE renderMode) {
  self->renderGlyphRun(destination, r, g, b, a, glyphAnalysis, *boundingRect, renderMode);
}

//  QString
//      QWindowsFontEngineDirectWrite::filenameFromFontFile(IDWriteFontFile
//      *fontFile)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QWindowsFontEngineDirectWrite20filenameFromFontFileEP15IDWriteFontFile(
    IDWriteFontFile *fontFile) {
  return new QString(QWindowsFontEngineDirectWrite::filenameFromFontFile(fontFile));
}

//  DWRITE_RENDERING_MODE
//      QWindowsFontEngineDirectWrite::hintingPreferenceToRenderingMode(const
//      QFontDef &fontDef) const
extern "C" Q_DECL_EXPORT
DWRITE_RENDERING_MODE ritual_ZNK29QWindowsFontEngineDirectWrite32hintingPreferenceToRenderingModeERK8QFontDef(
    const QWindowsFontEngineDirectWrite *self,
    const QFontDef *fontDef) {
  return self->hintingPreferenceToRenderingMode(*fontDef);
}

//  bool QWindowsFontEngineDirectWrite::useSymmetricAntialiasing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowsFontEngineDirectWrite24useSymmetricAntialiasingEv(
    const QWindowsFontEngineDirectWrite *self) {
  return self->useSymmetricAntialiasing();
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(directwrite)
