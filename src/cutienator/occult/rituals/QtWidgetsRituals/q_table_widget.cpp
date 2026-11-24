//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(tablewidget)
#include <QtWidgets/qtablewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTableWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTableWidget : QTableWidget {
  using QTableWidget::event;
  using QTableWidget::dropMimeData;
  using QTableWidget::supportedDropActions;
  using QTableWidget::dropEvent;
};

//  A QTableWidget that Python can take functions over in. Every QTableWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableWidgetCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tablewidget)
typedef bool (*CuteQTableWidgetCall1)(const void *, int, int, const QMimeData *, int, int *);
#endif  // QT_CONFIG(tablewidget)
#if QT_CONFIG(tablewidget)
typedef int (*CuteQTableWidgetCall2)(const void *, int *);
#endif  // QT_CONFIG(tablewidget)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(tablewidget)
typedef void (*CuteQTableWidgetCall3)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tablewidget)
typedef void (*CuteQTableWidgetCall4)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall6)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall7)(const void *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef const QRect * (*CuteQTableWidgetCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall9)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef const QModelIndex * (*CuteQTableWidgetCall10)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall11)(const void *, int, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall12)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall13)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(tableview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall14)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef int (*CuteQTableWidgetCall15)(const void *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef int (*CuteQTableWidgetCall16)(const void *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall17)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef const QRegion * (*CuteQTableWidgetCall18)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall19)(const void *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(tableview)
typedef const QSize * (*CuteQTableWidgetCall20)(const void *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef int (*CuteQTableWidgetCall21)(const void *, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef int (*CuteQTableWidgetCall22)(const void *, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall23)(const void *, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall24)(const void *, int, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef bool (*CuteQTableWidgetCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall26)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef void (*CuteQTableWidgetCall27)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall28)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQTableWidgetCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQTableWidgetCall30)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall31)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall32)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall33)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall34)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall35)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall36)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall37)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall38)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall39)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall40)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall41)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTableWidgetCall42)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQTableWidgetCall43)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTableWidgetCall44)(const void *, int, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTableWidgetCall45)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTableWidgetCall46)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall47)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall48)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall49)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall50)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall51)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall52)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall53)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall54)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall55)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall56)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall57)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetCall58)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTableWidgetCall59)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTableWidgetCall60)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTableWidgetCall61)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTableWidgetCall62)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTableWidgetCall63)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTableWidgetCall64)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQTableWidgetCall65)(const void *, QEvent *, int *);
typedef void (*CuteQTableWidgetCall66)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTableWidgetCall67)(const void *, int *);
typedef void (*CuteQTableWidgetCall68)(const void *, bool, int *);
typedef int (*CuteQTableWidgetCall69)(const void *, int, int *);
typedef bool (*CuteQTableWidgetCall70)(const void *, int *);
typedef void * (*CuteQTableWidgetCall71)(const void *, int *);
typedef void (*CuteQTableWidgetCall72)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTableWidgetCall73)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTableWidgetCall74)(const void *, QEvent *, int *);
typedef void (*CuteQTableWidgetCall75)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTableWidgetCall76)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQTableWidgetCall77)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQTableWidgetCall78)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQTableWidgetCall79)(const void *, QShowEvent *, int *);
typedef void (*CuteQTableWidgetCall80)(const void *, QHideEvent *, int *);
typedef int (*CuteQTableWidgetCall81)(const void *, int, int *);
typedef void (*CuteQTableWidgetCall82)(const void *, QPainter *, int *);
typedef void * (*CuteQTableWidgetCall83)(const void *, QPoint *, int *);
typedef void * (*CuteQTableWidgetCall84)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetCall85)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetCall86)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetCall87)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTableWidgetCall88)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTableWidget : public QTableWidget {
public:
  using QTableWidget::QTableWidget;
  void *taken[89] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN12QTableWidget12dropMimeDataEiiPK9QMimeDataN2Qt10DropActionE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZNK12QTableWidget20supportedDropActionsEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tablewidget)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[63] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[64] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[76] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[77] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[78] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[84] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[85] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[86] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[87] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[88] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tablewidget)
  //  bool QTableWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTableWidgetCall0 call = reinterpret_cast<CuteQTableWidgetCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QTableWidget::event(e);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(tablewidget)
  //  bool QTableWidget::dropMimeData(int row, int column, const QMimeData
  //      *data, Qt::DropAction action)
  bool dropMimeData(
      int row,
      int column,
      const QMimeData *data,
      Qt::DropAction action) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTableWidgetCall1 call = reinterpret_cast<CuteQTableWidgetCall1>(taken[1]);
      bool given = call(this, row, column, data, static_cast<int>(action), &handled);
      if (handled) return given;
    }
    return QTableWidget::dropMimeData(row, column, data, action);
  }
