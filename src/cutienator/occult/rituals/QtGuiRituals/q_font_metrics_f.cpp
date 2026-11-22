//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfontmetrics.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfontmetrics.h>
#include <QtGui/qfont.h>
#include <QtCore/qchar.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextoption.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QFontMetricsF::QFontMetricsF(const QFont &font)
extern "C" Q_DECL_EXPORT
QFontMetricsF *ritual_ZN13QFontMetricsFC1ERK5QFont(const QFont *font) {
  return new QFontMetricsF(*font);
}

//  QFontMetricsF::QFontMetricsF(const QFont &font, const QPaintDevice *pd)
extern "C" Q_DECL_EXPORT
QFontMetricsF *ritual_ZN13QFontMetricsFC1ERK5QFontPK12QPaintDevice(
    const QFont *font,
    const QPaintDevice *pd) {
  return new QFontMetricsF(*font, pd);
}

//  QFontMetricsF::QFontMetricsF(const QFontMetrics &a0)
extern "C" Q_DECL_EXPORT
QFontMetricsF *ritual_ZN13QFontMetricsFC1ERK12QFontMetrics(
    const QFontMetrics *a0) {
  return new QFontMetricsF(*a0);
}

//  QFontMetricsF::QFontMetricsF(const QFontMetricsF &a0)
extern "C" Q_DECL_EXPORT
QFontMetricsF *ritual_ZN13QFontMetricsFC1ERKS_(const QFontMetricsF *a0) {
  return new QFontMetricsF(*a0);
}

//  QFontMetricsF::~QFontMetricsF()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontMetricsFD1Ev(QFontMetricsF *self) {
  delete self;
}

//  qreal QFontMetricsF::ascent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF6ascentEv(const QFontMetricsF *self) {
  return self->ascent();
}

//  qreal QFontMetricsF::capHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF9capHeightEv(const QFontMetricsF *self) {
  return self->capHeight();
}

//  qreal QFontMetricsF::descent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF7descentEv(const QFontMetricsF *self) {
  return self->descent();
}

//  qreal QFontMetricsF::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF6heightEv(const QFontMetricsF *self) {
  return self->height();
}

//  qreal QFontMetricsF::leading() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF7leadingEv(const QFontMetricsF *self) {
  return self->leading();
}

//  qreal QFontMetricsF::lineSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF11lineSpacingEv(const QFontMetricsF *self) {
  return self->lineSpacing();
}

//  qreal QFontMetricsF::minLeftBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF14minLeftBearingEv(
    const QFontMetricsF *self) {
  return self->minLeftBearing();
}

//  qreal QFontMetricsF::minRightBearing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF15minRightBearingEv(
    const QFontMetricsF *self) {
  return self->minRightBearing();
}

//  qreal QFontMetricsF::maxWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF8maxWidthEv(const QFontMetricsF *self) {
  return self->maxWidth();
}

//  qreal QFontMetricsF::xHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF7xHeightEv(const QFontMetricsF *self) {
  return self->xHeight();
}

//  qreal QFontMetricsF::averageCharWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF16averageCharWidthEv(
    const QFontMetricsF *self) {
  return self->averageCharWidth();
}

//  bool QFontMetricsF::inFont(QChar a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontMetricsF6inFontE5QChar(
    const QFontMetricsF *self,
    const QChar *a0) {
  return self->inFont(*a0);
}

//  bool QFontMetricsF::inFontUcs4(uint ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontMetricsF10inFontUcs4Ej(
    const QFontMetricsF *self,
    uint ucs4) {
  return self->inFontUcs4(ucs4);
}

//  qreal QFontMetricsF::leftBearing(QChar a0) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF11leftBearingE5QChar(
    const QFontMetricsF *self,
    const QChar *a0) {
  return self->leftBearing(*a0);
}

//  qreal QFontMetricsF::rightBearing(QChar a0) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF12rightBearingE5QChar(
    const QFontMetricsF *self,
    const QChar *a0) {
  return self->rightBearing(*a0);
}

//  qreal QFontMetricsF::horizontalAdvance(const QString &string, int length)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF17horizontalAdvanceERK7QStringi(
    const QFontMetricsF *self,
    const QString *string,
    int length) {
  return self->horizontalAdvance(*string, length);
}

