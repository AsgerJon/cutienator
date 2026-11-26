//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtGui/qcolor.h>
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qfontengineglyphcache_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformfontdatabase.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvarlengtharray.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qstringiterator_p.h>
#if QT_CONFIG(harfbuzz)
#  include <QtGui/private/qharfbuzzng_p.h>
#endif
#include <algorithm>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/text/qfontengine.cpp, line 1822, as _ZNK14QFontEngineBox10glyphIndexEj
inline glyph_t QFontEngineBox::glyphIndex(uint ucs4) const
{
    Q_UNUSED(ucs4);
    return 1;
}

//  from src/gui/text/qfontengine.cpp, line 1852, as _ZNK14QFontEngineBox14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE
inline void QFontEngineBox::recalcAdvances(QGlyphLayout *glyphs, QFontEngine::ShaperFlags) const
{
    for (int i = 0; i < glyphs->numGlyphs; i++)
        glyphs->advances[i] = _size;
}

//  from src/gui/text/qfontengine.cpp, line 1858, as _ZN14QFontEngineBox16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE
inline void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags flags)
{
    if (!glyphs.numGlyphs)
        return;

    QVarLengthArray<QFixedPoint> positions;
    QVarLengthArray<glyph_t> positioned_glyphs;
    QTransform matrix = QTransform::fromTranslate(x, y - _size);
    getGlyphPositions(glyphs, matrix, flags, positioned_glyphs, positions);

    QSize s(_size - 3, _size - 3);
    for (int k = 0; k < positions.size(); k++)
        path->addRect(QRectF(positions[k].toPointF(), s));
}

//  from src/gui/text/qfontengine.cpp, line 1914, as _ZNK14QFontEngineBox13cloneWithSizeEd
inline QFontEngine *QFontEngineBox::cloneWithSize(qreal pixelSize) const
{
    QFontEngineBox *fe = new QFontEngineBox(pixelSize);
    return fe;
}

//  from src/gui/text/qfontengine.cpp, line 1920, as _ZNK14QFontEngineBox6ascentEv
inline QFixed QFontEngineBox::ascent() const
{
    return _size;
}

//  from src/gui/text/qfontengine.cpp, line 1925, as _ZNK14QFontEngineBox9capHeightEv
inline QFixed QFontEngineBox::capHeight() const
{
    return _size;
}

//  from src/gui/text/qfontengine.cpp, line 1930, as _ZNK14QFontEngineBox7descentEv
inline QFixed QFontEngineBox::descent() const
{
    return 0;
}

//  from src/gui/text/qfontengine.cpp, line 1935, as _ZNK14QFontEngineBox7leadingEv
inline QFixed QFontEngineBox::leading() const
{
    QFixed l = _size * QFixed::fromReal(qreal(0.15));
    return l.ceil();
}

//  from src/gui/text/qfontengine.cpp, line 1941, as _ZNK14QFontEngineBox12maxCharWidthEv
inline qreal QFontEngineBox::maxCharWidth() const
{
    return _size;
}

//  from src/gui/text/qfontengine.cpp, line 1951, as _ZN14QFontEngineBox16alphaMapForGlyphEj
inline QImage QFontEngineBox::alphaMapForGlyph(glyph_t)
{
    QImage image(_size, _size, QImage::Format_Alpha8);
    image.fill(0);

    uchar *bits = image.bits();
    for (int i=2; i <= _size-3; ++i) {
        bits[i + 2 * image.bytesPerLine()] = 255;
        bits[i + (_size - 3) * image.bytesPerLine()] = 255;
        bits[2 + i * image.bytesPerLine()] = 255;
        bits[_size - 3 + i * image.bytesPerLine()] = 255;
    }
    return image;
}

//  from src/gui/text/qfontengine.cpp, line 1946, as _ZNK14QFontEngineBox9canRenderEPK5QChari
inline bool QFontEngineBox::canRender(const QChar *, int) const
{
    return true;
}

//  from src/gui/text/qfontengine.cpp, line 1804, as _ZN14QFontEngineBoxC1Ei
inline QFontEngineBox::QFontEngineBox(int size)
    : QFontEngine(Box),
      _size(size)
{
    cache_cost = sizeof(QFontEngineBox);
}

//  from src/gui/text/qfontengine.cpp, line 1818, as _ZN14QFontEngineBoxD1Ev
inline QFontEngineBox::~QFontEngineBox()
{
}

