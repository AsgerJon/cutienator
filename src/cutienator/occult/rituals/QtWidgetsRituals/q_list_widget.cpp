//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlistwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlistwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QListWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQListWidget : QListWidget {
  using QListWidget::dropEvent;
  using QListWidget::event;
  using QListWidget::dropMimeData;
  using QListWidget::supportedDropActions;
};

//  A QListWidget that Python can take functions over in. Every QListWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQListWidgetCall0)(const void *, QItemSelectionModel *, int *);
typedef void (*CuteQListWidgetCall1)(const void *, QDropEvent *, int *);
typedef bool (*CuteQListWidgetCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQListWidgetCall3)(const void *, int, const QMimeData *, int, int *);
typedef int (*CuteQListWidgetCall4)(const void *, int *);
typedef const QRect * (*CuteQListWidgetCall5)(const void *, const QModelIndex *, int *);
typedef void (*CuteQListWidgetCall6)(const void *, const QModelIndex *, int, int *);
typedef const QModelIndex * (*CuteQListWidgetCall7)(const void *, const QPoint *, int *);
typedef void (*CuteQListWidgetCall8)(const void *, int *);
typedef void (*CuteQListWidgetCall9)(const void *, int *);
typedef void (*CuteQListWidgetCall10)(const void *, const QModelIndex *, int *);
typedef void (*CuteQListWidgetCall11)(const void *, int, int, int *);
typedef void (*CuteQListWidgetCall12)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQListWidgetCall13)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQListWidgetCall14)(const void *, QMouseEvent *, int *);
typedef void (*CuteQListWidgetCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQListWidgetCall16)(const void *, QWheelEvent *, int *);
typedef void (*CuteQListWidgetCall17)(const void *, QTimerEvent *, int *);
typedef void (*CuteQListWidgetCall18)(const void *, QResizeEvent *, int *);
typedef void (*CuteQListWidgetCall19)(const void *, QDragMoveEvent *, int *);
typedef void (*CuteQListWidgetCall20)(const void *, QDragLeaveEvent *, int *);
typedef void (*CuteQListWidgetCall21)(const void *, int, int *);
typedef void (*CuteQListWidgetCall22)(const void *, QStyleOptionViewItem *, int *);
typedef void (*CuteQListWidgetCall23)(const void *, QPaintEvent *, int *);
typedef int (*CuteQListWidgetCall24)(const void *, int *);
typedef int (*CuteQListWidgetCall25)(const void *, int *);
typedef void (*CuteQListWidgetCall26)(const void *, const QRect *, int, int *);
typedef const QRegion * (*CuteQListWidgetCall27)(const void *, const QItemSelection *, int *);
typedef void (*CuteQListWidgetCall28)(const void *, int *);
typedef bool (*CuteQListWidgetCall29)(const void *, const QModelIndex *, int *);
typedef void (*CuteQListWidgetCall30)(const void *, const QItemSelection *, const QItemSelection *, int *);
typedef void (*CuteQListWidgetCall31)(const void *, const QModelIndex *, const QModelIndex *, int *);
typedef const QSize * (*CuteQListWidgetCall32)(const void *, int *);
typedef void (*CuteQListWidgetCall33)(const void *, const QString *, int *);
typedef int (*CuteQListWidgetCall34)(const void *, int, int *);
typedef int (*CuteQListWidgetCall35)(const void *, int, int *);
typedef void * (*CuteQListWidgetCall36)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQListWidgetCall37)(const void *, int, int *);
typedef void (*CuteQListWidgetCall38)(const void *, int *);
typedef void (*CuteQListWidgetCall39)(const void *, int *);
typedef void (*CuteQListWidgetCall40)(const void *, int *);
typedef void (*CuteQListWidgetCall41)(const void *, int, int *);
typedef void (*CuteQListWidgetCall42)(const void *, int, int *);
typedef void (*CuteQListWidgetCall43)(const void *, int, int *);
typedef void (*CuteQListWidgetCall44)(const void *, int, int *);
typedef void (*CuteQListWidgetCall45)(const void *, QWidget *, int, int *);
typedef void (*CuteQListWidgetCall46)(const void *, QWidget *, int *);
typedef void (*CuteQListWidgetCall47)(const void *, QObject *, int *);
typedef bool (*CuteQListWidgetCall48)(const void *, const QModelIndex *, int, QEvent *, int *);
typedef int (*CuteQListWidgetCall49)(const void *, const QModelIndex *, const QEvent *, int *);
typedef bool (*CuteQListWidgetCall50)(const void *, bool, int *);
typedef bool (*CuteQListWidgetCall51)(const void *, QEvent *, int *);
typedef void (*CuteQListWidgetCall52)(const void *, QMouseEvent *, int *);
typedef void (*CuteQListWidgetCall53)(const void *, QMouseEvent *, int *);
typedef void (*CuteQListWidgetCall54)(const void *, QDragEnterEvent *, int *);
typedef void (*CuteQListWidgetCall55)(const void *, QFocusEvent *, int *);
typedef void (*CuteQListWidgetCall56)(const void *, QFocusEvent *, int *);
typedef void (*CuteQListWidgetCall57)(const void *, QKeyEvent *, int *);
typedef void (*CuteQListWidgetCall58)(const void *, QInputMethodEvent *, int *);
typedef bool (*CuteQListWidgetCall59)(const void *, QObject *, QEvent *, int *);
typedef const QSize * (*CuteQListWidgetCall60)(const void *, int *);
typedef const QSize * (*CuteQListWidgetCall61)(const void *, int *);
typedef void (*CuteQListWidgetCall62)(const void *, QWidget *, int *);
typedef void (*CuteQListWidgetCall63)(const void *, QContextMenuEvent *, int *);
typedef void (*CuteQListWidgetCall64)(const void *, QEvent *, int *);
typedef void (*CuteQListWidgetCall65)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQListWidgetCall66)(const void *, int *);
typedef void (*CuteQListWidgetCall67)(const void *, bool, int *);
typedef int (*CuteQListWidgetCall68)(const void *, int, int *);
typedef bool (*CuteQListWidgetCall69)(const void *, int *);
typedef void * (*CuteQListWidgetCall70)(const void *, int *);
typedef void (*CuteQListWidgetCall71)(const void *, QKeyEvent *, int *);
typedef void (*CuteQListWidgetCall72)(const void *, QEnterEvent *, int *);
typedef void (*CuteQListWidgetCall73)(const void *, QEvent *, int *);
typedef void (*CuteQListWidgetCall74)(const void *, QMoveEvent *, int *);
typedef void (*CuteQListWidgetCall75)(const void *, QCloseEvent *, int *);
typedef void (*CuteQListWidgetCall76)(const void *, QTabletEvent *, int *);
typedef void (*CuteQListWidgetCall77)(const void *, QActionEvent *, int *);
typedef void (*CuteQListWidgetCall78)(const void *, QShowEvent *, int *);
typedef void (*CuteQListWidgetCall79)(const void *, QHideEvent *, int *);
typedef int (*CuteQListWidgetCall80)(const void *, int, int *);
typedef void (*CuteQListWidgetCall81)(const void *, QPainter *, int *);
typedef void * (*CuteQListWidgetCall82)(const void *, QPoint *, int *);
typedef void * (*CuteQListWidgetCall83)(const void *, int *);
typedef void (*CuteQListWidgetCall84)(const void *, QChildEvent *, int *);
typedef void (*CuteQListWidgetCall85)(const void *, QEvent *, int *);
typedef void (*CuteQListWidgetCall86)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQListWidgetCall87)(const void *, const QMetaMethod *, int *);
class CuteQListWidget : public QListWidget {
public:
  using QListWidget::QListWidget;
  void *taken[88] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QListWidget12dropMimeDataEiPK9QMimeDataN2Qt10DropActionE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QListWidget20supportedDropActionsEv")) {
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
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
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

