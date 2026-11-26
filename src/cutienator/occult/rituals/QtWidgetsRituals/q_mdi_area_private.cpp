//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qmdiarea.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtWidgets/qmdisubwindow.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qmdiarea_p.h>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStyle>
#include <QtCore/QChildEvent>
#include <QtGui/QResizeEvent>
#include <QtWidgets/QScrollBar>
#include <QtCore/QtAlgorithms>
#include <QtGui/QPainter>
#include <QtGui/QFontMetrics>
#include <QtWidgets/QStyleOption>
#include <QtCore/QDebug>
#include <QtCore/qmath.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtWidgets/private/qlayoutengine_p.h>
#include <algorithm>
#include <QtWidgets/qabstractscrollarea.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qboxlayout.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmargins.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#include <QtCore/QDebug>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtWidgets/private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif
#include <QtWidgets/private/qmdisubwindow_p.h>
#include <QtWidgets/QApplication>
#include <QtWidgets/QStylePainter>
#include <QtWidgets/QVBoxLayout>
#include <QtGui/QMouseEvent>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/QWhatsThis>
#endif
#if QT_CONFIG(tooltip)
#include <QtWidgets/QToolTip>
#endif
#if QT_CONFIG(mainwindow)
#include <QtWidgets/QMainWindow>
#endif
#include <QtWidgets/QScrollBar>
#include <QtCore/QDebug>
#include <QtWidgets/QMdiArea>
#include <QtCore/QScopedValueRollback>
#if QT_CONFIG(action)
#  include <QtWidgets/qaction.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/QMenu>
#endif
#include <QtWidgets/QProxyStyle>
#include <QtWidgets/qframe.h>
#include <QtGui/qbitmap.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qframe_p.h>
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

