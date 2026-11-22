//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlistview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlistview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QListView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QListView10metaObjectEv(
    const QListView *self) {
  return self->metaObject();
}

//  QString QListView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QListView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QListView::tr(s, c, n));
}

//  QListView::QListView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QListView *ritual_ZN9QListViewC1EP7QWidget(QWidget *parent) {
  return new QListView(parent);
}

//  QListView::~QListView()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListViewD1Ev(QListView *self) {
  delete self;
}

//  void QListView::setMovement(Movement movement)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView11setMovementENS_8MovementE(
    QListView *self,
    QListView::Movement movement) {
  self->setMovement(movement);
}

//  Movement QListView::movement() const
extern "C" Q_DECL_EXPORT
QListView::Movement ritual_ZNK9QListView8movementEv(const QListView *self) {
  return self->movement();
}

//  void QListView::setFlow(Flow flow)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView7setFlowENS_4FlowE(
    QListView *self,
    QListView::Flow flow) {
  self->setFlow(flow);
}

//  Flow QListView::flow() const
extern "C" Q_DECL_EXPORT
QListView::Flow ritual_ZNK9QListView4flowEv(const QListView *self) {
  return self->flow();
}

//  void QListView::setWrapping(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView11setWrappingEb(QListView *self, bool enable) {
  self->setWrapping(enable);
}

//  bool QListView::isWrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QListView10isWrappingEv(const QListView *self) {
  return self->isWrapping();
}

//  void QListView::setResizeMode(ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView13setResizeModeENS_10ResizeModeE(
    QListView *self,
    QListView::ResizeMode mode) {
  self->setResizeMode(mode);
}

//  ResizeMode QListView::resizeMode() const
extern "C" Q_DECL_EXPORT
QListView::ResizeMode ritual_ZNK9QListView10resizeModeEv(
    const QListView *self) {
  return self->resizeMode();
}

//  void QListView::setLayoutMode(LayoutMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView13setLayoutModeENS_10LayoutModeE(
    QListView *self,
    QListView::LayoutMode mode) {
  self->setLayoutMode(mode);
}

//  LayoutMode QListView::layoutMode() const
extern "C" Q_DECL_EXPORT
QListView::LayoutMode ritual_ZNK9QListView10layoutModeEv(
    const QListView *self) {
  return self->layoutMode();
}

//  void QListView::setSpacing(int space)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView10setSpacingEi(QListView *self, int space) {
  self->setSpacing(space);
}

//  int QListView::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView7spacingEv(const QListView *self) {
  return self->spacing();
}

//  void QListView::setBatchSize(int batchSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView12setBatchSizeEi(QListView *self, int batchSize) {
  self->setBatchSize(batchSize);
}

//  int QListView::batchSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView9batchSizeEv(const QListView *self) {
  return self->batchSize();
}

//  void QListView::setGridSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView11setGridSizeERK5QSize(
    QListView *self,
    const QSize *size) {
  self->setGridSize(*size);
}

//  QSize QListView::gridSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QListView8gridSizeEv(const QListView *self) {
  return new QSize(self->gridSize());
}

//  void QListView::setViewMode(ViewMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView11setViewModeENS_8ViewModeE(
    QListView *self,
    QListView::ViewMode mode) {
  self->setViewMode(mode);
}

//  ViewMode QListView::viewMode() const
extern "C" Q_DECL_EXPORT
QListView::ViewMode ritual_ZNK9QListView8viewModeEv(const QListView *self) {
  return self->viewMode();
}

//  void QListView::clearPropertyFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView18clearPropertyFlagsEv(QListView *self) {
  self->clearPropertyFlags();
}

//  bool QListView::isRowHidden(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QListView11isRowHiddenEi(const QListView *self, int row) {
  return self->isRowHidden(row);
}

//  void QListView::setRowHidden(int row, bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView12setRowHiddenEib(
    QListView *self,
    int row,
    bool hide) {
  self->setRowHidden(row, hide);
}

//  void QListView::setModelColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView14setModelColumnEi(QListView *self, int column) {
  self->setModelColumn(column);
}

//  int QListView::modelColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView11modelColumnEv(const QListView *self) {
  return self->modelColumn();
}

//  void QListView::setUniformItemSizes(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView19setUniformItemSizesEb(
    QListView *self,
    bool enable) {
  self->setUniformItemSizes(enable);
}

//  bool QListView::uniformItemSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QListView16uniformItemSizesEv(const QListView *self) {
  return self->uniformItemSizes();
}

//  void QListView::setWordWrap(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView11setWordWrapEb(QListView *self, bool on) {
  self->setWordWrap(on);
}

//  bool QListView::wordWrap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QListView8wordWrapEv(const QListView *self) {
  return self->wordWrap();
}

//  void QListView::setSelectionRectVisible(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView23setSelectionRectVisibleEb(
    QListView *self,
    bool show) {
  self->setSelectionRectVisible(show);
}

//  bool QListView::isSelectionRectVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QListView22isSelectionRectVisibleEv(const QListView *self) {
  return self->isSelectionRectVisible();
}

//  void QListView::setItemAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView16setItemAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QListView *self,
    int alignment) {
  self->setItemAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  Qt::Alignment QListView::itemAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView13itemAlignmentEv(const QListView *self) {
  return static_cast<int>(self->itemAlignment().toInt());
}

//  QRect QListView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QListView10visualRectERK11QModelIndex(
    const QListView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QListView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QListView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QModelIndex QListView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK9QListView7indexAtERK6QPoint(
    const QListView *self,
    const QPoint *p) {
  return new QModelIndex(self->indexAt(*p));
}

//  void QListView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView13doItemsLayoutEv(QListView *self) {
  self->doItemsLayout();
}

//  void QListView::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView5resetEv(QListView *self) {
  self->reset();
}

//  void QListView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView12setRootIndexERK11QModelIndex(
    QListView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}