  //  void QListWidget::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[0]) {
      int handled = 0;
      CuteQListWidgetCall0 call = reinterpret_cast<CuteQListWidgetCall0>(taken[0]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QListWidget::setSelectionModel(selectionModel);
  }

  //  void QListWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQListWidgetCall1 call = reinterpret_cast<CuteQListWidgetCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QListWidget::dropEvent(event);
  }

  //  bool QListWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQListWidgetCall2 call = reinterpret_cast<CuteQListWidgetCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QListWidget::event(e);
  }

  //  bool QListWidget::dropMimeData(int index, const QMimeData *data,
  //      Qt::DropAction action)
  bool dropMimeData(
      int index,
      const QMimeData *data,
      Qt::DropAction action) override {
    if (taken[3]) {
      int handled = 0;
      CuteQListWidgetCall3 call = reinterpret_cast<CuteQListWidgetCall3>(taken[3]);
      bool given = call(this, index, data, static_cast<int>(action), &handled);
      if (handled) return given;
    }
    return QListWidget::dropMimeData(index, data, action);
  }

  //  Qt::DropActions QListWidget::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQListWidgetCall4 call = reinterpret_cast<CuteQListWidgetCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QListWidget::supportedDropActions();
  }

  //  QRect QListView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQListWidgetCall5 call = reinterpret_cast<CuteQListWidgetCall5>(taken[5]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QListView::visualRect(index);
  }

  //  void QListView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQListWidgetCall6 call = reinterpret_cast<CuteQListWidgetCall6>(taken[6]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QListView::scrollTo(index, hint);
  }

  //  QModelIndex QListView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQListWidgetCall7 call = reinterpret_cast<CuteQListWidgetCall7>(taken[7]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QListView::indexAt(p);
  }

  //  void QListView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[8]) {
      int handled = 0;
      CuteQListWidgetCall8 call = reinterpret_cast<CuteQListWidgetCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::doItemsLayout();
  }

  //  void QListView::reset()
  void reset() override {
    if (taken[9]) {
      int handled = 0;
      CuteQListWidgetCall9 call = reinterpret_cast<CuteQListWidgetCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::reset();
  }

  //  void QListView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[10]) {
      int handled = 0;
      CuteQListWidgetCall10 call = reinterpret_cast<CuteQListWidgetCall10>(taken[10]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QListView::setRootIndex(index);
  }

  //  void QListView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[11]) {
      int handled = 0;
      CuteQListWidgetCall11 call = reinterpret_cast<CuteQListWidgetCall11>(taken[11]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QListView::scrollContentsBy(dx, dy);
  }

  //  void QListView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[12]) {
      int handled = 0;
      CuteQListWidgetCall12 call = reinterpret_cast<CuteQListWidgetCall12>(taken[12]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QListView::rowsInserted(parent, start, end);
  }

  //  void QListView::rowsAboutToBeRemoved(const QModelIndex &parent, int
  //      start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[13]) {
      int handled = 0;
      CuteQListWidgetCall13 call = reinterpret_cast<CuteQListWidgetCall13>(taken[13]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QListView::rowsAboutToBeRemoved(parent, start, end);
  }

  //  void QListView::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQListWidgetCall14 call = reinterpret_cast<CuteQListWidgetCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseMoveEvent(e);
  }

  //  void QListView::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQListWidgetCall15 call = reinterpret_cast<CuteQListWidgetCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseReleaseEvent(e);
  }

  //  void QListView::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQListWidgetCall16 call = reinterpret_cast<CuteQListWidgetCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::wheelEvent(e);
  }

  //  void QListView::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQListWidgetCall17 call = reinterpret_cast<CuteQListWidgetCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::timerEvent(e);
  }

  //  void QListView::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[18]) {
      int handled = 0;
      CuteQListWidgetCall18 call = reinterpret_cast<CuteQListWidgetCall18>(taken[18]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::resizeEvent(e);
  }

  //  void QListView::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQListWidgetCall19 call = reinterpret_cast<CuteQListWidgetCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dragMoveEvent(e);
  }

  //  void QListView::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[20]) {
      int handled = 0;
      CuteQListWidgetCall20 call = reinterpret_cast<CuteQListWidgetCall20>(taken[20]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dragLeaveEvent(e);
  }

  //  void QListView::startDrag(Qt::DropActions supportedActions)
  void startDrag(Qt::DropActions supportedActions) override {
    if (taken[21]) {
      int handled = 0;
      CuteQListWidgetCall21 call = reinterpret_cast<CuteQListWidgetCall21>(taken[21]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QListView::startDrag(supportedActions);
  }

  //  void QListView::initViewItemOption(QStyleOptionViewItem *option)
  //      const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQListWidgetCall22 call = reinterpret_cast<CuteQListWidgetCall22>(taken[22]);
      call(this, option, &handled);
      if (handled) return;
    }
    QListView::initViewItemOption(option);
  }

  //  void QListView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[23]) {
      int handled = 0;
      CuteQListWidgetCall23 call = reinterpret_cast<CuteQListWidgetCall23>(taken[23]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::paintEvent(e);
  }

  //  int QListView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQListWidgetCall24 call = reinterpret_cast<CuteQListWidgetCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QListView::horizontalOffset();
  }

  //  int QListView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQListWidgetCall25 call = reinterpret_cast<CuteQListWidgetCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QListView::verticalOffset();
  }

  //  void QListView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[26]) {
      int handled = 0;
      CuteQListWidgetCall26 call = reinterpret_cast<CuteQListWidgetCall26>(taken[26]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QListView::setSelection(rect, command);
  }

  //  QRegion QListView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQListWidgetCall27 call = reinterpret_cast<CuteQListWidgetCall27>(taken[27]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QListView::visualRegionForSelection(selection);
  }

  //  void QListView::updateGeometries()
  void updateGeometries() override {
    if (taken[28]) {
      int handled = 0;
      CuteQListWidgetCall28 call = reinterpret_cast<CuteQListWidgetCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::updateGeometries();
  }

  //  bool QListView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQListWidgetCall29 call = reinterpret_cast<CuteQListWidgetCall29>(taken[29]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QListView::isIndexHidden(index);
  }

  //  void QListView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[30]) {
      int handled = 0;
      CuteQListWidgetCall30 call = reinterpret_cast<CuteQListWidgetCall30>(taken[30]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QListView::selectionChanged(selected, deselected);
  }

  //  void QListView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[31]) {
      int handled = 0;
      CuteQListWidgetCall31 call = reinterpret_cast<CuteQListWidgetCall31>(taken[31]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QListView::currentChanged(current, previous);
  }

  //  QSize QListView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQListWidgetCall32 call = reinterpret_cast<CuteQListWidgetCall32>(taken[32]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QListView::viewportSizeHint();
  }

  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[33]) {
      int handled = 0;
      CuteQListWidgetCall33 call = reinterpret_cast<CuteQListWidgetCall33>(taken[33]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }

  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQListWidgetCall34 call = reinterpret_cast<CuteQListWidgetCall34>(taken[34]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }

  //  int QAbstractItemView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQListWidgetCall35 call = reinterpret_cast<CuteQListWidgetCall35>(taken[35]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForColumn(column);
  }

  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQListWidgetCall36 call = reinterpret_cast<CuteQListWidgetCall36>(taken[36]);
      void * given = call(this, &index, &handled);
      if (handled) return static_cast<QAbstractItemDelegate *>(given);
    }
    return QAbstractItemView::itemDelegateForIndex(index);
  }

  //  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQListWidgetCall37 call = reinterpret_cast<CuteQListWidgetCall37>(taken[37]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }

  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[38]) {
      int handled = 0;
      CuteQListWidgetCall38 call = reinterpret_cast<CuteQListWidgetCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectAll();
  }

  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[39]) {
      int handled = 0;
      CuteQListWidgetCall39 call = reinterpret_cast<CuteQListWidgetCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }

  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[40]) {
      int handled = 0;
      CuteQListWidgetCall40 call = reinterpret_cast<CuteQListWidgetCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }

  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[41]) {
      int handled = 0;
      CuteQListWidgetCall41 call = reinterpret_cast<CuteQListWidgetCall41>(taken[41]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }

  //  void QAbstractItemView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[42]) {
      int handled = 0;
      CuteQListWidgetCall42 call = reinterpret_cast<CuteQListWidgetCall42>(taken[42]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarAction(action);
  }

  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[43]) {
      int handled = 0;
      CuteQListWidgetCall43 call = reinterpret_cast<CuteQListWidgetCall43>(taken[43]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }

  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[44]) {
      int handled = 0;
      CuteQListWidgetCall44 call = reinterpret_cast<CuteQListWidgetCall44>(taken[44]);
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
    if (taken[45]) {
      int handled = 0;
      CuteQListWidgetCall45 call = reinterpret_cast<CuteQListWidgetCall45>(taken[45]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }

  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[46]) {
      int handled = 0;
      CuteQListWidgetCall46 call = reinterpret_cast<CuteQListWidgetCall46>(taken[46]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }

  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[47]) {
      int handled = 0;
      CuteQListWidgetCall47 call = reinterpret_cast<CuteQListWidgetCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQListWidgetCall48 call = reinterpret_cast<CuteQListWidgetCall48>(taken[48]);
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
    if (taken[49]) {
      int handled = 0;
      CuteQListWidgetCall49 call = reinterpret_cast<CuteQListWidgetCall49>(taken[49]);
      int given = call(this, &index, event, &handled);
      if (handled) return QFlags<QItemSelectionModel::SelectionFlag>::fromInt(given);
    }
    return QAbstractItemView::selectionCommand(index, event);
  }

  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[50]) {
      int handled = 0;
      CuteQListWidgetCall50 call = reinterpret_cast<CuteQListWidgetCall50>(taken[50]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }

  //  bool QAbstractItemView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQListWidgetCall51 call = reinterpret_cast<CuteQListWidgetCall51>(taken[51]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::viewportEvent(event);
  }

  //  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQListWidgetCall52 call = reinterpret_cast<CuteQListWidgetCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }

  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQListWidgetCall53 call = reinterpret_cast<CuteQListWidgetCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseDoubleClickEvent(event);
  }

  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQListWidgetCall54 call = reinterpret_cast<CuteQListWidgetCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }

  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQListWidgetCall55 call = reinterpret_cast<CuteQListWidgetCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }

  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQListWidgetCall56 call = reinterpret_cast<CuteQListWidgetCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }

  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQListWidgetCall57 call = reinterpret_cast<CuteQListWidgetCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }

  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQListWidgetCall58 call = reinterpret_cast<CuteQListWidgetCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::inputMethodEvent(event);
  }

  //  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQListWidgetCall59 call = reinterpret_cast<CuteQListWidgetCall59>(taken[59]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }

  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQListWidgetCall60 call = reinterpret_cast<CuteQListWidgetCall60>(taken[60]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }

  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[61]) {
      int handled = 0;
      CuteQListWidgetCall61 call = reinterpret_cast<CuteQListWidgetCall61>(taken[61]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }

  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[62]) {
      int handled = 0;
      CuteQListWidgetCall62 call = reinterpret_cast<CuteQListWidgetCall62>(taken[62]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }

  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQListWidgetCall63 call = reinterpret_cast<CuteQListWidgetCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQListWidgetCall64 call = reinterpret_cast<CuteQListWidgetCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[65]) {
      int handled = 0;
      CuteQListWidgetCall65 call = reinterpret_cast<CuteQListWidgetCall65>(taken[65]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[66]) {
      int handled = 0;
      CuteQListWidgetCall66 call = reinterpret_cast<CuteQListWidgetCall66>(taken[66]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[67]) {
      int handled = 0;
      CuteQListWidgetCall67 call = reinterpret_cast<CuteQListWidgetCall67>(taken[67]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[68]) {
      int handled = 0;
      CuteQListWidgetCall68 call = reinterpret_cast<CuteQListWidgetCall68>(taken[68]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQListWidgetCall69 call = reinterpret_cast<CuteQListWidgetCall69>(taken[69]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[70]) {
      int handled = 0;
      CuteQListWidgetCall70 call = reinterpret_cast<CuteQListWidgetCall70>(taken[70]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQListWidgetCall71 call = reinterpret_cast<CuteQListWidgetCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQListWidgetCall72 call = reinterpret_cast<CuteQListWidgetCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQListWidgetCall73 call = reinterpret_cast<CuteQListWidgetCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQListWidgetCall74 call = reinterpret_cast<CuteQListWidgetCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQListWidgetCall75 call = reinterpret_cast<CuteQListWidgetCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQListWidgetCall76 call = reinterpret_cast<CuteQListWidgetCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }

  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQListWidgetCall77 call = reinterpret_cast<CuteQListWidgetCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQListWidgetCall78 call = reinterpret_cast<CuteQListWidgetCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[79]) {
      int handled = 0;
      CuteQListWidgetCall79 call = reinterpret_cast<CuteQListWidgetCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQListWidgetCall80 call = reinterpret_cast<CuteQListWidgetCall80>(taken[80]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQListWidgetCall81 call = reinterpret_cast<CuteQListWidgetCall81>(taken[81]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[82]) {
      int handled = 0;
      CuteQListWidgetCall82 call = reinterpret_cast<CuteQListWidgetCall82>(taken[82]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[83]) {
      int handled = 0;
      CuteQListWidgetCall83 call = reinterpret_cast<CuteQListWidgetCall83>(taken[83]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      CuteQListWidgetCall84 call = reinterpret_cast<CuteQListWidgetCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[85]) {
      int handled = 0;
      CuteQListWidgetCall85 call = reinterpret_cast<CuteQListWidgetCall85>(taken[85]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[86]) {
      int handled = 0;
      CuteQListWidgetCall86 call = reinterpret_cast<CuteQListWidgetCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[87]) {
      int handled = 0;
      CuteQListWidgetCall87 call = reinterpret_cast<CuteQListWidgetCall87>(taken[87]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QListWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QListWidget10metaObjectEv(
    const QListWidget *self) {
  return self->metaObject();
}

//  QString QListWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QListWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QListWidget::tr(s, c, n));
}

//  QListWidget::QListWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QListWidget *ritual_ZN11QListWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQListWidget(parent);
}

//  QListWidget::~QListWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidgetD1Ev(QListWidget *self) {
  delete self;
}

//  void QListWidget::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget17setSelectionModelEP19QItemSelectionModel(
    QListWidget *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  QListWidgetItem *QListWidget::item(int row) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget4itemEi(
    const QListWidget *self,
    int row) {
  return self->item(row);
}

//  int QListWidget::row(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget3rowEPK15QListWidgetItem(
    const QListWidget *self,
    const QListWidgetItem *item) {
  return self->row(item);
}

//  void QListWidget::insertItem(int row, QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget10insertItemEiP15QListWidgetItem(
    QListWidget *self,
    int row,
    QListWidgetItem *item) {
  self->insertItem(row, item);
}

//  void QListWidget::insertItem(int row, const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget10insertItemEiRK7QString(
    QListWidget *self,
    int row,
    const QString *label) {
  self->insertItem(row, *label);
}

//  void QListWidget::addItem(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget7addItemERK7QString(
    QListWidget *self,
    const QString *label) {
  self->addItem(*label);
}

//  void QListWidget::addItem(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget7addItemEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->addItem(item);
}

//  QListWidgetItem *QListWidget::takeItem(int row)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN11QListWidget8takeItemEi(
    QListWidget *self,
    int row) {
  return self->takeItem(row);
}

//  int QListWidget::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget5countEv(const QListWidget *self) {
  return self->count();
}

//  QListWidgetItem *QListWidget::currentItem() const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget11currentItemEv(
    const QListWidget *self) {
  return self->currentItem();
}

//  void QListWidget::setCurrentItem(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget14setCurrentItemEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->setCurrentItem(item);
}

