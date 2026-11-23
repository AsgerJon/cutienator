//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtableview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtableview.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTableView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTableView : QTableView {
  using QTableView::scrollContentsBy;
  using QTableView::initViewItemOption;
  using QTableView::paintEvent;
  using QTableView::timerEvent;
  using QTableView::dropEvent;
  using QTableView::horizontalOffset;
  using QTableView::verticalOffset;
  using QTableView::setSelection;
  using QTableView::visualRegionForSelection;
  using QTableView::updateGeometries;
  using QTableView::viewportSizeHint;
  using QTableView::sizeHintForRow;
  using QTableView::sizeHintForColumn;
  using QTableView::verticalScrollbarAction;
  using QTableView::horizontalScrollbarAction;
  using QTableView::isIndexHidden;
  using QTableView::selectionChanged;
  using QTableView::currentChanged;
};

//  A QTableView that Python can take functions over in. Every QTableView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTableViewCall0)(const void *, QAbstractItemModel *, int *);
typedef void (*CuteQTableViewCall1)(const void *, const QModelIndex *, int *);
typedef void (*CuteQTableViewCall2)(const void *, QItemSelectionModel *, int *);
typedef void (*CuteQTableViewCall3)(const void *, int *);
typedef const QRect * (*CuteQTableViewCall4)(const void *, const QModelIndex *, int *);
typedef void (*CuteQTableViewCall5)(const void *, const QModelIndex *, int, int *);
typedef const QModelIndex * (*CuteQTableViewCall6)(const void *, const QPoint *, int *);
typedef void (*CuteQTableViewCall7)(const void *, int, int, int *);
typedef void (*CuteQTableViewCall8)(const void *, QStyleOptionViewItem *, int *);
typedef void (*CuteQTableViewCall9)(const void *, QPaintEvent *, int *);
typedef void (*CuteQTableViewCall10)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTableViewCall11)(const void *, QDropEvent *, int *);
typedef int (*CuteQTableViewCall12)(const void *, int *);
typedef int (*CuteQTableViewCall13)(const void *, int *);
typedef void (*CuteQTableViewCall14)(const void *, const QRect *, int, int *);
typedef const QRegion * (*CuteQTableViewCall15)(const void *, const QItemSelection *, int *);
typedef void (*CuteQTableViewCall16)(const void *, int *);
typedef const QSize * (*CuteQTableViewCall17)(const void *, int *);
typedef int (*CuteQTableViewCall18)(const void *, int, int *);
typedef int (*CuteQTableViewCall19)(const void *, int, int *);
typedef void (*CuteQTableViewCall20)(const void *, int, int *);
typedef void (*CuteQTableViewCall21)(const void *, int, int *);
typedef bool (*CuteQTableViewCall22)(const void *, const QModelIndex *, int *);
typedef void (*CuteQTableViewCall23)(const void *, const QItemSelection *, const QItemSelection *, int *);
typedef void (*CuteQTableViewCall24)(const void *, const QModelIndex *, const QModelIndex *, int *);
typedef void (*CuteQTableViewCall25)(const void *, const QString *, int *);
typedef void * (*CuteQTableViewCall26)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQTableViewCall27)(const void *, int, int *);
typedef void (*CuteQTableViewCall28)(const void *, int *);
typedef void (*CuteQTableViewCall29)(const void *, int *);
typedef void (*CuteQTableViewCall30)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQTableViewCall31)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQTableViewCall32)(const void *, int *);
typedef void (*CuteQTableViewCall33)(const void *, int *);
typedef void (*CuteQTableViewCall34)(const void *, int, int *);
typedef void (*CuteQTableViewCall35)(const void *, int, int *);
typedef void (*CuteQTableViewCall36)(const void *, QWidget *, int, int *);
typedef void (*CuteQTableViewCall37)(const void *, QWidget *, int *);
typedef void (*CuteQTableViewCall38)(const void *, QObject *, int *);
typedef bool (*CuteQTableViewCall39)(const void *, const QModelIndex *, int, QEvent *, int *);
typedef int (*CuteQTableViewCall40)(const void *, const QModelIndex *, const QEvent *, int *);
typedef void (*CuteQTableViewCall41)(const void *, int, int *);
typedef bool (*CuteQTableViewCall42)(const void *, bool, int *);
typedef bool (*CuteQTableViewCall43)(const void *, QEvent *, int *);
typedef bool (*CuteQTableViewCall44)(const void *, QEvent *, int *);
typedef void (*CuteQTableViewCall45)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTableViewCall46)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTableViewCall47)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTableViewCall48)(const void *, QMouseEvent *, int *);
typedef void (*CuteQTableViewCall49)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQTableViewCall50)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQTableViewCall51)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQTableViewCall52)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTableViewCall53)(const void *, QFocusEvent *, int *);
typedef void (*CuteQTableViewCall54)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTableViewCall55)(const void *, QResizeEvent *, int *);
typedef void (*CuteQTableViewCall56)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQTableViewCall57)(const void *, QObject *, QEvent *, int *);
typedef const QSize * (*CuteQTableViewCall58)(const void *, int *);
typedef const QSize * (*CuteQTableViewCall59)(const void *, int *);
typedef void (*CuteQTableViewCall60)(const void *, QWidget *, int *);
typedef void (*CuteQTableViewCall61)(const void *, QWheelEvent *, int *);
typedef void (*CuteQTableViewCall62)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQTableViewCall63)(const void *, QEvent *, int *);
typedef void (*CuteQTableViewCall64)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTableViewCall65)(const void *, int *);
typedef void (*CuteQTableViewCall66)(const void *, bool, int *);
typedef int (*CuteQTableViewCall67)(const void *, int, int *);
typedef bool (*CuteQTableViewCall68)(const void *, int *);
typedef void * (*CuteQTableViewCall69)(const void *, int *);
typedef void (*CuteQTableViewCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTableViewCall71)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTableViewCall72)(const void *, QEvent *, int *);
typedef void (*CuteQTableViewCall73)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTableViewCall74)(const void *, QCloseEvent *, int *);
typedef void (*CuteQTableViewCall75)(const void *, QTabletEvent *, int *);
typedef void (*CuteQTableViewCall76)(const void *, QActionEvent *, int *);
typedef void (*CuteQTableViewCall77)(const void *, QShowEvent *, int *);
typedef void (*CuteQTableViewCall78)(const void *, QHideEvent *, int *);
typedef int (*CuteQTableViewCall79)(const void *, int, int *);
typedef void (*CuteQTableViewCall80)(const void *, QPainter *, int *);
typedef void * (*CuteQTableViewCall81)(const void *, QPoint *, int *);
typedef void * (*CuteQTableViewCall82)(const void *, int *);
typedef void (*CuteQTableViewCall83)(const void *, QChildEvent *, int *);
typedef void (*CuteQTableViewCall84)(const void *, QEvent *, int *);
typedef void (*CuteQTableViewCall85)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTableViewCall86)(const void *, const QMetaMethod *, int *);
class CuteQTableView : public QTableView {
public:
  using QTableView::QTableView;
  void *taken[87] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[86] = call;
      return true;
    }
    return false;
  }

  //  void QTableView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTableViewCall0 call = reinterpret_cast<CuteQTableViewCall0>(taken[0]);
      call(this, model, &handled);
      if (handled) return;
    }
    QTableView::setModel(model);
  }

  //  void QTableView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTableViewCall1 call = reinterpret_cast<CuteQTableViewCall1>(taken[1]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QTableView::setRootIndex(index);
  }

  //  void QTableView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTableViewCall2 call = reinterpret_cast<CuteQTableViewCall2>(taken[2]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QTableView::setSelectionModel(selectionModel);
  }

  //  void QTableView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTableViewCall3 call = reinterpret_cast<CuteQTableViewCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTableView::doItemsLayout();
  }

  //  QRect QTableView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTableViewCall4 call = reinterpret_cast<CuteQTableViewCall4>(taken[4]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTableView::visualRect(index);
  }

  //  void QTableView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTableViewCall5 call = reinterpret_cast<CuteQTableViewCall5>(taken[5]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QTableView::scrollTo(index, hint);
  }

  //  QModelIndex QTableView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTableViewCall6 call = reinterpret_cast<CuteQTableViewCall6>(taken[6]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QTableView::indexAt(p);
  }

  //  void QTableView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTableViewCall7 call = reinterpret_cast<CuteQTableViewCall7>(taken[7]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QTableView::scrollContentsBy(dx, dy);
  }

  //  void QTableView::initViewItemOption(QStyleOptionViewItem *option)
  //      const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTableViewCall8 call = reinterpret_cast<CuteQTableViewCall8>(taken[8]);
      call(this, option, &handled);
      if (handled) return;
    }
    QTableView::initViewItemOption(option);
  }

  //  void QTableView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTableViewCall9 call = reinterpret_cast<CuteQTableViewCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTableView::paintEvent(e);
  }

  //  void QTableView::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTableViewCall10 call = reinterpret_cast<CuteQTableViewCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTableView::timerEvent(event);
  }

  //  void QTableView::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTableViewCall11 call = reinterpret_cast<CuteQTableViewCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTableView::dropEvent(event);
  }

  //  int QTableView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTableViewCall12 call = reinterpret_cast<CuteQTableViewCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTableView::horizontalOffset();
  }

  //  int QTableView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTableViewCall13 call = reinterpret_cast<CuteQTableViewCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTableView::verticalOffset();
  }

  //  void QTableView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTableViewCall14 call = reinterpret_cast<CuteQTableViewCall14>(taken[14]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QTableView::setSelection(rect, command);
  }

  //  QRegion QTableView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTableViewCall15 call = reinterpret_cast<CuteQTableViewCall15>(taken[15]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QTableView::visualRegionForSelection(selection);
  }

  //  void QTableView::updateGeometries()
  void updateGeometries() override {
    if (taken[16]) {
      int handled = 0;
      CuteQTableViewCall16 call = reinterpret_cast<CuteQTableViewCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QTableView::updateGeometries();
  }

  //  QSize QTableView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTableViewCall17 call = reinterpret_cast<CuteQTableViewCall17>(taken[17]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTableView::viewportSizeHint();
  }

  //  int QTableView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTableViewCall18 call = reinterpret_cast<CuteQTableViewCall18>(taken[18]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QTableView::sizeHintForRow(row);
  }

  //  int QTableView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQTableViewCall19 call = reinterpret_cast<CuteQTableViewCall19>(taken[19]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QTableView::sizeHintForColumn(column);
  }

  //  void QTableView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTableViewCall20 call = reinterpret_cast<CuteQTableViewCall20>(taken[20]);
      call(this, action, &handled);
      if (handled) return;
    }
    QTableView::verticalScrollbarAction(action);
  }

  //  void QTableView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTableViewCall21 call = reinterpret_cast<CuteQTableViewCall21>(taken[21]);
      call(this, action, &handled);
      if (handled) return;
    }
    QTableView::horizontalScrollbarAction(action);
  }

  //  bool QTableView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTableViewCall22 call = reinterpret_cast<CuteQTableViewCall22>(taken[22]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTableView::isIndexHidden(index);
  }

  //  void QTableView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTableViewCall23 call = reinterpret_cast<CuteQTableViewCall23>(taken[23]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QTableView::selectionChanged(selected, deselected);
  }

  //  void QTableView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTableViewCall24 call = reinterpret_cast<CuteQTableViewCall24>(taken[24]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QTableView::currentChanged(current, previous);
  }

  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTableViewCall25 call = reinterpret_cast<CuteQTableViewCall25>(taken[25]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }

  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQTableViewCall26 call = reinterpret_cast<CuteQTableViewCall26>(taken[26]);
      void * given = call(this, &index, &handled);
      if (handled) return static_cast<QAbstractItemDelegate *>(given);
    }
    return QAbstractItemView::itemDelegateForIndex(index);
  }

  //  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQTableViewCall27 call = reinterpret_cast<CuteQTableViewCall27>(taken[27]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }

  //  void QAbstractItemView::reset()
  void reset() override {
    if (taken[28]) {
      int handled = 0;
      CuteQTableViewCall28 call = reinterpret_cast<CuteQTableViewCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::reset();
  }

  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTableViewCall29 call = reinterpret_cast<CuteQTableViewCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectAll();
  }

  //  void QAbstractItemView::rowsInserted(const QModelIndex &parent, int
  //      start, int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[30]) {
      int handled = 0;
      CuteQTableViewCall30 call = reinterpret_cast<CuteQTableViewCall30>(taken[30]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemView::rowsInserted(parent, start, end);
  }

  //  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex
  //      &parent, int start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTableViewCall31 call = reinterpret_cast<CuteQTableViewCall31>(taken[31]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemView::rowsAboutToBeRemoved(parent, start, end);
  }

  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[32]) {
      int handled = 0;
      CuteQTableViewCall32 call = reinterpret_cast<CuteQTableViewCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }

  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[33]) {
      int handled = 0;
      CuteQTableViewCall33 call = reinterpret_cast<CuteQTableViewCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }

  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[34]) {
      int handled = 0;
      CuteQTableViewCall34 call = reinterpret_cast<CuteQTableViewCall34>(taken[34]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }

  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[35]) {
      int handled = 0;
      CuteQTableViewCall35 call = reinterpret_cast<CuteQTableViewCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQTableViewCall36 call = reinterpret_cast<CuteQTableViewCall36>(taken[36]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }

  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTableViewCall37 call = reinterpret_cast<CuteQTableViewCall37>(taken[37]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }

  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[38]) {
      int handled = 0;
      CuteQTableViewCall38 call = reinterpret_cast<CuteQTableViewCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CuteQTableViewCall39 call = reinterpret_cast<CuteQTableViewCall39>(taken[39]);
      bool given = call(this, &index, static_cast<int>(trigger), event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::edit(index, trigger, event);
  }

  //  QItemSelectionModel::SelectionFlags
  //      QAbstractItemView::selectionCommand(const QModelIndex &index,
  //      const QEvent *event) const
  QItemSelectionModel::SelectionFlags selectionCommand(
      const QModelIndex &index,
      const QEvent *event) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQTableViewCall40 call = reinterpret_cast<CuteQTableViewCall40>(taken[40]);
      int given = call(this, &index, event, &handled);
      if (handled) return QFlags<QItemSelectionModel::SelectionFlag>::fromInt(given);
    }
    return QAbstractItemView::selectionCommand(index, event);
  }

  //  void QAbstractItemView::startDrag(Qt::DropActions supportedActions)
  void startDrag(Qt::DropActions supportedActions) override {
    if (taken[41]) {
      int handled = 0;
      CuteQTableViewCall41 call = reinterpret_cast<CuteQTableViewCall41>(taken[41]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QAbstractItemView::startDrag(supportedActions);
  }

  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTableViewCall42 call = reinterpret_cast<CuteQTableViewCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }

  //  bool QAbstractItemView::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQTableViewCall43 call = reinterpret_cast<CuteQTableViewCall43>(taken[43]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::event(event);
  }

  //  bool QAbstractItemView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQTableViewCall44 call = reinterpret_cast<CuteQTableViewCall44>(taken[44]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::viewportEvent(event);
  }

  //  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQTableViewCall45 call = reinterpret_cast<CuteQTableViewCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }

  //  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTableViewCall46 call = reinterpret_cast<CuteQTableViewCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseMoveEvent(event);
  }

  //  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTableViewCall47 call = reinterpret_cast<CuteQTableViewCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseReleaseEvent(event);
  }

  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQTableViewCall48 call = reinterpret_cast<CuteQTableViewCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseDoubleClickEvent(event);
  }

  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQTableViewCall49 call = reinterpret_cast<CuteQTableViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }

  //  void QAbstractItemView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQTableViewCall50 call = reinterpret_cast<CuteQTableViewCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragMoveEvent(event);
  }

  //  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQTableViewCall51 call = reinterpret_cast<CuteQTableViewCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragLeaveEvent(event);
  }

  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQTableViewCall52 call = reinterpret_cast<CuteQTableViewCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }

  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQTableViewCall53 call = reinterpret_cast<CuteQTableViewCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }

  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQTableViewCall54 call = reinterpret_cast<CuteQTableViewCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }

  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQTableViewCall55 call = reinterpret_cast<CuteQTableViewCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::resizeEvent(event);
  }

  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQTableViewCall56 call = reinterpret_cast<CuteQTableViewCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::inputMethodEvent(event);
  }

  //  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQTableViewCall57 call = reinterpret_cast<CuteQTableViewCall57>(taken[57]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[58]) {
      int handled = 0;
      CuteQTableViewCall58 call = reinterpret_cast<CuteQTableViewCall58>(taken[58]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[59]) {
      int handled = 0;
      CuteQTableViewCall59 call = reinterpret_cast<CuteQTableViewCall59>(taken[59]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }

  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[60]) {
      int handled = 0;
      CuteQTableViewCall60 call = reinterpret_cast<CuteQTableViewCall60>(taken[60]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }

  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQTableViewCall61 call = reinterpret_cast<CuteQTableViewCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }

  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQTableViewCall62 call = reinterpret_cast<CuteQTableViewCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQTableViewCall63 call = reinterpret_cast<CuteQTableViewCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[64]) {
      int handled = 0;
      CuteQTableViewCall64 call = reinterpret_cast<CuteQTableViewCall64>(taken[64]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQTableViewCall65 call = reinterpret_cast<CuteQTableViewCall65>(taken[65]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[66]) {
      int handled = 0;
      CuteQTableViewCall66 call = reinterpret_cast<CuteQTableViewCall66>(taken[66]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[67]) {
      int handled = 0;
      CuteQTableViewCall67 call = reinterpret_cast<CuteQTableViewCall67>(taken[67]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[68]) {
      int handled = 0;
      CuteQTableViewCall68 call = reinterpret_cast<CuteQTableViewCall68>(taken[68]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQTableViewCall69 call = reinterpret_cast<CuteQTableViewCall69>(taken[69]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQTableViewCall70 call = reinterpret_cast<CuteQTableViewCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQTableViewCall71 call = reinterpret_cast<CuteQTableViewCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQTableViewCall72 call = reinterpret_cast<CuteQTableViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQTableViewCall73 call = reinterpret_cast<CuteQTableViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQTableViewCall74 call = reinterpret_cast<CuteQTableViewCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQTableViewCall75 call = reinterpret_cast<CuteQTableViewCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQTableViewCall76 call = reinterpret_cast<CuteQTableViewCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQTableViewCall77 call = reinterpret_cast<CuteQTableViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQTableViewCall78 call = reinterpret_cast<CuteQTableViewCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQTableViewCall79 call = reinterpret_cast<CuteQTableViewCall79>(taken[79]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQTableViewCall80 call = reinterpret_cast<CuteQTableViewCall80>(taken[80]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQTableViewCall81 call = reinterpret_cast<CuteQTableViewCall81>(taken[81]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[82]) {
      int handled = 0;
      CuteQTableViewCall82 call = reinterpret_cast<CuteQTableViewCall82>(taken[82]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[83]) {
      int handled = 0;
      CuteQTableViewCall83 call = reinterpret_cast<CuteQTableViewCall83>(taken[83]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      CuteQTableViewCall84 call = reinterpret_cast<CuteQTableViewCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[85]) {
      int handled = 0;
      CuteQTableViewCall85 call = reinterpret_cast<CuteQTableViewCall85>(taken[85]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[86]) {
      int handled = 0;
      CuteQTableViewCall86 call = reinterpret_cast<CuteQTableViewCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

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
  return new CuteQTableView(parent);
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

//  void QTableView::rowMoved(int row, int oldIndex, int newIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView8rowMovedEiii(
    QTableView *self,
    int row,
    int oldIndex,
    int newIndex) {
  self->rowMoved(row, oldIndex, newIndex);
}

//  void QTableView::columnMoved(int column, int oldIndex, int newIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView11columnMovedEiii(
    QTableView *self,
    int column,
    int oldIndex,
    int newIndex) {
  self->columnMoved(column, oldIndex, newIndex);
}

//  void QTableView::rowResized(int row, int oldHeight, int newHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView10rowResizedEiii(
    QTableView *self,
    int row,
    int oldHeight,
    int newHeight) {
  self->rowResized(row, oldHeight, newHeight);
}

//  void QTableView::columnResized(int column, int oldWidth, int newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView13columnResizedEiii(
    QTableView *self,
    int column,
    int oldWidth,
    int newWidth) {
  self->columnResized(column, oldWidth, newWidth);
}

//  void QTableView::rowCountChanged(int oldCount, int newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView15rowCountChangedEii(
    QTableView *self,
    int oldCount,
    int newCount) {
  self->rowCountChanged(oldCount, newCount);
}

//  void QTableView::columnCountChanged(int oldCount, int newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView18columnCountChangedEii(
    QTableView *self,
    int oldCount,
    int newCount) {
  self->columnCountChanged(oldCount, newCount);
}

//  void QTableView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView16scrollContentsByEii(
    QTableView *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QTableView::initViewItemOption(QStyleOptionViewItem *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QTableView18initViewItemOptionEP20QStyleOptionViewItem(
    const QTableView *self,
    QStyleOptionViewItem *option) {
  self->initViewItemOption(option);
}

//  void QTableView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView10paintEventEP11QPaintEvent(
    QTableView *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QTableView::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView10timerEventEP11QTimerEvent(
    QTableView *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QTableView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView9dropEventEP10QDropEvent(
    QTableView *self,
    QDropEvent *event) {
  self->dropEvent(event);
}

//  int QTableView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView16horizontalOffsetEv(const QTableView *self) {
  return self->horizontalOffset();
}

//  int QTableView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView14verticalOffsetEv(const QTableView *self) {
  return self->verticalOffset();
}

//  QModelIndex QTableView::moveCursor(CursorAction cursorAction,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN10QTableView10moveCursorEN17QAbstractItemView12CursorActionE6QFlagsIN2Qt16KeyboardModifierEE(
    QTableView *self,
    QAbstractItemView::CursorAction cursorAction,
    int modifiers) {
  return new QModelIndex(
      self->moveCursor(
          cursorAction,
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}

//  void QTableView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTableView *self,
    const QRect *rect,
    int command) {
  self->setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QTableView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK10QTableView24visualRegionForSelectionERK14QItemSelection(
    const QTableView *self,
    const QItemSelection *selection) {
  return new QRegion(self->visualRegionForSelection(*selection));
}

//  QModelIndexList QTableView::selectedIndexes() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK10QTableView15selectedIndexesEv(
    const QTableView *self) {
  return new QList<QModelIndex>(self->selectedIndexes());
}

//  void QTableView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView16updateGeometriesEv(QTableView *self) {
  self->updateGeometries();
}

//  QSize QTableView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QTableView16viewportSizeHintEv(const QTableView *self) {
  return new QSize(self->viewportSizeHint());
}

//  int QTableView::sizeHintForRow(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView14sizeHintForRowEi(
    const QTableView *self,
    int row) {
  return self->sizeHintForRow(row);
}

//  int QTableView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView17sizeHintForColumnEi(
    const QTableView *self,
    int column) {
  return self->sizeHintForColumn(column);
}

//  void QTableView::verticalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView23verticalScrollbarActionEi(
    QTableView *self,
    int action) {
  self->verticalScrollbarAction(action);
}

//  void QTableView::horizontalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView25horizontalScrollbarActionEi(
    QTableView *self,
    int action) {
  self->horizontalScrollbarAction(action);
}

//  bool QTableView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTableView13isIndexHiddenERK11QModelIndex(
    const QTableView *self,
    const QModelIndex *index) {
  return self->isIndexHidden(*index);
}

