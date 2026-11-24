//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemview.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAbstractItemView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractItemView : QAbstractItemView {
  using QAbstractItemView::rowsInserted;
  using QAbstractItemView::rowsAboutToBeRemoved;
  using QAbstractItemView::selectionChanged;
  using QAbstractItemView::currentChanged;
  using QAbstractItemView::updateEditorData;
  using QAbstractItemView::updateEditorGeometries;
  using QAbstractItemView::updateGeometries;
  using QAbstractItemView::verticalScrollbarAction;
  using QAbstractItemView::horizontalScrollbarAction;
  using QAbstractItemView::verticalScrollbarValueChanged;
  using QAbstractItemView::horizontalScrollbarValueChanged;
  using QAbstractItemView::closeEditor;
  using QAbstractItemView::commitData;
  using QAbstractItemView::editorDestroyed;
  using QAbstractItemView::edit;
  using QAbstractItemView::selectionCommand;
  using QAbstractItemView::startDrag;
  using QAbstractItemView::initViewItemOption;
  using QAbstractItemView::focusNextPrevChild;
  using QAbstractItemView::event;
  using QAbstractItemView::viewportEvent;
  using QAbstractItemView::mousePressEvent;
  using QAbstractItemView::mouseMoveEvent;
  using QAbstractItemView::mouseReleaseEvent;
  using QAbstractItemView::mouseDoubleClickEvent;
  using QAbstractItemView::dragEnterEvent;
  using QAbstractItemView::dragMoveEvent;
  using QAbstractItemView::dragLeaveEvent;
  using QAbstractItemView::dropEvent;
  using QAbstractItemView::focusInEvent;
  using QAbstractItemView::focusOutEvent;
  using QAbstractItemView::keyPressEvent;
  using QAbstractItemView::resizeEvent;
  using QAbstractItemView::timerEvent;
  using QAbstractItemView::inputMethodEvent;
  using QAbstractItemView::eventFilter;
  using QAbstractItemView::viewportSizeHint;
};

