//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtGui/qbrush.h>

//  QTextFrameFormat::QTextFrameFormat()
extern "C" Q_DECL_EXPORT
QTextFrameFormat *ritual_ZN16QTextFrameFormatC1Ev() {
  return new QTextFrameFormat();
}

//  bool QTextFrameFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextFrameFormat7isValidEv(const QTextFrameFormat *self) {
  return self->isValid();
}

//  void QTextFrameFormat::setPosition(Position f)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat11setPositionENS_8PositionE(
    QTextFrameFormat *self,
    QTextFrameFormat::Position f) {
  self->setPosition(f);
}

//  Position QTextFrameFormat::position() const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::Position ritual_ZNK16QTextFrameFormat8positionEv(
    const QTextFrameFormat *self) {
  return self->position();
}

//  void QTextFrameFormat::setBorder(qreal border)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat9setBorderEd(
    QTextFrameFormat *self,
    qreal border) {
  self->setBorder(border);
}

//  qreal QTextFrameFormat::border() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat6borderEv(const QTextFrameFormat *self) {
  return self->border();
}

//  void QTextFrameFormat::setBorderBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat14setBorderBrushERK6QBrush(
    QTextFrameFormat *self,
    const QBrush *brush) {
  self->setBorderBrush(*brush);
}

//  QBrush QTextFrameFormat::borderBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK16QTextFrameFormat11borderBrushEv(
    const QTextFrameFormat *self) {
  return new QBrush(self->borderBrush());
}

//  void QTextFrameFormat::setBorderStyle(BorderStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat14setBorderStyleENS_11BorderStyleE(
    QTextFrameFormat *self,
    QTextFrameFormat::BorderStyle style) {
  self->setBorderStyle(style);
}

//  BorderStyle QTextFrameFormat::borderStyle() const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::BorderStyle ritual_ZNK16QTextFrameFormat11borderStyleEv(
    const QTextFrameFormat *self) {
  return self->borderStyle();
}

//  void QTextFrameFormat::setMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat9setMarginEd(
    QTextFrameFormat *self,
    qreal margin) {
  self->setMargin(margin);
}

//  qreal QTextFrameFormat::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat6marginEv(const QTextFrameFormat *self) {
  return self->margin();
}

//  void QTextFrameFormat::setTopMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat12setTopMarginEd(
    QTextFrameFormat *self,
    qreal margin) {
  self->setTopMargin(margin);
}

//  qreal QTextFrameFormat::topMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat9topMarginEv(
    const QTextFrameFormat *self) {
  return self->topMargin();
}

//  void QTextFrameFormat::setBottomMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat15setBottomMarginEd(
    QTextFrameFormat *self,
    qreal margin) {
  self->setBottomMargin(margin);
}

//  qreal QTextFrameFormat::bottomMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat12bottomMarginEv(
    const QTextFrameFormat *self) {
  return self->bottomMargin();
}

//  void QTextFrameFormat::setLeftMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat13setLeftMarginEd(
    QTextFrameFormat *self,
    qreal margin) {
  self->setLeftMargin(margin);
}

//  qreal QTextFrameFormat::leftMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat10leftMarginEv(
    const QTextFrameFormat *self) {
  return self->leftMargin();
}

//  void QTextFrameFormat::setRightMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat14setRightMarginEd(
    QTextFrameFormat *self,
    qreal margin) {
  self->setRightMargin(margin);
}

//  qreal QTextFrameFormat::rightMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat11rightMarginEv(
    const QTextFrameFormat *self) {
  return self->rightMargin();
}

//  void QTextFrameFormat::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat10setPaddingEd(
    QTextFrameFormat *self,
    qreal padding) {
  self->setPadding(padding);
}

//  qreal QTextFrameFormat::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextFrameFormat7paddingEv(const QTextFrameFormat *self) {
  return self->padding();
}

//  void QTextFrameFormat::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat8setWidthEd(
    QTextFrameFormat *self,
    qreal width) {
  self->setWidth(width);
}

//  void QTextFrameFormat::setWidth(const QTextLength &length)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat8setWidthERK11QTextLength(
    QTextFrameFormat *self,
    const QTextLength *length) {
  self->setWidth(*length);
}

//  QTextLength QTextFrameFormat::width() const
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZNK16QTextFrameFormat5widthEv(
    const QTextFrameFormat *self) {
  return new QTextLength(self->width());
}

//  void QTextFrameFormat::setHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat9setHeightEd(
    QTextFrameFormat *self,
    qreal height) {
  self->setHeight(height);
}

//  void QTextFrameFormat::setHeight(const QTextLength &height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat9setHeightERK11QTextLength(
    QTextFrameFormat *self,
    const QTextLength *height) {
  self->setHeight(*height);
}

//  QTextLength QTextFrameFormat::height() const
extern "C" Q_DECL_EXPORT
QTextLength *ritual_ZNK16QTextFrameFormat6heightEv(
    const QTextFrameFormat *self) {
  return new QTextLength(self->height());
}

//  void QTextFrameFormat::setPageBreakPolicy(PageBreakFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormat18setPageBreakPolicyE6QFlagsIN11QTextFormat13PageBreakFlagEE(
    QTextFrameFormat *self,
    int flags) {
  self->setPageBreakPolicy(
      QFlags<QTextFormat::PageBreakFlag>::fromInt(flags));
}

//  PageBreakFlags QTextFrameFormat::pageBreakPolicy() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextFrameFormat15pageBreakPolicyEv(
    const QTextFrameFormat *self) {
  return static_cast<int>(self->pageBreakPolicy().toInt());
}

//  QTextFrameFormat::QTextFrameFormat(const QTextFormat &fmt)
extern "C" Q_DECL_EXPORT
QTextFrameFormat *ritual_ZN16QTextFrameFormatC1ERK11QTextFormat(
    const QTextFormat *fmt) {
  return new QTextFrameFormat(*fmt);
}

//  QTextFrameFormat::~QTextFrameFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextFrameFormatD1Ev(QTextFrameFormat *self) {
  delete self;
}
