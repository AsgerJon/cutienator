//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qheaderview.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QHeaderView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQHeaderView : QHeaderView {
  using QHeaderView::currentChanged;
  using QHeaderView::event;
  using QHeaderView::paintEvent;
  using QHeaderView::mousePressEvent;
  using QHeaderView::mouseMoveEvent;
  using QHeaderView::mouseReleaseEvent;
  using QHeaderView::mouseDoubleClickEvent;
  using QHeaderView::viewportEvent;
  using QHeaderView::paintSection;
  using QHeaderView::sectionSizeFromContents;
  using QHeaderView::horizontalOffset;
  using QHeaderView::verticalOffset;
  using QHeaderView::updateGeometries;
  using QHeaderView::scrollContentsBy;
  using QHeaderView::rowsInserted;
  using QHeaderView::visualRect;
  using QHeaderView::scrollTo;
  using QHeaderView::indexAt;
  using QHeaderView::isIndexHidden;
  using QHeaderView::setSelection;
  using QHeaderView::visualRegionForSelection;
  using QHeaderView::initStyleOptionForIndex;
};

//  A QHeaderView that Python can take functions over in. Every QHeaderView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall0)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQHeaderViewCall1)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall2)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall3)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall4)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall5)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall7)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall8)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall9)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall10)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewCall12)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall13)(const void *, QPainter *, const QRect *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQHeaderViewCall14)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQHeaderViewCall15)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQHeaderViewCall16)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall17)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall19)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQHeaderViewCall20)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall21)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QModelIndex * (*CuteQHeaderViewCall22)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall24)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRegion * (*CuteQHeaderViewCall25)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall26)(const void *, QStyleOptionHeader *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall27)(const void *, QStyleOptionHeader *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall28)(const void *, QStyleOptionFrame *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall29)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall30)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQHeaderViewCall31)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQHeaderViewCall32)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQHeaderViewCall33)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQHeaderViewCall34)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall35)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall36)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall37)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall38)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall39)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall40)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall41)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall42)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall44)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall45)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall46)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall47)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewCall48)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQHeaderViewCall49)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQHeaderViewCall50)(const void *, int, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall51)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewCall52)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall53)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall54)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall55)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall56)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall57)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall58)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall59)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall60)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall61)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewCall62)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewCall63)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQHeaderViewCall64)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQHeaderViewCall65)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQHeaderViewCall66)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQHeaderViewCall67)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQHeaderViewCall68)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQHeaderViewCall69)(const void *, QEvent *, int *);
typedef int (*CuteQHeaderViewCall70)(const void *, int *);
typedef int (*CuteQHeaderViewCall71)(const void *, int, int *);
typedef bool (*CuteQHeaderViewCall72)(const void *, int *);
typedef void * (*CuteQHeaderViewCall73)(const void *, int *);
typedef void (*CuteQHeaderViewCall74)(const void *, QKeyEvent *, int *);
typedef void (*CuteQHeaderViewCall75)(const void *, QEnterEvent *, int *);
typedef void (*CuteQHeaderViewCall76)(const void *, QEvent *, int *);
typedef void (*CuteQHeaderViewCall77)(const void *, QMoveEvent *, int *);
typedef void (*CuteQHeaderViewCall78)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQHeaderViewCall79)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQHeaderViewCall80)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQHeaderViewCall81)(const void *, QShowEvent *, int *);
typedef void (*CuteQHeaderViewCall82)(const void *, QHideEvent *, int *);
typedef int (*CuteQHeaderViewCall83)(const void *, int, int *);
typedef void (*CuteQHeaderViewCall84)(const void *, QPainter *, int *);
typedef void * (*CuteQHeaderViewCall85)(const void *, QPoint *, int *);
typedef void * (*CuteQHeaderViewCall86)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderViewCall87)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderViewCall88)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderViewCall89)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHeaderViewCall90)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHeaderView : public QHeaderView {
public:
  using QHeaderView::QHeaderView;
  void *taken[91] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK11QHeaderView12paintSectionEP8QPainterRK5QRecti")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK11QHeaderView23sectionSizeFromContentsEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK11QHeaderView23initStyleOptionForIndexEP18QStyleOptionHeaderi")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK11QHeaderView15initStyleOptionEP18QStyleOptionHeader")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
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
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
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
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[63] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[64] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[65] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[66] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[67] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[68] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
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
  //  void QHeaderView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeaderViewCall0 call = reinterpret_cast<CuteQHeaderViewCall0>(taken[0]);
      call(this, model, &handled);
      if (handled) return;
    }
    QHeaderView::setModel(model);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QSize QHeaderView::sizeHint() const
  QSize sizeHint() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQHeaderViewCall1 call = reinterpret_cast<CuteQHeaderViewCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHeaderView::sizeHint();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::setVisible(bool v)
  void setVisible(bool v) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHeaderViewCall2 call = reinterpret_cast<CuteQHeaderViewCall2>(taken[2]);
      call(this, v, &handled);
      if (handled) return;
    }
    QHeaderView::setVisible(v);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[3]) {
      int handled = 0;
      CuteQHeaderViewCall3 call = reinterpret_cast<CuteQHeaderViewCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QHeaderView::doItemsLayout();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::reset()
  void reset() override {
    if (taken[4]) {
      int handled = 0;
      CuteQHeaderViewCall4 call = reinterpret_cast<CuteQHeaderViewCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QHeaderView::reset();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::currentChanged(const QModelIndex &current, const
  //      QModelIndex &old)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &old) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHeaderViewCall5 call = reinterpret_cast<CuteQHeaderViewCall5>(taken[5]);
      call(this, &current, &old, &handled);
      if (handled) return;
    }
    QHeaderView::currentChanged(current, old);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  bool QHeaderView::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHeaderViewCall6 call = reinterpret_cast<CuteQHeaderViewCall6>(taken[6]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QHeaderView::event(e);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHeaderViewCall7 call = reinterpret_cast<CuteQHeaderViewCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QHeaderView::paintEvent(e);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::mousePressEvent(QMouseEvent *e)
  void mousePressEvent(QMouseEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHeaderViewCall8 call = reinterpret_cast<CuteQHeaderViewCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QHeaderView::mousePressEvent(e);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::mouseMoveEvent(QMouseEvent *e)
  void mouseMoveEvent(QMouseEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHeaderViewCall9 call = reinterpret_cast<CuteQHeaderViewCall9>(taken[9]);
      call(this, e, &handled);
      if (handled) return;
    }
    QHeaderView::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHeaderViewCall10 call = reinterpret_cast<CuteQHeaderViewCall10>(taken[10]);
      call(this, e, &handled);
      if (handled) return;
    }
    QHeaderView::mouseReleaseEvent(e);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::mouseDoubleClickEvent(QMouseEvent *e)
  void mouseDoubleClickEvent(QMouseEvent *e) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHeaderViewCall11 call = reinterpret_cast<CuteQHeaderViewCall11>(taken[11]);
      call(this, e, &handled);
      if (handled) return;
    }
    QHeaderView::mouseDoubleClickEvent(e);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  bool QHeaderView::viewportEvent(QEvent *e)
  bool viewportEvent(QEvent *e) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHeaderViewCall12 call = reinterpret_cast<CuteQHeaderViewCall12>(taken[12]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QHeaderView::viewportEvent(e);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::paintSection(QPainter *painter, const QRect &rect,
  //      int logicalIndex) const
  void paintSection(
      QPainter *painter,
      const QRect &rect,
      int logicalIndex) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQHeaderViewCall13 call = reinterpret_cast<CuteQHeaderViewCall13>(taken[13]);
      call(this, painter, &rect, logicalIndex, &handled);
      if (handled) return;
    }
    QHeaderView::paintSection(painter, rect, logicalIndex);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QSize QHeaderView::sectionSizeFromContents(int logicalIndex) const
  QSize sectionSizeFromContents(int logicalIndex) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQHeaderViewCall14 call = reinterpret_cast<CuteQHeaderViewCall14>(taken[14]);
      const QSize * given = call(this, logicalIndex, &handled);
      if (handled && given) return *given;
    }
    return QHeaderView::sectionSizeFromContents(logicalIndex);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QHeaderView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQHeaderViewCall15 call = reinterpret_cast<CuteQHeaderViewCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHeaderView::horizontalOffset();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QHeaderView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQHeaderViewCall16 call = reinterpret_cast<CuteQHeaderViewCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHeaderView::verticalOffset();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::updateGeometries()
  void updateGeometries() override {
    if (taken[17]) {
      int handled = 0;
      CuteQHeaderViewCall17 call = reinterpret_cast<CuteQHeaderViewCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QHeaderView::updateGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  void QHeaderView::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[18]) {
      int handled = 0;
      CuteQHeaderViewCall18 call = reinterpret_cast<CuteQHeaderViewCall18>(taken[18]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QHeaderView::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::rowsInserted(const QModelIndex &parent, int start,
  //      int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHeaderViewCall19 call = reinterpret_cast<CuteQHeaderViewCall19>(taken[19]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QHeaderView::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QRect QHeaderView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQHeaderViewCall20 call = reinterpret_cast<CuteQHeaderViewCall20>(taken[20]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QHeaderView::visualRect(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::scrollTo(const QModelIndex &index, ScrollHint hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[21]) {
      int handled = 0;
      CuteQHeaderViewCall21 call = reinterpret_cast<CuteQHeaderViewCall21>(taken[21]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QHeaderView::scrollTo(index, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QModelIndex QHeaderView::indexAt(const QPoint &p) const
  QModelIndex indexAt(const QPoint &p) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQHeaderViewCall22 call = reinterpret_cast<CuteQHeaderViewCall22>(taken[22]);
      const QModelIndex * given = call(this, &p, &handled);
      if (handled && given) return *given;
    }
    return QHeaderView::indexAt(p);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QHeaderView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQHeaderViewCall23 call = reinterpret_cast<CuteQHeaderViewCall23>(taken[23]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QHeaderView::isIndexHidden(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags flags)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags flags) override {
    if (taken[24]) {
      int handled = 0;
      CuteQHeaderViewCall24 call = reinterpret_cast<CuteQHeaderViewCall24>(taken[24]);
      call(this, &rect, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QHeaderView::setSelection(rect, flags);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QRegion QHeaderView::visualRegionForSelection(const QItemSelection
  //      &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQHeaderViewCall25 call = reinterpret_cast<CuteQHeaderViewCall25>(taken[25]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QHeaderView::visualRegionForSelection(selection);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::initStyleOptionForIndex(QStyleOptionHeader *option,
  //      int logicalIndex) const
  void initStyleOptionForIndex(
      QStyleOptionHeader *option,
      int logicalIndex) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQHeaderViewCall26 call = reinterpret_cast<CuteQHeaderViewCall26>(taken[26]);
      call(this, option, logicalIndex, &handled);
      if (handled) return;
    }
    QHeaderView::initStyleOptionForIndex(option, logicalIndex);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::initStyleOption(QStyleOptionHeader *option) const
  void initStyleOption(QStyleOptionHeader *option) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQHeaderViewCall27 call = reinterpret_cast<CuteQHeaderViewCall27>(taken[27]);
      call(this, option, &handled);
      if (handled) return;
    }
    QHeaderView::initStyleOption(option);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QHeaderView::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQHeaderViewCall28 call = reinterpret_cast<CuteQHeaderViewCall28>(taken[28]);
      call(this, option, &handled);
      if (handled) return;
    }
    QHeaderView::initStyleOption(option);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setSelectionModel(QItemSelectionModel
  //      *selectionModel)
  void setSelectionModel(QItemSelectionModel *selectionModel) override {
    if (taken[29]) {
      int handled = 0;
      CuteQHeaderViewCall29 call = reinterpret_cast<CuteQHeaderViewCall29>(taken[29]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QAbstractItemView::setSelectionModel(selectionModel);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[30]) {
      int handled = 0;
      CuteQHeaderViewCall30 call = reinterpret_cast<CuteQHeaderViewCall30>(taken[30]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQHeaderViewCall31 call = reinterpret_cast<CuteQHeaderViewCall31>(taken[31]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQHeaderViewCall32 call = reinterpret_cast<CuteQHeaderViewCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQHeaderViewCall33 call = reinterpret_cast<CuteQHeaderViewCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQHeaderViewCall34 call = reinterpret_cast<CuteQHeaderViewCall34>(taken[34]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[35]) {
      int handled = 0;
      CuteQHeaderViewCall35 call = reinterpret_cast<CuteQHeaderViewCall35>(taken[35]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QAbstractItemView::setRootIndex(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[36]) {
      int handled = 0;
      CuteQHeaderViewCall36 call = reinterpret_cast<CuteQHeaderViewCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectAll();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex
  //      &parent, int start, int end)
  void rowsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[37]) {
      int handled = 0;
      CuteQHeaderViewCall37 call = reinterpret_cast<CuteQHeaderViewCall37>(taken[37]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemView::rowsAboutToBeRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::selectionChanged(const QItemSelection
  //      &selected, const QItemSelection &deselected)
  void selectionChanged(
      const QItemSelection &selected,
      const QItemSelection &deselected) override {
    if (taken[38]) {
      int handled = 0;
      CuteQHeaderViewCall38 call = reinterpret_cast<CuteQHeaderViewCall38>(taken[38]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectionChanged(selected, deselected);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[39]) {
      int handled = 0;
      CuteQHeaderViewCall39 call = reinterpret_cast<CuteQHeaderViewCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[40]) {
      int handled = 0;
      CuteQHeaderViewCall40 call = reinterpret_cast<CuteQHeaderViewCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[41]) {
      int handled = 0;
      CuteQHeaderViewCall41 call = reinterpret_cast<CuteQHeaderViewCall41>(taken[41]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[42]) {
      int handled = 0;
      CuteQHeaderViewCall42 call = reinterpret_cast<CuteQHeaderViewCall42>(taken[42]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[43]) {
      int handled = 0;
      CuteQHeaderViewCall43 call = reinterpret_cast<CuteQHeaderViewCall43>(taken[43]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[44]) {
      int handled = 0;
      CuteQHeaderViewCall44 call = reinterpret_cast<CuteQHeaderViewCall44>(taken[44]);
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
    if (taken[45]) {
      int handled = 0;
      CuteQHeaderViewCall45 call = reinterpret_cast<CuteQHeaderViewCall45>(taken[45]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[46]) {
      int handled = 0;
      CuteQHeaderViewCall46 call = reinterpret_cast<CuteQHeaderViewCall46>(taken[46]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[47]) {
      int handled = 0;
      CuteQHeaderViewCall47 call = reinterpret_cast<CuteQHeaderViewCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQHeaderViewCall48 call = reinterpret_cast<CuteQHeaderViewCall48>(taken[48]);
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
    if (taken[49]) {
      int handled = 0;
      CuteQHeaderViewCall49 call = reinterpret_cast<CuteQHeaderViewCall49>(taken[49]);
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
    if (taken[50]) {
      int handled = 0;
      CuteQHeaderViewCall50 call = reinterpret_cast<CuteQHeaderViewCall50>(taken[50]);
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
    if (taken[51]) {
      int handled = 0;
      CuteQHeaderViewCall51 call = reinterpret_cast<CuteQHeaderViewCall51>(taken[51]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractItemView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[52]) {
      int handled = 0;
      CuteQHeaderViewCall52 call = reinterpret_cast<CuteQHeaderViewCall52>(taken[52]);
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
    if (taken[53]) {
      int handled = 0;
      CuteQHeaderViewCall53 call = reinterpret_cast<CuteQHeaderViewCall53>(taken[53]);
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
    if (taken[54]) {
      int handled = 0;
      CuteQHeaderViewCall54 call = reinterpret_cast<CuteQHeaderViewCall54>(taken[54]);
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
    if (taken[55]) {
      int handled = 0;
      CuteQHeaderViewCall55 call = reinterpret_cast<CuteQHeaderViewCall55>(taken[55]);
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
    if (taken[56]) {
      int handled = 0;
      CuteQHeaderViewCall56 call = reinterpret_cast<CuteQHeaderViewCall56>(taken[56]);
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
    if (taken[57]) {
      int handled = 0;
      CuteQHeaderViewCall57 call = reinterpret_cast<CuteQHeaderViewCall57>(taken[57]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[58]) {
      int handled = 0;
      CuteQHeaderViewCall58 call = reinterpret_cast<CuteQHeaderViewCall58>(taken[58]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[59]) {
      int handled = 0;
      CuteQHeaderViewCall59 call = reinterpret_cast<CuteQHeaderViewCall59>(taken[59]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[60]) {
      int handled = 0;
      CuteQHeaderViewCall60 call = reinterpret_cast<CuteQHeaderViewCall60>(taken[60]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::resizeEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[61]) {
      int handled = 0;
      CuteQHeaderViewCall61 call = reinterpret_cast<CuteQHeaderViewCall61>(taken[61]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::timerEvent(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[62]) {
      int handled = 0;
      CuteQHeaderViewCall62 call = reinterpret_cast<CuteQHeaderViewCall62>(taken[62]);
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
    if (taken[63]) {
      int handled = 0;
      CuteQHeaderViewCall63 call = reinterpret_cast<CuteQHeaderViewCall63>(taken[63]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::eventFilter(object, event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  QSize QAbstractItemView::viewportSizeHint() const
  QSize viewportSizeHint() const override {
    if (taken[64]) {
      int handled = 0;
      CuteQHeaderViewCall64 call = reinterpret_cast<CuteQHeaderViewCall64>(taken[64]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::viewportSizeHint();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQHeaderViewCall65 call = reinterpret_cast<CuteQHeaderViewCall65>(taken[65]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[66]) {
      int handled = 0;
      CuteQHeaderViewCall66 call = reinterpret_cast<CuteQHeaderViewCall66>(taken[66]);
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
    if (taken[67]) {
      int handled = 0;
      CuteQHeaderViewCall67 call = reinterpret_cast<CuteQHeaderViewCall67>(taken[67]);
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
    if (taken[68]) {
      int handled = 0;
      CuteQHeaderViewCall68 call = reinterpret_cast<CuteQHeaderViewCall68>(taken[68]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQHeaderViewCall69 call = reinterpret_cast<CuteQHeaderViewCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[70]) {
      int handled = 0;
      CuteQHeaderViewCall70 call = reinterpret_cast<CuteQHeaderViewCall70>(taken[70]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[71]) {
      int handled = 0;
      CuteQHeaderViewCall71 call = reinterpret_cast<CuteQHeaderViewCall71>(taken[71]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[72]) {
      int handled = 0;
      CuteQHeaderViewCall72 call = reinterpret_cast<CuteQHeaderViewCall72>(taken[72]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[73]) {
      int handled = 0;
      CuteQHeaderViewCall73 call = reinterpret_cast<CuteQHeaderViewCall73>(taken[73]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQHeaderViewCall74 call = reinterpret_cast<CuteQHeaderViewCall74>(taken[74]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[75]) {
      int handled = 0;
      CuteQHeaderViewCall75 call = reinterpret_cast<CuteQHeaderViewCall75>(taken[75]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[76]) {
      int handled = 0;
      CuteQHeaderViewCall76 call = reinterpret_cast<CuteQHeaderViewCall76>(taken[76]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[77]) {
      int handled = 0;
      CuteQHeaderViewCall77 call = reinterpret_cast<CuteQHeaderViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQHeaderViewCall78 call = reinterpret_cast<CuteQHeaderViewCall78>(taken[78]);
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
      CuteQHeaderViewCall79 call = reinterpret_cast<CuteQHeaderViewCall79>(taken[79]);
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
      CuteQHeaderViewCall80 call = reinterpret_cast<CuteQHeaderViewCall80>(taken[80]);
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
      CuteQHeaderViewCall81 call = reinterpret_cast<CuteQHeaderViewCall81>(taken[81]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[82]) {
      int handled = 0;
      CuteQHeaderViewCall82 call = reinterpret_cast<CuteQHeaderViewCall82>(taken[82]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[83]) {
      int handled = 0;
      CuteQHeaderViewCall83 call = reinterpret_cast<CuteQHeaderViewCall83>(taken[83]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[84]) {
      int handled = 0;
      CuteQHeaderViewCall84 call = reinterpret_cast<CuteQHeaderViewCall84>(taken[84]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[85]) {
      int handled = 0;
      CuteQHeaderViewCall85 call = reinterpret_cast<CuteQHeaderViewCall85>(taken[85]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[86]) {
      int handled = 0;
      CuteQHeaderViewCall86 call = reinterpret_cast<CuteQHeaderViewCall86>(taken[86]);
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
      CuteQHeaderViewCall87 call = reinterpret_cast<CuteQHeaderViewCall87>(taken[87]);
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
      CuteQHeaderViewCall88 call = reinterpret_cast<CuteQHeaderViewCall88>(taken[88]);
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
      CuteQHeaderViewCall89 call = reinterpret_cast<CuteQHeaderViewCall89>(taken[89]);
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
      CuteQHeaderViewCall90 call = reinterpret_cast<CuteQHeaderViewCall90>(taken[90]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHeaderView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHeaderView10metaObjectEv(
    const QHeaderView *self) {
  return self->metaObject();
}

//  QString QHeaderView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHeaderView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHeaderView::tr(s, c, n));
}

//  QHeaderView::QHeaderView(Qt::Orientation orientation, QWidget *parent)
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZN11QHeaderViewC1EN2Qt11OrientationEP7QWidget(
    Qt::Orientation orientation,
    QWidget *parent) {
  return new CuteQHeaderView(orientation, parent);
}

//  QHeaderView::~QHeaderView()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderViewD1Ev(QHeaderView *self) {
  delete self;
}

//  void QHeaderView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView8setModelEP18QAbstractItemModel(
    QHeaderView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  Qt::Orientation QHeaderView::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK11QHeaderView11orientationEv(
    const QHeaderView *self) {
  return self->orientation();
}

//  int QHeaderView::offset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView6offsetEv(const QHeaderView *self) {
  return self->offset();
}

//  int QHeaderView::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView6lengthEv(const QHeaderView *self) {
  return self->length();
}

//  QSize QHeaderView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QHeaderView8sizeHintEv(const QHeaderView *self) {
  return new QSize(self->sizeHint());
}

//  void QHeaderView::setVisible(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView10setVisibleEb(QHeaderView *self, bool v) {
  self->setVisible(v);
}

//  int QHeaderView::sectionSizeHint(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView15sectionSizeHintEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionSizeHint(logicalIndex);
}

//  int QHeaderView::visualIndexAt(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView13visualIndexAtEi(
    const QHeaderView *self,
    int position) {
  return self->visualIndexAt(position);
}

//  int QHeaderView::logicalIndexAt(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14logicalIndexAtEi(
    const QHeaderView *self,
    int position) {
  return self->logicalIndexAt(position);
}

//  int QHeaderView::logicalIndexAt(int x, int y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14logicalIndexAtEii(
    const QHeaderView *self,
    int x,
    int y) {
  return self->logicalIndexAt(x, y);
}

//  int QHeaderView::logicalIndexAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14logicalIndexAtERK6QPoint(
    const QHeaderView *self,
    const QPoint *pos) {
  return self->logicalIndexAt(*pos);
}

//  int QHeaderView::sectionSize(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView11sectionSizeEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionSize(logicalIndex);
}

//  int QHeaderView::sectionPosition(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView15sectionPositionEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionPosition(logicalIndex);
}

//  int QHeaderView::sectionViewportPosition(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView23sectionViewportPositionEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionViewportPosition(logicalIndex);
}

//  void QHeaderView::moveSection(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView11moveSectionEii(
    QHeaderView *self,
    int from,
    int to) {
  self->moveSection(from, to);
}

//  void QHeaderView::swapSections(int first, int second)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView12swapSectionsEii(
    QHeaderView *self,
    int first,
    int second) {
  self->swapSections(first, second);
}

//  void QHeaderView::resizeSection(int logicalIndex, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView13resizeSectionEii(
    QHeaderView *self,
    int logicalIndex,
    int size) {
  self->resizeSection(logicalIndex, size);
}

//  void QHeaderView::resizeSections(QHeaderView::ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView14resizeSectionsENS_10ResizeModeE(
    QHeaderView *self,
    QHeaderView::ResizeMode mode) {
  self->resizeSections(mode);
}

//  bool QHeaderView::isSectionHidden(int logicalIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView15isSectionHiddenEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->isSectionHidden(logicalIndex);
}

//  void QHeaderView::setSectionHidden(int logicalIndex, bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16setSectionHiddenEib(
    QHeaderView *self,
    int logicalIndex,
    bool hide) {
  self->setSectionHidden(logicalIndex, hide);
}

//  int QHeaderView::hiddenSectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18hiddenSectionCountEv(const QHeaderView *self) {
  return self->hiddenSectionCount();
}

//  void QHeaderView::hideSection(int logicalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView11hideSectionEi(
    QHeaderView *self,
    int logicalIndex) {
  self->hideSection(logicalIndex);
}

//  void QHeaderView::showSection(int logicalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView11showSectionEi(
    QHeaderView *self,
    int logicalIndex) {
  self->showSection(logicalIndex);
}

//  int QHeaderView::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView5countEv(const QHeaderView *self) {
  return self->count();
}

//  int QHeaderView::visualIndex(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView11visualIndexEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->visualIndex(logicalIndex);
}

//  int QHeaderView::logicalIndex(int visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView12logicalIndexEi(
    const QHeaderView *self,
    int visualIndex) {
  return self->logicalIndex(visualIndex);
}

//  void QHeaderView::setSectionsMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView18setSectionsMovableEb(
    QHeaderView *self,
    bool movable) {
  self->setSectionsMovable(movable);
}

//  bool QHeaderView::sectionsMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView15sectionsMovableEv(const QHeaderView *self) {
  return self->sectionsMovable();
}

//  void QHeaderView::setFirstSectionMovable(bool movable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView22setFirstSectionMovableEb(
    QHeaderView *self,
    bool movable) {
  self->setFirstSectionMovable(movable);
}

//  bool QHeaderView::isFirstSectionMovable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView21isFirstSectionMovableEv(
    const QHeaderView *self) {
  return self->isFirstSectionMovable();
}

//  void QHeaderView::setSectionsClickable(bool clickable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setSectionsClickableEb(
    QHeaderView *self,
    bool clickable) {
  self->setSectionsClickable(clickable);
}

//  bool QHeaderView::sectionsClickable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView17sectionsClickableEv(const QHeaderView *self) {
  return self->sectionsClickable();
}

//  void QHeaderView::setHighlightSections(bool highlight)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setHighlightSectionsEb(
    QHeaderView *self,
    bool highlight) {
  self->setHighlightSections(highlight);
}

//  bool QHeaderView::highlightSections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView17highlightSectionsEv(const QHeaderView *self) {
  return self->highlightSections();
}

//  ResizeMode QHeaderView::sectionResizeMode(int logicalIndex) const
extern "C" Q_DECL_EXPORT
QHeaderView::ResizeMode ritual_ZNK11QHeaderView17sectionResizeModeEi(
    const QHeaderView *self,
    int logicalIndex) {
  return self->sectionResizeMode(logicalIndex);
}

//  void QHeaderView::setSectionResizeMode(ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setSectionResizeModeENS_10ResizeModeE(
    QHeaderView *self,
    QHeaderView::ResizeMode mode) {
  self->setSectionResizeMode(mode);
}

//  void QHeaderView::setSectionResizeMode(int logicalIndex, ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView20setSectionResizeModeEiNS_10ResizeModeE(
    QHeaderView *self,
    int logicalIndex,
    QHeaderView::ResizeMode mode) {
  self->setSectionResizeMode(logicalIndex, mode);
}

//  void QHeaderView::setResizeContentsPrecision(int precision)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView26setResizeContentsPrecisionEi(
    QHeaderView *self,
    int precision) {
  self->setResizeContentsPrecision(precision);
}

//  int QHeaderView::resizeContentsPrecision() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView23resizeContentsPrecisionEv(
    const QHeaderView *self) {
  return self->resizeContentsPrecision();
}

//  int QHeaderView::stretchSectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView19stretchSectionCountEv(const QHeaderView *self) {
  return self->stretchSectionCount();
}

//  void QHeaderView::setSortIndicatorShown(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setSortIndicatorShownEb(
    QHeaderView *self,
    bool show) {
  self->setSortIndicatorShown(show);
}

//  bool QHeaderView::isSortIndicatorShown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView20isSortIndicatorShownEv(
    const QHeaderView *self) {
  return self->isSortIndicatorShown();
}

//  void QHeaderView::setSortIndicator(int logicalIndex, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16setSortIndicatorEiN2Qt9SortOrderE(
    QHeaderView *self,
    int logicalIndex,
    Qt::SortOrder order) {
  self->setSortIndicator(logicalIndex, order);
}

//  int QHeaderView::sortIndicatorSection() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView20sortIndicatorSectionEv(
    const QHeaderView *self) {
  return self->sortIndicatorSection();
}

//  Qt::SortOrder QHeaderView::sortIndicatorOrder() const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK11QHeaderView18sortIndicatorOrderEv(
    const QHeaderView *self) {
  return self->sortIndicatorOrder();
}

//  void QHeaderView::setSortIndicatorClearable(bool clearable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView25setSortIndicatorClearableEb(
    QHeaderView *self,
    bool clearable) {
  self->setSortIndicatorClearable(clearable);
}

//  bool QHeaderView::isSortIndicatorClearable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView24isSortIndicatorClearableEv(
    const QHeaderView *self) {
  return self->isSortIndicatorClearable();
}

//  bool QHeaderView::stretchLastSection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView18stretchLastSectionEv(const QHeaderView *self) {
  return self->stretchLastSection();
}

//  void QHeaderView::setStretchLastSection(bool stretch)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setStretchLastSectionEb(
    QHeaderView *self,
    bool stretch) {
  self->setStretchLastSection(stretch);
}

//  bool QHeaderView::cascadingSectionResizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView23cascadingSectionResizesEv(
    const QHeaderView *self) {
  return self->cascadingSectionResizes();
}

//  void QHeaderView::setCascadingSectionResizes(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView26setCascadingSectionResizesEb(
    QHeaderView *self,
    bool enable) {
  self->setCascadingSectionResizes(enable);
}

//  int QHeaderView::defaultSectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18defaultSectionSizeEv(const QHeaderView *self) {
  return self->defaultSectionSize();
}

//  void QHeaderView::setDefaultSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setDefaultSectionSizeEi(
    QHeaderView *self,
    int size) {
  self->setDefaultSectionSize(size);
}

//  void QHeaderView::resetDefaultSectionSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView23resetDefaultSectionSizeEv(QHeaderView *self) {
  self->resetDefaultSectionSize();
}

//  int QHeaderView::minimumSectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18minimumSectionSizeEv(const QHeaderView *self) {
  return self->minimumSectionSize();
}

//  void QHeaderView::setMinimumSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setMinimumSectionSizeEi(
    QHeaderView *self,
    int size) {
  self->setMinimumSectionSize(size);
}

//  int QHeaderView::maximumSectionSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView18maximumSectionSizeEv(const QHeaderView *self) {
  return self->maximumSectionSize();
}

//  void QHeaderView::setMaximumSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21setMaximumSectionSizeEi(
    QHeaderView *self,
    int size) {
  self->setMaximumSectionSize(size);
}

//  Qt::Alignment QHeaderView::defaultAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView16defaultAlignmentEv(const QHeaderView *self) {
  return static_cast<int>(self->defaultAlignment().toInt());
}

//  void QHeaderView::setDefaultAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView19setDefaultAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QHeaderView *self,
    int alignment) {
  self->setDefaultAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QHeaderView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView13doItemsLayoutEv(QHeaderView *self) {
  self->doItemsLayout();
}

//  bool QHeaderView::sectionsMoved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView13sectionsMovedEv(const QHeaderView *self) {
  return self->sectionsMoved();
}

//  bool QHeaderView::sectionsHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView14sectionsHiddenEv(const QHeaderView *self) {
  return self->sectionsHidden();
}

#if !defined(QT_NO_DATASTREAM)
//  QByteArray QHeaderView::saveState() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QHeaderView9saveStateEv(const QHeaderView *self) {
  return new QByteArray(self->saveState());
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  bool QHeaderView::restoreState(const QByteArray &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QHeaderView12restoreStateERK10QByteArray(
    QHeaderView *self,
    const QByteArray *state) {
  return self->restoreState(*state);
}
#endif  // !defined(QT_NO_DATASTREAM)

//  void QHeaderView::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView5resetEv(QHeaderView *self) {
  self->reset();
}

//  void QHeaderView::setOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView9setOffsetEi(QHeaderView *self, int offset) {
  self->setOffset(offset);
}

//  void QHeaderView::setOffsetToSectionPosition(int visualIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView26setOffsetToSectionPositionEi(
    QHeaderView *self,
    int visualIndex) {
  self->setOffsetToSectionPosition(visualIndex);
}

//  void QHeaderView::setOffsetToLastSection()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView22setOffsetToLastSectionEv(QHeaderView *self) {
  self->setOffsetToLastSection();
}

//  void QHeaderView::headerDataChanged(Qt::Orientation orientation, int
//      logicalFirst, int logicalLast)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView17headerDataChangedEN2Qt11OrientationEii(
    QHeaderView *self,
    Qt::Orientation orientation,
    int logicalFirst,
    int logicalLast) {
  self->headerDataChanged(orientation, logicalFirst, logicalLast);
}

//  void QHeaderView::updateSection(int logicalIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView13updateSectionEi(
    QHeaderView *self,
    int logicalIndex) {
  self->updateSection(logicalIndex);
}

//  void QHeaderView::resizeSections()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView14resizeSectionsEv(QHeaderView *self) {
  self->resizeSections();
}

//  void QHeaderView::sectionsInserted(const QModelIndex &parent, int
//      logicalFirst, int logicalLast)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16sectionsInsertedERK11QModelIndexii(
    QHeaderView *self,
    const QModelIndex *parent,
    int logicalFirst,
    int logicalLast) {
  self->sectionsInserted(*parent, logicalFirst, logicalLast);
}

