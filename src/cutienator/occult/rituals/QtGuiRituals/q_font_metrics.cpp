//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfontmetrics.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfontmetrics.h>
#include <QtGui/qfont.h>
#include <QtCore/qchar.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextoption.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QFontMetrics::QFontMetrics(const QFont &a0)
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QFontMetricsC1ERK5QFont(const QFont *a0) {
  return new QFontMetrics(*a0);
}

//  QFontMetrics::QFontMetrics(const QFont &font, const QPaintDevice *pd)
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QFontMetricsC1ERK5QFontPK12QPaintDevice(
    const QFont *font,
    const QPaintDevice *pd) {
  return new QFontMetrics(*font, pd);
}

//  QFontMetrics::QFontMetrics(const QFontMetrics &a0)
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QFontMetricsC1ERKS_(const QFontMetrics *a0) {
  return new QFontMetrics(*a0);
}

//  QFontMetrics::QFontMetrics(QFontMetrics &&a0)
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QFontMetricsC1EOS_(QFontMetrics *a0) {
  return new QFontMetrics(std::move(*a0));
}

//  QFontMetrics::~QFontMetrics()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontMetricsD1Ev(QFontMetrics *self) {
  delete self;
}

//  QFontMetrics &QFontMetrics::operator=(const QFontMetrics &a0)
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QFontMetricsaSERKS_(
    QFontMetrics *self,
    const QFontMetrics *a0) {
  return &(self->operator=(*a0));
}

//  QFontMetrics &QFontMetrics::operator=(QFontMetrics &&other)
extern "C" Q_DECL_EXPORT
QFontMetrics *ritual_ZN12QFontMetricsaSEOS_(
    QFontMetrics *self,
    QFontMetrics *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QFontMetrics::swap(QFontMetrics &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QFontMetrics4swapERS_(
    QFontMetrics *self,
    QFontMetrics *other) {
  self->swap(*other);
}

//  int QFontMetrics::ascent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics6ascentEv(const QFontMetrics *self) {
  return self->ascent();
}

//  int QFontMetrics::capHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics9capHeightEv(const QFontMetrics *self) {
  return self->capHeight();
}

//  int QFontMetrics::descent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics7descentEv(const QFontMetrics *self) {
  return self->descent();
}

//  int QFontMetrics::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics6heightEv(const QFontMetrics *self) {
  return self->height();
}

//  int QFontMetrics::leading() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics7leadingEv(const QFontMetrics *self) {
  return self->leading();
}

//  int QFontMetrics::lineSpacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics11lineSpacingEv(const QFontMetrics *self) {
  return self->lineSpacing();
}

//  int QFontMetrics::minLeftBearing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics14minLeftBearingEv(const QFontMetrics *self) {
  return self->minLeftBearing();
}

//  int QFontMetrics::minRightBearing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics15minRightBearingEv(const QFontMetrics *self) {
  return self->minRightBearing();
}

//  int QFontMetrics::maxWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics8maxWidthEv(const QFontMetrics *self) {
  return self->maxWidth();
}

//  int QFontMetrics::xHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics7xHeightEv(const QFontMetrics *self) {
  return self->xHeight();
}

//  int QFontMetrics::averageCharWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics16averageCharWidthEv(const QFontMetrics *self) {
  return self->averageCharWidth();
}

//  bool QFontMetrics::inFont(QChar a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QFontMetrics6inFontE5QChar(
    const QFontMetrics *self,
    const QChar *a0) {
  return self->inFont(*a0);
}

//  bool QFontMetrics::inFontUcs4(uint ucs4) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QFontMetrics10inFontUcs4Ej(
    const QFontMetrics *self,
    uint ucs4) {
  return self->inFontUcs4(ucs4);
}

//  int QFontMetrics::leftBearing(QChar a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics11leftBearingE5QChar(
    const QFontMetrics *self,
    const QChar *a0) {
  return self->leftBearing(*a0);
}

//  int QFontMetrics::rightBearing(QChar a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics12rightBearingE5QChar(
    const QFontMetrics *self,
    const QChar *a0) {
  return self->rightBearing(*a0);
}

//  int QFontMetrics::horizontalAdvance(const QString &a0, int len) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics17horizontalAdvanceERK7QStringi(
    const QFontMetrics *self,
    const QString *a0,
    int len) {
  return self->horizontalAdvance(*a0, len);
}

