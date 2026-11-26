//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(menu)
#if QT_CONFIG(menu)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qmenu.cpp, line 854, as local:qmenu.cpp:ResetOnDestroy
class ResetOnDestroy
{
public:
    ResetOnDestroy(QMenuSloppyState *sloppyState, bool *guard)
        : toReset(sloppyState)
        , guard(guard)
    {
        *guard = false;
    }

    ~ResetOnDestroy()
    {
        if (!*guard)
            toReset->reset();
    }

    QMenuSloppyState *toReset;
    bool *guard;
};

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

//  from src/widgets/widgets/qmenu.cpp, line 910, as _ZNK12QMenuPrivate15topCausedWidgetEv
inline QWidget *QMenuPrivate::topCausedWidget() const
{
    QWidget* top = causedPopup.widget;
    while (QMenu* m = qobject_cast<QMenu *>(top))
        top = m->d_func()->causedPopup.widget;
    return top;
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

//  from src/widgets/widgets/qmenu.cpp, line 333, as _ZNK12QMenuPrivate17updateActionRectsEv
inline void QMenuPrivate::updateActionRects() const
{
    updateActionRects(popupGeometry());
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

//  from src/widgets/widgets/qmenu.cpp, line 279, as _ZNK12QMenuPrivate14scrollerHeightEv
inline int QMenuPrivate::scrollerHeight() const
{
    Q_Q(const QMenu);
    return q->style()->pixelMetric(QStyle::PM_MenuScrollerHeight, nullptr, q);
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

//  from src/widgets/styles/qstyle.cpp, line 2475, as _ZN13QStylePrivate21useFullScreenForPopupEv
inline bool QStylePrivate::useFullScreenForPopup()
{
    auto theme = QGuiApplicationPrivate::platformTheme();
    return theme && theme->themeHint(QPlatformTheme::UseFullScreenForPopupMenu).toBool();
}

//  from src/widgets/widgets/qmenu.cpp, line 780, as _ZN16QMenuSloppyState5resetEv
inline void QMenuSloppyState::reset()
{
    m_enabled = false;
    m_first_mouse = true;
    m_init_guard = false;
    m_use_reset_action = true;
    m_uni_dir_discarded_count = 0;
    m_time.stop();
    m_reset_action = nullptr;
    m_origin_action = nullptr;
    m_action_rect = QRect();
    m_previous_point = QPointF();
    if (m_sub_menu) {
        QMenuPrivate::get(m_sub_menu)->sloppyState.m_parent = nullptr;
        m_sub_menu = nullptr;
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 797, as _ZN16QMenuSloppyState5enterEv
inline void QMenuSloppyState::enter()
{
    QMenuPrivate *menuPriv = QMenuPrivate::get(m_menu);

    if (m_discard_state_when_entering_parent && m_sub_menu == menuPriv->activeMenu) {
        menuPriv->hideMenu(m_sub_menu);
        reset();
    }
    if (m_parent)
        m_parent->childEnter();
}

//  from src/widgets/widgets/qmenu.cpp, line 809, as _ZN16QMenuSloppyState10childEnterEv
inline void QMenuSloppyState::childEnter()
{
    stopTimer();
    if (m_parent)
        m_parent->childEnter();
}

//  from src/widgets/widgets/qmenu.cpp, line 816, as _ZN16QMenuSloppyState5leaveEv
inline void QMenuSloppyState::leave()
{
    if (!m_dont_start_time_on_leave) {
        if (m_parent)
            m_parent->childLeave();
        startTimerIfNotRunning();
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 825, as _ZN16QMenuSloppyState10childLeaveEv
inline void QMenuSloppyState::childLeave()
{
    if (m_enabled && !QMenuPrivate::get(m_menu)->hasReceievedEnter) {
        startTimerIfNotRunning();
        if (m_parent)
            m_parent->childLeave();
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 834, as _ZN16QMenuSloppyState15setSubMenuPopupERK5QRectP7QActionP5QMenu
inline void QMenuSloppyState::setSubMenuPopup(const QRect &actionRect, QAction *resetAction, QMenu *subMenu)
{
    m_enabled = true;
    m_init_guard = true;
    m_use_reset_action = true;
    m_time.stop();
    m_action_rect = actionRect;
    if (m_sub_menu)
        QMenuPrivate::get(m_sub_menu)->sloppyState.m_parent = nullptr;
    m_sub_menu = subMenu;
    QMenuPrivate::get(subMenu)->sloppyState.m_parent = this;
    m_reset_action = resetAction;
    m_origin_action = resetAction;
}

//  from src/widgets/widgets/qmenu.cpp, line 849, as _ZNK16QMenuSloppyState25hasParentActiveDelayTimerEv
inline bool QMenuSloppyState::hasParentActiveDelayTimer() const
{
    return m_parent && m_parent->m_menu && QMenuPrivate::get(m_parent->m_menu)->delayState.timer.isActive();
}
//  -----------------------------------------------------------------------

//  QMenuSloppyState::QMenuSloppyState()
extern "C" Q_DECL_EXPORT
QMenuSloppyState *ritual_ZN16QMenuSloppyStateC1Ev() {
  return new QMenuSloppyState();
}

//  QMenuSloppyState::~QMenuSloppyState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyStateD1Ev(QMenuSloppyState *self) {
  delete self;
}

//  void QMenuSloppyState::initialize(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState10initializeEP5QMenu(
    QMenuSloppyState *self,
    QMenu *menu) {
  self->initialize(menu);
}

//  void QMenuSloppyState::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState5resetEv(QMenuSloppyState *self) {
  self->reset();
}

//  bool QMenuSloppyState::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMenuSloppyState7enabledEv(const QMenuSloppyState *self) {
  return self->enabled();
}

//  void QMenuSloppyState::startTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState10startTimerEv(QMenuSloppyState *self) {
  self->startTimer();
}

//  void QMenuSloppyState::startTimerIfNotRunning()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState22startTimerIfNotRunningEv(
    QMenuSloppyState *self) {
  self->startTimerIfNotRunning();
}

//  void QMenuSloppyState::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState9stopTimerEv(QMenuSloppyState *self) {
  self->stopTimer();
}

//  void QMenuSloppyState::enter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState5enterEv(QMenuSloppyState *self) {
  self->enter();
}

//  void QMenuSloppyState::childEnter()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState10childEnterEv(QMenuSloppyState *self) {
  self->childEnter();
}