//  from src/gui/text/qfontengine.cpp, line 1882, as _ZN14QFontEngineBox4drawEP12QPaintEngineddRK12QTextItemInt
inline void QFontEngineBox::draw(QPaintEngine *p, qreal x, qreal y, const QTextItemInt &ti)
{
    if (!ti.glyphs.numGlyphs)
        return;

    // any fixes here should probably also be done in QPaintEnginePrivate::drawBoxTextItem
    QSize s(_size - 3, _size - 3);

    QVarLengthArray<QFixedPoint> positions;
    QVarLengthArray<glyph_t> glyphs;
    QTransform matrix = QTransform::fromTranslate(x, y - _size);
    ti.fontEngine->getGlyphPositions(ti.glyphs, matrix, ti.flags, glyphs, positions);
    if (glyphs.size() == 0)
        return;


    QPainter *painter = p->painter();
    painter->save();
    painter->setBrush(Qt::NoBrush);
    QPen pen = painter->pen();
    pen.setWidthF(lineThickness().toReal());
    painter->setPen(pen);
    for (int k = 0; k < positions.size(); k++)
        painter->drawRect(QRectF(positions[k].toPointF(), s));
    painter->restore();
}
//  -----------------------------------------------------------------------

//  A QFontEngineBox that Python can take functions over in. Every QFontEngineBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef glyph_t (*CuteQFontEngineBoxCall0)(const void *, uint, int *);
typedef void (*CuteQFontEngineBoxCall1)(const void *, QGlyphLayout *, int, int *);
typedef void (*CuteQFontEngineBoxCall2)(const void *, qreal, qreal, const QGlyphLayout *, QPainterPath *, int, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineBoxCall3)(const void *, const QGlyphLayout *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineBoxCall4)(const void *, glyph_t, int *);
typedef void * (*CuteQFontEngineBoxCall5)(const void *, qreal, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall6)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall7)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall8)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall9)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall10)(const void *, int *);
typedef qreal (*CuteQFontEngineBoxCall11)(const void *, int *);
typedef qreal (*CuteQFontEngineBoxCall12)(const void *, int *);
typedef qreal (*CuteQFontEngineBoxCall13)(const void *, int *);
typedef const QImage * (*CuteQFontEngineBoxCall14)(const void *, glyph_t, int *);
typedef bool (*CuteQFontEngineBoxCall15)(const void *, const QChar *, int, int *);
typedef const QFontEngine::Properties * (*CuteQFontEngineBoxCall16)(const void *, int *);
typedef void (*CuteQFontEngineBoxCall17)(const void *, glyph_t, QPainterPath *, glyph_metrics_t *, int *);
typedef const QFontEngine::FaceId * (*CuteQFontEngineBoxCall18)(const void *, int *);
typedef int (*CuteQFontEngineBoxCall19)(const void *, int *);
typedef bool (*CuteQFontEngineBoxCall20)(const void *, int *);
typedef bool (*CuteQFontEngineBoxCall21)(const void *, int *);
typedef const QFixedPoint * (*CuteQFontEngineBoxCall22)(const void *, const QFixedPoint *, int *);
typedef void (*CuteQFontEngineBoxCall23)(const void *, QGlyphLayout *, int, int *);
typedef const QImage * (*CuteQFontEngineBoxCall24)(const void *, glyph_t, const QFixedPoint *, int *);
typedef const QImage * (*CuteQFontEngineBoxCall25)(const void *, glyph_t, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineBoxCall26)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineBoxCall27)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int *);
typedef const QImage * (*CuteQFontEngineBoxCall28)(const void *, glyph_t, const QFixedPoint *, const QTransform *, const QColor *, int *);
typedef void * (*CuteQFontEngineBoxCall29)(const void *, glyph_t, const QFixedPoint *, int, const QTransform *, int *);
typedef bool (*CuteQFontEngineBoxCall30)(const void *, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineBoxCall31)(const void *, glyph_t, const QFixedPoint *, const QTransform *, int, int *);
typedef void (*CuteQFontEngineBoxCall32)(const void *, glyph_t, int *);
typedef const glyph_metrics_t * (*CuteQFontEngineBoxCall33)(const void *, glyph_t, const QTransform *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall34)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall35)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall36)(const void *, int *);
typedef const QFixed * (*CuteQFontEngineBoxCall37)(const void *, int *);
typedef bool (*CuteQFontEngineBoxCall38)(const void *, const QTransform *, int *);
typedef int (*CuteQFontEngineBoxCall39)(const void *, int *);
typedef int (*CuteQFontEngineBoxCall40)(const void *, int, int *);
typedef void * (*CuteQFontEngineBoxCall41)(const void *, int *);
typedef QString * (*CuteQFontEngineBoxCall42)(const void *, glyph_t, int *);
typedef glyph_t (*CuteQFontEngineBoxCall43)(const void *, const QLatin1String *, int *);
typedef bool (*CuteQFontEngineBoxCall44)(const void *, int *);
typedef bool (*CuteQFontEngineBoxCall45)(const void *, int, int *);
typedef void (*CuteQFontEngineBoxCall46)(const void *, int, int *);
typedef void (*CuteQFontEngineBoxCall47)(const void *, int *);
class CuteQFontEngineBox : public QFontEngineBox {
public:
  using QFontEngineBox::QFontEngineBox;
  void *taken[48] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphIndexEj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14recalcAdvancesEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxERK12QGlyphLayout")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEj")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13cloneWithSizeEd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12emSquareSizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6ascentEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9capHeightEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7descentEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7leadingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine12maxCharWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine14minLeftBearingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine15minRightBearingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEj")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9canRenderEPK5QChari")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10propertiesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16getUnscaledGlyphEjP12QPainterPathP15glyph_metrics_t")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6faceIdEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine11synthesizedEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine35supportsHorizontalSubPixelPositionsEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine33supportsVerticalSubPixelPositionsEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine19subPixelPositionForERK11QFixedPoint")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9doKerningEP12QGlyphLayout6QFlagsINS_10ShaperFlagEE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPoint")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK10QTransform")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine16alphaMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaRGBMapForGlyphEjRK11QFixedPointRK10QTransform")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine14bitmapForGlyphEjRK11QFixedPointRK10QTransformRK6QColor")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine9glyphDataEjRK11QFixedPointNS_11GlyphFormatERK10QTransform")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine18hasInternalCachingEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19alphaMapBoundingBoxEjRK11QFixedPointRK10QTransformNS_11GlyphFormatE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine20removeGlyphFromCacheEj")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11boundingBoxEjRK10QTransform")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine7xHeightEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine16averageCharWidthEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine13lineThicknessEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine17underlinePositionEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine22supportsTransformationERK10QTransform")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine10glyphCountEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine11glyphMarginENS_11GlyphFormatE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine6handleEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9glyphNameEj")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine9findGlyphE13QLatin1String")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine25hasUnreliableGlyphOutlineEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine29expectsGammaCorrectedBlendingENS_11GlyphFormatE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFontEngine19setDefaultHintStyleENS_9HintStyleE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFontEngine23initializeHeightMetricsEv")) {
      taken[47] = call;
      return true;
    }
    return false;
  }

  //  glyph_t QFontEngineBox::glyphIndex(uint ucs4) const
  glyph_t glyphIndex(uint ucs4) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontEngineBoxCall0 call = reinterpret_cast<CuteQFontEngineBoxCall0>(taken[0]);
      glyph_t given = call(this, ucs4, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::glyphIndex(ucs4);
  }

  //  void QFontEngineBox::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
  //      const
  void recalcAdvances(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontEngineBoxCall1 call = reinterpret_cast<CuteQFontEngineBoxCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineBox::recalcAdvances(a0, a1);
  }

  //  void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const
  //      QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags
  //      flags)
  void addOutlineToPath(
      qreal x,
      qreal y,
      const QGlyphLayout &glyphs,
      QPainterPath *path,
      QTextItem::RenderFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontEngineBoxCall2 call = reinterpret_cast<CuteQFontEngineBoxCall2>(taken[2]);
      call(this, x, y, &glyphs, path, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QFontEngineBox::addOutlineToPath(x, y, glyphs, path, flags);
  }

  //  glyph_metrics_t QFontEngineBox::boundingBox(const QGlyphLayout
  //      &glyphs)
  glyph_metrics_t boundingBox(const QGlyphLayout &glyphs) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontEngineBoxCall3 call = reinterpret_cast<CuteQFontEngineBoxCall3>(taken[3]);
      const glyph_metrics_t * given = call(this, &glyphs, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::boundingBox(glyphs);
  }

  //  glyph_metrics_t QFontEngineBox::boundingBox(glyph_t glyph)
  glyph_metrics_t boundingBox(glyph_t glyph) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontEngineBoxCall4 call = reinterpret_cast<CuteQFontEngineBoxCall4>(taken[4]);
      const glyph_metrics_t * given = call(this, glyph, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::boundingBox(glyph);
  }

  //  QFontEngine *QFontEngineBox::cloneWithSize(qreal pixelSize) const
  QFontEngine *cloneWithSize(qreal pixelSize) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontEngineBoxCall5 call = reinterpret_cast<CuteQFontEngineBoxCall5>(taken[5]);
      void * given = call(this, pixelSize, &handled);
      if (handled) return static_cast<QFontEngine *>(given);
    }
    return QFontEngineBox::cloneWithSize(pixelSize);
  }

  //  QFixed QFontEngineBox::emSquareSize() const
  QFixed emSquareSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontEngineBoxCall6 call = reinterpret_cast<CuteQFontEngineBoxCall6>(taken[6]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::emSquareSize();
  }

  //  QFixed QFontEngineBox::ascent() const
  QFixed ascent() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontEngineBoxCall7 call = reinterpret_cast<CuteQFontEngineBoxCall7>(taken[7]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::ascent();
  }

  //  QFixed QFontEngineBox::capHeight() const
  QFixed capHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontEngineBoxCall8 call = reinterpret_cast<CuteQFontEngineBoxCall8>(taken[8]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::capHeight();
  }

  //  QFixed QFontEngineBox::descent() const
  QFixed descent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontEngineBoxCall9 call = reinterpret_cast<CuteQFontEngineBoxCall9>(taken[9]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::descent();
  }

  //  QFixed QFontEngineBox::leading() const
  QFixed leading() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontEngineBoxCall10 call = reinterpret_cast<CuteQFontEngineBoxCall10>(taken[10]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::leading();
  }

  //  qreal QFontEngineBox::maxCharWidth() const
  qreal maxCharWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontEngineBoxCall11 call = reinterpret_cast<CuteQFontEngineBoxCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::maxCharWidth();
  }

  //  qreal QFontEngineBox::minLeftBearing() const
  qreal minLeftBearing() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontEngineBoxCall12 call = reinterpret_cast<CuteQFontEngineBoxCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::minLeftBearing();
  }

  //  qreal QFontEngineBox::minRightBearing() const
  qreal minRightBearing() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontEngineBoxCall13 call = reinterpret_cast<CuteQFontEngineBoxCall13>(taken[13]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::minRightBearing();
  }

  //  QImage QFontEngineBox::alphaMapForGlyph(glyph_t a0)
  QImage alphaMapForGlyph(glyph_t a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontEngineBoxCall14 call = reinterpret_cast<CuteQFontEngineBoxCall14>(taken[14]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QFontEngineBox::alphaMapForGlyph(a0);
  }

  //  bool QFontEngineBox::canRender(const QChar *string, int len) const
  bool canRender(const QChar *string, int len) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFontEngineBoxCall15 call = reinterpret_cast<CuteQFontEngineBoxCall15>(taken[15]);
      bool given = call(this, string, len, &handled);
      if (handled) return given;
    }
    return QFontEngineBox::canRender(string, len);
  }

  //  Properties QFontEngine::properties() const
  QFontEngine::Properties properties() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontEngineBoxCall16 call = reinterpret_cast<CuteQFontEngineBoxCall16>(taken[16]);
      const QFontEngine::Properties * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::properties();
  }

  //  void QFontEngine::getUnscaledGlyph(glyph_t glyph, QPainterPath *path,
  //      glyph_metrics_t *metrics)
  void getUnscaledGlyph(
      glyph_t glyph,
      QPainterPath *path,
      glyph_metrics_t *metrics) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFontEngineBoxCall17 call = reinterpret_cast<CuteQFontEngineBoxCall17>(taken[17]);
      call(this, glyph, path, metrics, &handled);
      if (handled) return;
    }
    QFontEngine::getUnscaledGlyph(glyph, path, metrics);
  }

  //  FaceId QFontEngine::faceId() const
  QFontEngine::FaceId faceId() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQFontEngineBoxCall18 call = reinterpret_cast<CuteQFontEngineBoxCall18>(taken[18]);
      const QFontEngine::FaceId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::faceId();
  }

  //  int QFontEngine::synthesized() const
  int synthesized() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontEngineBoxCall19 call = reinterpret_cast<CuteQFontEngineBoxCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::synthesized();
  }

  //  bool QFontEngine::supportsHorizontalSubPixelPositions() const
  bool supportsHorizontalSubPixelPositions() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontEngineBoxCall20 call = reinterpret_cast<CuteQFontEngineBoxCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsHorizontalSubPixelPositions();
  }

  //  bool QFontEngine::supportsVerticalSubPixelPositions() const
  bool supportsVerticalSubPixelPositions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontEngineBoxCall21 call = reinterpret_cast<CuteQFontEngineBoxCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsVerticalSubPixelPositions();
  }

  //  QFixedPoint QFontEngine::subPixelPositionFor(const QFixedPoint
  //      &position) const
  QFixedPoint subPixelPositionFor(
      const QFixedPoint &position) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontEngineBoxCall22 call = reinterpret_cast<CuteQFontEngineBoxCall22>(taken[22]);
      const QFixedPoint * given = call(this, &position, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::subPixelPositionFor(position);
  }

  //  void QFontEngine::doKerning(QGlyphLayout *a0, ShaperFlags a1) const
  void doKerning(
      QGlyphLayout *a0,
      QFontEngine::ShaperFlags a1) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQFontEngineBoxCall23 call = reinterpret_cast<CuteQFontEngineBoxCall23>(taken[23]);
      call(this, a0, static_cast<int>(a1.toInt()), &handled);
      if (handled) return;
    }
    QFontEngine::doKerning(a0, a1);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition)
  QImage alphaMapForGlyph(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFontEngineBoxCall24 call = reinterpret_cast<CuteQFontEngineBoxCall24>(taken[24]);
      const QImage * given = call(this, glyph, &subPixelPosition, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(glyph, subPixelPosition);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QTransform &t)
  QImage alphaMapForGlyph(glyph_t a0, const QTransform &t) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFontEngineBoxCall25 call = reinterpret_cast<CuteQFontEngineBoxCall25>(taken[25]);
      const QImage * given = call(this, a0, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0, t);
  }

  //  QImage QFontEngine::alphaMapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t)
  QImage alphaMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFontEngineBoxCall26 call = reinterpret_cast<CuteQFontEngineBoxCall26>(taken[26]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngine::alphaRGBMapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t)
  QImage alphaRGBMapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t) override {
    if (taken[27]) {
      int handled = 0;
      CuteQFontEngineBoxCall27 call = reinterpret_cast<CuteQFontEngineBoxCall27>(taken[27]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaRGBMapForGlyph(a0, subPixelPosition, t);
  }

  //  QImage QFontEngine::bitmapForGlyph(glyph_t a0, const QFixedPoint
  //      &subPixelPosition, const QTransform &t, const QColor &color)
  QImage bitmapForGlyph(
      glyph_t a0,
      const QFixedPoint &subPixelPosition,
      const QTransform &t,
      const QColor &color) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFontEngineBoxCall28 call = reinterpret_cast<CuteQFontEngineBoxCall28>(taken[28]);
      const QImage * given = call(this, a0, &subPixelPosition, &t, &color, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::bitmapForGlyph(a0, subPixelPosition, t, color);
  }

  //  Glyph *QFontEngine::glyphData(glyph_t glyph, const QFixedPoint
  //      &subPixelPosition, GlyphFormat neededFormat, const QTransform &t)
  QFontEngine::Glyph *glyphData(
      glyph_t glyph,
      const QFixedPoint &subPixelPosition,
      QFontEngine::GlyphFormat neededFormat,
      const QTransform &t) override {
    if (taken[29]) {
      int handled = 0;
      CuteQFontEngineBoxCall29 call = reinterpret_cast<CuteQFontEngineBoxCall29>(taken[29]);
      void * given = call(this, glyph, &subPixelPosition, static_cast<int>(neededFormat), &t, &handled);
      if (handled) return static_cast<QFontEngine::Glyph *>(given);
    }
    return QFontEngine::glyphData(glyph, subPixelPosition, neededFormat, t);
  }

  //  bool QFontEngine::hasInternalCaching() const
  bool hasInternalCaching() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQFontEngineBoxCall30 call = reinterpret_cast<CuteQFontEngineBoxCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasInternalCaching();
  }

  //  glyph_metrics_t QFontEngine::alphaMapBoundingBox(glyph_t glyph, const
  //      QFixedPoint &a1, const QTransform &matrix, GlyphFormat a3)
  glyph_metrics_t alphaMapBoundingBox(
      glyph_t glyph,
      const QFixedPoint &a1,
      const QTransform &matrix,
      QFontEngine::GlyphFormat a3) override {
    if (taken[31]) {
      int handled = 0;
      CuteQFontEngineBoxCall31 call = reinterpret_cast<CuteQFontEngineBoxCall31>(taken[31]);
      const glyph_metrics_t * given = call(this, glyph, &a1, &matrix, static_cast<int>(a3), &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::alphaMapBoundingBox(glyph, a1, matrix, a3);
  }

  //  void QFontEngine::removeGlyphFromCache(glyph_t a0)
  void removeGlyphFromCache(glyph_t a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQFontEngineBoxCall32 call = reinterpret_cast<CuteQFontEngineBoxCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFontEngine::removeGlyphFromCache(a0);
  }

  //  glyph_metrics_t QFontEngine::boundingBox(glyph_t glyph, const
  //      QTransform &matrix)
  glyph_metrics_t boundingBox(
      glyph_t glyph,
      const QTransform &matrix) override {
    if (taken[33]) {
      int handled = 0;
      CuteQFontEngineBoxCall33 call = reinterpret_cast<CuteQFontEngineBoxCall33>(taken[33]);
      const glyph_metrics_t * given = call(this, glyph, &matrix, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::boundingBox(glyph, matrix);
  }

  //  QFixed QFontEngine::xHeight() const
  QFixed xHeight() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQFontEngineBoxCall34 call = reinterpret_cast<CuteQFontEngineBoxCall34>(taken[34]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::xHeight();
  }

  //  QFixed QFontEngine::averageCharWidth() const
  QFixed averageCharWidth() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQFontEngineBoxCall35 call = reinterpret_cast<CuteQFontEngineBoxCall35>(taken[35]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::averageCharWidth();
  }

  //  QFixed QFontEngine::lineThickness() const
  QFixed lineThickness() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQFontEngineBoxCall36 call = reinterpret_cast<CuteQFontEngineBoxCall36>(taken[36]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::lineThickness();
  }

  //  QFixed QFontEngine::underlinePosition() const
  QFixed underlinePosition() const override {
    if (taken[37]) {
      int handled = 0;
      CuteQFontEngineBoxCall37 call = reinterpret_cast<CuteQFontEngineBoxCall37>(taken[37]);
      const QFixed * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFontEngine::underlinePosition();
  }

  //  bool QFontEngine::supportsTransformation(const QTransform &transform)
  //      const
  bool supportsTransformation(const QTransform &transform) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQFontEngineBoxCall38 call = reinterpret_cast<CuteQFontEngineBoxCall38>(taken[38]);
      bool given = call(this, &transform, &handled);
      if (handled) return given;
    }
    return QFontEngine::supportsTransformation(transform);
  }

  //  int QFontEngine::glyphCount() const
  int glyphCount() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQFontEngineBoxCall39 call = reinterpret_cast<CuteQFontEngineBoxCall39>(taken[39]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphCount();
  }

  //  int QFontEngine::glyphMargin(GlyphFormat format)
  int glyphMargin(QFontEngine::GlyphFormat format) override {
    if (taken[40]) {
      int handled = 0;
      CuteQFontEngineBoxCall40 call = reinterpret_cast<CuteQFontEngineBoxCall40>(taken[40]);
      int given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::glyphMargin(format);
  }

  //  Qt::HANDLE QFontEngine::handle() const
  Qt::HANDLE handle() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQFontEngineBoxCall41 call = reinterpret_cast<CuteQFontEngineBoxCall41>(taken[41]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt::HANDLE>(given);
    }
    return QFontEngine::handle();
  }

  //  QString QFontEngine::glyphName(glyph_t index) const
  QString glyphName(glyph_t index) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQFontEngineBoxCall42 call = reinterpret_cast<CuteQFontEngineBoxCall42>(taken[42]);
      QString * given = call(this, index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFontEngine::glyphName(index);
  }

  //  glyph_t QFontEngine::findGlyph(QLatin1StringView name) const
  glyph_t findGlyph(QLatin1StringView name) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQFontEngineBoxCall43 call = reinterpret_cast<CuteQFontEngineBoxCall43>(taken[43]);
      glyph_t given = call(this, &name, &handled);
      if (handled) return given;
    }
    return QFontEngine::findGlyph(name);
  }

  //  bool QFontEngine::hasUnreliableGlyphOutline() const
  bool hasUnreliableGlyphOutline() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQFontEngineBoxCall44 call = reinterpret_cast<CuteQFontEngineBoxCall44>(taken[44]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontEngine::hasUnreliableGlyphOutline();
  }

  //  bool
  //      QFontEngine::expectsGammaCorrectedBlending(QFontEngine::GlyphForm
  //      at format) const
  bool expectsGammaCorrectedBlending(
      QFontEngine::GlyphFormat format) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQFontEngineBoxCall45 call = reinterpret_cast<CuteQFontEngineBoxCall45>(taken[45]);
      bool given = call(this, static_cast<int>(format), &handled);
      if (handled) return given;
    }
    return QFontEngine::expectsGammaCorrectedBlending(format);
  }

  //  void QFontEngine::setDefaultHintStyle(HintStyle a0)
  void setDefaultHintStyle(QFontEngine::HintStyle a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQFontEngineBoxCall46 call = reinterpret_cast<CuteQFontEngineBoxCall46>(taken[46]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QFontEngine::setDefaultHintStyle(a0);
  }

  //  void QFontEngine::initializeHeightMetrics() const
  void initializeHeightMetrics() const override {
    if (taken[47]) {
      int handled = 0;
      CuteQFontEngineBoxCall47 call = reinterpret_cast<CuteQFontEngineBoxCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QFontEngine::initializeHeightMetrics();
  }
};

//  QFontEngineBox::~QFontEngineBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFontEngineBoxD1Ev(QFontEngineBox *self) {
  delete self;
}