//  int QFontMetrics::horizontalAdvance(const QString &a0, const QTextOption
//      &textOption) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics17horizontalAdvanceERK7QStringRK11QTextOption(
    const QFontMetrics *self,
    const QString *a0,
    const QTextOption *textOption) {
  return self->horizontalAdvance(*a0, *textOption);
}

//  int QFontMetrics::horizontalAdvance(QChar a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics17horizontalAdvanceE5QChar(
    const QFontMetrics *self,
    const QChar *a0) {
  return self->horizontalAdvance(*a0);
}

//  QRect QFontMetrics::boundingRect(QChar a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics12boundingRectE5QChar(
    const QFontMetrics *self,
    const QChar *a0) {
  return new QRect(self->boundingRect(*a0));
}

//  QRect QFontMetrics::boundingRect(const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics12boundingRectERK7QString(
    const QFontMetrics *self,
    const QString *text) {
  return new QRect(self->boundingRect(*text));
}

//  QRect QFontMetrics::boundingRect(const QString &text, const QTextOption
//      &textOption) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics12boundingRectERK7QStringRK11QTextOption(
    const QFontMetrics *self,
    const QString *text,
    const QTextOption *textOption) {
  return new QRect(self->boundingRect(*text, *textOption));
}

//  QRect QFontMetrics::boundingRect(const QRect &r, int flags, const QString
//      &text, int tabstops, int *tabarray) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics12boundingRectERK5QRectiRK7QStringiPi(
    const QFontMetrics *self,
    const QRect *r,
    int flags,
    const QString *text,
    int tabstops,
    int *tabarray) {
  return new QRect(self->boundingRect(*r, flags, *text, tabstops, tabarray));
}

//  QRect QFontMetrics::boundingRect(int x, int y, int w, int h, int flags,
//      const QString &text, int tabstops, int *tabarray) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics12boundingRectEiiiiiRK7QStringiPi(
    const QFontMetrics *self,
    int x,
    int y,
    int w,
    int h,
    int flags,
    const QString *text,
    int tabstops,
    int *tabarray) {
  return new QRect(
      self->boundingRect(
          x,
          y,
          w,
          h,
          flags,
          *text,
          tabstops,
          tabarray));
}

//  QSize QFontMetrics::size(int flags, const QString &str, int tabstops, int
//      *tabarray) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QFontMetrics4sizeEiRK7QStringiPi(
    const QFontMetrics *self,
    int flags,
    const QString *str,
    int tabstops,
    int *tabarray) {
  return new QSize(self->size(flags, *str, tabstops, tabarray));
}

//  QRect QFontMetrics::tightBoundingRect(const QString &text) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics17tightBoundingRectERK7QString(
    const QFontMetrics *self,
    const QString *text) {
  return new QRect(self->tightBoundingRect(*text));
}

//  QRect QFontMetrics::tightBoundingRect(const QString &text, const
//      QTextOption &textOption) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QFontMetrics17tightBoundingRectERK7QStringRK11QTextOption(
    const QFontMetrics *self,
    const QString *text,
    const QTextOption *textOption) {
  return new QRect(self->tightBoundingRect(*text, *textOption));
}

//  QString QFontMetrics::elidedText(const QString &text, Qt::TextElideMode
//      mode, int width, int flags) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QFontMetrics10elidedTextERK7QStringN2Qt13TextElideModeEii(
    const QFontMetrics *self,
    const QString *text,
    Qt::TextElideMode mode,
    int width,
    int flags) {
  return new QString(self->elidedText(*text, mode, width, flags));
}

//  int QFontMetrics::underlinePos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics12underlinePosEv(const QFontMetrics *self) {
  return self->underlinePos();
}

//  int QFontMetrics::overlinePos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics11overlinePosEv(const QFontMetrics *self) {
  return self->overlinePos();
}

//  int QFontMetrics::strikeOutPos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics12strikeOutPosEv(const QFontMetrics *self) {
  return self->strikeOutPos();
}

//  int QFontMetrics::lineWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QFontMetrics9lineWidthEv(const QFontMetrics *self) {
  return self->lineWidth();
}

//  qreal QFontMetrics::fontDpi() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QFontMetrics7fontDpiEv(const QFontMetrics *self) {
  return self->fontDpi();
}

//  bool QFontMetrics::operator==(const QFontMetrics &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QFontMetricseqERKS_(
    const QFontMetrics *self,
    const QFontMetrics *other) {
  return self->operator==(*other);
}

//  bool QFontMetrics::operator!=(const QFontMetrics &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QFontMetricsneERKS_(
    const QFontMetrics *self,
    const QFontMetrics *other) {
  return self->operator!=(*other);
}
