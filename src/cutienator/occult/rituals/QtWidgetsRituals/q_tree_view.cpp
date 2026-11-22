//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreeview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtreeview.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QTreeView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTreeView10metaObjectEv(
    const QTreeView *self) {
  return self->metaObject();
}

//  QString QTreeView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTreeView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTreeView::tr(s, c, n));
}

//  QTreeView::QTreeView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTreeView *ritual_ZN9QTreeViewC1EP7QWidget(QWidget *parent) {
  return new QTreeView(parent);
}

//  QTreeView::~QTreeView()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeViewD1Ev(QTreeView *self) {
  delete self;
}

//  void QTreeView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView8setModelEP18QAbstractItemModel(
    QTreeView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  void QTreeView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView12setRootIndexERK11QModelIndex(
    QTreeView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QTreeView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView17setSelectionModelEP19QItemSelectionModel(
    QTreeView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  QHeaderView *QTreeView::header() const
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZNK9QTreeView6headerEv(const QTreeView *self) {
  return self->header();
}

//  void QTreeView::setHeader(QHeaderView *header)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView9setHeaderEP11QHeaderView(
    QTreeView *self,
    QHeaderView *header) {
  self->setHeader(header);
}

//  int QTreeView::autoExpandDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView15autoExpandDelayEv(const QTreeView *self) {
  return self->autoExpandDelay();
}

//  void QTreeView::setAutoExpandDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView18setAutoExpandDelayEi(QTreeView *self, int delay) {
  self->setAutoExpandDelay(delay);
}

//  int QTreeView::indentation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView11indentationEv(const QTreeView *self) {
  return self->indentation();
}

//  void QTreeView::setIndentation(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView14setIndentationEi(QTreeView *self, int i) {
  self->setIndentation(i);
}

//  void QTreeView::resetIndentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView16resetIndentationEv(QTreeView *self) {
  self->resetIndentation();
}

//  bool QTreeView::rootIsDecorated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView15rootIsDecoratedEv(const QTreeView *self) {
  return self->rootIsDecorated();
}

//  void QTreeView::setRootIsDecorated(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView18setRootIsDecoratedEb(QTreeView *self, bool show) {
  self->setRootIsDecorated(show);
}

//  bool QTreeView::uniformRowHeights() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView17uniformRowHeightsEv(const QTreeView *self) {
  return self->uniformRowHeights();
}

//  void QTreeView::setUniformRowHeights(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView20setUniformRowHeightsEb(
    QTreeView *self,
    bool uniform) {
  self->setUniformRowHeights(uniform);
}

//  bool QTreeView::itemsExpandable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView15itemsExpandableEv(const QTreeView *self) {
  return self->itemsExpandable();
}

//  void QTreeView::setItemsExpandable(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView18setItemsExpandableEb(
    QTreeView *self,
    bool enable) {
  self->setItemsExpandable(enable);
}

//  bool QTreeView::expandsOnDoubleClick() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView20expandsOnDoubleClickEv(const QTreeView *self) {
  return self->expandsOnDoubleClick();
}

//  void QTreeView::setExpandsOnDoubleClick(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView23setExpandsOnDoubleClickEb(
    QTreeView *self,
    bool enable) {
  self->setExpandsOnDoubleClick(enable);
}

//  int QTreeView::columnViewportPosition(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView22columnViewportPositionEi(
    const QTreeView *self,
    int column) {
  return self->columnViewportPosition(column);
}

//  int QTreeView::columnWidth(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView11columnWidthEi(const QTreeView *self, int column) {
  return self->columnWidth(column);
}

//  void QTreeView::setColumnWidth(int column, int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView14setColumnWidthEii(
    QTreeView *self,
    int column,
    int width) {
  self->setColumnWidth(column, width);
}

//  int QTreeView::columnAt(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView8columnAtEi(const QTreeView *self, int x) {
  return self->columnAt(x);
}

//  bool QTreeView::isColumnHidden(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView14isColumnHiddenEi(
    const QTreeView *self,
    int column) {
  return self->isColumnHidden(column);
}

//  void QTreeView::setColumnHidden(int column, bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView15setColumnHiddenEib(
    QTreeView *self,
    int column,
    bool hide) {
  self->setColumnHidden(column, hide);
}

//  bool QTreeView::isHeaderHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView14isHeaderHiddenEv(const QTreeView *self) {
  return self->isHeaderHidden();
}

//  void QTreeView::setHeaderHidden(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView15setHeaderHiddenEb(QTreeView *self, bool hide) {
  self->setHeaderHidden(hide);
}

//  bool QTreeView::isRowHidden(int row, const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView11isRowHiddenEiRK11QModelIndex(
    const QTreeView *self,
    int row,
    const QModelIndex *parent) {
  return self->isRowHidden(row, *parent);
}

//  void QTreeView::setRowHidden(int row, const QModelIndex &parent, bool
//      hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView12setRowHiddenEiRK11QModelIndexb(
    QTreeView *self,
    int row,
    const QModelIndex *parent,
    bool hide) {
  self->setRowHidden(row, *parent, hide);
}