//  qreal QFontMetricsF::horizontalAdvance(QChar a0) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF17horizontalAdvanceE5QChar(
    const QFontMetricsF *self,
    const QChar *a0) {
  return self->horizontalAdvance(*a0);
}

//  qreal QFontMetricsF::horizontalAdvance(const QString &string, const
//      QTextOption &textOption) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF17horizontalAdvanceERK7QStringRK11QTextOption(
    const QFontMetricsF *self,
    const QString *string,
    const QTextOption *textOption) {
  return self->horizontalAdvance(*string, *textOption);
}

//  QRectF QFontMetricsF::boundingRect(const QString &string) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QFontMetricsF12boundingRectERK7QString(
    const QFontMetricsF *self,
    const QString *string) {
  return new QRectF(self->boundingRect(*string));
}

//  QRectF QFontMetricsF::boundingRect(const QString &text, const QTextOption
//      &textOption) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QFontMetricsF12boundingRectERK7QStringRK11QTextOption(
    const QFontMetricsF *self,
    const QString *text,
    const QTextOption *textOption) {
  return new QRectF(self->boundingRect(*text, *textOption));
}

//  QRectF QFontMetricsF::boundingRect(QChar a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QFontMetricsF12boundingRectE5QChar(
    const QFontMetricsF *self,
    const QChar *a0) {
  return new QRectF(self->boundingRect(*a0));
}

//  QRectF QFontMetricsF::boundingRect(const QRectF &r, int flags, const
//      QString &string, int tabstops, int *tabarray) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QFontMetricsF12boundingRectERK6QRectFiRK7QStringiPi(
    const QFontMetricsF *self,
    const QRectF *r,
    int flags,
    const QString *string,
    int tabstops,
    int *tabarray) {
  return new QRectF(
      self->boundingRect(
          *r,
          flags,
          *string,
          tabstops,
          tabarray));
}

//  QSizeF QFontMetricsF::size(int flags, const QString &str, int tabstops,
//      int *tabarray) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK13QFontMetricsF4sizeEiRK7QStringiPi(
    const QFontMetricsF *self,
    int flags,
    const QString *str,
    int tabstops,
    int *tabarray) {
  return new QSizeF(self->size(flags, *str, tabstops, tabarray));
}

//  QRectF QFontMetricsF::tightBoundingRect(const QString &text) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QFontMetricsF17tightBoundingRectERK7QString(
    const QFontMetricsF *self,
    const QString *text) {
  return new QRectF(self->tightBoundingRect(*text));
}

//  QRectF QFontMetricsF::tightBoundingRect(const QString &text, const
//      QTextOption &textOption) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QFontMetricsF17tightBoundingRectERK7QStringRK11QTextOption(
    const QFontMetricsF *self,
    const QString *text,
    const QTextOption *textOption) {
  return new QRectF(self->tightBoundingRect(*text, *textOption));
}

//  QString QFontMetricsF::elidedText(const QString &text, Qt::TextElideMode
//      mode, qreal width, int flags) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFontMetricsF10elidedTextERK7QStringN2Qt13TextElideModeEdi(
    const QFontMetricsF *self,
    const QString *text,
    Qt::TextElideMode mode,
    qreal width,
    int flags) {
  return new QString(self->elidedText(*text, mode, width, flags));
}

//  qreal QFontMetricsF::underlinePos() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF12underlinePosEv(const QFontMetricsF *self) {
  return self->underlinePos();
}

//  qreal QFontMetricsF::overlinePos() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF11overlinePosEv(const QFontMetricsF *self) {
  return self->overlinePos();
}

//  qreal QFontMetricsF::strikeOutPos() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF12strikeOutPosEv(const QFontMetricsF *self) {
  return self->strikeOutPos();
}

//  qreal QFontMetricsF::lineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF9lineWidthEv(const QFontMetricsF *self) {
  return self->lineWidth();
}

//  qreal QFontMetricsF::fontDpi() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QFontMetricsF7fontDpiEv(const QFontMetricsF *self) {
  return self->fontDpi();
}

//  bool QFontMetricsF::operator==(const QFontMetricsF &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontMetricsFeqERKS_(
    const QFontMetricsF *self,
    const QFontMetricsF *other) {
  return self->operator==(*other);
}

//  bool QFontMetricsF::operator!=(const QFontMetricsF &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontMetricsFneERKS_(
    const QFontMetricsF *self,
    const QFontMetricsF *other) {
  return self->operator!=(*other);
}
