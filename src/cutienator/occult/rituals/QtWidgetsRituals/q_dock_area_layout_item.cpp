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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qdockarealayout.cpp, line 246, as local:qdockarealayout.cpp:tabId
#if QT_CONFIG(tabbar)
static quintptr tabId(const QDockAreaLayoutItem &item)
{
    if (item.widgetItem == nullptr)
        return 0;
    return reinterpret_cast<quintptr>(item.widgetItem->widget());
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 307, as _ZNK19QDockAreaLayoutInfo11minimumSizeEv
inline QSize QDockAreaLayoutInfo::minimumSize() const
{
    if (isEmpty())
        return QSize(0, 0);

    int a = 0, b = 0;
    bool first = true;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

        QSize min_size = item.minimumSize();
#if QT_CONFIG(tabbar)
        if (tabbed) {
            a = qMax(a, pick(o, min_size));
        } else
#endif
        {
            if (!first)
                a += *sep;
            a += pick(o, min_size);
        }
        b = qMax(b, perp(o, min_size));

        first = false;
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

#if QT_CONFIG(tabbar)
    QSize tbm = tabBarMinimumSize();
    if (!tbm.isNull()) {
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::RoundedSouth:
            case QTabBar::TriangularNorth:
            case QTabBar::TriangularSouth:
                result.rheight() += tbm.height();
                result.rwidth() = qMax(tbm.width(), result.width());
                break;
            case QTabBar::RoundedEast:
            case QTabBar::RoundedWest:
            case QTabBar::TriangularEast:
            case QTabBar::TriangularWest:
                result.rheight() = qMax(tbm.height(), result.height());
                result.rwidth() += tbm.width();
                break;
            default:
                break;
        }
    }
#endif // QT_CONFIG(tabbar)

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 366, as _ZNK19QDockAreaLayoutInfo11maximumSizeEv
inline QSize QDockAreaLayoutInfo::maximumSize() const
{
    if (isEmpty())
        return QSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX);

    int a = 0, b = QWIDGETSIZE_MAX;
#if QT_CONFIG(tabbar)
    if (tabbed)
        a = QWIDGETSIZE_MAX;
#endif

    int min_perp = 0;

    bool first = true;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

        QSize max_size = item.maximumSize();
        min_perp = qMax(min_perp, perp(o, item.minimumSize()));

#if QT_CONFIG(tabbar)
        if (tabbed) {
            a = qMin(a, pick(o, max_size));
        } else
#endif
        {
            if (!first)
                a += *sep;
            a += pick(o, max_size);
        }
        b = qMin(b, perp(o, max_size));

        a = qMin(a, int(QWIDGETSIZE_MAX));
        b = qMin(b, int(QWIDGETSIZE_MAX));

        first = false;
    }

    b = qMax(b, min_perp);

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

#if QT_CONFIG(tabbar)
    QSize tbh = tabBarSizeHint();
    if (!tbh.isNull()) {
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::RoundedSouth:
                result.rheight() += tbh.height();
                break;
            case QTabBar::RoundedEast:
            case QTabBar::RoundedWest:
                result.rwidth() += tbh.width();
                break;
            default:
                break;
        }
    }
#endif // QT_CONFIG(tabbar)

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 433, as _ZNK19QDockAreaLayoutInfo8sizeHintEv
inline QSize QDockAreaLayoutInfo::sizeHint() const
{
    if (isEmpty())
        return QSize(0, 0);

    int a = 0, b = 0;
    int min_perp = 0;
    int max_perp = QWIDGETSIZE_MAX;
    const QDockAreaLayoutItem *previous = nullptr;
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

        bool gap = item.flags & QDockAreaLayoutItem::GapItem;

        QSize size_hint = item.sizeHint();
        min_perp = qMax(min_perp, perp(o, item.minimumSize()));
        max_perp = qMin(max_perp, perp(o, item.maximumSize()));

#if QT_CONFIG(tabbar)
        if (tabbed) {
            a = qMax(a, gap ? item.size : pick(o, size_hint));
        } else
#endif
        {
            if (previous && !gap && !(previous->flags &  QDockAreaLayoutItem::GapItem)
                && !previous->hasFixedSize(o)) {
                a += *sep;
            }
            a += gap ? item.size : pick(o, size_hint);
        }
        b = qMax(b, perp(o, size_hint));

        previous = &item;
    }

    max_perp = qMax(max_perp, min_perp);
    b = qMax(b, min_perp);
    b = qMin(b, max_perp);

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

#if QT_CONFIG(tabbar)
    if (tabbed) {
        QSize tbh = tabBarSizeHint();
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::RoundedSouth:
            case QTabBar::TriangularNorth:
            case QTabBar::TriangularSouth:
                result.rheight() += tbh.height();
                result.rwidth() = qMax(tbh.width(), result.width());
                break;
            case QTabBar::RoundedEast:
            case QTabBar::RoundedWest:
            case QTabBar::TriangularEast:
            case QTabBar::TriangularWest:
                result.rheight() = qMax(tbh.height(), result.height());
                result.rwidth() += tbh.width();
                break;
            default:
                break;
        }
    }
#endif // QT_CONFIG(tabbar)

    return result;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2319, as _ZNK19QDockAreaLayoutInfo17tabBarMinimumSizeEv
