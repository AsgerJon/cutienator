//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmenubar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(menubar)
#if QT_CONFIG(menubar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmenubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(accessibility)
# include <QtGui/qaccessible.h>
#endif
#include <QtGui/qpainter.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qevent.h>
#if QT_CONFIG(mainwindow)
#include <QtWidgets/qmainwindow.h>
#endif
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qmenubar_p.h>
#include <QtGui/private/qscreen_p.h>
#include <QtWidgets/private/qstyle_p.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qmenu.h>
#include <QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/private/qwidgetwindow_p.h>
#include <QtWidgets/qactiongroup.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qstyle.h>
#include <QtGui/qevent.h>
#include <QtCore/qtimer.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(accessibility)
# include <QtGui/qaccessible.h>
#endif
#if QT_CONFIG(effects)
# include <QtWidgets/private/qeffects_p.h>
#endif
#if QT_CONFIG(whatsthis)
# include <QtWidgets/qwhatsthis.h>
#endif
#include <QtWidgets/private/qmenu_p.h>
#if QT_CONFIG(menubar)
#include <QtWidgets/private/qmenubar_p.h>
#endif
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/qpushbutton.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtGui/qwindow.h>
#include <QtWidgets/private/qpushbutton_p.h>
#include <QtGui/private/qaction_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtWidgets/private/qstyle_p.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmapcache.h>
#include <QtCore/qset.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/private/qstyle_p.h>
#include <QtWidgets/private/qstylehelper_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#ifndef QT_NO_DEBUG
#include <QtCore/qdebug.h>
#endif
#include <QtCore/q20utility.h>
#include <limits.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qmenubar.cpp, line 39, as local:qmenubar.cpp:QMenuBarExtension
class QMenuBarExtension : public QToolButton
{
public:
    explicit QMenuBarExtension(QWidget *parent);

    QSize sizeHint() const override;
    void paintEvent(QPaintEvent *) override;
};

//  from src/widgets/widgets/qmenubar.cpp, line 48, as local:qmenubar.cpp:QMenuBarExtension::QMenuBarExtension
inline QMenuBarExtension::QMenuBarExtension(QWidget *parent)
    : QToolButton(parent)
{
    setObjectName("qt_menubar_ext_button"_L1);
    setAutoRaise(true);
#if QT_CONFIG(menu)
    setPopupMode(QToolButton::InstantPopup);
#endif
    setIcon(style()->standardIcon(QStyle::SP_ToolBarHorizontalExtensionButton, nullptr, parentWidget()));
}

//  from src/widgets/widgets/qmenubar.cpp, line 59, as local:qmenubar.cpp:QMenuBarExtension::paintEvent
inline void QMenuBarExtension::paintEvent(QPaintEvent *)
{
    QStylePainter p(this);
    QStyleOptionToolButton opt;
    initStyleOption(&opt);
    // We do not need to draw both extension arrows
    opt.features &= ~QStyleOptionToolButton::HasMenu;
    p.drawComplexControl(QStyle::CC_ToolButton, opt);
}

//  from src/widgets/widgets/qmenubar.cpp, line 70, as local:qmenubar.cpp:QMenuBarExtension::sizeHint
inline QSize QMenuBarExtension::sizeHint() const
{
    int ext = style()->pixelMetric(QStyle::PM_ToolBarExtensionExtent, nullptr, parentWidget());
    return QSize(ext, ext);
}

