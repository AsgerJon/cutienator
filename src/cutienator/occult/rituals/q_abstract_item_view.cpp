//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractitemview.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QAbstractItemView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAbstractItemView10metaObjectEv(
    const QAbstractItemView *self) {
  return self->metaObject();
}

//  QString QAbstractItemView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAbstractItemView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemView::tr(s, c, n));
}

//  QAbstractItemView::~QAbstractItemView()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemViewD1Ev(QAbstractItemView *self) {
  delete self;
}

//  void QAbstractItemView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView8setModelEP18QAbstractItemModel(
    QAbstractItemView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractItemModel *QAbstractItemView::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK17QAbstractItemView5modelEv(
    const QAbstractItemView *self) {
  return self->model();
}

//  void QAbstractItemView::setSelectionModel(QItemSelectionModel
//      *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel(
    QAbstractItemView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  QItemSelectionModel *QAbstractItemView::selectionModel() const
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZNK17QAbstractItemView14selectionModelEv(
    const QAbstractItemView *self) {
  return self->selectionModel();
}

//  void QAbstractItemView::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setItemDelegateEP21QAbstractItemDelegate(
    QAbstractItemView *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView12itemDelegateEv(
    const QAbstractItemView *self) {
  return self->itemDelegate();
}

//  void QAbstractItemView::setSelectionMode(QAbstractItemView::SelectionMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16setSelectionModeENS_13SelectionModeE(
    QAbstractItemView *self,
    QAbstractItemView::SelectionMode mode) {
  self->setSelectionMode(mode);
}

//  QAbstractItemView::SelectionMode QAbstractItemView::selectionMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::SelectionMode ritual_ZNK17QAbstractItemView13selectionModeEv(
    const QAbstractItemView *self) {
  return self->selectionMode();
}

//  void QAbstractItemView::setSelectionBehavior(QAbstractItemView::Selection
//      Behavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20setSelectionBehaviorENS_17SelectionBehaviorE(
    QAbstractItemView *self,
    QAbstractItemView::SelectionBehavior behavior) {
  self->setSelectionBehavior(behavior);
}

//  QAbstractItemView::SelectionBehavior
//      QAbstractItemView::selectionBehavior() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::SelectionBehavior ritual_ZNK17QAbstractItemView17selectionBehaviorEv(
    const QAbstractItemView *self) {
  return self->selectionBehavior();
}

//  QModelIndex QAbstractItemView::currentIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QAbstractItemView12currentIndexEv(
    const QAbstractItemView *self) {
  return new QModelIndex(self->currentIndex());
}

//  QModelIndex QAbstractItemView::rootIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QAbstractItemView9rootIndexEv(
    const QAbstractItemView *self) {
  return new QModelIndex(self->rootIndex());
}

//  void QAbstractItemView::setEditTriggers(EditTriggers triggers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setEditTriggersE6QFlagsINS_11EditTriggerEE(
    QAbstractItemView *self,
    int triggers) {
  self->setEditTriggers(
      QFlags<QAbstractItemView::EditTrigger>::fromInt(triggers));
}

//  EditTriggers QAbstractItemView::editTriggers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView12editTriggersEv(
    const QAbstractItemView *self) {
  return static_cast<int>(self->editTriggers().toInt());
}

//  void QAbstractItemView::setVerticalScrollMode(ScrollMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21setVerticalScrollModeENS_10ScrollModeE(
    QAbstractItemView *self,
    QAbstractItemView::ScrollMode mode) {
  self->setVerticalScrollMode(mode);
}

//  ScrollMode QAbstractItemView::verticalScrollMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::ScrollMode ritual_ZNK17QAbstractItemView18verticalScrollModeEv(
    const QAbstractItemView *self) {
  return self->verticalScrollMode();
}

//  void QAbstractItemView::resetVerticalScrollMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23resetVerticalScrollModeEv(
    QAbstractItemView *self) {
  self->resetVerticalScrollMode();
}

//  void QAbstractItemView::setHorizontalScrollMode(ScrollMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23setHorizontalScrollModeENS_10ScrollModeE(
    QAbstractItemView *self,
    QAbstractItemView::ScrollMode mode) {
  self->setHorizontalScrollMode(mode);
}

//  ScrollMode QAbstractItemView::horizontalScrollMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::ScrollMode ritual_ZNK17QAbstractItemView20horizontalScrollModeEv(
    const QAbstractItemView *self) {
  return self->horizontalScrollMode();
}

//  void QAbstractItemView::resetHorizontalScrollMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView25resetHorizontalScrollModeEv(
    QAbstractItemView *self) {
  self->resetHorizontalScrollMode();
}

