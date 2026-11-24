//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(treewidget)
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
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTreeWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTreeWidget : QTreeWidget {
  using QTreeWidget::event;
  using QTreeWidget::dropMimeData;
  using QTreeWidget::supportedDropActions;
  using QTreeWidget::dropEvent;
};

//  A QTreeWidget that Python can take functions over in. Every QTreeWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treewidget)
typedef void (*CuteQTreeWidgetCall0)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeWidgetCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
typedef bool (*CuteQTreeWidgetCall2)(const void *, QTreeWidgetItem *, int, const QMimeData *, int, int *);
#endif  // QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
typedef int (*CuteQTreeWidgetCall3)(const void *, int *);
#endif  // QT_CONFIG(treewidget)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treewidget)
typedef void (*CuteQTreeWidgetCall4)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treewidget)
typedef void (*CuteQTreeWidgetCall5)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall7)(const void *, const QString *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRect * (*CuteQTreeWidgetCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall9)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QModelIndex * (*CuteQTreeWidgetCall10)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall11)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall12)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall13)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall14)(const void *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall15)(const void *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall16)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall17)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeWidgetCall18)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeWidgetCall19)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall20)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRegion * (*CuteQTreeWidgetCall21)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall22)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall23)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall24)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall25)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall26)(const void *, QPainter *, const QRect *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall27)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall28)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall29)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall30)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall31)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
typedef bool (*CuteQTreeWidgetCall33)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall34)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
typedef const QSize * (*CuteQTreeWidgetCall35)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeWidgetCall36)(const void *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall37)(const void *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef bool (*CuteQTreeWidgetCall38)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall39)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetCall40)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQTreeWidgetCall41)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQTreeWidgetCall42)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQTreeWidgetCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall44)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall45)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall46)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall47)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall48)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall49)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall50)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeWidgetCall51)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQTreeWidgetCall52)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTreeWidgetCall53)(const void *, int, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall54)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeWidgetCall55)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall56)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall57)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall58)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall59)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall60)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetCall61)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeWidgetCall62)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTreeWidgetCall63)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTreeWidgetCall64)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeWidgetCall65)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeWidgetCall66)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeWidgetCall67)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQTreeWidgetCall68)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTreeWidgetCall69)(const void *, int *);
typedef void (*CuteQTreeWidgetCall70)(const void *, bool, int *);
typedef int (*CuteQTreeWidgetCall71)(const void *, int, int *);
typedef bool (*CuteQTreeWidgetCall72)(const void *, int *);
typedef void * (*CuteQTreeWidgetCall73)(const void *, int *);
typedef void (*CuteQTreeWidgetCall74)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTreeWidgetCall75)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTreeWidgetCall76)(const void *, QEvent *, int *);
typedef void (*CuteQTreeWidgetCall77)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTreeWidgetCall78)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQTreeWidgetCall79)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQTreeWidgetCall80)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQTreeWidgetCall81)(const void *, QShowEvent *, int *);
typedef void (*CuteQTreeWidgetCall82)(const void *, QHideEvent *, int *);
typedef int (*CuteQTreeWidgetCall83)(const void *, int, int *);
typedef void (*CuteQTreeWidgetCall84)(const void *, QPainter *, int *);
typedef void * (*CuteQTreeWidgetCall85)(const void *, QPoint *, int *);
typedef void * (*CuteQTreeWidgetCall86)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeWidgetCall87)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeWidgetCall88)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeWidgetCall89)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeWidgetCall90)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTreeWidget : public QTreeWidget {
public:
  using QTreeWidget::QTreeWidget;
  void *taken[91] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN11QTreeWidget12dropMimeDataEP15QTreeWidgetItemiPK9QMimeDataN2Qt10DropActionE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZNK11QTreeWidget20supportedDropActionsEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treewidget)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK9QTreeView7drawRowEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK9QTreeView12drawBranchesEP8QPainterRK5QRectRK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[63] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[64] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[65] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[66] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[67] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[78] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[79] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[80] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[86] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[87] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[88] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[89] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[90] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treewidget)
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
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treewidget)
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
#endif  // QT_CONFIG(treewidget)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(treewidget)
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
#endif  // QT_CONFIG(treewidget)