//  from src/widgets/widgets/qmdiarea.cpp, line 147, as local:qmdiarea.cpp:sanityCheck
static bool sanityCheck(const QMdiSubWindow * const child, const char *where)
{
    if (Q_UNLIKELY(!child)) {
        const char error[] = "null pointer";
        Q_ASSERT_X(false, where, error);
        qWarning("%s:%s", where, error);
        return false;
    }
    return true;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 175, as local:qmdiarea.cpp:setIndex
static void setIndex(int *index, int candidate, int min, int max, bool isIncreasing)
{
    if (!index)
        return;

    if (isIncreasing) {
        if (candidate > max)
            *index = min;
        else
            *index = qMax(candidate, min);
    } else {
        if (candidate < min)
            *index = max;
        else
            *index = qMin(candidate, max);
    }
    Q_ASSERT(*index >= min && *index <= max);
}

//  from src/widgets/widgets/qmdiarea.cpp, line 194, as local:qmdiarea.cpp:useScrollBar
static inline bool useScrollBar(const QRect &childrenRect, const QSize &maxViewportSize,
                                Qt::Orientation orientation)
{
    if (orientation == Qt::Horizontal)
        return  childrenRect.width() > maxViewportSize.width()
                || childrenRect.left() < 0
                || childrenRect.right() >= maxViewportSize.width();
    else
        return childrenRect.height() > maxViewportSize.height()
               || childrenRect.top() < 0
               || childrenRect.bottom() >= maxViewportSize.height();
}

//  from src/widgets/widgets/qmdiarea.cpp, line 518, as local:qmdiarea.cpp:QMdiAreaTabBar
#if QT_CONFIG(tabbar)
class QMdiAreaTabBar : public QTabBar
{
public:
    QMdiAreaTabBar(QWidget *parent) : QTabBar(parent) {}

protected:
    void mousePressEvent(QMouseEvent *event) override;
#ifndef QT_NO_CONTEXTMENU
    void contextMenuEvent(QContextMenuEvent *event) override;
#endif

private:
    QMdiSubWindow *subWindowFromIndex(int index) const;
};
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qmdiarea.cpp, line 536, as local:qmdiarea.cpp:QMdiAreaTabBar::mousePressEvent
#if QT_CONFIG(tabbar)
inline void QMdiAreaTabBar::mousePressEvent(QMouseEvent *event)
{
    if (event->button() != Qt::MiddleButton) {
        QTabBar::mousePressEvent(event);
        return;
    }

    QMdiSubWindow *subWindow = subWindowFromIndex(tabAt(event->position().toPoint()));
    if (!subWindow) {
        event->ignore();
        return;
    }

    subWindow->close();
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qmdiarea.cpp, line 556, as local:qmdiarea.cpp:QMdiAreaTabBar::contextMenuEvent
#if QT_CONFIG(tabbar)
#if !defined(QT_NO_CONTEXTMENU)
inline void QMdiAreaTabBar::contextMenuEvent(QContextMenuEvent *event)
{
    QPointer<QMdiSubWindow> subWindow = subWindowFromIndex(tabAt(event->pos()));
    if (!subWindow || subWindow->isHidden()) {
        event->ignore();
        return;
    }

#if QT_CONFIG(menu)
    QMdiSubWindowPrivate *subWindowPrivate = subWindow->d_func();
    if (!subWindowPrivate->systemMenu) {
        event->ignore();
        return;
    }

    QMdiSubWindow *currentSubWindow = subWindowFromIndex(currentIndex());
    Q_ASSERT(currentSubWindow);

    // We don't want these actions to show up in the system menu when the
    // current sub-window is maximized, i.e. covers the entire viewport.
    if (currentSubWindow->isMaximized()) {
        subWindowPrivate->setVisible(QMdiSubWindowPrivate::MoveAction, false);
        subWindowPrivate->setVisible(QMdiSubWindowPrivate::ResizeAction, false);
        subWindowPrivate->setVisible(QMdiSubWindowPrivate::MinimizeAction, false);
        subWindowPrivate->setVisible(QMdiSubWindowPrivate::MaximizeAction, false);
        subWindowPrivate->setVisible(QMdiSubWindowPrivate::RestoreAction, false);
        subWindowPrivate->setVisible(QMdiSubWindowPrivate::StayOnTopAction, false);
    }

    // Show system menu.
    subWindowPrivate->systemMenu->exec(event->globalPos());
    if (!subWindow)
        return;

    // Restore action visibility.
    subWindowPrivate->updateActions();
#endif // QT_CONFIG(menu)
}
#endif  // !defined(QT_NO_CONTEXTMENU)
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qmdiarea.cpp, line 599, as local:qmdiarea.cpp:QMdiAreaTabBar::subWindowFromIndex
#if QT_CONFIG(tabbar)
inline QMdiSubWindow *QMdiAreaTabBar::subWindowFromIndex(int index) const
{
    if (index < 0 || index >= count())
        return nullptr;

    QMdiArea *mdiArea = qobject_cast<QMdiArea *>(parentWidget());
    Q_ASSERT(mdiArea);

    const QList<QMdiSubWindow *> subWindows = mdiArea->subWindowList();
    Q_ASSERT(index < subWindows.size());

    QMdiSubWindow *subWindow = mdiArea->subWindowList().at(index);
    Q_ASSERT(subWindow);

    return subWindow;
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 215, as local:qmdisubwindow.cpp:isChildOfTabbedQMdiArea
static inline bool isChildOfTabbedQMdiArea(const QMdiSubWindow *child)
{
    Q_ASSERT(child);
    if (QMdiArea *mdiArea = child->mdiArea()) {
        if (mdiArea->viewMode() == QMdiArea::TabbedView)
            return true;
    }
    return false;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1334, as _ZN15QMdiAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE
inline void QMdiAreaPrivate::scrollBarPolicyChanged(Qt::Orientation orientation, Qt::ScrollBarPolicy policy)
{
    if (childWindows.isEmpty())
        return;

    const QMdiSubWindow::SubWindowOption option = orientation == Qt::Horizontal ?
        QMdiSubWindow::AllowOutsideAreaHorizontally : QMdiSubWindow::AllowOutsideAreaVertically;
    const bool enable = policy != Qt::ScrollBarAlwaysOff;
    // Take a copy because child->setOption() may indirectly call QCoreApplication::sendEvent(),
    // the latter could call unknown code that could e.g. recurse into the class
    // modifying childWindows.
    const auto subWindows = childWindows;
    for (QMdiSubWindow *child : subWindows) {
        if (!sanityCheck(child, "QMdiArea::scrollBarPolicyChanged"))
            continue;
        child->setOption(option, enable);
    }
    updateScrollBars();
}

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 133, as _ZN26QAbstractScrollAreaPrivateC2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
    :hbar(nullptr), vbar(nullptr), vbarpolicy(Qt::ScrollBarAsNeeded), hbarpolicy(Qt::ScrollBarAsNeeded),
     shownOnce(false), inResize(false), sizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored),
     viewport(nullptr), cornerWidget(nullptr), left(0), top(0), right(0), bottom(0),
     xoffset(0), yoffset(0), viewportFilter(nullptr)
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 141, as _ZN26QAbstractScrollAreaPrivateD2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1368, as _ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv
#if QT_CONFIG(scrollarea)
inline QPoint QAbstractScrollAreaPrivate::contentsOffset() const
{
    Q_Q(const QAbstractScrollArea);
    QPoint offset;
    if (vbar->isVisible())
        offset.setY(vbar->value());
    if (hbar->isVisible()) {
        if (q->isRightToLeft())
            offset.setX(hbar->maximum() - hbar->value());
        else
            offset.setX(hbar->value());
    }
    return offset;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1315, as _ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint
#if QT_CONFIG(scrollarea)
inline bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint &startPos) const
{
    Q_Q(const QAbstractScrollArea);

    // don't start scrolling on a QAbstractSlider
    if (qobject_cast<QAbstractSlider *>(q->viewport()->childAt(startPos)))
        return false;

    return true;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1416, as _ZN20QMdiSubWindowPrivate9setActiveEbb
inline void QMdiSubWindowPrivate::setActive(bool activate, bool changeFocus)
{
    Q_Q(QMdiSubWindow);
    if (!parent || !activationEnabled)
        return;

    if (activate && !isActive && q->isEnabled()) {
        isActive = true;
        isExplicitlyDeactivated = false;
        Qt::WindowStates oldWindowState = q->windowState();
        ensureWindowState(Qt::WindowActive);
        emit q->aboutToActivate();
#if QT_CONFIG(menubar)
        if (QMenuBar *mBar = menuBar())
            showButtonsInMenuBar(mBar);
#endif
        Q_ASSERT(isActive);
        emit q->windowStateChanged(oldWindowState, q->windowState());
    } else if (!activate && isActive) {
        isActive = false;
        Qt::WindowStates oldWindowState = q->windowState();
        q->overrideWindowState(q->windowState() & ~Qt::WindowActive);
        if (changeFocus) {
            storeFocusWidget();
            QWidget *focusWidget = QApplication::focusWidget();
            if (focusWidget && (focusWidget == q || q->isAncestorOf(focusWidget)))
                focusWidget->clearFocus();
        }
        if (baseWidget)
            baseWidget->overrideWindowState(baseWidget->windowState() & ~Qt::WindowActive);
        Q_ASSERT(!isActive);
        emit q->windowStateChanged(oldWindowState, q->windowState());
    }

    if (activate && isActive && q->isEnabled() && !q->hasFocus()
            && !q->isAncestorOf(QApplication::focusWidget())) {
        if (changeFocus)
            setFocusWidget();
        ensureWindowState(Qt::WindowActive);
    }

    int frameWidth = q->style()->pixelMetric(QStyle::PM_MdiSubWindowFrameWidth, nullptr, q);
    int titleBarHeight = this->titleBarHeight();
    QRegion windowDecoration = QRegion(0, 0, q->width(), q->height());
    windowDecoration -= QRegion(frameWidth, titleBarHeight, q->width() - 2 * frameWidth,
                                q->height() - titleBarHeight - frameWidth);

    // Make sure we don't use cached style options if we get
    // resize events right before activation/deactivation.
    if (resizeTimer.isActive()) {
        resizeTimer.stop();
        updateDirtyRegions();
    }

    q->update(windowDecoration);
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1006, as _ZN15QMdiAreaPrivate19emitWindowActivatedEP13QMdiSubWindow
inline void QMdiAreaPrivate::emitWindowActivated(QMdiSubWindow *activeWindow)
{
    Q_Q(QMdiArea);
    Q_ASSERT(activeWindow);
    if (activeWindow == active)
        return;
    Q_ASSERT(activeWindow->d_func()->isActive);

    if (!aboutToBecomeActive)
        _q_deactivateAllWindows(activeWindow);
    Q_ASSERT(aboutToBecomeActive);

    // This is true only if 'DontMaximizeSubWindowOnActivation' is disabled
    // and the previous active window was maximized.
    if (showActiveWindowMaximized) {
        if (!activeWindow->isMaximized())
            activeWindow->showMaximized();
        showActiveWindowMaximized = false;
    }

    // Put in front to update activation order.
    const int indexToActiveWindow = childWindows.indexOf(activeWindow);
    Q_ASSERT(indexToActiveWindow != -1);
    const int index = indicesToActivatedChildren.indexOf(indexToActiveWindow);
    Q_ASSERT(index != -1);
    indicesToActivatedChildren.move(index, 0);
    internalRaise(activeWindow);

    if (updatesDisabledByUs) {
        q->setUpdatesEnabled(true);
        updatesDisabledByUs = false;
    }

    Q_ASSERT(aboutToBecomeActive == activeWindow);
    active = activeWindow;
    aboutToBecomeActive = nullptr;
    Q_ASSERT(active->d_func()->isActive);

#if QT_CONFIG(tabbar)
    if (tabBar && tabBar->currentIndex() != indexToActiveWindow)
        tabBar->setCurrentIndex(indexToActiveWindow);
#endif

    if (active->isMaximized() && scrollBarsEnabled())
        updateScrollBars();

    emit q->subWindowActivated(active);
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1200, as _ZNK15QMdiAreaPrivate13internalRaiseEP13QMdiSubWindow
inline void QMdiAreaPrivate::internalRaise(QMdiSubWindow *mdiChild) const
{
    if (!sanityCheck(mdiChild, "QMdiArea::internalRaise") || childWindows.size() < 2)
        return;

    QMdiSubWindow *stackUnderChild = nullptr;
    if (!windowStaysOnTop(mdiChild)) {
        const auto children = viewport->children(); // take a copy, as raising/stacking under changes the order
        for (QObject *object : children) {
            QMdiSubWindow *child = qobject_cast<QMdiSubWindow *>(object);
            if (!child || !childWindows.contains(child))
                continue;
            if (!child->isHidden() && windowStaysOnTop(child)) {
                if (stackUnderChild)
                    child->stackUnder(stackUnderChild);
                else
                    child->raise();
                stackUnderChild = child;
            }
        }
    }

    if (stackUnderChild)
        mdiChild->stackUnder(stackUnderChild);
    else
        mdiChild->raise();
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1411, as _ZNK15QMdiAreaPrivate20nextVisibleSubWindowEiN8QMdiArea11WindowOrderEii
inline QMdiSubWindow *QMdiAreaPrivate::nextVisibleSubWindow(int increaseFactor, QMdiArea::WindowOrder order,
                                                     int removedIndex, int fromIndex) const
{
    if (childWindows.isEmpty())
        return nullptr;

    Q_Q(const QMdiArea);
    const QList<QMdiSubWindow *> subWindows = q->subWindowList(order);
    QMdiSubWindow *current = nullptr;

    if (removedIndex < 0) {
        if (fromIndex >= 0 && fromIndex < subWindows.size())
            current = childWindows.at(fromIndex);
        else
            current = q->currentSubWindow();
    }

    // There's no current sub-window (removed or deactivated),
    // so we have to pick the last active or the next in creation order.
    if (!current) {
        if (removedIndex >= 0 && order == QMdiArea::CreationOrder) {
            int candidateIndex = -1;
            setIndex(&candidateIndex, removedIndex, 0, subWindows.size() - 1, true);
            current = childWindows.at(candidateIndex);
        } else {
            current = subWindows.back();
        }
    }
    Q_ASSERT(current);

    // Find the index for the current sub-window in the given activation order
    const int indexToCurrent = subWindows.indexOf(current);
    const bool increasing = increaseFactor > 0;

    // and use that index + increseFactor as a candidate.
    int index = -1;
    setIndex(&index, indexToCurrent + increaseFactor, 0, subWindows.size() - 1, increasing);
    Q_ASSERT(index != -1);

    // Try to find another window if the candidate is hidden.
    while (subWindows.at(index)->isHidden()) {
        setIndex(&index, index + increaseFactor, 0, subWindows.size() - 1, increasing);
        if (index == indexToCurrent)
            break;
    }

    if (!subWindows.at(index)->isHidden())
        return subWindows.at(index);
    return nullptr;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1506, as _ZN15QMdiAreaPrivate17showRubberBandForEP13QMdiSubWindow
#if QT_CONFIG(rubberband)
inline void QMdiAreaPrivate::showRubberBandFor(QMdiSubWindow *subWindow)
{
    if (!subWindow || !rubberBand)
        return;

#if QT_CONFIG(tabbar)
    if (viewMode == QMdiArea::TabbedView)
        rubberBand->setGeometry(tabBar->tabRect(childWindows.indexOf(subWindow)));
    else
#endif
        rubberBand->setGeometry(subWindow->geometry());

    rubberBand->raise();
    rubberBand->show();
}
#endif  // QT_CONFIG(rubberband)

//  from src/widgets/widgets/qframe.cpp, line 19, as _ZN13QFramePrivateC2Ev
inline QFramePrivate::QFramePrivate()
    : frect(0, 0, 0, 0),
      frameStyle(QFrame::NoFrame | QFrame::Plain),
      lineWidth(1),
      midLineWidth(0),
      frameWidth(0),
      leftFrameWidth(0), rightFrameWidth(0),
      topFrameWidth(0), bottomFrameWidth(0)
{
}

//  from src/widgets/widgets/qframe.cpp, line 30, as _ZN13QFramePrivateD2Ev
inline QFramePrivate::~QFramePrivate()
{
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1132, as _ZN15QMdiAreaPrivate16updateScrollBarsEv
inline void QMdiAreaPrivate::updateScrollBars()
{
    if (ignoreGeometryChange || !scrollBarsEnabled())
        return;

    Q_Q(QMdiArea);
    QSize maxSize = q->maximumViewportSize();
    QSize hbarExtent = hbar->sizeHint();
    QSize vbarExtent = vbar->sizeHint();

    if (q->style()->styleHint(QStyle::SH_ScrollView_FrameOnlyAroundContents, nullptr, q)) {
        const int doubleFrameWidth = frameWidth * 2;
        if (hbarpolicy == Qt::ScrollBarAlwaysOn)
            maxSize.rheight() -= doubleFrameWidth;
        if (vbarpolicy == Qt::ScrollBarAlwaysOn)
            maxSize.rwidth() -= doubleFrameWidth;
        hbarExtent.rheight() += doubleFrameWidth;
        vbarExtent.rwidth() += doubleFrameWidth;
    }

    const QRect childrenRect = active && active->isMaximized()
                               ? active->geometry() : viewport->childrenRect();
    bool useHorizontalScrollBar = useScrollBar(childrenRect, maxSize, Qt::Horizontal);
    bool useVerticalScrollBar = useScrollBar(childrenRect, maxSize, Qt::Vertical);

    if (useHorizontalScrollBar && !useVerticalScrollBar) {
        const QSize max = maxSize - QSize(0, hbarExtent.height());
        useVerticalScrollBar = useScrollBar(childrenRect, max, Qt::Vertical);
    }

    if (useVerticalScrollBar && !useHorizontalScrollBar) {
        const QSize max = maxSize - QSize(vbarExtent.width(), 0);
        useHorizontalScrollBar = useScrollBar(childrenRect, max, Qt::Horizontal);
    }

    if (useHorizontalScrollBar && hbarpolicy != Qt::ScrollBarAlwaysOn)
        maxSize.rheight() -= hbarExtent.height();
    if (useVerticalScrollBar && vbarpolicy != Qt::ScrollBarAlwaysOn)
        maxSize.rwidth() -= vbarExtent.width();

    QRect viewportRect(QPoint(0, 0), maxSize);
    const int startX = q->isLeftToRight() ? childrenRect.left() : viewportRect.right()
                                                                  - childrenRect.right();

    const auto singleStep = defaultSingleStep();

    // Horizontal scroll bar.
    if (isSubWindowsTiled && hbar->value() != 0)
        hbar->setValue(0);
    const int xOffset = startX + hbar->value();
    hbar->setRange(qMin(0, xOffset),
                   qMax(0, xOffset + childrenRect.width() - viewportRect.width()));
    hbar->setPageStep(childrenRect.width());
    hbar->setSingleStep(childrenRect.width() / singleStep);

    // Vertical scroll bar.
    if (isSubWindowsTiled && vbar->value() != 0)
        vbar->setValue(0);
    const int yOffset = childrenRect.top() + vbar->value();
    vbar->setRange(qMin(0, yOffset),
                   qMax(0, yOffset + childrenRect.height() - viewportRect.height()));
    vbar->setPageStep(childrenRect.height());
    vbar->setSingleStep(childrenRect.height() / singleStep);
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1965, as _ZN20QMdiSubWindowPrivate14setFocusWidgetEv
inline void QMdiSubWindowPrivate::setFocusWidget()
{
    Q_Q(QMdiSubWindow);
    if (!baseWidget) {
        q->setFocus();
        return;
    }

    // This will give focus to the next child if possible, otherwise
    // do nothing, hence it's not possible to tab between windows with
    // just hitting tab (unless Qt::TabFocus is removed from the focus policy).
    if (focusInReason == Qt::TabFocusReason) {
        q->focusNextChild();
        return;
    }

    // Same as above, but gives focus to the previous child.
    if (focusInReason == Qt::BacktabFocusReason) {
        q->focusPreviousChild();
        return;
    }

    if (!(q->windowState() & Qt::WindowMinimized) && restoreFocus())
        return;

    if (QWidget *focusWidget = baseWidget->focusWidget()) {
        if (!focusWidget->hasFocus() && q->isAncestorOf(focusWidget)
                && focusWidget->isVisible() && !q->isMinimized()
                && focusWidget->focusPolicy() != Qt::NoFocus) {
            focusWidget->setFocus();
        } else {
            q->setFocus();
        }
        return;
    }

    QWidget *focusWidget = q->nextInFocusChain();
    while (focusWidget && focusWidget != q && focusWidget->focusPolicy() == Qt::NoFocus)
        focusWidget = focusWidget->nextInFocusChain();
    if (focusWidget && q->isAncestorOf(focusWidget))
        focusWidget->setFocus();
    else if (baseWidget->focusPolicy() != Qt::NoFocus)
        baseWidget->setFocus();
    else if (!q->hasFocus())
        q->setFocus();
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1317, as _ZN20QMdiSubWindowPrivate16storeFocusWidgetEv
inline void QMdiSubWindowPrivate::storeFocusWidget()
{
    if (QWidget *focus = QApplication::focusWidget()) {
        if (!restoreFocusWidget && q_func()->isAncestorOf(focus))
            restoreFocusWidget = focus;
    }
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1668, as _ZN20QMdiSubWindowPrivate17ensureWindowStateEN2Qt11WindowStateE
inline void QMdiSubWindowPrivate::ensureWindowState(Qt::WindowState state)
{
    Q_Q(QMdiSubWindow);
    Qt::WindowStates windowStates = q->windowState() | state;
    switch (state) {
    case Qt::WindowMinimized:
        windowStates &= ~Qt::WindowMaximized;
        windowStates &= ~Qt::WindowFullScreen;
        windowStates &= ~Qt::WindowNoState;
        break;
    case Qt::WindowMaximized:
        windowStates &= ~Qt::WindowMinimized;
        windowStates &= ~Qt::WindowFullScreen;
        windowStates &= ~Qt::WindowNoState;
        break;
    case Qt::WindowNoState:
        windowStates &= ~Qt::WindowMinimized;
        windowStates &= ~Qt::WindowMaximized;
        windowStates &= ~Qt::WindowFullScreen;
        break;
    default:
        break;
    }
    if (baseWidget) {
        if (!(baseWidget->windowState() & Qt::WindowActive) && windowStates & Qt::WindowActive)
            baseWidget->overrideWindowState(windowStates & ~Qt::WindowActive);
        else
            baseWidget->overrideWindowState(windowStates);
    }
    q->overrideWindowState(windowStates);
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1088, as _ZN20QMdiSubWindowPrivate18updateDirtyRegionsEv
inline void QMdiSubWindowPrivate::updateDirtyRegions()
{
    // No update necessary
    if (!parent)
        return;

    for (OperationInfoMap::iterator it = operationMap.begin(), end = operationMap.end(); it != end; ++it)
        it.value().region = getRegion(it.key());
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1613, as _ZNK20QMdiSubWindowPrivate15titleBarOptionsEv
inline QStyleOptionTitleBar QMdiSubWindowPrivate::titleBarOptions() const
{
    Q_Q(const QMdiSubWindow);
    QStyleOptionTitleBar titleBarOptions;
    titleBarOptions.initFrom(q);
    if (activeSubControl != QStyle::SC_None) {
        if (hoveredSubControl == activeSubControl) {
            titleBarOptions.state |= QStyle::State_Sunken;
            titleBarOptions.activeSubControls = activeSubControl;
        }
    } else if (autoRaise() && hoveredSubControl != QStyle::SC_None
               && hoveredSubControl != QStyle::SC_TitleBarLabel) {
        titleBarOptions.state |= QStyle::State_MouseOver;
        titleBarOptions.activeSubControls = hoveredSubControl;
    } else {
        titleBarOptions.state &= ~QStyle::State_MouseOver;
        titleBarOptions.activeSubControls = QStyle::SC_None;
    }

    titleBarOptions.subControls = QStyle::SC_All;
    titleBarOptions.titleBarFlags = q->windowFlags();
    titleBarOptions.titleBarState = q->windowState();
    titleBarOptions.palette = titleBarPalette;
    titleBarOptions.icon = menuIcon;

    if (isActive) {
        titleBarOptions.state |= QStyle::State_Active;
        titleBarOptions.titleBarState |= QStyle::State_Active;
        titleBarOptions.palette.setCurrentColorGroup(QPalette::Active);
    } else {
        titleBarOptions.state &= ~QStyle::State_Active;
        titleBarOptions.palette.setCurrentColorGroup(QPalette::Inactive);
    }

    int border = hasBorder(titleBarOptions) ? 4 : 0;
    int paintHeight = titleBarHeight(titleBarOptions);
    paintHeight -= q->isMinimized() ? 2 * border : border;
    titleBarOptions.rect = QRect(border, border, q->width() - 2 * border, paintHeight);

    if (!windowTitle.isEmpty()) {
        // Set the text here before asking for the width of the title bar label
        // in case people uses the actual text to calculate the width.
        titleBarOptions.text = windowTitle;
        titleBarOptions.fontMetrics = QFontMetrics(font, q);
        int width = q->style()->subControlRect(QStyle::CC_TitleBar, &titleBarOptions,
                                               QStyle::SC_TitleBarLabel, q).width();
        // Set elided text if we don't have enough space for the entire title.
        titleBarOptions.text = titleBarOptions.fontMetrics.elidedText(windowTitle, Qt::ElideRight, width);
    }
    return titleBarOptions;
}

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1485, as _ZNK26QAbstractScrollAreaPrivate17defaultSingleStepEv
#if QT_CONFIG(scrollarea)
inline int QAbstractScrollAreaPrivate::defaultSingleStep() const
{
    auto *platformTheme = QGuiApplicationPrivate::platformTheme();
    return platformTheme->themeHint(QPlatformTheme::ScrollSingleStepDistance).value<int>();
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 2012, as _ZN20QMdiSubWindowPrivate12restoreFocusEv
inline bool QMdiSubWindowPrivate::restoreFocus()
{
    if (restoreFocusWidget.isNull())
        return false;
    QWidget *candidate = restoreFocusWidget;
    restoreFocusWidget.clear();
    if (!candidate->hasFocus() && q_func()->isAncestorOf(candidate)
        && candidate->isVisible()
        && candidate->focusPolicy() != Qt::NoFocus) {
        candidate->setFocus();
        return true;
    }
    return candidate->hasFocus();
}

//  from src/widgets/widgets/qmdiarea.cpp, line 620, as _ZN15QMdiAreaPrivateC1Ev
inline QMdiAreaPrivate::QMdiAreaPrivate()
    : cascader(nullptr),
      regularTiler(nullptr),
      iconTiler(nullptr),
      placer(nullptr),
#if QT_CONFIG(rubberband)
      rubberBand(nullptr),
#endif
#if QT_CONFIG(tabbar)
      tabBar(nullptr),
#endif
      activationOrder(QMdiArea::CreationOrder),
      viewMode(QMdiArea::SubWindowView),
#if QT_CONFIG(tabbar)
      documentMode(false),
      tabsClosable(false),
      tabsMovable(false),
#endif
#if QT_CONFIG(tabwidget)
      tabShape(QTabWidget::Rounded),
      tabPosition(QTabWidget::North),
#endif
      ignoreGeometryChange(false),
      ignoreWindowStateChange(false),
      isActivated(false),
      isSubWindowsTiled(false),
      showActiveWindowMaximized(false),
      tileCalledFromResizeEvent(false),
      updatesDisabledByUs(false),
      inViewModeChange(false),
      indexToNextWindow(-1),
      indexToPreviousWindow(-1),
      indexToHighlighted(-1),
      indexToLastActiveTab(-1)
{
}

//  from src/widgets/widgets/qmdiarea.cpp, line 757, as _ZN15QMdiAreaPrivate11_q_closeTabEi
inline void QMdiAreaPrivate::_q_closeTab(int index)
{
#if !QT_CONFIG(tabbar)
    Q_UNUSED(index);
#else
    QMdiSubWindow *subWindow = childWindows.at(index);
    Q_ASSERT(subWindow);
    subWindow->close();
#endif // QT_CONFIG(tabbar)
}

//  from src/widgets/widgets/qmdiarea.cpp, line 768, as _ZN15QMdiAreaPrivate10_q_moveTabEii
inline void QMdiAreaPrivate::_q_moveTab(int from, int to)
{
#if !QT_CONFIG(tabbar)
    Q_UNUSED(from);
    Q_UNUSED(to);
#else
    childWindows.move(from, to);

    // Put the active window in front to update activation order.
    const int indexToActiveWindow = childWindows.indexOf(active);
    if (indexToActiveWindow != -1) {
        const int index = indicesToActivatedChildren.indexOf(indexToActiveWindow);
        Q_ASSERT(index != -1);
        if (index != 0) { // if it's not in front
            indicesToActivatedChildren.move(index, 0);
            internalRaise(active);
        }
    }
#endif // QT_CONFIG(tabbar)
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1058, as _ZN15QMdiAreaPrivate17resetActiveWindowEP13QMdiSubWindow
inline void QMdiAreaPrivate::resetActiveWindow(QMdiSubWindow *deactivatedWindow)
{
    Q_Q(QMdiArea);
    if (deactivatedWindow) {
        if (deactivatedWindow != active)
            return;
        active = nullptr;
        if ((aboutToBecomeActive || isActivated || lastWindowAboutToBeDestroyed())
            && !isExplicitlyDeactivated(deactivatedWindow) && !q->window()->isMinimized()) {
            return;
        }
        emit q->subWindowActivated(nullptr);
        return;
    }

    if (aboutToBecomeActive)
        return;

    active = nullptr;
    emit q->subWindowActivated(nullptr);
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1292, as _ZNK15QMdiAreaPrivate17scrollBarsEnabledEv
inline bool QMdiAreaPrivate::scrollBarsEnabled() const
{
    return hbarpolicy != Qt::ScrollBarAlwaysOff || vbarpolicy != Qt::ScrollBarAlwaysOff;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1300, as _ZNK15QMdiAreaPrivate28lastWindowAboutToBeDestroyedEv
inline bool QMdiAreaPrivate::lastWindowAboutToBeDestroyed() const
{
    if (childWindows.size() != 1)
        return false;

    QMdiSubWindow *last = childWindows.at(0);
    if (!last)
        return true;

    if (!last->testAttribute(Qt::WA_DeleteOnClose))
        return false;

    return last->d_func()->data.is_closing;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1318, as _ZNK15QMdiAreaPrivate25setChildActivationEnabledEbb
inline void QMdiAreaPrivate::setChildActivationEnabled(bool enable, bool onlyNextActivationEvent) const
{
    for (QMdiSubWindow *subWindow : childWindows) {
        if (!subWindow || !subWindow->isVisible())
            continue;
        if (onlyNextActivationEvent)
            subWindow->d_func()->ignoreNextActivationEvent = !enable;
        else
            subWindow->d_func()->activationEnabled = enable;
    }
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1228, as _ZN15QMdiAreaPrivate23resizeToMinimumTileSizeERK5QSizei
inline QRect QMdiAreaPrivate::resizeToMinimumTileSize(const QSize &minSubWindowSize, int subWindowCount)
{
    Q_Q(QMdiArea);
    if (!minSubWindowSize.isValid() || subWindowCount <= 0)
        return viewport->rect();

    // Calculate minimum size.
    const int columns = qMax(qCeil(qSqrt(qreal(subWindowCount))), 1);
    const int rows = qMax((subWindowCount % columns) ? (subWindowCount / columns + 1)
                                                     : (subWindowCount / columns), 1);
    const int minWidth = minSubWindowSize.width() * columns;
    const int minHeight = minSubWindowSize.height() * rows;

    // Increase area size if necessary. Scroll bars are provided if we're not able
    // to resize to the minimum size.
    if (!tileCalledFromResizeEvent) {
        QWidget *topLevel = q;
        // Find the topLevel for this area, either a real top-level or a sub-window.
        while (topLevel && !topLevel->isWindow() && topLevel->windowType() != Qt::SubWindow)
            topLevel = topLevel->parentWidget();
        // We don't want sub-subwindows to be placed at the edge, thus add 2 pixels.
        int minAreaWidth = minWidth + left + right + 2;
        int minAreaHeight = minHeight + top + bottom + 2;
        if (hbar->isVisible())
            minAreaHeight += hbar->height();
        if (vbar->isVisible())
            minAreaWidth += vbar->width();
        if (q->style()->styleHint(QStyle::SH_ScrollView_FrameOnlyAroundContents, nullptr, q)) {
            const int frame = q->style()->pixelMetric(QStyle::PM_DefaultFrameWidth, nullptr, q);
            minAreaWidth += 2 * frame;
            minAreaHeight += 2 * frame;
        }
        const QSize diff = QSize(minAreaWidth, minAreaHeight).expandedTo(q->size()) - q->size();
        // Only resize topLevel widget if scroll bars are disabled.
        if (hbarpolicy == Qt::ScrollBarAlwaysOff)
            topLevel->resize(topLevel->size().width() + diff.width(), topLevel->size().height());
        if (vbarpolicy == Qt::ScrollBarAlwaysOff)
            topLevel->resize(topLevel->size().width(), topLevel->size().height() + diff.height());
    }

    QRect domain = viewport->rect();

    // Adjust domain width and provide horizontal scroll bar.
    if (domain.width() < minWidth) {
        domain.setWidth(minWidth);
        if (hbarpolicy == Qt::ScrollBarAlwaysOff)
            q->setHorizontalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        else
            hbar->setValue(0);
    }
    // Adjust domain height and provide vertical scroll bar.
    if (domain.height() < minHeight) {
        domain.setHeight(minHeight);
        if (vbarpolicy  == Qt::ScrollBarAlwaysOff)
            q->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);
        else
            vbar->setValue(0);
    }
    return domain;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1465, as _ZN15QMdiAreaPrivate22highlightNextSubWindowEi
inline void QMdiAreaPrivate::highlightNextSubWindow(int increaseFactor)
{
    if (childWindows.size() == 1)
        return;

    Q_Q(QMdiArea);
    // There's no highlighted sub-window atm, use current.
    if (indexToHighlighted < 0) {
        QMdiSubWindow *current = q->currentSubWindow();
        if (!current)
            return;
        indexToHighlighted = childWindows.indexOf(current);
    }

    Q_ASSERT(indexToHighlighted >= 0);
    Q_ASSERT(indexToHighlighted < childWindows.size());

    QMdiSubWindow *highlight = nextVisibleSubWindow(increaseFactor, activationOrder, -1, indexToHighlighted);
    if (!highlight)
        return;

#if QT_CONFIG(rubberband)
    if (!rubberBand) {
        rubberBand = new QRubberBand(QRubberBand::Rectangle, q);
        // For accessibility to identify this special widget.
        rubberBand->setObjectName("qt_rubberband"_L1);
        rubberBand->setWindowFlags(rubberBand->windowFlags() | Qt::WindowStaysOnTopHint);
    }
#endif

    // Only highlight if we're not switching back to the previously active window (Ctrl-Tab once).
#if QT_CONFIG(rubberband)
    if (!tabToPreviousTimer.isActive())
        showRubberBandFor(highlight);
#endif

    indexToHighlighted = childWindows.indexOf(highlight);
    Q_ASSERT(indexToHighlighted >= 0);
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1354, as _ZNK15QMdiAreaPrivate13subWindowListEN8QMdiArea11WindowOrderEb
inline QList<QMdiSubWindow*>
QMdiAreaPrivate::subWindowList(QMdiArea::WindowOrder order, bool reversed) const
{
    QList<QMdiSubWindow *> list;
    if (childWindows.isEmpty())
        return list;

    if (order == QMdiArea::CreationOrder) {
        for (QMdiSubWindow *child : childWindows) {
            if (!child)
                continue;
            if (!reversed)
                list.append(child);
            else
                list.prepend(child);
        }
    } else if (order == QMdiArea::StackingOrder) {
        for (QObject *object : viewport->children()) {
            QMdiSubWindow *child = qobject_cast<QMdiSubWindow *>(object);
            if (!child || !childWindows.contains(child))
                continue;
            if (!reversed)
                list.append(child);
            else
                list.prepend(child);
        }
    } else { // ActivationHistoryOrder
        Q_ASSERT(indicesToActivatedChildren.size() == childWindows.size());
        for (int i = indicesToActivatedChildren.size() - 1; i >= 0; --i) {
            QMdiSubWindow *child = childWindows.at(indicesToActivatedChildren.at(i));
            if (!child)
                continue;
            if (!reversed)
                list.append(child);
            else
                list.prepend(child);
        }
    }
    return list;
}

//  from src/widgets/widgets/qmdiarea.cpp, line 1398, as _ZN15QMdiAreaPrivate19disconnectSubWindowEP7QObject
inline void QMdiAreaPrivate::disconnectSubWindow(QObject *subWindow)
{
    if (!subWindow)
        return;

    Q_Q(QMdiArea);
    QObject::disconnect(subWindow, nullptr, q, nullptr);
    subWindow->removeEventFilter(q);
}
//  -----------------------------------------------------------------------

//  A QMdiAreaPrivate that Python can take functions over in. Every QMdiAreaPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(mdiarea)
typedef void (*CuteQMdiAreaPrivateCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQMdiAreaPrivateCall1)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QPoint * (*CuteQMdiAreaPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQMdiAreaPrivateCall3)(const void *, bool, int *);
typedef void (*CuteQMdiAreaPrivateCall4)(const void *, int, int *);
typedef void (*CuteQMdiAreaPrivateCall5)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall6)(const void *, int *);
typedef void * (*CuteQMdiAreaPrivateCall7)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQMdiAreaPrivateCall8)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQMdiAreaPrivateCall9)(const void *, int *);
typedef int (*CuteQMdiAreaPrivateCall10)(const void *, int *);
typedef const QImage * (*CuteQMdiAreaPrivateCall11)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall12)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall13)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall14)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall15)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall16)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall17)(const void *, int *);
typedef void (*CuteQMdiAreaPrivateCall18)(const void *, int *);
typedef bool (*CuteQMdiAreaPrivateCall19)(const void *, int *);
typedef bool (*CuteQMdiAreaPrivateCall20)(const void *, int *);
class CuteQMdiAreaPrivate : public QMdiAreaPrivate {
public:
  using QMdiAreaPrivate::QMdiAreaPrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(mdiarea)
  //  void QMdiAreaPrivate::scrollBarPolicyChanged(Qt::Orientation a0,
  //      Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall0 call = reinterpret_cast<CuteQMdiAreaPrivateCall0>(taken[0]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QMdiAreaPrivate::scrollBarPolicyChanged(a0, a1);
  }
#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
  //      &startPos) const
  bool canStartScrollingAt(const QPoint &startPos) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall1 call = reinterpret_cast<CuteQMdiAreaPrivateCall1>(taken[1]);
      bool given = call(this, &startPos, &handled);
      if (handled) return given;
    }
    return QAbstractScrollAreaPrivate::canStartScrollingAt(startPos);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall2 call = reinterpret_cast<CuteQMdiAreaPrivateCall2>(taken[2]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollAreaPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall3 call = reinterpret_cast<CuteQMdiAreaPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall4 call = reinterpret_cast<CuteQMdiAreaPrivateCall4>(taken[4]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall5 call = reinterpret_cast<CuteQMdiAreaPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall6 call = reinterpret_cast<CuteQMdiAreaPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall7 call = reinterpret_cast<CuteQMdiAreaPrivateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall8 call = reinterpret_cast<CuteQMdiAreaPrivateCall8>(taken[8]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall9 call = reinterpret_cast<CuteQMdiAreaPrivateCall9>(taken[9]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[10]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall10 call = reinterpret_cast<CuteQMdiAreaPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall11 call = reinterpret_cast<CuteQMdiAreaPrivateCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[12]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall12 call = reinterpret_cast<CuteQMdiAreaPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[13]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall13 call = reinterpret_cast<CuteQMdiAreaPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[14]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall14 call = reinterpret_cast<CuteQMdiAreaPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[15]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall15 call = reinterpret_cast<CuteQMdiAreaPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall16 call = reinterpret_cast<CuteQMdiAreaPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall17 call = reinterpret_cast<CuteQMdiAreaPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[18]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall18 call = reinterpret_cast<CuteQMdiAreaPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[19]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall19 call = reinterpret_cast<CuteQMdiAreaPrivateCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[20]) {
      int handled = 0;
      CuteQMdiAreaPrivateCall20 call = reinterpret_cast<CuteQMdiAreaPrivateCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QMdiArea *QMdiAreaPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMdiArea *ritual_ZN15QMdiAreaPrivate6q_funcEv(QMdiAreaPrivate *self) {
  return self->q_func();
}

//  const QMdiArea *QMdiAreaPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMdiArea *ritual_ZNK15QMdiAreaPrivate6q_funcEv(
    const QMdiAreaPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(scrollarea)
//  QMdiAreaPrivate::QMdiAreaPrivate()
extern "C" Q_DECL_EXPORT
QMdiAreaPrivate *ritual_ZN15QMdiAreaPrivateC1Ev() {
  return new CuteQMdiAreaPrivate();
}
#endif  // QT_CONFIG(scrollarea)

//  void QMdiAreaPrivate::_q_closeTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate11_q_closeTabEi(
    QMdiAreaPrivate *self,
    int index) {
  self->_q_closeTab(index);
}

//  void QMdiAreaPrivate::_q_moveTab(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate10_q_moveTabEii(
    QMdiAreaPrivate *self,
    int from,
    int to) {
  self->_q_moveTab(from, to);
}

//  void QMdiAreaPrivate::resetActiveWindow(QMdiSubWindow *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate17resetActiveWindowEP13QMdiSubWindow(
    QMdiAreaPrivate *self,
    QMdiSubWindow *child) {
  self->resetActiveWindow(child);
}

//  bool QMdiAreaPrivate::scrollBarsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMdiAreaPrivate17scrollBarsEnabledEv(
    const QMdiAreaPrivate *self) {
  return self->scrollBarsEnabled();
}

//  bool QMdiAreaPrivate::lastWindowAboutToBeDestroyed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMdiAreaPrivate28lastWindowAboutToBeDestroyedEv(
    const QMdiAreaPrivate *self) {
  return self->lastWindowAboutToBeDestroyed();
}

//  void QMdiAreaPrivate::setChildActivationEnabled(bool enable, bool
//      onlyNextActivationEvent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QMdiAreaPrivate25setChildActivationEnabledEbb(
    const QMdiAreaPrivate *self,
    bool enable,
    bool onlyNextActivationEvent) {
  self->setChildActivationEnabled(enable, onlyNextActivationEvent);
}

//  QRect QMdiAreaPrivate::resizeToMinimumTileSize(const QSize
//      &minSubWindowSize, int subWindowCount)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN15QMdiAreaPrivate23resizeToMinimumTileSizeERK5QSizei(
    QMdiAreaPrivate *self,
    const QSize *minSubWindowSize,
    int subWindowCount) {
  return new QRect(
      self->resizeToMinimumTileSize(
          *minSubWindowSize,
          subWindowCount));
}

//  void QMdiAreaPrivate::scrollBarPolicyChanged(Qt::Orientation a0,
//      Qt::ScrollBarPolicy a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE(
    QMdiAreaPrivate *self,
    Qt::Orientation a0,
    Qt::ScrollBarPolicy a1) {
  self->scrollBarPolicyChanged(a0, a1);
}

#if QT_CONFIG(rubberband)
//  void QMdiAreaPrivate::highlightNextSubWindow(int increaseFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate22highlightNextSubWindowEi(
    QMdiAreaPrivate *self,
    int increaseFactor) {
  self->highlightNextSubWindow(increaseFactor);
}
#endif  // QT_CONFIG(rubberband)

//  QList<QMdiSubWindow *>
//      QMdiAreaPrivate::subWindowList(QMdiArea::WindowOrder a0, bool
//      reversed) const
extern "C" Q_DECL_EXPORT
QList<QMdiSubWindow *> *ritual_ZNK15QMdiAreaPrivate13subWindowListEN8QMdiArea11WindowOrderEb(
    const QMdiAreaPrivate *self,
    QMdiArea::WindowOrder a0,
    bool reversed) {
  return new QList<QMdiSubWindow *>(self->subWindowList(a0, reversed));
}

//  void QMdiAreaPrivate::disconnectSubWindow(QObject *subWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate19disconnectSubWindowEP7QObject(
    QMdiAreaPrivate *self,
    QObject *subWindow) {
  self->disconnectSubWindow(subWindow);
}

//  void QMdiAreaPrivate::startResizeTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate16startResizeTimerEv(QMdiAreaPrivate *self) {
  self->startResizeTimer();
}

//  void QMdiAreaPrivate::startTabToPreviousTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate23startTabToPreviousTimerEv(
    QMdiAreaPrivate *self) {
  self->startTabToPreviousTimer();
}

//  bool QMdiAreaPrivate::windowStaysOnTop(QMdiSubWindow *subWindow) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMdiAreaPrivate16windowStaysOnTopEP13QMdiSubWindow(
    const QMdiAreaPrivate *self,
    QMdiSubWindow *subWindow) {
  return self->windowStaysOnTop(subWindow);
}

//  bool QMdiAreaPrivate::isExplicitlyDeactivated(QMdiSubWindow *subWindow)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMdiAreaPrivate23isExplicitlyDeactivatedEP13QMdiSubWindow(
    const QMdiAreaPrivate *self,
    QMdiSubWindow *subWindow) {
  return self->isExplicitlyDeactivated(subWindow);
}

#if QT_CONFIG(rubberband)
//  void QMdiAreaPrivate::hideRubberBand()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate14hideRubberBandEv(QMdiAreaPrivate *self) {
  self->hideRubberBand();
}
#endif  // QT_CONFIG(rubberband)

//  a Python function taken by a CuteQMdiAreaPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMdiAreaPrivate(
    QMdiAreaPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMdiAreaPrivate *>(self)->take(key, call);
}

#if QT_CONFIG(scrollarea)
//  void QMdiAreaPrivate::scrollBarPolicyChanged(Qt::Orientation a0,
//      Qt::ScrollBarPolicy a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QMdiAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE(
    QMdiAreaPrivate *self,
    Qt::Orientation a0,
    Qt::ScrollBarPolicy a1) {
  self->QMdiAreaPrivate::scrollBarPolicyChanged(a0, a1);
}
#endif  // QT_CONFIG(scrollarea)

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
