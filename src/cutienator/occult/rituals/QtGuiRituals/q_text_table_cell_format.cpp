//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtGui/qbrush.h>

//  QTextTableCellFormat::QTextTableCellFormat()
extern "C" Q_DECL_EXPORT
QTextTableCellFormat *ritual_ZN20QTextTableCellFormatC1Ev() {
  return new QTextTableCellFormat();
}

//  bool QTextTableCellFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextTableCellFormat7isValidEv(
    const QTextTableCellFormat *self) {
  return self->isValid();
}

//  void QTextTableCellFormat::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat13setTopPaddingEd(
    QTextTableCellFormat *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  qreal QTextTableCellFormat::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat10topPaddingEv(
    const QTextTableCellFormat *self) {
  return self->topPadding();
}

//  void QTextTableCellFormat::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat16setBottomPaddingEd(
    QTextTableCellFormat *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  qreal QTextTableCellFormat::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat13bottomPaddingEv(
    const QTextTableCellFormat *self) {
  return self->bottomPadding();
}

//  void QTextTableCellFormat::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat14setLeftPaddingEd(
    QTextTableCellFormat *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  qreal QTextTableCellFormat::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat11leftPaddingEv(
    const QTextTableCellFormat *self) {
  return self->leftPadding();
}

//  void QTextTableCellFormat::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat15setRightPaddingEd(
    QTextTableCellFormat *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  qreal QTextTableCellFormat::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat12rightPaddingEv(
    const QTextTableCellFormat *self) {
  return self->rightPadding();
}

//  void QTextTableCellFormat::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat10setPaddingEd(
    QTextTableCellFormat *self,
    qreal padding) {
  self->setPadding(padding);
}

//  void QTextTableCellFormat::setTopBorder(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat12setTopBorderEd(
    QTextTableCellFormat *self,
    qreal width) {
  self->setTopBorder(width);
}

//  qreal QTextTableCellFormat::topBorder() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat9topBorderEv(
    const QTextTableCellFormat *self) {
  return self->topBorder();
}

//  void QTextTableCellFormat::setBottomBorder(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat15setBottomBorderEd(
    QTextTableCellFormat *self,
    qreal width) {
  self->setBottomBorder(width);
}

//  qreal QTextTableCellFormat::bottomBorder() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat12bottomBorderEv(
    const QTextTableCellFormat *self) {
  return self->bottomBorder();
}

//  void QTextTableCellFormat::setLeftBorder(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat13setLeftBorderEd(
    QTextTableCellFormat *self,
    qreal width) {
  self->setLeftBorder(width);
}

//  qreal QTextTableCellFormat::leftBorder() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat10leftBorderEv(
    const QTextTableCellFormat *self) {
  return self->leftBorder();
}

//  void QTextTableCellFormat::setRightBorder(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat14setRightBorderEd(
    QTextTableCellFormat *self,
    qreal width) {
  self->setRightBorder(width);
}

//  qreal QTextTableCellFormat::rightBorder() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QTextTableCellFormat11rightBorderEv(
    const QTextTableCellFormat *self) {
  return self->rightBorder();
}

//  void QTextTableCellFormat::setBorder(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat9setBorderEd(
    QTextTableCellFormat *self,
    qreal width) {
  self->setBorder(width);
}

//  void
//      QTextTableCellFormat::setTopBorderStyle(QTextFrameFormat::BorderStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat17setTopBorderStyleEN16QTextFrameFormat11BorderStyleE(
    QTextTableCellFormat *self,
    QTextFrameFormat::BorderStyle style) {
  self->setTopBorderStyle(style);
}

//  QTextFrameFormat::BorderStyle QTextTableCellFormat::topBorderStyle()
//      const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::BorderStyle ritual_ZNK20QTextTableCellFormat14topBorderStyleEv(
    const QTextTableCellFormat *self) {
  return self->topBorderStyle();
}

//  void
//      QTextTableCellFormat::setBottomBorderStyle(QTextFrameFormat::BorderSt
//      yle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat20setBottomBorderStyleEN16QTextFrameFormat11BorderStyleE(
    QTextTableCellFormat *self,
    QTextFrameFormat::BorderStyle style) {
  self->setBottomBorderStyle(style);
}