//  void QAbstractItemView::setAutoScroll(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13setAutoScrollEb(
    QAbstractItemView *self,
    bool enable) {
  self->setAutoScroll(enable);
}

//  bool QAbstractItemView::hasAutoScroll() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView13hasAutoScrollEv(
    const QAbstractItemView *self) {
  return self->hasAutoScroll();
}

//  void QAbstractItemView::setAutoScrollMargin(int margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView19setAutoScrollMarginEi(
    QAbstractItemView *self,
    int margin) {
  self->setAutoScrollMargin(margin);
}

//  int QAbstractItemView::autoScrollMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView16autoScrollMarginEv(
    const QAbstractItemView *self) {
  return self->autoScrollMargin();
}

//  void QAbstractItemView::setTabKeyNavigation(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView19setTabKeyNavigationEb(
    QAbstractItemView *self,
    bool enable) {
  self->setTabKeyNavigation(enable);
}

//  bool QAbstractItemView::tabKeyNavigation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView16tabKeyNavigationEv(
    const QAbstractItemView *self) {
  return self->tabKeyNavigation();
}

//  void QAbstractItemView::setDropIndicatorShown(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21setDropIndicatorShownEb(
    QAbstractItemView *self,
    bool enable) {
  self->setDropIndicatorShown(enable);
}

//  bool QAbstractItemView::showDropIndicator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView17showDropIndicatorEv(
    const QAbstractItemView *self) {
  return self->showDropIndicator();
}

//  void QAbstractItemView::setDragEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14setDragEnabledEb(
    QAbstractItemView *self,
    bool enable) {
  self->setDragEnabled(enable);
}

//  bool QAbstractItemView::dragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView11dragEnabledEv(
    const QAbstractItemView *self) {
  return self->dragEnabled();
}

//  void QAbstractItemView::setDragDropOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView24setDragDropOverwriteModeEb(
    QAbstractItemView *self,
    bool overwrite) {
  self->setDragDropOverwriteMode(overwrite);
}

//  bool QAbstractItemView::dragDropOverwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView21dragDropOverwriteModeEv(
    const QAbstractItemView *self) {
  return self->dragDropOverwriteMode();
}

//  void QAbstractItemView::setDragDropMode(DragDropMode behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setDragDropModeENS_12DragDropModeE(
    QAbstractItemView *self,
    QAbstractItemView::DragDropMode behavior) {
  self->setDragDropMode(behavior);
}

//  DragDropMode QAbstractItemView::dragDropMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::DragDropMode ritual_ZNK17QAbstractItemView12dragDropModeEv(
    const QAbstractItemView *self) {
  return self->dragDropMode();
}

//  void QAbstractItemView::setDefaultDropAction(Qt::DropAction dropAction)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20setDefaultDropActionEN2Qt10DropActionE(
    QAbstractItemView *self,
    Qt::DropAction dropAction) {
  self->setDefaultDropAction(dropAction);
}

//  Qt::DropAction QAbstractItemView::defaultDropAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK17QAbstractItemView17defaultDropActionEv(
    const QAbstractItemView *self) {
  return self->defaultDropAction();
}

//  void QAbstractItemView::setAlternatingRowColors(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23setAlternatingRowColorsEb(
    QAbstractItemView *self,
    bool enable) {
  self->setAlternatingRowColors(enable);
}

//  bool QAbstractItemView::alternatingRowColors() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView20alternatingRowColorsEv(
    const QAbstractItemView *self) {
  return self->alternatingRowColors();
}

//  void QAbstractItemView::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView11setIconSizeERK5QSize(
    QAbstractItemView *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  QSize QAbstractItemView::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QAbstractItemView8iconSizeEv(
    const QAbstractItemView *self) {
  return new QSize(self->iconSize());
}

//  void QAbstractItemView::setTextElideMode(Qt::TextElideMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16setTextElideModeEN2Qt13TextElideModeE(
    QAbstractItemView *self,
    Qt::TextElideMode mode) {
  self->setTextElideMode(mode);
}

//  Qt::TextElideMode QAbstractItemView::textElideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK17QAbstractItemView13textElideModeEv(
    const QAbstractItemView *self) {
  return self->textElideMode();
}

//  void QAbstractItemView::keyboardSearch(const QString &search)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14keyboardSearchERK7QString(
    QAbstractItemView *self,
    const QString *search) {
  self->keyboardSearch(*search);
}

