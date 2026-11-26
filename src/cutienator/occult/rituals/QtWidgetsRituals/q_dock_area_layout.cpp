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
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtCore/QList>
#include <QtCore/QString>
#include <QtCore/QSet>
#include <QtWidgets/QWidget>
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1549, as _ZNK19QDockAreaLayoutInfo12hasFixedSizeEv
inline bool QDockAreaLayoutInfo::hasFixedSize() const
{
    return perp(o, minimumSize()) == perp(o, maximumSize());
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1440, as _ZNK19QDockAreaLayoutInfo13findSeparatorERK6QPoint
inline QList<int> QDockAreaLayoutInfo::findSeparator(const QPoint &_pos) const
{
#if QT_CONFIG(tabbar)
    if (tabbed)
        return QList<int>();
#endif

    int pos = pick(o, _pos);

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip() || (item.flags & QDockAreaLayoutItem::GapItem))
            continue;

        if (item.pos + item.size > pos) {
            if (item.subinfo != nullptr) {
                QList<int> result = item.subinfo->findSeparator(_pos);
                if (!result.isEmpty()) {
                    result.prepend(i);
                    return result;
                } else {
                    return QList<int>();
                }
            }
        }

        int next = this->next(i);
        if (next == -1 || (item_list.at(next).flags & QDockAreaLayoutItem::GapItem))
            continue;

        QRect sepRect = separatorRect(i);
        if (!sepRect.isNull() && *sep == 1)
            sepRect.adjust(-2, -2, 2, 2);
        //we also make sure we don't find a separator that's not there
        if (sepRect.contains(_pos) && !item.hasFixedSize(o)) {
            return QList<int>() << i;
        }

    }

    return QList<int>();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 292, as _ZNK19QDockAreaLayoutInfo7isEmptyEv
