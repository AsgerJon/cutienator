//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtreewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QTreeWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTreeWidget : QTreeWidget {
  using QTreeWidget::event;
  using QTreeWidget::dropMimeData;
  using QTreeWidget::dropEvent;
};

//  A QTreeWidget that Python can take functions over in. Every QTreeWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTreeWidgetCall0)(const void *, QItemSelectionModel *, int *);
typedef bool (*CuteQTreeWidgetCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQTreeWidgetCall2)(const void *, QTreeWidgetItem *, int, const QMimeData *, int, int *);
typedef void (*CuteQTreeWidgetCall3)(const void *, QDropEvent *, int *);
typedef void (*CuteQTreeWidgetCall4)(const void *, const QModelIndex *, int *);
typedef const QRect * (*CuteQTreeWidgetCall5)(const void *, const QModelIndex *, int *);
typedef void (*CuteQTreeWidgetCall6)(const void *, const QModelIndex *, int, int *);
typedef const QModelIndex * (*CuteQTreeWidgetCall7)(const void *, const QPoint *, int *);
typedef void (*CuteQTreeWidgetCall8)(const void *, int *);
typedef void (*CuteQTreeWidgetCall9)(const void *, int *);
typedef void (*CuteQTreeWidgetCall10)(const void *, int *);
typedef void (*CuteQTreeWidgetCall11)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall12)(const void *, int, int, int *);
typedef void (*CuteQTreeWidgetCall13)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQTreeWidgetCall14)(const void *, const QModelIndex *, int, int, int *);
typedef int (*CuteQTreeWidgetCall15)(const void *, int *);
typedef int (*CuteQTreeWidgetCall16)(const void *, int *);
typedef const QRegion * (*CuteQTreeWidgetCall17)(const void *, const QItemSelection *, int *);
typedef void (*CuteQTreeWidgetCall18)(const void *, QEvent *, int *);
typedef void (*CuteQTreeWidgetCall19)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTreeWidgetCall20)(const void *, QPaintEvent *, int *);
typedef void (*CuteQTreeWidgetCall21)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
typedef void (*CuteQTreeWidgetCall22)(const void *, QPainter *, const QRect *, const QModelIndex *, int *);
typedef void (*CuteQTreeWidgetCall23)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTreeWidgetCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTreeWidgetCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTreeWidgetCall26)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTreeWidgetCall27)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTreeWidgetCall28)(const void *, QDragMoveEvent *, int *);
typedef bool (*CuteQTreeWidgetCall29)(const void *, QEvent *, int *);
typedef void (*CuteQTreeWidgetCall30)(const void *, int *);
typedef const QSize * (*CuteQTreeWidgetCall31)(const void *, int *);
typedef int (*CuteQTreeWidgetCall32)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall33)(const void *, int, int *);
typedef bool (*CuteQTreeWidgetCall34)(const void *, const QModelIndex *, int *);
typedef void (*CuteQTreeWidgetCall35)(const void *, const QItemSelection *, const QItemSelection *, int *);
typedef void (*CuteQTreeWidgetCall36)(const void *, const QModelIndex *, const QModelIndex *, int *);
typedef int (*CuteQTreeWidgetCall37)(const void *, int, int *);
typedef void * (*CuteQTreeWidgetCall38)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQTreeWidgetCall39)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall40)(const void *, int *);
typedef void (*CuteQTreeWidgetCall41)(const void *, int *);
typedef void (*CuteQTreeWidgetCall42)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall43)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall44)(const void *, QWidget *, int, int *);
typedef void (*CuteQTreeWidgetCall45)(const void *, QWidget *, int *);
typedef void (*CuteQTreeWidgetCall46)(const void *, QObject *, int *);
typedef bool (*CuteQTreeWidgetCall47)(const void *, const QModelIndex *, int, QEvent *, int *);
typedef void (*CuteQTreeWidgetCall48)(const void *, QStyleOptionViewItem *, int *);
typedef bool (*CuteQTreeWidgetCall49)(const void *, bool, int *);
typedef void (*CuteQTreeWidgetCall50)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQTreeWidgetCall51)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQTreeWidgetCall52)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTreeWidgetCall53)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTreeWidgetCall54)(const void *, QResizeEvent *, int *);
typedef void (*CuteQTreeWidgetCall55)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQTreeWidgetCall56)(const void *, QObject *, QEvent *, int *);
typedef const QSize * (*CuteQTreeWidgetCall57)(const void *, int *);
typedef const QSize * (*CuteQTreeWidgetCall58)(const void *, int *);
typedef void (*CuteQTreeWidgetCall59)(const void *, QWidget *, int *);
typedef void (*CuteQTreeWidgetCall60)(const void *, QWheelEvent *, int *);
typedef void (*CuteQTreeWidgetCall61)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQTreeWidgetCall62)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTreeWidgetCall63)(const void *, int *);
typedef void (*CuteQTreeWidgetCall64)(const void *, bool, int *);
typedef int (*CuteQTreeWidgetCall65)(const void *, int, int *);
typedef bool (*CuteQTreeWidgetCall66)(const void *, int *);
typedef void * (*CuteQTreeWidgetCall67)(const void *, int *);
typedef void (*CuteQTreeWidgetCall68)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTreeWidgetCall69)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTreeWidgetCall70)(const void *, QEvent *, int *);
typedef void (*CuteQTreeWidgetCall71)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTreeWidgetCall72)(const void *, QCloseEvent *, int *);
typedef void (*CuteQTreeWidgetCall73)(const void *, QTabletEvent *, int *);
typedef void (*CuteQTreeWidgetCall74)(const void *, QActionEvent *, int *);
typedef void (*CuteQTreeWidgetCall75)(const void *, QShowEvent *, int *);
typedef void (*CuteQTreeWidgetCall76)(const void *, QHideEvent *, int *);
typedef int (*CuteQTreeWidgetCall77)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall78)(const void *, QPainter *, int *);
typedef void * (*CuteQTreeWidgetCall79)(const void *, QPoint *, int *);
typedef void * (*CuteQTreeWidgetCall80)(const void *, int *);
typedef void (*CuteQTreeWidgetCall81)(const void *, QChildEvent *, int *);
typedef void (*CuteQTreeWidgetCall82)(const void *, QEvent *, int *);
typedef void (*CuteQTreeWidgetCall83)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTreeWidgetCall84)(const void *, const QMetaMethod *, int *);
class CuteQTreeWidget : public QTreeWidget {
public:
  using QTreeWidget::QTreeWidget;
  void *taken[85] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QTreeWidget12dropMimeDataEP15QTreeWidgetItemiPK9QMimeDataN2Qt10DropActionE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QTreeView7drawRowEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QTreeView12drawBranchesEP8QPainterRK5QRectRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[84] = call;
      return true;
    }
    return false;
  }

  //  void QTreeWidget::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTreeWidgetCall0 call = reinterpret_cast<CuteQTreeWidgetCall0>(taken[0]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QTreeWidget::setSelectionModel(selectionModel);
  }

  //  bool QTreeWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTreeWidgetCall1 call = reinterpret_cast<CuteQTreeWidgetCall1>(taken[1]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QTreeWidget::event(e);
  }

  //  bool QTreeWidget::dropMimeData(QTreeWidgetItem *parent, int index,
  //      const QMimeData *data, Qt::DropAction action)
  bool dropMimeData(
      QTreeWidgetItem *parent,
      int index,
      const QMimeData *data,
      Qt::DropAction action) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTreeWidgetCall2 call = reinterpret_cast<CuteQTreeWidgetCall2>(taken[2]);
      bool given = call(this, parent, index, data, static_cast<int>(action), &handled);
      if (handled) return given;
    }
    return QTreeWidget::dropMimeData(parent, index, data, action);
  }

  //  void QTreeWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTreeWidgetCall3 call = reinterpret_cast<CuteQTreeWidgetCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeWidget::dropEvent(event);
  }

  //  void QTreeView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTreeWidgetCall4 call = reinterpret_cast<CuteQTreeWidgetCall4>(taken[4]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QTreeView::setRootIndex(index);
  }

  //  QRect QTreeView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTreeWidgetCall5 call = reinterpret_cast<CuteQTreeWidgetCall5>(taken[5]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::visualRect(index);
  }

  //  void QTreeView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTreeWidgetCall6 call = reinterpret_cast<CuteQTreeWidgetCall6>(taken[6]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QTreeView::scrollTo(index, hint);
  }

  //  QModelIndex QTreeView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTreeWidgetCall7 call = reinterpret_cast<CuteQTreeWidgetCall7>(taken[7]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::indexAt(p);
  }

  //  void QTreeView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[8]) {
      int handled = 0;
      CuteQTreeWidgetCall8 call = reinterpret_cast<CuteQTreeWidgetCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::doItemsLayout();
  }

  //  void QTreeView::reset()
  void reset() override {
    if (taken[9]) {
      int handled = 0;
      CuteQTreeWidgetCall9 call = reinterpret_cast<CuteQTreeWidgetCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::reset();
  }

  //  void QTreeView::selectAll()
  void selectAll() override {
    if (taken[10]) {
      int handled = 0;
      CuteQTreeWidgetCall10 call = reinterpret_cast<CuteQTreeWidgetCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::selectAll();
  }

  //  void QTreeView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTreeWidgetCall11 call = reinterpret_cast<CuteQTreeWidgetCall11>(taken[11]);
      call(this, value, &handled);
      if (handled) return;
    }
    QTreeView::verticalScrollbarValueChanged(value);
  }

  //  void QTreeView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTreeWidgetCall12 call = reinterpret_cast<CuteQTreeWidgetCall12>(taken[12]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QTreeView::scrollContentsBy(dx, dy);
  }

  //  void QTreeView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTreeWidgetCall13 call = reinterpret_cast<CuteQTreeWidgetCall13>(taken[13]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QTreeView::rowsInserted(parent, start, end);
  }

  //  void QTreeView::rowsAboutToBeRemoved(const QModelIndex &parent, int
  //      start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTreeWidgetCall14 call = reinterpret_cast<CuteQTreeWidgetCall14>(taken[14]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QTreeView::rowsAboutToBeRemoved(parent, start, end);
  }

  //  int QTreeView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTreeWidgetCall15 call = reinterpret_cast<CuteQTreeWidgetCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTreeView::horizontalOffset();
  }

  //  int QTreeView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTreeWidgetCall16 call = reinterpret_cast<CuteQTreeWidgetCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTreeView::verticalOffset();
  }

  //  QRegion QTreeView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTreeWidgetCall17 call = reinterpret_cast<CuteQTreeWidgetCall17>(taken[17]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::visualRegionForSelection(selection);
  }

  //  void QTreeView::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTreeWidgetCall18 call = reinterpret_cast<CuteQTreeWidgetCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::changeEvent(event);
  }

  //  void QTreeView::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTreeWidgetCall19 call = reinterpret_cast<CuteQTreeWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::timerEvent(event);
  }

  //  void QTreeView::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTreeWidgetCall20 call = reinterpret_cast<CuteQTreeWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::paintEvent(event);
  }

  //  void QTreeView::drawRow(QPainter *painter, const QStyleOptionViewItem
  //      &options, const QModelIndex &index) const
  void drawRow(
      QPainter *painter,
      const QStyleOptionViewItem &options,
      const QModelIndex &index) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTreeWidgetCall21 call = reinterpret_cast<CuteQTreeWidgetCall21>(taken[21]);
      call(this, painter, &options, &index, &handled);
      if (handled) return;
    }
    QTreeView::drawRow(painter, options, index);
  }

  //  void QTreeView::drawBranches(QPainter *painter, const QRect &rect,
  //      const QModelIndex &index) const
  void drawBranches(
      QPainter *painter,
      const QRect &rect,
      const QModelIndex &index) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTreeWidgetCall22 call = reinterpret_cast<CuteQTreeWidgetCall22>(taken[22]);
      call(this, painter, &rect, &index, &handled);
      if (handled) return;
    }
    QTreeView::drawBranches(painter, rect, index);
  }

  //  void QTreeView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTreeWidgetCall23 call = reinterpret_cast<CuteQTreeWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mousePressEvent(event);
  }

  //  void QTreeView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTreeWidgetCall24 call = reinterpret_cast<CuteQTreeWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseReleaseEvent(event);
  }

  //  void QTreeView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTreeWidgetCall25 call = reinterpret_cast<CuteQTreeWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseDoubleClickEvent(event);
  }

  //  void QTreeView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTreeWidgetCall26 call = reinterpret_cast<CuteQTreeWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseMoveEvent(event);
  }

  //  void QTreeView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTreeWidgetCall27 call = reinterpret_cast<CuteQTreeWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::keyPressEvent(event);
  }

  //  void QTreeView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTreeWidgetCall28 call = reinterpret_cast<CuteQTreeWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::dragMoveEvent(event);
  }

  //  bool QTreeView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQTreeWidgetCall29 call = reinterpret_cast<CuteQTreeWidgetCall29>(taken[29]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QTreeView::viewportEvent(event);
  }

  //  void QTreeView::updateGeometries()
  void updateGeometries() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTreeWidgetCall30 call = reinterpret_cast<CuteQTreeWidgetCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::updateGeometries();
  }

  //  QSize QTreeView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQTreeWidgetCall31 call = reinterpret_cast<CuteQTreeWidgetCall31>(taken[31]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::viewportSizeHint();
  }

  //  int QTreeView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQTreeWidgetCall32 call = reinterpret_cast<CuteQTreeWidgetCall32>(taken[32]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QTreeView::sizeHintForColumn(column);
  }

  //  void QTreeView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTreeWidgetCall33 call = reinterpret_cast<CuteQTreeWidgetCall33>(taken[33]);
      call(this, action, &handled);
      if (handled) return;
    }
    QTreeView::horizontalScrollbarAction(action);
  }

  //  bool QTreeView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQTreeWidgetCall34 call = reinterpret_cast<CuteQTreeWidgetCall34>(taken[34]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTreeView::isIndexHidden(index);
  }

  //  void QTreeView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[35]) {
      int handled = 0;
      CuteQTreeWidgetCall35 call = reinterpret_cast<CuteQTreeWidgetCall35>(taken[35]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QTreeView::selectionChanged(selected, deselected);
  }

  //  void QTreeView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[36]) {
      int handled = 0;
      CuteQTreeWidgetCall36 call = reinterpret_cast<CuteQTreeWidgetCall36>(taken[36]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QTreeView::currentChanged(current, previous);
  }

  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQTreeWidgetCall37 call = reinterpret_cast<CuteQTreeWidgetCall37>(taken[37]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }

  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQTreeWidgetCall38 call = reinterpret_cast<CuteQTreeWidgetCall38>(taken[38]);
      void * given = call(this, &index, &handled);
      if (handled) return static_cast<QAbstractItemDelegate *>(given);
    }
    return QAbstractItemView::itemDelegateForIndex(index);
  }

  //  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQTreeWidgetCall39 call = reinterpret_cast<CuteQTreeWidgetCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }

  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[40]) {
      int handled = 0;
      CuteQTreeWidgetCall40 call = reinterpret_cast<CuteQTreeWidgetCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }

  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[41]) {
      int handled = 0;
      CuteQTreeWidgetCall41 call = reinterpret_cast<CuteQTreeWidgetCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }

  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTreeWidgetCall42 call = reinterpret_cast<CuteQTreeWidgetCall42>(taken[42]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }

  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[43]) {
      int handled = 0;
      CuteQTreeWidgetCall43 call = reinterpret_cast<CuteQTreeWidgetCall43>(taken[43]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarValueChanged(value);
  }

  //  void QAbstractItemView::closeEditor(QWidget *editor,
  //      QAbstractItemDelegate::EndEditHint hint)
  void closeEditor(
      QWidget *editor,
      QAbstractItemDelegate::EndEditHint hint) override {
    if (taken[44]) {
      int handled = 0;
      CuteQTreeWidgetCall44 call = reinterpret_cast<CuteQTreeWidgetCall44>(taken[44]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }

  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[45]) {
      int handled = 0;
      CuteQTreeWidgetCall45 call = reinterpret_cast<CuteQTreeWidgetCall45>(taken[45]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }

  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTreeWidgetCall46 call = reinterpret_cast<CuteQTreeWidgetCall46>(taken[46]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::editorDestroyed(editor);
  }

  //  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
  //      trigger, QEvent *event)
  bool edit(
      const QModelIndex &index,
      QAbstractItemView::EditTrigger trigger,
      QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTreeWidgetCall47 call = reinterpret_cast<CuteQTreeWidgetCall47>(taken[47]);
      bool given = call(this, &index, static_cast<int>(trigger), event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::edit(index, trigger, event);
  }

  //  void QAbstractItemView::initViewItemOption(QStyleOptionViewItem
  //      *option) const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQTreeWidgetCall48 call = reinterpret_cast<CuteQTreeWidgetCall48>(taken[48]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractItemView::initViewItemOption(option);
  }

  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[49]) {
      int handled = 0;
      CuteQTreeWidgetCall49 call = reinterpret_cast<CuteQTreeWidgetCall49>(taken[49]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }

  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQTreeWidgetCall50 call = reinterpret_cast<CuteQTreeWidgetCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }

  //  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQTreeWidgetCall51 call = reinterpret_cast<CuteQTreeWidgetCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragLeaveEvent(event);
  }

  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQTreeWidgetCall52 call = reinterpret_cast<CuteQTreeWidgetCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }

  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQTreeWidgetCall53 call = reinterpret_cast<CuteQTreeWidgetCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }

  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQTreeWidgetCall54 call = reinterpret_cast<CuteQTreeWidgetCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::resizeEvent(event);
  }

  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQTreeWidgetCall55 call = reinterpret_cast<CuteQTreeWidgetCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::inputMethodEvent(event);
  }

  //  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQTreeWidgetCall56 call = reinterpret_cast<CuteQTreeWidgetCall56>(taken[56]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[57]) {
      int handled = 0;
      CuteQTreeWidgetCall57 call = reinterpret_cast<CuteQTreeWidgetCall57>(taken[57]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[58]) {
      int handled = 0;
      CuteQTreeWidgetCall58 call = reinterpret_cast<CuteQTreeWidgetCall58>(taken[58]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }

  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[59]) {
      int handled = 0;
      CuteQTreeWidgetCall59 call = reinterpret_cast<CuteQTreeWidgetCall59>(taken[59]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }

  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQTreeWidgetCall60 call = reinterpret_cast<CuteQTreeWidgetCall60>(taken[60]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }

  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQTreeWidgetCall61 call = reinterpret_cast<CuteQTreeWidgetCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[62]) {
      int handled = 0;
      CuteQTreeWidgetCall62 call = reinterpret_cast<CuteQTreeWidgetCall62>(taken[62]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[63]) {
      int handled = 0;
      CuteQTreeWidgetCall63 call = reinterpret_cast<CuteQTreeWidgetCall63>(taken[63]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[64]) {
      int handled = 0;
      CuteQTreeWidgetCall64 call = reinterpret_cast<CuteQTreeWidgetCall64>(taken[64]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[65]) {
      int handled = 0;
      CuteQTreeWidgetCall65 call = reinterpret_cast<CuteQTreeWidgetCall65>(taken[65]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[66]) {
      int handled = 0;
      CuteQTreeWidgetCall66 call = reinterpret_cast<CuteQTreeWidgetCall66>(taken[66]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[67]) {
      int handled = 0;
      CuteQTreeWidgetCall67 call = reinterpret_cast<CuteQTreeWidgetCall67>(taken[67]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[68]) {
      int handled = 0;
      CuteQTreeWidgetCall68 call = reinterpret_cast<CuteQTreeWidgetCall68>(taken[68]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[69]) {
      int handled = 0;
      CuteQTreeWidgetCall69 call = reinterpret_cast<CuteQTreeWidgetCall69>(taken[69]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQTreeWidgetCall70 call = reinterpret_cast<CuteQTreeWidgetCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQTreeWidgetCall71 call = reinterpret_cast<CuteQTreeWidgetCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQTreeWidgetCall72 call = reinterpret_cast<CuteQTreeWidgetCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQTreeWidgetCall73 call = reinterpret_cast<CuteQTreeWidgetCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQTreeWidgetCall74 call = reinterpret_cast<CuteQTreeWidgetCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQTreeWidgetCall75 call = reinterpret_cast<CuteQTreeWidgetCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQTreeWidgetCall76 call = reinterpret_cast<CuteQTreeWidgetCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[77]) {
      int handled = 0;
      CuteQTreeWidgetCall77 call = reinterpret_cast<CuteQTreeWidgetCall77>(taken[77]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[78]) {
      int handled = 0;
      CuteQTreeWidgetCall78 call = reinterpret_cast<CuteQTreeWidgetCall78>(taken[78]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQTreeWidgetCall79 call = reinterpret_cast<CuteQTreeWidgetCall79>(taken[79]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[80]) {
      int handled = 0;
      CuteQTreeWidgetCall80 call = reinterpret_cast<CuteQTreeWidgetCall80>(taken[80]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[81]) {
      int handled = 0;
      CuteQTreeWidgetCall81 call = reinterpret_cast<CuteQTreeWidgetCall81>(taken[81]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[82]) {
      int handled = 0;
      CuteQTreeWidgetCall82 call = reinterpret_cast<CuteQTreeWidgetCall82>(taken[82]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[83]) {
      int handled = 0;
      CuteQTreeWidgetCall83 call = reinterpret_cast<CuteQTreeWidgetCall83>(taken[83]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[84]) {
      int handled = 0;
      CuteQTreeWidgetCall84 call = reinterpret_cast<CuteQTreeWidgetCall84>(taken[84]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTreeWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTreeWidget10metaObjectEv(
    const QTreeWidget *self) {
  return self->metaObject();
}

//  QString QTreeWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTreeWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTreeWidget::tr(s, c, n));
}

//  QTreeWidget::QTreeWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTreeWidget *ritual_ZN11QTreeWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQTreeWidget(parent);
}

//  QTreeWidget::~QTreeWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidgetD1Ev(QTreeWidget *self) {
  delete self;
}

//  int QTreeWidget::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget11columnCountEv(const QTreeWidget *self) {
  return self->columnCount();
}

//  void QTreeWidget::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setColumnCountEi(
    QTreeWidget *self,
    int columns) {
  self->setColumnCount(columns);
}

//  QTreeWidgetItem *QTreeWidget::invisibleRootItem() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget17invisibleRootItemEv(
    const QTreeWidget *self) {
  return self->invisibleRootItem();
}

//  QTreeWidgetItem *QTreeWidget::topLevelItem(int index) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget12topLevelItemEi(
    const QTreeWidget *self,
    int index) {
  return self->topLevelItem(index);
}

//  int QTreeWidget::topLevelItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget17topLevelItemCountEv(const QTreeWidget *self) {
  return self->topLevelItemCount();
}

//  void QTreeWidget::insertTopLevelItem(int index, QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget18insertTopLevelItemEiP15QTreeWidgetItem(
    QTreeWidget *self,
    int index,
    QTreeWidgetItem *item) {
  self->insertTopLevelItem(index, item);
}

//  void QTreeWidget::addTopLevelItem(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget15addTopLevelItemEP15QTreeWidgetItem(
    QTreeWidget *self,
    QTreeWidgetItem *item) {
  self->addTopLevelItem(item);
}

//  QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN11QTreeWidget16takeTopLevelItemEi(
    QTreeWidget *self,
    int index) {
  return self->takeTopLevelItem(index);
}

//  int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget19indexOfTopLevelItemEP15QTreeWidgetItem(
    const QTreeWidget *self,
    QTreeWidgetItem *item) {
  return self->indexOfTopLevelItem(item);
}

//  QTreeWidgetItem *QTreeWidget::headerItem() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget10headerItemEv(
    const QTreeWidget *self) {
  return self->headerItem();
}

//  void QTreeWidget::setHeaderItem(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget13setHeaderItemEP15QTreeWidgetItem(
    QTreeWidget *self,
    QTreeWidgetItem *item) {
  self->setHeaderItem(item);
}

//  void QTreeWidget::setHeaderLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setHeaderLabelERK7QString(
    QTreeWidget *self,
    const QString *label) {
  self->setHeaderLabel(*label);
}

//  QTreeWidgetItem *QTreeWidget::currentItem() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget11currentItemEv(
    const QTreeWidget *self) {
  return self->currentItem();
}

//  int QTreeWidget::currentColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget13currentColumnEv(const QTreeWidget *self) {
  return self->currentColumn();
}