#if QT_CONFIG(treewidget)
  //  Qt::DropActions QTreeWidget::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTreeWidgetCall3 call = reinterpret_cast<CuteQTreeWidgetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QTreeWidget::supportedDropActions();
  }
#endif  // QT_CONFIG(treewidget)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treewidget)
  //  void QTreeWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTreeWidgetCall4 call = reinterpret_cast<CuteQTreeWidgetCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treewidget)
  //  void QTreeWidget::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTreeWidgetCall5 call = reinterpret_cast<CuteQTreeWidgetCall5>(taken[5]);
      call(this, model, &handled);
      if (handled) return;
    }
    QTreeWidget::setModel(model);
  }
#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTreeWidgetCall6 call = reinterpret_cast<CuteQTreeWidgetCall6>(taken[6]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QTreeView::setRootIndex(index);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTreeWidgetCall7 call = reinterpret_cast<CuteQTreeWidgetCall7>(taken[7]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QTreeView::keyboardSearch(search);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  QRect QTreeView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTreeWidgetCall8 call = reinterpret_cast<CuteQTreeWidgetCall8>(taken[8]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::visualRect(index);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTreeWidgetCall9 call = reinterpret_cast<CuteQTreeWidgetCall9>(taken[9]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QTreeView::scrollTo(index, hint);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  QModelIndex QTreeView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTreeWidgetCall10 call = reinterpret_cast<CuteQTreeWidgetCall10>(taken[10]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::indexAt(p);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[11]) {
      int handled = 0;
      CuteQTreeWidgetCall11 call = reinterpret_cast<CuteQTreeWidgetCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::doItemsLayout();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::reset()
  void reset() override {
    if (taken[12]) {
      int handled = 0;
      CuteQTreeWidgetCall12 call = reinterpret_cast<CuteQTreeWidgetCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::reset();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::selectAll()
  void selectAll() override {
    if (taken[13]) {
      int handled = 0;
      CuteQTreeWidgetCall13 call = reinterpret_cast<CuteQTreeWidgetCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::selectAll();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTreeWidgetCall14 call = reinterpret_cast<CuteQTreeWidgetCall14>(taken[14]);
      call(this, value, &handled);
      if (handled) return;
    }
    QTreeView::verticalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
  //  void QTreeView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTreeWidgetCall15 call = reinterpret_cast<CuteQTreeWidgetCall15>(taken[15]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QTreeView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTreeWidgetCall16 call = reinterpret_cast<CuteQTreeWidgetCall16>(taken[16]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QTreeView::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::rowsAboutToBeRemoved(const QModelIndex &parent, int
  //      start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTreeWidgetCall17 call = reinterpret_cast<CuteQTreeWidgetCall17>(taken[17]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QTreeView::rowsAboutToBeRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  int QTreeView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTreeWidgetCall18 call = reinterpret_cast<CuteQTreeWidgetCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTreeView::horizontalOffset();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  int QTreeView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQTreeWidgetCall19 call = reinterpret_cast<CuteQTreeWidgetCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTreeView::verticalOffset();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTreeWidgetCall20 call = reinterpret_cast<CuteQTreeWidgetCall20>(taken[20]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QTreeView::setSelection(rect, command);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  QRegion QTreeView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTreeWidgetCall21 call = reinterpret_cast<CuteQTreeWidgetCall21>(taken[21]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::visualRegionForSelection(selection);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(treeview)
  //  void QTreeView::changeEvent(QEvent *event)
  void changeEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTreeWidgetCall22 call = reinterpret_cast<CuteQTreeWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::changeEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
  //  void QTreeView::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTreeWidgetCall23 call = reinterpret_cast<CuteQTreeWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::timerEvent(event);
  }
#endif  // QT_CONFIG(treeview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(treeview)
  //  void QTreeView::paintEvent(QPaintEvent *event)
  void paintEvent(QPaintEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTreeWidgetCall24 call = reinterpret_cast<CuteQTreeWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::paintEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::drawRow(QPainter *painter, const QStyleOptionViewItem
  //      &options, const QModelIndex &index) const
  void drawRow(
      QPainter *painter,
      const QStyleOptionViewItem &options,
      const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTreeWidgetCall25 call = reinterpret_cast<CuteQTreeWidgetCall25>(taken[25]);
      call(this, painter, &options, &index, &handled);
      if (handled) return;
    }
    QTreeView::drawRow(painter, options, index);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::drawBranches(QPainter *painter, const QRect &rect,
  //      const QModelIndex &index) const
  void drawBranches(
      QPainter *painter,
      const QRect &rect,
      const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQTreeWidgetCall26 call = reinterpret_cast<CuteQTreeWidgetCall26>(taken[26]);
      call(this, painter, &rect, &index, &handled);
      if (handled) return;
    }
    QTreeView::drawBranches(painter, rect, index);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTreeWidgetCall27 call = reinterpret_cast<CuteQTreeWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTreeWidgetCall28 call = reinterpret_cast<CuteQTreeWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQTreeWidgetCall29 call = reinterpret_cast<CuteQTreeWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQTreeWidgetCall30 call = reinterpret_cast<CuteQTreeWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTreeWidgetCall31 call = reinterpret_cast<CuteQTreeWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treeview)
  //  void QTreeView::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTreeWidgetCall32 call = reinterpret_cast<CuteQTreeWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
  //  bool QTreeView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTreeWidgetCall33 call = reinterpret_cast<CuteQTreeWidgetCall33>(taken[33]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QTreeView::viewportEvent(event);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::updateGeometries()
  void updateGeometries() override {
    if (taken[34]) {
      int handled = 0;
      CuteQTreeWidgetCall34 call = reinterpret_cast<CuteQTreeWidgetCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeView::updateGeometries();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
  //  QSize QTreeView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQTreeWidgetCall35 call = reinterpret_cast<CuteQTreeWidgetCall35>(taken[35]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QTreeView::viewportSizeHint();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  int QTreeView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQTreeWidgetCall36 call = reinterpret_cast<CuteQTreeWidgetCall36>(taken[36]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QTreeView::sizeHintForColumn(column);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTreeWidgetCall37 call = reinterpret_cast<CuteQTreeWidgetCall37>(taken[37]);
      call(this, action, &handled);
      if (handled) return;
    }
    QTreeView::horizontalScrollbarAction(action);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  bool QTreeView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQTreeWidgetCall38 call = reinterpret_cast<CuteQTreeWidgetCall38>(taken[38]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTreeView::isIndexHidden(index);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[39]) {
      int handled = 0;
      CuteQTreeWidgetCall39 call = reinterpret_cast<CuteQTreeWidgetCall39>(taken[39]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QTreeView::selectionChanged(selected, deselected);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[40]) {
      int handled = 0;
      CuteQTreeWidgetCall40 call = reinterpret_cast<CuteQTreeWidgetCall40>(taken[40]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QTreeView::currentChanged(current, previous);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[41]) {
      int handled = 0;
      CuteQTreeWidgetCall41 call = reinterpret_cast<CuteQTreeWidgetCall41>(taken[41]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQTreeWidgetCall42 call = reinterpret_cast<CuteQTreeWidgetCall42>(taken[42]);
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
    if (taken[43]) {
      int handled = 0;
      CuteQTreeWidgetCall43 call = reinterpret_cast<CuteQTreeWidgetCall43>(taken[43]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[44]) {
      int handled = 0;
      CuteQTreeWidgetCall44 call = reinterpret_cast<CuteQTreeWidgetCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[45]) {
      int handled = 0;
      CuteQTreeWidgetCall45 call = reinterpret_cast<CuteQTreeWidgetCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[46]) {
      int handled = 0;
      CuteQTreeWidgetCall46 call = reinterpret_cast<CuteQTreeWidgetCall46>(taken[46]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[47]) {
      int handled = 0;
      CuteQTreeWidgetCall47 call = reinterpret_cast<CuteQTreeWidgetCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQTreeWidgetCall48 call = reinterpret_cast<CuteQTreeWidgetCall48>(taken[48]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[49]) {
      int handled = 0;
      CuteQTreeWidgetCall49 call = reinterpret_cast<CuteQTreeWidgetCall49>(taken[49]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[50]) {
      int handled = 0;
      CuteQTreeWidgetCall50 call = reinterpret_cast<CuteQTreeWidgetCall50>(taken[50]);
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
    if (taken[51]) {
      int handled = 0;
      CuteQTreeWidgetCall51 call = reinterpret_cast<CuteQTreeWidgetCall51>(taken[51]);
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
    if (taken[52]) {
      int handled = 0;
      CuteQTreeWidgetCall52 call = reinterpret_cast<CuteQTreeWidgetCall52>(taken[52]);
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
    if (taken[53]) {
      int handled = 0;
      CuteQTreeWidgetCall53 call = reinterpret_cast<CuteQTreeWidgetCall53>(taken[53]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QAbstractItemView::startDrag(supportedActions);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::initViewItemOption(QStyleOptionViewItem
  //      *option) const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[54]) {
      int handled = 0;
      CuteQTreeWidgetCall54 call = reinterpret_cast<CuteQTreeWidgetCall54>(taken[54]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractItemView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[55]) {
      int handled = 0;
      CuteQTreeWidgetCall55 call = reinterpret_cast<CuteQTreeWidgetCall55>(taken[55]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQTreeWidgetCall56 call = reinterpret_cast<CuteQTreeWidgetCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQTreeWidgetCall57 call = reinterpret_cast<CuteQTreeWidgetCall57>(taken[57]);
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
    if (taken[58]) {
      int handled = 0;
      CuteQTreeWidgetCall58 call = reinterpret_cast<CuteQTreeWidgetCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQTreeWidgetCall59 call = reinterpret_cast<CuteQTreeWidgetCall59>(taken[59]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[60]) {
      int handled = 0;
      CuteQTreeWidgetCall60 call = reinterpret_cast<CuteQTreeWidgetCall60>(taken[60]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::resizeEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[61]) {
      int handled = 0;
      CuteQTreeWidgetCall61 call = reinterpret_cast<CuteQTreeWidgetCall61>(taken[61]);
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
    if (taken[62]) {
      int handled = 0;
      CuteQTreeWidgetCall62 call = reinterpret_cast<CuteQTreeWidgetCall62>(taken[62]);
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
    if (taken[63]) {
      int handled = 0;
      CuteQTreeWidgetCall63 call = reinterpret_cast<CuteQTreeWidgetCall63>(taken[63]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[64]) {
      int handled = 0;
      CuteQTreeWidgetCall64 call = reinterpret_cast<CuteQTreeWidgetCall64>(taken[64]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[65]) {
      int handled = 0;
      CuteQTreeWidgetCall65 call = reinterpret_cast<CuteQTreeWidgetCall65>(taken[65]);
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
    if (taken[66]) {
      int handled = 0;
      CuteQTreeWidgetCall66 call = reinterpret_cast<CuteQTreeWidgetCall66>(taken[66]);
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
    if (taken[67]) {
      int handled = 0;
      CuteQTreeWidgetCall67 call = reinterpret_cast<CuteQTreeWidgetCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[68]) {
      int handled = 0;
      CuteQTreeWidgetCall68 call = reinterpret_cast<CuteQTreeWidgetCall68>(taken[68]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQTreeWidgetCall69 call = reinterpret_cast<CuteQTreeWidgetCall69>(taken[69]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[70]) {
      int handled = 0;
      CuteQTreeWidgetCall70 call = reinterpret_cast<CuteQTreeWidgetCall70>(taken[70]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[71]) {
      int handled = 0;
      CuteQTreeWidgetCall71 call = reinterpret_cast<CuteQTreeWidgetCall71>(taken[71]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[72]) {
      int handled = 0;
      CuteQTreeWidgetCall72 call = reinterpret_cast<CuteQTreeWidgetCall72>(taken[72]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[73]) {
      int handled = 0;
      CuteQTreeWidgetCall73 call = reinterpret_cast<CuteQTreeWidgetCall73>(taken[73]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQTreeWidgetCall74 call = reinterpret_cast<CuteQTreeWidgetCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQTreeWidgetCall75 call = reinterpret_cast<CuteQTreeWidgetCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQTreeWidgetCall76 call = reinterpret_cast<CuteQTreeWidgetCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQTreeWidgetCall77 call = reinterpret_cast<CuteQTreeWidgetCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQTreeWidgetCall78 call = reinterpret_cast<CuteQTreeWidgetCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[79]) {
      int handled = 0;
      CuteQTreeWidgetCall79 call = reinterpret_cast<CuteQTreeWidgetCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[80]) {
      int handled = 0;
      CuteQTreeWidgetCall80 call = reinterpret_cast<CuteQTreeWidgetCall80>(taken[80]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[81]) {
      int handled = 0;
      CuteQTreeWidgetCall81 call = reinterpret_cast<CuteQTreeWidgetCall81>(taken[81]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[82]) {
      int handled = 0;
      CuteQTreeWidgetCall82 call = reinterpret_cast<CuteQTreeWidgetCall82>(taken[82]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[83]) {
      int handled = 0;
      CuteQTreeWidgetCall83 call = reinterpret_cast<CuteQTreeWidgetCall83>(taken[83]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[84]) {
      int handled = 0;
      CuteQTreeWidgetCall84 call = reinterpret_cast<CuteQTreeWidgetCall84>(taken[84]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[85]) {
      int handled = 0;
      CuteQTreeWidgetCall85 call = reinterpret_cast<CuteQTreeWidgetCall85>(taken[85]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[86]) {
      int handled = 0;
      CuteQTreeWidgetCall86 call = reinterpret_cast<CuteQTreeWidgetCall86>(taken[86]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[87]) {
      int handled = 0;
      CuteQTreeWidgetCall87 call = reinterpret_cast<CuteQTreeWidgetCall87>(taken[87]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[88]) {
      int handled = 0;
      CuteQTreeWidgetCall88 call = reinterpret_cast<CuteQTreeWidgetCall88>(taken[88]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[89]) {
      int handled = 0;
      CuteQTreeWidgetCall89 call = reinterpret_cast<CuteQTreeWidgetCall89>(taken[89]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[90]) {
      int handled = 0;
      CuteQTreeWidgetCall90 call = reinterpret_cast<CuteQTreeWidgetCall90>(taken[90]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
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

//  void QTreeWidget::insertTopLevelItems(int index, const
//      QList<QTreeWidgetItem *> &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget19insertTopLevelItemsEiRK5QListIP15QTreeWidgetItemE(
    QTreeWidget *self,
    int index,
    const QList<QTreeWidgetItem *> *items) {
  self->insertTopLevelItems(index, *items);
}

//  void QTreeWidget::addTopLevelItems(const QList<QTreeWidgetItem *> &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget16addTopLevelItemsERK5QListIP15QTreeWidgetItemE(
    QTreeWidget *self,
    const QList<QTreeWidgetItem *> *items) {
  self->addTopLevelItems(*items);
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

//  void QTreeWidget::setHeaderLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget15setHeaderLabelsERK5QListI7QStringE(
    QTreeWidget *self,
    const QList<QString> *labels) {
  self->setHeaderLabels(*labels);
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

//  QList<QTreeWidgetItem *> QTreeWidget::selectedItems() const
extern "C" Q_DECL_EXPORT
QList<QTreeWidgetItem *> *ritual_ZNK11QTreeWidget13selectedItemsEv(
    const QTreeWidget *self) {
  return new QList<QTreeWidgetItem *>(self->selectedItems());
}

//  QList<QTreeWidgetItem *> QTreeWidget::findItems(const QString &text,
//      Qt::MatchFlags flags, int column) const
extern "C" Q_DECL_EXPORT
QList<QTreeWidgetItem *> *ritual_ZNK11QTreeWidget9findItemsERK7QString6QFlagsIN2Qt9MatchFlagEEi(
    const QTreeWidget *self,
    const QString *text,
    int flags,
    int column) {
  return new QList<QTreeWidgetItem *>(
      self->findItems(
          *text,
          QFlags<Qt::MatchFlag>::fromInt(flags),
          column));
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

#if QT_CONFIG(draganddrop)
//  Qt::DropActions QTreeWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget20supportedDragActionsEv(
    const QTreeWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QTreeWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QTreeWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}
#endif  // QT_CONFIG(draganddrop)

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

//  bool QTreeWidget::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTreeWidget5eventEP6QEvent(QTreeWidget *self, QEvent *e) {
  return self->event(e);
}

//  QStringList QTreeWidget::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QTreeWidget9mimeTypesEv(
    const QTreeWidget *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QTreeWidget::mimeData(const QList<QTreeWidgetItem *> &items)
//      const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK11QTreeWidget8mimeDataERK5QListIP15QTreeWidgetItemE(
    const QTreeWidget *self,
    const QList<QTreeWidgetItem *> *items) {
  return self->mimeData(*items);
}

//  bool QTreeWidget::dropMimeData(QTreeWidgetItem *parent, int index, const
//      QMimeData *data, Qt::DropAction action)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTreeWidget12dropMimeDataEP15QTreeWidgetItemiPK9QMimeDataN2Qt10DropActionE(
    QTreeWidget *self,
    QTreeWidgetItem *parent,
    int index,
    const QMimeData *data,
    Qt::DropAction action) {
  return self->dropMimeData(parent, index, data, action);
}

//  Qt::DropActions QTreeWidget::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget20supportedDropActionsEv(
    const QTreeWidget *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

#if QT_CONFIG(draganddrop)
//  void QTreeWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget9dropEventEP10QDropEvent(
    QTreeWidget *self,
    QDropEvent *event) {
  self->dropEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  void QTreeWidget::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget8setModelEP18QAbstractItemModel(
    QTreeWidget *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QTreeWidgetPrivate *QTreeWidget::d_func()
extern "C" Q_DECL_EXPORT
QTreeWidgetPrivate *ritual_ZN11QTreeWidget6d_funcEv(QTreeWidget *self) {
  return self->d_func();
}

//  const QTreeWidgetPrivate *QTreeWidget::d_func() const
extern "C" Q_DECL_EXPORT
const QTreeWidgetPrivate *ritual_ZNK11QTreeWidget6d_funcEv(
    const QTreeWidget *self) {
  return self->d_func();
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

//  Qt::DropActions QTreeWidget::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QTreeWidget20supportedDropActionsEv(
    const QTreeWidget *self) {
  return static_cast<int>(
      static_cast<const OwnQTreeWidget *>(self)->OwnQTreeWidget::supportedDropActions().toInt());
}

#if QT_CONFIG(draganddrop)
//  void QTreeWidget::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTreeWidget9dropEventEP10QDropEvent(
    QTreeWidget *self,
    QDropEvent *event) {
  static_cast<OwnQTreeWidget *>(self)->OwnQTreeWidget::dropEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  void QTreeWidget::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTreeWidget8setModelEP18QAbstractItemModel(
    QTreeWidget *self,
    QAbstractItemModel *model) {
  self->QTreeWidget::setModel(model);
}

#endif  // QT_CONFIG(treewidget)