//  A QAbstractItemView that Python can take functions over in. Every QAbstractItemView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall0)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall1)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQAbstractItemViewCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall4)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QModelIndex * (*CuteQAbstractItemViewCall5)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAbstractItemViewCall6)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAbstractItemViewCall7)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQAbstractItemViewCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQAbstractItemViewCall9)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall10)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall12)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall13)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall14)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall15)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall16)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall17)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall18)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall19)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall20)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall21)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall22)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall23)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall24)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall25)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall26)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall27)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAbstractItemViewCall28)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAbstractItemViewCall29)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewCall30)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall31)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRegion * (*CuteQAbstractItemViewCall32)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewCall33)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQAbstractItemViewCall34)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQAbstractItemViewCall35)(const void *, int, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall36)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewCall37)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewCall38)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewCall39)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall40)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall41)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall42)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall43)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall44)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall45)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall46)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall47)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall48)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall49)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall50)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall51)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall52)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewCall53)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewCall54)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QSize * (*CuteQAbstractItemViewCall55)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQAbstractItemViewCall56)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQAbstractItemViewCall57)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewCall58)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewCall59)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewCall60)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewCall61)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewCall62)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewCall63)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractItemViewCall64)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQAbstractItemViewCall65)(const void *, int *);
typedef void (*CuteQAbstractItemViewCall66)(const void *, bool, int *);
typedef int (*CuteQAbstractItemViewCall67)(const void *, int, int *);
typedef bool (*CuteQAbstractItemViewCall68)(const void *, int *);
typedef void * (*CuteQAbstractItemViewCall69)(const void *, int *);
typedef void (*CuteQAbstractItemViewCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQAbstractItemViewCall71)(const void *, QEnterEvent *, int *);
typedef void (*CuteQAbstractItemViewCall72)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractItemViewCall73)(const void *, QMoveEvent *, int *);
typedef void (*CuteQAbstractItemViewCall74)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQAbstractItemViewCall75)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQAbstractItemViewCall76)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQAbstractItemViewCall77)(const void *, QShowEvent *, int *);
typedef void (*CuteQAbstractItemViewCall78)(const void *, QHideEvent *, int *);
typedef int (*CuteQAbstractItemViewCall79)(const void *, int, int *);
typedef void (*CuteQAbstractItemViewCall80)(const void *, QPainter *, int *);
typedef void * (*CuteQAbstractItemViewCall81)(const void *, QPoint *, int *);
typedef void * (*CuteQAbstractItemViewCall82)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemViewCall83)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemViewCall84)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemViewCall85)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemViewCall86)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractItemView : public QAbstractItemView {
public:
  using QAbstractItemView::QAbstractItemView;
  void *taken[87] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8setModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14keyboardSearchERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14sizeHintForRowEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView17sizeHintForColumnEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9selectAllEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateEditorDataEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView22updateEditorGeometriesEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView16updateGeometriesEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView23verticalScrollbarActionEi")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView25horizontalScrollbarActionEi")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView29verticalScrollbarValueChangedEi")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView10commitDataEP7QWidget")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView15editorDestroyedEP7QObject")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16horizontalOffsetEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView14verticalOffsetEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13viewportEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[53] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[54] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK19QAbstractScrollArea16viewportSizeHintEv")) {
      taken[55] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[56] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[57] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea13setupViewportEP7QWidget")) {
      taken[58] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[59] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[60] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[61] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[62] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
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
  //  void QAbstractItemView::setModel(QAbstractItemModel *model)
  void setModel(QAbstractItemModel *model) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractItemViewCall0 call = reinterpret_cast<CuteQAbstractItemViewCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractItemViewCall1 call = reinterpret_cast<CuteQAbstractItemViewCall1>(taken[1]);
      call(this, selectionModel, &handled);
      if (handled) return;
    }
    QAbstractItemView::setSelectionModel(selectionModel);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyboardSearch(const QString &search)
  void keyboardSearch(const QString &search) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractItemViewCall2 call = reinterpret_cast<CuteQAbstractItemViewCall2>(taken[2]);
      call(this, &search, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyboardSearch(search);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QRect QAbstractItemView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractItemViewCall3 call = reinterpret_cast<CuteQAbstractItemViewCall3>(taken[3]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::scrollTo(const QModelIndex &index, ScrollHint
  //      hint)
  void scrollTo(
      const QModelIndex &index,
      QAbstractItemView::ScrollHint hint) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractItemViewCall4 call = reinterpret_cast<CuteQAbstractItemViewCall4>(taken[4]);
      call(this, &index, static_cast<int>(hint), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QModelIndex QAbstractItemView::indexAt(const QPoint &point) const
  QModelIndex indexAt(const QPoint &point) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractItemViewCall5 call = reinterpret_cast<CuteQAbstractItemViewCall5>(taken[5]);
      const QModelIndex * given = call(this, &point, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForRow(int row) const
  int sizeHintForRow(int row) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractItemViewCall6 call = reinterpret_cast<CuteQAbstractItemViewCall6>(taken[6]);
      int given = call(this, row, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::sizeHintForRow(row);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::sizeHintForColumn(int column) const
  int sizeHintForColumn(int column) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractItemViewCall7 call = reinterpret_cast<CuteQAbstractItemViewCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractItemViewCall8 call = reinterpret_cast<CuteQAbstractItemViewCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractItemViewCall9 call = reinterpret_cast<CuteQAbstractItemViewCall9>(taken[9]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemView::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::reset()
  void reset() override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractItemViewCall10 call = reinterpret_cast<CuteQAbstractItemViewCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::reset();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setRootIndex(const QModelIndex &index)
  void setRootIndex(const QModelIndex &index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractItemViewCall11 call = reinterpret_cast<CuteQAbstractItemViewCall11>(taken[11]);
      call(this, &index, &handled);
      if (handled) return;
    }
    QAbstractItemView::setRootIndex(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::doItemsLayout()
  void doItemsLayout() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractItemViewCall12 call = reinterpret_cast<CuteQAbstractItemViewCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::doItemsLayout();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::selectAll()
  void selectAll() override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractItemViewCall13 call = reinterpret_cast<CuteQAbstractItemViewCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractItemViewCall14 call = reinterpret_cast<CuteQAbstractItemViewCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractItemViewCall15 call = reinterpret_cast<CuteQAbstractItemViewCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractItemViewCall16 call = reinterpret_cast<CuteQAbstractItemViewCall16>(taken[16]);
      call(this, &selected, &deselected, &handled);
      if (handled) return;
    }
    QAbstractItemView::selectionChanged(selected, deselected);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::currentChanged(const QModelIndex &current,
  //      const QModelIndex &previous)
  void currentChanged(
      const QModelIndex &current,
      const QModelIndex &previous) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractItemViewCall17 call = reinterpret_cast<CuteQAbstractItemViewCall17>(taken[17]);
      call(this, &current, &previous, &handled);
      if (handled) return;
    }
    QAbstractItemView::currentChanged(current, previous);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorData()
  void updateEditorData() override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractItemViewCall18 call = reinterpret_cast<CuteQAbstractItemViewCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorData();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateEditorGeometries()
  void updateEditorGeometries() override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractItemViewCall19 call = reinterpret_cast<CuteQAbstractItemViewCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateEditorGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::updateGeometries()
  void updateGeometries() override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractItemViewCall20 call = reinterpret_cast<CuteQAbstractItemViewCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemView::updateGeometries();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarAction(int action)
  void verticalScrollbarAction(int action) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractItemViewCall21 call = reinterpret_cast<CuteQAbstractItemViewCall21>(taken[21]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarAction(int action)
  void horizontalScrollbarAction(int action) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractItemViewCall22 call = reinterpret_cast<CuteQAbstractItemViewCall22>(taken[22]);
      call(this, action, &handled);
      if (handled) return;
    }
    QAbstractItemView::horizontalScrollbarAction(action);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::verticalScrollbarValueChanged(int value)
  void verticalScrollbarValueChanged(int value) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractItemViewCall23 call = reinterpret_cast<CuteQAbstractItemViewCall23>(taken[23]);
      call(this, value, &handled);
      if (handled) return;
    }
    QAbstractItemView::verticalScrollbarValueChanged(value);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
  void horizontalScrollbarValueChanged(int value) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractItemViewCall24 call = reinterpret_cast<CuteQAbstractItemViewCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractItemViewCall25 call = reinterpret_cast<CuteQAbstractItemViewCall25>(taken[25]);
      call(this, editor, static_cast<int>(hint), &handled);
      if (handled) return;
    }
    QAbstractItemView::closeEditor(editor, hint);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::commitData(QWidget *editor)
  void commitData(QWidget *editor) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractItemViewCall26 call = reinterpret_cast<CuteQAbstractItemViewCall26>(taken[26]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::commitData(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::editorDestroyed(QObject *editor)
  void editorDestroyed(QObject *editor) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractItemViewCall27 call = reinterpret_cast<CuteQAbstractItemViewCall27>(taken[27]);
      call(this, editor, &handled);
      if (handled) return;
    }
    QAbstractItemView::editorDestroyed(editor);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractItemViewCall28 call = reinterpret_cast<CuteQAbstractItemViewCall28>(taken[28]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  int QAbstractItemView::verticalOffset() const
  int verticalOffset() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractItemViewCall29 call = reinterpret_cast<CuteQAbstractItemViewCall29>(taken[29]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::isIndexHidden(const QModelIndex &index) const
  bool isIndexHidden(const QModelIndex &index) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractItemViewCall30 call = reinterpret_cast<CuteQAbstractItemViewCall30>(taken[30]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::setSelection(const QRect &rect,
  //      QItemSelectionModel::SelectionFlags command)
  void setSelection(
      const QRect &rect,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractItemViewCall31 call = reinterpret_cast<CuteQAbstractItemViewCall31>(taken[31]);
      call(this, &rect, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QRegion QAbstractItemView::visualRegionForSelection(const
  //      QItemSelection &selection) const
  QRegion visualRegionForSelection(
      const QItemSelection &selection) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractItemViewCall32 call = reinterpret_cast<CuteQAbstractItemViewCall32>(taken[32]);
      const QRegion * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
  //      trigger, QEvent *event)
  bool edit(
      const QModelIndex &index,
      QAbstractItemView::EditTrigger trigger,
      QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractItemViewCall33 call = reinterpret_cast<CuteQAbstractItemViewCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractItemViewCall34 call = reinterpret_cast<CuteQAbstractItemViewCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractItemViewCall35 call = reinterpret_cast<CuteQAbstractItemViewCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractItemViewCall36 call = reinterpret_cast<CuteQAbstractItemViewCall36>(taken[36]);
      call(this, option, &handled);
      if (handled) return;
    }
    QAbstractItemView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractItemViewCall37 call = reinterpret_cast<CuteQAbstractItemViewCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractItemViewCall38 call = reinterpret_cast<CuteQAbstractItemViewCall38>(taken[38]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractItemView::event(event);
  }
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  bool QAbstractItemView::viewportEvent(QEvent *event)
  bool viewportEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractItemViewCall39 call = reinterpret_cast<CuteQAbstractItemViewCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractItemViewCall40 call = reinterpret_cast<CuteQAbstractItemViewCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mousePressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractItemViewCall41 call = reinterpret_cast<CuteQAbstractItemViewCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseMoveEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractItemViewCall42 call = reinterpret_cast<CuteQAbstractItemViewCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::mouseReleaseEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQAbstractItemViewCall43 call = reinterpret_cast<CuteQAbstractItemViewCall43>(taken[43]);
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
    if (taken[44]) {
      int handled = 0;
      CuteQAbstractItemViewCall44 call = reinterpret_cast<CuteQAbstractItemViewCall44>(taken[44]);
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
    if (taken[45]) {
      int handled = 0;
      CuteQAbstractItemViewCall45 call = reinterpret_cast<CuteQAbstractItemViewCall45>(taken[45]);
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
    if (taken[46]) {
      int handled = 0;
      CuteQAbstractItemViewCall46 call = reinterpret_cast<CuteQAbstractItemViewCall46>(taken[46]);
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
    if (taken[47]) {
      int handled = 0;
      CuteQAbstractItemViewCall47 call = reinterpret_cast<CuteQAbstractItemViewCall47>(taken[47]);
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
    if (taken[48]) {
      int handled = 0;
      CuteQAbstractItemViewCall48 call = reinterpret_cast<CuteQAbstractItemViewCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusInEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQAbstractItemViewCall49 call = reinterpret_cast<CuteQAbstractItemViewCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::focusOutEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQAbstractItemViewCall50 call = reinterpret_cast<CuteQAbstractItemViewCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QAbstractItemView::keyPressEvent(event);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQAbstractItemViewCall51 call = reinterpret_cast<CuteQAbstractItemViewCall51>(taken[51]);
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
    if (taken[52]) {
      int handled = 0;
      CuteQAbstractItemViewCall52 call = reinterpret_cast<CuteQAbstractItemViewCall52>(taken[52]);
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
    if (taken[53]) {
      int handled = 0;
      CuteQAbstractItemViewCall53 call = reinterpret_cast<CuteQAbstractItemViewCall53>(taken[53]);
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
    if (taken[54]) {
      int handled = 0;
      CuteQAbstractItemViewCall54 call = reinterpret_cast<CuteQAbstractItemViewCall54>(taken[54]);
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
    if (taken[55]) {
      int handled = 0;
      CuteQAbstractItemViewCall55 call = reinterpret_cast<CuteQAbstractItemViewCall55>(taken[55]);
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
    if (taken[56]) {
      int handled = 0;
      CuteQAbstractItemViewCall56 call = reinterpret_cast<CuteQAbstractItemViewCall56>(taken[56]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::minimumSizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QSize QAbstractScrollArea::sizeHint() const
  QSize sizeHint() const override {
    if (taken[57]) {
      int handled = 0;
      CuteQAbstractItemViewCall57 call = reinterpret_cast<CuteQAbstractItemViewCall57>(taken[57]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollArea::sizeHint();
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::setupViewport(QWidget *viewport)
  void setupViewport(QWidget *viewport) override {
    if (taken[58]) {
      int handled = 0;
      CuteQAbstractItemViewCall58 call = reinterpret_cast<CuteQAbstractItemViewCall58>(taken[58]);
      call(this, viewport, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::setupViewport(viewport);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQAbstractItemViewCall59 call = reinterpret_cast<CuteQAbstractItemViewCall59>(taken[59]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::paintEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(wheelevent)
#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQAbstractItemViewCall60 call = reinterpret_cast<CuteQAbstractItemViewCall60>(taken[60]);
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
    if (taken[61]) {
      int handled = 0;
      CuteQAbstractItemViewCall61 call = reinterpret_cast<CuteQAbstractItemViewCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::contextMenuEvent(a0);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(scrollarea)
  //  void QAbstractScrollArea::scrollContentsBy(int dx, int dy)
  void scrollContentsBy(int dx, int dy) override {
    if (taken[62]) {
      int handled = 0;
      CuteQAbstractItemViewCall62 call = reinterpret_cast<CuteQAbstractItemViewCall62>(taken[62]);
      call(this, dx, dy, &handled);
      if (handled) return;
    }
    QAbstractScrollArea::scrollContentsBy(dx, dy);
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QFrame::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQAbstractItemViewCall63 call = reinterpret_cast<CuteQAbstractItemViewCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[64]) {
      int handled = 0;
      CuteQAbstractItemViewCall64 call = reinterpret_cast<CuteQAbstractItemViewCall64>(taken[64]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQAbstractItemViewCall65 call = reinterpret_cast<CuteQAbstractItemViewCall65>(taken[65]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[66]) {
      int handled = 0;
      CuteQAbstractItemViewCall66 call = reinterpret_cast<CuteQAbstractItemViewCall66>(taken[66]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[67]) {
      int handled = 0;
      CuteQAbstractItemViewCall67 call = reinterpret_cast<CuteQAbstractItemViewCall67>(taken[67]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[68]) {
      int handled = 0;
      CuteQAbstractItemViewCall68 call = reinterpret_cast<CuteQAbstractItemViewCall68>(taken[68]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQAbstractItemViewCall69 call = reinterpret_cast<CuteQAbstractItemViewCall69>(taken[69]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQAbstractItemViewCall70 call = reinterpret_cast<CuteQAbstractItemViewCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQAbstractItemViewCall71 call = reinterpret_cast<CuteQAbstractItemViewCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQAbstractItemViewCall72 call = reinterpret_cast<CuteQAbstractItemViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQAbstractItemViewCall73 call = reinterpret_cast<CuteQAbstractItemViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQAbstractItemViewCall74 call = reinterpret_cast<CuteQAbstractItemViewCall74>(taken[74]);
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
      CuteQAbstractItemViewCall75 call = reinterpret_cast<CuteQAbstractItemViewCall75>(taken[75]);
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
      CuteQAbstractItemViewCall76 call = reinterpret_cast<CuteQAbstractItemViewCall76>(taken[76]);
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
      CuteQAbstractItemViewCall77 call = reinterpret_cast<CuteQAbstractItemViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQAbstractItemViewCall78 call = reinterpret_cast<CuteQAbstractItemViewCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQAbstractItemViewCall79 call = reinterpret_cast<CuteQAbstractItemViewCall79>(taken[79]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQAbstractItemViewCall80 call = reinterpret_cast<CuteQAbstractItemViewCall80>(taken[80]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQAbstractItemViewCall81 call = reinterpret_cast<CuteQAbstractItemViewCall81>(taken[81]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[82]) {
      int handled = 0;
      CuteQAbstractItemViewCall82 call = reinterpret_cast<CuteQAbstractItemViewCall82>(taken[82]);
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
      CuteQAbstractItemViewCall83 call = reinterpret_cast<CuteQAbstractItemViewCall83>(taken[83]);
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
      CuteQAbstractItemViewCall84 call = reinterpret_cast<CuteQAbstractItemViewCall84>(taken[84]);
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
      CuteQAbstractItemViewCall85 call = reinterpret_cast<CuteQAbstractItemViewCall85>(taken[85]);
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
      CuteQAbstractItemViewCall86 call = reinterpret_cast<CuteQAbstractItemViewCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractItemView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAbstractItemView10metaObjectEv(
    const QAbstractItemView *self) {
  return self->metaObject();
}

//  QString QAbstractItemView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAbstractItemView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemView::tr(s, c, n));
}

//  QAbstractItemView::~QAbstractItemView()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemViewD1Ev(QAbstractItemView *self) {
  delete self;
}

//  void QAbstractItemView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView8setModelEP18QAbstractItemModel(
    QAbstractItemView *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  QAbstractItemModel *QAbstractItemView::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK17QAbstractItemView5modelEv(
    const QAbstractItemView *self) {
  return self->model();
}

//  void QAbstractItemView::setSelectionModel(QItemSelectionModel
//      *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel(
    QAbstractItemView *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  QItemSelectionModel *QAbstractItemView::selectionModel() const
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZNK17QAbstractItemView14selectionModelEv(
    const QAbstractItemView *self) {
  return self->selectionModel();
}

//  void QAbstractItemView::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setItemDelegateEP21QAbstractItemDelegate(
    QAbstractItemView *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView12itemDelegateEv(
    const QAbstractItemView *self) {
  return self->itemDelegate();
}

//  void QAbstractItemView::setSelectionMode(QAbstractItemView::SelectionMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16setSelectionModeENS_13SelectionModeE(
    QAbstractItemView *self,
    QAbstractItemView::SelectionMode mode) {
  self->setSelectionMode(mode);
}

//  QAbstractItemView::SelectionMode QAbstractItemView::selectionMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::SelectionMode ritual_ZNK17QAbstractItemView13selectionModeEv(
    const QAbstractItemView *self) {
  return self->selectionMode();
}

//  void QAbstractItemView::setSelectionBehavior(QAbstractItemView::Selection
//      Behavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20setSelectionBehaviorENS_17SelectionBehaviorE(
    QAbstractItemView *self,
    QAbstractItemView::SelectionBehavior behavior) {
  self->setSelectionBehavior(behavior);
}

//  QAbstractItemView::SelectionBehavior
//      QAbstractItemView::selectionBehavior() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::SelectionBehavior ritual_ZNK17QAbstractItemView17selectionBehaviorEv(
    const QAbstractItemView *self) {
  return self->selectionBehavior();
}

//  QModelIndex QAbstractItemView::currentIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QAbstractItemView12currentIndexEv(
    const QAbstractItemView *self) {
  return new QModelIndex(self->currentIndex());
}

//  QModelIndex QAbstractItemView::rootIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QAbstractItemView9rootIndexEv(
    const QAbstractItemView *self) {
  return new QModelIndex(self->rootIndex());
}

//  void QAbstractItemView::setEditTriggers(EditTriggers triggers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setEditTriggersE6QFlagsINS_11EditTriggerEE(
    QAbstractItemView *self,
    int triggers) {
  self->setEditTriggers(
      QFlags<QAbstractItemView::EditTrigger>::fromInt(triggers));
}

//  EditTriggers QAbstractItemView::editTriggers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView12editTriggersEv(
    const QAbstractItemView *self) {
  return static_cast<int>(self->editTriggers().toInt());
}

//  void QAbstractItemView::setVerticalScrollMode(ScrollMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21setVerticalScrollModeENS_10ScrollModeE(
    QAbstractItemView *self,
    QAbstractItemView::ScrollMode mode) {
  self->setVerticalScrollMode(mode);
}

//  ScrollMode QAbstractItemView::verticalScrollMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::ScrollMode ritual_ZNK17QAbstractItemView18verticalScrollModeEv(
    const QAbstractItemView *self) {
  return self->verticalScrollMode();
}

//  void QAbstractItemView::resetVerticalScrollMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23resetVerticalScrollModeEv(
    QAbstractItemView *self) {
  self->resetVerticalScrollMode();
}

//  void QAbstractItemView::setHorizontalScrollMode(ScrollMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23setHorizontalScrollModeENS_10ScrollModeE(
    QAbstractItemView *self,
    QAbstractItemView::ScrollMode mode) {
  self->setHorizontalScrollMode(mode);
}

//  ScrollMode QAbstractItemView::horizontalScrollMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::ScrollMode ritual_ZNK17QAbstractItemView20horizontalScrollModeEv(
    const QAbstractItemView *self) {
  return self->horizontalScrollMode();
}

//  void QAbstractItemView::resetHorizontalScrollMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView25resetHorizontalScrollModeEv(
    QAbstractItemView *self) {
  self->resetHorizontalScrollMode();
}

//  void QAbstractItemView::setAutoScroll(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13setAutoScrollEb(
    QAbstractItemView *self,
    bool enable) {
  self->setAutoScroll(enable);
}

//  bool QAbstractItemView::hasAutoScroll() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView13hasAutoScrollEv(
    const QAbstractItemView *self) {
  return self->hasAutoScroll();
}

//  void QAbstractItemView::setAutoScrollMargin(int margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView19setAutoScrollMarginEi(
    QAbstractItemView *self,
    int margin) {
  self->setAutoScrollMargin(margin);
}

//  int QAbstractItemView::autoScrollMargin() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView16autoScrollMarginEv(
    const QAbstractItemView *self) {
  return self->autoScrollMargin();
}

//  void QAbstractItemView::setTabKeyNavigation(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView19setTabKeyNavigationEb(
    QAbstractItemView *self,
    bool enable) {
  self->setTabKeyNavigation(enable);
}

//  bool QAbstractItemView::tabKeyNavigation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView16tabKeyNavigationEv(
    const QAbstractItemView *self) {
  return self->tabKeyNavigation();
}

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::setDropIndicatorShown(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21setDropIndicatorShownEb(
    QAbstractItemView *self,
    bool enable) {
  self->setDropIndicatorShown(enable);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemView::showDropIndicator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView17showDropIndicatorEv(
    const QAbstractItemView *self) {
  return self->showDropIndicator();
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::setDragEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14setDragEnabledEb(
    QAbstractItemView *self,
    bool enable) {
  self->setDragEnabled(enable);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemView::dragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView11dragEnabledEv(
    const QAbstractItemView *self) {
  return self->dragEnabled();
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::setDragDropOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView24setDragDropOverwriteModeEb(
    QAbstractItemView *self,
    bool overwrite) {
  self->setDragDropOverwriteMode(overwrite);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemView::dragDropOverwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView21dragDropOverwriteModeEv(
    const QAbstractItemView *self) {
  return self->dragDropOverwriteMode();
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::setDragDropMode(DragDropMode behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setDragDropModeENS_12DragDropModeE(
    QAbstractItemView *self,
    QAbstractItemView::DragDropMode behavior) {
  self->setDragDropMode(behavior);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  DragDropMode QAbstractItemView::dragDropMode() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::DragDropMode ritual_ZNK17QAbstractItemView12dragDropModeEv(
    const QAbstractItemView *self) {
  return self->dragDropMode();
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::setDefaultDropAction(Qt::DropAction dropAction)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20setDefaultDropActionEN2Qt10DropActionE(
    QAbstractItemView *self,
    Qt::DropAction dropAction) {
  self->setDefaultDropAction(dropAction);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  Qt::DropAction QAbstractItemView::defaultDropAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK17QAbstractItemView17defaultDropActionEv(
    const QAbstractItemView *self) {
  return self->defaultDropAction();
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractItemView::setAlternatingRowColors(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23setAlternatingRowColorsEb(
    QAbstractItemView *self,
    bool enable) {
  self->setAlternatingRowColors(enable);
}

//  bool QAbstractItemView::alternatingRowColors() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView20alternatingRowColorsEv(
    const QAbstractItemView *self) {
  return self->alternatingRowColors();
}

//  void QAbstractItemView::setIconSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView11setIconSizeERK5QSize(
    QAbstractItemView *self,
    const QSize *size) {
  self->setIconSize(*size);
}

//  QSize QAbstractItemView::iconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QAbstractItemView8iconSizeEv(
    const QAbstractItemView *self) {
  return new QSize(self->iconSize());
}

//  void QAbstractItemView::setTextElideMode(Qt::TextElideMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16setTextElideModeEN2Qt13TextElideModeE(
    QAbstractItemView *self,
    Qt::TextElideMode mode) {
  self->setTextElideMode(mode);
}

//  Qt::TextElideMode QAbstractItemView::textElideMode() const
extern "C" Q_DECL_EXPORT
Qt::TextElideMode ritual_ZNK17QAbstractItemView13textElideModeEv(
    const QAbstractItemView *self) {
  return self->textElideMode();
}

//  void QAbstractItemView::keyboardSearch(const QString &search)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14keyboardSearchERK7QString(
    QAbstractItemView *self,
    const QString *search) {
  self->keyboardSearch(*search);
}

//  QRect QAbstractItemView::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QAbstractItemView10visualRectERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  void QAbstractItemView::scrollTo(const QModelIndex &index, ScrollHint
//      hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE(
    QAbstractItemView *self,
    const QModelIndex *index,
    QAbstractItemView::ScrollHint hint) {
  self->scrollTo(*index, hint);
}

//  QModelIndex QAbstractItemView::indexAt(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK17QAbstractItemView7indexAtERK6QPoint(
    const QAbstractItemView *self,
    const QPoint *point) {
  return new QModelIndex(self->indexAt(*point));
}

//  QSize QAbstractItemView::sizeHintForIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QAbstractItemView16sizeHintForIndexERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return new QSize(self->sizeHintForIndex(*index));
}

//  int QAbstractItemView::sizeHintForRow(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView14sizeHintForRowEi(
    const QAbstractItemView *self,
    int row) {
  return self->sizeHintForRow(row);
}

//  int QAbstractItemView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView17sizeHintForColumnEi(
    const QAbstractItemView *self,
    int column) {
  return self->sizeHintForColumn(column);
}

//  int QAbstractItemView::updateThreshold() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView15updateThresholdEv(
    const QAbstractItemView *self) {
  return self->updateThreshold();
}

//  void QAbstractItemView::setUpdateThreshold(int threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView18setUpdateThresholdEi(
    QAbstractItemView *self,
    int threshold) {
  self->setUpdateThreshold(threshold);
}

//  Qt::MatchFlags QAbstractItemView::keyboardSearchFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView19keyboardSearchFlagsEv(
    const QAbstractItemView *self) {
  return static_cast<int>(self->keyboardSearchFlags().toInt());
}

//  void QAbstractItemView::setKeyboardSearchFlags(Qt::MatchFlags
//      searchFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView22setKeyboardSearchFlagsE6QFlagsIN2Qt9MatchFlagEE(
    QAbstractItemView *self,
    int searchFlags) {
  self->setKeyboardSearchFlags(QFlags<Qt::MatchFlag>::fromInt(searchFlags));
}

//  void QAbstractItemView::openPersistentEditor(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20openPersistentEditorERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->openPersistentEditor(*index);
}

//  void QAbstractItemView::closePersistentEditor(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21closePersistentEditorERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->closePersistentEditor(*index);
}

//  bool QAbstractItemView::isPersistentEditorOpen(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView22isPersistentEditorOpenERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->isPersistentEditorOpen(*index);
}

//  void QAbstractItemView::setIndexWidget(const QModelIndex &index, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14setIndexWidgetERK11QModelIndexP7QWidget(
    QAbstractItemView *self,
    const QModelIndex *index,
    QWidget *widget) {
  self->setIndexWidget(*index, widget);
}

//  QWidget *QAbstractItemView::indexWidget(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK17QAbstractItemView11indexWidgetERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->indexWidget(*index);
}

//  void QAbstractItemView::setItemDelegateForRow(int row,
//      QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21setItemDelegateForRowEiP21QAbstractItemDelegate(
    QAbstractItemView *self,
    int row,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegateForRow(row, delegate);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForRow(int row)
//      const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView18itemDelegateForRowEi(
    const QAbstractItemView *self,
    int row) {
  return self->itemDelegateForRow(row);
}

//  void QAbstractItemView::setItemDelegateForColumn(int column,
//      QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView24setItemDelegateForColumnEiP21QAbstractItemDelegate(
    QAbstractItemView *self,
    int column,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegateForColumn(column, delegate);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForColumn(int
//      column) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView21itemDelegateForColumnEi(
    const QAbstractItemView *self,
    int column) {
  return self->itemDelegateForColumn(column);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QAbstractItemDelegate *QAbstractItemView::itemDelegate(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView12itemDelegateERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->itemDelegate(*index);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->itemDelegateForIndex(*index);
}

//  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QAbstractItemView16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QAbstractItemView *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  void QAbstractItemView::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView5resetEv(QAbstractItemView *self) {
  self->reset();
}

//  void QAbstractItemView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView12setRootIndexERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->setRootIndex(*index);
}

//  void QAbstractItemView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13doItemsLayoutEv(QAbstractItemView *self) {
  self->doItemsLayout();
}

//  void QAbstractItemView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView9selectAllEv(QAbstractItemView *self) {
  self->selectAll();
}

//  void QAbstractItemView::edit(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView4editERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->edit(*index);
}

//  void QAbstractItemView::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14clearSelectionEv(
    QAbstractItemView *self) {
  self->clearSelection();
}

//  void QAbstractItemView::setCurrentIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15setCurrentIndexERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->setCurrentIndex(*index);
}

//  void QAbstractItemView::scrollToTop()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView11scrollToTopEv(QAbstractItemView *self) {
  self->scrollToTop();
}

//  void QAbstractItemView::scrollToBottom()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14scrollToBottomEv(
    QAbstractItemView *self) {
  self->scrollToBottom();
}

//  void QAbstractItemView::update(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView6updateERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->update(*index);
}

//  void QAbstractItemView::rowsInserted(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii(
    QAbstractItemView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsInserted(*parent, start, end);
}

//  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii(
    QAbstractItemView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsAboutToBeRemoved(*parent, start, end);
}

//  void QAbstractItemView::selectionChanged(const QItemSelection &selected,
//      const QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_(
    QAbstractItemView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  self->selectionChanged(*selected, *deselected);
}

//  void QAbstractItemView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_(
    QAbstractItemView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  self->currentChanged(*current, *previous);
}

