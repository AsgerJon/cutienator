//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>

//  QGridLayoutEngine::QGridLayoutEngine(Qt::Alignment defaultAlignment, bool
//      snapToPixelGrid)
extern "C" Q_DECL_EXPORT
QGridLayoutEngine *ritual_ZN17QGridLayoutEngineC1E6QFlagsIN2Qt13AlignmentFlagEEb(
    int defaultAlignment,
    bool snapToPixelGrid) {
  return new QGridLayoutEngine(
      QFlags<Qt::AlignmentFlag>::fromInt(defaultAlignment),
      snapToPixelGrid);
}

//  QGridLayoutEngine::~QGridLayoutEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngineD1Ev(QGridLayoutEngine *self) {
  delete self;
}

//  int QGridLayoutEngine::rowCount(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine8rowCountEN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    Qt::Orientation orientation) {
  return self->rowCount(orientation);
}

//  int QGridLayoutEngine::columnCount(Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine11columnCountEN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    Qt::Orientation orientation) {
  return self->columnCount(orientation);
}

//  int QGridLayoutEngine::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine8rowCountEv(const QGridLayoutEngine *self) {
  return self->rowCount();
}

//  int QGridLayoutEngine::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine11columnCountEv(
    const QGridLayoutEngine *self) {
  return self->columnCount();
}

//  int QGridLayoutEngine::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine9itemCountEv(
    const QGridLayoutEngine *self) {
  return self->itemCount();
}

//  QGridLayoutItem *QGridLayoutEngine::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QGridLayoutItem *ritual_ZNK17QGridLayoutEngine6itemAtEi(
    const QGridLayoutEngine *self,
    int index) {
  return self->itemAt(index);
}

//  int QGridLayoutEngine::effectiveFirstRow(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine17effectiveFirstRowEN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    Qt::Orientation orientation) {
  return self->effectiveFirstRow(orientation);
}

//  int QGridLayoutEngine::effectiveLastRow(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine16effectiveLastRowEN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    Qt::Orientation orientation) {
  return self->effectiveLastRow(orientation);
}

//  void QGridLayoutEngine::setSpacing(qreal spacing, Qt::Orientations
//      orientations)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine10setSpacingEd6QFlagsIN2Qt11OrientationEE(
    QGridLayoutEngine *self,
    qreal spacing,
    int orientations) {
  self->setSpacing(spacing, QFlags<Qt::Orientation>::fromInt(orientations));
}

//  qreal QGridLayoutEngine::spacing(Qt::Orientation orientation, const
//      QAbstractLayoutStyleInfo *styleInfo) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGridLayoutEngine7spacingEN2Qt11OrientationEPK24QAbstractLayoutStyleInfo(
    const QGridLayoutEngine *self,
    Qt::Orientation orientation,
    const QAbstractLayoutStyleInfo *styleInfo) {
  return self->spacing(orientation, styleInfo);
}

//  void QGridLayoutEngine::setRowSpacing(int row, qreal spacing,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine13setRowSpacingEidN2Qt11OrientationE(
    QGridLayoutEngine *self,
    int row,
    qreal spacing,
    Qt::Orientation orientation) {
  self->setRowSpacing(row, spacing, orientation);
}

//  qreal QGridLayoutEngine::rowSpacing(int row, Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGridLayoutEngine10rowSpacingEiN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    int row,
    Qt::Orientation orientation) {
  return self->rowSpacing(row, orientation);
}

//  void QGridLayoutEngine::setRowStretchFactor(int row, int stretch,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine19setRowStretchFactorEiiN2Qt11OrientationE(
    QGridLayoutEngine *self,
    int row,
    int stretch,
    Qt::Orientation orientation) {
  self->setRowStretchFactor(row, stretch, orientation);
}

//  int QGridLayoutEngine::rowStretchFactor(int row, Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine16rowStretchFactorEiN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    int row,
    Qt::Orientation orientation) {
  return self->rowStretchFactor(row, orientation);
}