//  glyph_t QFontEngineBox::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK14QFontEngineBox10glyphIndexEj(
    const QFontEngineBox *self,
    uint ucs4) {
  return self->glyphIndex(ucs4);
}

//  int QFontEngineBox::stringToCMap(const QChar *str, int len, QGlyphLayout
//      *glyphs, int *nglyphs, ShaperFlags flags) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QFontEngineBox12stringToCMapEPK5QChariP12QGlyphLayoutPi6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineBox *self,
    const QChar *str,
    int len,
    QGlyphLayout *glyphs,
    int *nglyphs,
    int flags) {
  return self->stringToCMap(
      str,
      len,
      glyphs,
      nglyphs,
      QFlags<QFontEngine::ShaperFlag>::fromInt(flags));
}

//  void QFontEngineBox::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QFontEngineBox14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineBox *self,
    QGlyphLayout *a0,
    int a1) {
  self->recalcAdvances(a0, QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineBox::draw(QPaintEngine *p, qreal x, qreal y, const
//      QTextItemInt &si)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFontEngineBox4drawEP12QPaintEngineddRK12QTextItemInt(
    QFontEngineBox *self,
    QPaintEngine *p,
    qreal x,
    qreal y,
    const QTextItemInt *si) {
  self->draw(p, x, y, *si);
}

//  void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const
//      QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QFontEngineBox16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineBox *self,
    qreal x,
    qreal y,
    const QGlyphLayout *glyphs,
    QPainterPath *path,
    int flags) {
  self->addOutlineToPath(
      x,
      y,
      *glyphs,
      path,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  glyph_metrics_t QFontEngineBox::boundingBox(const QGlyphLayout &glyphs)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN14QFontEngineBox11boundingBoxERK12QGlyphLayout(
    QFontEngineBox *self,
    const QGlyphLayout *glyphs) {
  return new glyph_metrics_t(self->boundingBox(*glyphs));
}

//  glyph_metrics_t QFontEngineBox::boundingBox(glyph_t glyph)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN14QFontEngineBox11boundingBoxEj(
    QFontEngineBox *self,
    glyph_t glyph) {
  return new glyph_metrics_t(self->boundingBox(glyph));
}

//  QFontEngine *QFontEngineBox::cloneWithSize(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK14QFontEngineBox13cloneWithSizeEd(
    const QFontEngineBox *self,
    qreal pixelSize) {
  return self->cloneWithSize(pixelSize);
}

//  QFixed QFontEngineBox::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK14QFontEngineBox12emSquareSizeEv(
    const QFontEngineBox *self) {
  return new QFixed(self->emSquareSize());
}

