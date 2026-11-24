//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#include <QtCore/qline.h>

//  QTextEngine::QTextEngine()
extern "C" Q_DECL_EXPORT
QTextEngine *ritual_ZN11QTextEngineC1Ev() {
  return new QTextEngine();
}

//  QTextEngine::QTextEngine(const QString &str, const QFont &f)
extern "C" Q_DECL_EXPORT
QTextEngine *ritual_ZN11QTextEngineC1ERK7QStringRK5QFont(
    const QString *str,
    const QFont *f) {
  return new QTextEngine(*str, *f);
}

//  QTextEngine::~QTextEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngineD1Ev(QTextEngine *self) {
  delete self;
}

//  void QTextEngine::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine10invalidateEv(QTextEngine *self) {
  self->invalidate();
}

//  void QTextEngine::clearLineData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine13clearLineDataEv(QTextEngine *self) {
  self->clearLineData();
}

//  void QTextEngine::validate() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine8validateEv(const QTextEngine *self) {
  self->validate();
}

//  void QTextEngine::itemize() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine7itemizeEv(const QTextEngine *self) {
  self->itemize();
}

//  bool QTextEngine::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextEngine13isRightToLeftEv(const QTextEngine *self) {
  return self->isRightToLeft();
}

//  const QCharAttributes *QTextEngine::attributes() const
extern "C" Q_DECL_EXPORT
const QCharAttributes *ritual_ZNK11QTextEngine10attributesEv(
    const QTextEngine *self) {
  return self->attributes();
}

//  void QTextEngine::shape(int item) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine5shapeEi(const QTextEngine *self, int item) {
  self->shape(item);
}

//  void QTextEngine::justify(const QScriptLine &si)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine7justifyERK11QScriptLine(
    QTextEngine *self,
    const QScriptLine *si) {
  self->justify(*si);
}

//  QFixed QTextEngine::alignLine(const QScriptLine &line)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN11QTextEngine9alignLineERK11QScriptLine(
    QTextEngine *self,
    const QScriptLine *line) {
  return new QFixed(self->alignLine(*line));
}

//  QFixed QTextEngine::width(int charFrom, int numChars) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QTextEngine5widthEii(
    const QTextEngine *self,
    int charFrom,
    int numChars) {
  return new QFixed(self->width(charFrom, numChars));
}

//  glyph_metrics_t QTextEngine::boundingBox(int from, int len) const
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZNK11QTextEngine11boundingBoxEii(
    const QTextEngine *self,
    int from,
    int len) {
  return new glyph_metrics_t(self->boundingBox(from, len));
}

//  glyph_metrics_t QTextEngine::tightBoundingBox(int from, int len) const
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZNK11QTextEngine16tightBoundingBoxEii(
    const QTextEngine *self,
    int from,
    int len) {
  return new glyph_metrics_t(self->tightBoundingBox(from, len));
}

//  int QTextEngine::length(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine6lengthEi(const QTextEngine *self, int item) {
  return self->length(item);
}

//  int QTextEngine::length(const QScriptItem *si) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine6lengthEPK11QScriptItem(
    const QTextEngine *self,
    const QScriptItem *si) {
  return self->length(si);
}

//  QFontEngine *QTextEngine::fontEngine(const QScriptItem &si, QFixed
//      *ascent, QFixed *descent, QFixed *leading) const
extern "C" Q_DECL_EXPORT
QFontEngine *ritual_ZNK11QTextEngine10fontEngineERK11QScriptItemP6QFixedS4_S4_(
    const QTextEngine *self,
    const QScriptItem *si,
    QFixed *ascent,
    QFixed *descent,
    QFixed *leading) {
  return self->fontEngine(*si, ascent, descent, leading);
}

//  QFont QTextEngine::font(const QScriptItem &si) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QTextEngine4fontERK11QScriptItem(
    const QTextEngine *self,
    const QScriptItem *si) {
  return new QFont(self->font(*si));
}

//  QFont QTextEngine::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK11QTextEngine4fontEv(const QTextEngine *self) {
  return new QFont(self->font());
}

//  QGlyphLayout QTextEngine::availableGlyphs(const QScriptItem *si) const
extern "C" Q_DECL_EXPORT
QGlyphLayout *ritual_ZNK11QTextEngine15availableGlyphsEPK11QScriptItem(
    const QTextEngine *self,
    const QScriptItem *si) {
  return new QGlyphLayout(self->availableGlyphs(si));
}

//  QGlyphLayout QTextEngine::shapedGlyphs(const QScriptItem *si) const
extern "C" Q_DECL_EXPORT
QGlyphLayout *ritual_ZNK11QTextEngine12shapedGlyphsEPK11QScriptItem(
    const QTextEngine *self,
    const QScriptItem *si) {
  return new QGlyphLayout(self->shapedGlyphs(si));
}