//  bool QTreeView::isFirstColumnSpanned(int row, const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView20isFirstColumnSpannedEiRK11QModelIndex(
    const QTreeView *self,
    int row,
    const QModelIndex *parent) {
  return self->isFirstColumnSpanned(row, *parent);
}

//  void QTreeView::setFirstColumnSpanned(int row, const QModelIndex &parent,
//      bool span)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView21setFirstColumnSpannedEiRK11QModelIndexb(
    QTreeView *self,
    int row,
    const QModelIndex *parent,
    bool span) {
  self->setFirstColumnSpanned(row, *parent, span);
}

//  bool QTreeView::isExpanded(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView10isExpandedERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return self->isExpanded(*index);
}

//  void QTreeView::setExpanded(const QModelIndex &index, bool expand)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11setExpandedERK11QModelIndexb(
    QTreeView *self,
    const QModelIndex *index,
    bool expand) {
  self->setExpanded(*index, expand);
}

//  void QTreeView::setSortingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView17setSortingEnabledEb(QTreeView *self, bool enable) {
  self->setSortingEnabled(enable);
}

//  bool QTreeView::isSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView16isSortingEnabledEv(const QTreeView *self) {
  return self->isSortingEnabled();
}

//  void QTreeView::setAnimated(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11setAnimatedEb(QTreeView *self, bool enable) {
  self->setAnimated(enable);
}

//  bool QTreeView::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView10isAnimatedEv(const QTreeView *self) {
  return self->isAnimated();
}

//  void QTreeView::setAllColumnsShowFocus(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView22setAllColumnsShowFocusEb(
    QTreeView *self,
    bool enable) {
  self->setAllColumnsShowFocus(enable);
}

//  bool QTreeView::allColumnsShowFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView19allColumnsShowFocusEv(const QTreeView *self) {
  return self->allColumnsShowFocus();
}

//  void QTreeView::setWordWrap(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11setWordWrapEb(QTreeView *self, bool on) {
  self->setWordWrap(on);
}

//  bool QTreeView::wordWrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView8wordWrapEv(const QTreeView *self) {
  return self->wordWrap();
}

//  void QTreeView::setTreePosition(int logicalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView15setTreePositionEi(
    QTreeView *self,
    int logicalIndex) {
  self->setTreePosition(logicalIndex);
}

//  int QTreeView::treePosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView12treePositionEv(const QTreeView *self) {
  return self->treePosition();
}

//  void QTreeView::keyboardSearch(const QString &search)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView14keyboardSearchERK7QString(
    QTreeView *self,
    const QString *search) {
  self->keyboardSearch(*search);
}

//  QRect QTreeView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QTreeView10visualRectERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  QRect QTreeView::itemDecorationRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QTreeView18itemDecorationRectERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return new QRect(self->itemDecorationRect(*index));
}

//  void QTreeView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QTreeView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QModelIndex QTreeView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QTreeView7indexAtERK6QPoint(
    const QTreeView *self,
    const QPoint *p) {
  return new QModelIndex(self->indexAt(*p));
}

//  QModelIndex QTreeView::indexAbove(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QTreeView10indexAboveERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return new QModelIndex(self->indexAbove(*index));
}

//  QModelIndex QTreeView::indexBelow(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QTreeView10indexBelowERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return new QModelIndex(self->indexBelow(*index));
}

//  void QTreeView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView13doItemsLayoutEv(QTreeView *self) {
  self->doItemsLayout();
}

//  void QTreeView::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView5resetEv(QTreeView *self) {
  self->reset();
}

//  void QTreeView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView9selectAllEv(QTreeView *self) {
  self->selectAll();
}

//  void QTreeView::hideColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView10hideColumnEi(QTreeView *self, int column) {
  self->hideColumn(column);
}

//  void QTreeView::showColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView10showColumnEi(QTreeView *self, int column) {
  self->showColumn(column);
}

//  void QTreeView::expand(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView6expandERK11QModelIndex(
    QTreeView *self,
    const QModelIndex *index) {
  self->expand(*index);
}

//  void QTreeView::collapse(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView8collapseERK11QModelIndex(
    QTreeView *self,
    const QModelIndex *index) {
  self->collapse(*index);
}

//  void QTreeView::resizeColumnToContents(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView22resizeColumnToContentsEi(
    QTreeView *self,
    int column) {
  self->resizeColumnToContents(column);
}

//  void QTreeView::sortByColumn(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView12sortByColumnEiN2Qt9SortOrderE(
    QTreeView *self,
    int column,
    Qt::SortOrder order) {
  self->sortByColumn(column, order);
}

//  void QTreeView::expandAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView9expandAllEv(QTreeView *self) {
  self->expandAll();
}

//  void QTreeView::expandRecursively(const QModelIndex &index, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView17expandRecursivelyERK11QModelIndexi(
    QTreeView *self,
    const QModelIndex *index,
    int depth) {
  self->expandRecursively(*index, depth);
}

//  void QTreeView::collapseAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11collapseAllEv(QTreeView *self) {
  self->collapseAll();
}

//  void QTreeView::expandToDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView13expandToDepthEi(QTreeView *self, int depth) {
  self->expandToDepth(depth);
}