//  void QGridLayoutEngine::setRowSizeHint(Qt::SizeHint which, int row, qreal
//      size, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine14setRowSizeHintEN2Qt8SizeHintEidNS0_11OrientationE(
    QGridLayoutEngine *self,
    Qt::SizeHint which,
    int row,
    qreal size,
    Qt::Orientation orientation) {
  self->setRowSizeHint(which, row, size, orientation);
}

//  qreal QGridLayoutEngine::rowSizeHint(Qt::SizeHint which, int row,
//      Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGridLayoutEngine11rowSizeHintEN2Qt8SizeHintEiNS0_11OrientationE(
    const QGridLayoutEngine *self,
    Qt::SizeHint which,
    int row,
    Qt::Orientation orientation) {
  return self->rowSizeHint(which, row, orientation);
}

//  bool QGridLayoutEngine::uniformCellWidths() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGridLayoutEngine17uniformCellWidthsEv(
    const QGridLayoutEngine *self) {
  return self->uniformCellWidths();
}

//  void QGridLayoutEngine::setUniformCellWidths(bool uniformCellWidths)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine20setUniformCellWidthsEb(
    QGridLayoutEngine *self,
    bool uniformCellWidths) {
  self->setUniformCellWidths(uniformCellWidths);
}

//  bool QGridLayoutEngine::uniformCellHeights() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGridLayoutEngine18uniformCellHeightsEv(
    const QGridLayoutEngine *self) {
  return self->uniformCellHeights();
}

//  void QGridLayoutEngine::setUniformCellHeights(bool uniformCellHeights)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine21setUniformCellHeightsEb(
    QGridLayoutEngine *self,
    bool uniformCellHeights) {
  self->setUniformCellHeights(uniformCellHeights);
}

//  void QGridLayoutEngine::setRowAlignment(int row, Qt::Alignment alignment,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine15setRowAlignmentEi6QFlagsIN2Qt13AlignmentFlagEENS1_11OrientationE(
    QGridLayoutEngine *self,
    int row,
    int alignment,
    Qt::Orientation orientation) {
  self->setRowAlignment(
      row,
      QFlags<Qt::AlignmentFlag>::fromInt(alignment),
      orientation);
}

//  Qt::Alignment QGridLayoutEngine::rowAlignment(int row, Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine12rowAlignmentEiN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    int row,
    Qt::Orientation orientation) {
  return static_cast<int>(self->rowAlignment(row, orientation).toInt());
}

//  Qt::Alignment QGridLayoutEngine::effectiveAlignment(const QGridLayoutItem
//      *layoutItem) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine18effectiveAlignmentEPK15QGridLayoutItem(
    const QGridLayoutEngine *self,
    const QGridLayoutItem *layoutItem) {
  return static_cast<int>(self->effectiveAlignment(layoutItem).toInt());
}

//  void QGridLayoutEngine::insertItem(QGridLayoutItem *item, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine10insertItemEP15QGridLayoutItemi(
    QGridLayoutEngine *self,
    QGridLayoutItem *item,
    int index) {
  self->insertItem(item, index);
}

//  void QGridLayoutEngine::addItem(QGridLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine7addItemEP15QGridLayoutItem(
    QGridLayoutEngine *self,
    QGridLayoutItem *item) {
  self->addItem(item);
}

//  void QGridLayoutEngine::removeItem(QGridLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine10removeItemEP15QGridLayoutItem(
    QGridLayoutEngine *self,
    QGridLayoutItem *item) {
  self->removeItem(item);
}

//  void QGridLayoutEngine::deleteItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine11deleteItemsEv(QGridLayoutEngine *self) {
  self->deleteItems();
}

//  QGridLayoutItem *QGridLayoutEngine::itemAt(int row, int column,
//      Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
QGridLayoutItem *ritual_ZNK17QGridLayoutEngine6itemAtEiiN2Qt11OrientationE(
    const QGridLayoutEngine *self,
    int row,
    int column,
    Qt::Orientation orientation) {
  return self->itemAt(row, column, orientation);
}

