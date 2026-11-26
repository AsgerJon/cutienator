//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qdockwidget.h>
#include <QtCore/qlist.h>
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

//  from src/widgets/widgets/qdockarealayout.cpp, line 2407, as _ZNK19QDockAreaLayoutInfo19tabIndexToListIndexEi
#if QT_CONFIG(tabbar)
inline int QDockAreaLayoutInfo::tabIndexToListIndex(int tabIndex) const
{
    Q_ASSERT(tabbed && tabBar);
    quintptr data = qvariant_cast<quintptr>(tabBar->tabData(tabIndex));
    for (int i = 0; i < item_list.size(); ++i) {
        if (tabId(item_list.at(i)) == data)
            return i;
    }
    return -1;
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 723, as _ZN22QDockWidgetGroupWindow10childEventEP11QChildEvent
#if QT_CONFIG(dockwidget)
inline void QDockWidgetGroupWindow::childEvent(QChildEvent *event)
{
    switch (event->type()) {
    case QEvent::ChildRemoved:
        if (auto *dockWidget = qobject_cast<QDockWidget *>(event->child()))
            dockWidget->removeEventFilter(this);
        destroyIfSingleItemLeft();
        break;
    case QEvent::ChildAdded:
        if (auto *dockWidget = qobject_cast<QDockWidget *>(event->child())) {
            dockWidget->installEventFilter(this);
            if (objectName().isEmpty())
                setObjectName(dockWidget->objectName() + QLatin1String("_groupWindow"));
        }
        break;
    default:
        break;
    }
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 359, as _ZN22QDockWidgetGroupWindow5eventEP6QEvent
#if QT_CONFIG(dockwidget)
inline bool QDockWidgetGroupWindow::event(QEvent *e)
{
    auto lay = static_cast<QDockWidgetGroupLayout *>(layout());
    if (lay && lay->windowEvent(e))
        return true;

    switch (e->type()) {
    case QEvent::Close:
#if QT_CONFIG(tabbar)
        // Forward the close to the QDockWidget just as if its close button was pressed
        if (QDockWidget *dw = activeTabbedDockWidget()) {
            dw->close();
            adjustFlags();
        }
#endif
        return true;
    case QEvent::Move:
#if QT_CONFIG(tabbar)
        // Let QDockWidgetPrivate::moseEvent handle the dragging
        if (QDockWidget *dw = activeTabbedDockWidget())
            static_cast<QDockWidgetPrivate *>(QObjectPrivate::get(dw))->moveEvent(static_cast<QMoveEvent*>(e));
#endif
        return true;
    case QEvent::NonClientAreaMouseMove:
    case QEvent::NonClientAreaMouseButtonPress:
    case QEvent::NonClientAreaMouseButtonRelease:
    case QEvent::NonClientAreaMouseButtonDblClick:
#if QT_CONFIG(tabbar)
        // Let the QDockWidgetPrivate of the currently visible dock widget handle the drag and drop
        if (QDockWidget *dw = activeTabbedDockWidget())
            static_cast<QDockWidgetPrivate *>(QObjectPrivate::get(dw))->nonClientAreaMouseEvent(static_cast<QMouseEvent*>(e));
#endif
        return true;
    case QEvent::ChildAdded:
        if (qobject_cast<QDockWidget *>(static_cast<QChildEvent*>(e)->child()))
            adjustFlags();
        break;
    case QEvent::LayoutRequest:
        // We might need to show the widget again
        destroyOrHideIfEmpty();
        break;
    case QEvent::Resize:
        updateCurrentGapRect();
        emit resized();
        break;
    default:
        break;
    }
    return QWidget::event(e);
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 743, as _ZN22QDockWidgetGroupWindow11eventFilterEP7QObjectP6QEvent
#if QT_CONFIG(dockwidget)
inline bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent *event)
{
    auto *dockWidget = qobject_cast<QDockWidget *>(obj);
    if (!dockWidget)
        return QWidget::eventFilter(obj, event);

    switch (event->type()) {
    case QEvent::Close:
        // We don't want closed dock widgets in a floating tab
        // => dock it to the main dock, before closing;
        reparentToMainWindow(dockWidget);
        dockWidget->setFloating(false);
        break;

    case QEvent::Hide:
        // if the dock widget is not an active tab, it is hidden anyway.
        // if it is the active tab, hide the whole group.
        if (dockWidget->isVisible())
            hide();
        break;

    default:
        break;
    }
    return QWidget::eventFilter(obj, event);
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 410, as _ZN22QDockWidgetGroupWindow10paintEventEP11QPaintEvent
#if QT_CONFIG(dockwidget)
inline void QDockWidgetGroupWindow::paintEvent(QPaintEvent *)
{
    QDockWidgetGroupLayout *lay = static_cast<QDockWidgetGroupLayout *>(layout());
    bool nativeDeco = lay->nativeWindowDeco();

    if (!nativeDeco) {
        QStyleOptionFrame framOpt;
        framOpt.initFrom(this);
        QStylePainter p(this);
        p.drawPrimitive(QStyle::PE_FrameDockWidget, framOpt);
    }
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qdockwidget.cpp, line 1083, as _ZN18QDockWidgetPrivate23nonClientAreaMouseEventEP11QMouseEvent
#if defined(Q_OS_LINUX)
inline void QDockWidgetPrivate::nonClientAreaMouseEvent(QMouseEvent *event)
{
    Q_Q(QDockWidget);

    int fw = q->style()->pixelMetric(QStyle::PM_DockWidgetFrameWidth, nullptr, q);

    QWidget *tl = q->topLevelWidget();
    QRect geo = tl->geometry();
    QRect titleRect = tl->frameGeometry();
    {
        titleRect.setLeft(geo.left());
        titleRect.setRight(geo.right());
        titleRect.setBottom(geo.top() - 1);
        titleRect.adjust(0, fw, 0, 0);
    }

    switch (event->type()) {
        case QEvent::NonClientAreaMouseButtonPress:
            if (!titleRect.contains(event->globalPosition().toPoint()))
                break;
            if (state != nullptr)
                break;
            if (qobject_cast<QMainWindow*>(parent) == nullptr && qobject_cast<QDockWidgetGroupWindow*>(parent) == nullptr)
                break;
            if (isAnimating())
                break;
            initDrag(event->position().toPoint(), true);
            if (state == nullptr)
                break;
            state->ctrlDrag = (event->modifiers() & Qt::ControlModifier) ||
                              (!hasFeature(this, QDockWidget::DockWidgetMovable) && q->isFloating());
            startDrag(DragScope::Group);
            break;
        case QEvent::NonClientAreaMouseMove:
            if (state == nullptr || !state->dragging)
                break;

#if !defined(Q_OS_MACOS) && !defined(Q_OS_WASM) && !defined(Q_OS_HARMONY)
            if (state->nca)
                endDrag(EndDragMode::LocationChange);
#endif
            break;
        case QEvent::NonClientAreaMouseButtonRelease:
#if defined(Q_OS_MACOS) || defined(Q_OS_WASM) || defined(Q_OS_HARMONY)
                        if (state)
                            endDrag(EndDragMode::LocationChange);
#endif
                        break;
        case QEvent::NonClientAreaMouseButtonDblClick:
            toggleTopLevel();
            break;
        default:
            break;
    }
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qdockarealayout.cpp, line 3440, as _ZN19QDockAreaLayoutInfo13separatorMoveERK5QListIiERK6QPointS6_
inline int QDockAreaLayoutInfo::separatorMove(const QList<int> &separator, const QPoint &origin,
                                       const QPoint &dest)
{
    int delta = 0;
    int index = separator.last();
    QDockAreaLayoutInfo *info = this->info(separator);
    delta = pick(info->o, dest - origin);
    if (delta != 0)
        delta = info->separatorMove(index, delta);
    info->apply(QWidgetAnimator::AnimationRule::Stop);
    return delta;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 423, as _ZNK22QDockWidgetGroupWindow10layoutInfoEv
#if QT_CONFIG(dockwidget)
inline QDockAreaLayoutInfo *QDockWidgetGroupWindow::layoutInfo() const
{
    return static_cast<QDockWidgetGroupLayout *>(layout())->dockAreaLayoutInfo();
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 434, as _ZNK22QDockWidgetGroupWindow13tabLayoutInfoEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline const QDockAreaLayoutInfo *QDockWidgetGroupWindow::tabLayoutInfo() const
{
    const QDockAreaLayoutInfo *info = layoutInfo();
    while (info && !info->tabbed) {
        // There should be only one tabbed subinfo otherwise we are not a floating tab but a real
        // window
        const QDockAreaLayoutInfo *next = nullptr;
        bool isSingle = false;
        for (const auto &item : info->item_list) {
            if (item.skip() || (item.flags & QDockAreaLayoutItem::GapItem))
                continue;
            if (next || isSingle) // Two visible things
                return nullptr;
            if (item.subinfo)
                next = item.subinfo;
            else if (item.widgetItem)
                isSingle = true;
        }
        if (isSingle)
            return info;
        info = next;
    }
    return info;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 462, as _ZNK22QDockWidgetGroupWindow22activeTabbedDockWidgetEv
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
inline QDockWidget *QDockWidgetGroupWindow::activeTabbedDockWidget() const
{
    QDockWidget *dw = nullptr;
    const QDockAreaLayoutInfo *info = tabLayoutInfo();
    if (!info)
        return nullptr;
    if (info->tabBar && info->tabBar->currentIndex() >= 0) {
        int i = info->tabIndexToListIndex(info->tabBar->currentIndex());
        if (i >= 0) {
            const QDockAreaLayoutItem &item = info->item_list.at(i);
            if (item.widgetItem)
                dw = qobject_cast<QDockWidget *>(item.widgetItem->widget());
        }
    }
    if (!dw) {
        for (int i = 0; !dw && i < info->item_list.size(); ++i) {
            const QDockAreaLayoutItem &item = info->item_list.at(i);
            if (item.skip())
                continue;
            if (!item.widgetItem)
                continue;
            dw = qobject_cast<QDockWidget *>(item.widgetItem->widget());
        }
    }
    return dw;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 543, as _ZNK22QDockWidgetGroupWindow21hasVisibleDockWidgetsEv
#if QT_CONFIG(dockwidget)
inline bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const
{
    const auto &children = findChildren<QDockWidget *>(Qt::FindChildrenRecursively);
    for (auto child : children) {
        // WA_WState_Visible is set on the dock widget, associated to the active tab
        // and unset on all others.
        // WA_WState_Hidden is set if the dock widgets have been explicitly hidden.
        // This is the relevant information to check (equivalent to !child->isHidden()).
        if (!child->testAttribute(Qt::WA_WState_Hidden))
            return true;
    }
    return false;
}
#endif  // QT_CONFIG(dockwidget)

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 613, as _ZNK22QDockWidgetGroupWindow14hasNativeDecosEv
#if QT_CONFIG(dockwidget)
inline bool QDockWidgetGroupWindow::hasNativeDecos() const
{
#if QT_CONFIG(tabbar)
    QDockWidget *dw = activeTabbedDockWidget();
    if (!dw) // We have a group of nested QDockWidgets (not just floating tabs)
        return true;

    if (!QDockWidgetLayout::wmSupportsNativeWindowDeco())
        return false;

    return dw->titleBarWidget() == nullptr;
#else
    return true;
#endif
}
#endif  // QT_CONFIG(dockwidget)
//  -----------------------------------------------------------------------

//  Only a class built on QDockWidgetGroupWindow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDockWidgetGroupWindow : QDockWidgetGroupWindow {
  using QDockWidgetGroupWindow::paintEvent;
};

//  const QMetaObject *QDockWidgetGroupWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDockWidgetGroupWindow10metaObjectEv(
    const QDockWidgetGroupWindow *self) {
  return self->metaObject();
}

//  void *QDockWidgetGroupWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QDockWidgetGroupWindow11qt_metacastEPKc(
    QDockWidgetGroupWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDockWidgetGroupWindow::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDockWidgetGroupWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QDockWidgetGroupWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if QT_CONFIG(dockwidget)
//  QDockAreaLayoutInfo *QDockWidgetGroupWindow::layoutInfo() const
extern "C" Q_DECL_EXPORT
QDockAreaLayoutInfo *ritual_ZNK22QDockWidgetGroupWindow10layoutInfoEv(
    const QDockWidgetGroupWindow *self) {
  return self->layoutInfo();
}
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(tabbar)
#if QT_CONFIG(dockwidget)
//  const QDockAreaLayoutInfo *QDockWidgetGroupWindow::tabLayoutInfo() const
extern "C" Q_DECL_EXPORT
const QDockAreaLayoutInfo *ritual_ZNK22QDockWidgetGroupWindow13tabLayoutInfoEv(
    const QDockWidgetGroupWindow *self) {
  return self->tabLayoutInfo();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
#if QT_CONFIG(dockwidget)
//  QDockWidget *QDockWidgetGroupWindow::activeTabbedDockWidget() const
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZNK22QDockWidgetGroupWindow22activeTabbedDockWidgetEv(
    const QDockWidgetGroupWindow *self) {
  return self->activeTabbedDockWidget();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(dockwidget)
//  bool QDockWidgetGroupWindow::hasVisibleDockWidgets() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDockWidgetGroupWindow21hasVisibleDockWidgetsEv(
    const QDockWidgetGroupWindow *self) {
  return self->hasVisibleDockWidgets();
}
#endif  // QT_CONFIG(dockwidget)

#if QT_CONFIG(tabbar)
#if QT_CONFIG(dockwidget)
//  bool QDockWidgetGroupWindow::hasNativeDecos() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDockWidgetGroupWindow14hasNativeDecosEv(
    const QDockWidgetGroupWindow *self) {
  return self->hasNativeDecos();
}
#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(tabbar)

//  void QDockWidgetGroupWindow::childEvent(QChildEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDockWidgetGroupWindow10childEventEP11QChildEvent(
    QDockWidgetGroupWindow *self,
    QChildEvent *event) {
  self->childEvent(event);
}

//  QList<QDockWidget *> QDockWidgetGroupWindow::dockWidgets() const
extern "C" Q_DECL_EXPORT
QList<QDockWidget *> *ritual_ZNK22QDockWidgetGroupWindow11dockWidgetsEv(
    const QDockWidgetGroupWindow *self) {
  return new QList<QDockWidget *>(self->dockWidgets());
}

//  void QDockWidgetGroupWindow::resized()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDockWidgetGroupWindow7resizedEv(
    QDockWidgetGroupWindow *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDockWidgetGroupWindow")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resized()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resized()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QDockWidgetGroupWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDockWidgetGroupWindow5eventEP6QEvent(
    QDockWidgetGroupWindow *self,
    QEvent *a0) {
  return self->event(a0);
}

//  bool QDockWidgetGroupWindow::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDockWidgetGroupWindow11eventFilterEP7QObjectP6QEvent(
    QDockWidgetGroupWindow *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

//  void QDockWidgetGroupWindow::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDockWidgetGroupWindow10paintEventEP11QPaintEvent(
    QDockWidgetGroupWindow *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
//  void QDockWidgetGroupWindow::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDockWidgetGroupWindow10paintEventEP11QPaintEvent(
    QDockWidgetGroupWindow *self,
    QPaintEvent *a0) {
  static_cast<OwnQDockWidgetGroupWindow *>(self)->OwnQDockWidgetGroupWindow::paintEvent(
      a0);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(dockwidget)

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(mainwindow)
#endif  // QT_CONFIG(mainwindow)
