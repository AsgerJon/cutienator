//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextlayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  QTextLine::QTextLine()
extern "C" Q_DECL_EXPORT
QTextLine *ritual_ZN9QTextLineC1Ev() {
  return new QTextLine();
}

//  bool QTextLine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextLine7isValidEv(const QTextLine *self) {
  return self->isValid();
}

//  QRectF QTextLine::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QTextLine4rectEv(const QTextLine *self) {
  return new QRectF(self->rect());
}

//  qreal QTextLine::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine1xEv(const QTextLine *self) {
  return self->x();
}

//  qreal QTextLine::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine1yEv(const QTextLine *self) {
  return self->y();
}

//  qreal QTextLine::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine5widthEv(const QTextLine *self) {
  return self->width();
}

//  qreal QTextLine::ascent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine6ascentEv(const QTextLine *self) {
  return self->ascent();
}

//  qreal QTextLine::descent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine7descentEv(const QTextLine *self) {
  return self->descent();
}

//  qreal QTextLine::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine6heightEv(const QTextLine *self) {
  return self->height();
}

//  qreal QTextLine::leading() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine7leadingEv(const QTextLine *self) {
  return self->leading();
}

//  void QTextLine::setLeadingIncluded(bool included)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextLine18setLeadingIncludedEb(
    QTextLine *self,
    bool included) {
  self->setLeadingIncluded(included);
}

//  bool QTextLine::leadingIncluded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextLine15leadingIncludedEv(const QTextLine *self) {
  return self->leadingIncluded();
}

//  qreal QTextLine::naturalTextWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine16naturalTextWidthEv(const QTextLine *self) {
  return self->naturalTextWidth();
}

//  qreal QTextLine::horizontalAdvance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine17horizontalAdvanceEv(const QTextLine *self) {
  return self->horizontalAdvance();
}

//  QRectF QTextLine::naturalTextRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QTextLine15naturalTextRectEv(const QTextLine *self) {
  return new QRectF(self->naturalTextRect());
}

//  qreal QTextLine::cursorToX(int *cursorPos, Edge edge) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine9cursorToXEPiNS_4EdgeE(
    const QTextLine *self,
    int *cursorPos,
    QTextLine::Edge edge) {
  return self->cursorToX(cursorPos, edge);
}

//  qreal QTextLine::cursorToX(int cursorPos, Edge edge) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextLine9cursorToXEiNS_4EdgeE(
    const QTextLine *self,
    int cursorPos,
    QTextLine::Edge edge) {
  return self->cursorToX(cursorPos, edge);
}

//  int QTextLine::xToCursor(qreal x, CursorPosition a1) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextLine9xToCursorEdNS_14CursorPositionE(
    const QTextLine *self,
    qreal x,
    QTextLine::CursorPosition a1) {
  return self->xToCursor(x, a1);
}

//  void QTextLine::setLineWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextLine12setLineWidthEd(QTextLine *self, qreal width) {
  self->setLineWidth(width);
}

//  void QTextLine::setNumColumns(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextLine13setNumColumnsEi(QTextLine *self, int columns) {
  self->setNumColumns(columns);
}

//  void QTextLine::setNumColumns(int columns, qreal alignmentWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextLine13setNumColumnsEid(
    QTextLine *self,
    int columns,
    qreal alignmentWidth) {
  self->setNumColumns(columns, alignmentWidth);
}

//  void QTextLine::setPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextLine11setPositionERK7QPointF(
    QTextLine *self,
    const QPointF *pos) {
  self->setPosition(*pos);
}

//  QPointF QTextLine::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QTextLine8positionEv(const QTextLine *self) {
  return new QPointF(self->position());
}

//  int QTextLine::textStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextLine9textStartEv(const QTextLine *self) {
  return self->textStart();
}

//  int QTextLine::textLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextLine10textLengthEv(const QTextLine *self) {
  return self->textLength();
}

//  int QTextLine::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextLine10lineNumberEv(const QTextLine *self) {
  return self->lineNumber();
}

//  void QTextLine::draw(QPainter *painter, const QPointF &position) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QTextLine4drawEP8QPainterRK7QPointF(
    const QTextLine *self,
    QPainter *painter,
    const QPointF *position) {
  self->draw(painter, *position);
}

//  QTextLine::~QTextLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextLineD1Ev(QTextLine *self) {
  delete self;
}