//  void QHeaderView::sectionsAboutToBeRemoved(const QModelIndex &parent, int
//      logicalFirst, int logicalLast)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView24sectionsAboutToBeRemovedERK11QModelIndexii(
    QHeaderView *self,
    const QModelIndex *parent,
    int logicalFirst,
    int logicalLast) {
  self->sectionsAboutToBeRemoved(*parent, logicalFirst, logicalLast);
}

//  void QHeaderView::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView10initializeEv(QHeaderView *self) {
  self->initialize();
}

//  void QHeaderView::initializeSections()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView18initializeSectionsEv(QHeaderView *self) {
  self->initializeSections();
}

//  void QHeaderView::initializeSections(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView18initializeSectionsEii(
    QHeaderView *self,
    int start,
    int end) {
  self->initializeSections(start, end);
}

//  void QHeaderView::currentChanged(const QModelIndex &current, const
//      QModelIndex &old)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView14currentChangedERK11QModelIndexS2_(
    QHeaderView *self,
    const QModelIndex *current,
    const QModelIndex *old) {
  self->currentChanged(*current, *old);
}

//  bool QHeaderView::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QHeaderView5eventEP6QEvent(QHeaderView *self, QEvent *e) {
  return self->event(e);
}

//  void QHeaderView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView10paintEventEP11QPaintEvent(
    QHeaderView *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QHeaderView::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView15mousePressEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QHeaderView::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView14mouseMoveEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QHeaderView::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView17mouseReleaseEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  self->mouseReleaseEvent(e);
}