//  QFixed QFontEngineBox::ascent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK14QFontEngineBox6ascentEv(const QFontEngineBox *self) {
  return new QFixed(self->ascent());
}

//  QFixed QFontEngineBox::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK14QFontEngineBox9capHeightEv(const QFontEngineBox *self) {
  return new QFixed(self->capHeight());
}

//  QFixed QFontEngineBox::descent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK14QFontEngineBox7descentEv(const QFontEngineBox *self) {
  return new QFixed(self->descent());
}

//  QFixed QFontEngineBox::leading() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK14QFontEngineBox7leadingEv(const QFontEngineBox *self) {
  return new QFixed(self->leading());
}

//  qreal QFontEngineBox::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QFontEngineBox12maxCharWidthEv(
    const QFontEngineBox *self) {
  return self->maxCharWidth();
}

//  qreal QFontEngineBox::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QFontEngineBox14minLeftBearingEv(
    const QFontEngineBox *self) {
  return self->minLeftBearing();
}

//  qreal QFontEngineBox::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QFontEngineBox15minRightBearingEv(
    const QFontEngineBox *self) {
  return self->minRightBearing();
}

//  QImage QFontEngineBox::alphaMapForGlyph(glyph_t a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN14QFontEngineBox16alphaMapForGlyphEj(
    QFontEngineBox *self,
    glyph_t a0) {
  return new QImage(self->alphaMapForGlyph(a0));
}

