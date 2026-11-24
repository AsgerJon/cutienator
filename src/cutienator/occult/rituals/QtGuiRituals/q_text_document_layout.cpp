//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocumentlayout_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocumentlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtexttable.h>
#include <QtGui/qtextlayout.h>
#include <QtGui/qtextformat.h>

//  Only a class built on QTextDocumentLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTextDocumentLayout : QTextDocumentLayout {
  using QTextDocumentLayout::documentChanged;
  using QTextDocumentLayout::resizeInlineObject;
  using QTextDocumentLayout::positionInlineObject;
  using QTextDocumentLayout::drawInlineObject;
  using QTextDocumentLayout::timerEvent;
};

//  const QMetaObject *QTextDocumentLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QTextDocumentLayout10metaObjectEv(
    const QTextDocumentLayout *self) {
  return self->metaObject();
}

//  QString QTextDocumentLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QTextDocumentLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextDocumentLayout::tr(s, c, n));
}

//  QTextDocumentLayout::QTextDocumentLayout(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextDocumentLayout *ritual_ZN19QTextDocumentLayoutC1EP13QTextDocument(
    QTextDocument *doc) {
  return new QTextDocumentLayout(doc);
}

//  void QTextDocumentLayout::draw(QPainter *painter, const PaintContext
//      &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout4drawEP8QPainterRKN27QAbstractTextDocumentLayout12PaintContextE(
    QTextDocumentLayout *self,
    QPainter *painter,
    const QAbstractTextDocumentLayout::PaintContext *context) {
  self->draw(painter, *context);
}

//  int QTextDocumentLayout::hitTest(const QPointF &point,
//      Qt::HitTestAccuracy accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QTextDocumentLayout *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->hitTest(*point, accuracy);
}

//  int QTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextDocumentLayout9pageCountEv(
    const QTextDocumentLayout *self) {
  return self->pageCount();
}

//  QSizeF QTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QTextDocumentLayout12documentSizeEv(
    const QTextDocumentLayout *self) {
  return new QSizeF(self->documentSize());
}

//  void QTextDocumentLayout::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout14setCursorWidthEi(
    QTextDocumentLayout *self,
    int width) {
  self->setCursorWidth(width);
}

//  int QTextDocumentLayout::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextDocumentLayout11cursorWidthEv(
    const QTextDocumentLayout *self) {
  return self->cursorWidth();
}

//  void QTextDocumentLayout::setFixedColumnWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout19setFixedColumnWidthEi(
    QTextDocumentLayout *self,
    int width) {
  self->setFixedColumnWidth(width);
}

//  void QTextDocumentLayout::setViewport(const QRectF &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout11setViewportERK6QRectF(
    QTextDocumentLayout *self,
    const QRectF *viewport) {
  self->setViewport(*viewport);
}

//  QRectF QTextDocumentLayout::frameBoundingRect(QTextFrame *frame) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QTextDocumentLayout *self,
    QTextFrame *frame) {
  return new QRectF(self->frameBoundingRect(frame));
}

//  QRectF QTextDocumentLayout::blockBoundingRect(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

//  QRectF QTextDocumentLayout::tableBoundingRect(QTextTable *table) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QTextDocumentLayout17tableBoundingRectEP10QTextTable(
    const QTextDocumentLayout *self,
    QTextTable *table) {
  return new QRectF(self->tableBoundingRect(table));
}

//  QRectF QTextDocumentLayout::tableCellBoundingRect(QTextTable *table,
//      const QTextTableCell &cell) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QTextDocumentLayout21tableCellBoundingRectEP10QTextTableRK14QTextTableCell(
    const QTextDocumentLayout *self,
    QTextTable *table,
    const QTextTableCell *cell) {
  return new QRectF(self->tableCellBoundingRect(table, *cell));
}

//  int QTextDocumentLayout::layoutStatus() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextDocumentLayout12layoutStatusEv(
    const QTextDocumentLayout *self) {
  return self->layoutStatus();
}

//  int QTextDocumentLayout::dynamicPageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextDocumentLayout16dynamicPageCountEv(
    const QTextDocumentLayout *self) {
  return self->dynamicPageCount();
}

//  QSizeF QTextDocumentLayout::dynamicDocumentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QTextDocumentLayout19dynamicDocumentSizeEv(
    const QTextDocumentLayout *self) {
  return new QSizeF(self->dynamicDocumentSize());
}

//  void QTextDocumentLayout::ensureLayouted(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout14ensureLayoutedEd(
    QTextDocumentLayout *self,
    qreal a0) {
  self->ensureLayouted(a0);
}

//  qreal QTextDocumentLayout::idealWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QTextDocumentLayout10idealWidthEv(
    const QTextDocumentLayout *self) {
  return self->idealWidth();
}

//  bool QTextDocumentLayout::contentHasAlignment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextDocumentLayout19contentHasAlignmentEv(
    const QTextDocumentLayout *self) {
  return self->contentHasAlignment();
}

