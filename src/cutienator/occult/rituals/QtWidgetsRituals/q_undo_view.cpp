//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qundoview.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(undoview)
#if QT_CONFIG(undoview)
#include <QtWidgets/qundoview.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qitemselectionmodel.h>
#endif
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QUndoView that Python can take functions over in. Every QUndoView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRect * (*CuteQUndoViewCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall1)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QModelIndex * (*CuteQUndoViewCall2)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall3)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall4)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef bool (*CuteQUndoViewCall6)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall7)(const void *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall8)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall9)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall10)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall11)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall12)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall13)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall14)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall15)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall16)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall17)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall18)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall19)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall20)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQUndoViewCall21)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQUndoViewCall22)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall23)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRegion * (*CuteQUndoViewCall24)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall25)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef bool (*CuteQUndoViewCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall27)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQUndoViewCall28)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef const QSize * (*CuteQUndoViewCall29)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall30)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall31)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall32)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQUndoViewCall33)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQUndoViewCall34)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQUndoViewCall35)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQUndoViewCall36)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall37)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall38)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall39)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall40)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall41)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall42)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall44)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall45)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall46)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQUndoViewCall47)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQUndoViewCall48)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQUndoViewCall49)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQUndoViewCall50)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall51)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall52)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall53)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall54)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall55)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall56)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQUndoViewCall57)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQUndoViewCall58)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQUndoViewCall59)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQUndoViewCall60)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQUndoViewCall61)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQUndoViewCall62)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQUndoViewCall63)(const void *, QEvent *, int *);
typedef void (*CuteQUndoViewCall64)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQUndoViewCall65)(const void *, int *);
typedef void (*CuteQUndoViewCall66)(const void *, bool, int *);
typedef int (*CuteQUndoViewCall67)(const void *, int, int *);
typedef bool (*CuteQUndoViewCall68)(const void *, int *);
typedef void * (*CuteQUndoViewCall69)(const void *, int *);
typedef void (*CuteQUndoViewCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQUndoViewCall71)(const void *, QEnterEvent *, int *);
typedef void (*CuteQUndoViewCall72)(const void *, QEvent *, int *);
typedef void (*CuteQUndoViewCall73)(const void *, QMoveEvent *, int *);
typedef void (*CuteQUndoViewCall74)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQUndoViewCall75)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQUndoViewCall76)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQUndoViewCall77)(const void *, QShowEvent *, int *);
typedef void (*CuteQUndoViewCall78)(const void *, QHideEvent *, int *);
typedef int (*CuteQUndoViewCall79)(const void *, int, int *);
typedef void (*CuteQUndoViewCall80)(const void *, QPainter *, int *);
typedef void * (*CuteQUndoViewCall81)(const void *, QPoint *, int *);
typedef void * (*CuteQUndoViewCall82)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoViewCall83)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoViewCall84)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoViewCall85)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoViewCall86)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQUndoView : public QUndoView {
public:
  using QUndoView::QUndoView;
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
      CuteQUndoViewCall0 call = reinterpret_cast<CuteQUndoViewCall0>(taken[0]);
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
      CuteQUndoViewCall1 call = reinterpret_cast<CuteQUndoViewCall1>(taken[1]);
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
      CuteQUndoViewCall2 call = reinterpret_cast<CuteQUndoViewCall2>(taken[2]);
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
      CuteQUndoViewCall3 call = reinterpret_cast<CuteQUndoViewCall3>(taken[3]);
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
      CuteQUndoViewCall4 call = reinterpret_cast<CuteQUndoViewCall4>(taken[4]);
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
      CuteQUndoViewCall5 call = reinterpret_cast<CuteQUndoViewCall5>(taken[5]);
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
      CuteQUndoViewCall6 call = reinterpret_cast<CuteQUndoViewCall6>(taken[6]);
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
      CuteQUndoViewCall7 call = reinterpret_cast<CuteQUndoViewCall7>(taken[7]);
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
      CuteQUndoViewCall8 call = reinterpret_cast<CuteQUndoViewCall8>(taken[8]);
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
      CuteQUndoViewCall9 call = reinterpret_cast<CuteQUndoViewCall9>(taken[9]);
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
      CuteQUndoViewCall10 call = reinterpret_cast<CuteQUndoViewCall10>(taken[10]);
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
      CuteQUndoViewCall11 call = reinterpret_cast<CuteQUndoViewCall11>(taken[11]);
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
      CuteQUndoViewCall12 call = reinterpret_cast<CuteQUndoViewCall12>(taken[12]);
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
      CuteQUndoViewCall13 call = reinterpret_cast<CuteQUndoViewCall13>(taken[13]);
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
      CuteQUndoViewCall14 call = reinterpret_cast<CuteQUndoViewCall14>(taken[14]);
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
      CuteQUndoViewCall15 call = reinterpret_cast<CuteQUndoViewCall15>(taken[15]);
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
      CuteQUndoViewCall16 call = reinterpret_cast<CuteQUndoViewCall16>(taken[16]);
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
      CuteQUndoViewCall17 call = reinterpret_cast<CuteQUndoViewCall17>(taken[17]);
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
      CuteQUndoViewCall18 call = reinterpret_cast<CuteQUndoViewCall18>(taken[18]);
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
      CuteQUndoViewCall19 call = reinterpret_cast<CuteQUndoViewCall19>(taken[19]);
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
      CuteQUndoViewCall20 call = reinterpret_cast<CuteQUndoViewCall20>(taken[20]);
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
      CuteQUndoViewCall21 call = reinterpret_cast<CuteQUndoViewCall21>(taken[21]);
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
      CuteQUndoViewCall22 call = reinterpret_cast<CuteQUndoViewCall22>(taken[22]);
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
      CuteQUndoViewCall23 call = reinterpret_cast<CuteQUndoViewCall23>(taken[23]);
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
      CuteQUndoViewCall24 call = reinterpret_cast<CuteQUndoViewCall24>(taken[24]);
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
      CuteQUndoViewCall25 call = reinterpret_cast<CuteQUndoViewCall25>(taken[25]);
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
      CuteQUndoViewCall26 call = reinterpret_cast<CuteQUndoViewCall26>(taken[26]);
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
      CuteQUndoViewCall27 call = reinterpret_cast<CuteQUndoViewCall27>(taken[27]);
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
      CuteQUndoViewCall28 call = reinterpret_cast<CuteQUndoViewCall28>(taken[28]);
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
      CuteQUndoViewCall29 call = reinterpret_cast<CuteQUndoViewCall29>(taken[29]);
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
      CuteQUndoViewCall30 call = reinterpret_cast<CuteQUndoViewCall30>(taken[30]);
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
      CuteQUndoViewCall31 call = reinterpret_cast<CuteQUndoViewCall31>(taken[31]);
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
      CuteQUndoViewCall32 call = reinterpret_cast<CuteQUndoViewCall32>(taken[32]);
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
      CuteQUndoViewCall33 call = reinterpret_cast<CuteQUndoViewCall33>(taken[33]);
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
      CuteQUndoViewCall34 call = reinterpret_cast<CuteQUndoViewCall34>(taken[34]);
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
      CuteQUndoViewCall35 call = reinterpret_cast<CuteQUndoViewCall35>(taken[35]);
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
      CuteQUndoViewCall36 call = reinterpret_cast<CuteQUndoViewCall36>(taken[36]);
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
      CuteQUndoViewCall37 call = reinterpret_cast<CuteQUndoViewCall37>(taken[37]);
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
      CuteQUndoViewCall38 call = reinterpret_cast<CuteQUndoViewCall38>(taken[38]);
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
      CuteQUndoViewCall39 call = reinterpret_cast<CuteQUndoViewCall39>(taken[39]);
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
      CuteQUndoViewCall40 call = reinterpret_cast<CuteQUndoViewCall40>(taken[40]);
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
      CuteQUndoViewCall41 call = reinterpret_cast<CuteQUndoViewCall41>(taken[41]);
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
      CuteQUndoViewCall42 call = reinterpret_cast<CuteQUndoViewCall42>(taken[42]);
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
      CuteQUndoViewCall43 call = reinterpret_cast<CuteQUndoViewCall43>(taken[43]);
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
      CuteQUndoViewCall44 call = reinterpret_cast<CuteQUndoViewCall44>(taken[44]);
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
      CuteQUndoViewCall45 call = reinterpret_cast<CuteQUndoViewCall45>(taken[45]);
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
      CuteQUndoViewCall46 call = reinterpret_cast<CuteQUndoViewCall46>(taken[46]);
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
      CuteQUndoViewCall47 call = reinterpret_cast<CuteQUndoViewCall47>(taken[47]);
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
      CuteQUndoViewCall48 call = reinterpret_cast<CuteQUndoViewCall48>(taken[48]);
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
      CuteQUndoViewCall49 call = reinterpret_cast<CuteQUndoViewCall49>(taken[49]);
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
      CuteQUndoViewCall50 call = reinterpret_cast<CuteQUndoViewCall50>(taken[50]);
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
      CuteQUndoViewCall51 call = reinterpret_cast<CuteQUndoViewCall51>(taken[51]);
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
      CuteQUndoViewCall52 call = reinterpret_cast<CuteQUndoViewCall52>(taken[52]);
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
      CuteQUndoViewCall53 call = reinterpret_cast<CuteQUndoViewCall53>(taken[53]);
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
      CuteQUndoViewCall54 call = reinterpret_cast<CuteQUndoViewCall54>(taken[54]);
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
      CuteQUndoViewCall55 call = reinterpret_cast<CuteQUndoViewCall55>(taken[55]);
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
      CuteQUndoViewCall56 call = reinterpret_cast<CuteQUndoViewCall56>(taken[56]);
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
      CuteQUndoViewCall57 call = reinterpret_cast<CuteQUndoViewCall57>(taken[57]);
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
      CuteQUndoViewCall58 call = reinterpret_cast<CuteQUndoViewCall58>(taken[58]);
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
      CuteQUndoViewCall59 call = reinterpret_cast<CuteQUndoViewCall59>(taken[59]);
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
      CuteQUndoViewCall60 call = reinterpret_cast<CuteQUndoViewCall60>(taken[60]);
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
      CuteQUndoViewCall61 call = reinterpret_cast<CuteQUndoViewCall61>(taken[61]);
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
      CuteQUndoViewCall62 call = reinterpret_cast<CuteQUndoViewCall62>(taken[62]);
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
      CuteQUndoViewCall63 call = reinterpret_cast<CuteQUndoViewCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[64]) {
      int handled = 0;
      CuteQUndoViewCall64 call = reinterpret_cast<CuteQUndoViewCall64>(taken[64]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQUndoViewCall65 call = reinterpret_cast<CuteQUndoViewCall65>(taken[65]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[66]) {
      int handled = 0;
      CuteQUndoViewCall66 call = reinterpret_cast<CuteQUndoViewCall66>(taken[66]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[67]) {
      int handled = 0;
      CuteQUndoViewCall67 call = reinterpret_cast<CuteQUndoViewCall67>(taken[67]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[68]) {
      int handled = 0;
      CuteQUndoViewCall68 call = reinterpret_cast<CuteQUndoViewCall68>(taken[68]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQUndoViewCall69 call = reinterpret_cast<CuteQUndoViewCall69>(taken[69]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQUndoViewCall70 call = reinterpret_cast<CuteQUndoViewCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQUndoViewCall71 call = reinterpret_cast<CuteQUndoViewCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQUndoViewCall72 call = reinterpret_cast<CuteQUndoViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQUndoViewCall73 call = reinterpret_cast<CuteQUndoViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQUndoViewCall74 call = reinterpret_cast<CuteQUndoViewCall74>(taken[74]);
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
      CuteQUndoViewCall75 call = reinterpret_cast<CuteQUndoViewCall75>(taken[75]);
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
      CuteQUndoViewCall76 call = reinterpret_cast<CuteQUndoViewCall76>(taken[76]);
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
      CuteQUndoViewCall77 call = reinterpret_cast<CuteQUndoViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQUndoViewCall78 call = reinterpret_cast<CuteQUndoViewCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQUndoViewCall79 call = reinterpret_cast<CuteQUndoViewCall79>(taken[79]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQUndoViewCall80 call = reinterpret_cast<CuteQUndoViewCall80>(taken[80]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQUndoViewCall81 call = reinterpret_cast<CuteQUndoViewCall81>(taken[81]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[82]) {
      int handled = 0;
      CuteQUndoViewCall82 call = reinterpret_cast<CuteQUndoViewCall82>(taken[82]);
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
      CuteQUndoViewCall83 call = reinterpret_cast<CuteQUndoViewCall83>(taken[83]);
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
      CuteQUndoViewCall84 call = reinterpret_cast<CuteQUndoViewCall84>(taken[84]);
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
      CuteQUndoViewCall85 call = reinterpret_cast<CuteQUndoViewCall85>(taken[85]);
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
      CuteQUndoViewCall86 call = reinterpret_cast<CuteQUndoViewCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QUndoView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QUndoView10metaObjectEv(
    const QUndoView *self) {
  return self->metaObject();
}

//  void *QUndoView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QUndoView11qt_metacastEPKc(QUndoView *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QUndoView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QUndoView11qt_metacallEN11QMetaObject4CallEiPPv(
    QUndoView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QUndoView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QUndoView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUndoView::tr(s, c, n));
}

//  QUndoViewPrivate *QUndoView::d_func()
extern "C" Q_DECL_EXPORT
QUndoViewPrivate *ritual_ZN9QUndoView6d_funcEv(QUndoView *self) {
  return self->d_func();
}

//  const QUndoViewPrivate *QUndoView::d_func() const
extern "C" Q_DECL_EXPORT
const QUndoViewPrivate *ritual_ZNK9QUndoView6d_funcEv(
    const QUndoView *self) {
  return self->d_func();
}

//  QUndoView::QUndoView(QWidget *parent)
extern "C" Q_DECL_EXPORT
QUndoView *ritual_ZN9QUndoViewC1EP7QWidget(QWidget *parent) {
  return new CuteQUndoView(parent);
}

//  QUndoView::QUndoView(QUndoStack *stack, QWidget *parent)
extern "C" Q_DECL_EXPORT
QUndoView *ritual_ZN9QUndoViewC1EP10QUndoStackP7QWidget(
    QUndoStack *stack,
    QWidget *parent) {
  return new CuteQUndoView(stack, parent);
}

#if QT_CONFIG(undogroup)
//  QUndoView::QUndoView(QUndoGroup *group, QWidget *parent)
extern "C" Q_DECL_EXPORT
QUndoView *ritual_ZN9QUndoViewC1EP10QUndoGroupP7QWidget(
    QUndoGroup *group,
    QWidget *parent) {
  return new CuteQUndoView(group, parent);
}
#endif  // QT_CONFIG(undogroup)

//  QUndoView::~QUndoView()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoViewD1Ev(QUndoView *self) {
  delete self;
}

//  QUndoStack *QUndoView::stack() const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZNK9QUndoView5stackEv(const QUndoView *self) {
  return self->stack();
}

#if QT_CONFIG(undogroup)
//  QUndoGroup *QUndoView::group() const
extern "C" Q_DECL_EXPORT
QUndoGroup *ritual_ZNK9QUndoView5groupEv(const QUndoView *self) {
  return self->group();
}
#endif  // QT_CONFIG(undogroup)

//  void QUndoView::setEmptyLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView13setEmptyLabelERK7QString(
    QUndoView *self,
    const QString *label) {
  self->setEmptyLabel(*label);
}

//  QString QUndoView::emptyLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QUndoView10emptyLabelEv(const QUndoView *self) {
  return new QString(self->emptyLabel());
}

//  void QUndoView::setCleanIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView12setCleanIconERK5QIcon(
    QUndoView *self,
    const QIcon *icon) {
  self->setCleanIcon(*icon);
}

//  QIcon QUndoView::cleanIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK9QUndoView9cleanIconEv(const QUndoView *self) {
  return new QIcon(self->cleanIcon());
}

//  void QUndoView::setStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView8setStackEP10QUndoStack(
    QUndoView *self,
    QUndoStack *stack) {
  self->setStack(stack);
}

#if QT_CONFIG(undogroup)
//  void QUndoView::setGroup(QUndoGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QUndoView8setGroupEP10QUndoGroup(
    QUndoView *self,
    QUndoGroup *group) {
  self->setGroup(group);
}
#endif  // QT_CONFIG(undogroup)

//  a Python function taken by a CuteQUndoView, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUndoView(QUndoView *self, const char *key, void *call) {
  return static_cast<CuteQUndoView *>(self)->take(key, call);
}

#endif  // QT_CONFIG(undoview)
#endif  // QT_CONFIG(undoview)