//  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItem(
    QTreeWidget *self,
    QTreeWidgetItem *item) {
  self->setCurrentItem(item);
}

//  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->setCurrentItem(item, column);
}

//  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column,
    int command) {
  self->setCurrentItem(
      item,
      column,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QTreeWidgetItem *QTreeWidget::itemAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget6itemAtERK6QPoint(
    const QTreeWidget *self,
    const QPoint *p) {
  return self->itemAt(*p);
}

//  QTreeWidgetItem *QTreeWidget::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget6itemAtEii(
    const QTreeWidget *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QRect QTreeWidget::visualItemRect(const QTreeWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QTreeWidget14visualItemRectEPK15QTreeWidgetItem(
    const QTreeWidget *self,
    const QTreeWidgetItem *item) {
  return new QRect(self->visualItemRect(item));
}

//  int QTreeWidget::sortColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget10sortColumnEv(const QTreeWidget *self) {
  return self->sortColumn();
}

//  void QTreeWidget::sortItems(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget9sortItemsEiN2Qt9SortOrderE(
    QTreeWidget *self,
    int column,
    Qt::SortOrder order) {
  self->sortItems(column, order);
}

//  void QTreeWidget::editItem(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget8editItemEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->editItem(item, column);
}

//  void QTreeWidget::openPersistentEditor(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget20openPersistentEditorEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->openPersistentEditor(item, column);
}