//  void QListWidget::setCurrentItem(QListWidgetItem *item,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget14setCurrentItemEP15QListWidgetItem6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListWidget *self,
    QListWidgetItem *item,
    int command) {
  self->setCurrentItem(
      item,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  int QListWidget::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget10currentRowEv(const QListWidget *self) {
  return self->currentRow();
}

//  void QListWidget::setCurrentRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget13setCurrentRowEi(QListWidget *self, int row) {
  self->setCurrentRow(row);
}

//  void QListWidget::setCurrentRow(int row,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget13setCurrentRowEi6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListWidget *self,
    int row,
    int command) {
  self->setCurrentRow(
      row,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QListWidgetItem *QListWidget::itemAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget6itemAtERK6QPoint(
    const QListWidget *self,
    const QPoint *p) {
  return self->itemAt(*p);
}

//  QListWidgetItem *QListWidget::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget6itemAtEii(
    const QListWidget *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QRect QListWidget::visualItemRect(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QListWidget14visualItemRectEPK15QListWidgetItem(
    const QListWidget *self,
    const QListWidgetItem *item) {
  return new QRect(self->visualItemRect(item));
}

//  void QListWidget::sortItems(Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget9sortItemsEN2Qt9SortOrderE(
    QListWidget *self,
    Qt::SortOrder order) {
  self->sortItems(order);
}

//  void QListWidget::setSortingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget17setSortingEnabledEb(
    QListWidget *self,
    bool enable) {
  self->setSortingEnabled(enable);
}

//  bool QListWidget::isSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QListWidget16isSortingEnabledEv(const QListWidget *self) {
  return self->isSortingEnabled();
}

