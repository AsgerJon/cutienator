//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdistancefield_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 2. Kept as it is when the generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdistancefield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>

//  QDistanceField::QDistanceField()
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1Ev() {
  return new QDistanceField();
}

//  QDistanceField::QDistanceField(int width, int height)
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1Eii(int width, int height) {
  return new QDistanceField(width, height);
}

//  QDistanceField::QDistanceField(const QRawFont &font, glyph_t glyph, bool
//      doubleResolution)
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1ERK8QRawFontjb(
    const QRawFont *font,
    glyph_t glyph,
    bool doubleResolution) {
  return new QDistanceField(*font, glyph, doubleResolution);
}

//  QDistanceField::QDistanceField(QFontEngine *fontEngine, glyph_t glyph,
//      bool doubleResolution)
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1EP11QFontEnginejb(
    QFontEngine *fontEngine,
    glyph_t glyph,
    bool doubleResolution) {
  return new QDistanceField(fontEngine, glyph, doubleResolution);
}

//  QDistanceField::QDistanceField(const QPainterPath &path, glyph_t glyph,
//      bool doubleResolution)
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1ERK12QPainterPathjb(
    const QPainterPath *path,
    glyph_t glyph,
    bool doubleResolution) {
  return new QDistanceField(*path, glyph, doubleResolution);
}

//  QDistanceField::QDistanceField(QSize size, const QPainterPath &path,
//      glyph_t glyph, bool doubleResolution)
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1E5QSizeRK12QPainterPathjb(
    const QSize *size,
    const QPainterPath *path,
    glyph_t glyph,
    bool doubleResolution) {
  return new QDistanceField(*size, *path, glyph, doubleResolution);
}

//  bool QDistanceField::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QDistanceField6isNullEv(const QDistanceField *self) {
  return self->isNull();
}

//  glyph_t QDistanceField::glyph() const
extern "C" Q_DECL_EXPORT
glyph_t ritual_ZNK14QDistanceField5glyphEv(const QDistanceField *self) {
  return self->glyph();
}

//  void QDistanceField::setGlyph(const QRawFont &font, glyph_t glyph, bool
//      doubleResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDistanceField8setGlyphERK8QRawFontjb(
    QDistanceField *self,
    const QRawFont *font,
    glyph_t glyph,
    bool doubleResolution) {
  self->setGlyph(*font, glyph, doubleResolution);
}

//  void QDistanceField::setGlyph(QFontEngine *fontEngine, glyph_t glyph,
//      bool doubleResolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDistanceField8setGlyphEP11QFontEnginejb(
    QDistanceField *self,
    QFontEngine *fontEngine,
    glyph_t glyph,
    bool doubleResolution) {
  self->setGlyph(fontEngine, glyph, doubleResolution);
}

//  int QDistanceField::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QDistanceField5widthEv(const QDistanceField *self) {
  return self->width();
}

//  int QDistanceField::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QDistanceField6heightEv(const QDistanceField *self) {
  return self->height();
}

//  QDistanceField QDistanceField::copy(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZNK14QDistanceField4copyERK5QRect(
    const QDistanceField *self,
    const QRect *rect) {
  return new QDistanceField(self->copy(*rect));
}

//  QDistanceField QDistanceField::copy(int x, int y, int w, int h) const
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZNK14QDistanceField4copyEiiii(
    const QDistanceField *self,
    int x,
    int y,
    int w,
    int h) {
  return new QDistanceField(self->copy(x, y, w, h));
}

//  const uchar *QDistanceField::bits() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK14QDistanceField4bitsEv(const QDistanceField *self) {
  return self->bits();
}

//  const uchar *QDistanceField::constBits() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK14QDistanceField9constBitsEv(
    const QDistanceField *self) {
  return self->constBits();
}

//  const uchar *QDistanceField::scanLine(int a0) const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK14QDistanceField8scanLineEi(
    const QDistanceField *self,
    int a0) {
  return self->scanLine(a0);
}

//  const uchar *QDistanceField::constScanLine(int a0) const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK14QDistanceField13constScanLineEi(
    const QDistanceField *self,
    int a0) {
  return self->constScanLine(a0);
}

//  QImage QDistanceField::toImage(QImage::Format format) const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK14QDistanceField7toImageEN6QImage6FormatE(
    const QDistanceField *self,
    QImage::Format format) {
  return new QImage(self->toImage(format));
}

//  QDistanceField::QDistanceField(QDistanceFieldData *data)
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_ZN14QDistanceFieldC1EP18QDistanceFieldData(
    QDistanceFieldData *data) {
  return new QDistanceField(data);
}

//  QDistanceField::~QDistanceField()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDistanceFieldD1Ev(QDistanceField *self) {
  delete self;
}

//  QList<QDistanceField>::QList()
extern "C" Q_DECL_EXPORT
QList<QDistanceField> *ritual_list_make_QDistanceField() {
  return new QList<QDistanceField>();
}

//  void QList<QDistanceField>::append(const QDistanceField &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDistanceField(
    QList<QDistanceField> *self,
    const QDistanceField *element) {
  self->append(*element);
}

//  qsizetype QList<QDistanceField>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDistanceField(
    const QList<QDistanceField> *self) {
  return self->size();
}

//  const QDistanceField &QList<QDistanceField>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDistanceField *ritual_list_at_QDistanceField(
    const QList<QDistanceField> *self,
    long long index) {
  return new QDistanceField(self->at(index));
}

//  QList<QDistanceField>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDistanceField(QList<QDistanceField> *self) {
  delete self;
}

//  uchar *QDistanceField::bits()
extern "C" Q_DECL_EXPORT
uchar *ritual_ZN14QDistanceField4bitsEv(
    QDistanceField *self) {
  return self->bits();
}

//  uchar *QDistanceField::scanLine(int a0)
extern "C" Q_DECL_EXPORT
uchar *ritual_ZN14QDistanceField8scanLineEi(
    QDistanceField *self,
    int a0) {
  return self->scanLine(a0);
}