//  void QTreeWidget::closePersistentEditor(QTreeWidgetItem *item, int
//      column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget21closePersistentEditorEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->closePersistentEditor(item, column);
}

//  bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem *item, int
//      column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTreeWidget22isPersistentEditorOpenEP15QTreeWidgetItemi(
    const QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  return self->isPersistentEditorOpen(item, column);
}

//  QWidget *QTreeWidget::itemWidget(QTreeWidgetItem *item, int column) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QTreeWidget10itemWidgetEP15QTreeWidgetItemi(
    const QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  return self->itemWidget(item, column);
}

//  void QTreeWidget::setItemWidget(QTreeWidgetItem *item, int column,
//      QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget13setItemWidgetEP15QTreeWidgetItemiP7QWidget(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column,
    QWidget *widget) {
  self->setItemWidget(item, column, widget);
}

//  void QTreeWidget::removeItemWidget(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget16removeItemWidgetEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->removeItemWidget(item, column);
}

//  QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget9itemAboveEPK15QTreeWidgetItem(
    const QTreeWidget *self,
    const QTreeWidgetItem *item) {
  return self->itemAbove(item);
}

//  QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget9itemBelowEPK15QTreeWidgetItem(
    const QTreeWidget *self,
    const QTreeWidgetItem *item) {
  return self->itemBelow(item);
}