//  bool QTextEngine::ensureSpace(int nGlyphs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextEngine11ensureSpaceEi(
    const QTextEngine *self,
    int nGlyphs) {
  return self->ensureSpace(nGlyphs);
}

//  void QTextEngine::freeMemory()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine10freeMemoryEv(QTextEngine *self) {
  self->freeMemory();
}

//  int QTextEngine::findItem(int strPos, int firstItem) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine8findItemEii(
    const QTextEngine *self,
    int strPos,
    int firstItem) {
  return self->findItem(strPos, firstItem);
}

//  QTextFormatCollection *QTextEngine::formatCollection() const
extern "C" Q_DECL_EXPORT
QTextFormatCollection *ritual_ZNK11QTextEngine16formatCollectionEv(
    const QTextEngine *self) {
  return self->formatCollection();
}

//  QTextCharFormat QTextEngine::format(const QScriptItem *si) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK11QTextEngine6formatEPK11QScriptItem(
    const QTextEngine *self,
    const QScriptItem *si) {
  return new QTextCharFormat(self->format(si));
}

//  QAbstractTextDocumentLayout *QTextEngine::docLayout() const
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout *ritual_ZNK11QTextEngine9docLayoutEv(
    const QTextEngine *self) {
  return self->docLayout();
}

//  int QTextEngine::formatIndex(const QScriptItem *si) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine11formatIndexEPK11QScriptItem(
    const QTextEngine *self,
    const QScriptItem *si) {
  return self->formatIndex(si);
}

//  QFixed QTextEngine::calculateTabWidth(int index, QFixed x) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QTextEngine17calculateTabWidthEi6QFixed(
    const QTextEngine *self,
    int index,
    const QFixed *x) {
  return new QFixed(self->calculateTabWidth(index, *x));
}

//  bool QTextEngine::visualCursorMovement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextEngine20visualCursorMovementEv(
    const QTextEngine *self) {
  return self->visualCursorMovement();
}

//  int QTextEngine::preeditAreaPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine19preeditAreaPositionEv(const QTextEngine *self) {
  return self->preeditAreaPosition();
}

//  QString QTextEngine::preeditAreaText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextEngine15preeditAreaTextEv(
    const QTextEngine *self) {
  return new QString(self->preeditAreaText());
}

//  void QTextEngine::setPreeditArea(int position, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine14setPreeditAreaEiRK7QString(
    QTextEngine *self,
    int position,
    const QString *text) {
  self->setPreeditArea(position, *text);
}

//  bool QTextEngine::hasFormats() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextEngine10hasFormatsEv(const QTextEngine *self) {
  return self->hasFormats();
}

//  void QTextEngine::init(QTextEngine *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine4initEPS_(QTextEngine *e) {
  QTextEngine::init(e);
}

//  void QTextEngine::indexFormats()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine12indexFormatsEv(QTextEngine *self) {
  self->indexFormats();
}

//  void QTextEngine::resolveFormats() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine14resolveFormatsEv(const QTextEngine *self) {
  self->resolveFormats();
}

//  bool QTextEngine::atWordSeparator(int position) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextEngine15atWordSeparatorEi(
    const QTextEngine *self,
    int position) {
  return self->atWordSeparator(position);
}

//  QString QTextEngine::elidedText(Qt::TextElideMode mode, QFixed width, int
//      flags, int from, int count) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextEngine10elidedTextEN2Qt13TextElideModeE6QFixediii(
    const QTextEngine *self,
    Qt::TextElideMode mode,
    const QFixed *width,
    int flags,
    int from,
    int count) {
  return new QString(self->elidedText(mode, *width, flags, from, count));
}

//  void QTextEngine::shapeLine(const QScriptLine &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine9shapeLineERK11QScriptLine(
    QTextEngine *self,
    const QScriptLine *line) {
  self->shapeLine(*line);
}

//  QFixed QTextEngine::leadingSpaceWidth(const QScriptLine &line)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN11QTextEngine17leadingSpaceWidthERK11QScriptLine(
    QTextEngine *self,
    const QScriptLine *line) {
  return new QFixed(self->leadingSpaceWidth(*line));
}

//  QFixed QTextEngine::offsetInLigature(const QScriptItem *si, int pos, int
//      max, int glyph_pos)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN11QTextEngine16offsetInLigatureEPK11QScriptItemiii(
    QTextEngine *self,
    const QScriptItem *si,
    int pos,
    int max,
    int glyph_pos) {
  return new QFixed(self->offsetInLigature(si, pos, max, glyph_pos));
}