//  from src/widgets/widgets/qmenubar.cpp, line 128, as _ZN15QMenuBarPrivate16updateGeometriesEv
#if defined(Q_OS_LINUX)
inline void QMenuBarPrivate::updateGeometries()
{
    Q_Q(QMenuBar);
    if (!itemsDirty)
        return;
    int q_width = q->width()-(q->style()->pixelMetric(QStyle::PM_MenuBarPanelWidth, nullptr, q)*2);
    int q_start = -1;
    if (leftWidget || rightWidget) {
        int vmargin = q->style()->pixelMetric(QStyle::PM_MenuBarVMargin, nullptr, q)
                      + q->style()->pixelMetric(QStyle::PM_MenuBarPanelWidth, nullptr, q);
        int hmargin = q->style()->pixelMetric(QStyle::PM_MenuBarHMargin, nullptr, q)
                      + q->style()->pixelMetric(QStyle::PM_MenuBarPanelWidth, nullptr, q);
        if (leftWidget && leftWidget->isVisible()) {
            QSize sz = leftWidget->sizeHint();
            q_width -= sz.width();
            q_start = sz.width();
            QPoint pos(hmargin, (q->height() - leftWidget->height()) / 2);
            QRect vRect = QStyle::visualRect(q->layoutDirection(), q->rect(), QRect(pos, sz));
            leftWidget->setGeometry(vRect);
        }
        if (rightWidget && rightWidget->isVisible()) {
            QSize sz = rightWidget->sizeHint();
            q_width -= sz.width();
            QPoint pos(q->width() - sz.width() - hmargin, vmargin);
            QRect vRect = QStyle::visualRect(q->layoutDirection(), q->rect(), QRect(pos, sz));
            rightWidget->setGeometry(vRect);
        }
    }

#ifdef Q_OS_MACOS
    if (q->isNativeMenuBar()) {//nothing to see here folks, move along..
        itemsDirty = false;
        return;
    }
#endif
    calcActionRects(q_width, q_start);
    currentAction = nullptr;
#ifndef QT_NO_SHORTCUT
    if (itemsDirty) {
        for (const auto shortcutId : std::as_const(shortcutIndexMap))
            q->releaseShortcut(shortcutId);
        shortcutIndexMap.clear();
        shortcutIndexMap.reserve(actions.size());
        for (const auto *action : std::as_const(actions))
            shortcutIndexMap.append(q->grabShortcut(QKeySequence::mnemonic(action->text())));
    }
#endif
    itemsDirty = false;

    hiddenActions.clear();
    //this is the menu rectangle without any extension
    QRect menuRect = this->menuRect(false);

    //we try to see if the actions will fit there
    bool hasHiddenActions = false;
    for (const auto &rect : std::as_const(actionRects)) {
        if (rect.isValid() && !menuRect.contains(rect)) {
            hasHiddenActions = true;
            break;
        }
    }

    //...and if not, determine the ones that fit on the menu with the extension visible
    if (hasHiddenActions) {
        menuRect = this->menuRect(true);
        for (qsizetype i = 0; i < actions.size(); ++i) {
            const QRect &rect = actionRects.at(i);
            if (rect.isValid() && !menuRect.contains(rect)) {
                hiddenActions.append(actions.at(i));
            }
        }
    }

    if (hiddenActions.size() > 0) {
        QMenu *pop = extension->menu();
        if (!pop) {
            pop = new QMenu(q);
            extension->setMenu(pop);
        }
        pop->clear();
        pop->addActions(hiddenActions);

        int vmargin = q->style()->pixelMetric(QStyle::PM_MenuBarVMargin, nullptr, q);
        int x = q->isRightToLeft()
                ? menuRect.left() - extension->sizeHint().width() + 1
                : menuRect.right();
        extension->setGeometry(x, vmargin, extension->sizeHint().width(), menuRect.height() - vmargin*2);
        extension->show();
    } else {
        extension->hide();
    }
    q->updateGeometry();
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qmenu.cpp, line 685, as _ZN12QMenuPrivate20setFirstActionActiveEv
inline void QMenuPrivate::setFirstActionActive()
{
    updateActionRects();
    for(int i = 0, saccum = 0; i < actions.size(); i++) {
        const QRect &rect = actionRects.at(i);
        if (rect.isNull())
            continue;
        if (scroll && scroll->scrollFlags & QMenuScroller::ScrollUp) {
            saccum -= rect.height();
            if (saccum > scroll->scrollOffset - scrollerHeight())
                continue;
        }
        QAction *act = actions.at(i);
        if (considerAction(act)) {
            setCurrentAction(act);
            break;
        }
    }
}

//  from src/widgets/styles/qstyle.cpp, line 2475, as _ZN13QStylePrivate21useFullScreenForPopupEv
inline bool QStylePrivate::useFullScreenForPopup()
{
    auto theme = QGuiApplicationPrivate::platformTheme();
    return theme && theme->themeHint(QPlatformTheme::UseFullScreenForPopupMenu).toBool();
}

//  from src/widgets/widgets/qmenubar.cpp, line 89, as _ZNK15QMenuBarPrivate8menuRectEb
inline QRect QMenuBarPrivate::menuRect(bool extVisible) const
{
    Q_Q(const QMenuBar);

    int hmargin = q->style()->pixelMetric(QStyle::PM_MenuBarPanelWidth, nullptr, q);
    QRect result = q->rect();
    result.adjust(hmargin, 0, -hmargin, 0);

    if (extVisible) {
        if (q->isRightToLeft())
            result.setLeft(result.left() + extension->sizeHint().width());
        else
            result.setWidth(result.width() - extension->sizeHint().width());
    }

    if (leftWidget && leftWidget->isVisible()) {
        QSize sz = leftWidget->sizeHint();
        if (q->isRightToLeft())
            result.setRight(result.right() - sz.width());
        else
            result.setLeft(result.left() + sz.width());
    }

    if (rightWidget && rightWidget->isVisible()) {
        QSize sz = rightWidget->sizeHint();
        if (q->isRightToLeft())
            result.setLeft(result.left() + sz.width());
        else
            result.setRight(result.right() - sz.width());
    }

    return result;
}

//  from src/widgets/widgets/qmenu.cpp, line 706, as _ZN12QMenuPrivate16setCurrentActionEP7QActioniNS_15SelectionReasonENS_18SelectionDirectionEb
inline void QMenuPrivate::setCurrentAction(QAction *action, int popup, SelectionReason reason,
                                    SelectionDirection direction, bool activateFirst)
{
    Q_Q(QMenu);
    tearoffHighlighted = 0;

    if (!considerAction(action))
        action = nullptr;

    // Reselect the currently active action in case mouse moved over other menu items when
    // moving from sub menu action to sub menu (QTBUG-20094).
    if (reason != SelectedFromKeyboard) {
        if (QMenu *menu = qobject_cast<QMenu*>(causedPopup.widget)) {
            if (causedPopup.action && menu->d_func()->activeMenu == q)
                // Reselect parent menu action only if mouse is over a menu and parent menu action is not already selected (QTBUG-47987)
                if (hasReceievedEnter && menu->d_func()->currentAction != causedPopup.action)
                    menu->d_func()->setCurrentAction(causedPopup.action, 0, reason, direction, false);
        }
    }

    if (currentAction)
        q->update(actionRect(currentAction));

    QMenu *hideActiveMenu = activeMenu;
    QAction *previousAction = currentAction;

    currentAction = action;
    if (action) {
        if (!action->isSeparator()) {
            activateAction(action, QAction::Hover);
            if (popup != -1) {
                // if the menu is visible then activate the required action,
                // otherwise we just mark the action as currentAction
                // and activate it when the menu will be popuped.
                if (q->isVisible())
                    popupAction(currentAction, popup, activateFirst);
            }
            q->update(actionRect(action));

            if (reason == SelectedFromKeyboard) {
                QWidget *widget = widgetItems.value(action);
                if (widget) {
                    if (widget->focusPolicy() != Qt::NoFocus)
                        widget->setFocus(direction == QMenuPrivate::SelectionDirection::Up ? Qt::BacktabFocusReason : Qt::TabFocusReason);
                } else {
                    //when the action has no QWidget, the QMenu itself should
                    // get the focus
                    // Since the menu is a pop-up, it uses the popup reason.
                    if (!q->hasFocus()) {
                        q->setFocus(Qt::PopupFocusReason);
                    }
                }
            }
        }
#if QT_CONFIG(statustip)
    }  else if (previousAction) {
        previousAction->d_func()->showStatusText(topCausedWidget(), QString());
#endif
    }
    if (hideActiveMenu && previousAction != currentAction) {
        if (popup == -1) {
#if QT_CONFIG(effects)
            // kill any running effect
            qFadeEffect(nullptr);
            qScrollEffect(nullptr);
#endif
            hideMenu(hideActiveMenu);
        } else if (!currentAction || !currentAction->menu()) {
            if (reason != SelectionReason::SelectedFromAPI)
                sloppyState.startTimerIfNotRunning();
        }
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 279, as _ZNK12QMenuPrivate14scrollerHeightEv
inline int QMenuPrivate::scrollerHeight() const
{
    Q_Q(const QMenu);
    return q->style()->pixelMetric(QStyle::PM_MenuScrollerHeight, nullptr, q);
}

//  from src/widgets/widgets/qmenu.cpp, line 333, as _ZNK12QMenuPrivate17updateActionRectsEv
inline void QMenuPrivate::updateActionRects() const
{
    updateActionRects(popupGeometry());
}

//  from src/widgets/widgets/qmenu.cpp, line 648, as _ZN12QMenuPrivate11popupActionEP7QActionib
inline void QMenuPrivate::popupAction(QAction *action, int delay, bool activateFirst)
{
    Q_Q(QMenu);
    if (action) {
        if (action->isEnabled()) {
            if (!delay)
                q->internalDelayedPopup();
            else if (action->menu() && !action->menu()->isVisible())
                delayState.start(delay, action);
            else if (!action->menu())
                delayState.stop();
            if (activateFirst && action->menu())
                action->menu()->d_func()->setFirstActionActive();
        }
    } else if (QMenu *menu = activeMenu) {  //hide the current item
        hideMenu(menu);
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 1445, as _ZN12QMenuPrivate14activateActionEP7QActionNS0_11ActionEventEb
inline void QMenuPrivate::activateAction(QAction *action, QAction::ActionEvent action_e, bool self)
{
    Q_Q(QMenu);
#if QT_CONFIG(whatsthis)
    bool inWhatsThisMode = QWhatsThis::inWhatsThisMode();
#endif
    if (!action || !q->isEnabled()
        || (action_e == QAction::Trigger
#if QT_CONFIG(whatsthis)
            && !inWhatsThisMode
#endif
            && (action->isSeparator() ||!action->isEnabled())))
        return;

    /* I have to save the caused stack here because it will be undone after popup execution (ie in the hide).
       Then I iterate over the list to actually send the events. --Sam
    */
    const QList<QPointer<QWidget>> causedStack = calcCausedStack();
    if (action_e == QAction::Trigger) {
#if QT_CONFIG(whatsthis)
        if (!inWhatsThisMode)
            actionAboutToTrigger = action;
#endif

        if (q->testAttribute(Qt::WA_DontShowOnScreen)) {
            hideUpToMenuBar();
        } else {
            for(QWidget *widget = QApplication::activePopupWidget(); widget; ) {
                if (QMenu *qmenu = qobject_cast<QMenu*>(widget)) {
                    if (qmenu == q)
                        hideUpToMenuBar();
                    widget = qmenu->d_func()->causedPopup.widget;
                } else {
                    break;
                }
            }
        }

#if QT_CONFIG(whatsthis)
        if (inWhatsThisMode) {
            QString s = action->whatsThis();
            if (s.isEmpty())
                s = whatsThis;
            QWhatsThis::showText(q->mapToGlobal(actionRect(action).center()), s, q);
            return;
        }
#endif
    }

    QPointer<QMenu> thisGuard(q);
    activateCausedStack(causedStack, action, action_e, self);
    if (!thisGuard)
        return;

    if (action_e == QAction::Hover) {
#if QT_CONFIG(accessibility)
        if (QAccessible::isActive()) {
            int actionIndex = indexOf(action);
            QAccessibleEvent focusEvent(q, QAccessible::Focus);
            focusEvent.setChild(actionIndex);
            QAccessible::updateAccessibility(&focusEvent);
        }
#endif
        action->showStatusText(topCausedWidget());
    } else {
        actionAboutToTrigger = nullptr;
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 546, as _ZN12QMenuPrivate8hideMenuEP5QMenu
inline void QMenuPrivate::hideMenu(QMenu *menu)
{
    if (!menu)
        return;

    // See two execs below. They may trigger an akward situation
    // when 'menu' (also known as 'q' or 'this' in the many functions
    // around) to become a dangling pointer if the loop manages
    // to execute 'deferred delete' ... posted while executing
    // this same loop. Not good!
    struct Reposter : QObject
    {
        Reposter(QMenu *menu) : q(menu)
        {
            Q_ASSERT(q);
            q->installEventFilter(this);
        }
        ~Reposter()
        {
            if (deleteLater)
                q->deleteLater();
        }
        bool eventFilter(QObject *obj, QEvent *event) override
        {
            if (obj == q && event->type() == QEvent::DeferredDelete)
                return deleteLater = true;

            return QObject::eventFilter(obj, event);
        }
        QMenu *q = nullptr;
        bool deleteLater = false;
    };

#if QT_CONFIG(effects)
    // If deleteLater has been called and the event loop spins, while waiting
    // for visual effects to happen, menu might become stale.
    // To prevent a QSignalBlocker from restoring a stale object, block and restore signals manually.
    QPointer<QMenu> stillAlive(menu);
    const bool signalsBlocked = menu->signalsBlocked();
    menu->blockSignals(true);

    aboutToHide = true;
    // Flash item which is about to trigger (if any).
    if (menu && menu->style()->styleHint(QStyle::SH_Menu_FlashTriggeredItem, nullptr, stillAlive)
        && currentAction && currentAction == actionAboutToTrigger
        && menu->actions().contains(currentAction)) {
        QEventLoop eventLoop;
        QAction *activeAction = currentAction;

        menu->setActiveAction(nullptr);
        const Reposter deleteDeleteLate(menu);
        QTimer::singleShot(60, &eventLoop, SLOT(quit()));
        eventLoop.exec();

        if (!stillAlive)
            return;

        // Select and wait 20 ms.
        menu->setActiveAction(activeAction);
        QTimer::singleShot(20, &eventLoop, SLOT(quit()));
        eventLoop.exec();
    }

    aboutToHide = false;

    if (stillAlive)
        menu->blockSignals(signalsBlocked);
    else
        return;

#endif // QT_CONFIG(effects)
    if (activeMenu == menu)
        activeMenu = nullptr;

    menu->d_func()->causedPopup.action = nullptr;
    menu->close();
    menu->d_func()->causedPopup.widget = nullptr;
}

//  from src/widgets/widgets/qmenu.cpp, line 506, as _ZNK12QMenuPrivate10actionRectEP7QAction
inline QRect QMenuPrivate::actionRect(QAction *act) const
{
    int index = actions.indexOf(act);
    if (index == -1)
        return QRect();

    updateActionRects();

    //we found the action
    return actionRects.at(index);
}

//  from src/widgets/widgets/qmenu.cpp, line 292, as _ZNK12QMenuPrivate13popupGeometryEP7QScreen
inline QRect QMenuPrivate::popupGeometry(QScreen *screen) const
{
    Q_Q(const QMenu);
    if (screen == nullptr
#if QT_CONFIG(graphicsview)
        && q->graphicsProxyWidget() == nullptr
#endif
        ) {
        screen = q->isVisible() ? q->screen() : popupScreen.data();
    }
    if (useFullScreenForPopup())
        return screen ? screen->geometry()
                      : QWidgetPrivate::screenGeometry(q);
    return screen ? screen->availableGeometry()
                  : QWidgetPrivate::availableScreenGeometry(q);
}

//  from src/widgets/widgets/qmenu.cpp, line 910, as _ZNK12QMenuPrivate15topCausedWidgetEv
inline QWidget *QMenuPrivate::topCausedWidget() const
{
    QWidget* top = causedPopup.widget;
    while (QMenu* m = qobject_cast<QMenu *>(top))
        top = m->d_func()->causedPopup.widget;
    return top;
}

//  from src/widgets/widgets/qmenu.cpp, line 338, as _ZNK12QMenuPrivate17updateActionRectsERK5QRect
inline void QMenuPrivate::updateActionRects(const QRect &screen) const
{
    Q_Q(const QMenu);
    if (!itemsDirty)
        return;

    q->ensurePolished();

    //let's reinitialize the buffer
    actionRects.resize(actions.size());
    actionRects.fill(QRect());

    int lastVisibleAction = getLastVisibleAction();

    QStyle *style = q->style();
    QStyleOption opt;
    opt.initFrom(q);
    const int hmargin = style->pixelMetric(QStyle::PM_MenuHMargin, &opt, q),
              vmargin = style->pixelMetric(QStyle::PM_MenuVMargin, &opt, q),
              icone = style->pixelMetric(QStyle::PM_SmallIconSize, &opt, q);
    const int fw = style->pixelMetric(QStyle::PM_MenuPanelWidth, &opt, q);
    const int deskFw = style->pixelMetric(QStyle::PM_MenuDesktopFrameWidth, &opt, q);
    const int tearoffHeight = tearoff ? style->pixelMetric(QStyle::PM_MenuTearoffHeight, &opt, q) : 0;
    const int base_y = vmargin + fw + topmargin + (scroll ? scroll->scrollOffset : 0) + tearoffHeight;
    const int column_max_y = screen.height() - 2 * deskFw - (vmargin + bottommargin + fw);
    int max_column_width = 0;
    int y = base_y;

    //for compatibility now - will have to refactor this away
    tabWidth = 0;
    maxIconWidth = 0;
    hasCheckableItems = false;
    ncols = 1;

    for (int i = 0; i < actions.size(); ++i) {
        QAction *action = actions.at(i);
        if (action->isSeparator() || !action->isVisible() || widgetItems.contains(action))
            continue;
        //..and some members
        hasCheckableItems |= action->isCheckable();
        QIcon is = action->icon();
        if (!is.isNull()) {
            maxIconWidth = qMax<uint>(maxIconWidth, icone + 4);
        }
    }

    //calculate size
    QFontMetrics qfm = q->fontMetrics();
    bool previousWasSeparator = true; // this is true to allow removing the leading separators
#if QT_CONFIG(shortcut)
    const bool contextMenu = isContextMenu();
#endif
    const bool menuSupportsSections = q->style()->styleHint(QStyle::SH_Menu_SupportsSections, nullptr, q);
    for(int i = 0; i <= lastVisibleAction; i++) {
        QAction *action = actions.at(i);
        const bool isSection = action->isSeparator() && (!action->text().isEmpty() || !action->icon().isNull());
        const bool isPlainSeparator = (isSection && !menuSupportsSections)
                                   || (action->isSeparator() && !isSection);

        if (!action->isVisible() ||
            (collapsibleSeparators && previousWasSeparator && isPlainSeparator))
            continue; // we continue, this action will get an empty QRect

        previousWasSeparator = isPlainSeparator;

        //let the style modify the above size..
        QStyleOptionMenuItem opt;
        q->initStyleOption(&opt, action);
        const QFontMetrics &fm = opt.fontMetrics;

        QSize sz;
        if (QWidget *w = widgetItems.value(action)) {
          sz = w->sizeHint().expandedTo(w->minimumSize()).expandedTo(w->minimumSizeHint()).boundedTo(w->maximumSize());
        } else {
            //calc what I think the size is..
            if (action->isSeparator() && action->text().isEmpty()) {
                sz = QSize(2, 2);
            } else {
                QString s = action->text();
                qsizetype t = s.indexOf(u'\t');
                if (t != -1) {
                    tabWidth = qMax(int(tabWidth), qfm.horizontalAdvance(s.mid(t+1)));
                    s = s.left(t);
#if QT_CONFIG(shortcut)
                } else if (action->isShortcutVisibleInContextMenu() || !contextMenu) {
                    QKeySequence seq = action->shortcut();
                    if (!seq.isEmpty())
                        tabWidth = qMax(int(tabWidth), qfm.horizontalAdvance(seq.toString(QKeySequence::NativeText)));
#endif
                }
                sz.setWidth(fm.boundingRect(QRect(), Qt::TextSingleLine | Qt::TextShowMnemonic, s).width());
                sz.setHeight(qMax(fm.height(), qfm.height()));

                QIcon is = action->icon();
                if (!is.isNull()) {
                    QSize is_sz = QSize(icone, icone);
                    if (is_sz.height() > sz.height())
                        sz.setHeight(is_sz.height());
                }
            }
            sz = style->sizeFromContents(QStyle::CT_MenuItem, &opt, sz, q);
        }


        if (!sz.isEmpty()) {
            max_column_width = qMax(max_column_width, sz.width());
            //wrapping
            if (!scroll && y + sz.height() > column_max_y) {
                ncols++;
                y = base_y;
            } else {
                y += sz.height();
            }
            //update the item
            actionRects[i] = QRect(0, 0, sz.width(), sz.height());
        }
    }

    max_column_width += tabWidth; //finally add in the tab width
    if (!tornoff || scroll) { // exclude non-scrollable tear-off menu since the tear-off menu has a fixed size
        const int sfcMargin = style->sizeFromContents(QStyle::CT_Menu, &opt, QSize(0, 0), q).width();
        const int min_column_width = q->minimumWidth() - (sfcMargin + leftmargin + rightmargin + 2 * (fw + hmargin));
        max_column_width = qMax(min_column_width, max_column_width);
    }

    //calculate position
    int x = hmargin + fw + leftmargin;
    y = base_y;

    for(int i = 0; i < actions.size(); i++) {
        QRect &rect = actionRects[i];
        if (rect.isNull())
            continue;
        if (!scroll && y + rect.height() > column_max_y) {
            x += max_column_width + hmargin;
            y = base_y;
        }
        rect.translate(x, y);                        //move
        rect.setWidth(max_column_width); //uniform width

        //we need to update the widgets geometry
        if (QWidget *widget = widgetItems.value(actions.at(i))) {
            widget->setGeometry(rect);
            widget->setVisible(actions.at(i)->isVisible());
        }

        y += rect.height();
    }
    itemsDirty = 0;
}

//  from src/widgets/widgets/qmenu.cpp, line 518, as _ZN12QMenuPrivate15hideUpToMenuBarEv
inline void QMenuPrivate::hideUpToMenuBar()
{
    Q_Q(QMenu);
    bool fadeMenus = q->style()->styleHint(QStyle::SH_Menu_FadeOutOnHide, nullptr, q);
    if (!tornoff) {
        QWidget *caused = causedPopup.widget;
        hideMenu(q); //hide after getting causedPopup
        while(caused) {
#if QT_CONFIG(menubar)
            if (QMenuBar *mb = qobject_cast<QMenuBar*>(caused)) {
                mb->d_func()->setCurrentAction(nullptr);
                mb->d_func()->setKeyboardMode(false);
                caused = nullptr;
            } else
#endif
            if (QMenu *m = qobject_cast<QMenu*>(caused)) {
                caused = m->d_func()->causedPopup.widget;
                if (!m->d_func()->tornoff)
                    hideMenu(m);
                if (!fadeMenus) // Mac doesn't clear the action until after hidden.
                    m->d_func()->setCurrentAction(nullptr);
            } else {                caused = nullptr;
            }
        }
    }
    setCurrentAction(nullptr);
}

//  from src/widgets/widgets/qmenu.cpp, line 1404, as _ZN12QMenuPrivate19activateCausedStackERK5QListI8QPointerI7QWidgetEEP7QActionNS7_11ActionEventEb
inline void QMenuPrivate::activateCausedStack(const QList<QPointer<QWidget>> &causedStack, QAction *action,
                                       QAction::ActionEvent action_e, bool self)
{
    Q_Q(QMenu);
    // can't use QScopedValueRollback here
    const bool activationRecursionGuardReset = activationRecursionGuard;
    activationRecursionGuard = true;
    QPointer<QMenu> guard(q);
    if (self)
        action->activate(action_e);
    if (!guard)
        return;
    auto boolBlocker = qScopeGuard([this, activationRecursionGuardReset]{
        activationRecursionGuard = activationRecursionGuardReset;
    });

    for(int i = 0; i < causedStack.size(); ++i) {
        QPointer<QWidget> widget = causedStack.at(i);
        if (!widget)
            continue;
        //fire
        if (QMenu *qmenu = qobject_cast<QMenu*>(widget)) {
            widget = qmenu->d_func()->causedPopup.widget;
            if (action_e == QAction::Trigger) {
                emit qmenu->triggered(action);
           } else if (action_e == QAction::Hover) {
                emit qmenu->hovered(action);
            }
#if QT_CONFIG(menubar)
        } else if (QMenuBar *qmenubar = qobject_cast<QMenuBar*>(widget)) {
            if (action_e == QAction::Trigger) {
                emit qmenubar->triggered(action);
            } else if (action_e == QAction::Hover) {
                emit qmenubar->hovered(action);
            }
            break; //nothing more..
#endif
        }
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 324, as _ZNK12QMenuPrivate13isContextMenuEv
inline bool QMenuPrivate::isContextMenu() const
{
#if QT_CONFIG(menubar)
    return qobject_cast<const QMenuBar *>(topCausedWidget()) == nullptr;
#else
    return true;
#endif
}

//  from src/widgets/widgets/qmenu.cpp, line 489, as _ZNK12QMenuPrivate20getLastVisibleActionEv
inline int QMenuPrivate::getLastVisibleAction() const
{
    //let's try to get the last visible action
    int lastVisibleAction = actions.size() - 1;
    for (;lastVisibleAction >= 0; --lastVisibleAction) {
        const QAction *action = actions.at(lastVisibleAction);
        if (action->isVisible()) {
            //removing trailing separators
            if (action->isSeparator() && collapsibleSeparators)
                continue;
            break;
        }
    }
    return lastVisibleAction;
}

//  from src/widgets/widgets/qmenu.cpp, line 287, as _ZNK12QMenuPrivate21useFullScreenForPopupEv
inline bool QMenuPrivate::useFullScreenForPopup() const
{
    return !tornoff && QStylePrivate::useFullScreenForPopup();
}

//  from src/widgets/widgets/qmenubar.cpp, line 696, as _ZNK15QMenuBarPrivate13getNextActionExx
inline QAction *QMenuBarPrivate::getNextAction(const qsizetype _start, const qsizetype increment) const
{
    Q_Q(const QMenuBar);
    const_cast<QMenuBarPrivate*>(this)->updateGeometries();
    bool allowActiveAndDisabled = q->style()->styleHint(QStyle::SH_Menu_AllowActiveAndDisabled, nullptr, q);
    const qsizetype start = (_start == -1 && increment == -1) ? actions.size() : _start;
    const qsizetype end =  increment == -1 ? 0 : actions.size() - 1;

    for (qsizetype i = start; i != end;) {
        i += increment;
        QAction *current = actions.at(i);
        if (!actionRects.at(i).isNull() && (allowActiveAndDisabled || current->isEnabled()))
            return current;
    }

    if (_start != -1) //let's try from the beginning or the end
        return getNextAction(-1, increment);

    return nullptr;
}

//  from src/widgets/widgets/qmenubar.cpp, line 384, as _ZNK15QMenuBarPrivate15calcActionRectsEii
inline void QMenuBarPrivate::calcActionRects(int max_width, int start) const
{
    Q_Q(const QMenuBar);

    if (!itemsDirty)
        return;

    //let's reinitialize the buffer
    actionRects.resize(actions.size());
    actionRects.fill(QRect());

    const QStyle *style = q->style();

    const int itemSpacing = style->pixelMetric(QStyle::PM_MenuBarItemSpacing, nullptr, q);
    int max_item_height = 0, separator = -1, separator_start = 0, separator_len = 0;

    //calculate size
    const QFontMetrics fm = q->fontMetrics();
    const int hmargin = style->pixelMetric(QStyle::PM_MenuBarHMargin, nullptr, q),
              vmargin = style->pixelMetric(QStyle::PM_MenuBarVMargin, nullptr, q),
                icone = style->pixelMetric(QStyle::PM_SmallIconSize, nullptr, q);
    for (qsizetype i = 0; i < actions.size(); ++i) {
        const QAction *action = actions.at(i);
        if (!action->isVisible())
            continue;

        QSize sz;

        //calc what I think the size is..
        if (action->isSeparator()) {
            if (style->styleHint(QStyle::SH_DrawMenuBarSeparator, nullptr, q))
                separator = i;
            continue; //we don't really position these!
        } else {
            const QString s = action->text();
            QIcon is = action->icon();
            // If an icon is set, only the icon is visible
            if (!is.isNull())
                sz = sz.expandedTo(QSize(icone, icone));
            else if (!s.isEmpty())
                sz = fm.size(Qt::TextShowMnemonic, s);
        }

        //let the style modify the above size..
        QStyleOptionMenuItemV2 opt;
        q->initStyleOption(&opt, action);
        sz = q->style()->sizeFromContents(QStyle::CT_MenuBarItem, &opt, sz, q);

        if (!sz.isEmpty()) {
            { //update the separator state
                int iWidth = sz.width() + itemSpacing;
                if (separator == -1)
                    separator_start += iWidth;
                else
                    separator_len += iWidth;
            }
            //maximum height
            max_item_height = qMax(max_item_height, sz.height());
            //append
            actionRects[i] = QRect(0, 0, sz.width(), sz.height());
        }
    }

    //calculate position
    const int fw = q->style()->pixelMetric(QStyle::PM_MenuBarPanelWidth, nullptr, q);
    int x = fw + ((start == -1) ? hmargin : start) + itemSpacing;
    int y = fw + vmargin;
    for (qsizetype i = 0; i < actionRects.size(); ++i) {
        QRect &rect = actionRects[i];
        if (rect.isNull())
            continue;

        //resize
        rect.setHeight(max_item_height);

        //move
        if (separator != -1 && i >= separator) { //after the separator
            int left = (max_width - separator_len - hmargin - itemSpacing) + (x - separator_start - hmargin);
            if (left < separator_start) { //wrap
                separator_start = x = hmargin;
                y += max_item_height;
            }
            rect.moveLeft(left);
        } else {
            rect.moveLeft(x);
        }
        rect.moveTop(y);

        //keep moving along..
        x += rect.width() + itemSpacing;

        //make sure we follow the layout direction
        rect = QStyle::visualRect(q->layoutDirection(), q->rect(), rect);
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 222, as _ZNK15QMenuBarPrivate10actionRectEP7QAction
inline QRect QMenuBarPrivate::actionRect(QAction *act) const
{
    const qsizetype index = actions.indexOf(act);

    //makes sure the geometries are up-to-date
    const_cast<QMenuBarPrivate*>(this)->updateGeometries();

    if (index < 0 || index >= actionRects.size())
        return QRect(); // that can happen in case of native menubar

    return actionRects.at(index);
}

//  from src/widgets/widgets/qmenubar.cpp, line 80, as _ZNK15QMenuBarPrivate8actionAtE6QPoint
inline QAction *QMenuBarPrivate::actionAt(QPoint p) const
{
    for (auto *action : actions) {
        if (actionRect(action).contains(p))
            return action;
    }
    return nullptr;
}

//  from src/widgets/widgets/qmenubar.cpp, line 340, as _ZN15QMenuBarPrivate16setCurrentActionEP7QActionbb
inline void QMenuBarPrivate::setCurrentAction(QAction *action, bool popup, bool activateFirst)
{
    if (currentAction == action && popup == popupState)
        return;

    autoReleaseTimer.stop();

    doChildEffects = (popup && !activeMenu);
    Q_Q(QMenuBar);
    QWidget *fw = nullptr;
    if (QMenu *menu = activeMenu) {
        activeMenu = nullptr;
        hoverAction = nullptr;
        if (popup) {
            fw = q->window()->focusWidget();
            q->setFocus(Qt::NoFocusReason);
        }
        menu->hide();
    }

    if (currentAction)
        q->update(actionRect(currentAction));

    popupState = popup;
#if QT_CONFIG(statustip)
    QAction *previousAction = currentAction;
#endif
    currentAction = action;
    if (action && action->isEnabled()) {
        activateAction(action, QAction::Hover);
        if (popup)
            popupAction(action, activateFirst);
        q->update(actionRect(action));
#if QT_CONFIG(statustip)
    }  else if (previousAction) {
        QString empty;
        QStatusTipEvent tip(empty);
        QCoreApplication::sendEvent(q, &tip);
#endif
    }
    if (fw)
        fw->setFocus(Qt::NoFocusReason);
}

//  from src/widgets/widgets/qmenubar.cpp, line 272, as _ZN15QMenuBarPrivate11popupActionEP7QActionb
inline void QMenuBarPrivate::popupAction(QAction *action, bool activateFirst)
{
    Q_Q(QMenuBar);
    if (!action || !action->menu() || closePopupMode)
        return;
    popupState = true;
    if (action->isEnabled() && action->menu()->isEnabled()) {
        closePopupMode = 0;
        activeMenu = action->menu();
        auto *activeMenuPriv = activeMenu->d_func();
        activeMenuPriv->causedPopup.widget = q;
        activeMenuPriv->causedPopup.action = action;

        QRect adjustedActionRect = actionRect(action);
        QPoint popupPos = adjustedActionRect.bottomLeft() + QPoint(0, 1);

        //we put the popup menu on the screen containing the bottom-center of the action rect
        QScreen *menubarScreen = q->window()->windowHandle()->screen();
        QPoint screenTestPos = q->mapToGlobal(popupPos + QPoint(adjustedActionRect.width() / 2, 0));
        QPointer<QScreen> popupScreen = menubarScreen->virtualSiblingAt(screenTestPos);
        if (!popupScreen)
            popupScreen = menubarScreen;
        std::swap(popupScreen, activeMenuPriv->popupScreen);
        const QSize popup_size = activeMenu->sizeHint();
        std::swap(popupScreen, activeMenuPriv->popupScreen);

        // Use screenTestPos.y() for the popup y position. This is the correct global y
        // consistent with the selected screen in cases where the action rect spans
        // multiple screens with different scale factors.
        QPoint pos(q->mapToGlobal(popupPos).x(), screenTestPos.y());

        QRect screenRect = QStylePrivate::useFullScreenForPopup()
            ? popupScreen->geometry()
            : popupScreen->availableGeometry();
        pos = QPoint(qMax(pos.x(), screenRect.x()), qMax(pos.y(), screenRect.y()));
        const bool fitUp = (pos.y() - popup_size.height() >= screenRect.top());
        const bool fitDown = (pos.y() + popup_size.height() <= screenRect.bottom());
        const bool rtl = q->isRightToLeft();
        const int actionWidth = adjustedActionRect.width();

        if (!fitUp && !fitDown) { //we should shift the menu
            bool shouldShiftToRight = !rtl;
            if (rtl && popup_size.width() > pos.x())
                shouldShiftToRight = true;
            else if (actionWidth + popup_size.width() + pos.x() > screenRect.right())
                shouldShiftToRight = false;

            if (shouldShiftToRight) {
                pos.rx() += actionWidth + (rtl ? popup_size.width() : 0);
            } else {
                //shift to left
                if (!rtl)
                    pos.rx() -= popup_size.width();
            }
        } else if (rtl) {
            pos.rx() += actionWidth;
        }

        if (!defaultPopDown || (fitUp && !fitDown))
            pos.setY(qMax(screenRect.y(), q->mapToGlobal(QPoint(0, adjustedActionRect.top()-popup_size.height())).y()));
        QMenuPrivate::get(activeMenu)->topData()->initialScreen = popupScreen;
        activeMenu->popup(pos);
        if (activateFirst)
            activeMenu->d_func()->setFirstActionActive();
    }
    q->update(actionRect(action));
}

//  from src/widgets/widgets/qmenubar.cpp, line 235, as _ZN15QMenuBarPrivate16focusFirstActionEv
inline void QMenuBarPrivate::focusFirstAction()
{
    if (!currentAction) {
        updateGeometries();
        qsizetype index = 0;
        while (index < actions.size() && actionRects.at(index).isNull()) ++index;
        if (index < actions.size())
            setCurrentAction(actions.at(index));
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 246, as _ZN15QMenuBarPrivate15setKeyboardModeEb
inline void QMenuBarPrivate::setKeyboardMode(bool b)
{
    Q_Q(QMenuBar);
    if (b && !q->style()->styleHint(QStyle::SH_MenuBar_AltKeyNavigation, nullptr, q)) {
        setCurrentAction(nullptr);
        return;
    }
    keyboardState = b;
    if (b) {
        QWidget *fw = QApplication::focusWidget();
        if (fw && fw != q && fw->window() != QApplication::activePopupWidget())
            keyboardFocusWidget = fw;
        focusFirstAction();
        q->setFocus(Qt::MenuBarFocusReason);
    } else {
        if (!popupState)
            setCurrentAction(nullptr);
        if (keyboardFocusWidget) {
            if (QApplication::focusWidget() == q)
                keyboardFocusWidget->setFocus(Qt::MenuBarFocusReason);
            keyboardFocusWidget = nullptr;
        }
    }
    q->update();
}

//  from src/widgets/widgets/qmenubar.cpp, line 480, as _ZN15QMenuBarPrivate14activateActionEP7QActionNS0_11ActionEventE
inline void QMenuBarPrivate::activateAction(QAction *action, QAction::ActionEvent action_e)
{
    Q_Q(QMenuBar);
    if (!action || !action->isEnabled())
        return;
    action->activate(action_e);
    if (action_e == QAction::Hover)
        action->showStatusText(q);

//     if (action_e == QAction::Trigger)
//         emit q->activated(action);
//     else if (action_e == QAction::Hover)
//         emit q->highlighted(action);
}

//  from src/widgets/widgets/qmenubar.cpp, line 496, as _ZN15QMenuBarPrivate18_q_actionTriggeredEv
inline void QMenuBarPrivate::_q_actionTriggered()
{
    Q_Q(QMenuBar);
    if (QAction *action = qobject_cast<QAction *>(q->sender())) {
        emit q->triggered(action);
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 504, as _ZN15QMenuBarPrivate16_q_actionHoveredEv
inline void QMenuBarPrivate::_q_actionHovered()
{
    Q_Q(QMenuBar);
    if (QAction *action = qobject_cast<QAction *>(q->sender())) {
        emit q->hovered(action);
#if QT_CONFIG(accessibility)
        if (QAccessible::isActive()) {
            int actionIndex = actions.indexOf(action);
            QAccessibleEvent focusEvent(q, QAccessible::Focus);
            focusEvent.setChild(actionIndex);
            QAccessible::updateAccessibility(&focusEvent);
        }
#endif // QT_CONFIG(accessibility)
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 1686, as _ZN15QMenuBarPrivate28_q_internalShortcutActivatedEi
inline void QMenuBarPrivate::_q_internalShortcutActivated(int id)
{
    Q_Q(QMenuBar);
    QAction *act = actions.at(id);
    if (act && act->menu()) {
        if (QPlatformMenu *platformMenu = act->menu()->platformMenu()) {
            platformMenu->showPopup(q->windowHandle(), actionRects.at(id), nullptr);
            return;
        }
    }

    keyboardFocusWidget = QApplication::focusWidget();
    setCurrentAction(act, true, true);
    if (act && !act->menu()) {
        activateAction(act, QAction::Trigger);
        //100 is the same as the default value in QPushButton::animateClick
        autoReleaseTimer.start(100, q);
    } else if (act && q->style()->styleHint(QStyle::SH_MenuBar_AltKeyNavigation, nullptr, q)) {
        // When we open a menu using a shortcut, we should end up in keyboard state
        setKeyboardMode(true);
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 1709, as _ZN15QMenuBarPrivate15_q_updateLayoutEv
inline void QMenuBarPrivate::_q_updateLayout()
{
    Q_Q(QMenuBar);
    itemsDirty = true;
    if (q->isVisible()) {
        updateGeometries();
        q->update();
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 123, as _ZN15QMenuBarPrivate9isVisibleEP7QAction
inline bool QMenuBarPrivate::isVisible(QAction *action)
{
    return !hiddenActions.contains(action);
}

//  from src/widgets/widgets/qmenubar.cpp, line 1306, as _ZN15QMenuBarPrivate14handleReparentEv
inline void QMenuBarPrivate::handleReparent()
{
    Q_Q(QMenuBar);
    QWidget *newParent = q->parentWidget();

    //Note: if parent is reparented, then window may change even if parent doesn't.
    // We need to install an avent filter on each parent up to the parent that is
    // also a window (for shortcuts)
    QWidget *newWindow = newParent ? newParent->window() : nullptr;

    QList<QPointer<QWidget>> newParents;
    // Remove event filters on ex-parents, keep them on still-parents
    // The parents are always ordered in the vector
    //
    // Take a copy because this method is called from changeEvent() and eventFilter(),
    // which might cause recursion into the class due to event processing, which might
    // modify oldParents.
    const auto copy = oldParents;
    for (const QPointer<QWidget> &w : copy) {
        if (w) {
            if (newParent == w) {
                newParents.append(w);
                if (newParent != newWindow) //stop at the window
                    newParent = newParent->parentWidget();
            } else {
                w->removeEventFilter(q);
            }
        }
    }

    // At this point, newParent is the next one to be added to newParents
    while (newParent && newParent != newWindow) {
        //install event filters all the way up to (excluding) the window
        newParents.append(newParent);
        newParent->installEventFilter(q);
        newParent = newParent->parentWidget();
    }

    if (newParent && newWindow) {
        // Install the event filter on the window
        newParents.append(newParent);
        newParent->installEventFilter(q);
    }
    oldParents = newParents;

    if (platformMenuBar) {
        if (newWindow) {
            // force the underlying platform window to be created, since
            // the platform menubar needs it (and we have no other way to
            // discover when the platform window is created)
            newWindow->createWinId();
            platformMenuBar->handleReparent(newWindow->windowHandle());
        } else {
            platformMenuBar->handleReparent(nullptr);
        }
    }
}

//  from src/widgets/widgets/qmenubar.cpp, line 1170, as _ZN15QMenuBarPrivate15getPlatformMenuEPK7QAction
inline QPlatformMenu *QMenuBarPrivate::getPlatformMenu(const QAction *action)
{
    if (!action || !action->menu())
        return nullptr;

    QPlatformMenu *platformMenu = action->menu()->platformMenu();
    if (!platformMenu && platformMenuBar) {
        platformMenu = platformMenuBar->createMenu();
        if (platformMenu)
            action->menu()->setPlatformMenu(platformMenu);
    }

    return platformMenu;
}

//  from src/widgets/widgets/qmenubar.cpp, line 1185, as _ZN15QMenuBarPrivate25findInsertionPlatformMenuEPK7QAction
inline QPlatformMenu *QMenuBarPrivate::findInsertionPlatformMenu(const QAction *action)
{
    Q_Q(QMenuBar);
    QPlatformMenu *beforeMenu = nullptr;
    for (qsizetype beforeIndex = indexOf(const_cast<QAction *>(action)) + 1;
         !beforeMenu && (beforeIndex < q->actions().size());
         ++beforeIndex) {
        beforeMenu = getPlatformMenu(q->actions().at(beforeIndex));
    }

    return beforeMenu;
}

//  from src/widgets/widgets/qmenubar.cpp, line 1198, as _ZN15QMenuBarPrivate24copyActionToPlatformMenuEPK7QActionP13QPlatformMenu
inline void QMenuBarPrivate::copyActionToPlatformMenu(const QAction *action, QPlatformMenu *menu)
{
    const auto tag = reinterpret_cast<quintptr>(action);
    if (menu->tag() != tag)
        menu->setTag(tag);
    menu->setText(action->text());
    menu->setVisible(action->isVisible());
    menu->setEnabled(action->isEnabled());
}
//  -----------------------------------------------------------------------

//  A QMenuBarPrivate that Python can take functions over in. Every QMenuBarPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMenuBarPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQMenuBarPrivateCall1)(const void *, int, int *);
typedef void (*CuteQMenuBarPrivateCall2)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall3)(const void *, int *);
typedef void * (*CuteQMenuBarPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQMenuBarPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQMenuBarPrivateCall6)(const void *, int *);
typedef int (*CuteQMenuBarPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQMenuBarPrivateCall8)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall9)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall10)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall11)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall12)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall13)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall14)(const void *, int *);
typedef void (*CuteQMenuBarPrivateCall15)(const void *, int *);
typedef bool (*CuteQMenuBarPrivateCall16)(const void *, int *);
typedef bool (*CuteQMenuBarPrivateCall17)(const void *, int *);
class CuteQMenuBarPrivate : public QMenuBarPrivate {
public:
  using QMenuBarPrivate::QMenuBarPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMenuBarPrivateCall0 call = reinterpret_cast<CuteQMenuBarPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMenuBarPrivateCall1 call = reinterpret_cast<CuteQMenuBarPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQMenuBarPrivateCall2 call = reinterpret_cast<CuteQMenuBarPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMenuBarPrivateCall3 call = reinterpret_cast<CuteQMenuBarPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQMenuBarPrivateCall4 call = reinterpret_cast<CuteQMenuBarPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQMenuBarPrivateCall5 call = reinterpret_cast<CuteQMenuBarPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQMenuBarPrivateCall6 call = reinterpret_cast<CuteQMenuBarPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMenuBarPrivateCall7 call = reinterpret_cast<CuteQMenuBarPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQMenuBarPrivateCall8 call = reinterpret_cast<CuteQMenuBarPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQMenuBarPrivateCall9 call = reinterpret_cast<CuteQMenuBarPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQMenuBarPrivateCall10 call = reinterpret_cast<CuteQMenuBarPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQMenuBarPrivateCall11 call = reinterpret_cast<CuteQMenuBarPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQMenuBarPrivateCall12 call = reinterpret_cast<CuteQMenuBarPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQMenuBarPrivateCall13 call = reinterpret_cast<CuteQMenuBarPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQMenuBarPrivateCall14 call = reinterpret_cast<CuteQMenuBarPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQMenuBarPrivateCall15 call = reinterpret_cast<CuteQMenuBarPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQMenuBarPrivateCall16 call = reinterpret_cast<CuteQMenuBarPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQMenuBarPrivateCall17 call = reinterpret_cast<CuteQMenuBarPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QMenuBar *QMenuBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZN15QMenuBarPrivate6q_funcEv(QMenuBarPrivate *self) {
  return self->q_func();
}

//  const QMenuBar *QMenuBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMenuBar *ritual_ZNK15QMenuBarPrivate6q_funcEv(
    const QMenuBarPrivate *self) {
  return self->q_func();
}

//  QMenuBarPrivate::QMenuBarPrivate()
extern "C" Q_DECL_EXPORT
QMenuBarPrivate *ritual_ZN15QMenuBarPrivateC1Ev() {
  return new CuteQMenuBarPrivate();
}

//  QMenuBarPrivate::~QMenuBarPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivateD1Ev(QMenuBarPrivate *self) {
  delete self;
}

#if defined(Q_OS_LINUX)
//  QAction *QMenuBarPrivate::getNextAction(const qsizetype start, const
//      qsizetype increment) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK15QMenuBarPrivate13getNextActionExx(
    const QMenuBarPrivate *self,
    qsizetype start,
    qsizetype increment) {
  return self->getNextAction(start, increment);
}
#endif  // defined(Q_OS_LINUX)

//  void QMenuBarPrivate::calcActionRects(int max_width, int start) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QMenuBarPrivate15calcActionRectsEii(
    const QMenuBarPrivate *self,
    int max_width,
    int start) {
  self->calcActionRects(max_width, start);
}

#if defined(Q_OS_LINUX)
//  QRect QMenuBarPrivate::actionRect(QAction *a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK15QMenuBarPrivate10actionRectEP7QAction(
    const QMenuBarPrivate *self,
    QAction *a0) {
  return new QRect(self->actionRect(a0));
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::mouseRelaseEventFromQMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate25mouseRelaseEventFromQMenuEv(
    QMenuBarPrivate *self) {
  self->mouseRelaseEventFromQMenu();
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  QAction *QMenuBarPrivate::actionAt(QPoint p) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK15QMenuBarPrivate8actionAtE6QPoint(
    const QMenuBarPrivate *self,
    const QPoint *p) {
  return self->actionAt(*p);
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::setCurrentAction(QAction *a0, bool a1, bool a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate16setCurrentActionEP7QActionbb(
    QMenuBarPrivate *self,
    QAction *a0,
    bool a1,
    bool a2) {
  self->setCurrentAction(a0, a1, a2);
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::popupAction(QAction *a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate11popupActionEP7QActionb(
    QMenuBarPrivate *self,
    QAction *a0,
    bool a1) {
  self->popupAction(a0, a1);
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::focusFirstAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate16focusFirstActionEv(QMenuBarPrivate *self) {
  self->focusFirstAction();
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::setKeyboardMode(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate15setKeyboardModeEb(
    QMenuBarPrivate *self,
    bool a0) {
  self->setKeyboardMode(a0);
}
#endif  // defined(Q_OS_LINUX)

//  void QMenuBarPrivate::activateAction(QAction *a0, QAction::ActionEvent
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate14activateActionEP7QActionNS0_11ActionEventE(
    QMenuBarPrivate *self,
    QAction *a0,
    QAction::ActionEvent a1) {
  self->activateAction(a0, a1);
}

//  void QMenuBarPrivate::_q_actionTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate18_q_actionTriggeredEv(
    QMenuBarPrivate *self) {
  self->_q_actionTriggered();
}

//  void QMenuBarPrivate::_q_actionHovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate16_q_actionHoveredEv(QMenuBarPrivate *self) {
  self->_q_actionHovered();
}

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::_q_internalShortcutActivated(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate28_q_internalShortcutActivatedEi(
    QMenuBarPrivate *self,
    int a0) {
  self->_q_internalShortcutActivated(a0);
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  void QMenuBarPrivate::_q_updateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate15_q_updateLayoutEv(QMenuBarPrivate *self) {
  self->_q_updateLayout();
}
#endif  // defined(Q_OS_LINUX)

//  bool QMenuBarPrivate::isVisible(QAction *action)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QMenuBarPrivate9isVisibleEP7QAction(
    QMenuBarPrivate *self,
    QAction *action) {
  return self->isVisible(action);
}

//  void QMenuBarPrivate::handleReparent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate14handleReparentEv(QMenuBarPrivate *self) {
  self->handleReparent();
}

//  QPlatformMenu *QMenuBarPrivate::getPlatformMenu(const QAction *action)
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZN15QMenuBarPrivate15getPlatformMenuEPK7QAction(
    QMenuBarPrivate *self,
    const QAction *action) {
  return self->getPlatformMenu(action);
}

//  QPlatformMenu *QMenuBarPrivate::findInsertionPlatformMenu(const QAction
//      *action)
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZN15QMenuBarPrivate25findInsertionPlatformMenuEPK7QAction(
    QMenuBarPrivate *self,
    const QAction *action) {
  return self->findInsertionPlatformMenu(action);
}

//  void QMenuBarPrivate::copyActionToPlatformMenu(const QAction *e,
//      QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMenuBarPrivate24copyActionToPlatformMenuEPK7QActionP13QPlatformMenu(
    QMenuBarPrivate *self,
    const QAction *e,
    QPlatformMenu *menu) {
  self->copyActionToPlatformMenu(e, menu);
}

//  int QMenuBarPrivate::indexOf(QAction *act) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QMenuBarPrivate7indexOfEP7QAction(
    const QMenuBarPrivate *self,
    QAction *act) {
  return self->indexOf(act);
}

//  a Python function taken by a CuteQMenuBarPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMenuBarPrivate(
    QMenuBarPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMenuBarPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menubar)