//  QTextFrameFormat::BorderStyle QTextTableCellFormat::bottomBorderStyle()
//      const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::BorderStyle ritual_ZNK20QTextTableCellFormat17bottomBorderStyleEv(
    const QTextTableCellFormat *self) {
  return self->bottomBorderStyle();
}

//  void
//      QTextTableCellFormat::setLeftBorderStyle(QTextFrameFormat::BorderStyl
//      e style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat18setLeftBorderStyleEN16QTextFrameFormat11BorderStyleE(
    QTextTableCellFormat *self,
    QTextFrameFormat::BorderStyle style) {
  self->setLeftBorderStyle(style);
}

//  QTextFrameFormat::BorderStyle QTextTableCellFormat::leftBorderStyle()
//      const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::BorderStyle ritual_ZNK20QTextTableCellFormat15leftBorderStyleEv(
    const QTextTableCellFormat *self) {
  return self->leftBorderStyle();
}

//  void
//      QTextTableCellFormat::setRightBorderStyle(QTextFrameFormat::BorderSty
//      le style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat19setRightBorderStyleEN16QTextFrameFormat11BorderStyleE(
    QTextTableCellFormat *self,
    QTextFrameFormat::BorderStyle style) {
  self->setRightBorderStyle(style);
}

//  QTextFrameFormat::BorderStyle QTextTableCellFormat::rightBorderStyle()
//      const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::BorderStyle ritual_ZNK20QTextTableCellFormat16rightBorderStyleEv(
    const QTextTableCellFormat *self) {
  return self->rightBorderStyle();
}

//  void QTextTableCellFormat::setBorderStyle(QTextFrameFormat::BorderStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat14setBorderStyleEN16QTextFrameFormat11BorderStyleE(
    QTextTableCellFormat *self,
    QTextFrameFormat::BorderStyle style) {
  self->setBorderStyle(style);
}

//  void QTextTableCellFormat::setTopBorderBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat17setTopBorderBrushERK6QBrush(
    QTextTableCellFormat *self,
    const QBrush *brush) {
  self->setTopBorderBrush(*brush);
}

//  QBrush QTextTableCellFormat::topBorderBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK20QTextTableCellFormat14topBorderBrushEv(
    const QTextTableCellFormat *self) {
  return new QBrush(self->topBorderBrush());
}

//  void QTextTableCellFormat::setBottomBorderBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat20setBottomBorderBrushERK6QBrush(
    QTextTableCellFormat *self,
    const QBrush *brush) {
  self->setBottomBorderBrush(*brush);
}

//  QBrush QTextTableCellFormat::bottomBorderBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK20QTextTableCellFormat17bottomBorderBrushEv(
    const QTextTableCellFormat *self) {
  return new QBrush(self->bottomBorderBrush());
}

//  void QTextTableCellFormat::setLeftBorderBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat18setLeftBorderBrushERK6QBrush(
    QTextTableCellFormat *self,
    const QBrush *brush) {
  self->setLeftBorderBrush(*brush);
}

//  QBrush QTextTableCellFormat::leftBorderBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK20QTextTableCellFormat15leftBorderBrushEv(
    const QTextTableCellFormat *self) {
  return new QBrush(self->leftBorderBrush());
}

//  void QTextTableCellFormat::setRightBorderBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat19setRightBorderBrushERK6QBrush(
    QTextTableCellFormat *self,
    const QBrush *brush) {
  self->setRightBorderBrush(*brush);
}

//  QBrush QTextTableCellFormat::rightBorderBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK20QTextTableCellFormat16rightBorderBrushEv(
    const QTextTableCellFormat *self) {
  return new QBrush(self->rightBorderBrush());
}

//  void QTextTableCellFormat::setBorderBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormat14setBorderBrushERK6QBrush(
    QTextTableCellFormat *self,
    const QBrush *brush) {
  self->setBorderBrush(*brush);
}

//  QTextTableCellFormat::~QTextTableCellFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextTableCellFormatD1Ev(QTextTableCellFormat *self) {
  delete self;
}