#endif  // QT_CONFIG(tablewidget)

#if QT_CONFIG(tablewidget)
  //  Qt::DropActions QTableWidget::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTableWidgetCall2 call = reinterpret_cast<CuteQTableWidgetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QTableWidget::supportedDropActions();
  }
#endif  // QT_CONFIG(tablewidget)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(tablewidget)
  //  void QTableWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTableWidgetCall3 call = reinterpret_cast<CuteQTableWidgetCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTableWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tablewidget)
  //  void QTableWidget::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTableWidgetCall4 call = reinterpret_cast<CuteQTableWidgetCall4>(taken[4]);
      call(this, model, &handled);
      if (handled) return;
    }
    QTableWidget::setModel(model);
  }
#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTableWidgetCall5 call = reinterpret_cast<CuteQTableWidgetCall5>(taken[5]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QTableView::setRootIndex(index);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTableWidgetCall6 call = reinterpret_cast<CuteQTableWidgetCall6>(taken[6]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QTableView::setSelectionModel(selectionModel);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[7]) {
      int handled = 0;
      CuteQTableWidgetCall7 call = reinterpret_cast<CuteQTableWidgetCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QTableView::doItemsLayout();
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  QRect QTableView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTableWidgetCall8 call = reinterpret_cast<CuteQTableWidgetCall8>(taken[8]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTableView::visualRect(index);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTableWidgetCall9 call = reinterpret_cast<CuteQTableWidgetCall9>(taken[9]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QTableView::scrollTo(index, hint);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  QModelIndex QTableView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTableWidgetCall10 call = reinterpret_cast<CuteQTableWidgetCall10>(taken[10]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QTableView::indexAt(p);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(tableview)
  //  void QTableView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTableWidgetCall11 call = reinterpret_cast<CuteQTableWidgetCall11>(taken[11]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QTableView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::initViewItemOption(QStyleOptionViewItem *option)
  //      const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTableWidgetCall12 call = reinterpret_cast<CuteQTableWidgetCall12>(taken[12]);
      call(this, option, &handled);
      if (handled) return;
    }
    QTableView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(tableview)
  //  void QTableView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTableWidgetCall13 call = reinterpret_cast<CuteQTableWidgetCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QTableView::paintEvent(e);
  }
#endif  // QT_CONFIG(tableview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(tableview)
  //  void QTableView::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTableWidgetCall14 call = reinterpret_cast<CuteQTableWidgetCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTableView::timerEvent(event);
  }
