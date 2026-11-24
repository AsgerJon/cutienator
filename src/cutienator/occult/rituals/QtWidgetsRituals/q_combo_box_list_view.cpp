//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(combobox)
#if QT_CONFIG(combobox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtGui/qregion.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qcombobox_p.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qlistview.h>
#if QT_CONFIG(tableview)
#include <QtWidgets/qtableview.h>
#endif
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qmap.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(treeview)
#include <QtWidgets/qtreeview.h>
#endif
#include <QtWidgets/qheaderview.h>
#include <QtCore/qmath.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(proxymodel)
#include <QtCore/qabstractproxymodel.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qlineedit_p.h>
#if QT_CONFIG(completer)
#include <QtWidgets/private/qcompleter_p.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(effects)
# include <QtWidgets/private/qeffects_p.h>
#endif
#include <QtWidgets/private/qstyle_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtGui/qpainter.h>
#include <QtCore/qpointer.h>
#include <array>
#include <chrono>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qcombobox.cpp, line 83, as _ZN17QComboBoxListView11resizeEventEP12QResizeEvent
inline void QComboBoxListView::resizeEvent(QResizeEvent *event)
{
    resizeContents(viewport()->width(), contentsSize().height());
    QListView::resizeEvent(event);
}

//  from src/widgets/widgets/qcombobox.cpp, line 89, as _ZNK17QComboBoxListView18initViewItemOptionEP20QStyleOptionViewItem
inline void QComboBoxListView::initViewItemOption(QStyleOptionViewItem *option) const
{
    QListView::initViewItemOption(option);
    option->showDecorationSelected = true;
    if (combo)
        option->font = combo->font();
}

//  from src/widgets/widgets/qcombobox.cpp, line 97, as _ZN17QComboBoxListView10paintEventEP11QPaintEvent
inline void QComboBoxListView::paintEvent(QPaintEvent *e)
{
    if (combo) {
        QStyleOptionComboBox opt;
        opt.initFrom(combo);
        opt.editable = combo->isEditable();
        if (combo->style()->styleHint(QStyle::SH_ComboBox_Popup, &opt, combo)) {
            //we paint the empty menu area to avoid having blank space that can happen when scrolling
            QStyleOptionMenuItem menuOpt;
            menuOpt.initFrom(this);
            menuOpt.palette = palette();
            menuOpt.state = QStyle::State_None;
            menuOpt.checkType = QStyleOptionMenuItem::NotCheckable;
            menuOpt.menuRect = e->rect();
            menuOpt.maxIconWidth = 0;
            menuOpt.reservedShortcutWidth = 0;
            QPainter p(viewport());
            combo->style()->drawControl(QStyle::CE_MenuEmptyArea, &menuOpt, &p, this);
        }
    }
    QListView::paintEvent(e);
}
//  -----------------------------------------------------------------------

//  Only a class built on QComboBoxListView may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQComboBoxListView : QComboBoxListView {
  using QComboBoxListView::resizeEvent;
  using QComboBoxListView::initViewItemOption;
  using QComboBoxListView::paintEvent;
};