//  void QAbstractItemView::updateEditorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16updateEditorDataEv(
    QAbstractItemView *self) {
  self->updateEditorData();
}

//  void QAbstractItemView::updateEditorGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView22updateEditorGeometriesEv(
    QAbstractItemView *self) {
  self->updateEditorGeometries();
}

//  void QAbstractItemView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16updateGeometriesEv(
    QAbstractItemView *self) {
  self->updateGeometries();
}

//  void QAbstractItemView::verticalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView23verticalScrollbarActionEi(
    QAbstractItemView *self,
    int action) {
  self->verticalScrollbarAction(action);
}

//  void QAbstractItemView::horizontalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView25horizontalScrollbarActionEi(
    QAbstractItemView *self,
    int action) {
  self->horizontalScrollbarAction(action);
}

//  void QAbstractItemView::verticalScrollbarValueChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView29verticalScrollbarValueChangedEi(
    QAbstractItemView *self,
    int value) {
  self->verticalScrollbarValueChanged(value);
}

//  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi(
    QAbstractItemView *self,
    int value) {
  self->horizontalScrollbarValueChanged(value);
}

//  void QAbstractItemView::closeEditor(QWidget *editor,
//      QAbstractItemDelegate::EndEditHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE(
    QAbstractItemView *self,
    QWidget *editor,
    QAbstractItemDelegate::EndEditHint hint) {
  self->closeEditor(editor, hint);
}

