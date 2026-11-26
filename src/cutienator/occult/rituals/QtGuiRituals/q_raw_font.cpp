//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qrawfont.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_RAWFONT)
#include <QtGui/qrawfont.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>
#include <QtGui/qimage.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>
#include <QtCore/qchar.h>
#include <QtGui/qfont.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QString>
#include <QtGui/QFontDatabase>

//  QRawFont::QRawFont()
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFontC1Ev() {
  return new QRawFont();
}

//  QRawFont::QRawFont(const QString &fileName, qreal pixelSize,
//      QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFontC1ERK7QStringdN5QFont17HintingPreferenceE(
    const QString *fileName,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return new QRawFont(*fileName, pixelSize, hintingPreference);
}

//  QRawFont::QRawFont(const QByteArray &fontData, qreal pixelSize,
//      QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFontC1ERK10QByteArraydN5QFont17HintingPreferenceE(
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  return new QRawFont(*fontData, pixelSize, hintingPreference);
}

//  QRawFont::QRawFont(const QRawFont &other)
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFontC1ERKS_(const QRawFont *other) {
  return new QRawFont(*other);
}

//  QRawFont &QRawFont::operator=(QRawFont &&other)
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFontaSEOS_(QRawFont *self, QRawFont *other) {
  return &(self->operator=(std::move(*other)));
}

//  QRawFont &QRawFont::operator=(const QRawFont &other)
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFontaSERKS_(QRawFont *self, const QRawFont *other) {
  return &(self->operator=(*other));
}

//  QRawFont::~QRawFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRawFontD1Ev(QRawFont *self) {
  delete self;
}

//  void QRawFont::swap(QRawFont &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRawFont4swapERS_(QRawFont *self, QRawFont *other) {
  self->swap(*other);
}

//  bool QRawFont::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFont7isValidEv(const QRawFont *self) {
  return self->isValid();
}

//  bool QRawFont::operator==(const QRawFont &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFonteqERKS_(
    const QRawFont *self,
    const QRawFont *other) {
  return self->operator==(*other);
}

//  bool QRawFont::operator!=(const QRawFont &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFontneERKS_(
    const QRawFont *self,
    const QRawFont *other) {
  return self->operator!=(*other);
}

//  quint32 QRawFont::glyphCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK8QRawFont10glyphCountEv(const QRawFont *self) {
  return self->glyphCount();
}

//  QString QRawFont::familyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QRawFont10familyNameEv(const QRawFont *self) {
  return new QString(self->familyName());
}

//  QString QRawFont::styleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QRawFont9styleNameEv(const QRawFont *self) {
  return new QString(self->styleName());
}

//  QFont::Style QRawFont::style() const
extern "C" Q_DECL_EXPORT
QFont::Style ritual_ZNK8QRawFont5styleEv(const QRawFont *self) {
  return self->style();
}

//  int QRawFont::weight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QRawFont6weightEv(const QRawFont *self) {
  return self->weight();
}

//  QList<quint32> QRawFont::glyphIndexesForString(const QString &text) const
extern "C" Q_DECL_EXPORT
QList<quint32> *ritual_ZNK8QRawFont21glyphIndexesForStringERK7QString(
    const QRawFont *self,
    const QString *text) {
  return new QList<quint32>(self->glyphIndexesForString(*text));
}

//  QList<QPointF> QRawFont::advancesForGlyphIndexes(const QList<quint32>
//      &glyphIndexes) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK8QRawFont23advancesForGlyphIndexesERK5QListIjE(
    const QRawFont *self,
    const QList<quint32> *glyphIndexes) {
  return new QList<QPointF>(self->advancesForGlyphIndexes(*glyphIndexes));
}

