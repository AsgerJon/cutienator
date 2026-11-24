//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlistview.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(listview)
#if QT_CONFIG(listview)
#include <QtWidgets/qlistview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QListView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQListView : QListView {
  using QListView::event;
  using QListView::scrollContentsBy;
  using QListView::rowsInserted;
  using QListView::rowsAboutToBeRemoved;
  using QListView::mouseMoveEvent;
  using QListView::mouseReleaseEvent;
  using QListView::wheelEvent;
  using QListView::timerEvent;
  using QListView::resizeEvent;
  using QListView::dragMoveEvent;
  using QListView::dragLeaveEvent;
  using QListView::dropEvent;
  using QListView::startDrag;
  using QListView::initViewItemOption;
  using QListView::paintEvent;
  using QListView::horizontalOffset;
  using QListView::verticalOffset;
  using QListView::setSelection;
  using QListView::visualRegionForSelection;
  using QListView::updateGeometries;
  using QListView::isIndexHidden;
  using QListView::selectionChanged;
  using QListView::currentChanged;
  using QListView::viewportSizeHint;
};

//  A QListView that Python can take functions over in. Every QListView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRect * (*CuteQListViewCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall1)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QModelIndex * (*CuteQListViewCall2)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall3)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall4)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef bool (*CuteQListViewCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall7)(const void *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall8)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall9)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall10)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall13)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall14)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall15)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall16)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall17)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall18)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall19)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall20)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQListViewCall21)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQListViewCall22)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall23)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRegion * (*CuteQListViewCall24)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall25)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef bool (*CuteQListViewCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall27)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewCall28)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef const QSize * (*CuteQListViewCall29)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall30)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall31)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall32)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQListViewCall33)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQListViewCall34)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQListViewCall35)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQListViewCall36)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall37)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall38)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall39)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall40)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall41)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall42)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall44)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall45)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall46)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQListViewCall47)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQListViewCall48)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQListViewCall49)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQListViewCall50)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall51)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall52)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall53)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall54)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall55)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall56)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewCall57)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQListViewCall58)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQListViewCall59)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQListViewCall60)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQListViewCall61)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQListViewCall62)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQListViewCall63)(const void *, QEvent *, int *);
typedef void (*CuteQListViewCall64)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQListViewCall65)(const void *, int *);
typedef void (*CuteQListViewCall66)(const void *, bool, int *);
typedef int (*CuteQListViewCall67)(const void *, int, int *);
typedef bool (*CuteQListViewCall68)(const void *, int *);
typedef void * (*CuteQListViewCall69)(const void *, int *);
typedef void (*CuteQListViewCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQListViewCall71)(const void *, QEnterEvent *, int *);
typedef void (*CuteQListViewCall72)(const void *, QEvent *, int *);
typedef void (*CuteQListViewCall73)(const void *, QMoveEvent *, int *);
typedef void (*CuteQListViewCall74)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQListViewCall75)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQListViewCall76)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQListViewCall77)(const void *, QShowEvent *, int *);
typedef void (*CuteQListViewCall78)(const void *, QHideEvent *, int *);
typedef int (*CuteQListViewCall79)(const void *, int, int *);
typedef void (*CuteQListViewCall80)(const void *, QPainter *, int *);
typedef void * (*CuteQListViewCall81)(const void *, QPoint *, int *);
typedef void * (*CuteQListViewCall82)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQListViewCall83)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQListViewCall84)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQListViewCall85)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQListViewCall86)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQListView : public QListView {
public:
  using QListView::QListView;
  void *taken[87] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
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
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
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
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[75] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[76] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[83] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[84] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[85] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[86] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QRect QListView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQListViewCall0 call = reinterpret_cast<CuteQListViewCall0>(taken[0]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QListView::visualRect(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[1]) {
      int handled = 0;
      CuteQListViewCall1 call = reinterpret_cast<CuteQListViewCall1>(taken[1]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QListView::scrollTo(index, hint);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QModelIndex QListView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQListViewCall2 call = reinterpret_cast<CuteQListViewCall2>(taken[2]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QListView::indexAt(p);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[3]) {
      int handled = 0;
      CuteQListViewCall3 call = reinterpret_cast<CuteQListViewCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::doItemsLayout();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::reset()
  void reset() override {
    if (taken[4]) {
      int handled = 0;
      CuteQListViewCall4 call = reinterpret_cast<CuteQListViewCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::reset();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQListViewCall5 call = reinterpret_cast<CuteQListViewCall5>(taken[5]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QListView::setRootIndex(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
  //  bool QListView::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQListViewCall6 call = reinterpret_cast<CuteQListViewCall6>(taken[6]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QListView::event(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
  //  void QListView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[7]) {
      int handled = 0;
      CuteQListViewCall7 call = reinterpret_cast<CuteQListViewCall7>(taken[7]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QListView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[8]) {
      int handled = 0;
      CuteQListViewCall8 call = reinterpret_cast<CuteQListViewCall8>(taken[8]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QListView::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::rowsAboutToBeRemoved(const QModelIndex &parent, int
  //      start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[9]) {
      int handled = 0;
      CuteQListViewCall9 call = reinterpret_cast<CuteQListViewCall9>(taken[9]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QListView::rowsAboutToBeRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(listview)
  //  void QListView::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQListViewCall10 call = reinterpret_cast<CuteQListViewCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QListView::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQListViewCall11 call = reinterpret_cast<CuteQListViewCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
  //  void QListView::wheelEvent(QWheelEvent *e)
  void wheelEvent(QWheelEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQListViewCall12 call = reinterpret_cast<CuteQListViewCall12>(taken[12]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::wheelEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
  //  void QListView::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[13]) {
      int handled = 0;
      CuteQListViewCall13 call = reinterpret_cast<CuteQListViewCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::timerEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(listview)
  //  void QListView::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQListViewCall14 call = reinterpret_cast<CuteQListViewCall14>(taken[14]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::resizeEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[15]) {
      int handled = 0;
      CuteQListViewCall15 call = reinterpret_cast<CuteQListViewCall15>(taken[15]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dragMoveEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dragLeaveEvent(QDragLeaveEvent *e)
  void dragLeaveEvent(QDragLeaveEvent *e) override {
    if (taken[16]) {
      int handled = 0;
      CuteQListViewCall16 call = reinterpret_cast<CuteQListViewCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dragLeaveEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dropEvent(QDropEvent *e)
  void dropEvent(QDropEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQListViewCall17 call = reinterpret_cast<CuteQListViewCall17>(taken[17]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::dropEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::startDrag(Qt::DropActions supportedActions)
  void startDrag(Qt::DropActions supportedActions) override {
    if (taken[18]) {
      int handled = 0;
      CuteQListViewCall18 call = reinterpret_cast<CuteQListViewCall18>(taken[18]);
      call(this, static_cast<int>(supportedActions.toInt()), &handled);
      if (handled) return;
    }
    QListView::startDrag(supportedActions);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::initViewItemOption(QStyleOptionViewItem *option)
  //      const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQListViewCall19 call = reinterpret_cast<CuteQListViewCall19>(taken[19]);
      call(this, option, &handled);
      if (handled) return;
    }
    QListView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(listview)
  //  void QListView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[20]) {
      int handled = 0;
      CuteQListViewCall20 call = reinterpret_cast<CuteQListViewCall20>(taken[20]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::paintEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  int QListView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQListViewCall21 call = reinterpret_cast<CuteQListViewCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QListView::horizontalOffset();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  int QListView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQListViewCall22 call = reinterpret_cast<CuteQListViewCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QListView::verticalOffset();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[23]) {
      int handled = 0;
      CuteQListViewCall23 call = reinterpret_cast<CuteQListViewCall23>(taken[23]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QListView::setSelection(rect, command);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QRegion QListView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQListViewCall24 call = reinterpret_cast<CuteQListViewCall24>(taken[24]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QListView::visualRegionForSelection(selection);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::updateGeometries()
  void updateGeometries() override {
    if (taken[25]) {
      int handled = 0;
      CuteQListViewCall25 call = reinterpret_cast<CuteQListViewCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QListView::updateGeometries();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  bool QListView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQListViewCall26 call = reinterpret_cast<CuteQListViewCall26>(taken[26]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QListView::isIndexHidden(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::selectionChanged(const QItemSelection &selected,
  //      const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[27]) {
      int handled = 0;
      CuteQListViewCall27 call = reinterpret_cast<CuteQListViewCall27>(taken[27]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QListView::selectionChanged(selected, deselected);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[28]) {
      int handled = 0;
      CuteQListViewCall28 call = reinterpret_cast<CuteQListViewCall28>(taken[28]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QListView::currentChanged(current, previous);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
  //  QSize QListView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQListViewCall29 call = reinterpret_cast<CuteQListViewCall29>(taken[29]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QListView::viewportSizeHint();
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[30]) {
      int handled = 0;
      CuteQListViewCall30 call = reinterpret_cast<CuteQListViewCall30>(taken[30]);
      call(this, model, &handled);
      if (handled) return;
    }
    QAbstractItemView::setModel(model);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[31]) {
      int handled = 0;
      CuteQListViewCall31 call = reinterpret_cast<CuteQListViewCall31>(taken[31]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QAbstractItemView::setSelectionModel(selectionModel);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[32]) {
      int handled = 0;
      CuteQListViewCall32 call = reinterpret_cast<CuteQListViewCall32>(taken[32]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQListViewCall33 call = reinterpret_cast<CuteQListViewCall33>(taken[33]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQListViewCall34 call = reinterpret_cast<CuteQListViewCall34>(taken[34]);
      int given = call(this, column, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForColumn(column);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
  //      QModelIndex &index) const
  QAbstractItemDelegate *itemDelegateForIndex(
      const QModelIndex &index) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQListViewCall35 call = reinterpret_cast<CuteQListViewCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQListViewCall36 call = reinterpret_cast<CuteQListViewCall36>(taken[36]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[37]) {
      int handled = 0;
      CuteQListViewCall37 call = reinterpret_cast<CuteQListViewCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectAll();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[38]) {
      int handled = 0;
      CuteQListViewCall38 call = reinterpret_cast<CuteQListViewCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[39]) {
      int handled = 0;
      CuteQListViewCall39 call = reinterpret_cast<CuteQListViewCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[40]) {
      int handled = 0;
      CuteQListViewCall40 call = reinterpret_cast<CuteQListViewCall40>(taken[40]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[41]) {
      int handled = 0;
      CuteQListViewCall41 call = reinterpret_cast<CuteQListViewCall41>(taken[41]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[42]) {
      int handled = 0;
      CuteQListViewCall42 call = reinterpret_cast<CuteQListViewCall42>(taken[42]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[43]) {
      int handled = 0;
      CuteQListViewCall43 call = reinterpret_cast<CuteQListViewCall43>(taken[43]);
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
    if (taken[44]) {
      int handled = 0;
      CuteQListViewCall44 call = reinterpret_cast<CuteQListViewCall44>(taken[44]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[45]) {
      int handled = 0;
      CuteQListViewCall45 call = reinterpret_cast<CuteQListViewCall45>(taken[45]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[46]) {
      int handled = 0;
      CuteQListViewCall46 call = reinterpret_cast<CuteQListViewCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQListViewCall47 call = reinterpret_cast<CuteQListViewCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQListViewCall48 call = reinterpret_cast<CuteQListViewCall48>(taken[48]);
      int given = call(this, &index, event, &handled);
      if (handled) return QFlags<QItemSelectionModel::SelectionFlag>::fromInt(given);
    }
    return QAbstractItemView::selectionCommand(index, event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[49]) {
      int handled = 0;
      CuteQListViewCall49 call = reinterpret_cast<CuteQListViewCall49>(taken[49]);
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
    if (taken[50]) {
      int handled = 0;
      CuteQListViewCall50 call = reinterpret_cast<CuteQListViewCall50>(taken[50]);
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
    if (taken[51]) {
      int handled = 0;
      CuteQListViewCall51 call = reinterpret_cast<CuteQListViewCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQListViewCall52 call = reinterpret_cast<CuteQListViewCall52>(taken[52]);
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
    if (taken[53]) {
      int handled = 0;
      CuteQListViewCall53 call = reinterpret_cast<CuteQListViewCall53>(taken[53]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[54]) {
      int handled = 0;
      CuteQListViewCall54 call = reinterpret_cast<CuteQListViewCall54>(taken[54]);
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
      CuteQListViewCall55 call = reinterpret_cast<CuteQListViewCall55>(taken[55]);
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
      CuteQListViewCall56 call = reinterpret_cast<CuteQListViewCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQListViewCall57 call = reinterpret_cast<CuteQListViewCall57>(taken[57]);
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
    if (taken[58]) {
      int handled = 0;
      CuteQListViewCall58 call = reinterpret_cast<CuteQListViewCall58>(taken[58]);
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
    if (taken[59]) {
      int handled = 0;
      CuteQListViewCall59 call = reinterpret_cast<CuteQListViewCall59>(taken[59]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[60]) {
      int handled = 0;
      CuteQListViewCall60 call = reinterpret_cast<CuteQListViewCall60>(taken[60]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[61]) {
      int handled = 0;
      CuteQListViewCall61 call = reinterpret_cast<CuteQListViewCall61>(taken[61]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
  void contextMenuEvent(QContextMenuEvent *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQListViewCall62 call = reinterpret_cast<CuteQListViewCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQListViewCall63 call = reinterpret_cast<CuteQListViewCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[64]) {
      int handled = 0;
      CuteQListViewCall64 call = reinterpret_cast<CuteQListViewCall64>(taken[64]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQListViewCall65 call = reinterpret_cast<CuteQListViewCall65>(taken[65]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[66]) {
      int handled = 0;
      CuteQListViewCall66 call = reinterpret_cast<CuteQListViewCall66>(taken[66]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[67]) {
      int handled = 0;
      CuteQListViewCall67 call = reinterpret_cast<CuteQListViewCall67>(taken[67]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[68]) {
      int handled = 0;
      CuteQListViewCall68 call = reinterpret_cast<CuteQListViewCall68>(taken[68]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQListViewCall69 call = reinterpret_cast<CuteQListViewCall69>(taken[69]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQListViewCall70 call = reinterpret_cast<CuteQListViewCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQListViewCall71 call = reinterpret_cast<CuteQListViewCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQListViewCall72 call = reinterpret_cast<CuteQListViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQListViewCall73 call = reinterpret_cast<CuteQListViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQListViewCall74 call = reinterpret_cast<CuteQListViewCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQListViewCall75 call = reinterpret_cast<CuteQListViewCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQListViewCall76 call = reinterpret_cast<CuteQListViewCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQListViewCall77 call = reinterpret_cast<CuteQListViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQListViewCall78 call = reinterpret_cast<CuteQListViewCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQListViewCall79 call = reinterpret_cast<CuteQListViewCall79>(taken[79]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQListViewCall80 call = reinterpret_cast<CuteQListViewCall80>(taken[80]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQListViewCall81 call = reinterpret_cast<CuteQListViewCall81>(taken[81]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[82]) {
      int handled = 0;
      CuteQListViewCall82 call = reinterpret_cast<CuteQListViewCall82>(taken[82]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[83]) {
      int handled = 0;
      CuteQListViewCall83 call = reinterpret_cast<CuteQListViewCall83>(taken[83]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[84]) {
      int handled = 0;
      CuteQListViewCall84 call = reinterpret_cast<CuteQListViewCall84>(taken[84]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[85]) {
      int handled = 0;
      CuteQListViewCall85 call = reinterpret_cast<CuteQListViewCall85>(taken[85]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[86]) {
      int handled = 0;
      CuteQListViewCall86 call = reinterpret_cast<CuteQListViewCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

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
  return new CuteQListView(parent);
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

//  bool QListView::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QListView5eventEP6QEvent(QListView *self, QEvent *e) {
  return self->event(e);
}

//  void QListView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView16scrollContentsByEii(
    QListView *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QListView::resizeContents(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView14resizeContentsEii(
    QListView *self,
    int width,
    int height) {
  self->resizeContents(width, height);
}

//  QSize QListView::contentsSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QListView12contentsSizeEv(const QListView *self) {
  return new QSize(self->contentsSize());
}

//  void QListView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView12rowsInsertedERK11QModelIndexii(
    QListView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsInserted(*parent, start, end);
}

//  void QListView::rowsAboutToBeRemoved(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView20rowsAboutToBeRemovedERK11QModelIndexii(
    QListView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsAboutToBeRemoved(*parent, start, end);
}

//  void QListView::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView14mouseMoveEventEP11QMouseEvent(
    QListView *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QListView::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView17mouseReleaseEventEP11QMouseEvent(
    QListView *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

#if QT_CONFIG(wheelevent)
//  void QListView::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView10wheelEventEP11QWheelEvent(
    QListView *self,
    QWheelEvent *e) {
  self->wheelEvent(e);
}
#endif  // QT_CONFIG(wheelevent)

//  void QListView::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView10timerEventEP11QTimerEvent(
    QListView *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QListView::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView11resizeEventEP12QResizeEvent(
    QListView *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

#if QT_CONFIG(draganddrop)
//  void QListView::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView13dragMoveEventEP14QDragMoveEvent(
    QListView *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListView::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView14dragLeaveEventEP15QDragLeaveEvent(
    QListView *self,
    QDragLeaveEvent *e) {
  self->dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListView::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView9dropEventEP10QDropEvent(
    QListView *self,
    QDropEvent *e) {
  self->dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListView::startDrag(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView9startDragE6QFlagsIN2Qt10DropActionEE(
    QListView *self,
    int supportedActions) {
  self->startDrag(QFlags<Qt::DropAction>::fromInt(supportedActions));
}
#endif  // QT_CONFIG(draganddrop)

//  void QListView::initViewItemOption(QStyleOptionViewItem *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QListView18initViewItemOptionEP20QStyleOptionViewItem(
    const QListView *self,
    QStyleOptionViewItem *option) {
  self->initViewItemOption(option);
}

//  void QListView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView10paintEventEP11QPaintEvent(
    QListView *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  int QListView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView16horizontalOffsetEv(const QListView *self) {
  return self->horizontalOffset();
}

//  int QListView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView14verticalOffsetEv(const QListView *self) {
  return self->verticalOffset();
}

//  QModelIndex QListView::moveCursor(CursorAction cursorAction,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN9QListView10moveCursorEN17QAbstractItemView12CursorActionE6QFlagsIN2Qt16KeyboardModifierEE(
    QListView *self,
    QAbstractItemView::CursorAction cursorAction,
    int modifiers) {
  return new QModelIndex(
      self->moveCursor(
          cursorAction,
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}

//  QRect QListView::rectForIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QListView12rectForIndexERK11QModelIndex(
    const QListView *self,
    const QModelIndex *index) {
  return new QRect(self->rectForIndex(*index));
}

//  void QListView::setPositionForIndex(const QPoint &position, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView19setPositionForIndexERK6QPointRK11QModelIndex(
    QListView *self,
    const QPoint *position,
    const QModelIndex *index) {
  self->setPositionForIndex(*position, *index);
}

//  void QListView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListView *self,
    const QRect *rect,
    int command) {
  self->setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QListView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK9QListView24visualRegionForSelectionERK14QItemSelection(
    const QListView *self,
    const QItemSelection *selection) {
  return new QRegion(self->visualRegionForSelection(*selection));
}

//  QModelIndexList QListView::selectedIndexes() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK9QListView15selectedIndexesEv(
    const QListView *self) {
  return new QList<QModelIndex>(self->selectedIndexes());
}

//  void QListView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView16updateGeometriesEv(QListView *self) {
  self->updateGeometries();
}

//  bool QListView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QListView13isIndexHiddenERK11QModelIndex(
    const QListView *self,
    const QModelIndex *index) {
  return self->isIndexHidden(*index);
}

//  void QListView::selectionChanged(const QItemSelection &selected, const
//      QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView16selectionChangedERK14QItemSelectionS2_(
    QListView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  self->selectionChanged(*selected, *deselected);
}

//  void QListView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QListView14currentChangedERK11QModelIndexS2_(
    QListView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  self->currentChanged(*current, *previous);
}

//  QSize QListView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QListView16viewportSizeHintEv(const QListView *self) {
  return new QSize(self->viewportSizeHint());
}

//  int QListView::visualIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QListView11visualIndexERK11QModelIndex(
    const QListView *self,
    const QModelIndex *index) {
  return self->visualIndex(*index);
}

//  QListViewPrivate *QListView::d_func()
extern "C" Q_DECL_EXPORT
QListViewPrivate *ritual_ZN9QListView6d_funcEv(QListView *self) {
  return self->d_func();
}

//  const QListViewPrivate *QListView::d_func() const
extern "C" Q_DECL_EXPORT
const QListViewPrivate *ritual_ZNK9QListView6d_funcEv(
    const QListView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQListView, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QListView(QListView *self, const char *key, void *call) {
  return static_cast<CuteQListView *>(self)->take(key, call);
}

//  QRect QListView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK9QListView10visualRectERK11QModelIndex(
    const QListView *self,
    const QModelIndex *index) {
  return new QRect(self->QListView::visualRect(*index));
}

//  void QListView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QListView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->QListView::scrollTo(*index, hint);
}

//  QModelIndex QListView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK9QListView7indexAtERK6QPoint(
    const QListView *self,
    const QPoint *p) {
  return new QModelIndex(self->QListView::indexAt(*p));
}

//  void QListView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView13doItemsLayoutEv(QListView *self) {
  self->QListView::doItemsLayout();
}

//  void QListView::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView5resetEv(QListView *self) {
  self->QListView::reset();
}

//  void QListView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView12setRootIndexERK11QModelIndex(
    QListView *self,
    const QModelIndex *index) {
  self->QListView::setRootIndex(*index);
}

//  bool QListView::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QListView5eventEP6QEvent(QListView *self, QEvent *e) {
  return static_cast<OwnQListView *>(self)->OwnQListView::event(e);
}

//  void QListView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView16scrollContentsByEii(
    QListView *self,
    int dx,
    int dy) {
  static_cast<OwnQListView *>(self)->OwnQListView::scrollContentsBy(dx, dy);
}

//  void QListView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView12rowsInsertedERK11QModelIndexii(
    QListView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQListView *>(self)->OwnQListView::rowsInserted(
      *parent,
      start,
      end);
}

//  void QListView::rowsAboutToBeRemoved(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView20rowsAboutToBeRemovedERK11QModelIndexii(
    QListView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQListView *>(self)->OwnQListView::rowsAboutToBeRemoved(
      *parent,
      start,
      end);
}

//  void QListView::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView14mouseMoveEventEP11QMouseEvent(
    QListView *self,
    QMouseEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::mouseMoveEvent(e);
}

//  void QListView::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView17mouseReleaseEventEP11QMouseEvent(
    QListView *self,
    QMouseEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::mouseReleaseEvent(e);
}

#if QT_CONFIG(wheelevent)
//  void QListView::wheelEvent(QWheelEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView10wheelEventEP11QWheelEvent(
    QListView *self,
    QWheelEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::wheelEvent(e);
}
#endif  // QT_CONFIG(wheelevent)

//  void QListView::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView10timerEventEP11QTimerEvent(
    QListView *self,
    QTimerEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::timerEvent(e);
}

//  void QListView::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView11resizeEventEP12QResizeEvent(
    QListView *self,
    QResizeEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::resizeEvent(e);
}

#if QT_CONFIG(draganddrop)
//  void QListView::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView13dragMoveEventEP14QDragMoveEvent(
    QListView *self,
    QDragMoveEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListView::dragLeaveEvent(QDragLeaveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView14dragLeaveEventEP15QDragLeaveEvent(
    QListView *self,
    QDragLeaveEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::dragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListView::dropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView9dropEventEP10QDropEvent(
    QListView *self,
    QDropEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::dropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListView::startDrag(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView9startDragE6QFlagsIN2Qt10DropActionEE(
    QListView *self,
    int supportedActions) {
  static_cast<OwnQListView *>(self)->OwnQListView::startDrag(
      QFlags<Qt::DropAction>::fromInt(supportedActions));
}
#endif  // QT_CONFIG(draganddrop)

//  void QListView::initViewItemOption(QStyleOptionViewItem *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QListView18initViewItemOptionEP20QStyleOptionViewItem(
    const QListView *self,
    QStyleOptionViewItem *option) {
  static_cast<const OwnQListView *>(self)->OwnQListView::initViewItemOption(
      option);
}

//  void QListView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView10paintEventEP11QPaintEvent(
    QListView *self,
    QPaintEvent *e) {
  static_cast<OwnQListView *>(self)->OwnQListView::paintEvent(e);
}

//  int QListView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QListView16horizontalOffsetEv(const QListView *self) {
  return static_cast<const OwnQListView *>(self)->OwnQListView::horizontalOffset();
}

//  int QListView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QListView14verticalOffsetEv(const QListView *self) {
  return static_cast<const OwnQListView *>(self)->OwnQListView::verticalOffset();
}

//  void QListView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListView *self,
    const QRect *rect,
    int command) {
  static_cast<OwnQListView *>(self)->OwnQListView::setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QListView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK9QListView24visualRegionForSelectionERK14QItemSelection(
    const QListView *self,
    const QItemSelection *selection) {
  return new QRegion(
      static_cast<const OwnQListView *>(self)->OwnQListView::visualRegionForSelection(
          *selection));
}

//  void QListView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView16updateGeometriesEv(QListView *self) {
  static_cast<OwnQListView *>(self)->OwnQListView::updateGeometries();
}

//  bool QListView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QListView13isIndexHiddenERK11QModelIndex(
    const QListView *self,
    const QModelIndex *index) {
  return static_cast<const OwnQListView *>(self)->OwnQListView::isIndexHidden(
      *index);
}

//  void QListView::selectionChanged(const QItemSelection &selected, const
//      QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView16selectionChangedERK14QItemSelectionS2_(
    QListView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  static_cast<OwnQListView *>(self)->OwnQListView::selectionChanged(
      *selected,
      *deselected);
}

//  void QListView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QListView14currentChangedERK11QModelIndexS2_(
    QListView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  static_cast<OwnQListView *>(self)->OwnQListView::currentChanged(
      *current,
      *previous);
}

//  QSize QListView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QListView16viewportSizeHintEv(const QListView *self) {
  return new QSize(
      static_cast<const OwnQListView *>(self)->OwnQListView::viewportSizeHint());
}

#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(listview)