//  void QAbstractItemView::commitData(QWidget *editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView10commitDataEP7QWidget(
    QAbstractItemView *self,
    QWidget *editor) {
  self->commitData(editor);
}

//  void QAbstractItemView::editorDestroyed(QObject *editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15editorDestroyedEP7QObject(
    QAbstractItemView *self,
    QObject *editor) {
  self->editorDestroyed(editor);
}

//  QModelIndex QAbstractItemView::moveCursor(CursorAction cursorAction,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN17QAbstractItemView10moveCursorENS_12CursorActionE6QFlagsIN2Qt16KeyboardModifierEE(
    QAbstractItemView *self,
    QAbstractItemView::CursorAction cursorAction,
    int modifiers) {
  return new QModelIndex(
      self->moveCursor(
          cursorAction,
          QFlags<Qt::KeyboardModifier>::fromInt(modifiers)));
}

//  int QAbstractItemView::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView16horizontalOffsetEv(
    const QAbstractItemView *self) {
  return self->horizontalOffset();
}

//  int QAbstractItemView::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView14verticalOffsetEv(
    const QAbstractItemView *self) {
  return self->verticalOffset();
}

//  bool QAbstractItemView::isIndexHidden(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->isIndexHidden(*index);
}

//  void QAbstractItemView::setSelection(const QRect &rect,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QAbstractItemView *self,
    const QRect *rect,
    int command) {
  self->setSelection(
      *rect,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QRegion QAbstractItemView::visualRegionForSelection(const QItemSelection
//      &selection) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSelection(
    const QAbstractItemView *self,
    const QItemSelection *selection) {
  return new QRegion(self->visualRegionForSelection(*selection));
}

//  QModelIndexList QAbstractItemView::selectedIndexes() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK17QAbstractItemView15selectedIndexesEv(
    const QAbstractItemView *self) {
  return new QList<QModelIndex>(self->selectedIndexes());
}

//  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
//      trigger, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent(
    QAbstractItemView *self,
    const QModelIndex *index,
    QAbstractItemView::EditTrigger trigger,
    QEvent *event) {
  return self->edit(*index, trigger, event);
}

