//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtCore/qlist.h>

//  QTextTableFormat::QTextTableFormat()
extern "C" Q_DECL_EXPORT
QTextTableFormat *ritual_ZN16QTextTableFormatC1Ev() {
  return new QTextTableFormat();
}

//  bool QTextTableFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextTableFormat7isValidEv(const QTextTableFormat *self) {
  return self->isValid();
}

//  int QTextTableFormat::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextTableFormat7columnsEv(const QTextTableFormat *self) {
  return self->columns();
}

//  void QTextTableFormat::setColumns(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat10setColumnsEi(
    QTextTableFormat *self,
    int columns) {
  self->setColumns(columns);
}

//  void QTextTableFormat::setColumnWidthConstraints(const QList<QTextLength>
//      &constraints)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat25setColumnWidthConstraintsERK5QListI11QTextLengthE(
    QTextTableFormat *self,
    const QList<QTextLength> *constraints) {
  self->setColumnWidthConstraints(*constraints);
}

//  QList<QTextLength> QTextTableFormat::columnWidthConstraints() const
extern "C" Q_DECL_EXPORT
QList<QTextLength> *ritual_ZNK16QTextTableFormat22columnWidthConstraintsEv(
    const QTextTableFormat *self) {
  return new QList<QTextLength>(self->columnWidthConstraints());
}

//  void QTextTableFormat::clearColumnWidthConstraints()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat27clearColumnWidthConstraintsEv(
    QTextTableFormat *self) {
  self->clearColumnWidthConstraints();
}

//  qreal QTextTableFormat::cellSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextTableFormat11cellSpacingEv(
    const QTextTableFormat *self) {
  return self->cellSpacing();
}

//  void QTextTableFormat::setCellSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat14setCellSpacingEd(
    QTextTableFormat *self,
    qreal spacing) {
  self->setCellSpacing(spacing);
}

//  qreal QTextTableFormat::cellPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QTextTableFormat11cellPaddingEv(
    const QTextTableFormat *self) {
  return self->cellPadding();
}

//  void QTextTableFormat::setCellPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat14setCellPaddingEd(
    QTextTableFormat *self,
    qreal padding) {
  self->setCellPadding(padding);
}

//  void QTextTableFormat::setAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTextTableFormat *self,
    int alignment) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QTextTableFormat::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextTableFormat9alignmentEv(const QTextTableFormat *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QTextTableFormat::setHeaderRowCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat17setHeaderRowCountEi(
    QTextTableFormat *self,
    int count) {
  self->setHeaderRowCount(count);
}

//  int QTextTableFormat::headerRowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextTableFormat14headerRowCountEv(
    const QTextTableFormat *self) {
  return self->headerRowCount();
}

//  void QTextTableFormat::setBorderCollapse(bool borderCollapse)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormat17setBorderCollapseEb(
    QTextTableFormat *self,
    bool borderCollapse) {
  self->setBorderCollapse(borderCollapse);
}

//  bool QTextTableFormat::borderCollapse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTextTableFormat14borderCollapseEv(
    const QTextTableFormat *self) {
  return self->borderCollapse();
}

//  QTextTableFormat::~QTextTableFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextTableFormatD1Ev(QTextTableFormat *self) {
  delete self;
}