//  void QHeaderView::mouseDoubleClickEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView21mouseDoubleClickEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  self->mouseDoubleClickEvent(e);
}

//  bool QHeaderView::viewportEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QHeaderView13viewportEventEP6QEvent(
    QHeaderView *self,
    QEvent *e) {
  return self->viewportEvent(e);
}

//  void QHeaderView::paintSection(QPainter *painter, const QRect &rect, int
//      logicalIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QHeaderView12paintSectionEP8QPainterRK5QRecti(
    const QHeaderView *self,
    QPainter *painter,
    const QRect *rect,
    int logicalIndex) {
  self->paintSection(painter, *rect, logicalIndex);
}

//  QSize QHeaderView::sectionSizeFromContents(int logicalIndex) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QHeaderView23sectionSizeFromContentsEi(
    const QHeaderView *self,
    int logicalIndex) {
  return new QSize(self->sectionSizeFromContents(logicalIndex));
}

//  int QHeaderView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView16horizontalOffsetEv(const QHeaderView *self) {
  return self->horizontalOffset();
}

//  int QHeaderView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QHeaderView14verticalOffsetEv(const QHeaderView *self) {
  return self->verticalOffset();
}

//  void QHeaderView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16updateGeometriesEv(QHeaderView *self) {
  self->updateGeometries();
}

