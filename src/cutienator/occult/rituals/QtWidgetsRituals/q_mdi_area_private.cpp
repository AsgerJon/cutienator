//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
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
#include "qabstractscrollarea.h"
#if QT_CONFIG(scrollarea)
#include "qscrollbar.h"
#include "qapplication.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qevent.h"
#include "qdebug.h"
#include "qboxlayout.h"
#include "qpainter.h"
#include "qmargins.h"
#if QT_CONFIG(itemviews)
#include "qheaderview.h"
#endif
#include <QDebug>
#include "qabstractscrollarea_p.h"
#include "qscrollbar_p.h"
#include <qwidget.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme.h>
#include <private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#endif
#endif
#include "qmdisubwindow_p.h"
#include <QApplication>
#include <QStylePainter>
#include <QVBoxLayout>
#include <QMouseEvent>
#if QT_CONFIG(whatsthis)
#include <QWhatsThis>
#endif
#if QT_CONFIG(tooltip)
#include <QToolTip>
#endif
#if QT_CONFIG(mainwindow)
#include <QMainWindow>
#endif
#include <QScrollBar>
#include <QDebug>
#include <QMdiArea>
#include <QScopedValueRollback>
#if QT_CONFIG(action)
#  include <qaction.h>
#endif
#if QT_CONFIG(menu)
#include <QMenu>
#endif
#include <QProxyStyle>
#include "qmdiarea_p.h"
#include <QApplication>
#include <QStyle>
#include <QChildEvent>
#include <QResizeEvent>
#include <QScrollBar>
#include <QtAlgorithms>
#include <QPainter>
#include <QFontMetrics>
#include <QStyleOption>
#include <QDebug>
#include <qmath.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#include <private/qlayoutengine_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  void QMdiAreaPrivate::_q_closeTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMdiAreaPrivate11_q_closeTabEi(
    QMdiAreaPrivate *self,
    int index) {
  self->_q_closeTab(index);
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

#endif  // QT_CONFIG(mdiarea)
