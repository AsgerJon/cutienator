//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qregion.h>
#include <QtCore/QList>
#include <QtCore/QString>
#include <QtCore/QSet>
#include <QtWidgets/QWidget>
#include <memory>
#include <QtWidgets/QLayoutItem>
#include <QtWidgets/QTabBar>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "QtWidgets/qapplication.h"
#include "QtWidgets/qwidget.h"
#if QT_CONFIG(tabbar)
#include "QtWidgets/qtabbar.h"
#endif
#include "QtWidgets/qstyle.h"
#include "QtWidgets/qapplication.h"
#include "QtCore/qvariant.h"
#include <QtWidgets/private/qdockarealayout_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qdockwidget_p.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#endif
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qproxystyle.h>
#include <QtGui/qwindow.h>
#include <QtGui/qscreen.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qdockwidget_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(dockwidget)
#include <QtWidgets/private/qdockarealayout_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(toolbar)
#include <QtWidgets/private/qtoolbar_p.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#endif
#include <QtWidgets/qmainwindow.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/private/qtabbar_p.h>
#endif
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtCore/qmimedata.h>
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#include <QtCore/qstring.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qstack.h>
#include <QtCore/qmap.h>
#include <QtCore/qpointer.h>
#ifndef QT_NO_DEBUG_STREAM
#  include <QtCore/qdebug.h>
#  include <QtCore/qtextstream.h>
#endif
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtCore/QScopedValueRollback>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qdockarealayout.cpp, line 46, as local:qdockarealayout.cpp:StateMarkers
using StateMarkers = QMainWindowLayoutState::StateMarkers;