//  bool QFontEngineBox::canRender(const QChar *string, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QFontEngineBox9canRenderEPK5QChari(
    const QFontEngineBox *self,
    const QChar *string,
    int len) {
  return self->canRender(string, len);
}

//  int QFontEngineBox::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QFontEngineBox4sizeEv(const QFontEngineBox *self) {
  return self->size();
}

//  a Python function taken by a CuteQFontEngineBox, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontEngineBox(
    QFontEngineBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontEngineBox *>(self)->take(key, call);
}

//  glyph_t QFontEngineBox::glyphIndex(uint ucs4) const
extern "C" Q_DECL_EXPORT
glyph_t ritual_own_ZNK14QFontEngineBox10glyphIndexEj(
    const QFontEngineBox *self,
    uint ucs4) {
  return self->QFontEngineBox::glyphIndex(ucs4);
}

//  void QFontEngineBox::recalcAdvances(QGlyphLayout *a0, ShaperFlags a1)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QFontEngineBox14recalcAdvancesEP12QGlyphLayout6QFlagsIN11QFontEngine10ShaperFlagEE(
    const QFontEngineBox *self,
    QGlyphLayout *a0,
    int a1) {
  self->QFontEngineBox::recalcAdvances(
      a0,
      QFlags<QFontEngine::ShaperFlag>::fromInt(a1));
}