//  A QComboBoxListView that Python can take functions over in. Every QComboBoxListView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxListViewCall0)(const void *, QResizeEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxListViewCall1)(const void *, QStyleOptionViewItem *, int *);
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
typedef void (*CuteQComboBoxListViewCall2)(const void *, QPaintEvent *, int *);
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRect * (*CuteQComboBoxListViewCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall4)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QModelIndex * (*CuteQComboBoxListViewCall5)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall6)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall7)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef bool (*CuteQComboBoxListViewCall9)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall10)(const void *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall11)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall12)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall13)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall14)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall15)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall16)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall17)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall18)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall19)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall20)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQComboBoxListViewCall21)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef int (*CuteQComboBoxListViewCall22)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall23)(const void *, const QRect *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef const QRegion * (*CuteQComboBoxListViewCall24)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall25)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef bool (*CuteQComboBoxListViewCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall27)(const void *, const QItemSelection *, const QItemSelection *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQComboBoxListViewCall28)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
typedef const QSize * (*CuteQComboBoxListViewCall29)(const void *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall30)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall31)(const void *, QItemSelectionModel *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall32)(const void *, const QString *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQComboBoxListViewCall33)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQComboBoxListViewCall34)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void * (*CuteQComboBoxListViewCall35)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QVariant * (*CuteQComboBoxListViewCall36)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall37)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall38)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall39)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall40)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall41)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall42)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall43)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall44)(const void *, QWidget *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall45)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall46)(const void *, QObject *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxListViewCall47)(const void *, const QModelIndex *, int, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef int (*CuteQComboBoxListViewCall48)(const void *, const QModelIndex *, const QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxListViewCall49)(const void *, bool, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxListViewCall50)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall51)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall52)(const void *, QMouseEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall53)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall54)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall55)(const void *, QFocusEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall56)(const void *, QKeyEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQComboBoxListViewCall57)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQComboBoxListViewCall58)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQComboBoxListViewCall59)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QSize * (*CuteQComboBoxListViewCall60)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQComboBoxListViewCall61)(const void *, QWidget *, int *);
#endif  // QT_CONFIG(scrollarea)
#if !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQComboBoxListViewCall62)(const void *, QContextMenuEvent *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQComboBoxListViewCall63)(const void *, QEvent *, int *);
typedef void (*CuteQComboBoxListViewCall64)(const void *, QStyleOptionFrame *, int *);
typedef int (*CuteQComboBoxListViewCall65)(const void *, int *);
typedef void (*CuteQComboBoxListViewCall66)(const void *, bool, int *);
typedef int (*CuteQComboBoxListViewCall67)(const void *, int, int *);
typedef bool (*CuteQComboBoxListViewCall68)(const void *, int *);
typedef void * (*CuteQComboBoxListViewCall69)(const void *, int *);
typedef void (*CuteQComboBoxListViewCall70)(const void *, QKeyEvent *, int *);
typedef void (*CuteQComboBoxListViewCall71)(const void *, QEnterEvent *, int *);
typedef void (*CuteQComboBoxListViewCall72)(const void *, QEvent *, int *);
typedef void (*CuteQComboBoxListViewCall73)(const void *, QMoveEvent *, int *);
typedef void (*CuteQComboBoxListViewCall74)(const void *, QCloseEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQComboBoxListViewCall75)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteQComboBoxListViewCall76)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
typedef void (*CuteQComboBoxListViewCall77)(const void *, QShowEvent *, int *);
typedef void (*CuteQComboBoxListViewCall78)(const void *, QHideEvent *, int *);
typedef int (*CuteQComboBoxListViewCall79)(const void *, int, int *);
typedef void (*CuteQComboBoxListViewCall80)(const void *, QPainter *, int *);
typedef void * (*CuteQComboBoxListViewCall81)(const void *, QPoint *, int *);
typedef void * (*CuteQComboBoxListViewCall82)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxListViewCall83)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxListViewCall84)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxListViewCall85)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQComboBoxListViewCall86)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQComboBoxListView : public QComboBoxListView {
public:
  using QComboBoxListView::QComboBoxListView;
  void *taken[87] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionViewItem")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(combobox)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView10visualRectERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK17QAbstractItemView7indexAtERK6QPoint")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView13doItemsLayoutEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView5resetEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12setRootIndexERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QAbstractScrollArea16scrollContentsByEii")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(wheelevent)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(wheelevent)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(itemviews)
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

#if QT_CONFIG(combobox)
  //  void QComboBoxListView::resizeEvent(QResizeEvent *event)
  void resizeEvent(QResizeEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQComboBoxListViewCall0 call = reinterpret_cast<CuteQComboBoxListViewCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QComboBoxListView::resizeEvent(event);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(combobox)
  //  void QComboBoxListView::initViewItemOption(QStyleOptionViewItem
  //      *option) const
  void initViewItemOption(QStyleOptionViewItem *option) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQComboBoxListViewCall1 call = reinterpret_cast<CuteQComboBoxListViewCall1>(taken[1]);
      call(this, option, &handled);
      if (handled) return;
    }
    QComboBoxListView::initViewItemOption(option);
  }
#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(combobox)
  //  void QComboBoxListView::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQComboBoxListViewCall2 call = reinterpret_cast<CuteQComboBoxListViewCall2>(taken[2]);
      call(this, e, &handled);
      if (handled) return;
    }
    QComboBoxListView::paintEvent(e);
  }