//  QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem *item, int
//      column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QTreeWidget13indexFromItemEPK15QTreeWidgetItemi(
    const QTreeWidget *self,
    const QTreeWidgetItem *item,
    int column) {
  return new QModelIndex(self->indexFromItem(item, column));
}

//  QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget13itemFromIndexERK11QModelIndex(
    const QTreeWidget *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  void QTreeWidget::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget17setSelectionModelEP19QItemSelectionModel(
    QTreeWidget *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  Qt::DropActions QTreeWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget20supportedDragActionsEv(
    const QTreeWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QTreeWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QTreeWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QTreeWidget::scrollToItem(const QTreeWidgetItem *item,
//      QAbstractItemView::ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget12scrollToItemEPK15QTreeWidgetItemN17QAbstractItemView10ScrollHintE(
    QTreeWidget *self,
    const QTreeWidgetItem *item,
    QAbstractItemView::ScrollHint hint) {
  self->scrollToItem(item, hint);
}

//  void QTreeWidget::expandItem(const QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget10expandItemEPK15QTreeWidgetItem(
    QTreeWidget *self,
    const QTreeWidgetItem *item) {
  self->expandItem(item);
}

//  void QTreeWidget::collapseItem(const QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget12collapseItemEPK15QTreeWidgetItem(
    QTreeWidget *self,
    const QTreeWidgetItem *item) {
  self->collapseItem(item);
}

