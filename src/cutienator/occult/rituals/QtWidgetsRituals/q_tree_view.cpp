//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreeview.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
#include <QtWidgets/qtreeview.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTreeView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTreeView : QTreeView {
  using QTreeView::verticalScrollbarValueChanged;
  using QTreeView::scrollContentsBy;
  using QTreeView::rowsInserted;
  using QTreeView::rowsAboutToBeRemoved;
  using QTreeView::horizontalOffset;
  using QTreeView::verticalOffset;
  using QTreeView::setSelection;
  using QTreeView::visualRegionForSelection;
  using QTreeView::changeEvent;
  using QTreeView::timerEvent;
  using QTreeView::paintEvent;
  using QTreeView::drawRow;
  using QTreeView::drawBranches;
  using QTreeView::mousePressEvent;
  using QTreeView::mouseReleaseEvent;
  using QTreeView::mouseDoubleClickEvent;
  using QTreeView::mouseMoveEvent;
  using QTreeView::keyPressEvent;
  using QTreeView::dragMoveEvent;
  using QTreeView::viewportEvent;
  using QTreeView::updateGeometries;
  using QTreeView::viewportSizeHint;
  using QTreeView::sizeHintForColumn;
  using QTreeView::horizontalScrollbarAction;
  using QTreeView::isIndexHidden;
  using QTreeView::selectionChanged;
  using QTreeView::currentChanged;
};