//  void QTableView::selectionChanged(const QItemSelection &selected, const
//      QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView16selectionChangedERK14QItemSelectionS2_(
    QTableView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  self->selectionChanged(*selected, *deselected);
}

//  void QTableView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTableView14currentChangedERK11QModelIndexS2_(
    QTableView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  self->currentChanged(*current, *previous);
}

//  int QTableView::visualIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTableView11visualIndexERK11QModelIndex(
    const QTableView *self,
    const QModelIndex *index) {
  return self->visualIndex(*index);
}

//  a Python function taken by a CuteQTableView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableView(QTableView *self, const char *key, void *call) {
  return static_cast<CuteQTableView *>(self)->take(key, call);
}

//  void QTableView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView8setModelEP18QAbstractItemModel(
    QTableView *self,
    QAbstractItemModel *model) {
  self->QTableView::setModel(model);
}

//  void QTableView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView12setRootIndexERK11QModelIndex(
    QTableView *self,
    const QModelIndex *index) {
  self->QTableView::setRootIndex(*index);
}

//  void QTableView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView17setSelectionModelEP19QItemSelectionModel(
    QTableView *self,
    QItemSelectionModel *selectionModel) {
  self->QTableView::setSelectionModel(selectionModel);
}

//  void QTableView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView13doItemsLayoutEv(QTableView *self) {
  self->QTableView::doItemsLayout();
}