//  void QHeaderView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView16scrollContentsByEii(
    QHeaderView *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QHeaderView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView12rowsInsertedERK11QModelIndexii(
    QHeaderView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsInserted(*parent, start, end);
}

//  QRect QHeaderView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QHeaderView10visualRectERK11QModelIndex(
    const QHeaderView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QHeaderView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QHeaderView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QModelIndex QHeaderView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QHeaderView7indexAtERK6QPoint(
    const QHeaderView *self,
    const QPoint *p) {
  return new QModelIndex(self->indexAt(*p));
}

//  bool QHeaderView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHeaderView13isIndexHiddenERK11QModelIndex(
    const QHeaderView *self,
    const QModelIndex *index) {
  return self->isIndexHidden(*index);
}

//  QModelIndex QHeaderView::moveCursor(CursorAction a0,
//      Qt::KeyboardModifiers a1)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN11QHeaderView10moveCursorEN17QAbstractItemView12CursorActionE6QFlagsIN2Qt16KeyboardModifierEE(
    QHeaderView *self,
    QAbstractItemView::CursorAction a0,
    int a1) {
  return new QModelIndex(
      self->moveCursor(
          a0,
          QFlags<Qt::KeyboardModifier>::fromInt(a1)));
}

//  void QHeaderView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHeaderView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QHeaderView *self,
    const QRect *rect,
    int flags) {
  self->setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(flags));
}