//  void QListWidget::editItem(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget8editItemEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->editItem(item);
}

//  void QListWidget::openPersistentEditor(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget20openPersistentEditorEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->openPersistentEditor(item);
}

//  void QListWidget::closePersistentEditor(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget21closePersistentEditorEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->closePersistentEditor(item);
}

//  bool QListWidget::isPersistentEditorOpen(QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QListWidget22isPersistentEditorOpenEP15QListWidgetItem(
    const QListWidget *self,
    QListWidgetItem *item) {
  return self->isPersistentEditorOpen(item);
}

//  QWidget *QListWidget::itemWidget(QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QListWidget10itemWidgetEP15QListWidgetItem(
    const QListWidget *self,
    QListWidgetItem *item) {
  return self->itemWidget(item);
}

//  void QListWidget::setItemWidget(QListWidgetItem *item, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget13setItemWidgetEP15QListWidgetItemP7QWidget(
    QListWidget *self,
    QListWidgetItem *item,
    QWidget *widget) {
  self->setItemWidget(item, widget);
}

//  void QListWidget::removeItemWidget(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget16removeItemWidgetEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->removeItemWidget(item);
}

//  QModelIndex QListWidget::indexFromItem(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QListWidget13indexFromItemEPK15QListWidgetItem(
    const QListWidget *self,
    const QListWidgetItem *item) {
  return new QModelIndex(self->indexFromItem(item));
}