//  QList<QPointF> QRawFont::advancesForGlyphIndexes(const QList<quint32>
//      &glyphIndexes, LayoutFlags layoutFlags) const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK8QRawFont23advancesForGlyphIndexesERK5QListIjE6QFlagsINS_10LayoutFlagEE(
    const QRawFont *self,
    const QList<quint32> *glyphIndexes,
    int layoutFlags) {
  return new QList<QPointF>(
      self->advancesForGlyphIndexes(
          *glyphIndexes,
          QFlags<QRawFont::LayoutFlag>::fromInt(layoutFlags)));
}

//  bool QRawFont::glyphIndexesForChars(const QChar *chars, int numChars,
//      quint32 *glyphIndexes, int *numGlyphs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFont20glyphIndexesForCharsEPK5QChariPjPi(
    const QRawFont *self,
    const QChar *chars,
    int numChars,
    quint32 *glyphIndexes,
    int *numGlyphs) {
  return self->glyphIndexesForChars(
      chars,
      numChars,
      glyphIndexes,
      numGlyphs);
}

//  bool QRawFont::advancesForGlyphIndexes(const quint32 *glyphIndexes,
//      QPointF *advances, int numGlyphs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFont23advancesForGlyphIndexesEPKjP7QPointFi(
    const QRawFont *self,
    const quint32 *glyphIndexes,
    QPointF *advances,
    int numGlyphs) {
  return self->advancesForGlyphIndexes(glyphIndexes, advances, numGlyphs);
}

//  bool QRawFont::advancesForGlyphIndexes(const quint32 *glyphIndexes,
//      QPointF *advances, int numGlyphs, LayoutFlags layoutFlags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFont23advancesForGlyphIndexesEPKjP7QPointFi6QFlagsINS_10LayoutFlagEE(
    const QRawFont *self,
    const quint32 *glyphIndexes,
    QPointF *advances,
    int numGlyphs,
    int layoutFlags) {
  return self->advancesForGlyphIndexes(
      glyphIndexes,
      advances,
      numGlyphs,
      QFlags<QRawFont::LayoutFlag>::fromInt(layoutFlags));
}

//  QImage QRawFont::alphaMapForGlyph(quint32 glyphIndex, AntialiasingType
//      antialiasingType, const QTransform &transform) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK8QRawFont16alphaMapForGlyphEjNS_16AntialiasingTypeERK10QTransform(
    const QRawFont *self,
    quint32 glyphIndex,
    QRawFont::AntialiasingType antialiasingType,
    const QTransform *transform) {
  return new QImage(
      self->alphaMapForGlyph(
          glyphIndex,
          antialiasingType,
          *transform));
}

//  QPainterPath QRawFont::pathForGlyph(quint32 glyphIndex) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK8QRawFont12pathForGlyphEj(
    const QRawFont *self,
    quint32 glyphIndex) {
  return new QPainterPath(self->pathForGlyph(glyphIndex));
}

//  QRectF QRawFont::boundingRect(quint32 glyphIndex) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK8QRawFont12boundingRectEj(
    const QRawFont *self,
    quint32 glyphIndex) {
  return new QRectF(self->boundingRect(glyphIndex));
}

//  void QRawFont::setPixelSize(qreal pixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRawFont12setPixelSizeEd(QRawFont *self, qreal pixelSize) {
  self->setPixelSize(pixelSize);
}

//  qreal QRawFont::pixelSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont9pixelSizeEv(const QRawFont *self) {
  return self->pixelSize();
}

//  QFont::HintingPreference QRawFont::hintingPreference() const
extern "C" Q_DECL_EXPORT
QFont::HintingPreference ritual_ZNK8QRawFont17hintingPreferenceEv(
    const QRawFont *self) {
  return self->hintingPreference();
}

//  qreal QRawFont::ascent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont6ascentEv(const QRawFont *self) {
  return self->ascent();
}

//  qreal QRawFont::capHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont9capHeightEv(const QRawFont *self) {
  return self->capHeight();
}

//  qreal QRawFont::descent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont7descentEv(const QRawFont *self) {
  return self->descent();
}

//  qreal QRawFont::leading() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont7leadingEv(const QRawFont *self) {
  return self->leading();
}