//  void QFontEngineBox::addOutlineToPath(qreal x, qreal y, const
//      QGlyphLayout &glyphs, QPainterPath *path, QTextItem::RenderFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QFontEngineBox16addOutlineToPathEddRK12QGlyphLayoutP12QPainterPath6QFlagsIN9QTextItem10RenderFlagEE(
    QFontEngineBox *self,
    qreal x,
    qreal y,
    const QGlyphLayout *glyphs,
    QPainterPath *path,
    int flags) {
  self->QFontEngineBox::addOutlineToPath(
      x,
      y,
      *glyphs,
      path,
      QFlags<QTextItem::RenderFlag>::fromInt(flags));
}

//  QFixed QFontEngineBox::emSquareSize() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK14QFontEngineBox12emSquareSizeEv(
    const QFontEngineBox *self) {
  return new QFixed(self->QFontEngineBox::emSquareSize());
}

//  QFixed QFontEngineBox::ascent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK14QFontEngineBox6ascentEv(const QFontEngineBox *self) {
  return new QFixed(self->QFontEngineBox::ascent());
}

//  QFixed QFontEngineBox::capHeight() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK14QFontEngineBox9capHeightEv(
    const QFontEngineBox *self) {
  return new QFixed(self->QFontEngineBox::capHeight());
}

