//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcolumnview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcolumnview.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QColumnView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQColumnView : QColumnView {
  using QColumnView::isIndexHidden;
  using QColumnView::resizeEvent;
  using QColumnView::setSelection;
  using QColumnView::visualRegionForSelection;
  using QColumnView::horizontalOffset;
  using QColumnView::verticalOffset;
  using QColumnView::rowsInserted;
  using QColumnView::currentChanged;
  using QColumnView::scrollContentsBy;
  using QColumnView::createColumn;
};

//  A QColumnView that Python can take functions over in. Every QColumnView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QModelIndex * (*CuteQColumnViewCall0)(const void *, const QPoint *, int *);
typedef void (*CuteQColumnViewCall1)(const void *, const QModelIndex *, int, int *);
typedef const QSize * (*CuteQColumnViewCall2)(const void *, int *);
typedef const QRect * (*CuteQColumnViewCall3)(const void *, const QModelIndex *, int *);
typedef void (*CuteQColumnViewCall4)(const void *, QAbstractItemModel *, int *);
typedef void (*CuteQColumnViewCall5)(const void *, QItemSelectionModel *, int *);
typedef void (*CuteQColumnViewCall6)(const void *, const QModelIndex *, int *);
typedef void (*CuteQColumnViewCall7)(const void *, int *);
typedef bool (*CuteQColumnViewCall8)(const void *, const QModelIndex *, int *);
typedef void (*CuteQColumnViewCall9)(const void *, QResizeEvent *, int *);
typedef void (*CuteQColumnViewCall10)(const void *, const QRect *, int, int *);
typedef const QRegion * (*CuteQColumnViewCall11)(const void *, const QItemSelection *, int *);
typedef int (*CuteQColumnViewCall12)(const void *, int *);
typedef int (*CuteQColumnViewCall13)(const void *, int *);
typedef void (*CuteQColumnViewCall14)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQColumnViewCall15)(const void *, const QModelIndex *, const QModelIndex *, int *);
typedef void (*CuteQColumnViewCall16)(const void *, int, int, int *);
typedef void * (*CuteQColumnViewCall17)(const void *, const QModelIndex *, int *);
typedef void (*CuteQColumnViewCall18)(const void *, const QString *, int *);
typedef int (*CuteQColumnViewCall19)(const void *, int, int *);
typedef int (*CuteQColumnViewCall20)(const void *, int, int *);
typedef void * (*CuteQColumnViewCall21)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQColumnViewCall22)(const void *, int, int *);
typedef void (*CuteQColumnViewCall23)(const void *, int *);
typedef void (*CuteQColumnViewCall24)(const void *, int *);
typedef void (*CuteQColumnViewCall25)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQColumnViewCall26)(const void *, const QItemSelection *, const QItemSelection *, int *);
typedef void (*CuteQColumnViewCall27)(const void *, int *);
typedef void (*CuteQColumnViewCall28)(const void *, int *);
typedef void (*CuteQColumnViewCall29)(const void *, int *);
typedef void (*CuteQColumnViewCall30)(const void *, int, int *);
typedef void (*CuteQColumnViewCall31)(const void *, int, int *);
typedef void (*CuteQColumnViewCall32)(const void *, int, int *);
typedef void (*CuteQColumnViewCall33)(const void *, int, int *);
typedef void (*CuteQColumnViewCall34)(const void *, QWidget *, int, int *);
typedef void (*CuteQColumnViewCall35)(const void *, QWidget *, int *);
typedef void (*CuteQColumnViewCall36)(const void *, QObject *, int *);
typedef bool (*CuteQColumnViewCall37)(const void *, const QModelIndex *, int, QEvent *, int *);
typedef int (*CuteQColumnViewCall38)(const void *, const QModelIndex *, const QEvent *, int *);
typedef void (*CuteQColumnViewCall39)(const void *, int, int *);
typedef void (*CuteQColumnViewCall40)(const void *, QStyleOptionViewItem *, int *);
typedef bool (*CuteQColumnViewCall41)(const void *, bool, int *);
typedef bool (*CuteQColumnViewCall42)(const void *, QEvent *, int *);
typedef bool (*CuteQColumnViewCall43)(const void *, QEvent *, int *);
typedef void (*CuteQColumnViewCall44)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColumnViewCall45)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColumnViewCall46)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColumnViewCall47)(const void *, QMouseEvent *, int *);
typedef void (*CuteQColumnViewCall48)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQColumnViewCall49)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQColumnViewCall50)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQColumnViewCall51)(const void *, QDropEvent *, int *);
typedef void (*CuteQColumnViewCall52)(const void *, QFocusEvent *, int *);
typedef void (*CuteQColumnViewCall53)(const void *, QFocusEvent *, int *);
typedef void (*CuteQColumnViewCall54)(const void *, QKeyEvent *, int *);
typedef void (*CuteQColumnViewCall55)(const void *, QTimerEvent *, int *);
typedef void (*CuteQColumnViewCall56)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQColumnViewCall57)(const void *, QObject *, QEvent *, int *);
typedef const QSize * (*CuteQColumnViewCall58)(const void *, int *);
typedef const QSize * (*CuteQColumnViewCall59)(const void *, int *);
typedef void (*CuteQColumnViewCall60)(const void *, QWidget *, int *);
typedef void (*CuteQColumnViewCall61)(const void *, QPaintEvent *, int *);
typedef void (*CuteQColumnViewCall62)(const void *, QWheelEvent *, int *);
typedef void (*CuteQColumnViewCall63)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQColumnViewCall64)(const void *, QEvent *, int *);
typedef void (*CuteQColumnViewCall65)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQColumnViewCall66)(const void *, int *);
typedef void (*CuteQColumnViewCall67)(const void *, bool, int *);
typedef int (*CuteQColumnViewCall68)(const void *, int, int *);
typedef bool (*CuteQColumnViewCall69)(const void *, int *);
typedef void * (*CuteQColumnViewCall70)(const void *, int *);
typedef void (*CuteQColumnViewCall71)(const void *, QKeyEvent *, int *);
typedef void (*CuteQColumnViewCall72)(const void *, QEnterEvent *, int *);
typedef void (*CuteQColumnViewCall73)(const void *, QEvent *, int *);
typedef void (*CuteQColumnViewCall74)(const void *, QMoveEvent *, int *);
typedef void (*CuteQColumnViewCall75)(const void *, QCloseEvent *, int *);
typedef void (*CuteQColumnViewCall76)(const void *, QTabletEvent *, int *);
typedef void (*CuteQColumnViewCall77)(const void *, QActionEvent *, int *);
typedef void (*CuteQColumnViewCall78)(const void *, QShowEvent *, int *);
typedef void (*CuteQColumnViewCall79)(const void *, QHideEvent *, int *);
typedef int (*CuteQColumnViewCall80)(const void *, int, int *);
typedef void (*CuteQColumnViewCall81)(const void *, QPainter *, int *);
typedef void * (*CuteQColumnViewCall82)(const void *, QPoint *, int *);
typedef void * (*CuteQColumnViewCall83)(const void *, int *);
typedef void (*CuteQColumnViewCall84)(const void *, QChildEvent *, int *);
typedef void (*CuteQColumnViewCall85)(const void *, QEvent *, int *);
typedef void (*CuteQColumnViewCall86)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQColumnViewCall87)(const void *, const QMetaMethod *, int *);
class CuteQColumnView : public QColumnView {
public:
  using QColumnView::QColumnView;
  void *taken[88] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
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
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QColumnView12createColumnERK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[87] = call;
      return true;
    }
    return false;
  }

  //  QModelIndex QColumnView::indexAt(const QPoint &point) const
  QModelIndex indexAt(const QPoint &point) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQColumnViewCall0 call = reinterpret_cast<CuteQColumnViewCall0>(taken[0]);
      const QModelIndex * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return QColumnView::indexAt(point);
  }

  //  void QColumnView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColumnViewCall1 call = reinterpret_cast<CuteQColumnViewCall1>(taken[1]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QColumnView::scrollTo(index, hint);
  }

  //  QSize QColumnView::sizeHint() const
  QSize sizeHint() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQColumnViewCall2 call = reinterpret_cast<CuteQColumnViewCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QColumnView::sizeHint();
  }

  //  QRect QColumnView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQColumnViewCall3 call = reinterpret_cast<CuteQColumnViewCall3>(taken[3]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QColumnView::visualRect(index);
  }

  //  void QColumnView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[4]) {
      int handled = 0;
      CuteQColumnViewCall4 call = reinterpret_cast<CuteQColumnViewCall4>(taken[4]);
      call(this, model, &handled);
      if (handled) return;
    }
    QColumnView::setModel(model);
  }

  //  void QColumnView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[5]) {
      int handled = 0;
      CuteQColumnViewCall5 call = reinterpret_cast<CuteQColumnViewCall5>(taken[5]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QColumnView::setSelectionModel(selectionModel);
  }

  //  void QColumnView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[6]) {
      int handled = 0;
      CuteQColumnViewCall6 call = reinterpret_cast<CuteQColumnViewCall6>(taken[6]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QColumnView::setRootIndex(index);
  }

  //  void QColumnView::selectAll()
  void selectAll() override {
    if (taken[7]) {
      int handled = 0;
      CuteQColumnViewCall7 call = reinterpret_cast<CuteQColumnViewCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QColumnView::selectAll();
  }

  //  bool QColumnView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQColumnViewCall8 call = reinterpret_cast<CuteQColumnViewCall8>(taken[8]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QColumnView::isIndexHidden(index);
  }

  //  void QColumnView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQColumnViewCall9 call = reinterpret_cast<CuteQColumnViewCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QColumnView::resizeEvent(event);
  }

  //  void QColumnView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[10]) {
      int handled = 0;
      CuteQColumnViewCall10 call = reinterpret_cast<CuteQColumnViewCall10>(taken[10]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QColumnView::setSelection(rect, command);
  }

  //  QRegion QColumnView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQColumnViewCall11 call = reinterpret_cast<CuteQColumnViewCall11>(taken[11]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QColumnView::visualRegionForSelection(selection);
  }

  //  int QColumnView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQColumnViewCall12 call = reinterpret_cast<CuteQColumnViewCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QColumnView::horizontalOffset();
  }

  //  int QColumnView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQColumnViewCall13 call = reinterpret_cast<CuteQColumnViewCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QColumnView::verticalOffset();
  }

  //  void QColumnView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[14]) {
      int handled = 0;
      CuteQColumnViewCall14 call = reinterpret_cast<CuteQColumnViewCall14>(taken[14]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QColumnView::rowsInserted(parent, start, end);
  }

  //  void QColumnView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[15]) {
      int handled = 0;
      CuteQColumnViewCall15 call = reinterpret_cast<CuteQColumnViewCall15>(taken[15]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QColumnView::currentChanged(current, previous);
  }

  //  void QColumnView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[16]) {
      int handled = 0;
      CuteQColumnViewCall16 call = reinterpret_cast<CuteQColumnViewCall16>(taken[16]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QColumnView::scrollContentsBy(dx, dy);
  }

  //  QAbstractItemView *QColumnView::createColumn(const QModelIndex
  //      &rootIndex)
  QAbstractItemView *createColumn(const QModelIndex &rootIndex) override {
    if (taken[17]) {
      int handled = 0;
      CuteQColumnViewCall17 call = reinterpret_cast<CuteQColumnViewCall17>(taken[17]);
      void * given = call(this, &rootIndex, &handled);
      if (handled) return static_cast<QAbstractItemView *>(given);
    }
    return QColumnView::createColumn(rootIndex);
  }

  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[18]) {
      int handled = 0;
      CuteQColumnViewCall18 call = reinterpret_cast<CuteQColumnViewCall18>(taken[18]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }

  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQColumnViewCall19 call = reinterpret_cast<CuteQColumnViewCall19>(taken[19]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }

  //  int QAbstractItemView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQColumnViewCall20 call = reinterpret_cast<CuteQColumnViewCall20>(taken[20]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForColumn(column);
  }

  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQColumnViewCall21 call = reinterpret_cast<CuteQColumnViewCall21>(taken[21]);
      void * given = call(this, &index, &handled);
      if (handled) return static_cast<QAbstractItemDelegate *>(given);
    }
    return QAbstractItemView::itemDelegateForIndex(index);
  }

  //  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQColumnViewCall22 call = reinterpret_cast<CuteQColumnViewCall22>(taken[22]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }

  //  void QAbstractItemView::reset()
  void reset() override {
    if (taken[23]) {
      int handled = 0;
      CuteQColumnViewCall23 call = reinterpret_cast<CuteQColumnViewCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::reset();
  }

  //  void QAbstractItemView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[24]) {
      int handled = 0;
      CuteQColumnViewCall24 call = reinterpret_cast<CuteQColumnViewCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::doItemsLayout();
  }

  //  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex
  //      &parent, int start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[25]) {
      int handled = 0;
      CuteQColumnViewCall25 call = reinterpret_cast<CuteQColumnViewCall25>(taken[25]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemView::rowsAboutToBeRemoved(parent, start, end);
  }

  //  void QAbstractItemView::selectionChanged(const QItemSelection
  //      &selected, const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[26]) {
      int handled = 0;
      CuteQColumnViewCall26 call = reinterpret_cast<CuteQColumnViewCall26>(taken[26]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectionChanged(selected, deselected);
  }

  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[27]) {
      int handled = 0;
      CuteQColumnViewCall27 call = reinterpret_cast<CuteQColumnViewCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }

  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[28]) {
      int handled = 0;
      CuteQColumnViewCall28 call = reinterpret_cast<CuteQColumnViewCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }

  //  void QAbstractItemView::updateGeometries()
  void updateGeometries() override {
    if (taken[29]) {
      int handled = 0;
      CuteQColumnViewCall29 call = reinterpret_cast<CuteQColumnViewCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateGeometries();
  }

  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[30]) {
      int handled = 0;
      CuteQColumnViewCall30 call = reinterpret_cast<CuteQColumnViewCall30>(taken[30]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }

  //  void QAbstractItemView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[31]) {
      int handled = 0;
      CuteQColumnViewCall31 call = reinterpret_cast<CuteQColumnViewCall31>(taken[31]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarAction(action);
  }

  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[32]) {
      int handled = 0;
      CuteQColumnViewCall32 call = reinterpret_cast<CuteQColumnViewCall32>(taken[32]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }

  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[33]) {
      int handled = 0;
      CuteQColumnViewCall33 call = reinterpret_cast<CuteQColumnViewCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQColumnViewCall34 call = reinterpret_cast<CuteQColumnViewCall34>(taken[34]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }

  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[35]) {
      int handled = 0;
      CuteQColumnViewCall35 call = reinterpret_cast<CuteQColumnViewCall35>(taken[35]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }

  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[36]) {
      int handled = 0;
      CuteQColumnViewCall36 call = reinterpret_cast<CuteQColumnViewCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteQColumnViewCall37 call = reinterpret_cast<CuteQColumnViewCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQColumnViewCall38 call = reinterpret_cast<CuteQColumnViewCall38>(taken[38]);
      int given = call(this, &index, event, &handled);
      if (handled) return QFlags<QItemSelectionModel::SelectionFlag>::fromInt(given);
    }
    return QAbstractItemView::selectionCommand(index, event);
  }

  //  void QAbstractItemView::startDrag(Qt::DropActions supportedActions)
  void startDrag(Qt::DropActions supportedActions) override {
    if (taken[39]) {
      int handled = 0;
      CuteQColumnViewCall39 call = reinterpret_cast<CuteQColumnViewCall39>(taken[39]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QAbstractItemView::startDrag(supportedActions);
  }

  //  void QAbstractItemView::initViewItemOption(QStyleOptionViewItem
  //      *option) const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQColumnViewCall40 call = reinterpret_cast<CuteQColumnViewCall40>(taken[40]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractItemView::initViewItemOption(option);
  }

  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[41]) {
      int handled = 0;
      CuteQColumnViewCall41 call = reinterpret_cast<CuteQColumnViewCall41>(taken[41]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }

  //  bool QAbstractItemView::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQColumnViewCall42 call = reinterpret_cast<CuteQColumnViewCall42>(taken[42]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::event(event);
  }

  //  bool QAbstractItemView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQColumnViewCall43 call = reinterpret_cast<CuteQColumnViewCall43>(taken[43]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::viewportEvent(event);
  }

  //  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteQColumnViewCall44 call = reinterpret_cast<CuteQColumnViewCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }

  //  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteQColumnViewCall45 call = reinterpret_cast<CuteQColumnViewCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseMoveEvent(event);
  }

  //  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQColumnViewCall46 call = reinterpret_cast<CuteQColumnViewCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseReleaseEvent(event);
  }

  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQColumnViewCall47 call = reinterpret_cast<CuteQColumnViewCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseDoubleClickEvent(event);
  }

  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQColumnViewCall48 call = reinterpret_cast<CuteQColumnViewCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }

  //  void QAbstractItemView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQColumnViewCall49 call = reinterpret_cast<CuteQColumnViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragMoveEvent(event);
  }

  //  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQColumnViewCall50 call = reinterpret_cast<CuteQColumnViewCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragLeaveEvent(event);
  }

  //  void QAbstractItemView::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQColumnViewCall51 call = reinterpret_cast<CuteQColumnViewCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dropEvent(event);
  }

  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQColumnViewCall52 call = reinterpret_cast<CuteQColumnViewCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }

  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQColumnViewCall53 call = reinterpret_cast<CuteQColumnViewCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }

  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQColumnViewCall54 call = reinterpret_cast<CuteQColumnViewCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }

  //  void QAbstractItemView::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQColumnViewCall55 call = reinterpret_cast<CuteQColumnViewCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::timerEvent(event);
  }

  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQColumnViewCall56 call = reinterpret_cast<CuteQColumnViewCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::inputMethodEvent(event);
  }

  //  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQColumnViewCall57 call = reinterpret_cast<CuteQColumnViewCall57>(taken[57]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }

  //  QSize QAbstractItemView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[58]) {
      int handled = 0;
      CuteQColumnViewCall58 call = reinterpret_cast<CuteQColumnViewCall58>(taken[58]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::viewportSizeHint();
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[59]) {
      int handled = 0;
      CuteQColumnViewCall59 call = reinterpret_cast<CuteQColumnViewCall59>(taken[59]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[60]) {
      int handled = 0;
      CuteQColumnViewCall60 call = reinterpret_cast<CuteQColumnViewCall60>(taken[60]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }

  //  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQColumnViewCall61 call = reinterpret_cast<CuteQColumnViewCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::paintEvent(a0);
  }

  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQColumnViewCall62 call = reinterpret_cast<CuteQColumnViewCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }

  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQColumnViewCall63 call = reinterpret_cast<CuteQColumnViewCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQColumnViewCall64 call = reinterpret_cast<CuteQColumnViewCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[65]) {
      int handled = 0;
      CuteQColumnViewCall65 call = reinterpret_cast<CuteQColumnViewCall65>(taken[65]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[66]) {
      int handled = 0;
      CuteQColumnViewCall66 call = reinterpret_cast<CuteQColumnViewCall66>(taken[66]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[67]) {
      int handled = 0;
      CuteQColumnViewCall67 call = reinterpret_cast<CuteQColumnViewCall67>(taken[67]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[68]) {
      int handled = 0;
      CuteQColumnViewCall68 call = reinterpret_cast<CuteQColumnViewCall68>(taken[68]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQColumnViewCall69 call = reinterpret_cast<CuteQColumnViewCall69>(taken[69]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[70]) {
      int handled = 0;
      CuteQColumnViewCall70 call = reinterpret_cast<CuteQColumnViewCall70>(taken[70]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQColumnViewCall71 call = reinterpret_cast<CuteQColumnViewCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQColumnViewCall72 call = reinterpret_cast<CuteQColumnViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQColumnViewCall73 call = reinterpret_cast<CuteQColumnViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQColumnViewCall74 call = reinterpret_cast<CuteQColumnViewCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQColumnViewCall75 call = reinterpret_cast<CuteQColumnViewCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQColumnViewCall76 call = reinterpret_cast<CuteQColumnViewCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQColumnViewCall77 call = reinterpret_cast<CuteQColumnViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQColumnViewCall78 call = reinterpret_cast<CuteQColumnViewCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[79]) {
      int handled = 0;
      CuteQColumnViewCall79 call = reinterpret_cast<CuteQColumnViewCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQColumnViewCall80 call = reinterpret_cast<CuteQColumnViewCall80>(taken[80]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQColumnViewCall81 call = reinterpret_cast<CuteQColumnViewCall81>(taken[81]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[82]) {
      int handled = 0;
      CuteQColumnViewCall82 call = reinterpret_cast<CuteQColumnViewCall82>(taken[82]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[83]) {
      int handled = 0;
      CuteQColumnViewCall83 call = reinterpret_cast<CuteQColumnViewCall83>(taken[83]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      CuteQColumnViewCall84 call = reinterpret_cast<CuteQColumnViewCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[85]) {
      int handled = 0;
      CuteQColumnViewCall85 call = reinterpret_cast<CuteQColumnViewCall85>(taken[85]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[86]) {
      int handled = 0;
      CuteQColumnViewCall86 call = reinterpret_cast<CuteQColumnViewCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[87]) {
      int handled = 0;
      CuteQColumnViewCall87 call = reinterpret_cast<CuteQColumnViewCall87>(taken[87]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QColumnView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QColumnView10metaObjectEv(
    const QColumnView *self) {
  return self->metaObject();
}

//  QString QColumnView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QColumnView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QColumnView::tr(s, c, n));
}

//  QColumnView::QColumnView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QColumnView *ritual_ZN11QColumnViewC1EP7QWidget(QWidget *parent) {
  return new CuteQColumnView(parent);
}

//  QColumnView::~QColumnView()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnViewD1Ev(QColumnView *self) {
  delete self;
}

//  QModelIndex QColumnView::indexAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QColumnView7indexAtERK6QPoint(
    const QColumnView *self,
    const QPoint *point) {
  return new QModelIndex(self->indexAt(*point));
}

//  void QColumnView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QColumnView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QSize QColumnView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QColumnView8sizeHintEv(const QColumnView *self) {
  return new QSize(self->sizeHint());
}

//  QRect QColumnView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QColumnView10visualRectERK11QModelIndex(
    const QColumnView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QColumnView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView8setModelEP18QAbstractItemModel(
    QColumnView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  void QColumnView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView17setSelectionModelEP19QItemSelectionModel(
    QColumnView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  void QColumnView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView12setRootIndexERK11QModelIndex(
    QColumnView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QColumnView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView9selectAllEv(QColumnView *self) {
  self->selectAll();
}

//  void QColumnView::setResizeGripsVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView21setResizeGripsVisibleEb(
    QColumnView *self,
    bool visible) {
  self->setResizeGripsVisible(visible);
}

//  bool QColumnView::resizeGripsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColumnView18resizeGripsVisibleEv(const QColumnView *self) {
  return self->resizeGripsVisible();
}

//  void QColumnView::setPreviewColumnVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView23setPreviewColumnVisibleEb(
    QColumnView *self,
    bool visible) {
  self->setPreviewColumnVisible(visible);
}

//  bool QColumnView::isPreviewColumnVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QColumnView22isPreviewColumnVisibleEv(
    const QColumnView *self) {
  return self->isPreviewColumnVisible();
}

//  QWidget *QColumnView::previewWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QColumnView13previewWidgetEv(const QColumnView *self) {
  return self->previewWidget();
}

//  void QColumnView::setPreviewWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QColumnView16setPreviewWidgetEP7QWidget(
    QColumnView *self,
    QWidget *widget) {
  self->setPreviewWidget(widget);
}

//  a Python function taken by a CuteQColumnView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColumnView(
    QColumnView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColumnView *>(self)->take(key, call);
}

//  QModelIndex QColumnView::indexAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK11QColumnView7indexAtERK6QPoint(
    const QColumnView *self,
    const QPoint *point) {
  return new QModelIndex(self->QColumnView::indexAt(*point));
}

//  void QColumnView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QColumnView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->QColumnView::scrollTo(*index, hint);
}

//  QSize QColumnView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QColumnView8sizeHintEv(const QColumnView *self) {
  return new QSize(self->QColumnView::sizeHint());
}

//  QRect QColumnView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QColumnView10visualRectERK11QModelIndex(
    const QColumnView *self,
    const QModelIndex *index) {
  return new QRect(self->QColumnView::visualRect(*index));
}