//  qreal QRawFont::xHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont7xHeightEv(const QRawFont *self) {
  return self->xHeight();
}

//  qreal QRawFont::averageCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont16averageCharWidthEv(const QRawFont *self) {
  return self->averageCharWidth();
}

//  qreal QRawFont::maxCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont12maxCharWidthEv(const QRawFont *self) {
  return self->maxCharWidth();
}

//  qreal QRawFont::lineThickness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont13lineThicknessEv(const QRawFont *self) {
  return self->lineThickness();
}

//  qreal QRawFont::underlinePosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont17underlinePositionEv(const QRawFont *self) {
  return self->underlinePosition();
}

//  qreal QRawFont::unitsPerEm() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QRawFont10unitsPerEmEv(const QRawFont *self) {
  return self->unitsPerEm();
}

//  QString QRawFont::glyphName(quint32 glyphIndex) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QRawFont9glyphNameEj(
    const QRawFont *self,
    quint32 glyphIndex) {
  return new QString(self->glyphName(glyphIndex));
}

//  void QRawFont::loadFromFile(const QString &fileName, qreal pixelSize,
//      QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRawFont12loadFromFileERK7QStringdN5QFont17HintingPreferenceE(
    QRawFont *self,
    const QString *fileName,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  self->loadFromFile(*fileName, pixelSize, hintingPreference);
}

//  void QRawFont::loadFromData(const QByteArray &fontData, qreal pixelSize,
//      QFont::HintingPreference hintingPreference)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QRawFont12loadFromDataERK10QByteArraydN5QFont17HintingPreferenceE(
    QRawFont *self,
    const QByteArray *fontData,
    qreal pixelSize,
    QFont::HintingPreference hintingPreference) {
  self->loadFromData(*fontData, pixelSize, hintingPreference);
}

//  bool QRawFont::supportsCharacter(uint ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFont17supportsCharacterEj(
    const QRawFont *self,
    uint ucs4) {
  return self->supportsCharacter(ucs4);
}

//  bool QRawFont::supportsCharacter(QChar character) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QRawFont17supportsCharacterE5QChar(
    const QRawFont *self,
    const QChar *character) {
  return self->supportsCharacter(*character);
}

//  QList<QFontDatabase::WritingSystem> QRawFont::supportedWritingSystems()
//      const
extern "C" Q_DECL_EXPORT
QList<QFontDatabase::WritingSystem> *ritual_ZNK8QRawFont23supportedWritingSystemsEv(
    const QRawFont *self) {
  return new QList<QFontDatabase::WritingSystem>(
      self->supportedWritingSystems());
}

//  QByteArray QRawFont::fontTable(const char *tagName) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QRawFont9fontTableEPKc(
    const QRawFont *self,
    const char *tagName) {
  return new QByteArray(self->fontTable(tagName));
}

//  QByteArray QRawFont::fontTable(QFont::Tag tag) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QRawFont9fontTableEN5QFont3TagE(
    const QRawFont *self,
    const QFont::Tag *tag) {
  return new QByteArray(self->fontTable(*tag));
}

//  QRawFont QRawFont::fromFont(const QFont &font,
//      QFontDatabase::WritingSystem writingSystem)
extern "C" Q_DECL_EXPORT
QRawFont *ritual_ZN8QRawFont8fromFontERK5QFontN13QFontDatabase13WritingSystemE(
    const QFont *font,
    QFontDatabase::WritingSystem writingSystem) {
  return new QRawFont(QRawFont::fromFont(*font, writingSystem));
}

//  a QList<quint32> a ritual of QRawFont gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRawFont__QList_quint32(QList<quint32> *self) {
  delete self;
}

//  a QList<QFontDatabase::WritingSystem> a ritual of QRawFont gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRawFont__QList_QFontDatabase_WritingSystem(
    QList<QFontDatabase::WritingSystem> *self) {
  delete self;
}

#endif  // !defined(QT_NO_RAWFONT)