//  QRect QTableView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK10QTableView10visualRectERK11QModelIndex(
    const QTableView *self,
    const QModelIndex *index) {
  return new QRect(self->QTableView::visualRect(*index));
}

//  void QTableView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QTableView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->QTableView::scrollTo(*index, hint);
}

//  QModelIndex QTableView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK10QTableView7indexAtERK6QPoint(
    const QTableView *self,
    const QPoint *p) {
  return new QModelIndex(self->QTableView::indexAt(*p));
}

//  void QTableView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView16scrollContentsByEii(
    QTableView *self,
    int dx,
    int dy) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::scrollContentsBy(
      dx,
      dy);
}

//  void QTableView::initViewItemOption(QStyleOptionViewItem *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10QTableView18initViewItemOptionEP20QStyleOptionViewItem(
    const QTableView *self,
    QStyleOptionViewItem *option) {
  static_cast<const OwnQTableView *>(self)->OwnQTableView::initViewItemOption(
      option);
}

//  void QTableView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView10paintEventEP11QPaintEvent(
    QTableView *self,
    QPaintEvent *e) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::paintEvent(e);
}

//  void QTableView::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView10timerEventEP11QTimerEvent(
    QTableView *self,
    QTimerEvent *event) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::timerEvent(event);
}

//  void QTableView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView9dropEventEP10QDropEvent(
    QTableView *self,
    QDropEvent *event) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::dropEvent(event);
}