//  void QGridLayoutEngine::insertRow(int row, Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine9insertRowEiN2Qt11OrientationE(
    QGridLayoutEngine *self,
    int row,
    Qt::Orientation orientation) {
  self->insertRow(row, orientation);
}

//  void QGridLayoutEngine::removeRows(int row, int count, Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine10removeRowsEiiN2Qt11OrientationE(
    QGridLayoutEngine *self,
    int row,
    int count,
    Qt::Orientation orientation) {
  self->removeRows(row, count, orientation);
}

//  void QGridLayoutEngine::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine10invalidateEv(QGridLayoutEngine *self) {
  self->invalidate();
}

//  void QGridLayoutEngine::setGeometries(const QRectF &contentsGeometry,
//      const QAbstractLayoutStyleInfo *styleInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine13setGeometriesERK6QRectFPK24QAbstractLayoutStyleInfo(
    QGridLayoutEngine *self,
    const QRectF *contentsGeometry,
    const QAbstractLayoutStyleInfo *styleInfo) {
  self->setGeometries(*contentsGeometry, styleInfo);
}

//  QRectF QGridLayoutEngine::cellRect(const QRectF &contentsGeometry, int
//      row, int column, int rowSpan, int columnSpan, const
//      QAbstractLayoutStyleInfo *styleInfo) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGridLayoutEngine8cellRectERK6QRectFiiiiPK24QAbstractLayoutStyleInfo(
    const QGridLayoutEngine *self,
    const QRectF *contentsGeometry,
    int row,
    int column,
    int rowSpan,
    int columnSpan,
    const QAbstractLayoutStyleInfo *styleInfo) {
  return new QRectF(
      self->cellRect(
          *contentsGeometry,
          row,
          column,
          rowSpan,
          columnSpan,
          styleInfo));
}

//  QSizeF QGridLayoutEngine::sizeHint(Qt::SizeHint which, const QSizeF
//      &constraint, const QAbstractLayoutStyleInfo *styleInfo) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK17QGridLayoutEngine8sizeHintEN2Qt8SizeHintERK6QSizeFPK24QAbstractLayoutStyleInfo(
    const QGridLayoutEngine *self,
    Qt::SizeHint which,
    const QSizeF *constraint,
    const QAbstractLayoutStyleInfo *styleInfo) {
  return new QSizeF(self->sizeHint(which, *constraint, styleInfo));
}

//  bool QGridLayoutEngine::ensureDynamicConstraint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGridLayoutEngine23ensureDynamicConstraintEv(
    const QGridLayoutEngine *self) {
  return self->ensureDynamicConstraint();
}

//  bool QGridLayoutEngine::hasDynamicConstraint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGridLayoutEngine20hasDynamicConstraintEv(
    const QGridLayoutEngine *self) {
  return self->hasDynamicConstraint();
}

//  Qt::Orientation QGridLayoutEngine::constraintOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK17QGridLayoutEngine21constraintOrientationEv(
    const QGridLayoutEngine *self) {
  return self->constraintOrientation();
}

//  QLayoutPolicy::ControlTypes QGridLayoutEngine::controlTypes(LayoutSide
//      side) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine12controlTypesE10LayoutSide(
    const QGridLayoutEngine *self,
    LayoutSide side) {
  return static_cast<int>(self->controlTypes(side).toInt());
}

//  void QGridLayoutEngine::transpose()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine9transposeEv(QGridLayoutEngine *self) {
  self->transpose();
}

//  void QGridLayoutEngine::setVisualDirection(Qt::LayoutDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine18setVisualDirectionEN2Qt15LayoutDirectionE(
    QGridLayoutEngine *self,
    Qt::LayoutDirection direction) {
  self->setVisualDirection(direction);
}

//  Qt::LayoutDirection QGridLayoutEngine::visualDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK17QGridLayoutEngine15visualDirectionEv(
    const QGridLayoutEngine *self) {
  return self->visualDirection();
}

