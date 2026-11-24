//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbarlayout_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbarlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qapplication.h>
#include <qaction.h>
#include <qwidgetaction.h>
#include <qtoolbar.h>
#include <qstyleoption.h>
#if QT_CONFIG(toolbutton)
#include <qtoolbutton.h>
#endif
#include <qmenu.h>
#include <qdebug.h>
#include <qmath.h>
#ifdef Q_OS_MACOS
#include <qpa/qplatformnativeinterface.h>
#endif
#include "qmainwindowlayout_p.h"
#if QT_CONFIG(toolbutton)
#include "qtoolbarextension_p.h"
#endif
#include "qtoolbarlayout_p.h"
#include "qtoolbarseparator_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 36, as _ZN12QToolBarItemC1EP7QWidget
inline QToolBarItem::QToolBarItem(QWidget *widget)
    : QWidgetItem(widget), action(nullptr), customWidget(false)
{
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 67, as _ZN14QToolBarLayoutD1Ev
inline QToolBarLayout::~QToolBarLayout()
{
    while (!items.isEmpty()) {
        QToolBarItem *item = items.takeFirst();
        if (QWidgetAction *widgetAction = qobject_cast<QWidgetAction*>(item->action)) {
            if (item->customWidget)
                widgetAction->releaseWidget(item->widget());
        }
        delete item;
    }
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 128, as _ZN14QToolBarLayout7addItemEP11QLayoutItem
inline void QToolBarLayout::addItem(QLayoutItem*)
{
    qWarning("QToolBarLayout::addItem(): please use addAction() instead");
    return;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 134, as _ZNK14QToolBarLayout6itemAtEi
inline QLayoutItem *QToolBarLayout::itemAt(int index) const
{
    if (index < 0 || index >= items.size())
        return nullptr;
    return items.at(index);
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 141, as _ZN14QToolBarLayout6takeAtEi
inline QLayoutItem *QToolBarLayout::takeAt(int index)
{
    if (index < 0 || index >= items.size())
        return nullptr;
    QToolBarItem *item = items.takeAt(index);

    if (popupMenu)
        popupMenu->removeAction(item->action);

    QWidgetAction *widgetAction = qobject_cast<QWidgetAction*>(item->action);
    if (widgetAction != nullptr && item->customWidget) {
        widgetAction->releaseWidget(item->widget());
    } else {
        // destroy the QToolButton/QToolBarSeparator
        item->widget()->hide();
        item->widget()->deleteLater();
    }

    invalidate();
    return item;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 184, as _ZNK14QToolBarLayout5countEv
inline int QToolBarLayout::count() const
{
    return items.size();
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 189, as _ZNK14QToolBarLayout7isEmptyEv
inline bool QToolBarLayout::isEmpty() const
{
    if (dirty)
        updateGeomArray();
    return empty;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 196, as _ZN14QToolBarLayout10invalidateEv
inline void QToolBarLayout::invalidate()
{
    dirty = true;
    QLayout::invalidate();
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 202, as _ZNK14QToolBarLayout19expandingDirectionsEv
inline Qt::Orientations QToolBarLayout::expandingDirections() const
{
    if (dirty)
        updateGeomArray();
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return {};
    Qt::Orientation o = tb->orientation();
    return expanding ? Qt::Orientations(o) : Qt::Orientations{};
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 340, as _ZN14QToolBarLayout11setGeometryERK5QRect
inline void QToolBarLayout::setGeometry(const QRect &rect)
{
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const QMargins margins = contentsMargins();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);
    Qt::Orientation o = tb->orientation();

    QLayout::setGeometry(rect);

    updateMacBorderMetrics();

    bool ranOutOfSpace = false;
    if (!animating)
        ranOutOfSpace = layoutActions(rect.size());

    if (expanded || animating || ranOutOfSpace) {
        Qt::ToolBarArea area = Qt::TopToolBarArea;
        if (QMainWindow *win = qobject_cast<QMainWindow*>(tb->parentWidget()))
            area = win->toolBarArea(tb);
        QSize hint = sizeHint();

        QPoint pos;
        rpick(o, pos) = pick(o, rect.bottomRight()) -
                pick(o, QSize(margins.bottom(), margins.right())) - extensionExtent + 2;
        if (area == Qt::LeftToolBarArea || area == Qt::TopToolBarArea)
            rperp(o, pos) = perp(o, rect.topLeft()) +
                    perp(o, QSize(margins.top(), margins.left()));
        else
            rperp(o, pos) = perp(o, rect.bottomRight()) -
                    perp(o, QSize(margins.bottom(), margins.right())) -
                    (perp(o, hint) - perp(o, margins)) + 1;
        QSize size;
        rpick(o, size) = extensionExtent;
        rperp(o, size) = perp(o, hint) - perp(o, margins);
        QRect r(pos, size);

        if (o == Qt::Horizontal)
            r = QStyle::visualRect(parentWidget()->layoutDirection(), rect, r);

        extension->setGeometry(r);

        if (extension->isHidden())
            extension->show();
    } else {
        if (!extension->isHidden())
            extension->hide();
    }
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 657, as _ZNK14QToolBarLayout11minimumSizeEv
inline QSize QToolBarLayout::minimumSize() const
{
    if (dirty)
        updateGeomArray();
    return minSize;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 664, as _ZNK14QToolBarLayout8sizeHintEv
inline QSize QToolBarLayout::sizeHint() const
{
    if (dirty)
        updateGeomArray();
    return hint;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 175, as _ZNK14QToolBarLayout7indexOfEPK7QAction
inline int QToolBarLayout::indexOf(const QAction *action) const
{
    for (int i = 0; i < items.size(); ++i) {
        if (items.at(i)->action == action)
            return i;
    }
    return -1;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 542, as _ZNK14QToolBarLayout12expandedSizeERK5QSize
inline QSize QToolBarLayout::expandedSize(const QSize &size) const
{
    if (dirty)
        updateGeomArray();

    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return QSize(0, 0);
    QMainWindow *win = qobject_cast<QMainWindow*>(tb->parentWidget());
    Qt::Orientation o = tb->orientation();
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int handleExtent = movable()
            ? style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb) : 0;
    const QMargins margins = contentsMargins();
    const int spacing = this->spacing();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);

    int total_w = 0;
    int count = 0;
    for (int x = 0; x < items.size(); ++x) {
        if (!geomArray[x].empty) {
            total_w += (count == 0 ? 0 : spacing) + geomArray[x].minimumSize;
            ++count;
        }
    }
    if (count == 0)
        return QSize(0, 0);

    int min_w = pick(o, size);
    int rows = (int)qSqrt(qreal(count));
    if (rows == 1)
        ++rows;      // we want to expand to at least two rows
    int space = total_w/rows + spacing + extensionExtent;
    space = qMax(space, min_w - pick(o, margins) - handleExtent);
    if (win != nullptr)
        space = qMin(space, pick(o, win->size()) - pick(o, margins) - handleExtent);

    int w = 0;
    int h = 0;
    int i = 0;
    while (i < items.size()) {
        int count = 0;
        int size = 0;
        int prev = -1;
        int rowHeight = 0;
        for (; i < items.size(); ++i) {
            if (geomArray[i].empty)
                continue;

            int newSize = size + (count == 0 ? 0 : spacing) + geomArray[i].minimumSize;
            rowHeight = qMax(rowHeight, perp(o, items.at(i)->sizeHint()));
            if (prev != -1 && newSize > space) {
                if (count > 1 && size + spacing + extensionExtent > space) {
                    size -= spacing + geomArray[prev].minimumSize;
                    i = prev;
                }
                break;
            }

            size = newSize;
            prev = i;
            ++count;
        }

        w = qMax(size, w);
        h += rowHeight + spacing;
    }

    w += pick(Qt::Horizontal, margins) + handleExtent + spacing + extensionExtent;
    w = qMax(w, min_w);
    if (win != nullptr)
        w = qMin(w, pick(o, win->size()));
    h += pick(Qt::Vertical, margins) - spacing; //there is no spacing before the first row

    QSize result;
    rpick(o, result) = w;
    rperp(o, result) = h;
    return result;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 98, as _ZN14QToolBarLayout15setUsePopupMenuEb
inline void QToolBarLayout::setUsePopupMenu(bool set)
{
    if (!dirty && ((popupMenu == nullptr) == set))
        invalidate();
    if (!set) {
        QObject::connect(extension, SIGNAL(clicked(bool)),
                        this, SLOT(setExpanded(bool)), Qt::UniqueConnection);
        extension->setPopupMode(QToolButton::DelayedPopup);
        extension->setMenu(nullptr);
        delete popupMenu;
        popupMenu = nullptr;
    } else {
        QObject::disconnect(extension, SIGNAL(clicked(bool)),
                            this, SLOT(setExpanded(bool)));
        extension->setPopupMode(QToolButton::InstantPopup);
        if (!popupMenu) {
            popupMenu = new QMenu(extension);
        }
        extension->setMenu(popupMenu);
    }
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 120, as _ZN14QToolBarLayout17checkUsePopupMenuEv
inline void QToolBarLayout::checkUsePopupMenu()
{
    QToolBar *tb = static_cast<QToolBar *>(parent());
    QMainWindow *mw = qobject_cast<QMainWindow *>(tb->parent());
    Qt::Orientation o = tb->orientation();
    setUsePopupMenu(!mw || tb->isFloating() || perp(o, expandedSize(mw->size())) >= perp(o, mw->size()));
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 213, as _ZNK14QToolBarLayout7movableEv
inline bool QToolBarLayout::movable() const
{
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return false;
    QMainWindow *win = qobject_cast<QMainWindow*>(tb->parentWidget());
    return tb->isMovable() && win != nullptr;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 79, as _ZN14QToolBarLayout22updateMarginAndSpacingEv
inline void QToolBarLayout::updateMarginAndSpacing()
{
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int margin = style->pixelMetric(QStyle::PM_ToolBarItemMargin, &opt, tb)
            + style->pixelMetric(QStyle::PM_ToolBarFrameWidth, &opt, tb);
    setContentsMargins(margin, margin, margin, margin);
    setSpacing(style->pixelMetric(QStyle::PM_ToolBarItemSpacing, &opt, tb));
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 93, as _ZNK14QToolBarLayout13hasExpandFlagEv
inline bool QToolBarLayout::hasExpandFlag() const
{
    return expandFlag;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 314, as _ZN14QToolBarLayout22updateMacBorderMetricsEv
inline void QToolBarLayout::updateMacBorderMetrics()
{
#ifdef Q_OS_MACOS
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return;

    QRect rect = geometry();

    QMainWindow *mainWindow = qobject_cast<QMainWindow*>(tb->parentWidget());
    if (!mainWindow || !mainWindow->isWindow() || !mainWindow->unifiedTitleAndToolBarOnMac())
        return;

    extern QMainWindowLayout *qt_mainwindow_layout(const QMainWindow *window);
    auto *mainWindowLayout = qt_mainwindow_layout(mainWindow);

    QPoint upper = tb->mapToParent(rect.topLeft());
    QPoint lower = tb->mapToParent(rect.bottomLeft() + QPoint(0, 1));

    if (mainWindow->toolBarArea(tb) == Qt::TopToolBarArea)
        mainWindowLayout->registerUnifiedToolBarArea(tb, upper.y(), lower.y());
    else
        mainWindowLayout->registerUnifiedToolBarArea(tb, 0, 0);
#endif
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 222, as _ZNK14QToolBarLayout15updateGeomArrayEv
inline void QToolBarLayout::updateGeomArray() const
{
    if (!dirty)
        return;

    QToolBarLayout *that = const_cast<QToolBarLayout*>(this);

    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int handleExtent = movable()
            ? style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb) : 0;
    const QMargins margins = contentsMargins();
    const int spacing = this->spacing();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);
    Qt::Orientation o = tb->orientation();

    that->minSize = QSize(0, 0);
    that->hint = QSize(0, 0);
    rperp(o, that->minSize) = style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb);
    rperp(o, that->hint) = style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb);

    that->expanding = false;
    that->empty = false;

    QList<QLayoutStruct> a(items.size() + 1); // + 1 for the stretch

    int count = 0;
    for (int i = 0; i < items.size(); ++i) {
        QToolBarItem *item = items.at(i);

        QSize max = item->maximumSize();
        QSize min = item->minimumSize();
        QSize hint = item->sizeHint();
        Qt::Orientations exp = item->expandingDirections();
        bool empty = item->isEmpty();

        that->expanding = expanding || exp & o;


        if (item->widget()) {
            if ((item->widget()->sizePolicy().horizontalPolicy() & QSizePolicy::ExpandFlag)) {
                that->expandFlag = true;
            }
        }

        if (!empty) {
            if (count == 0) // the minimum size only displays one widget
                rpick(o, that->minSize) += pick(o, min);
            int s = perp(o, minSize);
            rperp(o, that->minSize) = qMax(s, perp(o, min));

            //we only add spacing before item (ie never before the first one)
            rpick(o, that->hint) += (count == 0 ? 0 : spacing) + pick(o, hint);
            s = perp(o, that->hint);
            rperp(o, that->hint) = qMax(s, perp(o, hint));
            ++count;
        }

        a[i].sizeHint = pick(o, hint);
        a[i].maximumSize = pick(o, max);
        a[i].minimumSize = pick(o, min);
        a[i].expansive = exp & o;
        if (o == Qt::Horizontal)
            a[i].stretch = item->widget()->sizePolicy().horizontalStretch();
        else
            a[i].stretch = item->widget()->sizePolicy().verticalStretch();
        a[i].empty = empty;
    }

    that->geomArray = a;
    that->empty = count == 0;

    rpick(o, that->minSize) += handleExtent;
    that->minSize += QSize(pick(Qt::Horizontal, margins), pick(Qt::Vertical, margins));
    if (items.size() > 1)
        rpick(o, that->minSize) += spacing + extensionExtent;

    rpick(o, that->hint) += handleExtent;
    that->hint += QSize(pick(Qt::Horizontal, margins), pick(Qt::Vertical, margins));
    that->dirty = false;
}
//  -----------------------------------------------------------------------

//  A QToolBarLayout that Python can take functions over in. Every QToolBarLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarLayoutCall0)(const void *, QLayoutItem *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef void * (*CuteQToolBarLayoutCall1)(const void *, int, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef void * (*CuteQToolBarLayoutCall2)(const void *, int, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef int (*CuteQToolBarLayoutCall3)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef bool (*CuteQToolBarLayoutCall4)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarLayoutCall5)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef int (*CuteQToolBarLayoutCall6)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef void (*CuteQToolBarLayoutCall7)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef const QSize * (*CuteQToolBarLayoutCall8)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
typedef const QSize * (*CuteQToolBarLayoutCall9)(const void *, int *);
#endif  // QT_CONFIG(toolbar)
typedef int (*CuteQToolBarLayoutCall10)(const void *, int *);
typedef void (*CuteQToolBarLayoutCall11)(const void *, int, int *);
typedef const QRect * (*CuteQToolBarLayoutCall12)(const void *, int *);
typedef const QSize * (*CuteQToolBarLayoutCall13)(const void *, int *);
typedef int (*CuteQToolBarLayoutCall14)(const void *, const QWidget *, int *);
typedef int (*CuteQToolBarLayoutCall15)(const void *, const QLayoutItem *, int *);
typedef int (*CuteQToolBarLayoutCall16)(const void *, int *);
typedef void * (*CuteQToolBarLayoutCall17)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQToolBarLayoutCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarLayoutCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQToolBarLayoutCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQToolBarLayoutCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarLayoutCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarLayoutCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQToolBarLayoutCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQToolBarLayoutCall26)(const void *, int *);
typedef int (*CuteQToolBarLayoutCall27)(const void *, int, int *);
typedef int (*CuteQToolBarLayoutCall28)(const void *, int, int *);
typedef void * (*CuteQToolBarLayoutCall29)(const void *, int *);
typedef void * (*CuteQToolBarLayoutCall30)(const void *, int *);
class CuteQToolBarLayout : public QToolBarLayout {
public:
  using QToolBarLayout::QToolBarLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(toolbar)
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem11maximumSizeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK7QWidget")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QLayout7indexOfEPK11QLayoutItem")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK11QLayoutItem17hasHeightForWidthEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem14heightForWidthEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem21minimumHeightForWidthEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem6widgetEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem10spacerItemEv")) {
      taken[30] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(toolbar)
  //  void QToolBarLayout::addItem(QLayoutItem *item)
  void addItem(QLayoutItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBarLayoutCall0 call = reinterpret_cast<CuteQToolBarLayoutCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QToolBarLayout::addItem(item);
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  QLayoutItem *QToolBarLayout::itemAt(int index) const
  QLayoutItem *itemAt(int index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBarLayoutCall1 call = reinterpret_cast<CuteQToolBarLayoutCall1>(taken[1]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QToolBarLayout::itemAt(index);
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  QLayoutItem *QToolBarLayout::takeAt(int index)
  QLayoutItem *takeAt(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolBarLayoutCall2 call = reinterpret_cast<CuteQToolBarLayoutCall2>(taken[2]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QToolBarLayout::takeAt(index);
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  int QToolBarLayout::count() const
  int count() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolBarLayoutCall3 call = reinterpret_cast<CuteQToolBarLayoutCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QToolBarLayout::count();
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  bool QToolBarLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolBarLayoutCall4 call = reinterpret_cast<CuteQToolBarLayoutCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QToolBarLayout::isEmpty();
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  void QToolBarLayout::invalidate()
  void invalidate() override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolBarLayoutCall5 call = reinterpret_cast<CuteQToolBarLayoutCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QToolBarLayout::invalidate();
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  Qt::Orientations QToolBarLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolBarLayoutCall6 call = reinterpret_cast<CuteQToolBarLayoutCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QToolBarLayout::expandingDirections();
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  void QToolBarLayout::setGeometry(const QRect &r)
  void setGeometry(const QRect &r) override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolBarLayoutCall7 call = reinterpret_cast<CuteQToolBarLayoutCall7>(taken[7]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QToolBarLayout::setGeometry(r);
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  QSize QToolBarLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolBarLayoutCall8 call = reinterpret_cast<CuteQToolBarLayoutCall8>(taken[8]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QToolBarLayout::minimumSize();
  }
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
  //  QSize QToolBarLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolBarLayoutCall9 call = reinterpret_cast<CuteQToolBarLayoutCall9>(taken[9]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QToolBarLayout::sizeHint();
  }
#endif  // QT_CONFIG(toolbar)

  //  int QLayout::spacing() const
  int spacing() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolBarLayoutCall10 call = reinterpret_cast<CuteQToolBarLayoutCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::spacing();
  }

  //  void QLayout::setSpacing(int a0)
  void setSpacing(int a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolBarLayoutCall11 call = reinterpret_cast<CuteQToolBarLayoutCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLayout::setSpacing(a0);
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolBarLayoutCall12 call = reinterpret_cast<CuteQToolBarLayoutCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  QSize QLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolBarLayoutCall13 call = reinterpret_cast<CuteQToolBarLayoutCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::maximumSize();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolBarLayoutCall14 call = reinterpret_cast<CuteQToolBarLayoutCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQToolBarLayoutCall15 call = reinterpret_cast<CuteQToolBarLayoutCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQToolBarLayoutCall16 call = reinterpret_cast<CuteQToolBarLayoutCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSizePolicy::ControlType>::fromInt(given);
    }
    return QLayout::controlTypes();
  }

  //  QLayoutItem *QLayout::replaceWidget(QWidget *from, QWidget *to,
  //      Qt::FindChildOptions options)
  QLayoutItem *replaceWidget(
      QWidget *from,
      QWidget *to,
      Qt::FindChildOptions options) override {
    if (taken[17]) {
      int handled = 0;
      CuteQToolBarLayoutCall17 call = reinterpret_cast<CuteQToolBarLayoutCall17>(taken[17]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[18]) {
      int handled = 0;
      CuteQToolBarLayoutCall18 call = reinterpret_cast<CuteQToolBarLayoutCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQToolBarLayoutCall19 call = reinterpret_cast<CuteQToolBarLayoutCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQToolBarLayoutCall20 call = reinterpret_cast<CuteQToolBarLayoutCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQToolBarLayoutCall21 call = reinterpret_cast<CuteQToolBarLayoutCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQToolBarLayoutCall22 call = reinterpret_cast<CuteQToolBarLayoutCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQToolBarLayoutCall23 call = reinterpret_cast<CuteQToolBarLayoutCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQToolBarLayoutCall24 call = reinterpret_cast<CuteQToolBarLayoutCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQToolBarLayoutCall25 call = reinterpret_cast<CuteQToolBarLayoutCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QLayoutItem::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQToolBarLayoutCall26 call = reinterpret_cast<CuteQToolBarLayoutCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayoutItem::hasHeightForWidth();
  }

  //  int QLayoutItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQToolBarLayoutCall27 call = reinterpret_cast<CuteQToolBarLayoutCall27>(taken[27]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::heightForWidth(a0);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQToolBarLayoutCall28 call = reinterpret_cast<CuteQToolBarLayoutCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQToolBarLayoutCall29 call = reinterpret_cast<CuteQToolBarLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQToolBarLayoutCall30 call = reinterpret_cast<CuteQToolBarLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QToolBarLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QToolBarLayout10metaObjectEv(
    const QToolBarLayout *self) {
  return self->metaObject();
}

//  QToolBarLayout::~QToolBarLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayoutD1Ev(QToolBarLayout *self) {
  delete self;
}

//  void QToolBarLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout7addItemEP11QLayoutItem(
    QToolBarLayout *self,
    QLayoutItem *item) {
  self->addItem(item);
}

//  QLayoutItem *QToolBarLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK14QToolBarLayout6itemAtEi(
    const QToolBarLayout *self,
    int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QToolBarLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN14QToolBarLayout6takeAtEi(
    QToolBarLayout *self,
    int index) {
  return self->takeAt(index);
}

//  int QToolBarLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QToolBarLayout5countEv(const QToolBarLayout *self) {
  return self->count();
}

//  bool QToolBarLayout::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QToolBarLayout7isEmptyEv(const QToolBarLayout *self) {
  return self->isEmpty();
}

//  void QToolBarLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout10invalidateEv(QToolBarLayout *self) {
  self->invalidate();
}

//  Qt::Orientations QToolBarLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QToolBarLayout19expandingDirectionsEv(
    const QToolBarLayout *self) {
  return static_cast<int>(self->expandingDirections().toInt());
}

//  void QToolBarLayout::setGeometry(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout11setGeometryERK5QRect(
    QToolBarLayout *self,
    const QRect *r) {
  self->setGeometry(*r);
}

//  QSize QToolBarLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QToolBarLayout11minimumSizeEv(
    const QToolBarLayout *self) {
  return new QSize(self->minimumSize());
}

//  QSize QToolBarLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QToolBarLayout8sizeHintEv(const QToolBarLayout *self) {
  return new QSize(self->sizeHint());
}

//  int QToolBarLayout::indexOf(const QAction *action) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QToolBarLayout7indexOfEPK7QAction(
    const QToolBarLayout *self,
    const QAction *action) {
  return self->indexOf(action);
}

//  QSize QToolBarLayout::expandedSize(const QSize &size) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QToolBarLayout12expandedSizeERK5QSize(
    const QToolBarLayout *self,
    const QSize *size) {
  return new QSize(self->expandedSize(*size));
}

//  void QToolBarLayout::setUsePopupMenu(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout15setUsePopupMenuEb(
    QToolBarLayout *self,
    bool set) {
  self->setUsePopupMenu(set);
}

//  void QToolBarLayout::checkUsePopupMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout17checkUsePopupMenuEv(QToolBarLayout *self) {
  self->checkUsePopupMenu();
}

//  bool QToolBarLayout::movable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QToolBarLayout7movableEv(const QToolBarLayout *self) {
  return self->movable();
}

//  void QToolBarLayout::updateMarginAndSpacing()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout22updateMarginAndSpacingEv(
    QToolBarLayout *self) {
  self->updateMarginAndSpacing();
}

//  bool QToolBarLayout::hasExpandFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QToolBarLayout13hasExpandFlagEv(
    const QToolBarLayout *self) {
  return self->hasExpandFlag();
}