#if QT_CONFIG(tabbar)
inline QSize QDockAreaLayoutInfo::tabBarMinimumSize() const
{
    if (!updateTabBar())
        return QSize(0, 0);

    return tabBar->minimumSizeHint();
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 292, as _ZNK19QDockAreaLayoutInfo7isEmptyEv
inline bool QDockAreaLayoutInfo::isEmpty() const
{
    return next(-1) == -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2327, as _ZNK19QDockAreaLayoutInfo14tabBarSizeHintEv
#if QT_CONFIG(tabbar)
inline QSize QDockAreaLayoutInfo::tabBarSizeHint() const
{
    if (!updateTabBar())
        return QSize(0, 0);

    return tabBar->sizeHint();
}
#endif  // QT_CONFIG(tabbar)

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1719, as _ZNK19QDockAreaLayoutInfo4nextEi
inline int QDockAreaLayoutInfo::next(int index) const
{
    for (int i = index + 1; i < item_list.size(); ++i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 65, as _ZN19QDockAreaLayoutItemC1EP11QLayoutItem
inline QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem *_widgetItem)
    : widgetItem(_widgetItem), subinfo(nullptr), placeHolderItem(nullptr), pos(0), size(-1), flags(NoFlags)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 70, as _ZN19QDockAreaLayoutItemC1EP19QDockAreaLayoutInfo
inline QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutInfo *_subinfo)
    : widgetItem(nullptr), subinfo(_subinfo), placeHolderItem(nullptr), pos(0), size(-1), flags(NoFlags)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 75, as _ZN19QDockAreaLayoutItemC1EP16QPlaceHolderItem
inline QDockAreaLayoutItem::QDockAreaLayoutItem(QPlaceHolderItem *_placeHolderItem)
    : widgetItem(nullptr), subinfo(nullptr), placeHolderItem(_placeHolderItem), pos(0), size(-1), flags(NoFlags)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 80, as _ZN19QDockAreaLayoutItemC1ERKS_
inline QDockAreaLayoutItem::QDockAreaLayoutItem(const QDockAreaLayoutItem &other)
    : widgetItem(other.widgetItem), subinfo(nullptr), placeHolderItem(nullptr), pos(other.pos),
        size(other.size), flags(other.flags)
{
    if (other.subinfo != nullptr)
        subinfo = new QDockAreaLayoutInfo(*other.subinfo);
    else if (other.placeHolderItem != nullptr)
        placeHolderItem = new QPlaceHolderItem(*other.placeHolderItem);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 162, as _ZN19QDockAreaLayoutItemaSERKS_
inline QDockAreaLayoutItem
    &QDockAreaLayoutItem::operator = (const QDockAreaLayoutItem &other)
{
    if (this == &other)
        return *this;

    widgetItem = other.widgetItem;
    delete subinfo;
    if (other.subinfo == nullptr)
        subinfo = nullptr;
    else
        subinfo = new QDockAreaLayoutInfo(*other.subinfo);

    delete placeHolderItem;
    if (other.placeHolderItem == nullptr)
        placeHolderItem = nullptr;
    else
        placeHolderItem = new QPlaceHolderItem(*other.placeHolderItem);

    pos = other.pos;
    size = other.size;
    flags = other.flags;

    return *this;
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
//  -----------------------------------------------------------------------

//  QDockAreaLayoutItem::QDockAreaLayoutItem(QLayoutItem *_widgetItem)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1EP11QLayoutItem(
    QLayoutItem *_widgetItem) {
  return new QDockAreaLayoutItem(_widgetItem);
}

//  QDockAreaLayoutItem::QDockAreaLayoutItem(QDockAreaLayoutInfo *_subinfo)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1EP19QDockAreaLayoutInfo(
    QDockAreaLayoutInfo *_subinfo) {
  return new QDockAreaLayoutItem(_subinfo);
}

//  QDockAreaLayoutItem::QDockAreaLayoutItem(QPlaceHolderItem
//      *_placeHolderItem)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1EP16QPlaceHolderItem(
    QPlaceHolderItem *_placeHolderItem) {
  return new QDockAreaLayoutItem(_placeHolderItem);
}

//  QDockAreaLayoutItem::QDockAreaLayoutItem(const QDockAreaLayoutItem
//      &other)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemC1ERKS_(
    const QDockAreaLayoutItem *other) {
  return new QDockAreaLayoutItem(*other);
}

//  QDockAreaLayoutItem::~QDockAreaLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutItemD1Ev(QDockAreaLayoutItem *self) {
  delete self;
}

//  QDockAreaLayoutItem &QDockAreaLayoutItem::operator=(const
//      QDockAreaLayoutItem &other)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutItem *ritual_ZN19QDockAreaLayoutItemaSERKS_(
    QDockAreaLayoutItem *self,
    const QDockAreaLayoutItem *other) {
  return &(self->operator=(*other));
}

//  bool QDockAreaLayoutItem::skip() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutItem4skipEv(
    const QDockAreaLayoutItem *self) {
  return self->skip();
}

//  bool QDockAreaLayoutItem::expansive(Qt::Orientation o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutItem9expansiveEN2Qt11OrientationE(
    const QDockAreaLayoutItem *self,
    Qt::Orientation o) {
  return self->expansive(o);
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