//  QItemSelectionModel::SelectionFlags
//      QAbstractItemView::selectionCommand(const QModelIndex &index, const
//      QEvent *event) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent(
    const QAbstractItemView *self,
    const QModelIndex *index,
    const QEvent *event) {
  return static_cast<int>(self->selectionCommand(*index, event).toInt());
}

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::startDrag(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE(
    QAbstractItemView *self,
    int supportedActions) {
  self->startDrag(QFlags<Qt::DropAction>::fromInt(supportedActions));
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractItemView::initViewItemOption(QStyleOptionViewItem *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem(
    const QAbstractItemView *self,
    QStyleOptionViewItem *option) {
  self->initViewItemOption(option);
}

//  State QAbstractItemView::state() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::State ritual_ZNK17QAbstractItemView5stateEv(
    const QAbstractItemView *self) {
  return self->state();
}

//  void QAbstractItemView::setState(State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView8setStateENS_5StateE(
    QAbstractItemView *self,
    QAbstractItemView::State state) {
  self->setState(state);
}

//  void QAbstractItemView::scheduleDelayedItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView26scheduleDelayedItemsLayoutEv(
    QAbstractItemView *self) {
  self->scheduleDelayedItemsLayout();
}

//  void QAbstractItemView::executeDelayedItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView25executeDelayedItemsLayoutEv(
    QAbstractItemView *self) {
  self->executeDelayedItemsLayout();
}