#endif  // QT_CONFIG(combobox)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  QRect QListView::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQComboBoxListViewCall3 call = reinterpret_cast<CuteQComboBoxListViewCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQComboBoxListViewCall4 call = reinterpret_cast<CuteQComboBoxListViewCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQComboBoxListViewCall5 call = reinterpret_cast<CuteQComboBoxListViewCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQComboBoxListViewCall6 call = reinterpret_cast<CuteQComboBoxListViewCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQComboBoxListViewCall7 call = reinterpret_cast<CuteQComboBoxListViewCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQComboBoxListViewCall8 call = reinterpret_cast<CuteQComboBoxListViewCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQComboBoxListViewCall9 call = reinterpret_cast<CuteQComboBoxListViewCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQComboBoxListViewCall10 call = reinterpret_cast<CuteQComboBoxListViewCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQComboBoxListViewCall11 call = reinterpret_cast<CuteQComboBoxListViewCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQComboBoxListViewCall12 call = reinterpret_cast<CuteQComboBoxListViewCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQComboBoxListViewCall13 call = reinterpret_cast<CuteQComboBoxListViewCall13>(taken[13]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::mouseMoveEvent(e);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QListView::mouseReleaseEvent(QMouseEvent *e)
  void mouseReleaseEvent(QMouseEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQComboBoxListViewCall14 call = reinterpret_cast<CuteQComboBoxListViewCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQComboBoxListViewCall15 call = reinterpret_cast<CuteQComboBoxListViewCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQComboBoxListViewCall16 call = reinterpret_cast<CuteQComboBoxListViewCall16>(taken[16]);
      call(this, e, &handled);
      if (handled) return;
    }
    QListView::timerEvent(e);
  }
