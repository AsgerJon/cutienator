//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qplaintextedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>

//  const QMetaObject *QPlainTextDocumentLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QPlainTextDocumentLayout10metaObjectEv(
    const QPlainTextDocumentLayout *self) {
  return self->metaObject();
}

//  QString QPlainTextDocumentLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QPlainTextDocumentLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlainTextDocumentLayout::tr(s, c, n));
}

//  QPlainTextDocumentLayout::QPlainTextDocumentLayout(QTextDocument
//      *document)
extern "C" Q_DECL_EXPORT
QPlainTextDocumentLayout *ritual_ZN24QPlainTextDocumentLayoutC1EP13QTextDocument(
    QTextDocument *document) {
  return new QPlainTextDocumentLayout(document);
}

//  QPlainTextDocumentLayout::~QPlainTextDocumentLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayoutD1Ev(
    QPlainTextDocumentLayout *self) {
  delete self;
}

//  void QPlainTextDocumentLayout::draw(QPainter *a0, const PaintContext &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout4drawEP8QPainterRKN27QAbstractTextDocumentLayout12PaintContextE(
    QPlainTextDocumentLayout *self,
    QPainter *a0,
    const QAbstractTextDocumentLayout::PaintContext *a1) {
  self->draw(a0, *a1);
}

//  int QPlainTextDocumentLayout::hitTest(const QPointF &a0,
//      Qt::HitTestAccuracy a1) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPlainTextDocumentLayout7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QPlainTextDocumentLayout *self,
    const QPointF *a0,
    Qt::HitTestAccuracy a1) {
  return self->hitTest(*a0, a1);
}

//  int QPlainTextDocumentLayout::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPlainTextDocumentLayout9pageCountEv(
    const QPlainTextDocumentLayout *self) {
  return self->pageCount();
}

//  QSizeF QPlainTextDocumentLayout::documentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK24QPlainTextDocumentLayout12documentSizeEv(
    const QPlainTextDocumentLayout *self) {
  return new QSizeF(self->documentSize());
}

//  QRectF QPlainTextDocumentLayout::frameBoundingRect(QTextFrame *a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QPlainTextDocumentLayout17frameBoundingRectEP10QTextFrame(
    const QPlainTextDocumentLayout *self,
    QTextFrame *a0) {
  return new QRectF(self->frameBoundingRect(a0));
}

//  QRectF QPlainTextDocumentLayout::blockBoundingRect(const QTextBlock
//      &block) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QPlainTextDocumentLayout17blockBoundingRectERK10QTextBlock(
    const QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

//  void QPlainTextDocumentLayout::ensureBlockLayout(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QPlainTextDocumentLayout17ensureBlockLayoutERK10QTextBlock(
    const QPlainTextDocumentLayout *self,
    const QTextBlock *block) {
  self->ensureBlockLayout(*block);
}

//  void QPlainTextDocumentLayout::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout14setCursorWidthEi(
    QPlainTextDocumentLayout *self,
    int width) {
  self->setCursorWidth(width);
}

//  int QPlainTextDocumentLayout::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPlainTextDocumentLayout11cursorWidthEv(
    const QPlainTextDocumentLayout *self) {
  return self->cursorWidth();
}

//  void QPlainTextDocumentLayout::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPlainTextDocumentLayout13requestUpdateEv(
    QPlainTextDocumentLayout *self) {
  self->requestUpdate();
}
