//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextlayout.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qrawfont.h>
#include <QtGui/qtextoption.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qglyphrun.h>
#include <QtCore/qlist.h>

//  QTextLayout::QTextLayout()
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZN11QTextLayoutC1Ev() {
  return new QTextLayout();
}

//  QTextLayout::QTextLayout(const QString &text)
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZN11QTextLayoutC1ERK7QString(const QString *text) {
  return new QTextLayout(*text);
}

//  QTextLayout::QTextLayout(const QString &text, const QFont &font, const
//      QPaintDevice *paintdevice)
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZN11QTextLayoutC1ERK7QStringRK5QFontPK12QPaintDevice(
    const QString *text,
    const QFont *font,
    const QPaintDevice *paintdevice) {
  return new QTextLayout(*text, *font, paintdevice);
}

//  QTextLayout::QTextLayout(const QTextBlock &b)
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZN11QTextLayoutC1ERK10QTextBlock(const QTextBlock *b) {
  return new QTextLayout(*b);
}

//  QTextLayout::~QTextLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayoutD1Ev(QTextLayout *self) {
  delete self;
}

//  void QTextLayout::setFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout7setFontERK5QFont(
    QTextLayout *self,
    const QFont *f) {
  self->setFont(*f);
}

//  QFont QTextLayout::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QTextLayout4fontEv(const QTextLayout *self) {
  return new QFont(self->font());
}

#if !defined(QT_NO_RAWFONT)
//  void QTextLayout::setRawFont(const QRawFont &rawFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout10setRawFontERK8QRawFont(
    QTextLayout *self,
    const QRawFont *rawFont) {
  self->setRawFont(*rawFont);
}
#endif  // !defined(QT_NO_RAWFONT)

//  void QTextLayout::setText(const QString &string)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout7setTextERK7QString(
    QTextLayout *self,
    const QString *string) {
  self->setText(*string);
}

//  QString QTextLayout::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextLayout4textEv(const QTextLayout *self) {
  return new QString(self->text());
}

//  void QTextLayout::setTextOption(const QTextOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout13setTextOptionERK11QTextOption(
    QTextLayout *self,
    const QTextOption *option) {
  self->setTextOption(*option);
}

//  const QTextOption &QTextLayout::textOption() const
extern "C" Q_DECL_EXPORT
QTextOption *ritual_ZNK11QTextLayout10textOptionEv(const QTextLayout *self) {
  return new QTextOption(self->textOption());
}

//  void QTextLayout::setPreeditArea(int position, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout14setPreeditAreaEiRK7QString(
    QTextLayout *self,
    int position,
    const QString *text) {
  self->setPreeditArea(position, *text);
}

//  int QTextLayout::preeditAreaPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextLayout19preeditAreaPositionEv(const QTextLayout *self) {
  return self->preeditAreaPosition();
}

//  QString QTextLayout::preeditAreaText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextLayout15preeditAreaTextEv(
    const QTextLayout *self) {
  return new QString(self->preeditAreaText());
}

//  void QTextLayout::clearFormats()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout12clearFormatsEv(QTextLayout *self) {
  self->clearFormats();
}

//  void QTextLayout::setCacheEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout15setCacheEnabledEb(
    QTextLayout *self,
    bool enable) {
  self->setCacheEnabled(enable);
}

//  bool QTextLayout::cacheEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextLayout12cacheEnabledEv(const QTextLayout *self) {
  return self->cacheEnabled();
}

//  void QTextLayout::setCursorMoveStyle(Qt::CursorMoveStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout18setCursorMoveStyleEN2Qt15CursorMoveStyleE(
    QTextLayout *self,
    Qt::CursorMoveStyle style) {
  self->setCursorMoveStyle(style);
}

//  Qt::CursorMoveStyle QTextLayout::cursorMoveStyle() const
extern "C" Q_DECL_EXPORT
Qt::CursorMoveStyle ritual_ZNK11QTextLayout15cursorMoveStyleEv(
    const QTextLayout *self) {
  return self->cursorMoveStyle();
}

//  void QTextLayout::beginLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout11beginLayoutEv(QTextLayout *self) {
  self->beginLayout();
}

//  void QTextLayout::endLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout9endLayoutEv(QTextLayout *self) {
  self->endLayout();
}

//  void QTextLayout::clearLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout11clearLayoutEv(QTextLayout *self) {
  self->clearLayout();
}

//  QTextLine QTextLayout::createLine()
extern "C" Q_DECL_EXPORT
QTextLine *ritual_ZN11QTextLayout10createLineEv(QTextLayout *self) {
  return new QTextLine(self->createLine());
}

//  int QTextLayout::lineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextLayout9lineCountEv(const QTextLayout *self) {
  return self->lineCount();
}

