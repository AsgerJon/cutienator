//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsgridlayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsgridlayout.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QGraphicsGridLayout::QGraphicsGridLayout(QGraphicsLayoutItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsGridLayout *ritual_ZN19QGraphicsGridLayoutC1EP19QGraphicsLayoutItem(
    QGraphicsLayoutItem *parent) {
  return new QGraphicsGridLayout(parent);
}

//  QGraphicsGridLayout::~QGraphicsGridLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayoutD1Ev(QGraphicsGridLayout *self) {
  delete self;
}

//  void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item, int row, int
//      column, int rowSpan, int columnSpan, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout7addItemEP19QGraphicsLayoutItemiiii6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    int alignment) {
  self->addItem(
      item,
      row,
      column,
      rowSpan,
      columnSpan,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item, int row, int
//      column, Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout7addItemEP19QGraphicsLayoutItemii6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item,
    int row,
    int column,
    int alignment) {
  self->addItem(
      item,
      row,
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QGraphicsGridLayout::setHorizontalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout20setHorizontalSpacingEd(
    QGraphicsGridLayout *self,
    qreal spacing) {
  self->setHorizontalSpacing(spacing);
}

//  qreal QGraphicsGridLayout::horizontalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout17horizontalSpacingEv(
    const QGraphicsGridLayout *self) {
  return self->horizontalSpacing();
}

//  void QGraphicsGridLayout::setVerticalSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout18setVerticalSpacingEd(
    QGraphicsGridLayout *self,
    qreal spacing) {
  self->setVerticalSpacing(spacing);
}

//  qreal QGraphicsGridLayout::verticalSpacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout15verticalSpacingEv(
    const QGraphicsGridLayout *self) {
  return self->verticalSpacing();
}

//  void QGraphicsGridLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout10setSpacingEd(
    QGraphicsGridLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  void QGraphicsGridLayout::setRowSpacing(int row, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout13setRowSpacingEid(
    QGraphicsGridLayout *self,
    int row,
    qreal spacing) {
  self->setRowSpacing(row, spacing);
}

//  qreal QGraphicsGridLayout::rowSpacing(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout10rowSpacingEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowSpacing(row);
}

//  void QGraphicsGridLayout::setColumnSpacing(int column, qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout16setColumnSpacingEid(
    QGraphicsGridLayout *self,
    int column,
    qreal spacing) {
  self->setColumnSpacing(column, spacing);
}

//  qreal QGraphicsGridLayout::columnSpacing(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout13columnSpacingEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnSpacing(column);
}

//  void QGraphicsGridLayout::setRowStretchFactor(int row, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setRowStretchFactorEii(
    QGraphicsGridLayout *self,
    int row,
    int stretch) {
  self->setRowStretchFactor(row, stretch);
}

//  int QGraphicsGridLayout::rowStretchFactor(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout16rowStretchFactorEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowStretchFactor(row);
}

//  void QGraphicsGridLayout::setColumnStretchFactor(int column, int stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout22setColumnStretchFactorEii(
    QGraphicsGridLayout *self,
    int column,
    int stretch) {
  self->setColumnStretchFactor(column, stretch);
}

//  int QGraphicsGridLayout::columnStretchFactor(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout19columnStretchFactorEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnStretchFactor(column);
}

//  void QGraphicsGridLayout::setRowMinimumHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setRowMinimumHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowMinimumHeight(row, height);
}

//  qreal QGraphicsGridLayout::rowMinimumHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout16rowMinimumHeightEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowMinimumHeight(row);
}

//  void QGraphicsGridLayout::setRowPreferredHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout21setRowPreferredHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowPreferredHeight(row, height);
}

//  qreal QGraphicsGridLayout::rowPreferredHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout18rowPreferredHeightEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowPreferredHeight(row);
}

//  void QGraphicsGridLayout::setRowMaximumHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setRowMaximumHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowMaximumHeight(row, height);
}

//  qreal QGraphicsGridLayout::rowMaximumHeight(int row) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout16rowMaximumHeightEi(
    const QGraphicsGridLayout *self,
    int row) {
  return self->rowMaximumHeight(row);
}