//  QRegion QHeaderView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK11QHeaderView24visualRegionForSelectionERK14QItemSelection(
    const QHeaderView *self,
    const QItemSelection *selection) {
  return new QRegion(self->visualRegionForSelection(*selection));
}

//  void QHeaderView::initStyleOptionForIndex(QStyleOptionHeader *option, int
//      logicalIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QHeaderView23initStyleOptionForIndexEP18QStyleOptionHeaderi(
    const QHeaderView *self,
    QStyleOptionHeader *option,
    int logicalIndex) {
  self->initStyleOptionForIndex(option, logicalIndex);
}

//  void QHeaderView::initStyleOption(QStyleOptionHeader *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QHeaderView15initStyleOptionEP18QStyleOptionHeader(
    const QHeaderView *self,
    QStyleOptionHeader *option) {
  self->initStyleOption(option);
}

//  void QHeaderView::initStyleOption(QStyleOptionFrame *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QHeaderView15initStyleOptionEP17QStyleOptionFrame(
    const QHeaderView *self,
    QStyleOptionFrame *option) {
  self->initStyleOption(option);
}

//  QHeaderViewPrivate *QHeaderView::d_func()
extern "C" Q_DECL_EXPORT
QHeaderViewPrivate *ritual_ZN11QHeaderView6d_funcEv(QHeaderView *self) {
  return self->d_func();
}