//  from src/widgets/widgets/qdockarealayout.cpp, line 246, as local:qdockarealayout.cpp:tabId
#if QT_CONFIG(tabbar)
static quintptr tabId(const QDockAreaLayoutItem &item)
{
    if (item.widgetItem == nullptr)
        return 0;
    return reinterpret_cast<quintptr>(item.widgetItem->widget());
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 254, as local:qdockarealayout.cpp:zero
static const int zero = 0;

//  from src/widgets/widgets/qdockarealayout.cpp, line 521, as local:qdockarealayout.cpp:realMinSize
static int realMinSize(const QDockAreaLayoutInfo &info)
{
    int result = 0;
    bool first = true;
    for (int i = 0; i < info.item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = info.item_list.at(i);
        if (item.skip())
            continue;

        int min = 0;
        if ((item.flags & QDockAreaLayoutItem::KeepSize) && item.size != -1)
            min = item.size;
        else
            min = pick(info.o, item.minimumSize());

        if (!first)
            result += *info.sep;
        result += min;

        first = false;
    }

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 546, as local:qdockarealayout.cpp:realMaxSize
static int realMaxSize(const QDockAreaLayoutInfo &info)
{
    int result = 0;
    bool first = true;
    for (int i = 0; i < info.item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = info.item_list.at(i);
        if (item.skip())
            continue;

        int max = 0;
        if ((item.flags & QDockAreaLayoutItem::KeepSize) && item.size != -1)
            max = item.size;
        else
            max = pick(info.o, item.maximumSize());

        if (!first)
            result += *info.sep;
        result += max;

        if (result >= QWIDGETSIZE_MAX)
            return QWIDGETSIZE_MAX;

        first = false;
    }

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 681, as local:qdockarealayout.cpp:dockPosHelper
static QInternal::DockPosition dockPosHelper(const QRect &rect, const QPoint &_pos,
                                        Qt::Orientation o,
                                        bool nestingEnabled,
                                        QDockAreaLayoutInfo::TabMode tabMode)
{
    if (tabMode == QDockAreaLayoutInfo::ForceTabs)
        return QInternal::DockCount;

    QPoint pos = _pos - rect.topLeft();

    int x = pos.x();
    int y = pos.y();
    int w = rect.width();
    int h = rect.height();

    if (tabMode != QDockAreaLayoutInfo::NoTabs) {
        // is it in the center?
        if (nestingEnabled) {
        /*             2/3
                +--------------+
                |              |
                |   CCCCCCCC   |
           2/3  |   CCCCCCCC   |
                |   CCCCCCCC   |
                |              |
                +--------------+     */

            QRect center(w/6, h/6, 2*w/3, 2*h/3);
            if (center.contains(pos))
                return QInternal::DockCount;
        } else if (o == Qt::Horizontal) {
        /*             2/3
                +--------------+
                |   CCCCCCCC   |
                |   CCCCCCCC   |
                |   CCCCCCCC   |
                |   CCCCCCCC   |
                |   CCCCCCCC   |
                +--------------+     */

            if (x > w/6 && x < w*5/6)
                return QInternal::DockCount;
        } else {
        /*
                +--------------+
                |              |
           2/3  |CCCCCCCCCCCCCC|
                |CCCCCCCCCCCCCC|
                |              |
                +--------------+     */
            if (y > h/6 && y < 5*h/6)
                return QInternal::DockCount;
        }
    }

    // not in the center. which edge?
    if (nestingEnabled) {
        if (o == Qt::Horizontal) {
    /*       1/3  1/3 1/3
            +------------+     (we've already ruled out the center)
            |LLLLTTTTRRRR|
            |LLLLTTTTRRRR|
            |LLLLBBBBRRRR|
            |LLLLBBBBRRRR|
            +------------+    */

            if (x < w/3)
                return QInternal::LeftDock;
            if (x > 2*w/3)
                return QInternal::RightDock;
            if (y < h/2)
                return QInternal::TopDock;
            return QInternal::BottomDock;
        } else {
    /*      +------------+     (we've already ruled out the center)
        1/3 |TTTTTTTTTTTT|
            |LLLLLLRRRRRR|
        1/3 |LLLLLLRRRRRR|
        1/3 |BBBBBBBBBBBB|
            +------------+    */

            if (y < h/3)
                return QInternal::TopDock;
            if (y > 2*h/3)
                return QInternal::BottomDock;
            if (x < w/2)
                return QInternal::LeftDock;
            return QInternal::RightDock;
        }
    } else {
        if (o == Qt::Horizontal) {
            return x < w/2
                    ? QInternal::LeftDock
                    : QInternal::RightDock;
        } else {
            return y < h/2
                    ? QInternal::TopDock
                    : QInternal::BottomDock;
        }
    }
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 874, as local:qdockarealayout.cpp:shrink
static inline int shrink(QLayoutStruct &ls, int delta)
{
    if (ls.empty)
        return 0;
    int old_size = ls.size;
    ls.size = qMax(ls.size - delta, ls.minimumSize);
    return old_size - ls.size;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 883, as local:qdockarealayout.cpp:grow
static inline int grow(QLayoutStruct &ls, int delta)
{
    if (ls.empty)
        return 0;
    int old_size = ls.size;
    ls.size = qMin(ls.size + delta, ls.maximumSize);
    return ls.size - old_size;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1154, as local:qdockarealayout.cpp:dockedGeometry
static QRect dockedGeometry(QWidget *widget)
{
    int titleHeight = 0;

    QDockWidgetLayout *layout
        = qobject_cast<QDockWidgetLayout*>(widget->layout());
    if (layout && layout->nativeWindowDeco())
        titleHeight = layout->titleHeight();

    QRect result = widget->geometry();
    result.adjust(0, -titleHeight, 0, 0);
    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1638, as local:qdockarealayout.cpp:paintSep
static void paintSep(QPainter *p, QWidget *w, const QRect &r, Qt::Orientation o, bool mouse_over)
{
    QStyleOption opt(0);
    opt.state = QStyle::State_None;
    if (w->isEnabled())
        opt.state |= QStyle::State_Enabled;
    if (o != Qt::Horizontal)
        opt.state |= QStyle::State_Horizontal;
    if (mouse_over)
        opt.state |= QStyle::State_MouseOver;
    opt.rect = r;
    opt.palette = w->palette();

    w->style()->drawPrimitive(QStyle::PE_IndicatorDockWidgetResizeHandle, &opt, p, w);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2117, as local:qdockarealayout.cpp:raiseSeparatorWidget
#if QT_CONFIG(tabbar)
static void raiseSeparatorWidget(QWidget *separatorWidget)
{
    Q_ASSERT(separatorWidget);

#if QT_CONFIG(toolbar)
    // Raise the separator widget, but make sure it doesn't go above
    // an expanded toolbar, as that would break mouse event hit testing.
    Q_ASSERT(separatorWidget->parent());
    const auto toolBars = separatorWidget->parent()->findChildren<QToolBar*>(Qt::FindDirectChildrenOnly);
    for (auto *toolBar : toolBars) {
        if (auto *toolBarLayout = qobject_cast<QToolBarLayout*>(toolBar->layout())) {
            if (toolBarLayout->expanded) {
                separatorWidget->stackUnder(toolBar);
                return;
            }
        }
    }
#endif

    separatorWidget->raise();
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 261, as local:qmainwindowlayout.cpp:QDockWidgetGroupLayout
#if QT_CONFIG(dockwidget)
class QDockWidgetGroupLayout : public QLayout,
                               public QMainWindowLayoutSeparatorHelper<QDockWidgetGroupLayout>
{
    QWidgetResizeHandler *resizer;
public:
    QDockWidgetGroupLayout(QDockWidgetGroupWindow* parent) : QLayout(parent) {
        setSizeConstraint(QLayout::SetMinAndMaxSize);
        resizer = new QWidgetResizeHandler(parent);
    }
    ~QDockWidgetGroupLayout() {
        layoutState.deleteAllLayoutItems();
    }

    void addItem(QLayoutItem*) override { Q_UNREACHABLE(); }
    int count() const override { return 0; }
    QLayoutItem* itemAt(int index) const override
    {
        int x = 0;
        return layoutState.itemAt(&x, index);
    }
    QLayoutItem* takeAt(int index) override
    {
        int x = 0;
        QLayoutItem *ret = layoutState.takeAt(&x, index);
        if (savedState.rect.isValid() && ret->widget()) {
            // we need to remove the item also from the saved state to prevent crash
            QList<int> path = savedState.indexOf(ret->widget());
            if (!path.isEmpty())
                savedState.remove(path);
            // Also, the item may be contained several times as a gap item.
            path = layoutState.indexOf(ret->widget());
            if (!path.isEmpty())
                layoutState.remove(path);
        }
        return ret;
    }
    QSize sizeHint() const override
    {
        int fw = frameWidth();
        return layoutState.sizeHint() + QSize(fw, fw);
    }
    QSize minimumSize() const override
    {
        int fw = frameWidth();
        return layoutState.minimumSize() + QSize(fw, fw);
    }
    QSize maximumSize() const override
    {
        int fw = frameWidth();
        return layoutState.maximumSize() + QSize(fw, fw);
    }
    void setGeometry(const QRect&r) override
    {
        groupWindow()->destroyOrHideIfEmpty();
        QDockAreaLayoutInfo *li = dockAreaLayoutInfo();
        if (li->isEmpty())
            return;
        int fw = frameWidth();
#if QT_CONFIG(tabbar)
        li->reparentWidgets(parentWidget());
#endif
        li->rect = r.adjusted(fw, fw, -fw, -fw);
        li->fitItems();
        li->apply(QWidgetAnimator::AnimationRule::Stop);
        if (savedState.rect.isValid())
            savedState.rect = li->rect;
        resizer->setEnabled(!nativeWindowDeco());
    }

    QDockAreaLayoutInfo *dockAreaLayoutInfo() { return &layoutState; }

#if QT_CONFIG(toolbar)
    QToolBarAreaLayout *toolBarAreaLayout()
    {
        return nullptr; // QDockWidgetGroupWindow doesn't have toolbars
    }
#endif

    bool nativeWindowDeco() const
    {
        return groupWindow()->hasNativeDecos();
    }

    int frameWidth() const
    {
        return nativeWindowDeco() ? 0 :
            parentWidget()->style()->pixelMetric(QStyle::PM_DockWidgetFrameWidth, nullptr, parentWidget());
    }

    QDockWidgetGroupWindow *groupWindow() const
    {
        return static_cast<QDockWidgetGroupWindow *>(parent());
    }

    QDockAreaLayoutInfo layoutState;
    QDockAreaLayoutInfo savedState;
};
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2067, as local:qmainwindowlayout.cpp:QMainWindowTabBar
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
class QMainWindowTabBar : public QTabBar
{
    Q_OBJECT
    QPointer<QMainWindow> mainWindow;
    QPointer<QDockWidget> draggingDock; // Currently dragging (detached) dock widget
public:
    QMainWindowTabBar(QMainWindow *parent);
    ~QMainWindowTabBar();
    QDockWidget *dockAt(int index) const;
    QList<QDockWidget *> dockWidgets() const;
    bool contains(const QDockWidget *dockWidget) const;
protected:
    bool event(QEvent *e) override;
    void mouseReleaseEvent(QMouseEvent*) override;
    void mouseMoveEvent(QMouseEvent*) override;

};
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2112, as local:qmainwindowlayout.cpp:QMainWindowTabBar::QMainWindowTabBar
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline QMainWindowTabBar::QMainWindowTabBar(QMainWindow *parent)
    : QTabBar(parent), mainWindow(parent)
{
    setExpanding(false);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2118, as local:qmainwindowlayout.cpp:QMainWindowTabBar::dockWidgets
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline QList<QDockWidget *> QMainWindowTabBar::dockWidgets() const
{
    QList<QDockWidget *> docks;
    for (int i = 0; i < count(); ++i) {
        if (QDockWidget *dock = dockAt(i))
            docks << dock;
    }
    return docks;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2128, as local:qmainwindowlayout.cpp:QMainWindowTabBar::contains
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline bool QMainWindowTabBar::contains(const QDockWidget *dockWidget) const
{
    for (int i = 0; i < count(); ++i) {
        if (dockAt(i) == dockWidget)
            return true;
    }
    return false;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2169, as local:qmainwindowlayout.cpp:moveToUnplugPosition
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
static void moveToUnplugPosition(QPoint mouse, QDockWidget *dockWidget)
{
    Q_ASSERT(dockWidget);

    if (auto *tbWidget = dockWidget->titleBarWidget()) {
        dockWidget->move(mouse - tbWidget->rect().center());
        return;
    }

    const bool vertical = dockWidget->features().testFlag(QDockWidget::DockWidgetVerticalTitleBar);
    const int deltaX = vertical ? QApplication::startDragDistance() : dockWidget->width() / 2;
    const int deltaY = vertical ? dockWidget->height() / 2 : QApplication::startDragDistance();
    dockWidget->move(mouse - QPoint(deltaX, deltaY));
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2184, as local:qmainwindowlayout.cpp:QMainWindowTabBar::mouseMoveEvent
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline void QMainWindowTabBar::mouseMoveEvent(QMouseEvent *e)
{
    // The QTabBar handles the moving (reordering) of tabs.
    // When QTabBarPrivate::dragInProgress is true, and that the mouse is outside of a region
    // around the QTabBar, we will consider the user wants to drag that QDockWidget away from this
    // tab area.

    QTabBarPrivate *d = static_cast<QTabBarPrivate*>(d_ptr.data());
    if (!draggingDock && (mainWindow->dockOptions() & QMainWindow::GroupedDragging)) {
        int offset = QApplication::startDragDistance() + 1;
        offset *= 3;
        QRect r = rect().adjusted(-offset, -offset, offset, offset);
        if (d->dragInProgress && !r.contains(e->position().toPoint()) && d->validIndex(d->pressedIndex)) {
            draggingDock = dockAt(d->pressedIndex);
            if (draggingDock) {
                // We should drag this QDockWidget away by unpluging it.
                // First cancel the QTabBar's internal move
                d->moveTabFinished(d->pressedIndex);
                d->pressedIndex = -1;
                if (d->movingTab)
                    d->movingTab->setVisible(false);
                d->dragStartPosition = QPoint();

                // Then starts the drag using QDockWidgetPrivate's API
                QDockWidgetPrivate *dockPriv = static_cast<QDockWidgetPrivate *>(QObjectPrivate::get(draggingDock));
                QDockWidgetLayout *dwlayout = static_cast<QDockWidgetLayout *>(draggingDock->layout());
                dockPriv->initDrag(dwlayout->titleArea().center(), true);
                dockPriv->startDrag(QDockWidgetPrivate::DragScope::Widget);
                if (dockPriv->state)
                    dockPriv->state->ctrlDrag = e->modifiers() & Qt::ControlModifier;
            }
        }
    }

    if (draggingDock) {
        QDockWidgetPrivate *dockPriv = static_cast<QDockWidgetPrivate *>(QObjectPrivate::get(draggingDock));
        if (dockPriv->state && dockPriv->state->dragging) {
            // move will call QMainWindowLayout::hover
            moveToUnplugPosition(e->globalPosition().toPoint(), draggingDock);
        }
    }
    QTabBar::mouseMoveEvent(e);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2243, as local:qmainwindowlayout.cpp:QMainWindowTabBar::mouseReleaseEvent
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline void QMainWindowTabBar::mouseReleaseEvent(QMouseEvent *e)
{
    if (draggingDock && e->button() == Qt::LeftButton) {
        QDockWidgetPrivate *dockPriv = static_cast<QDockWidgetPrivate *>(QObjectPrivate::get(draggingDock));
        if (dockPriv->state && dockPriv->state->dragging)
            dockPriv->endDrag(QDockWidgetPrivate::EndDragMode::LocationChange);

        draggingDock = nullptr;
    }
    QTabBar::mouseReleaseEvent(e);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2255, as local:qmainwindowlayout.cpp:QMainWindowTabBar::event
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline bool QMainWindowTabBar::event(QEvent *e)
{
    // show the tooltip if tab is too small to fit label

    if (e->type() != QEvent::ToolTip)
        return QTabBar::event(e);
    QSize size = this->size();
    QSize hint = sizeHint();
    if (shape() == QTabBar::RoundedWest || shape() == QTabBar::RoundedEast) {
        size = size.transposed();
        hint = hint.transposed();
    }
    if (size.width() < hint.width())
        return QTabBar::event(e);
    e->accept();
    return true;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qdockarealayout.cpp, line 2226, as _ZNK19QDockAreaLayoutInfo12updateTabBarEv
#if QT_CONFIG(tabbar)
inline bool QDockAreaLayoutInfo::updateTabBar() const
{
    if (!tabbed)
        return false;

    QDockAreaLayoutInfo *that = const_cast<QDockAreaLayoutInfo*>(this);

    if (that->tabBar == nullptr) {
        that->tabBar = mainWindowLayout()->getTabBar();
        that->tabBar->setShape(static_cast<QTabBar::Shape>(tabBarShape));
        that->tabBar->setDrawBase(true);
    }

    const QSignalBlocker blocker(tabBar);
    bool gap = false;

    const quintptr oldCurrentId = currentTabId();

    int tab_idx = 0;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;
        if (item.flags & QDockAreaLayoutItem::GapItem) {
            gap = true;
            continue;
        }
        if (item.widgetItem == nullptr)
            continue;

        QDockWidget *dw = qobject_cast<QDockWidget*>(item.widgetItem->widget());
        QString title = dw->d_func()->fixedWindowTitle;
        quintptr id = tabId(item);
        const QIcon windowIcon = dw->testAttribute(Qt::WA_SetWindowIcon) ? dw->windowIcon()
                                                                         : QIcon();
        if (tab_idx == tabBar->count()) {
            tabBar->insertTab(tab_idx, windowIcon, title);
#if QT_CONFIG(tooltip)
            tabBar->setTabToolTip(tab_idx, title);
#endif
            tabBar->setTabData(tab_idx, id);
        } else if (qvariant_cast<quintptr>(tabBar->tabData(tab_idx)) != id) {
            if (tab_idx + 1 < tabBar->count()
                    && qvariant_cast<quintptr>(tabBar->tabData(tab_idx + 1)) == id)
                tabBar->removeTab(tab_idx);
            else {
                tabBar->insertTab(tab_idx, windowIcon, title);
#if QT_CONFIG(tooltip)
                tabBar->setTabToolTip(tab_idx, title);
#endif
                tabBar->setTabData(tab_idx, id);
            }
        }

        if (title != tabBar->tabText(tab_idx)) {
            tabBar->setTabText(tab_idx, title);
#if QT_CONFIG(tooltip)
            tabBar->setTabToolTip(tab_idx, title);
#endif
        }

        ++tab_idx;
    }

    while (tab_idx < tabBar->count()) {
        tabBar->removeTab(tab_idx);
    }

    if (oldCurrentId > 0 && currentTabId() != oldCurrentId)
        that->setCurrentTabId(oldCurrentId);

    if (QDockWidgetGroupWindow *dwgw = qobject_cast<QDockWidgetGroupWindow *>(tabBar->parent()))
        dwgw->adjustFlags();

    //returns if the tabbar is visible or not
    return ( (gap ? 1 : 0) + tabBar->count()) > 1;
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 117, as _ZNK19QDockAreaLayoutItem11minimumSizeEv
inline QSize QDockAreaLayoutItem::minimumSize() const
{
    if (widgetItem)
        return widgetItem->minimumSize().grownBy(widgetItem->widget()->contentsMargins());
    if (subinfo != nullptr)
        return subinfo->minimumSize();
    return QSize(0, 0);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 96, as _ZNK19QDockAreaLayoutItem4skipEv
inline bool QDockAreaLayoutItem::skip() const
{
    if (placeHolderItem != nullptr)
        return true;

    if (flags & GapItem)
        return false;

    if (widgetItem != nullptr)
        return widgetItem->isEmpty();

    if (subinfo != nullptr) {
        for (int i = 0; i < subinfo->item_list.size(); ++i) {
            if (!subinfo->item_list.at(i).skip())
                return false;
        }
    }

    return true;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 126, as _ZNK19QDockAreaLayoutItem11maximumSizeEv
inline QSize QDockAreaLayoutItem::maximumSize() const
{
    if (widgetItem)
        return widgetItem->maximumSize().grownBy(widgetItem->widget()->contentsMargins());
    if (subinfo != nullptr)
        return subinfo->maximumSize();
    return QSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 135, as _ZNK19QDockAreaLayoutItem12hasFixedSizeEN2Qt11OrientationE
inline bool QDockAreaLayoutItem::hasFixedSize(Qt::Orientation o) const
{
    return perp(o, minimumSize()) == perp(o, maximumSize());
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 151, as _ZNK19QDockAreaLayoutItem8sizeHintEv
inline QSize QDockAreaLayoutItem::sizeHint() const
{
    if (placeHolderItem != nullptr)
        return QSize(0, 0);
    if (widgetItem)
        return widgetItem->sizeHint().grownBy(widgetItem->widget()->contentsMargins());
    if (subinfo != nullptr)
        return subinfo->sizeHint();
    return QSize(-1, -1);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1349, as _ZNK19QDockAreaLayoutInfo8itemRectEib
inline QRect QDockAreaLayoutInfo::itemRect(int index, bool isGap) const
{
    const QDockAreaLayoutItem &item = item_list.at(index);

    if (item.skip())
        return QRect();

    if (isGap && !(item.flags & QDockAreaLayoutItem::GapItem))
        return QRect();

    QRect result;

#if QT_CONFIG(tabbar)
    if (tabbed) {
        if (isGap || tabId(item) == currentTabId())
            result = tabContentRect();
    } else
#endif
    {
        int pos = item.pos;
        int size = item.size;

        if (isGap) {
            int prev = this->prev(index);
            int next = this->next(index);
            if (prev != -1 && !(item_list.at(prev).flags & QDockAreaLayoutItem::GapItem)) {
                pos += *sep;
                size -= *sep;
            }
            if (next != -1 && !(item_list.at(next).flags & QDockAreaLayoutItem::GapItem))
                size -= *sep;
        }

        QPoint p;
        rpick(o, p) = pos;
        rperp(o, p) = perp(o, rect.topLeft());
        QSize s;
        rpick(o, s) = size;
        rperp(o, s) = perp(o, rect.size());
        result = QRect(p, s);
    }

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 140, as _ZNK19QDockAreaLayoutItem9expansiveEN2Qt11OrientationE
inline bool QDockAreaLayoutItem::expansive(Qt::Orientation o) const
{
    if ((flags & GapItem) || placeHolderItem != nullptr)
        return false;
    if (widgetItem != nullptr)
        return ((widgetItem->expandingDirections() & o) == o);
    if (subinfo != nullptr)
        return subinfo->expansive(o);
    return false;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

//  from src/widgets/widgets/qdockwidget.cpp, line 569, as _ZN15QDockWidgetItemC1EP11QDockWidget
inline QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    : QWidgetItem(dockWidget)
{
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2301, as _ZN17QMainWindowLayout9getTabBarEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline QTabBar *QMainWindowLayout::getTabBar()
{
    if (!usedTabBars.isEmpty() && !isInRestoreState) {
        /*
            If dock widgets have been removed and added while the main window was
            hidden, then the layout hasn't been activated yet, and tab bars from empty
            docking areas haven't been put in the cache yet.
        */
        activate();
    }

    QTabBar *bar = new QMainWindowTabBar(static_cast<QMainWindow *>(parentWidget()));
    bar->setDrawBase(true);
    bar->setElideMode(Qt::ElideRight);
    bar->setDocumentMode(_documentMode);
    bar->setMovable(true);
    connect(bar, SIGNAL(currentChanged(int)), this, SLOT(tabChanged()));
    connect(bar, &QTabBar::tabMoved, this, &QMainWindowLayout::tabMoved);

    usedTabBars.insert(bar);
    return bar;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 560, as _ZN22QDockWidgetGroupWindow11adjustFlagsEv
#if QT_CONFIG(dockwidget)
inline void QDockWidgetGroupWindow::adjustFlags()
{
    Qt::WindowFlags oldFlags = windowFlags();
    Qt::WindowFlags flags = oldFlags;

#if QT_CONFIG(tabbar)
    QDockWidget *top = activeTabbedDockWidget();
#else
    QDockWidget *top = nullptr;
#endif
    if (!top) { // nested tabs, show window decoration
        flags =
            ((oldFlags & ~Qt::FramelessWindowHint) | Qt::CustomizeWindowHint | Qt::WindowTitleHint);
    } else if (static_cast<QDockWidgetGroupLayout *>(layout())->nativeWindowDeco()) {
        flags |= Qt::CustomizeWindowHint | Qt::WindowTitleHint;
        flags.setFlag(Qt::WindowCloseButtonHint, top->features() & QDockWidget::DockWidgetClosable);
        flags &= ~Qt::FramelessWindowHint;
    } else {
        flags &= ~(Qt::WindowCloseButtonHint | Qt::CustomizeWindowHint | Qt::WindowTitleHint);
        flags |= Qt::FramelessWindowHint;
    }

    if (oldFlags != flags) {
        if (!windowHandle())
            create(); // The desired geometry is forgotten if we call setWindowFlags before having a window
        setWindowFlags(flags);
        const bool gainedNativeDecos = (oldFlags & Qt::FramelessWindowHint) && !(flags & Qt::FramelessWindowHint);
        const bool lostNativeDecos = !(oldFlags & Qt::FramelessWindowHint) && (flags & Qt::FramelessWindowHint);

        // Adjust the geometry after gaining/losing decos, so that the client area appears always
        // at the same place when tabbing
        if (lostNativeDecos) {
            QRect newGeometry = geometry();
            newGeometry.setTop(frameGeometry().top());
            const int bottomFrame = geometry().top() - frameGeometry().top();
            m_removedFrameSize = QSize((frameSize() - size()).width(), bottomFrame);
            setGeometry(newGeometry);
        } else if (gainedNativeDecos && m_removedFrameSize.isValid()) {
            QRect r = geometry();
            r.adjust(-m_removedFrameSize.width() / 2, 0,
                     -m_removedFrameSize.width() / 2, -m_removedFrameSize.height());
            setGeometry(r);
            m_removedFrameSize = QSize();
        }

        setVisible(hasVisibleDockWidgets());
    }

    QWidget *titleBarOf = top ? top : parentWidget();
    setWindowTitle(titleBarOf->windowTitle());
    setWindowIcon(titleBarOf->windowIcon());
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qdockarealayout.cpp, line 256, as _ZN19QDockAreaLayoutInfoC1Ev
inline QDockAreaLayoutInfo::QDockAreaLayoutInfo()
    : sep(&zero), dockPos(QInternal::LeftDock), o(Qt::Horizontal), mainWindow(nullptr)
#if QT_CONFIG(tabbar)
    , tabbed(false), tabBar(nullptr), tabBarShape(QTabBar::RoundedSouth)
#endif
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 264, as _ZN19QDockAreaLayoutInfoC1EPKiN9QInternal12DockPositionEN2Qt11OrientationEiP11QMainWindow
inline QDockAreaLayoutInfo::QDockAreaLayoutInfo(const int *_sep, QInternal::DockPosition _dockPos,
                                            Qt::Orientation _o, int tbshape,
                                            QMainWindow *window)
    : sep(_sep), dockPos(_dockPos), o(_o), mainWindow(window)
#if QT_CONFIG(tabbar)
    , tabbed(false), tabBar(nullptr), tabBarShape(static_cast<QTabBar::Shape>(tbshape))
#endif
{
#if !QT_CONFIG(tabbar)
    Q_UNUSED(tbshape);
#endif
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 277, as _ZNK19QDockAreaLayoutInfo4sizeEv
inline QSize QDockAreaLayoutInfo::size() const
{
    return isEmpty() ? QSize(0, 0) : rect.size();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1313, as _ZN19QDockAreaLayoutInfo4infoEP7QWidget
inline QDockAreaLayoutInfo *QDockAreaLayoutInfo::info(QWidget *widget)
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

#if QT_CONFIG(tabbar)
        if (tabbed && widget == tabBar)
            return this;
#endif

        if (item.widgetItem != nullptr && item.widgetItem->widget() == widget)
            return this;

        if (item.subinfo != nullptr) {
            if (QDockAreaLayoutInfo *result = item.subinfo->info(widget))
                return result;
        }
    }

    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 505, as _ZNK19QDockAreaLayoutInfo9expansiveEN2Qt11OrientationE
inline bool QDockAreaLayoutInfo::expansive(Qt::Orientation o) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        if (item_list.at(i).expansive(o))
            return true;
    }
    return false;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1408, as _ZNK19QDockAreaLayoutInfo13separatorRectEi
inline QRect QDockAreaLayoutInfo::separatorRect(int index) const
{
#if QT_CONFIG(tabbar)
    if (tabbed)
        return QRect();
#endif

    const QDockAreaLayoutItem &item = item_list.at(index);
    if (item.skip())
        return QRect();

    QPoint pos = rect.topLeft();
    rpick(o, pos) = item.pos + item.size;
    QSize s = rect.size();
    rpick(o, s) = *sep;

    return QRect(pos, s);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1427, as _ZNK19QDockAreaLayoutInfo13separatorRectERK5QListIiE
inline QRect QDockAreaLayoutInfo::separatorRect(const QList<int> &path) const
{
    Q_ASSERT(!path.isEmpty());

    const int index = path.first();
    if (path.size() > 1) {
        const QDockAreaLayoutItem &item = item_list.at(index);
        Q_ASSERT(item.subinfo != nullptr);
        return item.subinfo->separatorRect(path.mid(1));
    }
    return separatorRect(index);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 282, as _ZN19QDockAreaLayoutInfo5clearEv
inline void QDockAreaLayoutInfo::clear()
{
    item_list.clear();
    rect = QRect();
#if QT_CONFIG(tabbar)
    tabbed = false;
    tabBar = nullptr;
#endif
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 292, as _ZNK19QDockAreaLayoutInfo7isEmptyEv
inline bool QDockAreaLayoutInfo::isEmpty() const
{
    return next(-1) == -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1168, as _ZNK19QDockAreaLayoutInfo10hasGapItemERK5QListIiE
inline bool QDockAreaLayoutInfo::hasGapItem(const QList<int> &path) const
{
    // empty path has no gap item
    if (path.isEmpty())
        return false;

    // Index -1 isn't a gap
    // Index out of range points at a position to be created. That isn't a gap either.
    const int index = path.constFirst();
    if (index < 0 || index >= item_list.count())
        return false;

    return item_list[index].flags & QDockAreaLayoutItem::GapItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 297, as _ZNK19QDockAreaLayoutInfo19onlyHasPlaceholdersEv
inline bool QDockAreaLayoutInfo::onlyHasPlaceholders() const
{
    for (const QDockAreaLayoutItem &item : item_list) {
        if (!item.placeHolderItem)
            return false;
    }

    return true;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1719, as _ZNK19QDockAreaLayoutInfo4nextEi
inline int QDockAreaLayoutInfo::next(int index) const
{
    for (int i = index + 1; i < item_list.size(); ++i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1728, as _ZNK19QDockAreaLayoutInfo4prevEi
inline int QDockAreaLayoutInfo::prev(int index) const
{
    for (int i = index - 1; i >= 0; --i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1507, as _ZNK19QDockAreaLayoutInfo7indexOfEPK7QWidget
inline QList<int> QDockAreaLayoutInfo::indexOf(const QWidget *widget) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.placeHolderItem != nullptr)
            continue;

        if (item.subinfo != nullptr) {
            QList<int> result = item.subinfo->indexOf(widget);
            if (!result.isEmpty()) {
                result.prepend(i);
                return result;
            }
            continue;
        }

        if (!(item.flags & QDockAreaLayoutItem::GapItem) && item.widgetItem && item.widgetItem->widget() == widget) {
            QList<int> result;
            result << i;
            return result;
        }
    }

    return QList<int>();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1483, as _ZNK19QDockAreaLayoutInfo18indexOfPlaceHolderERK7QString
inline QList<int> QDockAreaLayoutInfo::indexOfPlaceHolder(const QString &objectName) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.subinfo != nullptr) {
            QList<int> result = item.subinfo->indexOfPlaceHolder(objectName);
            if (!result.isEmpty()) {
                result.prepend(i);
                return result;
            }
            continue;
        }

        if (item.placeHolderItem != nullptr && item.placeHolderItem->objectName == objectName) {
            QList<int> result;
            result << i;
            return result;
        }
    }

    return QList<int>();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1654, as _ZNK19QDockAreaLayoutInfo15separatorRegionEv
inline QRegion QDockAreaLayoutInfo::separatorRegion() const
{
    QRegion result;

    if (isEmpty())
        return result;
#if QT_CONFIG(tabbar)
    if (tabbed)
        return result;
#endif

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.skip())
            continue;

        int next = this->next(i);

        if (item.subinfo)
            result |= item.subinfo->separatorRegion();

        if (next == -1)
            break;
        result |= separatorRect(i);
    }

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1788, as _ZNK19QDockAreaLayoutInfo6itemAtEPii
inline QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.placeHolderItem != nullptr)
            continue;
        if (item.subinfo) {
            if (QLayoutItem *ret = item.subinfo->itemAt(x, index))
                return ret;
        } else if (item.widgetItem) {
            if ((*x)++ == index)
                return item.widgetItem;
        }
    }
    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2355, as _ZNK19QDockAreaLayoutInfo20usedSeparatorWidgetsEv
#if QT_CONFIG(tabbar)
inline QSet<QWidget*> QDockAreaLayoutInfo::usedSeparatorWidgets() const
{
    QSet<QWidget*> result;
    const int numSeparatorWidgets = separatorWidgets.size();
    result.reserve(numSeparatorWidgets);

    for (int i = 0; i < numSeparatorWidgets; ++i)
        result << separatorWidgets.at(i);

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.subinfo != nullptr)
            result += item.subinfo->usedSeparatorWidgets();
    }

    return result;
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1122, as _ZNK19QDockAreaLayoutInfo12currentTabIdEv
#if QT_CONFIG(tabbar)
inline quintptr QDockAreaLayoutInfo::currentTabId() const
{
    if (!tabbed || tabBar == nullptr)
        return 0;

    int index = tabBar->currentIndex();
    if (index == -1)
        return 0;

    return qvariant_cast<quintptr>(tabBar->tabData(index));
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1134, as _ZN19QDockAreaLayoutInfo13setCurrentTabEP7QWidget
#if QT_CONFIG(tabbar)
inline void QDockAreaLayoutInfo::setCurrentTab(QWidget *widget)
{
    setCurrentTabId(reinterpret_cast<quintptr>(widget));
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1139, as _ZN19QDockAreaLayoutInfo15setCurrentTabIdEy
#if QT_CONFIG(tabbar)
inline void QDockAreaLayoutInfo::setCurrentTabId(quintptr id)
{
    if (!tabbed || tabBar == nullptr)
        return;

    for (int i = 0; i < tabBar->count(); ++i) {
        if (qvariant_cast<quintptr>(tabBar->tabData(i)) == id) {
            tabBar->setCurrentIndex(i);
            return;
        }
    }
}
#endif  // QT_CONFIG(tabbar)
//  -----------------------------------------------------------------------

//  QDockAreaLayoutInfo::QDockAreaLayoutInfo()
extern "C" Q_DECL_EXPORT
QDockAreaLayoutInfo *ritual_ZN19QDockAreaLayoutInfoC1Ev() {
  return new QDockAreaLayoutInfo();
}

//  QDockAreaLayoutInfo::QDockAreaLayoutInfo(const int *_sep,
//      QInternal::DockPosition _dockPos, Qt::Orientation _o, int tbhape,
//      QMainWindow *window)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutInfo *ritual_ZN19QDockAreaLayoutInfoC1EPKiN9QInternal12DockPositionEN2Qt11OrientationEiP11QMainWindow(
    const int *_sep,
    QInternal::DockPosition _dockPos,
    Qt::Orientation _o,
    int tbhape,
    QMainWindow *window) {
  return new QDockAreaLayoutInfo(_sep, _dockPos, _o, tbhape, window);
}

//  QSize QDockAreaLayoutInfo::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QDockAreaLayoutInfo4sizeEv(
    const QDockAreaLayoutInfo *self) {
  return new QSize(self->size());
}

//  QDockAreaLayoutInfo *QDockAreaLayoutInfo::info(QWidget *widget)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutInfo *ritual_ZN19QDockAreaLayoutInfo4infoEP7QWidget(
    QDockAreaLayoutInfo *self,
    QWidget *widget) {
  return self->info(widget);
}

//  bool QDockAreaLayoutInfo::expansive(Qt::Orientation o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo9expansiveEN2Qt11OrientationE(
    const QDockAreaLayoutInfo *self,
    Qt::Orientation o) {
  return self->expansive(o);
}

//  QRect QDockAreaLayoutInfo::separatorRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QDockAreaLayoutInfo13separatorRectEi(
    const QDockAreaLayoutInfo *self,
    int index) {
  return new QRect(self->separatorRect(index));
}

//  QRect QDockAreaLayoutInfo::separatorRect(const QList<int> &path) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QDockAreaLayoutInfo13separatorRectERK5QListIiE(
    const QDockAreaLayoutInfo *self,
    const QList<int> *path) {
  return new QRect(self->separatorRect(*path));
}

//  void QDockAreaLayoutInfo::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfo5clearEv(QDockAreaLayoutInfo *self) {
  self->clear();
}

//  bool QDockAreaLayoutInfo::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo7isEmptyEv(
    const QDockAreaLayoutInfo *self) {
  return self->isEmpty();
}

//  bool QDockAreaLayoutInfo::hasGapItem(const QList<int> &path) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo10hasGapItemERK5QListIiE(
    const QDockAreaLayoutInfo *self,
    const QList<int> *path) {
  return self->hasGapItem(*path);
}

//  bool QDockAreaLayoutInfo::onlyHasPlaceholders() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo19onlyHasPlaceholdersEv(
    const QDockAreaLayoutInfo *self) {
  return self->onlyHasPlaceholders();
}

//  int QDockAreaLayoutInfo::next(int idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDockAreaLayoutInfo4nextEi(
    const QDockAreaLayoutInfo *self,
    int idx) {
  return self->next(idx);
}

//  int QDockAreaLayoutInfo::prev(int idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDockAreaLayoutInfo4prevEi(
    const QDockAreaLayoutInfo *self,
    int idx) {
  return self->prev(idx);
}

//  QList<int> QDockAreaLayoutInfo::indexOf(const QWidget *widget) const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK19QDockAreaLayoutInfo7indexOfEPK7QWidget(
    const QDockAreaLayoutInfo *self,
    const QWidget *widget) {
  return new QList<int>(self->indexOf(widget));
}

//  QList<int> QDockAreaLayoutInfo::indexOfPlaceHolder(const QString
//      &objectName) const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK19QDockAreaLayoutInfo18indexOfPlaceHolderERK7QString(
    const QDockAreaLayoutInfo *self,
    const QString *objectName) {
  return new QList<int>(self->indexOfPlaceHolder(*objectName));
}

//  QRegion QDockAreaLayoutInfo::separatorRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK19QDockAreaLayoutInfo15separatorRegionEv(
    const QDockAreaLayoutInfo *self) {
  return new QRegion(self->separatorRegion());
}

//  QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK19QDockAreaLayoutInfo6itemAtEPii(
    const QDockAreaLayoutInfo *self,
    int *x,
    int index) {
  return self->itemAt(x, index);
}

#if QT_CONFIG(tabbar)
//  QSet<QWidget *> QDockAreaLayoutInfo::usedSeparatorWidgets() const
extern "C" Q_DECL_EXPORT
QSet<QWidget *> *ritual_ZNK19QDockAreaLayoutInfo20usedSeparatorWidgetsEv(
    const QDockAreaLayoutInfo *self) {
  return new QSet<QWidget *>(self->usedSeparatorWidgets());
}
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
//  quintptr QDockAreaLayoutInfo::currentTabId() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK19QDockAreaLayoutInfo12currentTabIdEv(
    const QDockAreaLayoutInfo *self) {
  return self->currentTabId();
}
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
//  void QDockAreaLayoutInfo::setCurrentTab(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfo13setCurrentTabEP7QWidget(
    QDockAreaLayoutInfo *self,
    QWidget *widget) {
  self->setCurrentTab(widget);
}
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
//  void QDockAreaLayoutInfo::setCurrentTabId(quintptr id)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfo15setCurrentTabIdEy(
    QDockAreaLayoutInfo *self,
    quintptr id) {
  self->setCurrentTabId(id);
}
#endif  // QT_CONFIG(tabbar)

//  QDockAreaLayoutInfo::~QDockAreaLayoutInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfoD1Ev(QDockAreaLayoutInfo *self) {
  delete self;
}

//  a QList<int> a ritual of QDockAreaLayoutInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayoutInfo__QList_int(QList<int> *self) {
  delete self;
}

//  a std::unique_ptr<QLayoutItem> a ritual of QDockAreaLayoutInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayoutInfo__std_unique_ptr_QLayoutItem(
    std::unique_ptr<QLayoutItem> *self) {
  delete self;
}

//  a QSet<QWidget *> a ritual of QDockAreaLayoutInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayoutInfo__QSet_QWidget(QSet<QWidget *> *self) {
  delete self;
}

//  a QSet<QTabBar *> a ritual of QDockAreaLayoutInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayoutInfo__QSet_QTabBar(QSet<QTabBar *> *self) {
  delete self;
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