//  void QMenuSloppyState::leave()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState5leaveEv(QMenuSloppyState *self) {
  self->leave();
}

//  void QMenuSloppyState::childLeave()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState10childLeaveEv(QMenuSloppyState *self) {
  self->childLeave();
}

//  qreal QMenuSloppyState::slope(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN16QMenuSloppyState5slopeERK7QPointFS2_(
    const QPointF *p1,
    const QPointF *p2) {
  return QMenuSloppyState::slope(*p1, *p2);
}

//  bool QMenuSloppyState::checkSlope(qreal oldS, qreal newS, bool
//      wantSteeper)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QMenuSloppyState10checkSlopeEddb(
    QMenuSloppyState *self,
    qreal oldS,
    qreal newS,
    bool wantSteeper) {
  return self->checkSlope(oldS, newS, wantSteeper);
}

//  MouseEventResult QMenuSloppyState::processMouseEvent(const QPointF
//      &mousePos, QAction *resetAction, QAction *currentAction)
extern "C" Q_DECL_EXPORT
QMenuSloppyState::MouseEventResult ritual_ZN16QMenuSloppyState17processMouseEventERK7QPointFP7QActionS4_(
    QMenuSloppyState *self,
    const QPointF *mousePos,
    QAction *resetAction,
    QAction *currentAction) {
  return self->processMouseEvent(*mousePos, resetAction, currentAction);
}

//  void QMenuSloppyState::setSubMenuPopup(const QRect &actionRect, QAction
//      *resetAction, QMenu *subMenu)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMenuSloppyState15setSubMenuPopupERK5QRectP7QActionP5QMenu(
    QMenuSloppyState *self,
    const QRect *actionRect,
    QAction *resetAction,
    QMenu *subMenu) {
  self->setSubMenuPopup(*actionRect, resetAction, subMenu);
}

//  bool QMenuSloppyState::hasParentActiveDelayTimer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMenuSloppyState25hasParentActiveDelayTimerEv(
    const QMenuSloppyState *self) {
  return self->hasParentActiveDelayTimer();
}

//  int QMenuSloppyState::timeForTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QMenuSloppyState14timeForTimeoutEv(
    const QMenuSloppyState *self) {
  return self->timeForTimeout();
}

//  bool QMenuSloppyState::isTimerId(int timerId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMenuSloppyState9isTimerIdEi(
    const QMenuSloppyState *self,
    int timerId) {
  return self->isTimerId(timerId);
}

//  QMenu *QMenuSloppyState::subMenu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK16QMenuSloppyState7subMenuEv(const QMenuSloppyState *self) {
  return self->subMenu();
}

#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(menu)