//  void QAbstractItemView::setDirtyRegion(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14setDirtyRegionERK7QRegion(
    QAbstractItemView *self,
    const QRegion *region) {
  self->setDirtyRegion(*region);
}

//  void QAbstractItemView::scrollDirtyRegion(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView17scrollDirtyRegionEii(
    QAbstractItemView *self,
    int dx,
    int dy) {
  self->scrollDirtyRegion(dx, dy);
}

//  QPoint QAbstractItemView::dirtyRegionOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QAbstractItemView17dirtyRegionOffsetEv(
    const QAbstractItemView *self) {
  return new QPoint(self->dirtyRegionOffset());
}

//  void QAbstractItemView::startAutoScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15startAutoScrollEv(
    QAbstractItemView *self) {
  self->startAutoScroll();
}

//  void QAbstractItemView::stopAutoScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14stopAutoScrollEv(
    QAbstractItemView *self) {
  self->stopAutoScroll();
}

//  void QAbstractItemView::doAutoScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView12doAutoScrollEv(QAbstractItemView *self) {
  self->doAutoScroll();
}

//  bool QAbstractItemView::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAbstractItemView18focusNextPrevChildEb(
    QAbstractItemView *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  bool QAbstractItemView::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAbstractItemView5eventEP6QEvent(
    QAbstractItemView *self,
    QEvent *event) {
  return self->event(event);
}