//  int QGridLayoutEngine::grossRoundUp(int n)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QGridLayoutEngine12grossRoundUpEi(int n) {
  return QGridLayoutEngine::grossRoundUp(n);
}

//  void QGridLayoutEngine::maybeExpandGrid(int row, int column,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine15maybeExpandGridEiiN2Qt11OrientationE(
    QGridLayoutEngine *self,
    int row,
    int column,
    Qt::Orientation orientation) {
  self->maybeExpandGrid(row, column, orientation);
}

//  void QGridLayoutEngine::regenerateGrid()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine14regenerateGridEv(
    QGridLayoutEngine *self) {
  self->regenerateGrid();
}

//  int QGridLayoutEngine::internalGridRowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine20internalGridRowCountEv(
    const QGridLayoutEngine *self) {
  return self->internalGridRowCount();
}

//  int QGridLayoutEngine::internalGridColumnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGridLayoutEngine23internalGridColumnCountEv(
    const QGridLayoutEngine *self) {
  return self->internalGridColumnCount();
}

//  void QGridLayoutEngine::setItemAt(int row, int column, QGridLayoutItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine9setItemAtEiiP15QGridLayoutItem(
    QGridLayoutEngine *self,
    int row,
    int column,
    QGridLayoutItem *item) {
  self->setItemAt(row, column, item);
}

//  void QGridLayoutEngine::insertOrRemoveRows(int row, int delta,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGridLayoutEngine18insertOrRemoveRowsEiiN2Qt11OrientationE(
    QGridLayoutEngine *self,
    int row,
    int delta,
    Qt::Orientation orientation) {
  self->insertOrRemoveRows(row, delta, orientation);
}

//  void QGridLayoutEngine::fillRowData(QGridLayoutRowData *rowData, const
//      qreal *colPositions, const qreal *colSizes, Qt::Orientation
//      orientation, const QAbstractLayoutStyleInfo *styleInfo) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QGridLayoutEngine11fillRowDataEP18QGridLayoutRowDataPKdS3_N2Qt11OrientationEPK24QAbstractLayoutStyleInfo(
    const QGridLayoutEngine *self,
    QGridLayoutRowData *rowData,
    const qreal *colPositions,
    const qreal *colSizes,
    Qt::Orientation orientation,
    const QAbstractLayoutStyleInfo *styleInfo) {
  self->fillRowData(rowData, colPositions, colSizes, orientation, styleInfo);
}

//  void QGridLayoutEngine::ensureEffectiveFirstAndLastRows() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QGridLayoutEngine31ensureEffectiveFirstAndLastRowsEv(
    const QGridLayoutEngine *self) {
  self->ensureEffectiveFirstAndLastRows();
}

//  void QGridLayoutEngine::ensureColumnAndRowData(QGridLayoutRowData
//      *rowData, QGridLayoutBox *totalBox, const qreal *colPositions, const
//      qreal *colSizes, Qt::Orientation orientation, const
//      QAbstractLayoutStyleInfo *styleInfo) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QGridLayoutEngine22ensureColumnAndRowDataEP18QGridLayoutRowDataP14QGridLayoutBoxPKdS5_N2Qt11OrientationEPK24QAbstractLayoutStyleInfo(
    const QGridLayoutEngine *self,
    QGridLayoutRowData *rowData,
    QGridLayoutBox *totalBox,
    const qreal *colPositions,
    const qreal *colSizes,
    Qt::Orientation orientation,
    const QAbstractLayoutStyleInfo *styleInfo) {
  self->ensureColumnAndRowData(
      rowData,
      totalBox,
      colPositions,
      colSizes,
      orientation,
      styleInfo);
}

//  void QGridLayoutEngine::ensureGeometries(const QSizeF &size, const
//      QAbstractLayoutStyleInfo *styleInfo) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QGridLayoutEngine16ensureGeometriesERK6QSizeFPK24QAbstractLayoutStyleInfo(
    const QGridLayoutEngine *self,
    const QSizeF *size,
    const QAbstractLayoutStyleInfo *styleInfo) {
  self->ensureGeometries(*size, styleInfo);
}