//  int QTextEngine::positionInLigature(const QScriptItem *si, int end,
//      QFixed x, QFixed edge, int glyph_pos, bool cursorOnCharacter)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTextEngine18positionInLigatureEPK11QScriptItemi6QFixedS3_ib(
    QTextEngine *self,
    const QScriptItem *si,
    int end,
    const QFixed *x,
    const QFixed *edge,
    int glyph_pos,
    bool cursorOnCharacter) {
  return self->positionInLigature(
      si,
      end,
      *x,
      *edge,
      glyph_pos,
      cursorOnCharacter);
}

//  int QTextEngine::previousLogicalPosition(int oldPos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine23previousLogicalPositionEi(
    const QTextEngine *self,
    int oldPos) {
  return self->previousLogicalPosition(oldPos);
}

//  int QTextEngine::nextLogicalPosition(int oldPos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextEngine19nextLogicalPositionEi(
    const QTextEngine *self,
    int oldPos) {
  return self->nextLogicalPosition(oldPos);
}

//  int QTextEngine::lineNumberForTextPosition(int pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTextEngine25lineNumberForTextPositionEi(
    QTextEngine *self,
    int pos) {
  return self->lineNumberForTextPosition(pos);
}

//  int QTextEngine::positionAfterVisualMovement(int oldPos,
//      QTextCursor::MoveOperation op)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTextEngine27positionAfterVisualMovementEiN11QTextCursor13MoveOperationE(
    QTextEngine *self,
    int oldPos,
    QTextCursor::MoveOperation op) {
  return self->positionAfterVisualMovement(oldPos, op);
}

//  void QTextEngine::resetFontEngineCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine20resetFontEngineCacheEv(QTextEngine *self) {
  self->resetFontEngineCache();
}

//  void QTextEngine::enableDelayDecorations(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine22enableDelayDecorationsEb(
    QTextEngine *self,
    bool enable) {
  self->enableDelayDecorations(enable);
}

//  void QTextEngine::addUnderline(QPainter *painter, const QLineF &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine12addUnderlineEP8QPainterRK6QLineF(
    QTextEngine *self,
    QPainter *painter,
    const QLineF *line) {
  self->addUnderline(painter, *line);
}

//  void QTextEngine::addStrikeOut(QPainter *painter, const QLineF &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine12addStrikeOutEP8QPainterRK6QLineF(
    QTextEngine *self,
    QPainter *painter,
    const QLineF *line) {
  self->addStrikeOut(painter, *line);
}

//  void QTextEngine::addOverline(QPainter *painter, const QLineF &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine11addOverlineEP8QPainterRK6QLineF(
    QTextEngine *self,
    QPainter *painter,
    const QLineF *line) {
  self->addOverline(painter, *line);
}

//  void QTextEngine::drawDecorations(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine15drawDecorationsEP8QPainter(
    QTextEngine *self,
    QPainter *painter) {
  self->drawDecorations(painter);
}

//  void QTextEngine::clearDecorations()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine16clearDecorationsEv(QTextEngine *self) {
  self->clearDecorations();
}

//  void QTextEngine::adjustUnderlines()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextEngine16adjustUnderlinesEv(QTextEngine *self) {
  self->adjustUnderlines();
}

//  void QTextEngine::setBoundary(int strPos) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine11setBoundaryEi(
    const QTextEngine *self,
    int strPos) {
  self->setBoundary(strPos);
}

//  void QTextEngine::addRequiredBoundaries() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine21addRequiredBoundariesEv(
    const QTextEngine *self) {
  self->addRequiredBoundaries();
}

//  void QTextEngine::shapeText(int item) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextEngine9shapeTextEi(const QTextEngine *self, int item) {
  self->shapeText(item);
}

//  int QTextEngine::endOfLine(int lineNum)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTextEngine9endOfLineEi(QTextEngine *self, int lineNum) {
  return self->endOfLine(lineNum);
}

//  int QTextEngine::beginningOfLine(int lineNum)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTextEngine15beginningOfLineEi(
    QTextEngine *self,
    int lineNum) {
  return self->beginningOfLine(lineNum);
}

//  int QTextEngine::getClusterLength(unsigned short *logClusters, const
//      QCharAttributes *attributes, int from, int to, int glyph_pos, int
//      *start)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QTextEngine16getClusterLengthEPtPK15QCharAttributesiiiPi(
    QTextEngine *self,
    unsigned short *logClusters,
    const QCharAttributes *attributes,
    int from,
    int to,
    int glyph_pos,
    int *start) {
  return self->getClusterLength(
      logClusters,
      attributes,
      from,
      to,
      glyph_pos,
      start);
}