//  bool QAbstractItemView::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAbstractItemView13viewportEventEP6QEvent(
    QAbstractItemView *self,
    QEvent *event) {
  return self->viewportEvent(event);
}

//  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView15mousePressEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14mouseMoveEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView17mouseReleaseEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView21mouseDoubleClickEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14dragEnterEventEP15QDragEnterEvent(
    QAbstractItemView *self,
    QDragEnterEvent *event) {
  self->dragEnterEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13dragMoveEventEP14QDragMoveEvent(
    QAbstractItemView *self,
    QDragMoveEvent *event) {
  self->dragMoveEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView14dragLeaveEventEP15QDragLeaveEvent(
    QAbstractItemView *self,
    QDragLeaveEvent *event) {
  self->dragLeaveEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView9dropEventEP10QDropEvent(
    QAbstractItemView *self,
    QDropEvent *event) {
  self->dropEvent(event);
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractItemView::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView12focusInEventEP11QFocusEvent(
    QAbstractItemView *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13focusOutEventEP11QFocusEvent(
    QAbstractItemView *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView13keyPressEventEP9QKeyEvent(
    QAbstractItemView *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QAbstractItemView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView11resizeEventEP12QResizeEvent(
    QAbstractItemView *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QAbstractItemView::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView10timerEventEP11QTimerEvent(
    QAbstractItemView *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstractItemView16inputMethodEventEP17QInputMethodEvent(
    QAbstractItemView *self,
    QInputMethodEvent *event) {
  self->inputMethodEvent(event);
}

//  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAbstractItemView11eventFilterEP7QObjectP6QEvent(
    QAbstractItemView *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

#if QT_CONFIG(draganddrop)
//  DropIndicatorPosition QAbstractItemView::dropIndicatorPosition() const
extern "C" Q_DECL_EXPORT
QAbstractItemView::DropIndicatorPosition ritual_ZNK17QAbstractItemView21dropIndicatorPositionEv(
    const QAbstractItemView *self) {
  return self->dropIndicatorPosition();
}
#endif  // QT_CONFIG(draganddrop)

//  QSize QAbstractItemView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QAbstractItemView16viewportSizeHintEv(
    const QAbstractItemView *self) {
  return new QSize(self->viewportSizeHint());
}

//  QAbstractItemViewPrivate *QAbstractItemView::d_func()
extern "C" Q_DECL_EXPORT
QAbstractItemViewPrivate *ritual_ZN17QAbstractItemView6d_funcEv(
    QAbstractItemView *self) {
  return self->d_func();
}

//  const QAbstractItemViewPrivate *QAbstractItemView::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemViewPrivate *ritual_ZNK17QAbstractItemView6d_funcEv(
    const QAbstractItemView *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractItemView, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemView(
    QAbstractItemView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemView *>(self)->take(key, call);
}

//  void QAbstractItemView::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView8setModelEP18QAbstractItemModel(
    QAbstractItemView *self,
    QAbstractItemModel *model) {
  self->QAbstractItemView::setModel(model);
}

//  void QAbstractItemView::setSelectionModel(QItemSelectionModel
//      *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionModel(
    QAbstractItemView *self,
    QItemSelectionModel *selectionModel) {
  self->QAbstractItemView::setSelectionModel(selectionModel);
}

//  void QAbstractItemView::keyboardSearch(const QString &search)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView14keyboardSearchERK7QString(
    QAbstractItemView *self,
    const QString *search) {
  self->QAbstractItemView::keyboardSearch(*search);
}

//  int QAbstractItemView::sizeHintForRow(int row) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAbstractItemView14sizeHintForRowEi(
    const QAbstractItemView *self,
    int row) {
  return self->QAbstractItemView::sizeHintForRow(row);
}

//  int QAbstractItemView::sizeHintForColumn(int column) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAbstractItemView17sizeHintForColumnEi(
    const QAbstractItemView *self,
    int column) {
  return self->QAbstractItemView::sizeHintForColumn(column);
}

//  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_own_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex(
    const QAbstractItemView *self,
    const QModelIndex *index) {
  return self->QAbstractItemView::itemDelegateForIndex(*index);
}

//  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QAbstractItemView16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QAbstractItemView *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QAbstractItemView::inputMethodQuery(query));
}

//  void QAbstractItemView::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView5resetEv(QAbstractItemView *self) {
  self->QAbstractItemView::reset();
}

//  void QAbstractItemView::setRootIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView12setRootIndexERK11QModelIndex(
    QAbstractItemView *self,
    const QModelIndex *index) {
  self->QAbstractItemView::setRootIndex(*index);
}

//  void QAbstractItemView::doItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView13doItemsLayoutEv(
    QAbstractItemView *self) {
  self->QAbstractItemView::doItemsLayout();
}

//  void QAbstractItemView::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView9selectAllEv(QAbstractItemView *self) {
  self->QAbstractItemView::selectAll();
}

//  void QAbstractItemView::rowsInserted(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii(
    QAbstractItemView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::rowsInserted(
      *parent,
      start,
      end);
}

//  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii(
    QAbstractItemView *self,
    const QModelIndex *parent,
    int start,
    int end) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::rowsAboutToBeRemoved(
      *parent,
      start,
      end);
}