//  void QGraphicsGridLayout::setRowFixedHeight(int row, qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout17setRowFixedHeightEid(
    QGraphicsGridLayout *self,
    int row,
    qreal height) {
  self->setRowFixedHeight(row, height);
}

//  void QGraphicsGridLayout::setColumnMinimumWidth(int column, qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout21setColumnMinimumWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnMinimumWidth(column, width);
}

//  qreal QGraphicsGridLayout::columnMinimumWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout18columnMinimumWidthEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnMinimumWidth(column);
}

//  void QGraphicsGridLayout::setColumnPreferredWidth(int column, qreal
//      width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout23setColumnPreferredWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnPreferredWidth(column, width);
}

//  qreal QGraphicsGridLayout::columnPreferredWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout20columnPreferredWidthEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnPreferredWidth(column);
}

//  void QGraphicsGridLayout::setColumnMaximumWidth(int column, qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout21setColumnMaximumWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnMaximumWidth(column, width);
}

//  qreal QGraphicsGridLayout::columnMaximumWidth(int column) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsGridLayout18columnMaximumWidthEi(
    const QGraphicsGridLayout *self,
    int column) {
  return self->columnMaximumWidth(column);
}

//  void QGraphicsGridLayout::setColumnFixedWidth(int column, qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout19setColumnFixedWidthEid(
    QGraphicsGridLayout *self,
    int column,
    qreal width) {
  self->setColumnFixedWidth(column, width);
}

//  void QGraphicsGridLayout::setRowAlignment(int row, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout15setRowAlignmentEi6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    int row,
    int alignment) {
  self->setRowAlignment(row, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayout::rowAlignment(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout12rowAlignmentEi(
    const QGraphicsGridLayout *self,
    int row) {
  return static_cast<int>(self->rowAlignment(row).toInt());
}

//  void QGraphicsGridLayout::setColumnAlignment(int column, Qt::Alignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout18setColumnAlignmentEi6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    int column,
    int alignment) {
  self->setColumnAlignment(
      column,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayout::columnAlignment(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout15columnAlignmentEi(
    const QGraphicsGridLayout *self,
    int column) {
  return static_cast<int>(self->columnAlignment(column).toInt());
}

//  void QGraphicsGridLayout::setAlignment(QGraphicsLayoutItem *item,
//      Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout12setAlignmentEP19QGraphicsLayoutItem6QFlagsIN2Qt13AlignmentFlagEE(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item,
    int alignment) {
  self->setAlignment(item, QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QGraphicsGridLayout::alignment(QGraphicsLayoutItem *item)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout9alignmentEP19QGraphicsLayoutItem(
    const QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item) {
  return static_cast<int>(self->alignment(item).toInt());
}

//  int QGraphicsGridLayout::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout8rowCountEv(
    const QGraphicsGridLayout *self) {
  return self->rowCount();
}

//  int QGraphicsGridLayout::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout11columnCountEv(
    const QGraphicsGridLayout *self) {
  return self->columnCount();
}

//  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int row, int column)
//      const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK19QGraphicsGridLayout6itemAtEii(
    const QGraphicsGridLayout *self,
    int row,
    int column) {
  return self->itemAt(row, column);
}

//  int QGraphicsGridLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsGridLayout5countEv(
    const QGraphicsGridLayout *self) {
  return self->count();
}

//  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK19QGraphicsGridLayout6itemAtEi(
    const QGraphicsGridLayout *self,
    int index) {
  return self->itemAt(index);
}

//  void QGraphicsGridLayout::removeAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout8removeAtEi(
    QGraphicsGridLayout *self,
    int index) {
  self->removeAt(index);
}

//  void QGraphicsGridLayout::removeItem(QGraphicsLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout10removeItemEP19QGraphicsLayoutItem(
    QGraphicsGridLayout *self,
    QGraphicsLayoutItem *item) {
  self->removeItem(item);
}

//  void QGraphicsGridLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout10invalidateEv(
    QGraphicsGridLayout *self) {
  self->invalidate();
}

//  void QGraphicsGridLayout::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsGridLayout11setGeometryERK6QRectF(
    QGraphicsGridLayout *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QGraphicsGridLayout8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsGridLayout *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}