//  const QHeaderViewPrivate *QHeaderView::d_func() const
extern "C" Q_DECL_EXPORT
const QHeaderViewPrivate *ritual_ZNK11QHeaderView6d_funcEv(
    const QHeaderView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHeaderView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeaderView(
    QHeaderView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeaderView *>(self)->take(key, call);
}

//  void QHeaderView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView8setModelEP18QAbstractItemModel(
    QHeaderView *self,
    QAbstractItemModel *model) {
  self->QHeaderView::setModel(model);
}

//  QSize QHeaderView::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QHeaderView8sizeHintEv(const QHeaderView *self) {
  return new QSize(self->QHeaderView::sizeHint());
}

//  void QHeaderView::setVisible(bool v)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView10setVisibleEb(QHeaderView *self, bool v) {
  self->QHeaderView::setVisible(v);
}

//  void QHeaderView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView13doItemsLayoutEv(QHeaderView *self) {
  self->QHeaderView::doItemsLayout();
}

//  void QHeaderView::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView5resetEv(QHeaderView *self) {
  self->QHeaderView::reset();
}

//  void QHeaderView::currentChanged(const QModelIndex &current, const
//      QModelIndex &old)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView14currentChangedERK11QModelIndexS2_(
    QHeaderView *self,
    const QModelIndex *current,
    const QModelIndex *old) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::currentChanged(
      *current,
      *old);
}