//  QListWidgetItem *QListWidget::itemFromIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget13itemFromIndexERK11QModelIndex(
    const QListWidget *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  void QListWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QListWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  Qt::DropActions QListWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget20supportedDragActionsEv(
    const QListWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QListWidget::scrollToItem(const QListWidgetItem *item,
//      QAbstractItemView::ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget12scrollToItemEPK15QListWidgetItemN17QAbstractItemView10ScrollHintE(
    QListWidget *self,
    const QListWidgetItem *item,
    QAbstractItemView::ScrollHint hint) {
  self->scrollToItem(item, hint);
}

//  void QListWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget5clearEv(QListWidget *self) {
  self->clear();
}

//  a Python function taken by a CuteQListWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QListWidget(
    QListWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQListWidget *>(self)->take(key, call);
}

//  void QListWidget::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QListWidget17setSelectionModelEP19QItemSelectionModel(
    QListWidget *self,
    QItemSelectionModel *selectionModel) {
  self->QListWidget::setSelectionModel(selectionModel);
}

//  void QListWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QListWidget9dropEventEP10QDropEvent(
    QListWidget *self,
    QDropEvent *event) {
  static_cast<OwnQListWidget *>(self)->OwnQListWidget::dropEvent(event);
}

//  bool QListWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QListWidget5eventEP6QEvent(
    QListWidget *self,
    QEvent *e) {
  return static_cast<OwnQListWidget *>(self)->OwnQListWidget::event(e);
}

//  bool QListWidget::dropMimeData(int index, const QMimeData *data,
//      Qt::DropAction action)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QListWidget12dropMimeDataEiPK9QMimeDataN2Qt10DropActionE(
    QListWidget *self,
    int index,
    const QMimeData *data,
    Qt::DropAction action) {
  return static_cast<OwnQListWidget *>(self)->OwnQListWidget::dropMimeData(
      index,
      data,
      action);
}

//  Qt::DropActions QListWidget::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QListWidget20supportedDropActionsEv(
    const QListWidget *self) {
  return static_cast<int>(
      static_cast<const OwnQListWidget *>(self)->OwnQListWidget::supportedDropActions().toInt());
}