//  void QAbstractItemView::selectionChanged(const QItemSelection &selected,
//      const QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_(
    QAbstractItemView *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::selectionChanged(
      *selected,
      *deselected);
}

//  void QAbstractItemView::currentChanged(const QModelIndex &current, const
//      QModelIndex &previous)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_(
    QAbstractItemView *self,
    const QModelIndex *current,
    const QModelIndex *previous) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::currentChanged(
      *current,
      *previous);
}

//  void QAbstractItemView::updateEditorData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView16updateEditorDataEv(
    QAbstractItemView *self) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::updateEditorData();
}

//  void QAbstractItemView::updateEditorGeometries()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView22updateEditorGeometriesEv(
    QAbstractItemView *self) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::updateEditorGeometries();
}

//  void QAbstractItemView::updateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView16updateGeometriesEv(
    QAbstractItemView *self) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::updateGeometries();
}

//  void QAbstractItemView::verticalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView23verticalScrollbarActionEi(
    QAbstractItemView *self,
    int action) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::verticalScrollbarAction(
      action);
}

//  void QAbstractItemView::horizontalScrollbarAction(int action)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView25horizontalScrollbarActionEi(
    QAbstractItemView *self,
    int action) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::horizontalScrollbarAction(
      action);
}

//  void QAbstractItemView::verticalScrollbarValueChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView29verticalScrollbarValueChangedEi(
    QAbstractItemView *self,
    int value) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::verticalScrollbarValueChanged(
      value);
}

//  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi(
    QAbstractItemView *self,
    int value) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::horizontalScrollbarValueChanged(
      value);
}

//  void QAbstractItemView::closeEditor(QWidget *editor,
//      QAbstractItemDelegate::EndEditHint hint)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDelegate11EndEditHintE(
    QAbstractItemView *self,
    QWidget *editor,
    QAbstractItemDelegate::EndEditHint hint) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::closeEditor(
      editor,
      hint);
}

//  void QAbstractItemView::commitData(QWidget *editor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView10commitDataEP7QWidget(
    QAbstractItemView *self,
    QWidget *editor) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::commitData(
      editor);
}

//  void QAbstractItemView::editorDestroyed(QObject *editor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView15editorDestroyedEP7QObject(
    QAbstractItemView *self,
    QObject *editor) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::editorDestroyed(
      editor);
}

//  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
//      trigger, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6QEvent(
    QAbstractItemView *self,
    const QModelIndex *index,
    QAbstractItemView::EditTrigger trigger,
    QEvent *event) {
  return static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::edit(
      *index,
      trigger,
      event);
}

//  QItemSelectionModel::SelectionFlags
//      QAbstractItemView::selectionCommand(const QModelIndex &index, const
//      QEvent *event) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEvent(
    const QAbstractItemView *self,
    const QModelIndex *index,
    const QEvent *event) {
  return static_cast<int>(
      static_cast<const OwnQAbstractItemView *>(self)->OwnQAbstractItemView::selectionCommand(
          *index,
          event).toInt());
}

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::startDrag(Qt::DropActions supportedActions)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE(
    QAbstractItemView *self,
    int supportedActions) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::startDrag(
      QFlags<Qt::DropAction>::fromInt(supportedActions));
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractItemView::initViewItemOption(QStyleOptionViewItem *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem(
    const QAbstractItemView *self,
    QStyleOptionViewItem *option) {
  static_cast<const OwnQAbstractItemView *>(self)->OwnQAbstractItemView::initViewItemOption(
      option);
}

//  bool QAbstractItemView::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAbstractItemView18focusNextPrevChildEb(
    QAbstractItemView *self,
    bool next) {
  return static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::focusNextPrevChild(
      next);
}

//  bool QAbstractItemView::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAbstractItemView5eventEP6QEvent(
    QAbstractItemView *self,
    QEvent *event) {
  return static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::event(
      event);
}

//  bool QAbstractItemView::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAbstractItemView13viewportEventEP6QEvent(
    QAbstractItemView *self,
    QEvent *event) {
  return static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::viewportEvent(
      event);
}

//  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView15mousePressEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::mousePressEvent(
      event);
}

//  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView14mouseMoveEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::mouseMoveEvent(
      event);
}

//  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView17mouseReleaseEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::mouseReleaseEvent(
      event);
}

//  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView21mouseDoubleClickEventEP11QMouseEvent(
    QAbstractItemView *self,
    QMouseEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::mouseDoubleClickEvent(
      event);
}

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView14dragEnterEventEP15QDragEnterEvent(
    QAbstractItemView *self,
    QDragEnterEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::dragEnterEvent(
      event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dragMoveEvent(QDragMoveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView13dragMoveEventEP14QDragMoveEvent(
    QAbstractItemView *self,
    QDragMoveEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::dragMoveEvent(
      event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView14dragLeaveEventEP15QDragLeaveEvent(
    QAbstractItemView *self,
    QDragLeaveEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::dragLeaveEvent(
      event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemView::dropEvent(QDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView9dropEventEP10QDropEvent(
    QAbstractItemView *self,
    QDropEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::dropEvent(
      event);
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractItemView::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView12focusInEventEP11QFocusEvent(
    QAbstractItemView *self,
    QFocusEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::focusInEvent(
      event);
}

//  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView13focusOutEventEP11QFocusEvent(
    QAbstractItemView *self,
    QFocusEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::focusOutEvent(
      event);
}

//  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView13keyPressEventEP9QKeyEvent(
    QAbstractItemView *self,
    QKeyEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::keyPressEvent(
      event);
}

//  void QAbstractItemView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView11resizeEventEP12QResizeEvent(
    QAbstractItemView *self,
    QResizeEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::resizeEvent(
      event);
}

//  void QAbstractItemView::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView10timerEventEP11QTimerEvent(
    QAbstractItemView *self,
    QTimerEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::timerEvent(
      event);
}

//  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QAbstractItemView16inputMethodEventEP17QInputMethodEvent(
    QAbstractItemView *self,
    QInputMethodEvent *event) {
  static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::inputMethodEvent(
      event);
}

//  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAbstractItemView11eventFilterEP7QObjectP6QEvent(
    QAbstractItemView *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQAbstractItemView *>(self)->OwnQAbstractItemView::eventFilter(
      object,
      event);
}

//  QSize QAbstractItemView::viewportSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QAbstractItemView16viewportSizeHintEv(
    const QAbstractItemView *self) {
  return new QSize(
      static_cast<const OwnQAbstractItemView *>(self)->OwnQAbstractItemView::viewportSizeHint());
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