//  QRect QAbstractItemView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAbstractItemView10visualRectERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QAbstractItemView::scrollTo(const QModelIndex &index, ScrollHint
//      hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE(
    QAbstractItemView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QModelIndex QAbstractItemView::indexAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QAbstractItemView7indexAtERK6QPoint(
    const QAbstractItemView *self,
    const QPoint *point) {
  return new QModelIndex(self->indexAt(*point));
}

//  QSize QAbstractItemView::sizeHintForIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QAbstractItemView16sizeHintForIndexERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return new QSize(self->sizeHintForIndex(*index));
}

//  int QAbstractItemView::sizeHintForRow(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView14sizeHintForRowEi(
    const QAbstractItemView *self,
    int row) {
  return self->sizeHintForRow(row);
}

//  int QAbstractItemView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView17sizeHintForColumnEi(
    const QAbstractItemView *self,
    int column) {
  return self->sizeHintForColumn(column);
}

//  int QAbstractItemView::updateThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView15updateThresholdEv(
    const QAbstractItemView *self) {
  return self->updateThreshold();
}

//  void QAbstractItemView::setUpdateThreshold(int threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView18setUpdateThresholdEi(
    QAbstractItemView *self,
    int threshold) {
  self->setUpdateThreshold(threshold);
}

//  Qt::MatchFlags QAbstractItemView::keyboardSearchFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView19keyboardSearchFlagsEv(
    const QAbstractItemView *self) {
  return static_cast<int>(self->keyboardSearchFlags().toInt());
}

//  void QAbstractItemView::setKeyboardSearchFlags(Qt::MatchFlags
//      searchFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView22setKeyboardSearchFlagsE6QFlagsIN2Qt9MatchFlagEE(
    QAbstractItemView *self,
    int searchFlags) {
  self->setKeyboardSearchFlags(QFlags<Qt::MatchFlag>::fromInt(searchFlags));
}

//  void QAbstractItemView::openPersistentEditor(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20openPersistentEditorERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->openPersistentEditor(*index);
}

//  void QAbstractItemView::closePersistentEditor(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21closePersistentEditorERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->closePersistentEditor(*index);
}

//  bool QAbstractItemView::isPersistentEditorOpen(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView22isPersistentEditorOpenERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->isPersistentEditorOpen(*index);
}

//  void QAbstractItemView::setIndexWidget(const QModelIndex &index, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14setIndexWidgetERK11QModelIndexP7QWidget(
    QAbstractItemView *self,
    const QModelIndex *index,
    QWidget *widget) {
  self->setIndexWidget(*index, widget);
}

//  QWidget *QAbstractItemView::indexWidget(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK17QAbstractItemView11indexWidgetERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->indexWidget(*index);
}

//  void QAbstractItemView::setItemDelegateForRow(int row,
//      QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21setItemDelegateForRowEiP21QAbstractItemDelegate(
    QAbstractItemView *self,
    int row,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegateForRow(row, delegate);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForRow(int row)
//      const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView18itemDelegateForRowEi(
    const QAbstractItemView *self,
    int row) {
  return self->itemDelegateForRow(row);
}

//  void QAbstractItemView::setItemDelegateForColumn(int column,
//      QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView24setItemDelegateForColumnEiP21QAbstractItemDelegate(
    QAbstractItemView *self,
    int column,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegateForColumn(column, delegate);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForColumn(int
//      column) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView21itemDelegateForColumnEi(
    const QAbstractItemView *self,
    int column) {
  return self->itemDelegateForColumn(column);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegate(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView12itemDelegateERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->itemDelegate(*index);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->itemDelegateForIndex(*index);
}

//  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QAbstractItemView16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QAbstractItemView *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  void QAbstractItemView::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView5resetEv(QAbstractItemView *self) {
  self->reset();
}

//  void QAbstractItemView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView12setRootIndexERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QAbstractItemView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13doItemsLayoutEv(QAbstractItemView *self) {
  self->doItemsLayout();
}

//  void QAbstractItemView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView9selectAllEv(QAbstractItemView *self) {
  self->selectAll();
}

//  void QAbstractItemView::edit(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView4editERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->edit(*index);
}

//  void QAbstractItemView::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14clearSelectionEv(
    QAbstractItemView *self) {
  self->clearSelection();
}

//  void QAbstractItemView::setCurrentIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setCurrentIndexERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->setCurrentIndex(*index);
}

//  void QAbstractItemView::scrollToTop()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView11scrollToTopEv(QAbstractItemView *self) {
  self->scrollToTop();
}

//  void QAbstractItemView::scrollToBottom()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14scrollToBottomEv(
    QAbstractItemView *self) {
  self->scrollToBottom();
}

//  void QAbstractItemView::update(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView6updateERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->update(*index);
}