#endif  // QT_CONFIG(listview)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(draganddrop)
#if QT_CONFIG(listview)
  //  void QListView::dragMoveEvent(QDragMoveEvent *e)
  void dragMoveEvent(QDragMoveEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQComboBoxListViewCall17 call = reinterpret_cast<CuteQComboBoxListViewCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQComboBoxListViewCall18 call = reinterpret_cast<CuteQComboBoxListViewCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQComboBoxListViewCall19 call = reinterpret_cast<CuteQComboBoxListViewCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQComboBoxListViewCall20 call = reinterpret_cast<CuteQComboBoxListViewCall20>(taken[20]);
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
  //  int QListView::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQComboBoxListViewCall21 call = reinterpret_cast<CuteQComboBoxListViewCall21>(taken[21]);
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
      CuteQComboBoxListViewCall22 call = reinterpret_cast<CuteQComboBoxListViewCall22>(taken[22]);
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
      CuteQComboBoxListViewCall23 call = reinterpret_cast<CuteQComboBoxListViewCall23>(taken[23]);
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
      CuteQComboBoxListViewCall24 call = reinterpret_cast<CuteQComboBoxListViewCall24>(taken[24]);
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
      CuteQComboBoxListViewCall25 call = reinterpret_cast<CuteQComboBoxListViewCall25>(taken[25]);
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
      CuteQComboBoxListViewCall26 call = reinterpret_cast<CuteQComboBoxListViewCall26>(taken[26]);
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
      CuteQComboBoxListViewCall27 call = reinterpret_cast<CuteQComboBoxListViewCall27>(taken[27]);
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
      CuteQComboBoxListViewCall28 call = reinterpret_cast<CuteQComboBoxListViewCall28>(taken[28]);
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
      CuteQComboBoxListViewCall29 call = reinterpret_cast<CuteQComboBoxListViewCall29>(taken[29]);
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
      CuteQComboBoxListViewCall30 call = reinterpret_cast<CuteQComboBoxListViewCall30>(taken[30]);
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
      CuteQComboBoxListViewCall31 call = reinterpret_cast<CuteQComboBoxListViewCall31>(taken[31]);
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
      CuteQComboBoxListViewCall32 call = reinterpret_cast<CuteQComboBoxListViewCall32>(taken[32]);
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
      CuteQComboBoxListViewCall33 call = reinterpret_cast<CuteQComboBoxListViewCall33>(taken[33]);
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
      CuteQComboBoxListViewCall34 call = reinterpret_cast<CuteQComboBoxListViewCall34>(taken[34]);
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
      CuteQComboBoxListViewCall35 call = reinterpret_cast<CuteQComboBoxListViewCall35>(taken[35]);
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
      CuteQComboBoxListViewCall36 call = reinterpret_cast<CuteQComboBoxListViewCall36>(taken[36]);
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
      CuteQComboBoxListViewCall37 call = reinterpret_cast<CuteQComboBoxListViewCall37>(taken[37]);
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
      CuteQComboBoxListViewCall38 call = reinterpret_cast<CuteQComboBoxListViewCall38>(taken[38]);
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
      CuteQComboBoxListViewCall39 call = reinterpret_cast<CuteQComboBoxListViewCall39>(taken[39]);
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
      CuteQComboBoxListViewCall40 call = reinterpret_cast<CuteQComboBoxListViewCall40>(taken[40]);
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
      CuteQComboBoxListViewCall41 call = reinterpret_cast<CuteQComboBoxListViewCall41>(taken[41]);
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
      CuteQComboBoxListViewCall42 call = reinterpret_cast<CuteQComboBoxListViewCall42>(taken[42]);
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
      CuteQComboBoxListViewCall43 call = reinterpret_cast<CuteQComboBoxListViewCall43>(taken[43]);
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
      CuteQComboBoxListViewCall44 call = reinterpret_cast<CuteQComboBoxListViewCall44>(taken[44]);
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
      CuteQComboBoxListViewCall45 call = reinterpret_cast<CuteQComboBoxListViewCall45>(taken[45]);
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
      CuteQComboBoxListViewCall46 call = reinterpret_cast<CuteQComboBoxListViewCall46>(taken[46]);
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
      CuteQComboBoxListViewCall47 call = reinterpret_cast<CuteQComboBoxListViewCall47>(taken[47]);
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
      CuteQComboBoxListViewCall48 call = reinterpret_cast<CuteQComboBoxListViewCall48>(taken[48]);
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
      CuteQComboBoxListViewCall49 call = reinterpret_cast<CuteQComboBoxListViewCall49>(taken[49]);
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
      CuteQComboBoxListViewCall50 call = reinterpret_cast<CuteQComboBoxListViewCall50>(taken[50]);
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
      CuteQComboBoxListViewCall51 call = reinterpret_cast<CuteQComboBoxListViewCall51>(taken[51]);
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
      CuteQComboBoxListViewCall52 call = reinterpret_cast<CuteQComboBoxListViewCall52>(taken[52]);
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
      CuteQComboBoxListViewCall53 call = reinterpret_cast<CuteQComboBoxListViewCall53>(taken[53]);
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
      CuteQComboBoxListViewCall54 call = reinterpret_cast<CuteQComboBoxListViewCall54>(taken[54]);
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
      CuteQComboBoxListViewCall55 call = reinterpret_cast<CuteQComboBoxListViewCall55>(taken[55]);
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
      CuteQComboBoxListViewCall56 call = reinterpret_cast<CuteQComboBoxListViewCall56>(taken[56]);
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
      CuteQComboBoxListViewCall57 call = reinterpret_cast<CuteQComboBoxListViewCall57>(taken[57]);
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
      CuteQComboBoxListViewCall58 call = reinterpret_cast<CuteQComboBoxListViewCall58>(taken[58]);
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
      CuteQComboBoxListViewCall59 call = reinterpret_cast<CuteQComboBoxListViewCall59>(taken[59]);
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
      CuteQComboBoxListViewCall60 call = reinterpret_cast<CuteQComboBoxListViewCall60>(taken[60]);
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
      CuteQComboBoxListViewCall61 call = reinterpret_cast<CuteQComboBoxListViewCall61>(taken[61]);
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
      CuteQComboBoxListViewCall62 call = reinterpret_cast<CuteQComboBoxListViewCall62>(taken[62]);
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
      CuteQComboBoxListViewCall63 call = reinterpret_cast<CuteQComboBoxListViewCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFrame::changeEvent(a0);
  }

  //  void QFrame::initStyleOption(QStyleOptionFrame *option) const
  void initStyleOption(QStyleOptionFrame *option) const override {
    if (taken[64]) {
      int handled = 0;
      CuteQComboBoxListViewCall64 call = reinterpret_cast<CuteQComboBoxListViewCall64>(taken[64]);
      call(this, option, &handled);
      if (handled) return;
    }
    QFrame::initStyleOption(option);
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[65]) {
      int handled = 0;
      CuteQComboBoxListViewCall65 call = reinterpret_cast<CuteQComboBoxListViewCall65>(taken[65]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[66]) {
      int handled = 0;
      CuteQComboBoxListViewCall66 call = reinterpret_cast<CuteQComboBoxListViewCall66>(taken[66]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[67]) {
      int handled = 0;
      CuteQComboBoxListViewCall67 call = reinterpret_cast<CuteQComboBoxListViewCall67>(taken[67]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[68]) {
      int handled = 0;
      CuteQComboBoxListViewCall68 call = reinterpret_cast<CuteQComboBoxListViewCall68>(taken[68]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

  //  QPaintEngine *QWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[69]) {
      int handled = 0;
      CuteQComboBoxListViewCall69 call = reinterpret_cast<CuteQComboBoxListViewCall69>(taken[69]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QWidget::paintEngine();
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[70]) {
      int handled = 0;
      CuteQComboBoxListViewCall70 call = reinterpret_cast<CuteQComboBoxListViewCall70>(taken[70]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[71]) {
      int handled = 0;
      CuteQComboBoxListViewCall71 call = reinterpret_cast<CuteQComboBoxListViewCall71>(taken[71]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[72]) {
      int handled = 0;
      CuteQComboBoxListViewCall72 call = reinterpret_cast<CuteQComboBoxListViewCall72>(taken[72]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[73]) {
      int handled = 0;
      CuteQComboBoxListViewCall73 call = reinterpret_cast<CuteQComboBoxListViewCall73>(taken[73]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[74]) {
      int handled = 0;
      CuteQComboBoxListViewCall74 call = reinterpret_cast<CuteQComboBoxListViewCall74>(taken[74]);
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
      CuteQComboBoxListViewCall75 call = reinterpret_cast<CuteQComboBoxListViewCall75>(taken[75]);
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
      CuteQComboBoxListViewCall76 call = reinterpret_cast<CuteQComboBoxListViewCall76>(taken[76]);
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
      CuteQComboBoxListViewCall77 call = reinterpret_cast<CuteQComboBoxListViewCall77>(taken[77]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[78]) {
      int handled = 0;
      CuteQComboBoxListViewCall78 call = reinterpret_cast<CuteQComboBoxListViewCall78>(taken[78]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  int QWidget::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[79]) {
      int handled = 0;
      CuteQComboBoxListViewCall79 call = reinterpret_cast<CuteQComboBoxListViewCall79>(taken[79]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QWidget::metric(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[80]) {
      int handled = 0;
      CuteQComboBoxListViewCall80 call = reinterpret_cast<CuteQComboBoxListViewCall80>(taken[80]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPaintDevice *QWidget::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[81]) {
      int handled = 0;
      CuteQComboBoxListViewCall81 call = reinterpret_cast<CuteQComboBoxListViewCall81>(taken[81]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QWidget::redirected(offset);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[82]) {
      int handled = 0;
      CuteQComboBoxListViewCall82 call = reinterpret_cast<CuteQComboBoxListViewCall82>(taken[82]);
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
      CuteQComboBoxListViewCall83 call = reinterpret_cast<CuteQComboBoxListViewCall83>(taken[83]);
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
      CuteQComboBoxListViewCall84 call = reinterpret_cast<CuteQComboBoxListViewCall84>(taken[84]);
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
      CuteQComboBoxListViewCall85 call = reinterpret_cast<CuteQComboBoxListViewCall85>(taken[85]);
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
      CuteQComboBoxListViewCall86 call = reinterpret_cast<CuteQComboBoxListViewCall86>(taken[86]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QComboBoxListView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QComboBoxListView10metaObjectEv(
    const QComboBoxListView *self) {
  return self->metaObject();
}

//  void QComboBoxListView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QComboBoxListView11resizeEventEP12QResizeEvent(
    QComboBoxListView *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QComboBoxListView::initViewItemOption(QStyleOptionViewItem *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QComboBoxListView18initViewItemOptionEP20QStyleOptionViewItem(
    const QComboBoxListView *self,
    QStyleOptionViewItem *option) {
  self->initViewItemOption(option);
}

//  void QComboBoxListView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QComboBoxListView10paintEventEP11QPaintEvent(
    QComboBoxListView *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  a Python function taken by a CuteQComboBoxListView, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QComboBoxListView(
    QComboBoxListView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQComboBoxListView *>(self)->take(key, call);
}

//  void QComboBoxListView::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QComboBoxListView11resizeEventEP12QResizeEvent(
    QComboBoxListView *self,
    QResizeEvent *event) {
  static_cast<OwnQComboBoxListView *>(self)->OwnQComboBoxListView::resizeEvent(
      event);
}

//  void QComboBoxListView::initViewItemOption(QStyleOptionViewItem *option)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QComboBoxListView18initViewItemOptionEP20QStyleOptionViewItem(
    const QComboBoxListView *self,
    QStyleOptionViewItem *option) {
  static_cast<const OwnQComboBoxListView *>(self)->OwnQComboBoxListView::initViewItemOption(
      option);
}

//  void QComboBoxListView::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QComboBoxListView10paintEventEP11QPaintEvent(
    QComboBoxListView *self,
    QPaintEvent *e) {
  static_cast<OwnQComboBoxListView *>(self)->OwnQComboBoxListView::paintEvent(
      e);
}

#endif  // QT_CONFIG(combobox)
#endif  // QT_CONFIG(combobox)