//  void QColumnView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView8setModelEP18QAbstractItemModel(
    QColumnView *self,
    QAbstractItemModel *model) {
  self->QColumnView::setModel(model);
}

//  void QColumnView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView17setSelectionModelEP19QItemSelectionModel(
    QColumnView *self,
    QItemSelectionModel *selectionModel) {
  self->QColumnView::setSelectionModel(selectionModel);
}

//  void QColumnView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView12setRootIndexERK11QModelIndex(
    QColumnView *self,
    const QModelIndex *index) {
  self->QColumnView::setRootIndex(*index);
}

//  void QColumnView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView9selectAllEv(QColumnView *self) {
  self->QColumnView::selectAll();
}

//  bool QColumnView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QColumnView13isIndexHiddenERK11QModelIndex(
    const QColumnView *self,
    const QModelIndex *index) {
  return static_cast<const OwnQColumnView *>(self)->OwnQColumnView::isIndexHidden(
      *index);
}

//  void QColumnView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView11resizeEventEP12QResizeEvent(
    QColumnView *self,
    QResizeEvent *event) {
  static_cast<OwnQColumnView *>(self)->OwnQColumnView::resizeEvent(event);
}

//  void QColumnView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QColumnView *self,
    const QRect *rect,
    int command) {
  static_cast<OwnQColumnView *>(self)->OwnQColumnView::setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QColumnView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK11QColumnView24visualRegionForSelectionERK14QItemSelection(
    const QColumnView *self,
    const QItemSelection *selection) {
  return new QRegion(
      static_cast<const OwnQColumnView *>(self)->OwnQColumnView::visualRegionForSelection(
          *selection));
}

//  int QColumnView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QColumnView16horizontalOffsetEv(
    const QColumnView *self) {
  return static_cast<const OwnQColumnView *>(self)->OwnQColumnView::horizontalOffset();
}

//  int QColumnView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QColumnView14verticalOffsetEv(const QColumnView *self) {
  return static_cast<const OwnQColumnView *>(self)->OwnQColumnView::verticalOffset();
}

//  void QColumnView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView12rowsInsertedERK11QModelIndexii(
    QColumnView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQColumnView *>(self)->OwnQColumnView::rowsInserted(
      *parent,
      start,
      end);
}

//  void QColumnView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView14currentChangedERK11QModelIndexS2_(
    QColumnView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  static_cast<OwnQColumnView *>(self)->OwnQColumnView::currentChanged(
      *current,
      *previous);
}

//  void QColumnView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QColumnView16scrollContentsByEii(
    QColumnView *self,
    int dx,
    int dy) {
  static_cast<OwnQColumnView *>(self)->OwnQColumnView::scrollContentsBy(
      dx,
      dy);
}

//  QAbstractItemView *QColumnView::createColumn(const QModelIndex
//      &rootIndex)
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_own_ZN11QColumnView12createColumnERK11QModelIndex(
    QColumnView *self,
    const QModelIndex *rootIndex) {
  return static_cast<OwnQColumnView *>(self)->OwnQColumnView::createColumn(
      *rootIndex);
}