//  A QTreeView that Python can take functions over in. Every QTreeView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall0)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall2)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall3)(const void *, const QString *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRect * (*CuteQTreeViewCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall5)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QModelIndex * (*CuteQTreeViewCall6)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall7)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall8)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall9)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall10)(const void *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall11)(const void *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall12)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall13)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeViewCall14)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeViewCall15)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall16)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRegion * (*CuteQTreeViewCall17)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall18)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall19)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall20)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall21)(const void *, QPainter *, const QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall22)(const void *, QPainter *, const QRect *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall23)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall24)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall25)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall26)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall27)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall28)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
typedef bool (*CuteQTreeViewCall29)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall30)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
typedef const QSize * (*CuteQTreeViewCall31)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeViewCall32)(const void *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall33)(const void *, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef bool (*CuteQTreeViewCall34)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall35)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewCall36)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQTreeViewCall37)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQTreeViewCall38)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQTreeViewCall39)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall40)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall41)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall42)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall44)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall45)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall46)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeViewCall47)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQTreeViewCall48)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQTreeViewCall49)(const void *, int, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall50)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeViewCall51)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeViewCall52)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall53)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall54)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall55)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall56)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall57)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall58)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewCall59)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeViewCall60)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTreeViewCall61)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQTreeViewCall62)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeViewCall63)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeViewCall64)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeViewCall65)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQTreeViewCall66)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQTreeViewCall67)(const void *, int *);
typedef void (*CuteQTreeViewCall68)(const void *, bool, int *);
typedef int (*CuteQTreeViewCall69)(const void *, int, int *);
typedef bool (*CuteQTreeViewCall70)(const void *, int *);
typedef void * (*CuteQTreeViewCall71)(const void *, int *);
typedef void (*CuteQTreeViewCall72)(const void *, QKeyEvent *, int *);
typedef void (*CuteQTreeViewCall73)(const void *, QEnterEvent *, int *);
typedef void (*CuteQTreeViewCall74)(const void *, QEvent *, int *);
typedef void (*CuteQTreeViewCall75)(const void *, QMoveEvent *, int *);
typedef void (*CuteQTreeViewCall76)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQTreeViewCall77)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQTreeViewCall78)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQTreeViewCall79)(const void *, QShowEvent *, int *);
typedef void (*CuteQTreeViewCall80)(const void *, QHideEvent *, int *);
typedef int (*CuteQTreeViewCall81)(const void *, int, int *);
typedef void (*CuteQTreeViewCall82)(const void *, QPainter *, int *);
typedef void * (*CuteQTreeViewCall83)(const void *, QPoint *, int *);
typedef void * (*CuteQTreeViewCall84)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewCall85)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewCall86)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewCall87)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTreeViewCall88)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTreeView : public QTreeView {
public:
  using QTreeView::QTreeView;
  void *taken[89] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK9QTreeView7drawRowEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK9QTreeView12drawBranchesEP8QPainterRK5QRectRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
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
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[63] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[64] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[65] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
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

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTreeViewCall0 call = reinterpret_cast<CuteQTreeViewCall0>(taken[0]);
      call(this, model, &handled);
      if (handled) return;
    }
    QTreeView::setModel(model);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTreeViewCall1 call = reinterpret_cast<CuteQTreeViewCall1>(taken[1]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QTreeView::setRootIndex(index);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTreeViewCall2 call = reinterpret_cast<CuteQTreeViewCall2>(taken[2]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QTreeView::setSelectionModel(selectionModel);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTreeViewCall3 call = reinterpret_cast<CuteQTreeViewCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQTreeViewCall4 call = reinterpret_cast<CuteQTreeViewCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQTreeViewCall5 call = reinterpret_cast<CuteQTreeViewCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQTreeViewCall6 call = reinterpret_cast<CuteQTreeViewCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQTreeViewCall7 call = reinterpret_cast<CuteQTreeViewCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQTreeViewCall8 call = reinterpret_cast<CuteQTreeViewCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQTreeViewCall9 call = reinterpret_cast<CuteQTreeViewCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQTreeViewCall10 call = reinterpret_cast<CuteQTreeViewCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQTreeViewCall11 call = reinterpret_cast<CuteQTreeViewCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQTreeViewCall12 call = reinterpret_cast<CuteQTreeViewCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQTreeViewCall13 call = reinterpret_cast<CuteQTreeViewCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQTreeViewCall14 call = reinterpret_cast<CuteQTreeViewCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQTreeViewCall15 call = reinterpret_cast<CuteQTreeViewCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQTreeViewCall16 call = reinterpret_cast<CuteQTreeViewCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQTreeViewCall17 call = reinterpret_cast<CuteQTreeViewCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQTreeViewCall18 call = reinterpret_cast<CuteQTreeViewCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQTreeViewCall19 call = reinterpret_cast<CuteQTreeViewCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQTreeViewCall20 call = reinterpret_cast<CuteQTreeViewCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQTreeViewCall21 call = reinterpret_cast<CuteQTreeViewCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQTreeViewCall22 call = reinterpret_cast<CuteQTreeViewCall22>(taken[22]);
      call(this, painter, &rect, &index, &handled);
      if (handled) return;
    }
    QTreeView::drawBranches(painter, rect, index);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTreeViewCall23 call = reinterpret_cast<CuteQTreeViewCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTreeViewCall24 call = reinterpret_cast<CuteQTreeViewCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQTreeViewCall25 call = reinterpret_cast<CuteQTreeViewCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseDoubleClickEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTreeViewCall26 call = reinterpret_cast<CuteQTreeViewCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QTreeView::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(treeview)

#if QT_CONFIG(treeview)
  //  void QTreeView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTreeViewCall27 call = reinterpret_cast<CuteQTreeViewCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQTreeViewCall28 call = reinterpret_cast<CuteQTreeViewCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQTreeViewCall29 call = reinterpret_cast<CuteQTreeViewCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQTreeViewCall30 call = reinterpret_cast<CuteQTreeViewCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQTreeViewCall31 call = reinterpret_cast<CuteQTreeViewCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQTreeViewCall32 call = reinterpret_cast<CuteQTreeViewCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQTreeViewCall33 call = reinterpret_cast<CuteQTreeViewCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQTreeViewCall34 call = reinterpret_cast<CuteQTreeViewCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQTreeViewCall35 call = reinterpret_cast<CuteQTreeViewCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQTreeViewCall36 call = reinterpret_cast<CuteQTreeViewCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteQTreeViewCall37 call = reinterpret_cast<CuteQTreeViewCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQTreeViewCall38 call = reinterpret_cast<CuteQTreeViewCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CuteQTreeViewCall39 call = reinterpret_cast<CuteQTreeViewCall39>(taken[39]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[40]) {
      int handled = 0;
      CuteQTreeViewCall40 call = reinterpret_cast<CuteQTreeViewCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[41]) {
      int handled = 0;
      CuteQTreeViewCall41 call = reinterpret_cast<CuteQTreeViewCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTreeViewCall42 call = reinterpret_cast<CuteQTreeViewCall42>(taken[42]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[43]) {
      int handled = 0;
      CuteQTreeViewCall43 call = reinterpret_cast<CuteQTreeViewCall43>(taken[43]);
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
      CuteQTreeViewCall44 call = reinterpret_cast<CuteQTreeViewCall44>(taken[44]);
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
      CuteQTreeViewCall45 call = reinterpret_cast<CuteQTreeViewCall45>(taken[45]);
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
      CuteQTreeViewCall46 call = reinterpret_cast<CuteQTreeViewCall46>(taken[46]);
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
      CuteQTreeViewCall47 call = reinterpret_cast<CuteQTreeViewCall47>(taken[47]);
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
      CuteQTreeViewCall48 call = reinterpret_cast<CuteQTreeViewCall48>(taken[48]);
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
    if (taken[49]) {
      int handled = 0;
      CuteQTreeViewCall49 call = reinterpret_cast<CuteQTreeViewCall49>(taken[49]);
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
    if (taken[50]) {
      int handled = 0;
      CuteQTreeViewCall50 call = reinterpret_cast<CuteQTreeViewCall50>(taken[50]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractItemView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[51]) {
      int handled = 0;
      CuteQTreeViewCall51 call = reinterpret_cast<CuteQTreeViewCall51>(taken[51]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::focusNextPrevChild(next);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQTreeViewCall52 call = reinterpret_cast<CuteQTreeViewCall52>(taken[52]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::event(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[53]) {
      int handled = 0;
      CuteQTreeViewCall53 call = reinterpret_cast<CuteQTreeViewCall53>(taken[53]);
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
    if (taken[54]) {
      int handled = 0;
      CuteQTreeViewCall54 call = reinterpret_cast<CuteQTreeViewCall54>(taken[54]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[55]) {
      int handled = 0;
      CuteQTreeViewCall55 call = reinterpret_cast<CuteQTreeViewCall55>(taken[55]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::dropEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[56]) {
      int handled = 0;
      CuteQTreeViewCall56 call = reinterpret_cast<CuteQTreeViewCall56>(taken[56]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[57]) {
      int handled = 0;
      CuteQTreeViewCall57 call = reinterpret_cast<CuteQTreeViewCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQTreeViewCall58 call = reinterpret_cast<CuteQTreeViewCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::resizeEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQTreeViewCall59 call = reinterpret_cast<CuteQTreeViewCall59>(taken[59]);
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
    if (taken[60]) {
      int handled = 0;
      CuteQTreeViewCall60 call = reinterpret_cast<CuteQTreeViewCall60>(taken[60]);
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
    if (taken[61]) {
      int handled = 0;
      CuteQTreeViewCall61 call = reinterpret_cast<CuteQTreeViewCall61>(taken[61]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[62]) {
      int handled = 0;
      CuteQTreeViewCall62 call = reinterpret_cast<CuteQTreeViewCall62>(taken[62]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[63]) {
      int handled = 0;
      CuteQTreeViewCall63 call = reinterpret_cast<CuteQTreeViewCall63>(taken[63]);
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
    if (taken[64]) {
      int handled = 0;
      CuteQTreeViewCall64 call = reinterpret_cast<CuteQTreeViewCall64>(taken[64]);
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
    if (taken[65]) {
      int handled = 0;
      CuteQTreeViewCall65 call = reinterpret_cast<CuteQTreeViewCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[66]) {
      int handled = 0;
      CuteQTreeViewCall66 call = reinterpret_cast<CuteQTreeViewCall66>(taken[66]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[67]) {
      int handled = 0;
      CuteQTreeViewCall67 call = reinterpret_cast<CuteQTreeViewCall67>(taken[67]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[68]) {
      int handled = 0;
      CuteQTreeViewCall68 call = reinterpret_cast<CuteQTreeViewCall68>(taken[68]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[69]) {
      int handled = 0;
      CuteQTreeViewCall69 call = reinterpret_cast<CuteQTreeViewCall69>(taken[69]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[70]) {
      int handled = 0;
      CuteQTreeViewCall70 call = reinterpret_cast<CuteQTreeViewCall70>(taken[70]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[71]) {
      int handled = 0;
      CuteQTreeViewCall71 call = reinterpret_cast<CuteQTreeViewCall71>(taken[71]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQTreeViewCall72 call = reinterpret_cast<CuteQTreeViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQTreeViewCall73 call = reinterpret_cast<CuteQTreeViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQTreeViewCall74 call = reinterpret_cast<CuteQTreeViewCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQTreeViewCall75 call = reinterpret_cast<CuteQTreeViewCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQTreeViewCall76 call = reinterpret_cast<CuteQTreeViewCall76>(taken[76]);
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
      CuteQTreeViewCall77 call = reinterpret_cast<CuteQTreeViewCall77>(taken[77]);
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
      CuteQTreeViewCall78 call = reinterpret_cast<CuteQTreeViewCall78>(taken[78]);
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
      CuteQTreeViewCall79 call = reinterpret_cast<CuteQTreeViewCall79>(taken[79]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[80]) {
      int handled = 0;
      CuteQTreeViewCall80 call = reinterpret_cast<CuteQTreeViewCall80>(taken[80]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQTreeViewCall81 call = reinterpret_cast<CuteQTreeViewCall81>(taken[81]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[82]) {
      int handled = 0;
      CuteQTreeViewCall82 call = reinterpret_cast<CuteQTreeViewCall82>(taken[82]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[83]) {
      int handled = 0;
      CuteQTreeViewCall83 call = reinterpret_cast<CuteQTreeViewCall83>(taken[83]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[84]) {
      int handled = 0;
      CuteQTreeViewCall84 call = reinterpret_cast<CuteQTreeViewCall84>(taken[84]);
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
      CuteQTreeViewCall85 call = reinterpret_cast<CuteQTreeViewCall85>(taken[85]);
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
      CuteQTreeViewCall86 call = reinterpret_cast<CuteQTreeViewCall86>(taken[86]);
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
      CuteQTreeViewCall87 call = reinterpret_cast<CuteQTreeViewCall87>(taken[87]);
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
      CuteQTreeViewCall88 call = reinterpret_cast<CuteQTreeViewCall88>(taken[88]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

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
  return new CuteQTreeView(parent);
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

//  void QTreeView::columnResized(int column, int oldSize, int newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView13columnResizedEiii(
    QTreeView *self,
    int column,
    int oldSize,
    int newSize) {
  self->columnResized(column, oldSize, newSize);
}

//  void QTreeView::columnCountChanged(int oldCount, int newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView18columnCountChangedEii(
    QTreeView *self,
    int oldCount,
    int newCount) {
  self->columnCountChanged(oldCount, newCount);
}

//  void QTreeView::columnMoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11columnMovedEv(QTreeView *self) {
  self->columnMoved();
}

//  void QTreeView::reexpand()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView8reexpandEv(QTreeView *self) {
  self->reexpand();
}

//  void QTreeView::rowsRemoved(const QModelIndex &parent, int first, int
//      last)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11rowsRemovedERK11QModelIndexii(
    QTreeView *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->rowsRemoved(*parent, first, last);
}

//  void QTreeView::verticalScrollbarValueChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView29verticalScrollbarValueChangedEi(
    QTreeView *self,
    int value) {
  self->verticalScrollbarValueChanged(value);
}

//  void QTreeView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView16scrollContentsByEii(
    QTreeView *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QTreeView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView12rowsInsertedERK11QModelIndexii(
    QTreeView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsInserted(*parent, start, end);
}

//  void QTreeView::rowsAboutToBeRemoved(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView20rowsAboutToBeRemovedERK11QModelIndexii(
    QTreeView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsAboutToBeRemoved(*parent, start, end);
}

//  QModelIndex QTreeView::moveCursor(CursorAction cursorAction,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN9QTreeView10moveCursorEN17QAbstractItemView12CursorActionE6QFlagsIN2Qt16KeyboardModifierEE(
    QTreeView *self,
    QAbstractItemView::CursorAction cursorAction,
    int modifiers) {
  return new QModelIndex(
      self->moveCursor(
          cursorAction,
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}

//  int QTreeView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView16horizontalOffsetEv(const QTreeView *self) {
  return self->horizontalOffset();
}

//  int QTreeView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView14verticalOffsetEv(const QTreeView *self) {
  return self->verticalOffset();
}

//  void QTreeView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTreeView *self,
    const QRect *rect,
    int command) {
  self->setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QTreeView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK9QTreeView24visualRegionForSelectionERK14QItemSelection(
    const QTreeView *self,
    const QItemSelection *selection) {
  return new QRegion(self->visualRegionForSelection(*selection));
}

//  QModelIndexList QTreeView::selectedIndexes() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK9QTreeView15selectedIndexesEv(
    const QTreeView *self) {
  return new QList<QModelIndex>(self->selectedIndexes());
}

//  void QTreeView::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView11changeEventEP6QEvent(
    QTreeView *self,
    QEvent *event) {
  self->changeEvent(event);
}

//  void QTreeView::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView10timerEventEP11QTimerEvent(
    QTreeView *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QTreeView::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView10paintEventEP11QPaintEvent(
    QTreeView *self,
    QPaintEvent *event) {
  self->paintEvent(event);
}

//  void QTreeView::drawTree(QPainter *painter, const QRegion &region) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QTreeView8drawTreeEP8QPainterRK7QRegion(
    const QTreeView *self,
    QPainter *painter,
    const QRegion *region) {
  self->drawTree(painter, *region);
}

//  void QTreeView::drawRow(QPainter *painter, const QStyleOptionViewItem
//      &options, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QTreeView7drawRowEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QTreeView *self,
    QPainter *painter,
    const QStyleOptionViewItem *options,
    const QModelIndex *index) {
  self->drawRow(painter, *options, *index);
}

//  void QTreeView::drawBranches(QPainter *painter, const QRect &rect, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QTreeView12drawBranchesEP8QPainterRK5QRectRK11QModelIndex(
    const QTreeView *self,
    QPainter *painter,
    const QRect *rect,
    const QModelIndex *index) {
  self->drawBranches(painter, *rect, *index);
}

//  void QTreeView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView15mousePressEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QTreeView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView17mouseReleaseEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QTreeView::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView21mouseDoubleClickEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QTreeView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView14mouseMoveEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QTreeView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView13keyPressEventEP9QKeyEvent(
    QTreeView *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

#if QT_CONFIG(draganddrop)
//  void QTreeView::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView13dragMoveEventEP14QDragMoveEvent(
    QTreeView *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  bool QTreeView::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTreeView13viewportEventEP6QEvent(
    QTreeView *self,
    QEvent *event) {
  return self->viewportEvent(event);
}

//  void QTreeView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView16updateGeometriesEv(QTreeView *self) {
  self->updateGeometries();
}

//  QSize QTreeView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QTreeView16viewportSizeHintEv(const QTreeView *self) {
  return new QSize(self->viewportSizeHint());
}

//  int QTreeView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView17sizeHintForColumnEi(
    const QTreeView *self,
    int column) {
  return self->sizeHintForColumn(column);
}

//  int QTreeView::indexRowSizeHint(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView16indexRowSizeHintERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return self->indexRowSizeHint(*index);
}

//  int QTreeView::rowHeight(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView9rowHeightERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return self->rowHeight(*index);
}

//  void QTreeView::horizontalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView25horizontalScrollbarActionEi(
    QTreeView *self,
    int action) {
  self->horizontalScrollbarAction(action);
}

//  bool QTreeView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTreeView13isIndexHiddenERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return self->isIndexHidden(*index);
}

//  void QTreeView::selectionChanged(const QItemSelection &selected, const
//      QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView16selectionChangedERK14QItemSelectionS2_(
    QTreeView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  self->selectionChanged(*selected, *deselected);
}

//  void QTreeView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTreeView14currentChangedERK11QModelIndexS2_(
    QTreeView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  self->currentChanged(*current, *previous);
}

//  int QTreeView::visualIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTreeView11visualIndexERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return self->visualIndex(*index);
}

//  QTreeViewPrivate *QTreeView::d_func()
extern "C" Q_DECL_EXPORT
QTreeViewPrivate *ritual_ZN9QTreeView6d_funcEv(QTreeView *self) {
  return self->d_func();
}

//  const QTreeViewPrivate *QTreeView::d_func() const
extern "C" Q_DECL_EXPORT
const QTreeViewPrivate *ritual_ZNK9QTreeView6d_funcEv(
    const QTreeView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTreeView, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeView(QTreeView *self, const char *key, void *call) {
  return static_cast<CuteQTreeView *>(self)->take(key, call);
}

//  void QTreeView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView8setModelEP18QAbstractItemModel(
    QTreeView *self,
    QAbstractItemModel *model) {
  self->QTreeView::setModel(model);
}

//  void QTreeView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView12setRootIndexERK11QModelIndex(
    QTreeView *self,
    const QModelIndex *index) {
  self->QTreeView::setRootIndex(*index);
}

//  void QTreeView::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView17setSelectionModelEP19QItemSelectionModel(
    QTreeView *self,
    QItemSelectionModel *selectionModel) {
  self->QTreeView::setSelectionModel(selectionModel);
}

//  void QTreeView::keyboardSearch(const QString &search)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView14keyboardSearchERK7QString(
    QTreeView *self,
    const QString *search) {
  self->QTreeView::keyboardSearch(*search);
}

//  QRect QTreeView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK9QTreeView10visualRectERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return new QRect(self->QTreeView::visualRect(*index));
}

//  void QTreeView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QTreeView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->QTreeView::scrollTo(*index, hint);
}

//  QModelIndex QTreeView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK9QTreeView7indexAtERK6QPoint(
    const QTreeView *self,
    const QPoint *p) {
  return new QModelIndex(self->QTreeView::indexAt(*p));
}

//  void QTreeView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView13doItemsLayoutEv(QTreeView *self) {
  self->QTreeView::doItemsLayout();
}

