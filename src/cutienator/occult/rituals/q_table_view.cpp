//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtableview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtableview.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QTableView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTableView10metaObjectEv(
    const QTableView *self) {
  return self->metaObject();
}

//  QString QTableView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTableView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTableView::tr(s, c, n));
}

//  QTableView::QTableView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTableView *ritual_ZN10QTableViewC1EP7QWidget(QWidget *parent) {
  return new QTableView(parent);
}

//  QTableView::~QTableView()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableViewD1Ev(QTableView *self) {
  delete self;
}

//  void QTableView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView8setModelEP18QAbstractItemModel(
    QTableView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  void QTableView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12setRootIndexERK11QModelIndex(
    QTableView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QTableView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView17setSelectionModelEP19QItemSelectionModel(
    QTableView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  void QTableView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView13doItemsLayoutEv(QTableView *self) {
  self->doItemsLayout();
}

//  QHeaderView *QTableView::horizontalHeader() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK10QTableView16horizontalHeaderEv(
    const QTableView *self) {
  return self->horizontalHeader();
}

//  QHeaderView *QTableView::verticalHeader() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK10QTableView14verticalHeaderEv(
    const QTableView *self) {
  return self->verticalHeader();
}

//  void QTableView::setHorizontalHeader(QHeaderView *header)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView19setHorizontalHeaderEP11QHeaderView(
    QTableView *self,
    QHeaderView *header) {
  self->setHorizontalHeader(header);
}

//  void QTableView::setVerticalHeader(QHeaderView *header)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView17setVerticalHeaderEP11QHeaderView(
    QTableView *self,
    QHeaderView *header) {
  self->setVerticalHeader(header);
}

//  int QTableView::rowViewportPosition(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView19rowViewportPositionEi(
    const QTableView *self,
    int row) {
  return self->rowViewportPosition(row);
}

//  int QTableView::rowAt(int y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView5rowAtEi(const QTableView *self, int y) {
  return self->rowAt(y);
}

//  void QTableView::setRowHeight(int row, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12setRowHeightEii(
    QTableView *self,
    int row,
    int height) {
  self->setRowHeight(row, height);
}

//  int QTableView::rowHeight(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView9rowHeightEi(const QTableView *self, int row) {
  return self->rowHeight(row);
}

//  int QTableView::columnViewportPosition(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView22columnViewportPositionEi(
    const QTableView *self,
    int column) {
  return self->columnViewportPosition(column);
}

//  int QTableView::columnAt(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView8columnAtEi(const QTableView *self, int x) {
  return self->columnAt(x);
}

//  void QTableView::setColumnWidth(int column, int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView14setColumnWidthEii(
    QTableView *self,
    int column,
    int width) {
  self->setColumnWidth(column, width);
}

//  int QTableView::columnWidth(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView11columnWidthEi(
    const QTableView *self,
    int column) {
  return self->columnWidth(column);
}

//  bool QTableView::isRowHidden(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView11isRowHiddenEi(const QTableView *self, int row) {
  return self->isRowHidden(row);
}

//  void QTableView::setRowHidden(int row, bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12setRowHiddenEib(
    QTableView *self,
    int row,
    bool hide) {
  self->setRowHidden(row, hide);
}

//  bool QTableView::isColumnHidden(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView14isColumnHiddenEi(
    const QTableView *self,
    int column) {
  return self->isColumnHidden(column);
}

//  void QTableView::setColumnHidden(int column, bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView15setColumnHiddenEib(
    QTableView *self,
    int column,
    bool hide) {
  self->setColumnHidden(column, hide);
}

//  void QTableView::setSortingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView17setSortingEnabledEb(
    QTableView *self,
    bool enable) {
  self->setSortingEnabled(enable);
}

//  bool QTableView::isSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView16isSortingEnabledEv(const QTableView *self) {
  return self->isSortingEnabled();
}

//  bool QTableView::showGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView8showGridEv(const QTableView *self) {
  return self->showGrid();
}

//  Qt::PenStyle QTableView::gridStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenStyle ritual_ZNK10QTableView9gridStyleEv(const QTableView *self) {
  return self->gridStyle();
}

//  void QTableView::setGridStyle(Qt::PenStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12setGridStyleEN2Qt8PenStyleE(
    QTableView *self,
    Qt::PenStyle style) {
  self->setGridStyle(style);
}

//  void QTableView::setWordWrap(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView11setWordWrapEb(QTableView *self, bool on) {
  self->setWordWrap(on);
}

//  bool QTableView::wordWrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView8wordWrapEv(const QTableView *self) {
  return self->wordWrap();
}

//  void QTableView::setCornerButtonEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView22setCornerButtonEnabledEb(
    QTableView *self,
    bool enable) {
  self->setCornerButtonEnabled(enable);
}

//  bool QTableView::isCornerButtonEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView21isCornerButtonEnabledEv(
    const QTableView *self) {
  return self->isCornerButtonEnabled();
}

//  QRect QTableView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10QTableView10visualRectERK11QModelIndex(
    const QTableView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QTableView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QTableView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QModelIndex QTableView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QTableView7indexAtERK6QPoint(
    const QTableView *self,
    const QPoint *p) {
  return new QModelIndex(self->indexAt(*p));
}

//  void QTableView::setSpan(int row, int column, int rowSpan, int
//      columnSpan)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView7setSpanEiiii(
    QTableView *self,
    int row,
    int column,
    int rowSpan,
    int columnSpan) {
  self->setSpan(row, column, rowSpan, columnSpan);
}

//  int QTableView::rowSpan(int row, int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView7rowSpanEii(
    const QTableView *self,
    int row,
    int column) {
  return self->rowSpan(row, column);
}

//  int QTableView::columnSpan(int row, int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView10columnSpanEii(
    const QTableView *self,
    int row,
    int column) {
  return self->columnSpan(row, column);
}

//  void QTableView::clearSpans()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView10clearSpansEv(QTableView *self) {
  self->clearSpans();
}

//  void QTableView::selectRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView9selectRowEi(QTableView *self, int row) {
  self->selectRow(row);
}

//  void QTableView::selectColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12selectColumnEi(QTableView *self, int column) {
  self->selectColumn(column);
}

//  void QTableView::hideRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView7hideRowEi(QTableView *self, int row) {
  self->hideRow(row);
}

//  void QTableView::hideColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView10hideColumnEi(QTableView *self, int column) {
  self->hideColumn(column);
}

//  void QTableView::showRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView7showRowEi(QTableView *self, int row) {
  self->showRow(row);
}

//  void QTableView::showColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView10showColumnEi(QTableView *self, int column) {
  self->showColumn(column);
}

//  void QTableView::resizeRowToContents(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView19resizeRowToContentsEi(
    QTableView *self,
    int row) {
  self->resizeRowToContents(row);
}

//  void QTableView::resizeRowsToContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView20resizeRowsToContentsEv(QTableView *self) {
  self->resizeRowsToContents();
}

//  void QTableView::resizeColumnToContents(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView22resizeColumnToContentsEi(
    QTableView *self,
    int column) {
  self->resizeColumnToContents(column);
}

//  void QTableView::resizeColumnsToContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView23resizeColumnsToContentsEv(QTableView *self) {
  self->resizeColumnsToContents();
}

//  void QTableView::sortByColumn(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12sortByColumnEiN2Qt9SortOrderE(
    QTableView *self,
    int column,
    Qt::SortOrder order) {
  self->sortByColumn(column, order);
}

//  void QTableView::setShowGrid(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView11setShowGridEb(QTableView *self, bool show) {
  self->setShowGrid(show);
}
