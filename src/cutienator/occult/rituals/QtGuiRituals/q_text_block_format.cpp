//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtCore/QList>
#include <QtGui/QTextOption>

//  QTextBlockFormat::QTextBlockFormat()
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZN16QTextBlockFormatC1Ev() {
  return new QTextBlockFormat();
}

//  bool QTextBlockFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextBlockFormat7isValidEv(const QTextBlockFormat *self) {
  return self->isValid();
}

//  void QTextBlockFormat::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTextBlockFormat *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QTextBlockFormat::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextBlockFormat9alignmentEv(const QTextBlockFormat *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QTextBlockFormat::setTopMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat12setTopMarginEd(
    QTextBlockFormat *self,
    qreal margin) {
  self->setTopMargin(margin);
}

//  qreal QTextBlockFormat::topMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat9topMarginEv(
    const QTextBlockFormat *self) {
  return self->topMargin();
}

//  void QTextBlockFormat::setBottomMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat15setBottomMarginEd(
    QTextBlockFormat *self,
    qreal margin) {
  self->setBottomMargin(margin);
}

//  qreal QTextBlockFormat::bottomMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat12bottomMarginEv(
    const QTextBlockFormat *self) {
  return self->bottomMargin();
}

//  void QTextBlockFormat::setLeftMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat13setLeftMarginEd(
    QTextBlockFormat *self,
    qreal margin) {
  self->setLeftMargin(margin);
}

//  qreal QTextBlockFormat::leftMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat10leftMarginEv(
    const QTextBlockFormat *self) {
  return self->leftMargin();
}

//  void QTextBlockFormat::setRightMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat14setRightMarginEd(
    QTextBlockFormat *self,
    qreal margin) {
  self->setRightMargin(margin);
}

//  qreal QTextBlockFormat::rightMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat11rightMarginEv(
    const QTextBlockFormat *self) {
  return self->rightMargin();
}

//  void QTextBlockFormat::setTextIndent(qreal aindent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat13setTextIndentEd(
    QTextBlockFormat *self,
    qreal aindent) {
  self->setTextIndent(aindent);
}

//  qreal QTextBlockFormat::textIndent() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat10textIndentEv(
    const QTextBlockFormat *self) {
  return self->textIndent();
}

//  void QTextBlockFormat::setIndent(int indent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat9setIndentEi(
    QTextBlockFormat *self,
    int indent) {
  self->setIndent(indent);
}

//  int QTextBlockFormat::indent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextBlockFormat6indentEv(const QTextBlockFormat *self) {
  return self->indent();
}

//  void QTextBlockFormat::setHeadingLevel(int alevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat15setHeadingLevelEi(
    QTextBlockFormat *self,
    int alevel) {
  self->setHeadingLevel(alevel);
}

//  int QTextBlockFormat::headingLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextBlockFormat12headingLevelEv(
    const QTextBlockFormat *self) {
  return self->headingLevel();
}

//  void QTextBlockFormat::setLineHeight(qreal height, int heightType)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat13setLineHeightEdi(
    QTextBlockFormat *self,
    qreal height,
    int heightType) {
  self->setLineHeight(height, heightType);
}

//  qreal QTextBlockFormat::lineHeight(qreal scriptLineHeight, qreal scaling)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat10lineHeightEdd(
    const QTextBlockFormat *self,
    qreal scriptLineHeight,
    qreal scaling) {
  return self->lineHeight(scriptLineHeight, scaling);
}

//  qreal QTextBlockFormat::lineHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextBlockFormat10lineHeightEv(
    const QTextBlockFormat *self) {
  return self->lineHeight();
}

//  int QTextBlockFormat::lineHeightType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextBlockFormat14lineHeightTypeEv(
    const QTextBlockFormat *self) {
  return self->lineHeightType();
}

//  void QTextBlockFormat::setNonBreakableLines(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat20setNonBreakableLinesEb(
    QTextBlockFormat *self,
    bool b) {
  self->setNonBreakableLines(b);
}

//  bool QTextBlockFormat::nonBreakableLines() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextBlockFormat17nonBreakableLinesEv(
    const QTextBlockFormat *self) {
  return self->nonBreakableLines();
}

//  void QTextBlockFormat::setPageBreakPolicy(PageBreakFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat18setPageBreakPolicyE6QFlagsIN11QTextFormat13PageBreakFlagEE(
    QTextBlockFormat *self,
    int flags) {
  self->setPageBreakPolicy(
      QFlags<QTextFormat::PageBreakFlag>::fromInt(flags));
}

//  PageBreakFlags QTextBlockFormat::pageBreakPolicy() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextBlockFormat15pageBreakPolicyEv(
    const QTextBlockFormat *self) {
  return static_cast<int>(self->pageBreakPolicy().toInt());
}

//  void QTextBlockFormat::setTabPositions(const QList<QTextOption::Tab>
//      &tabs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat15setTabPositionsERK5QListIN11QTextOption3TabEE(
    QTextBlockFormat *self,
    const QList<QTextOption::Tab> *tabs) {
  self->setTabPositions(*tabs);
}

//  QList<QTextOption::Tab> QTextBlockFormat::tabPositions() const
extern "C" Q_DECL_EXPORT
QList<QTextOption::Tab> *ritual_ZNK16QTextBlockFormat12tabPositionsEv(
    const QTextBlockFormat *self) {
  return new QList<QTextOption::Tab>(self->tabPositions());
}

//  void QTextBlockFormat::setMarker(MarkerType marker)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormat9setMarkerENS_10MarkerTypeE(
    QTextBlockFormat *self,
    QTextBlockFormat::MarkerType marker) {
  self->setMarker(marker);
}

//  MarkerType QTextBlockFormat::marker() const
extern "C" Q_DECL_EXPORT
QTextBlockFormat::MarkerType ritual_ZNK16QTextBlockFormat6markerEv(
    const QTextBlockFormat *self) {
  return self->marker();
}

//  QTextBlockFormat::QTextBlockFormat(const QTextFormat &fmt)
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZN16QTextBlockFormatC1ERK11QTextFormat(
    const QTextFormat *fmt) {
  return new QTextBlockFormat(*fmt);
}

//  QDataStream &operator<<(QDataStream &a0, const QTextBlockFormat &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK16QTextBlockFormat(
    QDataStream *a0,
    const QTextBlockFormat *a1) {
  return &(operator<<(*a0, *a1));
}

//  QDataStream &operator>>(QDataStream &a0, QTextBlockFormat &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR16QTextBlockFormat(
    QDataStream *a0,
    QTextBlockFormat *a1) {
  return &(operator>>(*a0, *a1));
}

//  QTextBlockFormat::~QTextBlockFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextBlockFormatD1Ev(QTextBlockFormat *self) {
  delete self;
}

//  a QList<QTextOption::Tab> a ritual of QTextBlockFormat gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextBlockFormat__QList_QTextOption_Tab(
    QList<QTextOption::Tab> *self) {
  delete self;
}