//  void QTreeView::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView5resetEv(QTreeView *self) {
  self->QTreeView::reset();
}

//  void QTreeView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView9selectAllEv(QTreeView *self) {
  self->QTreeView::selectAll();
}

//  void QTreeView::verticalScrollbarValueChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView29verticalScrollbarValueChangedEi(
    QTreeView *self,
    int value) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::verticalScrollbarValueChanged(
      value);
}

//  void QTreeView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView16scrollContentsByEii(
    QTreeView *self,
    int dx,
    int dy) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::scrollContentsBy(dx, dy);
}

//  void QTreeView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView12rowsInsertedERK11QModelIndexii(
    QTreeView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::rowsInserted(
      *parent,
      start,
      end);
}

//  void QTreeView::rowsAboutToBeRemoved(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView20rowsAboutToBeRemovedERK11QModelIndexii(
    QTreeView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::rowsAboutToBeRemoved(
      *parent,
      start,
      end);
}

//  int QTreeView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QTreeView16horizontalOffsetEv(const QTreeView *self) {
  return static_cast<const OwnQTreeView *>(self)->OwnQTreeView::horizontalOffset();
}

//  int QTreeView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QTreeView14verticalOffsetEv(const QTreeView *self) {
  return static_cast<const OwnQTreeView *>(self)->OwnQTreeView::verticalOffset();
}