//  bool QHeaderView::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QHeaderView5eventEP6QEvent(
    QHeaderView *self,
    QEvent *e) {
  return static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::event(e);
}

//  void QHeaderView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView10paintEventEP11QPaintEvent(
    QHeaderView *self,
    QPaintEvent *e) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::paintEvent(e);
}

//  void QHeaderView::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView15mousePressEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::mousePressEvent(e);
}

//  void QHeaderView::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView14mouseMoveEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::mouseMoveEvent(e);
}

//  void QHeaderView::mouseReleaseEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView17mouseReleaseEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::mouseReleaseEvent(e);
}

//  void QHeaderView::mouseDoubleClickEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView21mouseDoubleClickEventEP11QMouseEvent(
    QHeaderView *self,
    QMouseEvent *e) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::mouseDoubleClickEvent(
      e);
}

//  bool QHeaderView::viewportEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QHeaderView13viewportEventEP6QEvent(
    QHeaderView *self,
    QEvent *e) {
  return static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::viewportEvent(
      e);
}

//  void QHeaderView::paintSection(QPainter *painter, const QRect &rect, int
//      logicalIndex) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QHeaderView12paintSectionEP8QPainterRK5QRecti(
    const QHeaderView *self,
    QPainter *painter,
    const QRect *rect,
    int logicalIndex) {
  static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::paintSection(
      painter,
      *rect,
      logicalIndex);
}