//  int QTableView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTableView16horizontalOffsetEv(const QTableView *self) {
  return static_cast<const OwnQTableView *>(self)->OwnQTableView::horizontalOffset();
}

//  int QTableView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTableView14verticalOffsetEv(const QTableView *self) {
  return static_cast<const OwnQTableView *>(self)->OwnQTableView::verticalOffset();
}

//  void QTableView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTableView *self,
    const QRect *rect,
    int command) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QTableView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK10QTableView24visualRegionForSelectionERK14QItemSelection(
    const QTableView *self,
    const QItemSelection *selection) {
  return new QRegion(
      static_cast<const OwnQTableView *>(self)->OwnQTableView::visualRegionForSelection(
          *selection));
}

//  void QTableView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView16updateGeometriesEv(QTableView *self) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::updateGeometries();
}

//  QSize QTableView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK10QTableView16viewportSizeHintEv(
    const QTableView *self) {
  return new QSize(
      static_cast<const OwnQTableView *>(self)->OwnQTableView::viewportSizeHint());
}

//  int QTableView::sizeHintForRow(int row) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTableView14sizeHintForRowEi(
    const QTableView *self,
    int row) {
  return static_cast<const OwnQTableView *>(self)->OwnQTableView::sizeHintForRow(
      row);
}

//  int QTableView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK10QTableView17sizeHintForColumnEi(
    const QTableView *self,
    int column) {
  return static_cast<const OwnQTableView *>(self)->OwnQTableView::sizeHintForColumn(
      column);
}

//  void QTableView::verticalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView23verticalScrollbarActionEi(
    QTableView *self,
    int action) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::verticalScrollbarAction(
      action);
}

//  void QTableView::horizontalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView25horizontalScrollbarActionEi(
    QTableView *self,
    int action) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::horizontalScrollbarAction(
      action);
}

//  bool QTableView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QTableView13isIndexHiddenERK11QModelIndex(
    const QTableView *self,
    const QModelIndex *index) {
  return static_cast<const OwnQTableView *>(self)->OwnQTableView::isIndexHidden(
      *index);
}

//  void QTableView::selectionChanged(const QItemSelection &selected, const
//      QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView16selectionChangedERK14QItemSelectionS2_(
    QTableView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::selectionChanged(
      *selected,
      *deselected);
}

//  void QTableView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTableView14currentChangedERK11QModelIndexS2_(
    QTableView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  static_cast<OwnQTableView *>(self)->OwnQTableView::currentChanged(
      *current,
      *previous);
}