inline bool QDockAreaLayoutInfo::isEmpty() const
{
    return next(-1) == -1;
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 574, as _ZN19QDockAreaLayoutInfo8fitItemsEv
inline void QDockAreaLayoutInfo::fitItems()
{
#if QT_CONFIG(tabbar)
    if (tabbed) {
        return;
    }
#endif

    QList<QLayoutStruct> layout_struct_list(item_list.size() * 2);
    int j = 0;

    int size = pick(o, rect.size());
    int min_size = realMinSize(*this);
    int max_size = realMaxSize(*this);
    int last_index = -1;

    const QDockAreaLayoutItem *previous = nullptr;
    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item = item_list[i];
        if (item.skip())
            continue;

        bool gap = item.flags & QDockAreaLayoutItem::GapItem;
        if (previous && !gap) {
            if (!(previous->flags & QDockAreaLayoutItem::GapItem)) {
                QLayoutStruct &ls = layout_struct_list[j++];
                ls.init();
                ls.minimumSize = ls.maximumSize = ls.sizeHint = previous->hasFixedSize(o) ? 0 : *sep;
                ls.empty = false;
            }
        }

        if (item.flags & QDockAreaLayoutItem::KeepSize) {
            // Check if the item can keep its size, without violating size constraints
            // of other items.

            if (size < min_size) {
                // There is too little space to keep this widget's size
                item.flags &= ~QDockAreaLayoutItem::KeepSize;
                min_size -= item.size;
                min_size += pick(o, item.minimumSize());
                min_size = qMax(0, min_size);
            } else if (size > max_size) {
                // There is too much space to keep this widget's size
                item.flags &= ~QDockAreaLayoutItem::KeepSize;
                max_size -= item.size;
                max_size += pick(o, item.maximumSize());
                max_size = qMin<int>(QWIDGETSIZE_MAX, max_size);
            }
        }

        last_index = j;
        QLayoutStruct &ls = layout_struct_list[j++];
        ls.init();
        ls.empty = false;
        if (item.flags & QDockAreaLayoutItem::KeepSize) {
            ls.minimumSize = ls.maximumSize = ls.sizeHint = item.size;
            ls.expansive = false;
            ls.stretch = 0;
        } else {
            ls.maximumSize = pick(o, item.maximumSize());
            ls.expansive = item.expansive(o);
            ls.minimumSize = pick(o, item.minimumSize());
            ls.sizeHint = item.size == -1 ? pick(o, item.sizeHint()) : item.size;
            ls.stretch = ls.expansive ? ls.sizeHint : 0;
        }

        item.flags &= ~QDockAreaLayoutItem::KeepSize;
        previous = &item;
    }
    layout_struct_list.resize(j);

    // If there is more space than the widgets can take (due to maximum size constraints),
    // we detect it here and stretch the last widget to take up the rest of the space.
    if (size > max_size && last_index != -1) {
        layout_struct_list[last_index].maximumSize = QWIDGETSIZE_MAX;
        layout_struct_list[last_index].expansive = true;
    }

    qGeomCalc(layout_struct_list, 0, j, pick(o, rect.topLeft()), size, 0);

    j = 0;
    bool prev_gap = false;
    bool first = true;
    for (int i = 0; i < item_list.size(); ++i) {
        QDockAreaLayoutItem &item = item_list[i];
        if (item.skip())
            continue;

        bool gap = item.flags & QDockAreaLayoutItem::GapItem;
        if (!first && !gap && !prev_gap)
            ++j;

        const QLayoutStruct &ls = layout_struct_list.at(j++);
        item.size = ls.size;
        item.pos = ls.pos;

        if (item.subinfo != nullptr) {
            item.subinfo->rect = itemRect(i);
            item.subinfo->fitItems();
        }

        prev_gap = gap;
        first = false;
    }
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

//  from src/widgets/widgets/qdockwidget.cpp, line 569, as _ZN15QDockWidgetItemC1EP11QDockWidget
inline QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    : QWidgetItem(dockWidget)
{
}

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1738, as _ZN19QDockAreaLayoutInfo3tabEiP11QLayoutItem
#if QT_CONFIG(tabbar)
inline void QDockAreaLayoutInfo::tab(int index, QLayoutItem *dockWidgetItem)
{
    if (tabbed) {
        item_list.append(QDockAreaLayoutItem(dockWidgetItem));
        updateTabBar();
        setCurrentTab(dockWidgetItem->widget());
    } else {
        QDockAreaLayoutInfo *new_info
            = new QDockAreaLayoutInfo(sep, dockPos, o, tabBarShape, mainWindow);
        item_list[index].subinfo = new_info;
        new_info->item_list.append(QDockAreaLayoutItem(item_list.at(index).widgetItem));
        item_list[index].widgetItem = nullptr;
        new_info->item_list.append(QDockAreaLayoutItem(dockWidgetItem));
        new_info->tabbed = true;
        new_info->updateTabBar();
        new_info->setCurrentTab(dockWidgetItem->widget());
    }
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1684, as _ZNK19QDockAreaLayoutInfo15paintSeparatorsEP8QPainterP7QWidgetRK7QRegionRK6QPoint
inline void QDockAreaLayoutInfo::paintSeparators(QPainter *p, QWidget *widget,
                                                    const QRegion &clip,
                                                    const QPoint &mouse) const
{
    if (isEmpty())
        return;
#if QT_CONFIG(tabbar)
    if (tabbed)
        return;
#endif

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.skip())
            continue;

        int next = this->next(i);
        if ((item.flags & QDockAreaLayoutItem::GapItem)
                || (next != -1 && (item_list.at(next).flags & QDockAreaLayoutItem::GapItem)))
            continue;

        if (item.subinfo) {
            if (clip.contains(item.subinfo->rect))
                item.subinfo->paintSeparators(p, widget, clip, mouse);
        }

        if (next == -1)
            break;
        QRect r = separatorRect(i);
        if (clip.contains(r) && !item.hasFixedSize(o))
            paintSep(p, widget, r, o, r.contains(mouse));
    }
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2335, as _ZNK19QDockAreaLayoutInfo11usedTabBarsEv
#if QT_CONFIG(tabbar)
inline QSet<QTabBar*> QDockAreaLayoutInfo::usedTabBars() const
{
    QSet<QTabBar*> result;

    if (tabbed) {
        updateTabBar();
        result.insert(tabBar);
    }

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.subinfo != nullptr)
            result += item.subinfo->usedTabBars();
    }

    return result;
}
#endif  // QT_CONFIG(tabbar)

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 1719, as _ZNK19QDockAreaLayoutInfo4nextEi
inline int QDockAreaLayoutInfo::next(int index) const
{
    for (int i = index + 1; i < item_list.size(); ++i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
}

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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2327, as _ZNK19QDockAreaLayoutInfo14tabBarSizeHintEv
#if QT_CONFIG(tabbar)
inline QSize QDockAreaLayoutInfo::tabBarSizeHint() const
{
    if (!updateTabBar())
        return QSize(0, 0);

    return tabBar->sizeHint();
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 2428, as _ZN15QDockAreaLayoutC1EP11QMainWindow
inline QDockAreaLayout::QDockAreaLayout(QMainWindow *win) : fallbackToSizeHints(true)
{
    mainWindow = win;
    sep = win->style()->pixelMetric(QStyle::PM_DockWidgetSeparatorExtent, nullptr, win);
#if QT_CONFIG(tabbar)
    const int tabShape = QTabBar::RoundedSouth;
#else
    const int tabShape = 0;
#endif
    docks[QInternal::LeftDock]
        = QDockAreaLayoutInfo(&sep, QInternal::LeftDock, Qt::Vertical, tabShape, win);
    docks[QInternal::RightDock]
        = QDockAreaLayoutInfo(&sep, QInternal::RightDock, Qt::Vertical, tabShape, win);
    docks[QInternal::TopDock]
        = QDockAreaLayoutInfo(&sep, QInternal::TopDock, Qt::Horizontal, tabShape, win);
    docks[QInternal::BottomDock]
        = QDockAreaLayoutInfo(&sep, QInternal::BottomDock, Qt::Horizontal, tabShape, win);
    centralWidgetItem = nullptr;


    corners[Qt::TopLeftCorner] = Qt::TopDockWidgetArea;
    corners[Qt::TopRightCorner] = Qt::TopDockWidgetArea;
    corners[Qt::BottomLeftCorner] = Qt::BottomDockWidgetArea;
    corners[Qt::BottomRightCorner] = Qt::BottomDockWidgetArea;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 2454, as _ZNK15QDockAreaLayout7isValidEv
inline bool QDockAreaLayout::isValid() const
{
    return rect.isValid();
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2522, as _ZNK15QDockAreaLayout18indexOfPlaceHolderERK7QString
inline QList<int> QDockAreaLayout::indexOfPlaceHolder(const QString &objectName) const
{
    for (std::size_t i = 0; i < docks.size(); ++i) {
        QList<int> result = docks[i].indexOfPlaceHolder(objectName);
        if (!result.isEmpty()) {
            result.prepend(int(i));
            return result;
        }
    }
    return QList<int>();
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2700, as _ZNK15QDockAreaLayout13separatorRectEi
inline QRect QDockAreaLayout::separatorRect(int index) const
{
    const QDockAreaLayoutInfo &dock = docks[index];
    if (dock.isEmpty())
        return QRect();
    QRect r = dock.rect;
    switch (index) {
        case QInternal::LeftDock:
            return QRect(r.right() + 1, r.top(), sep, r.height());
        case QInternal::RightDock:
            return QRect(r.left() - sep, r.top(), sep, r.height());
        case QInternal::TopDock:
            return QRect(r.left(), r.bottom() + 1, r.width(), sep);
        case QInternal::BottomDock:
            return QRect(r.left(), r.top() - sep, r.width(), sep);
        default:
            break;
    }
    return QRect();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 3076, as _ZN15QDockAreaLayout5clearEv
inline void QDockAreaLayout::clear()
{
    for (auto &dock : docks)
        dock.clear();

    rect = QRect();
    centralWidgetRect = QRect();
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 3543, as _ZNK15QDockAreaLayout20usedSeparatorWidgetsEv
#if QT_CONFIG(tabbar)
inline QSet<QWidget*> QDockAreaLayout::usedSeparatorWidgets() const
{
    QSet<QWidget*> result;
    const int numSeparators = separatorWidgets.size();
    result.reserve(numSeparators);
    for (int i = 0; i < numSeparators; ++i)
        result << separatorWidgets.at(i);
    for (const auto &dock : docks)
        result += dock.usedSeparatorWidgets();
    return result;
}
#endif  // QT_CONFIG(tabbar)
//  -----------------------------------------------------------------------

//  QDockAreaLayout::QDockAreaLayout(QMainWindow *win)
extern "C" Q_DECL_EXPORT
QDockAreaLayout *ritual_ZN15QDockAreaLayoutC1EP11QMainWindow(
    QMainWindow *win) {
  return new QDockAreaLayout(win);
}

//  bool QDockAreaLayout::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDockAreaLayout7isValidEv(const QDockAreaLayout *self) {
  return self->isValid();
}

//  QRect QDockAreaLayout::constrainedRect(QRect rect, QWidget *widget)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15QDockAreaLayout15constrainedRectE5QRectP7QWidget(
    const QRect *rect,
    QWidget *widget) {
  return new QRect(QDockAreaLayout::constrainedRect(*rect, widget));
}

//  QList<int> QDockAreaLayout::indexOfPlaceHolder(const QString &objectName)
//      const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK15QDockAreaLayout18indexOfPlaceHolderERK7QString(
    const QDockAreaLayout *self,
    const QString *objectName) {
  return new QList<int>(self->indexOfPlaceHolder(*objectName));
}

//  QList<int> QDockAreaLayout::indexOf(const QWidget *dockWidget) const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK15QDockAreaLayout7indexOfEPK7QWidget(
    const QDockAreaLayout *self,
    const QWidget *dockWidget) {
  return new QList<int>(self->indexOf(dockWidget));
}

//  QRect QDockAreaLayout::separatorRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QDockAreaLayout13separatorRectEi(
    const QDockAreaLayout *self,
    int index) {
  return new QRect(self->separatorRect(index));
}

//  void QDockAreaLayout::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDockAreaLayout5clearEv(QDockAreaLayout *self) {
  self->clear();
}

//  QLayoutItem *QDockAreaLayout::itemAt(int *x, int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK15QDockAreaLayout6itemAtEPii(
    const QDockAreaLayout *self,
    int *x,
    int index) {
  return self->itemAt(x, index);
}

#if QT_CONFIG(tabbar)
//  QSet<QWidget *> QDockAreaLayout::usedSeparatorWidgets() const
extern "C" Q_DECL_EXPORT
QSet<QWidget *> *ritual_ZNK15QDockAreaLayout20usedSeparatorWidgetsEv(
    const QDockAreaLayout *self) {
  return new QSet<QWidget *>(self->usedSeparatorWidgets());
}
#endif  // QT_CONFIG(tabbar)

//  QDockAreaLayout::~QDockAreaLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDockAreaLayoutD1Ev(QDockAreaLayout *self) {
  delete self;
}

//  a QList<int> a ritual of QDockAreaLayout gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayout__QList_int(QList<int> *self) {
  delete self;
}

//  a QSet<QTabBar *> a ritual of QDockAreaLayout gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayout__QSet_QTabBar(QSet<QTabBar *> *self) {
  delete self;
}

//  a QSet<QWidget *> a ritual of QDockAreaLayout gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDockAreaLayout__QSet_QWidget(QSet<QWidget *> *self) {
  delete self;
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
