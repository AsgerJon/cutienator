//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
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
#include <QtWidgets/QWidgetItem>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QStyleOption>
#include <QtWidgets/QApplication>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtoolbararealayout_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbar_p.h>
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 24, as local:qtoolbararealayout.cpp:StateMarkers
using StateMarkers = QMainWindowLayoutState::StateMarkers;

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1250, as local:qtoolbararealayout.cpp:getInt
static inline int getInt(QDataStream &stream)
{
    int x;
    stream >> x;
    return x;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3527, as _ZN15QDockAreaLayout20deleteAllLayoutItemsEv
inline void QDockAreaLayout::deleteAllLayoutItems()
{
    for (auto &dock : docks)
        dock.deleteAllLayoutItems();
}

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3152, as _ZNK15QDockAreaLayout17minimumStableSizeEv
inline QSize QDockAreaLayout::minimumStableSize() const
{
    return size_helper(&QDockAreaLayoutInfo::size, &QLayoutItem::minimumSize);
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3509, as _ZN15QDockAreaLayout6takeAtEPii
inline QLayoutItem *QDockAreaLayout::takeAt(int *x, int index)
{
    Q_ASSERT(x != nullptr);

    for (auto &dock : docks) {
        if (QLayoutItem *ret = dock.takeAt(x, index))
            return ret;
    }

    if (centralWidgetItem && (*x)++ == index) {
        QLayoutItem *ret = centralWidgetItem;
        centralWidgetItem = nullptr;
        return ret;
    }

    return nullptr;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 715, as _ZN18QToolBarAreaLayout6takeAtEPii
inline QLayoutItem *QToolBarAreaLayout::takeAt(int *x, int index)
{
    Q_ASSERT(x != nullptr);

    for (int i = 0; i < QInternal::DockCount; ++i) {
        QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            QToolBarAreaLayoutLine &line = dock.lines[j];

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                if ((*x)++ == index) {
                    QLayoutItem *result = line.toolBarItems.takeAt(k).widgetItem;
                    if (line.toolBarItems.isEmpty())
                        dock.lines.removeAt(j);
                    return result;
                }
            }
        }
    }

    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2684, as _ZN15QDockAreaLayout4itemERK5QListIiE
inline QDockAreaLayoutItem &QDockAreaLayout::item(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    return docks[index].item(path.mid(1));
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1063, as _ZN18QToolBarAreaLayout4itemERK5QListIiE
inline QToolBarAreaLayoutItem *QToolBarAreaLayout::item(const QList<int> &path)
{
    Q_ASSERT(path.size() == 3);

    if (path.at(0) < 0 || path.at(0) >= QInternal::DockCount)
        return nullptr;
    QToolBarAreaLayoutInfo &info = docks[path.at(0)];
    if (path.at(1) < 0 || path.at(1) >= info.lines.size())
        return nullptr;
    QToolBarAreaLayoutLine &line = info.lines[path.at(1)];
    if (path.at(2) < 0 || path.at(2) >= line.toolBarItems.size())
        return nullptr;
    return &(line.toolBarItems[path.at(2)]);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2692, as _ZNK15QDockAreaLayout8itemRectERK5QListIiE
inline QRect QDockAreaLayout::itemRect(const QList<int> &path) const
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    return docks[index].itemRect(path.mid(1));
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1078, as _ZNK18QToolBarAreaLayout8itemRectERK5QListIiE
inline QRect QToolBarAreaLayout::itemRect(const QList<int> &path) const
{
    const int i = path.first();

    QRect r = docks[i].itemRect(path.mid(1));
    if (docks[i].o == Qt::Horizontal)
        r = QStyle::visualRect(mainWindow->layoutDirection(),
                                docks[i].rect, r);
    return r;
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 942, as _ZNK18QToolBarAreaLayout7indexOfEP7QWidget
inline QList<int> QToolBarAreaLayout::indexOf(QWidget *toolBar) const
{
    QList<int> result;

    bool found = false;

    for (int i = 0; i < QInternal::DockCount; ++i) {
        const QToolBarAreaLayoutInfo &dock = docks[i];

        for (int j = 0; j < dock.lines.size(); ++j) {
            const QToolBarAreaLayoutLine &line = dock.lines.at(j);

            for (int k = 0; k < line.toolBarItems.size(); ++k) {
                const QToolBarAreaLayoutItem &item = line.toolBarItems.at(k);
                if (!item.gap && item.widgetItem->widget() == toolBar) {
                    found = true;
                    result.prepend(k);
                    break;
                }
            }

            if (found) {
                result.prepend(j);
                break;
            }
        }

        if (found) {
            result.prepend(i);
            break;
        }
    }

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2734, as _ZN15QDockAreaLayout9insertGapERK5QListIiEP11QLayoutItem
inline bool QDockAreaLayout::insertGap(const QList<int> &path, QLayoutItem *dockWidgetItem)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    return docks[index].insertGap(path.mid(1), dockWidgetItem);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1018, as _ZN18QToolBarAreaLayout9insertGapERK5QListIiEP11QLayoutItem
inline bool QToolBarAreaLayout::insertGap(const QList<int> &path, QLayoutItem *item)
{
    Q_ASSERT(path.size() == 3);
    const int i = path.first();
    Q_ASSERT(i >= 0 && i < QInternal::DockCount);
    return docks[i].insertGap(path.mid(1), item);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2764, as _ZN15QDockAreaLayout6removeERK5QListIiE
inline void QDockAreaLayout::remove(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    docks[index].remove(path.mid(1));
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3076, as _ZN15QDockAreaLayout5clearEv
inline void QDockAreaLayout::clear()
{
    for (auto &dock : docks)
        dock.clear();

    rect = QRect();
    centralWidgetRect = QRect();
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1056, as _ZN18QToolBarAreaLayout5clearEv
inline void QToolBarAreaLayout::clear()
{
    for (int i = 0; i < QInternal::DockCount; ++i)
        docks[i].clear();
    rect = QRect();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2742, as _ZN15QDockAreaLayout4plugERK5QListIiE
inline QLayoutItem *QDockAreaLayout::plug(const QList<int> &path)
{
#if QT_CONFIG(tabbar)
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    QLayoutItem *item = docks[index].plug(path.mid(1));
    docks[index].reparentWidgets(mainWindow);
    return item;
#else
    return nullptr;
#endif
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1089, as _ZN18QToolBarAreaLayout4plugERK5QListIiE
inline QLayoutItem *QToolBarAreaLayout::plug(const QList<int> &path)
{
    QToolBarAreaLayoutItem *item = this->item(path);
    if (Q_UNLIKELY(!item)) {
        qWarning() << "No item at" << path;
        return nullptr;
    }
    Q_ASSERT(item->gap);
    Q_ASSERT(item->widgetItem != nullptr);
    item->gap = false;
    return item->widgetItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2756, as _ZN15QDockAreaLayout6unplugERK5QListIiE
inline QLayoutItem *QDockAreaLayout::unplug(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());
    const int index = path.first();
    Q_ASSERT(index >= 0 && index < int(docks.size()));
    return docks[index].unplug(path.mid(1));
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 1102, as _ZN18QToolBarAreaLayout6unplugERK5QListIiEPS_
inline QLayoutItem *QToolBarAreaLayout::unplug(const QList<int> &path, QToolBarAreaLayout *other)
{
    //other needs to be update as well
    Q_ASSERT(path.size() == 3);
    QToolBarAreaLayoutItem *item = this->item(path);
    Q_ASSERT(item);

    //update the leading space here
    QToolBarAreaLayoutInfo &info = docks[path.at(0)];
    QToolBarAreaLayoutLine &line = info.lines[path.at(1)];
    if (item->size != pick(line.o, item->realSizeHint())) {
        //the item doesn't have its default size
        //so we'll give this to the next item
        int newExtraSpace = 0;
        //let's iterate over the siblings of the current item that pare placed before it
        //we need to find just the one before
        for (int i = path.at(2) - 1; i >= 0; --i) {
            QToolBarAreaLayoutItem &previous = line.toolBarItems[i];
            if (!previous.skip()) {
                //we need to check if it has a previous element and a next one
                //the previous will get its size changed
                for (int j = path.at(2) + 1; j < line.toolBarItems.size(); ++j) {
                    const QToolBarAreaLayoutItem &next = line.toolBarItems.at(j);
                    if (!next.skip()) {
                        newExtraSpace = next.pos - previous.pos - pick(line.o, previous.sizeHint());
                        previous.resize(line.o, next.pos - previous.pos);
                        break;
                    }
                }
                break;
            }
        }

        if (other) {
            QToolBarAreaLayoutInfo &info = other->docks[path.at(0)];
            QToolBarAreaLayoutLine &line = info.lines[path.at(1)];
            for (int i = path.at(2) - 1; i >= 0; --i) {
                QToolBarAreaLayoutItem &previous = line.toolBarItems[i];
                if (!previous.skip()) {
                    previous.resize(line.o, pick(line.o, previous.sizeHint()) + newExtraSpace);
                    break;
                }
            }

        }
    }

    Q_ASSERT(!item->gap);
    item->gap = true;
    return item->widgetItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2481, as _ZN15QDockAreaLayout12restoreStateER11QDataStreamRK5QListIP11QDockWidgetEN9QInternal8CallModeE
inline bool QDockAreaLayout::restoreState(QDataStream &stream, const QList<QDockWidget*> &_dockwidgets, QInternal::CallMode callMode)
{
    QList<QDockWidget*> dockwidgets = _dockwidgets;
    const bool testing = callMode == QInternal::Testing;
    int cnt;
    stream >> cnt;
    for (int i = 0; i < cnt; ++i) {
        int pos;
        stream >> pos;
        QSize size;
        stream >> size;
        if (!testing) {
            docks[pos].rect = QRect(QPoint(0, 0), size);
        }
        if (!docks[pos].restoreState(stream, dockwidgets, callMode)) {
            stream.setStatus(QDataStream::ReadCorruptData);
            return false;
        }
    }

    QSize size;
    stream >> size;
    centralWidgetRect = QRect(QPoint(0, 0), size);

    bool ok = stream.status() == QDataStream::Ok;

    if (ok) {
        QDockAreaLayoutCorners cornerData;
        for (auto &val : cornerData)
            stream >> val;

        if (stream.status() == QDataStream::Ok)
            corners = std::move(cornerData);

        if (!testing)
            fallbackToSizeHints = false;
    }

    return ok;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 256, as _ZN19QDockAreaLayoutInfoC1Ev
inline QDockAreaLayoutInfo::QDockAreaLayoutInfo()
    : sep(&zero), dockPos(QInternal::LeftDock), o(Qt::Horizontal), mainWindow(nullptr)
#if QT_CONFIG(tabbar)
    , tabbed(false), tabBar(nullptr), tabBarShape(QTabBar::RoundedSouth)
#endif
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2968, as _ZN15QDockAreaLayout7setGridEP5QListI13QLayoutStructES3_
inline void QDockAreaLayout::setGrid(QList<QLayoutStruct> *ver_struct_list,
                              QList<QLayoutStruct> *hor_struct_list)
{

    // top ---------------------------------------------------

    if (!docks[QInternal::TopDock].isEmpty()) {
        QRect r = docks[QInternal::TopDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(corners[Qt::TopLeftCorner] == Qt::TopDockWidgetArea
                || docks[QInternal::LeftDock].isEmpty()
                ? rect.left() : hor_struct_list->at(1).pos);
            r.setRight(corners[Qt::TopRightCorner] == Qt::TopDockWidgetArea
                || docks[QInternal::RightDock].isEmpty()
                ? rect.right() : hor_struct_list->at(2).pos - sep - 1);
        }
        if (ver_struct_list != nullptr) {
            r.setTop(rect.top());
            r.setBottom(ver_struct_list->at(1).pos - sep - 1);
        }
        docks[QInternal::TopDock].rect = r;
        docks[QInternal::TopDock].fitItems();
    }

    // bottom ---------------------------------------------------

    if (!docks[QInternal::BottomDock].isEmpty()) {
        QRect r = docks[QInternal::BottomDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(corners[Qt::BottomLeftCorner] == Qt::BottomDockWidgetArea
                        || docks[QInternal::LeftDock].isEmpty()
                            ? rect.left() : hor_struct_list->at(1).pos);
            r.setRight(corners[Qt::BottomRightCorner] == Qt::BottomDockWidgetArea
                        || docks[QInternal::RightDock].isEmpty()
                            ? rect.right() : hor_struct_list->at(2).pos - sep - 1);
        }
        if (ver_struct_list != nullptr) {
            r.setTop(ver_struct_list->at(2).pos);
            r.setBottom(rect.bottom());
        }
        docks[QInternal::BottomDock].rect = r;
        docks[QInternal::BottomDock].fitItems();
    }

    // left ---------------------------------------------------

    if (!docks[QInternal::LeftDock].isEmpty()) {
        QRect r = docks[QInternal::LeftDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(rect.left());
            r.setRight(hor_struct_list->at(1).pos - sep - 1);
        }
        if (ver_struct_list != nullptr) {
            r.setTop(corners[Qt::TopLeftCorner] == Qt::LeftDockWidgetArea
                || docks[QInternal::TopDock].isEmpty()
                ? rect.top() : ver_struct_list->at(1).pos);
            r.setBottom(corners[Qt::BottomLeftCorner] == Qt::LeftDockWidgetArea
                || docks[QInternal::BottomDock].isEmpty()
                ? rect.bottom() : ver_struct_list->at(2).pos - sep - 1);
        }
        docks[QInternal::LeftDock].rect = r;
        docks[QInternal::LeftDock].fitItems();
    }

    // right ---------------------------------------------------

    if (!docks[QInternal::RightDock].isEmpty()) {
        QRect r = docks[QInternal::RightDock].rect;
        if (hor_struct_list != nullptr) {
            r.setLeft(hor_struct_list->at(2).pos);
            r.setRight(rect.right());
        }
        if (ver_struct_list != nullptr) {
            r.setTop(corners[Qt::TopRightCorner] == Qt::RightDockWidgetArea
                        || docks[QInternal::TopDock].isEmpty()
                            ? rect.top() : ver_struct_list->at(1).pos);
            r.setBottom(corners[Qt::BottomRightCorner] == Qt::RightDockWidgetArea
                        || docks[QInternal::BottomDock].isEmpty()
                            ? rect.bottom() : ver_struct_list->at(2).pos - sep - 1);
        }
        docks[QInternal::RightDock].rect = r;
        docks[QInternal::RightDock].fitItems();
    }

    // center ---------------------------------------------------

    if (hor_struct_list != nullptr) {
        centralWidgetRect.setLeft(hor_struct_list->at(1).pos);
        centralWidgetRect.setWidth(hor_struct_list->at(1).size);
    }
    if (ver_struct_list != nullptr) {
        centralWidgetRect.setTop(ver_struct_list->at(1).pos);
        centralWidgetRect.setHeight(ver_struct_list->at(1).size);
    }
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1805, as _ZN19QDockAreaLayoutInfo6takeAtEPii
inline QLayoutItem *QDockAreaLayoutInfo::takeAt(int *x, int index)
{
    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item = item_list[i];
        if (item.placeHolderItem != nullptr)
            continue;
        else if (item.subinfo) {
            if (QLayoutItem *ret = item.subinfo->takeAt(x, index)) {
                unnest(i);
                return ret;
            }
        } else if (item.widgetItem) {
            if ((*x)++ == index) {
                QWidget *widget = item.widgetItem->widget();
                if (widget->isWidgetType())
                    item.placeHolderItem = new QPlaceHolderItem(widget);
                else
                    qCDebug(lcQpaDockWidgets) << widget << "is in destruction. No gap created.";
                QLayoutItem *ret = item.widgetItem;
                item.widgetItem = nullptr;
                if (item.size != -1)
                    item.flags |= QDockAreaLayoutItem::KeepSize;
                return ret;
            }
        }
    }
    return nullptr;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1394, as _ZNK19QDockAreaLayoutInfo8itemRectERK5QListIiE
inline QRect QDockAreaLayoutInfo::itemRect(const QList<int> &path) const
{
    Q_ASSERT(!path.isEmpty());

    const int index = path.first();
    if (path.size() > 1) {
        const QDockAreaLayoutItem &item = item_list.at(index);
        Q_ASSERT(item.subinfo != nullptr);
        return item.subinfo->itemRect(path.mid(1));
    }

    return itemRect(index);
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 542, as _ZNK22QToolBarAreaLayoutInfo8itemRectERK5QListIiE
inline QRect QToolBarAreaLayoutInfo::itemRect(const QList<int> &path) const
{
    Q_ASSERT(path.size() == 2);
    int j = path.at(0);
    int k = path.at(1);

    const QToolBarAreaLayoutLine &line = lines.at(j);
    const QToolBarAreaLayoutItem &item = line.toolBarItems.at(k);

    QRect result = line.rect;

    if (o == Qt::Horizontal) {
        result.setLeft(item.pos + line.rect.left());
        result.setWidth(item.size);
    } else {
        result.setTop(item.pos + line.rect.top());
        result.setHeight(item.size);
    }

    return result;
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

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 536, as _ZN22QToolBarAreaLayoutInfo5clearEv
inline void QToolBarAreaLayoutInfo::clear()
{
    lines.clear();
    rect = QRect();
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1064, as _ZN19QDockAreaLayoutInfo4plugERK5QListIiE
inline QLayoutItem *QDockAreaLayoutInfo::plug(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());

    int index = path.first();
    if (index < 0)
        index = -index - 1;

    if (path.size() > 1) {
        QDockAreaLayoutItem &item = item_list[index];
        Q_ASSERT(item.subinfo != nullptr);
        return item.subinfo->plug(path.mid(1));
    }

    QDockAreaLayoutItem &item = item_list[index];

    Q_ASSERT(item.widgetItem != nullptr);
    Q_ASSERT(item.flags & QDockAreaLayoutItem::GapItem);
    item.flags &= ~QDockAreaLayoutItem::GapItem;
    return item.widgetItem;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1086, as _ZN19QDockAreaLayoutInfo6unplugERK5QListIiE
inline QLayoutItem *QDockAreaLayoutInfo::unplug(const QList<int> &path)
{
    Q_ASSERT(!path.isEmpty());

    const int index = path.first();
    if (path.size() > 1) {
        QDockAreaLayoutItem &item = item_list[index];
        Q_ASSERT(item.subinfo != nullptr);
        return item.subinfo->unplug(path.mid(1));
    }

    QDockAreaLayoutItem &item = item_list[index];
    int prev = this->prev(index);
    int next = this->next(index);

    Q_ASSERT(!(item.flags & QDockAreaLayoutItem::GapItem));
    item.flags |= QDockAreaLayoutItem::GapItem;

#if QT_CONFIG(tabbar)
    if (tabbed) {
    } else
#endif
    {
        if (prev != -1 && !(item_list.at(prev).flags & QDockAreaLayoutItem::GapItem)) {
            item.pos -= *sep;
            item.size += *sep;
        }
        if (next != -1 && !(item_list.at(next).flags & QDockAreaLayoutItem::GapItem))
            item.size += *sep;
    }

    return item.widgetItem;
}

//  from src/widgets/widgets/qtoolbararealayout.cpp, line 26, as _ZNK22QToolBarAreaLayoutItem11minimumSizeEv
inline QSize QToolBarAreaLayoutItem::minimumSize() const
{
    if (skip())
        return QSize(0, 0);
    return qSmartMinSize(static_cast<QWidgetItem*>(widgetItem));
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2373, as _ZNK19QDockAreaLayoutInfo14tabContentRectEv
#if QT_CONFIG(tabbar)
inline QRect QDockAreaLayoutInfo::tabContentRect() const
{
    if (!tabbed)
        return QRect();

    QRect result = rect;
    QSize tbh = tabBarSizeHint();

    if (!tbh.isNull()) {
        switch (tabBarShape) {
            case QTabBar::RoundedNorth:
            case QTabBar::TriangularNorth:
                result.adjust(0, tbh.height(), 0, 0);
                break;
            case QTabBar::RoundedSouth:
            case QTabBar::TriangularSouth:
                result.adjust(0, 0, 0, -tbh.height());
                break;
            case QTabBar::RoundedEast:
            case QTabBar::TriangularEast:
                result.adjust(0, 0, -tbh.width(), 0);
                break;
            case QTabBar::RoundedWest:
            case QTabBar::TriangularWest:
                result.adjust(tbh.width(), 0, 0, 0);
                break;
            default:
                break;
        }
    }

    return result;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1728, as _ZNK19QDockAreaLayoutInfo4prevEi
inline int QDockAreaLayoutInfo::prev(int index) const
{
    for (int i = index - 1; i >= 0; --i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
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

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1046, as _ZNK22QMainWindowLayoutState8containsEP7QWidget
inline bool QMainWindowLayoutState::contains(QWidget *widget) const
{
#if QT_CONFIG(dockwidget)
    if (dockAreaLayout.centralWidgetItem != nullptr && dockAreaLayout.centralWidgetItem->widget() == widget)
        return true;
    if (!dockAreaLayout.indexOf(widget).isEmpty())
        return true;
#else
    if (centralWidgetItem && centralWidgetItem->widget() == widget)
        return true;
#endif

#if QT_CONFIG(toolbar)
    if (!toolBarAreaLayout.indexOf(widget).isEmpty())
        return true;
#endif
    return false;
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

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 1202, as _ZNK22QMainWindowLayoutState7isValidEv
inline bool QMainWindowLayoutState::isValid() const
{
    return rect.isValid();
}
//  -----------------------------------------------------------------------

//  void QMainWindowLayoutState::deleteCentralWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutState23deleteCentralWidgetItemEv(
    QMainWindowLayoutState *self) {
  self->deleteCentralWidgetItem();
}

//  QLayoutItem *QMainWindowLayoutState::itemAt(int index, int *x) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK22QMainWindowLayoutState6itemAtEiPi(
    const QMainWindowLayoutState *self,
    int index,
    int *x) {
  return self->itemAt(index, x);
}

//  bool QMainWindowLayoutState::contains(QWidget *widget) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QMainWindowLayoutState8containsEP7QWidget(
    const QMainWindowLayoutState *self,
    QWidget *widget) {
  return self->contains(widget);
}

//  void QMainWindowLayoutState::setCentralWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutState16setCentralWidgetEP7QWidget(
    QMainWindowLayoutState *self,
    QWidget *widget) {
  self->setCentralWidget(widget);
}

//  QWidget *QMainWindowLayoutState::centralWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK22QMainWindowLayoutState13centralWidgetEv(
    const QMainWindowLayoutState *self) {
  return self->centralWidget();
}

//  void QMainWindowLayoutState::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutState5clearEv(
    QMainWindowLayoutState *self) {
  self->clear();
}

//  bool QMainWindowLayoutState::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QMainWindowLayoutState7isValidEv(
    const QMainWindowLayoutState *self) {
  return self->isValid();
}

//  QMainWindowLayoutState::~QMainWindowLayoutState()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMainWindowLayoutStateD1Ev(QMainWindowLayoutState *self) {
  delete self;
}

//  a QList<int> a ritual of QMainWindowLayoutState gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMainWindowLayoutState__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(mainwindow)
#endif  // QT_CONFIG(mainwindow)