//  QTextLine QTextLayout::lineAt(int i) const
extern "C" Q_DECL_EXPORT
QTextLine *ritual_ZNK11QTextLayout6lineAtEi(const QTextLayout *self, int i) {
  return new QTextLine(self->lineAt(i));
}

//  QTextLine QTextLayout::lineForTextPosition(int pos) const
extern "C" Q_DECL_EXPORT
QTextLine *ritual_ZNK11QTextLayout19lineForTextPositionEi(
    const QTextLayout *self,
    int pos) {
  return new QTextLine(self->lineForTextPosition(pos));
}

//  bool QTextLayout::isValidCursorPosition(int pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextLayout21isValidCursorPositionEi(
    const QTextLayout *self,
    int pos) {
  return self->isValidCursorPosition(pos);
}

//  int QTextLayout::nextCursorPosition(int oldPos, CursorMode mode) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextLayout18nextCursorPositionEiNS_10CursorModeE(
    const QTextLayout *self,
    int oldPos,
    QTextLayout::CursorMode mode) {
  return self->nextCursorPosition(oldPos, mode);
}

//  int QTextLayout::previousCursorPosition(int oldPos, CursorMode mode)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextLayout22previousCursorPositionEiNS_10CursorModeE(
    const QTextLayout *self,
    int oldPos,
    QTextLayout::CursorMode mode) {
  return self->previousCursorPosition(oldPos, mode);
}

//  int QTextLayout::leftCursorPosition(int oldPos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextLayout18leftCursorPositionEi(
    const QTextLayout *self,
    int oldPos) {
  return self->leftCursorPosition(oldPos);
}

//  int QTextLayout::rightCursorPosition(int oldPos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextLayout19rightCursorPositionEi(
    const QTextLayout *self,
    int oldPos) {
  return self->rightCursorPosition(oldPos);
}

//  void QTextLayout::drawCursor(QPainter *p, const QPointF &pos, int
//      cursorPosition) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextLayout10drawCursorEP8QPainterRK7QPointFi(
    const QTextLayout *self,
    QPainter *p,
    const QPointF *pos,
    int cursorPosition) {
  self->drawCursor(p, *pos, cursorPosition);
}

//  void QTextLayout::drawCursor(QPainter *p, const QPointF &pos, int
//      cursorPosition, int width) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextLayout10drawCursorEP8QPainterRK7QPointFii(
    const QTextLayout *self,
    QPainter *p,
    const QPointF *pos,
    int cursorPosition,
    int width) {
  self->drawCursor(p, *pos, cursorPosition, width);
}

//  QPointF QTextLayout::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QTextLayout8positionEv(const QTextLayout *self) {
  return new QPointF(self->position());
}

//  void QTextLayout::setPosition(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout11setPositionERK7QPointF(
    QTextLayout *self,
    const QPointF *p) {
  self->setPosition(*p);
}

//  QRectF QTextLayout::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QTextLayout12boundingRectEv(const QTextLayout *self) {
  return new QRectF(self->boundingRect());
}

//  qreal QTextLayout::minimumWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QTextLayout12minimumWidthEv(const QTextLayout *self) {
  return self->minimumWidth();
}

//  qreal QTextLayout::maximumWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QTextLayout12maximumWidthEv(const QTextLayout *self) {
  return self->maximumWidth();
}

#if !defined(QT_NO_RAWFONT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QList<QGlyphRun> QTextLayout::glyphRuns(int from, int length,
//      GlyphRunRetrievalFlags flags) const
extern "C" Q_DECL_EXPORT
QList<QGlyphRun> *ritual_ZNK11QTextLayout9glyphRunsEii6QFlagsINS_21GlyphRunRetrievalFlagEE(
    const QTextLayout *self,
    int from,
    int length,
    int flags) {
  return new QList<QGlyphRun>(
      self->glyphRuns(
          from,
          length,
          QFlags<QTextLayout::GlyphRunRetrievalFlag>::fromInt(flags)));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_RAWFONT)

#if !defined(QT_NO_RAWFONT)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QList<QGlyphRun> QTextLayout::glyphRuns(int from, int length) const
extern "C" Q_DECL_EXPORT
QList<QGlyphRun> *ritual_ZNK11QTextLayout9glyphRunsEii(
    const QTextLayout *self,
    int from,
    int length) {
  return new QList<QGlyphRun>(self->glyphRuns(from, length));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_RAWFONT)

//  QTextEngine *QTextLayout::engine() const
extern "C" Q_DECL_EXPORT
QTextEngine *ritual_ZNK11QTextLayout6engineEv(const QTextLayout *self) {
  return self->engine();
}

//  void QTextLayout::setFlags(int flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextLayout8setFlagsEi(QTextLayout *self, int flags) {
  self->setFlags(flags);
}

//  QTextLayout::QTextLayout(QTextEngine *e)
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZN11QTextLayoutC1EP11QTextEngine(QTextEngine *e) {
  return new QTextLayout(e);
}