//  QSize QHeaderView::sectionSizeFromContents(int logicalIndex) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QHeaderView23sectionSizeFromContentsEi(
    const QHeaderView *self,
    int logicalIndex) {
  return new QSize(
      static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::sectionSizeFromContents(
          logicalIndex));
}

//  int QHeaderView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QHeaderView16horizontalOffsetEv(
    const QHeaderView *self) {
  return static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::horizontalOffset();
}

//  int QHeaderView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QHeaderView14verticalOffsetEv(const QHeaderView *self) {
  return static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::verticalOffset();
}

//  void QHeaderView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView16updateGeometriesEv(QHeaderView *self) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::updateGeometries();
}

//  void QHeaderView::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView16scrollContentsByEii(
    QHeaderView *self,
    int dx,
    int dy) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::scrollContentsBy(
      dx,
      dy);
}

//  void QHeaderView::rowsInserted(const QModelIndex &parent, int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView12rowsInsertedERK11QModelIndexii(
    QHeaderView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::rowsInserted(
      *parent,
      start,
      end);
}

//  QRect QHeaderView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK11QHeaderView10visualRectERK11QModelIndex(
    const QHeaderView *self,
    const QModelIndex *index) {
  return new QRect(
      static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::visualRect(
          *index));
}

//  void QHeaderView::scrollTo(const QModelIndex &index, ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QHeaderView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::scrollTo(
      *index,
      hint);
}

//  QModelIndex QHeaderView::indexAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK11QHeaderView7indexAtERK6QPoint(
    const QHeaderView *self,
    const QPoint *p) {
  return new QModelIndex(
      static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::indexAt(
          *p));
}

//  bool QHeaderView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QHeaderView13isIndexHiddenERK11QModelIndex(
    const QHeaderView *self,
    const QModelIndex *index) {
  return static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::isIndexHidden(
      *index);
}

//  void QHeaderView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QHeaderView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QHeaderView *self,
    const QRect *rect,
    int flags) {
  static_cast<OwnQHeaderView *>(self)->OwnQHeaderView::setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(flags));
}

//  QRegion QHeaderView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK11QHeaderView24visualRegionForSelectionERK14QItemSelection(
    const QHeaderView *self,
    const QItemSelection *selection) {
  return new QRegion(
      static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::visualRegionForSelection(
          *selection));
}

//  void QHeaderView::initStyleOptionForIndex(QStyleOptionHeader *option, int
//      logicalIndex) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QHeaderView23initStyleOptionForIndexEP18QStyleOptionHeaderi(
    const QHeaderView *self,
    QStyleOptionHeader *option,
    int logicalIndex) {
  static_cast<const OwnQHeaderView *>(self)->OwnQHeaderView::initStyleOptionForIndex(
      option,
      logicalIndex);
}

//  void QHeaderView::initStyleOption(QStyleOptionFrame *option) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QHeaderView15initStyleOptionEP17QStyleOptionFrame(
    const QHeaderView *self,
    QStyleOptionFrame *option) {
  self->QHeaderView::initStyleOption(option);
}

#endif  // QT_CONFIG(itemviews)