//  void QToolBarLayout::updateMacBorderMetrics()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QToolBarLayout22updateMacBorderMetricsEv(
    QToolBarLayout *self) {
  self->updateMacBorderMetrics();
}

//  void QToolBarLayout::updateGeomArray() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QToolBarLayout15updateGeomArrayEv(
    const QToolBarLayout *self) {
  self->updateGeomArray();
}

//  a Python function taken by a CuteQToolBarLayout, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBarLayout(
    QToolBarLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQToolBarLayout *>(self)->take(key, call);
}

//  void QToolBarLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QToolBarLayout7addItemEP11QLayoutItem(
    QToolBarLayout *self,
    QLayoutItem *item) {
  self->QToolBarLayout::addItem(item);
}

//  QLayoutItem *QToolBarLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK14QToolBarLayout6itemAtEi(
    const QToolBarLayout *self,
    int index) {
  return self->QToolBarLayout::itemAt(index);
}

//  QLayoutItem *QToolBarLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZN14QToolBarLayout6takeAtEi(
    QToolBarLayout *self,
    int index) {
  return self->QToolBarLayout::takeAt(index);
}

//  int QToolBarLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QToolBarLayout5countEv(const QToolBarLayout *self) {
  return self->QToolBarLayout::count();
}

//  bool QToolBarLayout::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QToolBarLayout7isEmptyEv(const QToolBarLayout *self) {
  return self->QToolBarLayout::isEmpty();
}

//  void QToolBarLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QToolBarLayout10invalidateEv(QToolBarLayout *self) {
  self->QToolBarLayout::invalidate();
}

//  Qt::Orientations QToolBarLayout::expandingDirections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QToolBarLayout19expandingDirectionsEv(
    const QToolBarLayout *self) {
  return static_cast<int>(
      self->QToolBarLayout::expandingDirections().toInt());
}

//  QSize QToolBarLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK14QToolBarLayout11minimumSizeEv(
    const QToolBarLayout *self) {
  return new QSize(self->QToolBarLayout::minimumSize());
}

//  QSize QToolBarLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK14QToolBarLayout8sizeHintEv(
    const QToolBarLayout *self) {
  return new QSize(self->QToolBarLayout::sizeHint());
}

#endif  // QT_CONFIG(toolbar)
