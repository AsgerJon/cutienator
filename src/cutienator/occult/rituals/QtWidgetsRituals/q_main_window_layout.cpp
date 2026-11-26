//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qwidgetanimator_p.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(mainwindow)
#include <QtWidgets/private/qmainwindowlayout_p.h>
#endif
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
#include <QtWidgets/QWidgetItem>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QStyleOption>
#include <QtWidgets/QApplication>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtoolbararealayout_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbar_p.h>
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
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#include <QtWidgets/qmenu.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmath.h>
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/private/qtoolbarextension_p.h>
#endif
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbarseparator_p.h>
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

//  from src/widgets/widgets/qdockwidget.cpp, line 39, as local:qdockwidget.cpp:mainwindow_from_dock
static const QMainWindow *mainwindow_from_dock(const QDockWidget *dock)
{
    for (const QWidget *p = dock->parentWidget(); p; p = p->parentWidget()) {
        if (const QMainWindow *window = qobject_cast<const QMainWindow*>(p))
            return window;
    }
    return nullptr;
}

//  from src/widgets/widgets/qdockwidget.cpp, line 54, as local:qdockwidget.cpp:hasFeature
static inline bool hasFeature(const QDockWidgetPrivate *priv, QDockWidget::DockWidgetFeature feature)
{ return (priv->features & feature) == feature; }

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 73, as local:qmainwindowlayout.cpp:toAnimationRule
static constexpr QWidgetAnimator::AnimationRule toAnimationRule(QMainWindow::DockOptions options)
{
    return options.testFlag(QMainWindow::AnimatedDocks) ? QWidgetAnimator::AnimationRule::Run
                                                        : QWidgetAnimator::AnimationRule::Stop;
}

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

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1496, as local:qmainwindowlayout.cpp:validateToolBarArea
#if QT_CONFIG(toolbar)
static constexpr Qt::ToolBarArea validateToolBarArea(Qt::ToolBarArea area)
{
    switch (area) {
    case Qt::LeftToolBarArea:
    case Qt::RightToolBarArea:
    case Qt::TopToolBarArea:
    case Qt::BottomToolBarArea:
        return area;
    default:
        break;
    }
    return Qt::TopToolBarArea;
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1510, as local:qmainwindowlayout.cpp:toDockPos
#if QT_CONFIG(toolbar)
static QInternal::DockPosition toDockPos(Qt::ToolBarArea area)
{
    switch (area) {
        case Qt::LeftToolBarArea: return QInternal::LeftDock;
        case Qt::RightToolBarArea: return QInternal::RightDock;
        case Qt::TopToolBarArea: return QInternal::TopDock;
        case Qt::BottomToolBarArea: return QInternal::BottomDock;
        default:
            break;
    }

    return QInternal::DockCount;
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1723, as local:qmainwindowlayout.cpp:toDockWidgetArea
#if QT_CONFIG(dockwidget)
inline static Qt::DockWidgetArea toDockWidgetArea(int pos)
{
    return QDockWidgetPrivate::toDockWidgetArea(static_cast<QInternal::DockPosition>(pos));
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1833, as local:qmainwindowlayout.cpp:tabwidgetPositionToTabBarShape
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget) && QT_CONFIG(tabwidget)
static QTabBar::Shape tabwidgetPositionToTabBarShape(QDockWidget *w)
{
    switch (static_cast<QDockWidgetPrivate *>(qt_widget_private(w))->tabPosition) {
    case QTabWidget::North:
        return QTabBar::RoundedNorth;
    case QTabWidget::South:
        return QTabBar::RoundedSouth;
    case QTabWidget::West:
        return QTabBar::RoundedWest;
    case QTabWidget::East:
        return QTabBar::RoundedEast;
    }
    Q_UNREACHABLE_RETURN(QTabBar::RoundedSouth);
}
#endif  // QT_CONFIG(dockwidget) && QT_CONFIG(tabwidget)
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

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2620, as local:qmainwindowlayout.cpp:fixToolBarOrientation
static void fixToolBarOrientation(QLayoutItem *item, int dockPos)
{
#if QT_CONFIG(toolbar)
    QToolBar *toolBar = qobject_cast<QToolBar*>(item->widget());
    if (toolBar == nullptr)
        return;

    QRect oldGeo = toolBar->geometry();

    QInternal::DockPosition pos
        = static_cast<QInternal::DockPosition>(dockPos);
    Qt::Orientation o = pos == QInternal::TopDock || pos == QInternal::BottomDock
                        ? Qt::Horizontal : Qt::Vertical;
    if (o != toolBar->orientation())
        toolBar->setOrientation(o);

    QSize hint = toolBar->sizeHint().boundedTo(toolBar->maximumSize())
                    .expandedTo(toolBar->minimumSize());

    if (toolBar->size() != hint) {
        QRect newGeo(oldGeo.topLeft(), hint);
        if (toolBar->layoutDirection() == Qt::RightToLeft)
            newGeo.moveRight(oldGeo.right());
        toolBar->setGeometry(newGeo);
    }

#else
    Q_UNUSED(item);
    Q_UNUSED(dockPos);
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2979, as local:qmainwindowlayout.cpp:unplugGroup
#if QT_CONFIG(dockwidget) && QT_CONFIG(tabwidget)
static bool unplugGroup(QMainWindowLayout *layout, QLayoutItem **item,
                        QDockAreaLayoutItem &parentItem)
{
    if (!parentItem.subinfo || !parentItem.subinfo->tabbed)
        return false;

    // The QDockWidget is part of a group of tab and we need to unplug them all.
    QDockWidgetGroupWindow *floatingTabs = layout->createTabbedDockWindow();
    QDockAreaLayoutInfo *info = floatingTabs->layoutInfo();
    *info = std::move(*parentItem.subinfo);
    delete parentItem.subinfo;
    parentItem.subinfo = nullptr;
    floatingTabs->setGeometry(info->rect.translated(layout->parentWidget()->pos()));
    floatingTabs->show();
    floatingTabs->raise();
    *item = new QDockWidgetGroupWindowItem(floatingTabs);
    parentItem.widgetItem = *item;
    return true;
}
#endif  // QT_CONFIG(dockwidget) && QT_CONFIG(tabwidget)

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 308, as local:qtoolbarlayout.cpp:defaultWidgetAction
static bool defaultWidgetAction(QToolBarItem *item)
{
    QWidgetAction *a = qobject_cast<QWidgetAction*>(item->action);
    return a != nullptr && a->defaultWidget() == item->widget();
}

//  from src/widgets/widgets/qwidgetanimator.cpp, line 18, as _ZN15QWidgetAnimatorC1EP17QMainWindowLayout
inline QWidgetAnimator::QWidgetAnimator(QMainWindowLayout *layout)
#if QT_CONFIG(mainwindow)
: m_mainWindowLayout(layout)
#endif
{
    Q_UNUSED(layout);
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2581, as _ZN17QMainWindowLayout10invalidateEv
inline void QMainWindowLayout::invalidate()
{
    QLayout::invalidate();
    minSize = szHint = QSize();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2547, as _ZN17QMainWindowLayout10timerEventEP11QTimerEvent
inline void QMainWindowLayout::timerEvent(QTimerEvent *e)
{
    if (e->timerId() == discardRestoredStateTimer.timerId()) {
        discardRestoredStateTimer.stop();
        restoredState.reset();
    }
    QLayout::timerEvent(e);
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1081, as _ZNK22QMainWindowLayoutState13centralWidgetEv
inline QWidget *QMainWindowLayoutState::centralWidget() const
{
    QLayoutItem *item = nullptr;

#if QT_CONFIG(dockwidget)
    item = dockAreaLayout.centralWidgetItem;
#else
    item = centralWidgetItem;
#endif

    if (item != nullptr)
        return item->widget();
    return nullptr;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1065, as _ZN22QMainWindowLayoutState16setCentralWidgetEP7QWidget
inline void QMainWindowLayoutState::setCentralWidget(QWidget *widget)
{
    QLayoutItem *item = nullptr;
    //make sure we remove the widget
    deleteCentralWidgetItem();

    if (widget != nullptr)
        item = new QWidgetItemV2(widget);

#if QT_CONFIG(dockwidget)
    dockAreaLayout.centralWidgetItem = item;
#else
    centralWidgetItem = item;
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1202, as _ZNK22QMainWindowLayoutState7isValidEv
inline bool QMainWindowLayoutState::isValid() const
{
    return rect.isValid();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 789, as _ZN18QToolBarAreaLayout18insertToolBarBreakEP8QToolBar
inline void QToolBarAreaLayout::insertToolBarBreak(QToolBar *before)
{
    if (auto pos = findToolBar(before))
        docks[*pos].insertToolBarBreak(before);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 795, as _ZN18QToolBarAreaLayout18removeToolBarBreakEP8QToolBar
inline void QToolBarAreaLayout::removeToolBarBreak(QToolBar *before)
{
    if (auto pos = findToolBar(before))
        docks[*pos].removeToolBarBreak(before);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 757, as _ZNK18QToolBarAreaLayout11findToolBarEPK8QToolBar
inline std::optional<QInternal::DockPosition> QToolBarAreaLayout::findToolBar(const QToolBar *toolBar) const
{
    for (std::size_t i = 0; i < docks.size(); ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];
        for (const auto &line : dock.lines) {
            for (const auto &item : line.toolBarItems) {
                if (item.widgetItem->widget() == toolBar)
                    return static_cast<QInternal::DockPosition>(i);
            }
        }
    }
    return {};
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 889, as _ZNK18QToolBarAreaLayout12toolBarBreakEP8QToolBar
inline bool QToolBarAreaLayout::toolBarBreak(QToolBar *toolBar) const
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if (line.toolBarItems.at(k).widgetItem->widget() == toolBar)
                    return j > 0 && k == 0;
            }
        }
    }

    return false;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 907, as _ZNK18QToolBarAreaLayout18getStyleOptionInfoEP19QStyleOptionToolBarP8QToolBar
inline void QToolBarAreaLayout::getStyleOptionInfo(QStyleOptionToolBar *option, QToolBar *toolBar) const
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if (line.toolBarItems.at(k).widgetItem->widget() == toolBar) {
                    if (line.toolBarItems.size() == 1)
                        option->positionWithinLine = QStyleOptionToolBar::OnlyOne;
                    else if (k == 0)
                        option->positionWithinLine = QStyleOptionToolBar::Beginning;
                    else if (k == line.toolBarItems.size() - 1)
                        option->positionWithinLine = QStyleOptionToolBar::End;
                    else
                        option->positionWithinLine = QStyleOptionToolBar::Middle;

                    if (dock.lines.size() == 1)
                        option->positionOfLine = QStyleOptionToolBar::OnlyOne;
                    else if (j == 0)
                        option->positionOfLine = QStyleOptionToolBar::Beginning;
                    else if (j == dock.lines.size() - 1)
                        option->positionOfLine = QStyleOptionToolBar::End;
                    else
                        option->positionOfLine = QStyleOptionToolBar::Middle;

                    return;
                }
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 678, as _ZNK18QToolBarAreaLayout8rectHintERK5QRect
inline QRect QToolBarAreaLayout::rectHint(const QRect &r) const
{
    int coef = visible ? 1 : -1;

    QRect result = r;

    QSize left_hint = docks[QInternal::LeftDock].sizeHint();
    QSize right_hint = docks[QInternal::RightDock].sizeHint();
    QSize top_hint = docks[QInternal::TopDock].sizeHint();
    QSize bottom_hint = docks[QInternal::BottomDock].sizeHint();

    result.adjust(-left_hint.width()*coef, -top_hint.height()*coef,
                    right_hint.width()*coef, bottom_hint.height()*coef);

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 806, as _ZN18QToolBarAreaLayout11moveToolBarEP8QToolBari
inline void QToolBarAreaLayout::moveToolBar(QToolBar *toolbar, int p)
{
    if (auto pos = findToolBar(toolbar))
        docks[*pos].moveToolBar(toolbar, p);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3322, as _ZN15QDockAreaLayout15splitDockWidgetEP11QDockWidgetS1_N2Qt11OrientationE
inline void QDockAreaLayout::splitDockWidget(QDockWidget *after,
                                               QDockWidget *dockWidget,
                                               Qt::Orientation orientation)
{
    const QList<int> path = indexOf(after);
    if (path.isEmpty())
        return;

    QDockAreaLayoutInfo *info = this->info(path);
    Q_ASSERT(info != nullptr);
    info->split(path.last(), orientation, new QDockWidgetItem(dockWidget));

    removePlaceHolder(dockWidget->objectName());
}

//  from src/widgets/widgets/qdockwidget.cpp, line 875, as _ZN18QDockWidgetPrivate16toDockWidgetAreaEN9QInternal12DockPositionE
inline Qt::DockWidgetArea QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)
{
    switch (pos) {
    case QInternal::LeftDock:   return Qt::LeftDockWidgetArea;
    case QInternal::RightDock:  return Qt::RightDockWidgetArea;
    case QInternal::TopDock:    return Qt::TopDockWidgetArea;
    case QInternal::BottomDock: return Qt::BottomDockWidgetArea;
    default: break;
    }
    return Qt::NoDockWidgetArea;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2534, as _ZNK15QDockAreaLayout7indexOfEPK7QWidget
inline QList<int> QDockAreaLayout::indexOf(const QWidget *dockWidget) const
{
    for (std::size_t i = 0; i < docks.size(); ++i) {
        QList<int> result = docks[i].indexOf(dockWidget);
        if (!result.isEmpty()) {
            result.prepend(int(i));
            return result;
        }
    }
    return QList<int>();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3184, as _ZN15QDockAreaLayout17restoreDockWidgetEP11QDockWidget
inline bool QDockAreaLayout::restoreDockWidget(QDockWidget *dockWidget)
{
    QDockAreaLayoutItem *item = nullptr;
    const auto groups =
            mainWindow->findChildren<QDockWidgetGroupWindow *>(Qt::FindDirectChildrenOnly);
    for (QDockWidgetGroupWindow *dwgw : groups) {
        QList<int> index = dwgw->layoutInfo()->indexOfPlaceHolder(dockWidget->objectName());
        if (!index.isEmpty()) {
            dockWidget->setParent(dwgw);
            item = const_cast<QDockAreaLayoutItem *>(&dwgw->layoutInfo()->item(index));
            break;
        }
    }
    if (!item) {
        QList<int> index = indexOfPlaceHolder(dockWidget->objectName());
        if (index.isEmpty())
            return false;
        item = const_cast<QDockAreaLayoutItem *>(&this->item(index));
    }

    QPlaceHolderItem *placeHolder = item->placeHolderItem;
    Q_ASSERT(placeHolder != nullptr);

    item->widgetItem = new QDockWidgetItem(dockWidget);

    if (placeHolder->window) {
        const QRect r = constrainedRect(placeHolder->topLevelRect, dockWidget);
        dockWidget->d_func()->setWindowState(QDockWidgetPrivate::WindowStates(
                                            {QDockWidgetPrivate::WindowState::Floating,
                                             QDockWidgetPrivate::WindowState::Unplug}), r);
    }
    dockWidget->setVisible(!placeHolder->hidden);

    item->placeHolderItem = nullptr;
    delete placeHolder;

    return true;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2200, as _ZN19QDockAreaLayoutInfo15reparentWidgetsEP7QWidget
#if QT_CONFIG(tabbar)
inline void QDockAreaLayoutInfo::reparentWidgets(QWidget *parent)
{
    if (tabBar)
        tabBar->setParent(parent);

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.flags & QDockAreaLayoutItem::GapItem)
            continue;
        if (item.subinfo)
            item.subinfo->reparentWidgets(parent);
        if (item.widgetItem) {
            QWidget *w = item.widgetItem->widget();
            if (qobject_cast<QDockWidgetGroupWindow *>(w))
                continue;
            if (w->parent() != parent) {
                bool hidden = w->isHidden();
                w->setParent(parent, w->windowFlags());
                if (!hidden)
                    w->show();
            }
        }
    }
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1854, as _ZN19QDockAreaLayoutInfo20deleteAllLayoutItemsEv
inline void QDockAreaLayoutInfo::deleteAllLayoutItems()
{
    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item= item_list[i];
        if (item.subinfo) {
            item.subinfo->deleteAllLayoutItems();
        } else {
            delete item.widgetItem;
            item.widgetItem = nullptr;
        }
    }
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1557, as _ZN19QDockAreaLayoutInfo5applyEN15QWidgetAnimator13AnimationRuleE
inline QDockWidget *QDockAreaLayoutInfo::apply(QWidgetAnimator::AnimationRule rule)
{
    QWidgetAnimator &widgetAnimator = mainWindowLayout()->widgetAnimator;

#if QT_CONFIG(tabbar)
    if (tabbed) {
        QRect tab_rect;
        QSize tbh = tabBarSizeHint();

        if (!tbh.isNull()) {
            switch (tabBarShape) {
                case QTabBar::RoundedNorth:
                case QTabBar::TriangularNorth:
                    tab_rect = QRect(rect.left(), rect.top(), rect.width(), tbh.height());
                    break;
                case QTabBar::RoundedSouth:
                case QTabBar::TriangularSouth:
                    tab_rect = QRect(rect.left(), rect.bottom() - tbh.height() + 1,
                                        rect.width(), tbh.height());
                    break;
                case QTabBar::RoundedEast:
                case QTabBar::TriangularEast:
                    tab_rect = QRect(rect.right() - tbh.width() + 1, rect.top(),
                                        tbh.width(), rect.height());
                    break;
                case QTabBar::RoundedWest:
                case QTabBar::TriangularWest:
                    tab_rect = QRect(rect.left(), rect.top(),
                                        tbh.width(), rect.height());
                    break;
                default:
                    break;
            }
        }

        widgetAnimator.animate(tabBar, tab_rect, rule);
    }
#endif // QT_CONFIG(tabbar)

    QDockWidget *activated = nullptr;

    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item = item_list[i];

        if (item.flags & QDockAreaLayoutItem::GapItem)
            continue;

        if (item.subinfo != nullptr) {
            item.subinfo->apply(rule);
            continue;
        }

        if (item.skip())
            continue;

        Q_ASSERT(item.widgetItem);
        QRect r = itemRect(i);
        QWidget *w = item.widgetItem->widget();

        QRect geo = w->geometry();
        widgetAnimator.animate(w, r, rule);
        if (!w->isHidden() && w->window()->isVisible()) {
            QDockWidget *dw = qobject_cast<QDockWidget*>(w);
            if (!r.isValid() && geo.right() >= 0 && geo.bottom() >= 0) {
                dw->lower();
                emit dw->visibilityChanged(false);
            } else if (r.isValid()
                        && (geo.right() < 0 || geo.bottom() < 0)) {
                emit dw->visibilityChanged(true);
                activated = dw;
            }
        }
    }
#if QT_CONFIG(tabbar)
    if (*sep == 1)
        updateSeparatorWidgets();
#endif // QT_CONFIG(tabbar)

    return activated;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3567, as _ZN15QDockAreaLayout8keepSizeEP11QDockWidget
inline void QDockAreaLayout::keepSize(QDockWidget *w)
{
    QList<int> path = indexOf(w);
    if (path.isEmpty())
        return;
    QDockAreaLayoutItem &item = this->item(path);
    if (item.size != -1)
        item.flags |= QDockAreaLayoutItem::KeepSize;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1297, as _ZNK22QMainWindowLayoutState9saveStateER11QDataStream
inline void QMainWindowLayoutState::saveState(QDataStream &stream) const
{
#if QT_CONFIG(dockwidget)
    dockAreaLayout.saveState(stream);
#if QT_CONFIG(tabbar)
    const QList<QDockWidgetGroupWindow *> floatingTabs =
        mainWindow->findChildren<QDockWidgetGroupWindow *>(Qt::FindDirectChildrenOnly);

    for (QDockWidgetGroupWindow *floating : floatingTabs) {
        if (floating->layoutInfo()->isEmpty())
            continue;
        stream << StateMarkers::FloatingDockWidgetTab;
        stream << floating->geometry();
        floating->layoutInfo()->saveState(stream);
    }
#endif
#endif
#if QT_CONFIG(toolbar)
    toolBarAreaLayout.saveState(stream);
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 3353, as _ZN17QMainWindowLayout10applyStateER22QMainWindowLayoutStateb
inline void QMainWindowLayout::applyState(QMainWindowLayoutState &newState, bool animate)
{
    // applying the state can lead to showing separator widgets, which would lead to a re-layout
    // (even though the separator widgets are not really part of the layout)
    // break the loop
    if (isInApplyState)
        return;
    isInApplyState = true;
#if QT_CONFIG(dockwidget) && QT_CONFIG(tabwidget)
    QSet<QTabBar*> used = newState.dockAreaLayout.usedTabBars();
    const auto groups =
            parent()->findChildren<QDockWidgetGroupWindow*>(Qt::FindDirectChildrenOnly);
    for (QDockWidgetGroupWindow *dwgw : groups)
        used += dwgw->layoutInfo()->usedTabBars();

    const QSet<QTabBar*> retired = usedTabBars - used;
    usedTabBars = used;
    for (QTabBar *tab_bar : retired) {
        unuseTabBar(tab_bar);
    }

    if (sep == 1) {
        const QSet<QWidget*> usedSeps = newState.dockAreaLayout.usedSeparatorWidgets();
        const QSet<QWidget*> retiredSeps = usedSeparatorWidgets - usedSeps;
        usedSeparatorWidgets = usedSeps;
        for (QWidget *sepWidget : retiredSeps)
            delete sepWidget;
    }

    for (int i = 0; i < QInternal::DockCount; ++i)
        newState.dockAreaLayout.docks[i].reparentWidgets(parentWidget());

#endif // QT_CONFIG(dockwidget) && QT_CONFIG(tabwidget)
    const auto rule = animate ? toAnimationRule(dockOptions) : QWidgetAnimator::AnimationRule::Stop;
    newState.apply(rule);
    isInApplyState = false;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 958, as _ZN22QMainWindowLayoutState20deleteAllLayoutItemsEv
inline void QMainWindowLayoutState::deleteAllLayoutItems()
{
#if QT_CONFIG(toolbar)
    toolBarAreaLayout.deleteAllLayoutItems();
#endif

#if QT_CONFIG(dockwidget)
    dockAreaLayout.deleteAllLayoutItems();
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1187, as _ZN22QMainWindowLayoutState5clearEv
inline void QMainWindowLayoutState::clear()
{
#if QT_CONFIG(toolbar)
    toolBarAreaLayout.clear();
#endif

#if QT_CONFIG(dockwidget)
    dockAreaLayout.clear();
#else
    centralWidgetRect = QRect();
#endif

    rect = QRect();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 940, as _ZN22QMainWindowLayoutState9fitLayoutEv
inline void QMainWindowLayoutState::fitLayout()
{
    QRect r;
#if !QT_CONFIG(toolbar)
    r = rect;
#else
    toolBarAreaLayout.rect = rect;
    r = toolBarAreaLayout.fitLayout();
#endif // QT_CONFIG(toolbar)

#if QT_CONFIG(dockwidget)
    dockAreaLayout.rect = r;
    dockAreaLayout.fitLayout();
#else
    centralWidgetRect = r;
#endif
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 902, as _ZNK22QMainWindowLayoutState4fitsEv
inline bool QMainWindowLayoutState::fits() const
{
    Q_ASSERT(mainWindow);

    QSize size;

#if QT_CONFIG(dockwidget)
    size = dockAreaLayout.minimumStableSize();
#endif

#if QT_CONFIG(toolbar)
    size.rwidth() += toolBarAreaLayout.docks[QInternal::LeftDock].rect.width();
    size.rwidth() += toolBarAreaLayout.docks[QInternal::RightDock].rect.width();
    size.rheight() += toolBarAreaLayout.docks[QInternal::TopDock].rect.height();
    size.rheight() += toolBarAreaLayout.docks[QInternal::BottomDock].rect.height();
#endif

    return size.width() <= mainWindow->width() && size.height() <= mainWindow->height();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 3121, as _ZN17QMainWindowLayout18updateGapIndicatorEv
inline void QMainWindowLayout::updateGapIndicator()
{
#if QT_CONFIG(rubberband)
    if (!widgetAnimator.animating() && (!currentGapPos.isEmpty()
#if QT_CONFIG(dockwidget)
                                        || currentHoveredFloat
#endif
                                        )) {
        QWidget *expectedParent =
#if QT_CONFIG(dockwidget)
            currentHoveredFloat ? currentHoveredFloat.data() :
#endif
            parentWidget();
        if (!gapIndicator) {
            gapIndicator = new QRubberBand(QRubberBand::Rectangle, expectedParent);
            // For accessibility to identify this special widget.
            gapIndicator->setObjectName("qt_rubberband"_L1);
        } else if (gapIndicator->parent() != expectedParent) {
            gapIndicator->setParent(expectedParent);
        }

        // Prevent re-entry in case of size change
        const bool sigBlockState = gapIndicator->signalsBlocked();
        auto resetSignals = qScopeGuard([this, sigBlockState](){ gapIndicator->blockSignals(sigBlockState); });
        gapIndicator->blockSignals(true);

#if QT_CONFIG(dockwidget)
        if (currentHoveredFloat)
            gapIndicator->setGeometry(currentHoveredFloat->currentGapRect);
        else
#endif
            gapIndicator->setGeometry(currentGapRect);

        gapIndicator->show();
        gapIndicator->raise();

        // Reset signal state

    } else if (gapIndicator) {
        gapIndicator->hide();
    }

#endif // QT_CONFIG(rubberband)
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 394, as _ZN14QToolBarLayout13layoutActionsERK5QSize
inline bool QToolBarLayout::layoutActions(const QSize &size)
{
    if (dirty)
        updateGeomArray();

    QRect rect(0, 0, size.width(), size.height());

    QList<QWidget*> showWidgets, hideWidgets;

    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return false;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int handleExtent = movable()
            ? style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb) : 0;
    const QMargins margins = contentsMargins();
    const int spacing = this->spacing();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);
    Qt::Orientation o = tb->orientation();
    bool extensionMenuContainsOnlyWidgetActions = true;

    int space = pick(o, rect.size()) - pick(o, margins) - handleExtent;
    if (space <= 0)
        return false;  // nothing to do.

    if (popupMenu)
        popupMenu->clear();

    bool ranOutOfSpace = false;
    int rows = 0;
    int rowPos = perp(o, rect.topLeft()) + perp(o, QSize(margins.top(), margins.left()));
    int i = 0;
    while (i < items.size()) {
        QList<QLayoutStruct> a = geomArray;

        int start = i;
        int size = 0;
        int prev = -1;
        int rowHeight = 0;
        int count = 0;
        int maximumSize = 0;
        bool expansiveRow = false;
        for (; i < items.size(); ++i) {
            if (a[i].empty)
                continue;

            int newSize = size + (count == 0 ? 0 : spacing) + a[i].minimumSize;
            if (prev != -1 && newSize > space) {
                if (rows == 0)
                    ranOutOfSpace = true;
                // do we have to move the previous item to the next line to make space for
                // the extension button?
                if (count > 1 && size + spacing + extensionExtent > space)
                    i = prev;
                break;
            }

            if (expanded)
                rowHeight = qMax(rowHeight, perp(o, items.at(i)->sizeHint()));
            expansiveRow = expansiveRow || a[i].expansive;
            size = newSize;
            maximumSize += spacing + (a[i].expansive ? a[i].maximumSize : a[i].smartSizeHint());
            prev = i;
            ++count;
        }

        // stretch at the end
        a[i].sizeHint = 0;
        a[i].maximumSize = QWIDGETSIZE_MAX;
        a[i].minimumSize = 0;
        a[i].expansive = true;
        a[i].stretch = 0;
        a[i].empty = true;

        if (expansiveRow && maximumSize < space) {
            expansiveRow = false;
            a[i].maximumSize = space - maximumSize;
        }

        qGeomCalc(a, start, i - start + (expansiveRow ? 0 : 1), 0,
                    space - (ranOutOfSpace ? (extensionExtent + spacing) : 0),
                    spacing);

        for (int j = start; j < i; ++j) {
            QToolBarItem *item = items.at(j);

            if (a[j].empty) {
                if (!item->widget()->isHidden())
                    hideWidgets << item->widget();
                continue;
            }

            QPoint pos;
            rpick(o, pos) = pick(o, QSize(margins.top(), margins.left())) + handleExtent + a[j].pos;
            rperp(o, pos) = rowPos;
            QSize size;
            rpick(o, size) = a[j].size;
            if (expanded)
                rperp(o, size) = rowHeight;
            else
                rperp(o, size) = perp(o, rect.size()) - perp(o, margins);
            QRect r(pos, size);

            if (o == Qt::Horizontal)
                r = QStyle::visualRect(parentWidget()->layoutDirection(), rect, r);

            item->setGeometry(r);

            if (item->widget()->isHidden())
                showWidgets << item->widget();
        }

        if (!expanded) {
            for (int j = i; j < items.size(); ++j) {
                QToolBarItem *item = items.at(j);
                if (!item->widget()->isHidden())
                    hideWidgets << item->widget();
                if (popupMenu) {
                    if (!defaultWidgetAction(item)) {
                        popupMenu->addAction(item->action);
                        extensionMenuContainsOnlyWidgetActions = false;
                    }
                }
            }
            break;
        }

        rowPos += rowHeight + spacing;
        ++rows;
    }

    // if we are using a popup menu, not the expadning toolbar effect, we cannot move custom
    // widgets into the menu. If only custom widget actions are chopped off, the popup menu
    // is empty. So we show the little extension button to show something is chopped off,
    // but we make it disabled.
    extension->setEnabled(popupMenu == nullptr || !extensionMenuContainsOnlyWidgetActions);

    // we have to do the show/hide here, because it triggers more calls to setGeometry :(
    for (int i = 0; i < showWidgets.size(); ++i)
        showWidgets.at(i)->show();
    for (int i = 0; i < hideWidgets.size(); ++i)
        hideWidgets.at(i)->hide();

    return ranOutOfSpace;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2556, as _ZN17QMainWindowLayout7addItemEP11QLayoutItem
inline void QMainWindowLayout::addItem(QLayoutItem *)
{ qWarning("QMainWindowLayout::addItem: Please use the public QMainWindow API instead"); }

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2490, as _ZN17QMainWindowLayout11setGeometryERK5QRect
#if defined(Q_OS_LINUX)
inline void QMainWindowLayout::setGeometry(const QRect &_r)
{
    // Check if the state is valid, and avoid replacing it again if it is currently used
    // in applyState
    if (savedState.isValid() || (restoredState && isInApplyState))
        return;

    QRect r = _r;

    QLayout::setGeometry(r);

    if (statusbar) {
        QRect sbr(QPoint(r.left(), 0),
                  QSize(r.width(), statusbar->heightForWidth(r.width()))
                  .expandedTo(statusbar->minimumSize()));
        sbr.moveBottom(r.bottom());
        QRect vr = QStyle::visualRect(parentWidget()->layoutDirection(), _r, sbr);
        statusbar->setGeometry(vr);
        r.setBottom(sbr.top() - 1);
    }

    if (restoredState) {
        /*
            The main window was hidden and was going to be maximized or full-screened when
            the state was restored. The state might have been for a larger window size than
            the current size (in _r), and the window might still be in the process of being
            shown and transitioning to the final size (there's no reliable way of knowing
            this across different platforms). Try again with the restored state.
        */
        layoutState = *restoredState;
        if (restoredState->fits()) {
            restoredState.reset();
            discardRestoredStateTimer.stop();
        } else {
            /*
                Try again in the next setGeometry call, but discard the restored state
                after 150ms without any further tries. That's a reasonably short amount of
                time during which we can expect the windowing system to either have completed
                showing the window, or resized the window once more (which then restarts the
                timer in timerEvent).
                If the windowing system is done, then the user won't have had a chance to
                change the layout interactively AND trigger another resize.
            */
            discardRestoredStateTimer.start(150, this);
        }
    }

    layoutState.rect = r;

    layoutState.fitLayout();
    applyState(layoutState, false);

#if defined(Q_OS_MACOS)
    updateUnifiedToolBarArea();
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2410, as _ZNK17QMainWindowLayout6itemAtEi
inline QLayoutItem *QMainWindowLayout::itemAt(int index) const
{
    int x = 0;

    if (QLayoutItem *ret = layoutState.itemAt(index, &x))
        return ret;

    if (statusbar && x++ == index)
        return statusbar;

    return nullptr;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2423, as _ZN17QMainWindowLayout6takeAtEi
inline QLayoutItem *QMainWindowLayout::takeAt(int index)
{
    int x = 0;

    if (QLayoutItem *ret = layoutState.takeAt(index, &x)) {
        // the widget might in fact have been destroyed by now
        if (QWidget *w = ret->widget()) {
            widgetAnimator.abort(w);
            if (w == pluggingWidget)
                pluggingWidget = nullptr;
        }

        if (savedState.isValid() ) {
            //we need to remove the item also from the saved state to prevent crash
            savedState.remove(ret);
            //Also, the item may be contained several times as a gap item.
            layoutState.remove(ret);
        }

#if QT_CONFIG(toolbar)
        if (!currentGapPos.isEmpty() && currentGapPos.constFirst() == 0) {
            currentGapPos = layoutState.toolBarAreaLayout.currentGapIndex();
            if (!currentGapPos.isEmpty()) {
                currentGapPos.prepend(0);
                currentGapRect = layoutState.itemRect(currentGapPos);
            }
        }
#endif

        return ret;
    }

    if (statusbar && x++ == index) {
        QLayoutItem *ret = statusbar;
        statusbar = nullptr;
        return ret;
    }

    return nullptr;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2402, as _ZNK17QMainWindowLayout5countEv
inline int QMainWindowLayout::count() const
{
    int result = 0;
    while (itemAt(result))
        ++result;
    return result;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2559, as _ZNK17QMainWindowLayout8sizeHintEv
inline QSize QMainWindowLayout::sizeHint() const
{
    if (!szHint.isValid()) {
        szHint = layoutState.sizeHint();
        const QSize sbHint = statusbar ? statusbar->sizeHint() : QSize(0, 0);
        szHint = QSize(qMax(sbHint.width(), szHint.width()),
                        sbHint.height() + szHint.height());
    }
    return szHint;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2570, as _ZNK17QMainWindowLayout11minimumSizeEv
inline QSize QMainWindowLayout::minimumSize() const
{
    if (!minSize.isValid()) {
        minSize = layoutState.minimumSize();
        const QSize sbMin = statusbar ? statusbar->minimumSize() : QSize(0, 0);
        minSize = QSize(qMax(sbMin.width(), minSize.width()),
                        sbMin.height() + minSize.height());
    }
    return minSize;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 969, as _ZN22QMainWindowLayoutState23deleteCentralWidgetItemEv
inline void QMainWindowLayoutState::deleteCentralWidgetItem()
{
#if QT_CONFIG(dockwidget)
    delete dockAreaLayout.centralWidgetItem;
    dockAreaLayout.centralWidgetItem = nullptr;
#else
    delete centralWidgetItem;
    centralWidgetItem = 0;
#endif
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 310, as _ZN22QToolBarAreaLayoutInfo18insertToolBarBreakEP8QToolBar
inline void QToolBarAreaLayoutInfo::insertToolBarBreak(QToolBar *before)
{
    if (before == nullptr) {
        if (!lines.isEmpty() && lines.constLast().toolBarItems.isEmpty())
            return;
        lines.append(QToolBarAreaLayoutLine(o));
        return;
    }

    for (int j = 0; j < lines.size(); ++j) {
        QToolBarAreaLayoutLine &line = lines[j];

        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            if (line.toolBarItems.at(k).widgetItem->widget() == before) {
                if (k == 0)
                    return;

                QToolBarAreaLayoutLine newLine(o);
                newLine.toolBarItems = line.toolBarItems.mid(k);
                line.toolBarItems = line.toolBarItems.mid(0, k);
                lines.insert(j + 1, newLine);

                return;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 338, as _ZN22QToolBarAreaLayoutInfo18removeToolBarBreakEP8QToolBar
inline void QToolBarAreaLayoutInfo::removeToolBarBreak(QToolBar *before)
{
    for (int j = 0; j < lines.size(); ++j) {
        const QToolBarAreaLayoutLine &line = lines.at(j);

        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            if (line.toolBarItems.at(k).widgetItem->widget() == before) {
                if (k != 0)
                    return;
                if (j == 0)
                    return;

                lines[j - 1].toolBarItems += lines[j].toolBarItems;
                lines.removeAt(j);

                return;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 184, as _ZNK22QToolBarAreaLayoutInfo8sizeHintEv
inline QSize QToolBarAreaLayoutInfo::sizeHint() const
{
    int a = 0, b = 0;
    for (int i = 0; i < lines.size(); ++i) {
        const QToolBarAreaLayoutLine &l = lines.at(i);
        if (l.skip())
            continue;

        QSize hint = l.sizeHint();
        a = qMax(a, pick(o, hint));
        b += perp(o, hint);
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 359, as _ZN22QToolBarAreaLayoutInfo11moveToolBarEP8QToolBari
inline void QToolBarAreaLayoutInfo::moveToolBar(QToolBar *toolbar, int pos)
{
    if (dirty)
        fitLayout();

    dirty = true;

    if (o == Qt::Vertical)
        pos -= rect.top();

    //here we actually update the preferredSize for the line containing the toolbar so that we move it
    for (int j = 0; j < lines.size(); ++j) {
        QToolBarAreaLayoutLine &line = lines[j];

        int previousIndex = -1;
        int minPos = 0;
        for (int k = 0; k < line.toolBarItems.size(); ++k) {
            QToolBarAreaLayoutItem &current = line.toolBarItems[k];
            if (current.widgetItem->widget() == toolbar) {
                int newPos = current.pos;

                if (previousIndex >= 0) {
                    QToolBarAreaLayoutItem &previous = line.toolBarItems[previousIndex];
                    if (pos < current.pos) {
                        newPos = qMax(pos, minPos);
                    } else {
                        //we check the max value for the position (until everything at the right is "compressed")
                        int maxPos = pick(o, rect.size());
                        for(int l = k; l < line.toolBarItems.size(); ++l) {
                            const QToolBarAreaLayoutItem &item = line.toolBarItems.at(l);
                            if (!item.skip()) {
                                maxPos -= pick(o, item.minimumSize());
                            }
                        }
                        newPos = qMin(pos, maxPos);
                    }

                    //extra is the number of pixels to add to the previous toolbar
                    int extra = newPos - current.pos;

                    //we check if the previous is near its size hint
                    //in which case we try to stick to it
                    const int diff = pick(o, previous.sizeHint()) - (previous.size + extra);
                    if (qAbs(diff) < QApplication::startDragDistance()) {
                        //we stick to the default place and size
                        extra += diff;
                    }

                    //update for the current item
                    current.extendSize(line.o, -extra);

                    if (extra >= 0) {
                        previous.extendSize(line.o, extra);
                    } else {
                        //we need to push the toolbars on the left starting with previous
                        extra = -extra; // we just need to know the number of pixels
                        ///at this point we need to get extra pixels from the toolbars at the left
                        for(int l = previousIndex; l >=0; --l) {
                            QToolBarAreaLayoutItem &item = line.toolBarItems[l];
                            if (!item.skip()) {
                                const int minPreferredSize = pick(o, item.minimumSize());
                                const int margin =  item.size - minPreferredSize;
                                if (margin < extra) {
                                    item.resize(line.o, minPreferredSize);
                                    extra -= margin;
                                } else {
                                    item.extendSize(line.o, -extra);
                                    extra = 0;
                                }
                            }
                        }
                        Q_ASSERT(extra == 0);
                    }
                } else {
                    //the item is the first one, it should be at position 0
                }

                return;

            } else if (!current.skip()) {
                previousIndex = k;
                minPos += pick(o, current.minimumSize());
            }
        }
    }
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2772, as _ZN15QDockAreaLayout17removePlaceHolderERK7QString
inline void QDockAreaLayout::removePlaceHolder(const QString &name)
{
    QList<int> index = indexOfPlaceHolder(name);
    if (!index.isEmpty())
        remove(index);
    const auto groups =
            mainWindow->findChildren<QDockWidgetGroupWindow *>(Qt::FindDirectChildrenOnly);
    for (QDockWidgetGroupWindow *dwgw : groups) {
        index = dwgw->layoutInfo()->indexOfPlaceHolder(name);
        if (!index.isEmpty()) {
            dwgw->layoutInfo()->remove(index);
            dwgw->destroyOrHideIfEmpty();
        }
    }
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3163, as _ZN15QDockAreaLayout15constrainedRectE5QRectP7QWidget
inline QRect QDockAreaLayout::constrainedRect(QRect rect, QWidget* widget)
{
    QScreen *screen = nullptr;
    if (QGuiApplication::primaryScreen()->virtualSiblings().size() > 1)
        screen = QGuiApplication::screenAt(rect.topLeft());
    if (!screen)
        screen = widget->screen();

    const QRect screenRect = screen->geometry();
    if (screenRect.isValid()) {
        rect.setWidth(qMin(rect.width(), screenRect.width()));
        rect.setHeight(qMin(rect.height(), screenRect.height()));
        rect.moveLeft(qMax(rect.left(), screenRect.left()));
        rect.moveTop(qMax(rect.top(), screenRect.top()));
        rect.moveRight(qMin(rect.right(), screenRect.right()));
        rect.moveBottom(qMin(rect.bottom(), screenRect.bottom()));
    }

    return rect;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2684, as _ZN15QDockAreaLayout4itemERK5QListIiE
inline QDockAreaLayoutItem &QDockAreaLayout::item(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    return docks[index].item(path.mid(1));
}

//  from src/widgets/widgets/qdockwidget.cpp, line 569, as _ZN15QDockWidgetItemC1EP11QDockWidget
inline QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    : QWidgetItem(dockWidget)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1776, as _ZN19QDockAreaLayoutInfo4itemERK5QListIiE
inline QDockAreaLayoutItem &QDockAreaLayoutInfo::item(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    if (path.size() > 1) {
        const QDockAreaLayoutItem &item = item_list[index];
        Q_ASSERT(item.subinfo != nullptr);
        return item.subinfo->item(path.mid(1));
    }
    return item_list[index];
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3527, as _ZN15QDockAreaLayout20deleteAllLayoutItemsEv
inline void QDockAreaLayout::deleteAllLayoutItems()
{
    for (auto &dock : docks)
        dock.deleteAllLayoutItems();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3076, as _ZN15QDockAreaLayout5clearEv
inline void QDockAreaLayout::clear()
{
    for (auto &dock : docks)
        dock.clear();

    rect = QRect();
    centralWidgetRect = QRect();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3064, as _ZN15QDockAreaLayout9fitLayoutEv
inline void QDockAreaLayout::fitLayout()
{
    QList<QLayoutStruct> ver_struct_list(3);
    QList<QLayoutStruct> hor_struct_list(3);
    getGrid(&ver_struct_list, &hor_struct_list);

    qGeomCalc(ver_struct_list, 0, 3, rect.top(), rect.height(), sep);
    qGeomCalc(hor_struct_list, 0, 3, rect.left(), rect.width(), sep);

    setGrid(&ver_struct_list, &hor_struct_list);
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2295, as _ZN17QMainWindowLayout11unuseTabBarEP7QTabBar
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline void QMainWindowLayout::unuseTabBar(QTabBar *bar)
{
    Q_ASSERT(qobject_cast<QMainWindowTabBar *>(bar));
    bar->deleteLater();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 739, as _ZN18QToolBarAreaLayout20deleteAllLayoutItemsEv
inline void QToolBarAreaLayout::deleteAllLayoutItems()
{
    for (int i = 0; i < QInternal::DockCount; ++i) {
        QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            QToolBarAreaLayoutLine &line = dock.lines[j];

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                QToolBarAreaLayoutItem &item = line.toolBarItems[k];
                if (!item.gap)
                    delete item.widgetItem;
                item.widgetItem = nullptr;
            }
        }
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1056, as _ZN18QToolBarAreaLayout5clearEv
inline void QToolBarAreaLayout::clear()
{
    for (int i = 0; i < QInternal::DockCount; ++i)
        docks[i].clear();
    rect = QRect();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 602, as _ZN18QToolBarAreaLayout9fitLayoutEv
inline QRect QToolBarAreaLayout::fitLayout()
{
    if (!visible)
        return rect;

    QSize left_hint = docks[QInternal::LeftDock].sizeHint();
    QSize right_hint = docks[QInternal::RightDock].sizeHint();
    QSize top_hint = docks[QInternal::TopDock].sizeHint();
    QSize bottom_hint = docks[QInternal::BottomDock].sizeHint();

    QRect center = rect.adjusted(left_hint.width(), top_hint.height(),
                                    -right_hint.width(), -bottom_hint.height());

    docks[QInternal::TopDock].rect = QRect(rect.left(), rect.top(),
                                rect.width(), top_hint.height());
    docks[QInternal::LeftDock].rect = QRect(rect.left(), center.top(),
                                left_hint.width(), center.height());
    docks[QInternal::RightDock].rect = QRect(center.right() + 1, center.top(),
                                    right_hint.width(), center.height());
    docks[QInternal::BottomDock].rect = QRect(rect.left(), center.bottom() + 1,
                                    rect.width(), bottom_hint.height());

    docks[QInternal::TopDock].fitLayout();
    docks[QInternal::LeftDock].fitLayout();
    docks[QInternal::RightDock].fitLayout();
    docks[QInternal::BottomDock].fitLayout();

    return center;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 980, as _ZNK22QMainWindowLayoutState6itemAtEiPi
inline QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x) const
{
#if QT_CONFIG(toolbar)
    if (QLayoutItem *ret = toolBarAreaLayout.itemAt(x, index))
        return ret;
#endif

#if QT_CONFIG(dockwidget)
    if (QLayoutItem *ret = dockAreaLayout.itemAt(x, index))
        return ret;
#else
    if (centralWidgetItem  && (*x)++ == index)
        return centralWidgetItem;
#endif

    return nullptr;
}

//  from src/widgets/widgets/qwidgetanimator.cpp, line 26, as _ZN15QWidgetAnimator5abortEP7QWidget
inline void QWidgetAnimator::abort(QWidget *w)
{
#if QT_CONFIG(animation)
    QPropertyAnimation *anim = m_animation_map.take(w);
    if (anim)
        anim->stop();
#if QT_CONFIG(mainwindow)
    m_mainWindowLayout->animationFinished(w);
#endif
#else
    Q_UNUSED(w); //there is no animation to abort
#endif // animation
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 860, as _ZNK22QMainWindowLayoutState8sizeHintEv
inline QSize QMainWindowLayoutState::sizeHint() const
{

    QSize result(0, 0);

#if QT_CONFIG(dockwidget)
    result = dockAreaLayout.sizeHint();
#else
    if (centralWidgetItem)
        result = centralWidgetItem->sizeHint();
#endif

#if QT_CONFIG(toolbar)
    result = toolBarAreaLayout.sizeHint(result);
#endif // QT_CONFIG(toolbar)

    return result;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 879, as _ZNK22QMainWindowLayoutState11minimumSizeEv
inline QSize QMainWindowLayoutState::minimumSize() const
{
    QSize result(0, 0);

#if QT_CONFIG(dockwidget)
    result = dockAreaLayout.minimumSize();
#else
    if (centralWidgetItem)
        result = centralWidgetItem->minimumSize();
#endif

#if QT_CONFIG(toolbar)
    result = toolBarAreaLayout.minimumSize(result);
#endif // QT_CONFIG(toolbar)

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 66, as _ZN22QToolBarAreaLayoutLineC1EN2Qt11OrientationE
inline QToolBarAreaLayoutLine::QToolBarAreaLayoutLine(Qt::Orientation orientation)
    : o(orientation)
{
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 153, as _ZNK22QToolBarAreaLayoutLine4skipEv
inline bool QToolBarAreaLayoutLine::skip() const
{
    for (int i = 0; i < toolBarItems.size(); ++i) {
        if (!toolBarItems.at(i).skip())
            return false;
    }
    return true;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 71, as _ZNK22QToolBarAreaLayoutLine8sizeHintEv
inline QSize QToolBarAreaLayoutLine::sizeHint() const
{
    int a = 0, b = 0;
    for (int i = 0; i < toolBarItems.size(); ++i) {
        const QToolBarAreaLayoutItem &item = toolBarItems.at(i);
        if (item.skip())
            continue;

        QSize sh = item.sizeHint();
        a += item.preferredSize > 0 ? item.preferredSize : pick(o, sh);
        b = qMax(b, perp(o, sh));
    }

    QSize result;
    rpick(o, result) = a;
    rperp(o, result) = b;

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 224, as _ZN22QToolBarAreaLayoutInfo9fitLayoutEv
inline void QToolBarAreaLayoutInfo::fitLayout()
{
    dirty = false;

    int b = 0;

    bool reverse = dockPos == QInternal::RightDock || dockPos == QInternal::BottomDock;

    int i = reverse ? lines.size() - 1 : 0;
    for (;;) {
        if ((reverse && i < 0) || (!reverse && i == lines.size()))
            break;

        QToolBarAreaLayoutLine &l = lines[i];
        if (!l.skip()) {
            if (o == Qt::Horizontal) {
                l.rect.setLeft(rect.left());
                l.rect.setRight(rect.right());
                l.rect.setTop(b + rect.top());
                b += l.sizeHint().height();
                l.rect.setBottom(b - 1 + rect.top());
            } else {
                l.rect.setTop(rect.top());
                l.rect.setBottom(rect.bottom());
                l.rect.setLeft(b + rect.left());
                b += l.sizeHint().width();
                l.rect.setRight(b - 1 + rect.left());
            }

            l.fitLayout();
        }

        i += reverse ? -1 : 1;
    }
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 26, as _ZNK22QToolBarAreaLayoutItem11minimumSizeEv
inline QSize QToolBarAreaLayoutItem::minimumSize() const
{
    if (skip())
        return QSize(0, 0);
    return qSmartMinSize(static_cast<QWidgetItem*>(widgetItem));
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 55, as _ZNK22QToolBarAreaLayoutItem4skipEv
inline bool QToolBarAreaLayoutItem::skip() const
{
    if (gap)
        return false;
    return widgetItem == nullptr || widgetItem->isEmpty();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 33, as _ZNK22QToolBarAreaLayoutItem8sizeHintEv
inline QSize QToolBarAreaLayoutItem::sizeHint() const
{
    if (skip())
        return QSize(0, 0);

    return realSizeHint();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3494, as _ZNK15QDockAreaLayout6itemAtEPii
inline QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const
{
    Q_ASSERT(x != nullptr);

    for (const auto &dock : docks) {
        if (QLayoutItem *ret = dock.itemAt(x, index))
            return ret;
    }

    if (centralWidgetItem && (*x)++ == index)
        return centralWidgetItem;

    return nullptr;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 695, as _ZNK18QToolBarAreaLayout6itemAtEPii
inline QLayoutItem *QToolBarAreaLayout::itemAt(int *x, int index) const
{
    Q_ASSERT(x != nullptr);

    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if ((*x)++ == index)
                    return line.toolBarItems.at(k).widgetItem;
            }
        }
    }

    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3137, as _ZNK15QDockAreaLayout8sizeHintEv
inline QSize QDockAreaLayout::sizeHint() const
{
    return size_helper(&QDockAreaLayoutInfo::sizeHint, &QLayoutItem::sizeHint);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 655, as _ZNK18QToolBarAreaLayout8sizeHintERK5QSize
inline QSize QToolBarAreaLayout::sizeHint(const QSize &centerHint) const
{
    if (!visible)
        return centerHint;

    QSize result = centerHint;

    QSize left_hint = docks[QInternal::LeftDock].sizeHint();
    QSize right_hint = docks[QInternal::RightDock].sizeHint();
    QSize top_hint = docks[QInternal::TopDock].sizeHint();
    QSize bottom_hint = docks[QInternal::BottomDock].sizeHint();

    result.setWidth(qMax(top_hint.width(), result.width()));
    result.setWidth(qMax(bottom_hint.width(), result.width()));
    result.setHeight(qMax(left_hint.height(), result.height()));
    result.setHeight(qMax(right_hint.height(), result.height()));

    result.rwidth() += left_hint.width() + right_hint.width();
    result.rheight() += top_hint.height() + bottom_hint.height();

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3142, as _ZNK15QDockAreaLayout11minimumSizeEv
inline QSize QDockAreaLayout::minimumSize() const
{
    return size_helper(&QDockAreaLayoutInfo::minimumSize, &QLayoutItem::minimumSize);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 632, as _ZNK18QToolBarAreaLayout11minimumSizeERK5QSize
inline QSize QToolBarAreaLayout::minimumSize(const QSize &centerMin) const
{
    if (!visible)
        return centerMin;

    QSize result = centerMin;

    QSize left_min = docks[QInternal::LeftDock].minimumSize();
    QSize right_min = docks[QInternal::RightDock].minimumSize();
    QSize top_min = docks[QInternal::TopDock].minimumSize();
    QSize bottom_min = docks[QInternal::BottomDock].minimumSize();

    result.setWidth(qMax(top_min.width(), result.width()));
    result.setWidth(qMax(bottom_min.width(), result.width()));
    result.setHeight(qMax(left_min.height(), result.height()));
    result.setHeight(qMax(right_min.height(), result.height()));

    result.rwidth() += left_min.width() + right_min.width();
    result.rheight() += top_min.height() + bottom_min.height();

    return result;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 42, as _ZNK22QToolBarAreaLayoutItem12realSizeHintEv
inline QSize QToolBarAreaLayoutItem::realSizeHint() const
{
    QWidget *wid = widgetItem->widget();
    QSize s = wid->sizeHint().expandedTo(wid->minimumSizeHint());
    if (wid->sizePolicy().horizontalPolicy() == QSizePolicy::Ignored)
        s.setWidth(0);
    if (wid->sizePolicy().verticalPolicy() == QSizePolicy::Ignored)
        s.setHeight(0);
    s = s.boundedTo(wid->maximumSize())
        .expandedTo(wid->minimumSize());
    return s;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 111, as _ZN22QToolBarAreaLayoutLine9fitLayoutEv
inline void QToolBarAreaLayoutLine::fitLayout()
{
    int last = -1;
    int min = pick(o, minimumSize());
    int space = pick(o, rect.size());
    int extra = qMax(0, space - min);

    for (int i = 0; i < toolBarItems.size(); ++i) {
        QToolBarAreaLayoutItem &item = toolBarItems[i];
        if (item.skip())
            continue;

        if (QToolBarLayout *tblayout = qobject_cast<QToolBarLayout*>(item.widgetItem->widget()->layout()))
            tblayout->checkUsePopupMenu();

        const int itemMin = pick(o, item.minimumSize());
        //preferredSize is the default if it is set, otherwise, we take the sizehint
        item.size = item.preferredSize > 0 ? item.preferredSize : pick(o, item.sizeHint());

        //the extraspace is the space above the item minimum sizehint
        const int extraSpace = qMin(item.size - itemMin, extra);
        item.size = itemMin + extraSpace; //that is the real size

        extra -= extraSpace;

        last = i;
    }

    // calculate the positions from the sizes
    int pos = 0;
    for (int i = 0; i < toolBarItems.size(); ++i) {
        QToolBarAreaLayoutItem &item = toolBarItems[i];
        if (item.skip())
            continue;

        item.pos = pos;
        if (i == last) // stretch the last item to the end of the line
            item.size = qMax(0, pick(o, rect.size()) - item.pos);
        pos += item.size;
    }
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

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2914, as _ZN17QMainWindowLayoutD1Ev
inline QMainWindowLayout::~QMainWindowLayout()
{
    layoutState.deleteAllLayoutItems();
    layoutState.deleteCentralWidgetItem();

    delete statusbar;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2937, as _ZNK17QMainWindowLayout9statusBarEv
#if QT_CONFIG(statusbar)
inline QStatusBar *QMainWindowLayout::statusBar() const
{ return statusbar ? qobject_cast<QStatusBar *>(statusbar->widget()) : 0; }
#endif  // QT_CONFIG(statusbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2940, as _ZN17QMainWindowLayout12setStatusBarEP10QStatusBar
#if QT_CONFIG(statusbar)
inline void QMainWindowLayout::setStatusBar(QStatusBar *sb)
{
    if (sb)
        addChildWidget(sb);
    delete statusbar;
    statusbar = sb ? new QWidgetItemV2(sb) : nullptr;
    invalidate();
}
#endif  // QT_CONFIG(statusbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2950, as _ZNK17QMainWindowLayout13centralWidgetEv
inline QWidget *QMainWindowLayout::centralWidget() const
{
    return layoutState.centralWidget();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2955, as _ZN17QMainWindowLayout16setCentralWidgetEP7QWidget
inline void QMainWindowLayout::setCentralWidget(QWidget *widget)
{
    if (widget != nullptr)
        addChildWidget(widget);
    layoutState.setCentralWidget(widget);
    if (savedState.isValid()) {
#if QT_CONFIG(dockwidget)
        savedState.dockAreaLayout.centralWidgetItem = layoutState.dockAreaLayout.centralWidgetItem;
        savedState.dockAreaLayout.fallbackToSizeHints = true;
#else
        savedState.centralWidgetItem = layoutState.centralWidgetItem;
#endif
    }
    invalidate();
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1552, as _ZN17QMainWindowLayout18insertToolBarBreakEP8QToolBar
#if QT_CONFIG(toolbar)
inline void QMainWindowLayout::insertToolBarBreak(QToolBar *before)
{
    layoutState.toolBarAreaLayout.insertToolBarBreak(before);
    if (savedState.isValid())
        savedState.toolBarAreaLayout.insertToolBarBreak(before);
    invalidate();
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1560, as _ZN17QMainWindowLayout18removeToolBarBreakEP8QToolBar
#if QT_CONFIG(toolbar)
inline void QMainWindowLayout::removeToolBarBreak(QToolBar *before)
{
    layoutState.toolBarAreaLayout.removeToolBarBreak(before);
    if (savedState.isValid())
        savedState.toolBarAreaLayout.removeToolBarBreak(before);
    invalidate();
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1638, as _ZNK17QMainWindowLayout11toolBarAreaEPK8QToolBar
#if QT_CONFIG(toolbar)
inline Qt::ToolBarArea QMainWindowLayout::toolBarArea(const QToolBar *toolbar) const
{
    std::optional<QInternal::DockPosition> pos
        = layoutState.toolBarAreaLayout.findToolBar(toolbar);
    if (!pos)
        return Qt::NoToolBarArea;
    switch (*pos) {
        case QInternal::LeftDock:   return Qt::LeftToolBarArea;
        case QInternal::RightDock:  return Qt::RightToolBarArea;
        case QInternal::TopDock:    return Qt::TopToolBarArea;
        case QInternal::BottomDock: return Qt::BottomToolBarArea;
        default: break;
    }
    return Qt::NoToolBarArea;
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1654, as _ZNK17QMainWindowLayout12toolBarBreakEP8QToolBar
#if QT_CONFIG(toolbar)
inline bool QMainWindowLayout::toolBarBreak(QToolBar *toolBar) const
{
    return layoutState.toolBarAreaLayout.toolBarBreak(toolBar);
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1659, as _ZNK17QMainWindowLayout18getStyleOptionInfoEP19QStyleOptionToolBarP8QToolBar
#if QT_CONFIG(toolbar)
inline void QMainWindowLayout::getStyleOptionInfo(QStyleOptionToolBar *option, QToolBar *toolBar) const
{
    option->toolBarArea = toolBarArea(toolBar);
    layoutState.toolBarAreaLayout.getStyleOptionInfo(option, toolBar);
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1578, as _ZN17QMainWindowLayout13removeToolBarEP8QToolBar
#if QT_CONFIG(toolbar)
inline void QMainWindowLayout::removeToolBar(QToolBar *toolbar)
{
    if (toolbar) {
        QObject::disconnect(parentWidget(), SIGNAL(iconSizeChanged(QSize)),
                   toolbar, SLOT(_q_updateIconSize(QSize)));
        QObject::disconnect(parentWidget(), SIGNAL(toolButtonStyleChanged(Qt::ToolButtonStyle)),
                   toolbar, SLOT(_q_updateToolButtonStyle(Qt::ToolButtonStyle)));

        removeWidget(toolbar);
    }
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1665, as _ZN17QMainWindowLayout21toggleToolBarsVisibleEv
#if QT_CONFIG(toolbar)
inline void QMainWindowLayout::toggleToolBarsVisible()
{
    layoutState.toolBarAreaLayout.visible = !layoutState.toolBarAreaLayout.visible;
    if (!layoutState.mainWindow->isMaximized()) {
        QPoint topLeft = parentWidget()->geometry().topLeft();
        QRect r = parentWidget()->geometry();
        r = layoutState.toolBarAreaLayout.rectHint(r);
        r.moveTo(topLeft);
        parentWidget()->setGeometry(r);
    } else {
        update();
    }
}
#endif  // QT_CONFIG(toolbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1765, as _ZN17QMainWindowLayout9setCornerEN2Qt6CornerENS0_14DockWidgetAreaE
#if QT_CONFIG(dockwidget)
inline void QMainWindowLayout::setCorner(Qt::Corner corner, Qt::DockWidgetArea area)
{
    if (layoutState.dockAreaLayout.corners[corner] == area)
        return;
    layoutState.dockAreaLayout.corners[corner] = area;
    if (savedState.isValid())
        savedState.dockAreaLayout.corners[corner] = area;
    invalidate();
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1775, as _ZNK17QMainWindowLayout6cornerEN2Qt6CornerE
#if QT_CONFIG(dockwidget)
inline Qt::DockWidgetArea QMainWindowLayout::corner(Qt::Corner corner) const
{
    return layoutState.dockAreaLayout.corners[corner];
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2051, as _ZNK17QMainWindowLayout14dockWidgetAreaEPK7QWidget
#if QT_CONFIG(dockwidget)
inline Qt::DockWidgetArea QMainWindowLayout::dockWidgetArea(const QWidget *widget) const
{
    const QList<int> pathToWidget = layoutState.dockAreaLayout.indexOf(widget);
    if (pathToWidget.isEmpty())
        return Qt::NoDockWidgetArea;
    return toDockWidgetArea(pathToWidget.first());
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1923, as _ZNK17QMainWindowLayout12documentModeEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline bool QMainWindowLayout::documentMode() const
{
    return _documentMode;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1928, as _ZN17QMainWindowLayout15setDocumentModeEb
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline void QMainWindowLayout::setDocumentMode(bool enabled)
{
    if (_documentMode == enabled)
        return;

    _documentMode = enabled;

    // Update the document mode for all tab bars
    for (QTabBar *bar : std::as_const(usedTabBars))
        bar->setDocumentMode(_documentMode);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2324, as _ZN17QMainWindowLayout18getSeparatorWidgetEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline QWidget *QMainWindowLayout::getSeparatorWidget()
{
    auto *separator = new QWidget(parentWidget());
    separator->setAttribute(Qt::WA_MouseNoMask, true);
    separator->setAutoFillBackground(false);
    separator->setObjectName("qt_qmainwindow_extended_splitter"_L1);
    usedSeparatorWidgets.insert(separator);
    return separator;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1951, as _ZNK17QMainWindowLayout8tabShapeEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
#if QT_CONFIG(tabwidget)
inline QTabWidget::TabShape QMainWindowLayout::tabShape() const
{
    return _tabShape;
}
#endif  // QT_CONFIG(tabwidget)
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2481, as _ZN17QMainWindowLayout18applyRestoredStateEv
inline void QMainWindowLayout::applyRestoredState()
{
    if (restoredState) {
        layoutState = *restoredState;
        restoredState.reset();
        discardRestoredStateTimer.stop();
    }
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 3440, as _ZN17QMainWindowLayout17needsPlatformDragEv
#if QT_CONFIG(draganddrop)
inline bool QMainWindowLayout::needsPlatformDrag()
{
    static const bool wayland =
            QGuiApplication::platformName().startsWith("wayland"_L1, Qt::CaseInsensitive);
    return wayland;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 3447, as _ZN17QMainWindowLayout25performPlatformWidgetDragEP11QLayoutItemRK6QPoint
#if QT_CONFIG(draganddrop)
inline Qt::DropAction QMainWindowLayout::performPlatformWidgetDrag(QLayoutItem *widgetItem,
                                                            const QPoint &pressPosition)
{
    draggingWidget = widgetItem;
    QWidget *widget = widgetItem->widget();
    auto drag = QDrag(widget);
    auto mimeData = new QMimeData();
    auto window = widgetItem->widget()->windowHandle();

    auto serialize = [](const auto &object) {
        QByteArray data;
        QDataStream dataStream(&data, QIODevice::WriteOnly);
        dataStream << object;
        return data;
    };
    mimeData->setData("application/x-qt-mainwindowdrag-window"_L1,
                      serialize(reinterpret_cast<qintptr>(window)));
    mimeData->setData("application/x-qt-mainwindowdrag-position"_L1, serialize(pressPosition));
    drag.setMimeData(mimeData);

    auto result = drag.exec();

    draggingWidget = nullptr;
    return result;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1999, as _ZN17QMainWindowLayout11showTabBarsEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline void QMainWindowLayout::showTabBars()
{
    const auto usedTabBarsCopy = usedTabBars; // list potentially modified by animations
    for (QTabBar *tab_bar : usedTabBarsCopy) {
        if (usedTabBars.contains(tab_bar)) // Showing a tab bar can cause another to be deleted.
            tab_bar->show();
    }
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)
//  -----------------------------------------------------------------------

//  Only a class built on QMainWindowLayout may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMainWindowLayout : QMainWindowLayout {
  using QMainWindowLayout::timerEvent;
};

//  A QMainWindowLayout that Python can take functions over in. Every QMainWindowLayout
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(mainwindow)
typedef void (*CuteQMainWindowLayoutCall0)(const void *, QLayoutItem *, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef void (*CuteQMainWindowLayoutCall1)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef void * (*CuteQMainWindowLayoutCall2)(const void *, int, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef void * (*CuteQMainWindowLayoutCall3)(const void *, int, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef int (*CuteQMainWindowLayoutCall4)(const void *, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef const QSize * (*CuteQMainWindowLayoutCall5)(const void *, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef const QSize * (*CuteQMainWindowLayoutCall6)(const void *, int *);
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
typedef void (*CuteQMainWindowLayoutCall7)(const void *, int *);
#endif  // QT_CONFIG(mainwindow)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(mainwindow)
typedef void (*CuteQMainWindowLayoutCall8)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(mainwindow)
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQMainWindowLayoutCall9)(const void *, int *);
typedef void (*CuteQMainWindowLayoutCall10)(const void *, int, int *);
typedef const QRect * (*CuteQMainWindowLayoutCall11)(const void *, int *);
typedef int (*CuteQMainWindowLayoutCall12)(const void *, int *);
typedef const QSize * (*CuteQMainWindowLayoutCall13)(const void *, int *);
typedef int (*CuteQMainWindowLayoutCall14)(const void *, const QWidget *, int *);
typedef int (*CuteQMainWindowLayoutCall15)(const void *, const QLayoutItem *, int *);
typedef bool (*CuteQMainWindowLayoutCall16)(const void *, int *);
typedef int (*CuteQMainWindowLayoutCall17)(const void *, int *);
typedef void * (*CuteQMainWindowLayoutCall18)(const void *, QWidget *, QWidget *, int, int *);
typedef void * (*CuteQMainWindowLayoutCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMainWindowLayoutCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMainWindowLayoutCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMainWindowLayoutCall22)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMainWindowLayoutCall23)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMainWindowLayoutCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMainWindowLayoutCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMainWindowLayoutCall26)(const void *, int *);
typedef int (*CuteQMainWindowLayoutCall27)(const void *, int, int *);
typedef int (*CuteQMainWindowLayoutCall28)(const void *, int, int *);
typedef void * (*CuteQMainWindowLayoutCall29)(const void *, int *);
typedef void * (*CuteQMainWindowLayoutCall30)(const void *, int *);
class CuteQMainWindowLayout : public QMainWindowLayout {
public:
  using QMainWindowLayout::QMainWindowLayout;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZN7QLayout7addItemEP11QLayoutItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZN11QLayoutItem11setGeometryERK5QRect")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZNK7QLayout6itemAtEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZN7QLayout6takeAtEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZNK7QLayout5countEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZNK11QLayoutItem8sizeHintEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZNK11QLayoutItem11minimumSizeEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZN11QLayoutItem10invalidateEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(mainwindow)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(mainwindow)
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK7QLayout7spacingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout10setSpacingEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem8geometryEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem19expandingDirectionsEv")) {
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
    if (!std::strcmp(key, "_ZNK11QLayoutItem7isEmptyEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLayoutItem12controlTypesEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QLayout13replaceWidgetEP7QWidgetS1_6QFlagsIN2Qt15FindChildOptionEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLayoutItem6layoutEv")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

#if QT_CONFIG(mainwindow)
  //  void QMainWindowLayout::addItem(QLayoutItem *item)
  void addItem(QLayoutItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMainWindowLayoutCall0 call = reinterpret_cast<CuteQMainWindowLayoutCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QMainWindowLayout::addItem(item);
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  void QMainWindowLayout::setGeometry(const QRect &r)
  void setGeometry(const QRect &r) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMainWindowLayoutCall1 call = reinterpret_cast<CuteQMainWindowLayoutCall1>(taken[1]);
      call(this, &r, &handled);
      if (handled) return;
    }
    QMainWindowLayout::setGeometry(r);
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  QLayoutItem *QMainWindowLayout::itemAt(int index) const
  QLayoutItem *itemAt(int index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMainWindowLayoutCall2 call = reinterpret_cast<CuteQMainWindowLayoutCall2>(taken[2]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QMainWindowLayout::itemAt(index);
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  QLayoutItem *QMainWindowLayout::takeAt(int index)
  QLayoutItem *takeAt(int index) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMainWindowLayoutCall3 call = reinterpret_cast<CuteQMainWindowLayoutCall3>(taken[3]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QMainWindowLayout::takeAt(index);
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  int QMainWindowLayout::count() const
  int count() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQMainWindowLayoutCall4 call = reinterpret_cast<CuteQMainWindowLayoutCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QMainWindowLayout::count();
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  QSize QMainWindowLayout::sizeHint() const
  QSize sizeHint() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQMainWindowLayoutCall5 call = reinterpret_cast<CuteQMainWindowLayoutCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMainWindowLayout::sizeHint();
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  QSize QMainWindowLayout::minimumSize() const
  QSize minimumSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQMainWindowLayoutCall6 call = reinterpret_cast<CuteQMainWindowLayoutCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMainWindowLayout::minimumSize();
  }
#endif  // QT_CONFIG(mainwindow)

#if QT_CONFIG(mainwindow)
  //  void QMainWindowLayout::invalidate()
  void invalidate() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMainWindowLayoutCall7 call = reinterpret_cast<CuteQMainWindowLayoutCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QMainWindowLayout::invalidate();
  }
#endif  // QT_CONFIG(mainwindow)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(mainwindow)
  //  void QMainWindowLayout::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQMainWindowLayoutCall8 call = reinterpret_cast<CuteQMainWindowLayoutCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QMainWindowLayout::timerEvent(e);
  }
#endif  // QT_CONFIG(mainwindow)
#endif  // !defined(QT_NO_QOBJECT)

  //  int QLayout::spacing() const
  int spacing() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQMainWindowLayoutCall9 call = reinterpret_cast<CuteQMainWindowLayoutCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::spacing();
  }

  //  void QLayout::setSpacing(int a0)
  void setSpacing(int a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQMainWindowLayoutCall10 call = reinterpret_cast<CuteQMainWindowLayoutCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QLayout::setSpacing(a0);
  }

  //  QRect QLayout::geometry() const
  QRect geometry() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQMainWindowLayoutCall11 call = reinterpret_cast<CuteQMainWindowLayoutCall11>(taken[11]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::geometry();
  }

  //  Qt::Orientations QLayout::expandingDirections() const
  Qt::Orientations expandingDirections() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQMainWindowLayoutCall12 call = reinterpret_cast<CuteQMainWindowLayoutCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::Orientation>::fromInt(given);
    }
    return QLayout::expandingDirections();
  }

  //  QSize QLayout::maximumSize() const
  QSize maximumSize() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQMainWindowLayoutCall13 call = reinterpret_cast<CuteQMainWindowLayoutCall13>(taken[13]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLayout::maximumSize();
  }

  //  int QLayout::indexOf(const QWidget *a0) const
  int indexOf(const QWidget *a0) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQMainWindowLayoutCall14 call = reinterpret_cast<CuteQMainWindowLayoutCall14>(taken[14]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  int QLayout::indexOf(const QLayoutItem *a0) const
  int indexOf(const QLayoutItem *a0) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQMainWindowLayoutCall15 call = reinterpret_cast<CuteQMainWindowLayoutCall15>(taken[15]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayout::indexOf(a0);
  }

  //  bool QLayout::isEmpty() const
  bool isEmpty() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQMainWindowLayoutCall16 call = reinterpret_cast<CuteQMainWindowLayoutCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayout::isEmpty();
  }

  //  QSizePolicy::ControlTypes QLayout::controlTypes() const
  QSizePolicy::ControlTypes controlTypes() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQMainWindowLayoutCall17 call = reinterpret_cast<CuteQMainWindowLayoutCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQMainWindowLayoutCall18 call = reinterpret_cast<CuteQMainWindowLayoutCall18>(taken[18]);
      void * given = call(this, from, to, static_cast<int>(options.toInt()), &handled);
      if (handled) return static_cast<QLayoutItem *>(given);
    }
    return QLayout::replaceWidget(from, to, options);
  }

  //  QLayout *QLayout::layout()
  QLayout *layout() override {
    if (taken[19]) {
      int handled = 0;
      CuteQMainWindowLayoutCall19 call = reinterpret_cast<CuteQMainWindowLayoutCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLayout *>(given);
    }
    return QLayout::layout();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QLayout::childEvent(QChildEvent *e)
  void childEvent(QChildEvent *e) override {
    if (taken[20]) {
      int handled = 0;
      CuteQMainWindowLayoutCall20 call = reinterpret_cast<CuteQMainWindowLayoutCall20>(taken[20]);
      call(this, e, &handled);
      if (handled) return;
    }
    QLayout::childEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQMainWindowLayoutCall21 call = reinterpret_cast<CuteQMainWindowLayoutCall21>(taken[21]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQMainWindowLayoutCall22 call = reinterpret_cast<CuteQMainWindowLayoutCall22>(taken[22]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQMainWindowLayoutCall23 call = reinterpret_cast<CuteQMainWindowLayoutCall23>(taken[23]);
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
      CuteQMainWindowLayoutCall24 call = reinterpret_cast<CuteQMainWindowLayoutCall24>(taken[24]);
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
      CuteQMainWindowLayoutCall25 call = reinterpret_cast<CuteQMainWindowLayoutCall25>(taken[25]);
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
      CuteQMainWindowLayoutCall26 call = reinterpret_cast<CuteQMainWindowLayoutCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLayoutItem::hasHeightForWidth();
  }

  //  int QLayoutItem::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQMainWindowLayoutCall27 call = reinterpret_cast<CuteQMainWindowLayoutCall27>(taken[27]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::heightForWidth(a0);
  }

  //  int QLayoutItem::minimumHeightForWidth(int a0) const
  int minimumHeightForWidth(int a0) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQMainWindowLayoutCall28 call = reinterpret_cast<CuteQMainWindowLayoutCall28>(taken[28]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QLayoutItem::minimumHeightForWidth(a0);
  }

  //  QWidget *QLayoutItem::widget() const
  QWidget *widget() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQMainWindowLayoutCall29 call = reinterpret_cast<CuteQMainWindowLayoutCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QLayoutItem::widget();
  }

  //  QSpacerItem *QLayoutItem::spacerItem()
  QSpacerItem *spacerItem() override {
    if (taken[30]) {
      int handled = 0;
      CuteQMainWindowLayoutCall30 call = reinterpret_cast<CuteQMainWindowLayoutCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSpacerItem *>(given);
    }
    return QLayoutItem::spacerItem();
  }
};

//  const QMetaObject *QMainWindowLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QMainWindowLayout10metaObjectEv(
    const QMainWindowLayout *self) {
  return self->metaObject();
}

//  void *QMainWindowLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QMainWindowLayout11qt_metacastEPKc(
    QMainWindowLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMainWindowLayout::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QMainWindowLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QMainWindowLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QMainWindowLayout::~QMainWindowLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayoutD1Ev(QMainWindowLayout *self) {
  delete self;
}

#if QT_CONFIG(statusbar)
//  QStatusBar *QMainWindowLayout::statusBar() const
extern "C" Q_DECL_EXPORT
QStatusBar *ritual_ZNK17QMainWindowLayout9statusBarEv(
    const QMainWindowLayout *self) {
  return self->statusBar();
}
#endif  // QT_CONFIG(statusbar)

#if QT_CONFIG(statusbar)
//  void QMainWindowLayout::setStatusBar(QStatusBar *sb)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout12setStatusBarEP10QStatusBar(
    QMainWindowLayout *self,
    QStatusBar *sb) {
  self->setStatusBar(sb);
}
#endif  // QT_CONFIG(statusbar)

//  QWidget *QMainWindowLayout::centralWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK17QMainWindowLayout13centralWidgetEv(
    const QMainWindowLayout *self) {
  return self->centralWidget();
}

//  void QMainWindowLayout::setCentralWidget(QWidget *cw)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout16setCentralWidgetEP7QWidget(
    QMainWindowLayout *self,
    QWidget *cw) {
  self->setCentralWidget(cw);
}

#if QT_CONFIG(toolbar)
//  void QMainWindowLayout::insertToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout18insertToolBarBreakEP8QToolBar(
    QMainWindowLayout *self,
    QToolBar *before) {
  self->insertToolBarBreak(before);
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  void QMainWindowLayout::removeToolBarBreak(QToolBar *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout18removeToolBarBreakEP8QToolBar(
    QMainWindowLayout *self,
    QToolBar *before) {
  self->removeToolBarBreak(before);
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  Qt::ToolBarArea QMainWindowLayout::toolBarArea(const QToolBar *toolbar)
//      const
extern "C" Q_DECL_EXPORT
Qt::ToolBarArea ritual_ZNK17QMainWindowLayout11toolBarAreaEPK8QToolBar(
    const QMainWindowLayout *self,
    const QToolBar *toolbar) {
  return self->toolBarArea(toolbar);
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  bool QMainWindowLayout::toolBarBreak(QToolBar *toolBar) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QMainWindowLayout12toolBarBreakEP8QToolBar(
    const QMainWindowLayout *self,
    QToolBar *toolBar) {
  return self->toolBarBreak(toolBar);
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  void QMainWindowLayout::getStyleOptionInfo(QStyleOptionToolBar *option,
//      QToolBar *toolBar) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QMainWindowLayout18getStyleOptionInfoEP19QStyleOptionToolBarP8QToolBar(
    const QMainWindowLayout *self,
    QStyleOptionToolBar *option,
    QToolBar *toolBar) {
  self->getStyleOptionInfo(option, toolBar);
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  void QMainWindowLayout::removeToolBar(QToolBar *toolbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout13removeToolBarEP8QToolBar(
    QMainWindowLayout *self,
    QToolBar *toolbar) {
  self->removeToolBar(toolbar);
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  void QMainWindowLayout::toggleToolBarsVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout21toggleToolBarsVisibleEv(
    QMainWindowLayout *self) {
  self->toggleToolBarsVisible();
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(toolbar)
//  QToolBarAreaLayout *QMainWindowLayout::toolBarAreaLayout()
extern "C" Q_DECL_EXPORT
QToolBarAreaLayout *ritual_ZN17QMainWindowLayout17toolBarAreaLayoutEv(
    QMainWindowLayout *self) {
  return self->toolBarAreaLayout();
}
#endif  // QT_CONFIG(toolbar)

#if QT_CONFIG(dockwidget)
//  void QMainWindowLayout::setCorner(Qt::Corner corner, Qt::DockWidgetArea
//      area)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout9setCornerEN2Qt6CornerENS0_14DockWidgetAreaE(
    QMainWindowLayout *self,
    Qt::Corner corner,
    Qt::DockWidgetArea area) {
  self->setCorner(corner, area);
}
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
//  Qt::DockWidgetArea QMainWindowLayout::corner(Qt::Corner corner) const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK17QMainWindowLayout6cornerEN2Qt6CornerE(
    const QMainWindowLayout *self,
    Qt::Corner corner) {
  return self->corner(corner);
}
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
//  Qt::DockWidgetArea QMainWindowLayout::dockWidgetArea(const QWidget
//      *widget) const
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZNK17QMainWindowLayout14dockWidgetAreaEPK7QWidget(
    const QMainWindowLayout *self,
    const QWidget *widget) {
  return self->dockWidgetArea(widget);
}
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  bool QMainWindowLayout::documentMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QMainWindowLayout12documentModeEv(
    const QMainWindowLayout *self) {
  return self->documentMode();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  void QMainWindowLayout::setDocumentMode(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout15setDocumentModeEb(
    QMainWindowLayout *self,
    bool enabled) {
  self->setDocumentMode(enabled);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  QWidget *QMainWindowLayout::getSeparatorWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN17QMainWindowLayout18getSeparatorWidgetEv(
    QMainWindowLayout *self) {
  return self->getSeparatorWidget();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
#if QT_CONFIG(tabwidget)
//  QTabWidget::TabShape QMainWindowLayout::tabShape() const
extern "C" Q_DECL_EXPORT
QTabWidget::TabShape ritual_ZNK17QMainWindowLayout8tabShapeEv(
    const QMainWindowLayout *self) {
  return self->tabShape();
}
#endif  // QT_CONFIG(tabwidget)
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
//  QDockAreaLayout *QMainWindowLayout::dockAreaLayoutInfo()
extern "C" Q_DECL_EXPORT
QDockAreaLayout *ritual_ZN17QMainWindowLayout18dockAreaLayoutInfoEv(
    QMainWindowLayout *self) {
  return self->dockAreaLayoutInfo();
}
#endif  // QT_CONFIG(dockwidget)

//  void QMainWindowLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout7addItemEP11QLayoutItem(
    QMainWindowLayout *self,
    QLayoutItem *item) {
  self->addItem(item);
}

//  void QMainWindowLayout::setGeometry(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout11setGeometryERK5QRect(
    QMainWindowLayout *self,
    const QRect *r) {
  self->setGeometry(*r);
}

//  QLayoutItem *QMainWindowLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK17QMainWindowLayout6itemAtEi(
    const QMainWindowLayout *self,
    int index) {
  return self->itemAt(index);
}

//  QLayoutItem *QMainWindowLayout::takeAt(int index)
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZN17QMainWindowLayout6takeAtEi(
    QMainWindowLayout *self,
    int index) {
  return self->takeAt(index);
}

//  int QMainWindowLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QMainWindowLayout5countEv(const QMainWindowLayout *self) {
  return self->count();
}

//  QSize QMainWindowLayout::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QMainWindowLayout8sizeHintEv(
    const QMainWindowLayout *self) {
  return new QSize(self->sizeHint());
}

//  QSize QMainWindowLayout::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QMainWindowLayout11minimumSizeEv(
    const QMainWindowLayout *self) {
  return new QSize(self->minimumSize());
}

//  void QMainWindowLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout10invalidateEv(QMainWindowLayout *self) {
  self->invalidate();
}

//  void QMainWindowLayout::applyRestoredState()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout18applyRestoredStateEv(
    QMainWindowLayout *self) {
  self->applyRestoredState();
}

#if QT_CONFIG(draganddrop)
//  bool QMainWindowLayout::needsPlatformDrag()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QMainWindowLayout17needsPlatformDragEv() {
  return QMainWindowLayout::needsPlatformDrag();
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  Qt::DropAction QMainWindowLayout::performPlatformWidgetDrag(QLayoutItem
//      *widgetItem, const QPoint &pressPosition)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN17QMainWindowLayout25performPlatformWidgetDragEP11QLayoutItemRK6QPoint(
    QMainWindowLayout *self,
    QLayoutItem *widgetItem,
    const QPoint *pressPosition) {
  return self->performPlatformWidgetDrag(widgetItem, *pressPosition);
}
#endif  // QT_CONFIG(draganddrop)

//  void QMainWindowLayout::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout10timerEventEP11QTimerEvent(
    QMainWindowLayout *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QMainWindowLayout::updateGapIndicator()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout18updateGapIndicatorEv(
    QMainWindowLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QMainWindowLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateGapIndicator()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateGapIndicator()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  void QMainWindowLayout::tabChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout10tabChangedEv(QMainWindowLayout *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QMainWindowLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tabChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tabChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  void QMainWindowLayout::tabMoved(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout8tabMovedEii(
    QMainWindowLayout *self,
    int from,
    int to) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QMainWindowLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tabMoved(int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tabMoved(int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&from)),
      const_cast<void *>(static_cast<const void *>(&to)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  void QMainWindowLayout::tabifyWhileFloating(QDockWidget *first,
//      QDockWidget *second)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout19tabifyWhileFloatingEP11QDockWidgetS1_(
    QMainWindowLayout *self,
    QDockWidget *first,
    QDockWidget *second) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QMainWindowLayout")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tabifyWhileFloating(QDockWidget *,QDockWidget *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tabifyWhileFloating(QDockWidget *,QDockWidget *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&first)),
      const_cast<void *>(static_cast<const void *>(&second)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(tabbar)
#if QT_CONFIG(dockwidget)
//  void QMainWindowLayout::showTabBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMainWindowLayout11showTabBarsEv(QMainWindowLayout *self) {
  self->showTabBars();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(tabbar)

//  a Python function taken by a CuteQMainWindowLayout, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMainWindowLayout(
    QMainWindowLayout *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMainWindowLayout *>(self)->take(key, call);
}

//  void QMainWindowLayout::addItem(QLayoutItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QMainWindowLayout7addItemEP11QLayoutItem(
    QMainWindowLayout *self,
    QLayoutItem *item) {
  self->QMainWindowLayout::addItem(item);
}

//  QLayoutItem *QMainWindowLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_own_ZNK17QMainWindowLayout6itemAtEi(
    const QMainWindowLayout *self,
    int index) {
  return self->QMainWindowLayout::itemAt(index);
}

//  int QMainWindowLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QMainWindowLayout5countEv(
    const QMainWindowLayout *self) {
  return self->QMainWindowLayout::count();
}

//  void QMainWindowLayout::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QMainWindowLayout10invalidateEv(
    QMainWindowLayout *self) {
  self->QMainWindowLayout::invalidate();
}

//  void QMainWindowLayout::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QMainWindowLayout10timerEventEP11QTimerEvent(
    QMainWindowLayout *self,
    QTimerEvent *e) {
  static_cast<OwnQMainWindowLayout *>(self)->OwnQMainWindowLayout::timerEvent(
      e);
}

#endif  // QT_CONFIG(mainwindow)
#endif  // QT_CONFIG(mainwindow)