//  void QTreeView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTreeView *self,
    const QRect *rect,
    int command) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QTreeView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK9QTreeView24visualRegionForSelectionERK14QItemSelection(
    const QTreeView *self,
    const QItemSelection *selection) {
  return new QRegion(
      static_cast<const OwnQTreeView *>(self)->OwnQTreeView::visualRegionForSelection(
          *selection));
}

//  void QTreeView::changeEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView11changeEventEP6QEvent(
    QTreeView *self,
    QEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::changeEvent(event);
}

//  void QTreeView::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView10timerEventEP11QTimerEvent(
    QTreeView *self,
    QTimerEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::timerEvent(event);
}

//  void QTreeView::paintEvent(QPaintEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView10paintEventEP11QPaintEvent(
    QTreeView *self,
    QPaintEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::paintEvent(event);
}

//  void QTreeView::drawRow(QPainter *painter, const QStyleOptionViewItem
//      &options, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QTreeView7drawRowEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QTreeView *self,
    QPainter *painter,
    const QStyleOptionViewItem *options,
    const QModelIndex *index) {
  static_cast<const OwnQTreeView *>(self)->OwnQTreeView::drawRow(
      painter,
      *options,
      *index);
}

//  void QTreeView::drawBranches(QPainter *painter, const QRect &rect, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QTreeView12drawBranchesEP8QPainterRK5QRectRK11QModelIndex(
    const QTreeView *self,
    QPainter *painter,
    const QRect *rect,
    const QModelIndex *index) {
  static_cast<const OwnQTreeView *>(self)->OwnQTreeView::drawBranches(
      painter,
      *rect,
      *index);
}