//  QFixed QFontEngineBox::descent() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK14QFontEngineBox7descentEv(
    const QFontEngineBox *self) {
  return new QFixed(self->QFontEngineBox::descent());
}

//  QFixed QFontEngineBox::leading() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_own_ZNK14QFontEngineBox7leadingEv(
    const QFontEngineBox *self) {
  return new QFixed(self->QFontEngineBox::leading());
}

//  qreal QFontEngineBox::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QFontEngineBox12maxCharWidthEv(
    const QFontEngineBox *self) {
  return self->QFontEngineBox::maxCharWidth();
}

//  qreal QFontEngineBox::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QFontEngineBox14minLeftBearingEv(
    const QFontEngineBox *self) {
  return self->QFontEngineBox::minLeftBearing();
}

//  qreal QFontEngineBox::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK14QFontEngineBox15minRightBearingEv(
    const QFontEngineBox *self) {
  return self->QFontEngineBox::minRightBearing();
}

//  QImage QFontEngineBox::alphaMapForGlyph(glyph_t a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN14QFontEngineBox16alphaMapForGlyphEj(
    QFontEngineBox *self,
    glyph_t a0) {
  return new QImage(self->QFontEngineBox::alphaMapForGlyph(a0));
}

//  bool QFontEngineBox::canRender(const QChar *string, int len) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QFontEngineBox9canRenderEPK5QChari(
    const QFontEngineBox *self,
    const QChar *string,
    int len) {
  return self->QFontEngineBox::canRender(string, len);
}
