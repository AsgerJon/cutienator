//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qrangemodel.h>

//  QRangeModelDetails::DroppedEntryCell::DroppedEntryCell()
extern "C" Q_DECL_EXPORT
QRangeModelDetails::DroppedEntryCell *ritual_ZN18QRangeModelDetails16DroppedEntryCellC1Ev() {
  return new QRangeModelDetails::DroppedEntryCell();
}

//  QRangeModelDetails::DroppedEntryCell::DroppedEntryCell(int row, int
//      column)
extern "C" Q_DECL_EXPORT
QRangeModelDetails::DroppedEntryCell *ritual_ZN18QRangeModelDetails16DroppedEntryCellC1Eii(
    int row,
    int column) {
  return new QRangeModelDetails::DroppedEntryCell(row, column);
}

//  bool operator==(const DroppedEntryCell &lhs, const DroppedEntryCell &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRangeModelDetailseqERKNS_16DroppedEntryCellES2_(
    const QRangeModelDetails::DroppedEntryCell *lhs,
    const QRangeModelDetails::DroppedEntryCell *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const DroppedEntryCell &lhs, const DroppedEntryCell &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QRangeModelDetailsneERKNS_16DroppedEntryCellES2_(
    const QRangeModelDetails::DroppedEntryCell *lhs,
    const QRangeModelDetails::DroppedEntryCell *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QRangeModelDetails::DroppedEntryCell::~DroppedEntryCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRangeModelDetails16DroppedEntryCellD1Ev(
    QRangeModelDetails::DroppedEntryCell *self) {
  delete self;
}

#endif  // !defined(Q_QDOC)