//  void QTextDocumentLayout::documentChanged(int from, int oldLength, int
//      length)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout15documentChangedEiii(
    QTextDocumentLayout *self,
    int from,
    int oldLength,
    int length) {
  self->documentChanged(from, oldLength, length);
}

//  void QTextDocumentLayout::resizeInlineObject(QTextInlineObject item, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout18resizeInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  self->resizeInlineObject(*item, posInDocument, *format);
}

//  void QTextDocumentLayout::positionInlineObject(QTextInlineObject item,
//      int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout20positionInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  self->positionInlineObject(*item, posInDocument, *format);
}

//  void QTextDocumentLayout::drawInlineObject(QPainter *p, const QRectF
//      &rect, QTextInlineObject item, int posInDocument, const QTextFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout16drawInlineObjectEP8QPainterRK6QRectF17QTextInlineObjectiRK11QTextFormat(
    QTextDocumentLayout *self,
    QPainter *p,
    const QRectF *rect,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  self->drawInlineObject(p, *rect, *item, posInDocument, *format);
}

//  void QTextDocumentLayout::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout10timerEventEP11QTimerEvent(
    QTextDocumentLayout *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  QRectF QTextDocumentLayout::doLayout(int from, int oldLength, int length)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN19QTextDocumentLayout8doLayoutEiii(
    QTextDocumentLayout *self,
    int from,
    int oldLength,
    int length) {
  return new QRectF(self->doLayout(from, oldLength, length));
}

//  void QTextDocumentLayout::layoutFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextDocumentLayout14layoutFinishedEv(
    QTextDocumentLayout *self) {
  self->layoutFinished();
}

//  void QTextDocumentLayout::draw(QPainter *painter, const PaintContext
//      &context)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QTextDocumentLayout4drawEP8QPainterRKN27QAbstractTextDocumentLayout12PaintContextE(
    QTextDocumentLayout *self,
    QPainter *painter,
    const QAbstractTextDocumentLayout::PaintContext *context) {
  self->QTextDocumentLayout::draw(painter, *context);
}

//  int QTextDocumentLayout::hitTest(const QPointF &point,
//      Qt::HitTestAccuracy accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QTextDocumentLayout *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->QTextDocumentLayout::hitTest(*point, accuracy);
}

//  int QTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QTextDocumentLayout9pageCountEv(
    const QTextDocumentLayout *self) {
  return self->QTextDocumentLayout::pageCount();
}

//  QSizeF QTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK19QTextDocumentLayout12documentSizeEv(
    const QTextDocumentLayout *self) {
  return new QSizeF(self->QTextDocumentLayout::documentSize());
}

//  QRectF QTextDocumentLayout::frameBoundingRect(QTextFrame *frame) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QTextDocumentLayout *self,
    QTextFrame *frame) {
  return new QRectF(self->QTextDocumentLayout::frameBoundingRect(frame));
}

//  QRectF QTextDocumentLayout::blockBoundingRect(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(self->QTextDocumentLayout::blockBoundingRect(*block));
}

//  void QTextDocumentLayout::documentChanged(int from, int oldLength, int
//      length)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QTextDocumentLayout15documentChangedEiii(
    QTextDocumentLayout *self,
    int from,
    int oldLength,
    int length) {
  static_cast<OwnQTextDocumentLayout *>(self)->OwnQTextDocumentLayout::documentChanged(
      from,
      oldLength,
      length);
}

//  void QTextDocumentLayout::resizeInlineObject(QTextInlineObject item, int
//      posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QTextDocumentLayout18resizeInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  static_cast<OwnQTextDocumentLayout *>(self)->OwnQTextDocumentLayout::resizeInlineObject(
      *item,
      posInDocument,
      *format);
}

//  void QTextDocumentLayout::positionInlineObject(QTextInlineObject item,
//      int posInDocument, const QTextFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QTextDocumentLayout20positionInlineObjectE17QTextInlineObjectiRK11QTextFormat(
    QTextDocumentLayout *self,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  static_cast<OwnQTextDocumentLayout *>(self)->OwnQTextDocumentLayout::positionInlineObject(
      *item,
      posInDocument,
      *format);
}

//  void QTextDocumentLayout::drawInlineObject(QPainter *p, const QRectF
//      &rect, QTextInlineObject item, int posInDocument, const QTextFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QTextDocumentLayout16drawInlineObjectEP8QPainterRK6QRectF17QTextInlineObjectiRK11QTextFormat(
    QTextDocumentLayout *self,
    QPainter *p,
    const QRectF *rect,
    const QTextInlineObject *item,
    int posInDocument,
    const QTextFormat *format) {
  static_cast<OwnQTextDocumentLayout *>(self)->OwnQTextDocumentLayout::drawInlineObject(
      p,
      *rect,
      *item,
      posInDocument,
      *format);
}

//  void QTextDocumentLayout::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QTextDocumentLayout10timerEventEP11QTimerEvent(
    QTextDocumentLayout *self,
    QTimerEvent *e) {
  static_cast<OwnQTextDocumentLayout *>(self)->OwnQTextDocumentLayout::timerEvent(
      e);
}