//  void QTreeWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget5clearEv(QTreeWidget *self) {
  self->clear();
}

//  a Python function taken by a CuteQTreeWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeWidget(
    QTreeWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTreeWidget *>(self)->take(key, call);
}

//  void QTreeWidget::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTreeWidget17setSelectionModelEP19QItemSelectionModel(
    QTreeWidget *self,
    QItemSelectionModel *selectionModel) {
  self->QTreeWidget::setSelectionModel(selectionModel);
}

//  bool QTreeWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTreeWidget5eventEP6QEvent(
    QTreeWidget *self,
    QEvent *e) {
  return static_cast<OwnQTreeWidget *>(self)->OwnQTreeWidget::event(e);
}

//  bool QTreeWidget::dropMimeData(QTreeWidgetItem *parent, int index, const
//      QMimeData *data, Qt::DropAction action)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTreeWidget12dropMimeDataEP15QTreeWidgetItemiPK9QMimeDataN2Qt10DropActionE(
    QTreeWidget *self,
    QTreeWidgetItem *parent,
    int index,
    const QMimeData *data,
    Qt::DropAction action) {
  return static_cast<OwnQTreeWidget *>(self)->OwnQTreeWidget::dropMimeData(
      parent,
      index,
      data,
      action);
}

//  void QTreeWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTreeWidget9dropEventEP10QDropEvent(
    QTreeWidget *self,
    QDropEvent *event) {
  static_cast<OwnQTreeWidget *>(self)->OwnQTreeWidget::dropEvent(event);
}