#endif  // QT_CONFIG(tableview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  int QTableView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQTableWidgetCall15 call = reinterpret_cast<CuteQTableWidgetCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTableView::horizontalOffset();
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  int QTableView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTableWidgetCall16 call = reinterpret_cast<CuteQTableWidgetCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTableView::verticalOffset();
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTableWidgetCall17 call = reinterpret_cast<CuteQTableWidgetCall17>(taken[17]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QTableView::setSelection(rect, command);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  QRegion QTableView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTableWidgetCall18 call = reinterpret_cast<CuteQTableWidgetCall18>(taken[18]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QTableView::visualRegionForSelection(selection);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::updateGeometries()
  void updateGeometries() override {
    if (taken[19]) {
      int handled = 0;
      CuteQTableWidgetCall19 call = reinterpret_cast<CuteQTableWidgetCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QTableView::updateGeometries();
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(tableview)
  //  QSize QTableView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQTableWidgetCall20 call = reinterpret_cast<CuteQTableWidgetCall20>(taken[20]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTableView::viewportSizeHint();
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  int QTableView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTableWidgetCall21 call = reinterpret_cast<CuteQTableWidgetCall21>(taken[21]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QTableView::sizeHintForRow(row);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  int QTableView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTableWidgetCall22 call = reinterpret_cast<CuteQTableWidgetCall22>(taken[22]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QTableView::sizeHintForColumn(column);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTableWidgetCall23 call = reinterpret_cast<CuteQTableWidgetCall23>(taken[23]);
      call(this, action, &handled);
      if (handled) return;
    }
    QTableView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTableWidgetCall24 call = reinterpret_cast<CuteQTableWidgetCall24>(taken[24]);
      call(this, action, &handled);
      if (handled) return;
    }
    QTableView::horizontalScrollbarAction(action);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  bool QTableView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTableWidgetCall25 call = reinterpret_cast<CuteQTableWidgetCall25>(taken[25]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTableView::isIndexHidden(index);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTableWidgetCall26 call = reinterpret_cast<CuteQTableWidgetCall26>(taken[26]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QTableView::selectionChanged(selected, deselected);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
  //  void QTableView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTableWidgetCall27 call = reinterpret_cast<CuteQTableWidgetCall27>(taken[27]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QTableView::currentChanged(current, previous);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTableWidgetCall28 call = reinterpret_cast<CuteQTableWidgetCall28>(taken[28]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQTableWidgetCall29 call = reinterpret_cast<CuteQTableWidgetCall29>(taken[29]);
      void * given = call(this, &index, &handled);
      if (handled) return static_cast<QAbstractItemDelegate *>(given);
    }
    return QAbstractItemView::itemDelegateForIndex(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
  //      query) const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQTableWidgetCall30 call = reinterpret_cast<CuteQTableWidgetCall30>(taken[30]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::reset()
  void reset() override {
    if (taken[31]) {
      int handled = 0;
      CuteQTableWidgetCall31 call = reinterpret_cast<CuteQTableWidgetCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::reset();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[32]) {
      int handled = 0;
      CuteQTableWidgetCall32 call = reinterpret_cast<CuteQTableWidgetCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectAll();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::rowsInserted(const QModelIndex &parent, int
  //      start, int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTableWidgetCall33 call = reinterpret_cast<CuteQTableWidgetCall33>(taken[33]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemView::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex
  //      &parent, int start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[34]) {
      int handled = 0;
      CuteQTableWidgetCall34 call = reinterpret_cast<CuteQTableWidgetCall34>(taken[34]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemView::rowsAboutToBeRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[35]) {
      int handled = 0;
      CuteQTableWidgetCall35 call = reinterpret_cast<CuteQTableWidgetCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[36]) {
      int handled = 0;
      CuteQTableWidgetCall36 call = reinterpret_cast<CuteQTableWidgetCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTableWidgetCall37 call = reinterpret_cast<CuteQTableWidgetCall37>(taken[37]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[38]) {
      int handled = 0;
      CuteQTableWidgetCall38 call = reinterpret_cast<CuteQTableWidgetCall38>(taken[38]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::closeEditor(QWidget *editor,
  //      QAbstractItemDelegate::EndEditHint hint)
  void closeEditor(
      QWidget *editor,
      QAbstractItemDelegate::EndEditHint hint) override {
    if (taken[39]) {
      int handled = 0;
      CuteQTableWidgetCall39 call = reinterpret_cast<CuteQTableWidgetCall39>(taken[39]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[40]) {
      int handled = 0;
      CuteQTableWidgetCall40 call = reinterpret_cast<CuteQTableWidgetCall40>(taken[40]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[41]) {
      int handled = 0;
      CuteQTableWidgetCall41 call = reinterpret_cast<CuteQTableWidgetCall41>(taken[41]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::editorDestroyed(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
  //      trigger, QEvent *event)
  bool edit(
      const QModelIndex &index,
      QAbstractItemView::EditTrigger trigger,
      QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTableWidgetCall42 call = reinterpret_cast<CuteQTableWidgetCall42>(taken[42]);
      bool given = call(this, &index, static_cast<int>(trigger), event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::edit(index, trigger, event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QItemSelectionModel::SelectionFlags
  //      QAbstractItemView::selectionCommand(const QModelIndex &index,
  //      const QEvent *event) const
  QItemSelectionModel::SelectionFlags selectionCommand(
      const QModelIndex &index,
      const QEvent *event) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQTableWidgetCall43 call = reinterpret_cast<CuteQTableWidgetCall43>(taken[43]);
      int given = call(this, &index, event, &handled);
      if (handled) return QFlags<QItemSelectionModel::SelectionFlag>::fromInt(given);
    }
    return QAbstractItemView::selectionCommand(index, event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
  //  void QAbstractItemView::startDrag(Qt::DropActions supportedActions)
  void startDrag(Qt::DropActions supportedActions) override {
    if (taken[44]) {
      int handled = 0;
      CuteQTableWidgetCall44 call = reinterpret_cast<CuteQTableWidgetCall44>(taken[44]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QAbstractItemView::startDrag(supportedActions);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[45]) {
      int handled = 0;
      CuteQTableWidgetCall45 call = reinterpret_cast<CuteQTableWidgetCall45>(taken[45]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTableWidgetCall46 call = reinterpret_cast<CuteQTableWidgetCall46>(taken[46]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::viewportEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTableWidgetCall47 call = reinterpret_cast<CuteQTableWidgetCall47>(taken[47]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQTableWidgetCall48 call = reinterpret_cast<CuteQTableWidgetCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQTableWidgetCall49 call = reinterpret_cast<CuteQTableWidgetCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQTableWidgetCall50 call = reinterpret_cast<CuteQTableWidgetCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQTableWidgetCall51 call = reinterpret_cast<CuteQTableWidgetCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQTableWidgetCall52 call = reinterpret_cast<CuteQTableWidgetCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQTableWidgetCall53 call = reinterpret_cast<CuteQTableWidgetCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQTableWidgetCall54 call = reinterpret_cast<CuteQTableWidgetCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQTableWidgetCall55 call = reinterpret_cast<CuteQTableWidgetCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQTableWidgetCall56 call = reinterpret_cast<CuteQTableWidgetCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQTableWidgetCall57 call = reinterpret_cast<CuteQTableWidgetCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::resizeEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQTableWidgetCall58 call = reinterpret_cast<CuteQTableWidgetCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::inputMethodEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQTableWidgetCall59 call = reinterpret_cast<CuteQTableWidgetCall59>(taken[59]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQTableWidgetCall60 call = reinterpret_cast<CuteQTableWidgetCall60>(taken[60]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[61]) {
      int handled = 0;
      CuteQTableWidgetCall61 call = reinterpret_cast<CuteQTableWidgetCall61>(taken[61]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[62]) {
      int handled = 0;
      CuteQTableWidgetCall62 call = reinterpret_cast<CuteQTableWidgetCall62>(taken[62]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQTableWidgetCall63 call = reinterpret_cast<CuteQTableWidgetCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::wheelEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQTableWidgetCall64 call = reinterpret_cast<CuteQTableWidgetCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQTableWidgetCall65 call = reinterpret_cast<CuteQTableWidgetCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[66]) {
      int handled = 0;
      CuteQTableWidgetCall66 call = reinterpret_cast<CuteQTableWidgetCall66>(taken[66]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[67]) {
      int handled = 0;
      CuteQTableWidgetCall67 call = reinterpret_cast<CuteQTableWidgetCall67>(taken[67]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[68]) {
      int handled = 0;
      CuteQTableWidgetCall68 call = reinterpret_cast<CuteQTableWidgetCall68>(taken[68]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[69]) {
      int handled = 0;
      CuteQTableWidgetCall69 call = reinterpret_cast<CuteQTableWidgetCall69>(taken[69]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[70]) {
      int handled = 0;
      CuteQTableWidgetCall70 call = reinterpret_cast<CuteQTableWidgetCall70>(taken[70]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[71]) {
      int handled = 0;
      CuteQTableWidgetCall71 call = reinterpret_cast<CuteQTableWidgetCall71>(taken[71]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQTableWidgetCall72 call = reinterpret_cast<CuteQTableWidgetCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQTableWidgetCall73 call = reinterpret_cast<CuteQTableWidgetCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQTableWidgetCall74 call = reinterpret_cast<CuteQTableWidgetCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQTableWidgetCall75 call = reinterpret_cast<CuteQTableWidgetCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQTableWidgetCall76 call = reinterpret_cast<CuteQTableWidgetCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQTableWidgetCall77 call = reinterpret_cast<CuteQTableWidgetCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQTableWidgetCall78 call = reinterpret_cast<CuteQTableWidgetCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[79]) {
      int handled = 0;
      CuteQTableWidgetCall79 call = reinterpret_cast<CuteQTableWidgetCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[80]) {
      int handled = 0;
      CuteQTableWidgetCall80 call = reinterpret_cast<CuteQTableWidgetCall80>(taken[80]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQTableWidgetCall81 call = reinterpret_cast<CuteQTableWidgetCall81>(taken[81]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[82]) {
      int handled = 0;
      CuteQTableWidgetCall82 call = reinterpret_cast<CuteQTableWidgetCall82>(taken[82]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[83]) {
      int handled = 0;
      CuteQTableWidgetCall83 call = reinterpret_cast<CuteQTableWidgetCall83>(taken[83]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[84]) {
      int handled = 0;
      CuteQTableWidgetCall84 call = reinterpret_cast<CuteQTableWidgetCall84>(taken[84]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[85]) {
      int handled = 0;
      CuteQTableWidgetCall85 call = reinterpret_cast<CuteQTableWidgetCall85>(taken[85]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[86]) {
      int handled = 0;
      CuteQTableWidgetCall86 call = reinterpret_cast<CuteQTableWidgetCall86>(taken[86]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[87]) {
      int handled = 0;
      CuteQTableWidgetCall87 call = reinterpret_cast<CuteQTableWidgetCall87>(taken[87]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[88]) {
      int handled = 0;
      CuteQTableWidgetCall88 call = reinterpret_cast<CuteQTableWidgetCall88>(taken[88]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTableWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QTableWidget10metaObjectEv(
    const QTableWidget *self) {
  return self->metaObject();
}

//  QString QTableWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTableWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTableWidget::tr(s, c, n));
}

//  QTableWidget::QTableWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZN12QTableWidgetC1EP7QWidget(QWidget *parent) {
  return new CuteQTableWidget(parent);
}

//  QTableWidget::QTableWidget(int rows, int columns, QWidget *parent)
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZN12QTableWidgetC1EiiP7QWidget(
    int rows,
    int columns,
    QWidget *parent) {
  return new CuteQTableWidget(rows, columns, parent);
}

//  QTableWidget::~QTableWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidgetD1Ev(QTableWidget *self) {
  delete self;
}

//  void QTableWidget::setRowCount(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget11setRowCountEi(QTableWidget *self, int rows) {
  self->setRowCount(rows);
}

//  int QTableWidget::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget8rowCountEv(const QTableWidget *self) {
  return self->rowCount();
}

//  void QTableWidget::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setColumnCountEi(
    QTableWidget *self,
    int columns) {
  self->setColumnCount(columns);
}

//  int QTableWidget::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget11columnCountEv(const QTableWidget *self) {
  return self->columnCount();
}

//  int QTableWidget::row(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget3rowEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return self->row(item);
}

//  int QTableWidget::column(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget6columnEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return self->column(item);
}

//  QTableWidgetItem *QTableWidget::item(int row, int column) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget4itemEii(
    const QTableWidget *self,
    int row,
    int column) {
  return self->item(row, column);
}

//  void QTableWidget::setItem(int row, int column, QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget7setItemEiiP16QTableWidgetItem(
    QTableWidget *self,
    int row,
    int column,
    QTableWidgetItem *item) {
  self->setItem(row, column, item);
}

//  QTableWidgetItem *QTableWidget::takeItem(int row, int column)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN12QTableWidget8takeItemEii(
    QTableWidget *self,
    int row,
    int column) {
  return self->takeItem(row, column);
}

//  QList<QTableWidgetItem *> QTableWidget::items(const QMimeData *data)
//      const
extern "C" Q_DECL_EXPORT
QList<QTableWidgetItem *> *ritual_ZNK12QTableWidget5itemsEPK9QMimeData(
    const QTableWidget *self,
    const QMimeData *data) {
  return new QList<QTableWidgetItem *>(self->items(data));
}

//  QModelIndex QTableWidget::indexFromItem(const QTableWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK12QTableWidget13indexFromItemEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return new QModelIndex(self->indexFromItem(item));
}

//  QTableWidgetItem *QTableWidget::itemFromIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget13itemFromIndexERK11QModelIndex(
    const QTableWidget *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  QTableWidgetItem *QTableWidget::verticalHeaderItem(int row) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget18verticalHeaderItemEi(
    const QTableWidget *self,
    int row) {
  return self->verticalHeaderItem(row);
}

//  void QTableWidget::setVerticalHeaderItem(int row, QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget21setVerticalHeaderItemEiP16QTableWidgetItem(
    QTableWidget *self,
    int row,
    QTableWidgetItem *item) {
  self->setVerticalHeaderItem(row, item);
}

//  QTableWidgetItem *QTableWidget::takeVerticalHeaderItem(int row)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN12QTableWidget22takeVerticalHeaderItemEi(
    QTableWidget *self,
    int row) {
  return self->takeVerticalHeaderItem(row);
}

//  QTableWidgetItem *QTableWidget::horizontalHeaderItem(int column) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget20horizontalHeaderItemEi(
    const QTableWidget *self,
    int column) {
  return self->horizontalHeaderItem(column);
}

//  void QTableWidget::setHorizontalHeaderItem(int column, QTableWidgetItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget23setHorizontalHeaderItemEiP16QTableWidgetItem(
    QTableWidget *self,
    int column,
    QTableWidgetItem *item) {
  self->setHorizontalHeaderItem(column, item);
}

//  QTableWidgetItem *QTableWidget::takeHorizontalHeaderItem(int column)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN12QTableWidget24takeHorizontalHeaderItemEi(
    QTableWidget *self,
    int column) {
  return self->takeHorizontalHeaderItem(column);
}

//  void QTableWidget::setVerticalHeaderLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget23setVerticalHeaderLabelsERK5QListI7QStringE(
    QTableWidget *self,
    const QList<QString> *labels) {
  self->setVerticalHeaderLabels(*labels);
}

//  void QTableWidget::setHorizontalHeaderLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget25setHorizontalHeaderLabelsERK5QListI7QStringE(
    QTableWidget *self,
    const QList<QString> *labels) {
  self->setHorizontalHeaderLabels(*labels);
}

//  int QTableWidget::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget10currentRowEv(const QTableWidget *self) {
  return self->currentRow();
}

//  int QTableWidget::currentColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget13currentColumnEv(const QTableWidget *self) {
  return self->currentColumn();
}

//  QTableWidgetItem *QTableWidget::currentItem() const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget11currentItemEv(
    const QTableWidget *self) {
  return self->currentItem();
}

//  void QTableWidget::setCurrentItem(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentItemEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->setCurrentItem(item);
}

//  void QTableWidget::setCurrentItem(QTableWidgetItem *item,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentItemEP16QTableWidgetItem6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTableWidget *self,
    QTableWidgetItem *item,
    int command) {
  self->setCurrentItem(
      item,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QTableWidget::setCurrentCell(int row, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentCellEii(
    QTableWidget *self,
    int row,
    int column) {
  self->setCurrentCell(row, column);
}

//  void QTableWidget::setCurrentCell(int row, int column,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentCellEii6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTableWidget *self,
    int row,
    int column,
    int command) {
  self->setCurrentCell(
      row,
      column,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QTableWidget::sortItems(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9sortItemsEiN2Qt9SortOrderE(
    QTableWidget *self,
    int column,
    Qt::SortOrder order) {
  self->sortItems(column, order);
}

//  void QTableWidget::setSortingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget17setSortingEnabledEb(
    QTableWidget *self,
    bool enable) {
  self->setSortingEnabled(enable);
}

//  bool QTableWidget::isSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTableWidget16isSortingEnabledEv(const QTableWidget *self) {
  return self->isSortingEnabled();
}

//  void QTableWidget::editItem(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget8editItemEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->editItem(item);
}

//  void QTableWidget::openPersistentEditor(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget20openPersistentEditorEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->openPersistentEditor(item);
}

//  void QTableWidget::closePersistentEditor(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget21closePersistentEditorEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->closePersistentEditor(item);
}

//  bool QTableWidget::isPersistentEditorOpen(QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTableWidget22isPersistentEditorOpenEP16QTableWidgetItem(
    const QTableWidget *self,
    QTableWidgetItem *item) {
  return self->isPersistentEditorOpen(item);
}

//  QWidget *QTableWidget::cellWidget(int row, int column) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK12QTableWidget10cellWidgetEii(
    const QTableWidget *self,
    int row,
    int column) {
  return self->cellWidget(row, column);
}

//  void QTableWidget::setCellWidget(int row, int column, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget13setCellWidgetEiiP7QWidget(
    QTableWidget *self,
    int row,
    int column,
    QWidget *widget) {
  self->setCellWidget(row, column, widget);
}

//  void QTableWidget::removeCellWidget(int row, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget16removeCellWidgetEii(
    QTableWidget *self,
    int row,
    int column) {
  self->removeCellWidget(row, column);
}

//  void QTableWidget::setRangeSelected(const QTableWidgetSelectionRange
//      &range, bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget16setRangeSelectedERK26QTableWidgetSelectionRangeb(
    QTableWidget *self,
    const QTableWidgetSelectionRange *range,
    bool select) {
  self->setRangeSelected(*range, select);
}

//  QList<QTableWidgetSelectionRange> QTableWidget::selectedRanges() const
extern "C" Q_DECL_EXPORT
QList<QTableWidgetSelectionRange> *ritual_ZNK12QTableWidget14selectedRangesEv(
    const QTableWidget *self) {
  return new QList<QTableWidgetSelectionRange>(self->selectedRanges());
}

//  QList<QTableWidgetItem *> QTableWidget::selectedItems() const
extern "C" Q_DECL_EXPORT
QList<QTableWidgetItem *> *ritual_ZNK12QTableWidget13selectedItemsEv(
    const QTableWidget *self) {
  return new QList<QTableWidgetItem *>(self->selectedItems());
}

//  QList<QTableWidgetItem *> QTableWidget::findItems(const QString &text,
//      Qt::MatchFlags flags) const
extern "C" Q_DECL_EXPORT
QList<QTableWidgetItem *> *ritual_ZNK12QTableWidget9findItemsERK7QString6QFlagsIN2Qt9MatchFlagEE(
    const QTableWidget *self,
    const QString *text,
    int flags) {
  return new QList<QTableWidgetItem *>(
      self->findItems(
          *text,
          QFlags<Qt::MatchFlag>::fromInt(flags)));
}

//  int QTableWidget::visualRow(int logicalRow) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget9visualRowEi(
    const QTableWidget *self,
    int logicalRow) {
  return self->visualRow(logicalRow);
}

//  int QTableWidget::visualColumn(int logicalColumn) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget12visualColumnEi(
    const QTableWidget *self,
    int logicalColumn) {
  return self->visualColumn(logicalColumn);
}

//  QTableWidgetItem *QTableWidget::itemAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget6itemAtERK6QPoint(
    const QTableWidget *self,
    const QPoint *p) {
  return self->itemAt(*p);
}

//  QTableWidgetItem *QTableWidget::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget6itemAtEii(
    const QTableWidget *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QRect QTableWidget::visualItemRect(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QTableWidget14visualItemRectEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return new QRect(self->visualItemRect(item));
}

//  const QTableWidgetItem *QTableWidget::itemPrototype() const
extern "C" Q_DECL_EXPORT
const QTableWidgetItem *ritual_ZNK12QTableWidget13itemPrototypeEv(
    const QTableWidget *self) {
  return self->itemPrototype();
}

//  void QTableWidget::setItemPrototype(const QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget16setItemPrototypeEPK16QTableWidgetItem(
    QTableWidget *self,
    const QTableWidgetItem *item) {
  self->setItemPrototype(item);
}

#if QT_CONFIG(draganddrop)
//  Qt::DropActions QTableWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget20supportedDragActionsEv(
    const QTableWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTableWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QTableWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}
#endif  // QT_CONFIG(draganddrop)

//  void QTableWidget::scrollToItem(const QTableWidgetItem *item,
//      QAbstractItemView::ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget12scrollToItemEPK16QTableWidgetItemN17QAbstractItemView10ScrollHintE(
    QTableWidget *self,
    const QTableWidgetItem *item,
    QAbstractItemView::ScrollHint hint) {
  self->scrollToItem(item, hint);
}

//  void QTableWidget::insertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9insertRowEi(QTableWidget *self, int row) {
  self->insertRow(row);
}

//  void QTableWidget::insertColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget12insertColumnEi(
    QTableWidget *self,
    int column) {
  self->insertColumn(column);
}

//  void QTableWidget::removeRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9removeRowEi(QTableWidget *self, int row) {
  self->removeRow(row);
}

//  void QTableWidget::removeColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget12removeColumnEi(
    QTableWidget *self,
    int column) {
  self->removeColumn(column);
}

//  void QTableWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget5clearEv(QTableWidget *self) {
  self->clear();
}

//  void QTableWidget::clearContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget13clearContentsEv(QTableWidget *self) {
  self->clearContents();
}

//  bool QTableWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QTableWidget5eventEP6QEvent(QTableWidget *self, QEvent *e) {
  return self->event(e);
}

//  QStringList QTableWidget::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK12QTableWidget9mimeTypesEv(
    const QTableWidget *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QTableWidget::mimeData(const QList<QTableWidgetItem *> &items)
//      const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK12QTableWidget8mimeDataERK5QListIP16QTableWidgetItemE(
    const QTableWidget *self,
    const QList<QTableWidgetItem *> *items) {
  return self->mimeData(*items);
}

//  bool QTableWidget::dropMimeData(int row, int column, const QMimeData
//      *data, Qt::DropAction action)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QTableWidget12dropMimeDataEiiPK9QMimeDataN2Qt10DropActionE(
    QTableWidget *self,
    int row,
    int column,
    const QMimeData *data,
    Qt::DropAction action) {
  return self->dropMimeData(row, column, data, action);
}

//  Qt::DropActions QTableWidget::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget20supportedDropActionsEv(
    const QTableWidget *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

#if QT_CONFIG(draganddrop)
//  void QTableWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9dropEventEP10QDropEvent(
    QTableWidget *self,
    QDropEvent *event) {
  self->dropEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  void QTableWidget::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget8setModelEP18QAbstractItemModel(
    QTableWidget *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QTableWidgetPrivate *QTableWidget::d_func()
extern "C" Q_DECL_EXPORT
QTableWidgetPrivate *ritual_ZN12QTableWidget6d_funcEv(QTableWidget *self) {
  return self->d_func();
}

//  const QTableWidgetPrivate *QTableWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QTableWidgetPrivate *ritual_ZNK12QTableWidget6d_funcEv(
    const QTableWidget *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTableWidget, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableWidget(
    QTableWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTableWidget *>(self)->take(key, call);
}

//  bool QTableWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QTableWidget5eventEP6QEvent(
    QTableWidget *self,
    QEvent *e) {
  return static_cast<OwnQTableWidget *>(self)->OwnQTableWidget::event(e);
}

//  bool QTableWidget::dropMimeData(int row, int column, const QMimeData
//      *data, Qt::DropAction action)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QTableWidget12dropMimeDataEiiPK9QMimeDataN2Qt10DropActionE(
    QTableWidget *self,
    int row,
    int column,
    const QMimeData *data,
    Qt::DropAction action) {
  return static_cast<OwnQTableWidget *>(self)->OwnQTableWidget::dropMimeData(
      row,
      column,
      data,
      action);
}

//  Qt::DropActions QTableWidget::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK12QTableWidget20supportedDropActionsEv(
    const QTableWidget *self) {
  return static_cast<int>(
      static_cast<const OwnQTableWidget *>(self)->OwnQTableWidget::supportedDropActions().toInt());
}

#if QT_CONFIG(draganddrop)
//  void QTableWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTableWidget9dropEventEP10QDropEvent(
    QTableWidget *self,
    QDropEvent *event) {
  static_cast<OwnQTableWidget *>(self)->OwnQTableWidget::dropEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  void QTableWidget::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QTableWidget8setModelEP18QAbstractItemModel(
    QTableWidget *self,
    QAbstractItemModel *model) {
  self->QTableWidget::setModel(model);
}

#endif  // QT_CONFIG(tablewidget)