//  void QTreeView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView15mousePressEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::mousePressEvent(event);
}

//  void QTreeView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView17mouseReleaseEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::mouseReleaseEvent(event);
}

//  void QTreeView::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView21mouseDoubleClickEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::mouseDoubleClickEvent(
      event);
}

//  void QTreeView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView14mouseMoveEventEP11QMouseEvent(
    QTreeView *self,
    QMouseEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::mouseMoveEvent(event);
}

//  void QTreeView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView13keyPressEventEP9QKeyEvent(
    QTreeView *self,
    QKeyEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::keyPressEvent(event);
}

#if QT_CONFIG(draganddrop)
//  void QTreeView::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView13dragMoveEventEP14QDragMoveEvent(
    QTreeView *self,
    QDragMoveEvent *event) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::dragMoveEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  bool QTreeView::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QTreeView13viewportEventEP6QEvent(
    QTreeView *self,
    QEvent *event) {
  return static_cast<OwnQTreeView *>(self)->OwnQTreeView::viewportEvent(
      event);
}

//  void QTreeView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView16updateGeometriesEv(QTreeView *self) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::updateGeometries();
}

//  QSize QTreeView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK9QTreeView16viewportSizeHintEv(const QTreeView *self) {
  return new QSize(
      static_cast<const OwnQTreeView *>(self)->OwnQTreeView::viewportSizeHint());
}

//  int QTreeView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK9QTreeView17sizeHintForColumnEi(
    const QTreeView *self,
    int column) {
  return static_cast<const OwnQTreeView *>(self)->OwnQTreeView::sizeHintForColumn(
      column);
}

//  void QTreeView::horizontalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView25horizontalScrollbarActionEi(
    QTreeView *self,
    int action) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::horizontalScrollbarAction(
      action);
}

//  bool QTreeView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QTreeView13isIndexHiddenERK11QModelIndex(
    const QTreeView *self,
    const QModelIndex *index) {
  return static_cast<const OwnQTreeView *>(self)->OwnQTreeView::isIndexHidden(
      *index);
}

//  void QTreeView::selectionChanged(const QItemSelection &selected, const
//      QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView16selectionChangedERK14QItemSelectionS2_(
    QTreeView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::selectionChanged(
      *selected,
      *deselected);
}

//  void QTreeView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QTreeView14currentChangedERK11QModelIndexS2_(
    QTreeView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  static_cast<OwnQTreeView *>(self)->OwnQTreeView::currentChanged(
      *current,
      *previous);
}

#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(treeview)
