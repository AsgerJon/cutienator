//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(menu)
#if QT_CONFIG(menu)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qmenu.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h>
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
#include <QtCore/QPoint>
#include <QtCore/QList>
#include <QtCore/QPointer>
#include <QtWidgets/QWidget>
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
#include <QtWidgets/qapplication.h>
#include <QtGui/qbitmap.h>
#if QT_CONFIG(dialog)
#include <QtWidgets/private/qdialog_p.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpointer.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qtoolbar.h>
#endif
#include <QtCore/qdebug.h>
#include <QtWidgets/qlayoutitem.h>
#if QT_CONFIG(dialogbuttonbox)
#include <QtWidgets/qdialogbuttonbox.h>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#include <QtWidgets/private/qmenu_p.h>
#endif
#include <QtWidgets/private/qpushbutton_p.h>
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

//  from src/widgets/widgets/qmenu.cpp, line 53, as local:qmenu.cpp:QTornOffMenu
class QTornOffMenu : public QMenu
{
    Q_OBJECT
    class QTornOffMenuPrivate : public QMenuPrivate
    {
        Q_DECLARE_PUBLIC(QTornOffMenu)
    public:
        QTornOffMenuPrivate(QMenu *p) : causedMenu(p), initialized(false) {
            tornoff = 1;
            causedPopup.widget = nullptr;
            causedPopup.action = p->d_func()->causedPopup.action;
            causedStack = p->d_func()->calcCausedStack();
        }

        void setMenuSize(const QSize &menuSize) {
            Q_Q(QTornOffMenu);
            QSize size = menuSize;
            const QPoint p = (!initialized) ? causedMenu->pos() : q->pos();
            const QRect screen = popupGeometry(QGuiApplication::screenAt(p));
            const int desktopFrame = q->style()->pixelMetric(QStyle::PM_MenuDesktopFrameWidth, nullptr, q);
            const int titleBarHeight = q->style()->pixelMetric(QStyle::PM_TitleBarHeight, nullptr, q);
            if (scroll && (size.height() > screen.height() - titleBarHeight || size.width() > screen.width())) {
                const int fw = q->style()->pixelMetric(QStyle::PM_MenuPanelWidth, nullptr, q);
                const int hmargin = q->style()->pixelMetric(QStyle::PM_MenuHMargin, nullptr, q);
                scroll->scrollFlags |= uint(QMenuPrivate::QMenuScroller::ScrollDown);
                size.setWidth(qMin(actionRects.at(getLastVisibleAction()).right() + fw + hmargin + rightmargin + 1, screen.width()));
                size.setHeight(screen.height() - desktopFrame * 2 - titleBarHeight);
            }
            q->setFixedSize(size);
        }

        QList<QPointer<QWidget>> calcCausedStack() const override { return causedStack; }
        QPointer<QMenu> causedMenu;
        QList<QPointer<QWidget>> causedStack;
        bool initialized;
    };

public:
    QTornOffMenu(QMenu *p) : QMenu(*(new QTornOffMenuPrivate(p)))
    {
        Q_D(QTornOffMenu);
        // make the torn-off menu a sibling of p (instead of a child)
        QWidget *parentWidget = d->causedStack.isEmpty() ? p : d->causedStack.constLast();
        if (!parentWidget && p)
            parentWidget = p;
        if (parentWidget && parentWidget->parentWidget())
            parentWidget = parentWidget->parentWidget();
        setParent(parentWidget, Qt::Window | Qt::Tool);
        setAttribute(Qt::WA_DeleteOnClose, true);
        setAttribute(Qt::WA_X11NetWmWindowTypeMenu, true);
        updateWindowTitle();
        setEnabled(p->isEnabled());
#if QT_CONFIG(style_stylesheet)
        setStyleSheet(p->styleSheet());
#endif
        if (style() != p->style())
            setStyle(p->style());
        setContentsMargins(p->contentsMargins());
        setLayoutDirection(p->layoutDirection());
        //QObject::connect(this, SIGNAL(triggered(QAction*)), this, SLOT(onTrigger(QAction*)));
        //QObject::connect(this, SIGNAL(hovered(QAction*)), this, SLOT(onHovered(QAction*)));
        QList<QAction*> items = p->actions();
        for(int i = 0; i < items.size(); i++)
            addAction(items.at(i));
        d->setMenuSize(sizeHint());
        d->initialized = true;
    }
    void syncWithMenu(QMenu *menu, QActionEvent *act)
    {
        Q_D(QTornOffMenu);
        if (menu != d->causedMenu)
            return;
        auto action = static_cast<QAction *>(act->action());
        if (act->type() == QEvent::ActionAdded) {
            insertAction(static_cast<QAction *>(act->before()), action);
        } else if (act->type() == QEvent::ActionRemoved)
            removeAction(action);
    }
    void actionEvent(QActionEvent *e) override
    {
        Q_D(QTornOffMenu);
        QMenu::actionEvent(e);
        if (d->initialized) {
            d->setMenuSize(sizeHint());
        }
    }

    void updateWindowTitle()
    {
        Q_D(QTornOffMenu);
        if (!d->causedMenu)
            return;
        const QString &cleanTitle = QPlatformTheme::removeMnemonics(d->causedMenu->title()).trimmed();
        setWindowTitle(cleanTitle);
    }

public slots:
    void onTrigger(QAction *action) { d_func()->activateAction(action, QAction::Trigger, false); }
    void onHovered(QAction *action) { d_func()->activateAction(action, QAction::Hover, false); }

private:
    Q_DECLARE_PRIVATE(QTornOffMenu)
    friend class QMenuPrivate;
};

//  from src/widgets/widgets/qmenu.cpp, line 220, as local:qmenu.cpp:getParentWidget
static QWidget *getParentWidget(const QAction *action)
{
    auto result = action->parent();
    while (result && !qobject_cast<QWidget *>(result))
        result = result->parent();
    return static_cast<QWidget *>(result);
}

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

//  from src/widgets/widgets/qmenu.cpp, line 309, as _ZNK12QMenuPrivate15calcCausedStackEv
inline QList<QPointer<QWidget>> QMenuPrivate::calcCausedStack() const
{
    QList<QPointer<QWidget>> ret;
    for(QWidget *widget = causedPopup.widget; widget; ) {
        ret.append(widget);
        if (QTornOffMenu *qtmenu = qobject_cast<QTornOffMenu*>(widget))
            ret += qtmenu->d_func()->causedStack;
        if (QMenu *qmenu = qobject_cast<QMenu*>(widget))
            widget = qmenu->d_func()->causedPopup.widget;
        else
            break;
    }
    return ret;
}

//  from src/widgets/styles/qstyle.cpp, line 2475, as _ZN13QStylePrivate21useFullScreenForPopupEv
inline bool QStylePrivate::useFullScreenForPopup()
{
    auto theme = QGuiApplicationPrivate::platformTheme();
    return theme && theme->themeHint(QPlatformTheme::UseFullScreenForPopupMenu).toBool();
}

//  from src/widgets/widgets/qpushbutton.cpp, line 587, as _ZN18QPushButtonPrivate20adjustedMenuPositionEv
#if QT_CONFIG(menu)
inline QPoint QPushButtonPrivate::adjustedMenuPosition()
{
    Q_Q(QPushButton);

    bool horizontal = true;
#if QT_CONFIG(toolbar)
    QToolBar *tb = qobject_cast<QToolBar*>(parent);
    if (tb && tb->orientation() == Qt::Vertical)
        horizontal = false;
#endif

    QWidgetItem item(q);
    QRect rect = item.geometry();
    rect.setRect(rect.x() - q->x(), rect.y() - q->y(), rect.width(), rect.height());

    QSize menuSize = menu->sizeHint();
    QPoint globalPos = q->mapToGlobal(rect.topLeft());
    int x = globalPos.x();
    int y = globalPos.y();
    const QRect availableGeometry = QWidgetPrivate::availableScreenGeometry(q, q->mapToGlobal(rect.center()));
    if (horizontal) {
        if (globalPos.y() + rect.height() + menuSize.height() <= availableGeometry.bottom()) {
            y += rect.height();
        } else if (globalPos.y() - menuSize.height() >= availableGeometry.y()) {
            y -= menuSize.height();
        }
        if (q->layoutDirection() == Qt::RightToLeft)
            x += rect.width() - menuSize.width();
    } else {
        if (globalPos.x() + rect.width() + menu->sizeHint().width() <= availableGeometry.right()) {
            x += rect.width();
        } else if (globalPos.x() - menuSize.width() >= availableGeometry.x()) {
            x -= menuSize.width();
        }
    }

    return QPoint(x,y);
}
#endif  // QT_CONFIG(menu)

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

//  from src/widgets/widgets/qmenu.cpp, line 158, as _ZN12QMenuPrivate4initEv
inline void QMenuPrivate::init()
{
    Q_Q(QMenu);
#if QT_CONFIG(whatsthis)
    q->setAttribute(Qt::WA_CustomWhatsThis);
#endif
    q->setAttribute(Qt::WA_X11NetWmWindowTypePopupMenu);
    defaultMenuAction = menuAction = new QAction(q);
    menuAction->setMenu(q); // this calls setOverrideMenuAction
    setOverrideMenuAction(nullptr);
    QObject::connect(menuAction, &QAction::changed, q, [this] {
        if (!tornPopup.isNull())
            tornPopup->updateWindowTitle();
    });
    q->setMouseTracking(q->style()->styleHint(QStyle::SH_Menu_MouseTracking, nullptr, q));
    if (q->style()->styleHint(QStyle::SH_Menu_Scrollable, nullptr, q)) {
        scroll = new QMenuPrivate::QMenuScroller;
        scroll->scrollFlags = QMenuPrivate::QMenuScroller::ScrollNone;
    }

    sloppyState.initialize(q);
    delayState.initialize(q);
    mousePopupDelay = q->style()->styleHint(QStyle::SH_Menu_SubMenuPopupDelay, nullptr, q);
}

//  from src/widgets/widgets/qmenu.cpp, line 183, as _ZN12QMenuPrivate18createPlatformMenuEv
inline QPlatformMenu *QMenuPrivate::createPlatformMenu()
{
    Q_Q(QMenu);
    if (platformMenu.isNull())
        q->setPlatformMenu(QGuiApplicationPrivate::platformTheme()->createPlatformMenu());
    return platformMenu.data();
}

//  from src/widgets/widgets/qmenu.cpp, line 191, as _ZN12QMenuPrivate15setPlatformMenuEP13QPlatformMenu
inline void QMenuPrivate::setPlatformMenu(QPlatformMenu *menu)
{
    Q_Q(QMenu);
    if (!platformMenu.isNull() && !platformMenu->parent())
        delete platformMenu.data();

    platformMenu = menu;
    if (!platformMenu.isNull()) {
        QObject::connect(platformMenu, SIGNAL(aboutToShow()), q, SLOT(_q_platformMenuAboutToShow()));
        QObject::connect(platformMenu, SIGNAL(aboutToHide()), q, SIGNAL(aboutToHide()));
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 204, as _ZN12QMenuPrivate16syncPlatformMenuEv
inline void QMenuPrivate::syncPlatformMenu()
{
    Q_Q(QMenu);
    if (platformMenu.isNull())
        return;

    QPlatformMenuItem *beforeItem = nullptr;
    const QList<QAction*> actions = q->actions();
    for (QList<QAction*>::const_reverse_iterator it = actions.rbegin(), end = actions.rend(); it != end; ++it) {
        QPlatformMenuItem *menuItem = insertActionInPlatformMenu(*it, beforeItem);
        beforeItem = menuItem;
    }
    platformMenu->syncSeparatorsCollapsible(collapsibleSeparators);
    platformMenu->setEnabled(q->isEnabled());
}

//  from src/widgets/widgets/qmenu.cpp, line 228, as _ZN12QMenuPrivate24copyActionToPlatformItemEPK7QActionP17QPlatformMenuItem
inline void QMenuPrivate::copyActionToPlatformItem(const QAction *action, QPlatformMenuItem *item)
{
    item->setText(action->text());
    item->setIsSeparator(action->isSeparator());
    if (action->isIconVisibleInMenu()) {
        item->setIcon(action->icon());
        if (QWidget *w = getParentWidget(action)) {
            QStyleOption opt;
            opt.initFrom(w);
            item->setIconSize(w->style()->pixelMetric(QStyle::PM_SmallIconSize, &opt, w));
        } else {
            QStyleOption opt;
            item->setIconSize(QApplication::style()->pixelMetric(QStyle::PM_SmallIconSize, &opt, nullptr));
        }
    } else {
        item->setIcon(QIcon());
    }
    item->setVisible(action->isVisible());
#if QT_CONFIG(shortcut)
    item->setShortcut(action->shortcut());
#endif
    item->setCheckable(action->isCheckable());
    item->setChecked(action->isChecked());
    item->setHasExclusiveGroup(action->actionGroup() && action->actionGroup()->isExclusive());
    item->setFont(action->font());
    item->setRole((QPlatformMenuItem::MenuRole) action->menuRole());
    item->setEnabled(action->isEnabled());

    if (action->menu()) {
        if (!action->menu()->platformMenu())
            action->menu()->setPlatformMenu(platformMenu->createSubMenu());
        item->setMenu(action->menu()->platformMenu());
    } else {
        item->setMenu(nullptr);
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 265, as _ZN12QMenuPrivate26insertActionInPlatformMenuEPK7QActionP17QPlatformMenuItem
inline QPlatformMenuItem * QMenuPrivate::insertActionInPlatformMenu(const QAction *action, QPlatformMenuItem *beforeItem)
{
    QPlatformMenuItem *menuItem = platformMenu->createMenuItem();
    Q_ASSERT(menuItem);

    menuItem->setTag(reinterpret_cast<quintptr>(action));
    QObject::connect(menuItem, &QPlatformMenuItem::activated, action, &QAction::trigger, Qt::QueuedConnection);
    QObject::connect(menuItem, &QPlatformMenuItem::hovered, action, &QAction::hovered, Qt::QueuedConnection);
    copyActionToPlatformItem(action, menuItem);
    platformMenu->insertMenuItem(menuItem, beforeItem);

    return menuItem;
}

//  from src/widgets/widgets/qmenu.cpp, line 279, as _ZNK12QMenuPrivate14scrollerHeightEv
inline int QMenuPrivate::scrollerHeight() const
{
    Q_Q(const QMenu);
    return q->style()->pixelMetric(QStyle::PM_MenuScrollerHeight, nullptr, q);
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

//  from src/widgets/widgets/qmenu.cpp, line 333, as _ZNK12QMenuPrivate17updateActionRectsEv
inline void QMenuPrivate::updateActionRects() const
{
    updateActionRects(popupGeometry());
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

//  from src/widgets/widgets/qmenu.cpp, line 287, as _ZNK12QMenuPrivate21useFullScreenForPopupEv
inline bool QMenuPrivate::useFullScreenForPopup() const
{
    return !tornoff && QStylePrivate::useFullScreenForPopup();
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

//  from src/widgets/widgets/qmenu.cpp, line 2313, as _ZN12QMenuPrivate5popupERK6QPointP7QActionSt8functionIFS0_RK5QSizeEE
inline void QMenuPrivate::popup(const QPoint &p, QAction *atAction, PositionFunction positionFunction)
{
    Q_Q(QMenu);
    popupScreen = QGuiApplication::screenAt(p);
    QScopeGuard popupScreenGuard([this](){ popupScreen.clear(); });

    if (scroll) { // reset scroll state from last popup
        if (scroll->scrollOffset)
            itemsDirty = 1; // sizeHint will be incorrect if there is previous scroll
        scroll->scrollOffset = 0;
        scroll->scrollFlags = QMenuPrivate::QMenuScroller::ScrollNone;
    }
    tearoffHighlighted = 0;
    motions = 0;
    doChildEffects = true;
    updateLayoutDirection();

    q->ensurePolished(); // Get the right font

    // Ensure that we get correct sizeHints by placing this window on the correct screen.
    if (!eventLoop) {
        bool screenSet = false;
        QScreen *screen = topData()->initialScreen;
        if (screen) {
            if (setScreen(screen))
                itemsDirty = true;
            screenSet = true;
        } else if (QMenu *parentMenu = qobject_cast<QMenu *>(parent)) {
            // a submenu is always opened from an open parent menu,
            // so show it on the same screen where the parent is. (QTBUG-76162)
            if (setScreen(parentMenu->screen()))
                itemsDirty = true;
            screenSet = true;
        }
        if (!screenSet && setScreenForPoint(p))
            itemsDirty = true;
    }

    const bool contextMenu = isContextMenu();
    if (lastContextMenu != contextMenu) {
        itemsDirty = true;
        lastContextMenu = contextMenu;
    }

    // Until QWidget::metric accepts the screen set on a widget (without having a window handle)
    // we need to make sure we get a window handle. This must be done near here because
    // we want the screen to be correctly set and items to be marked dirty.
    // (and screen set could 'fail' on oldscreen == newScreen if created before causing the
    // itemsDirty not to be set though needed to get the correct size on first show).
    if (!windowHandle()) {
        createWinId();
    }

#if QT_CONFIG(menubar)
    // if this menu is part of a chain attached to a QMenuBar, set the
    // _NET_WM_WINDOW_TYPE_DROPDOWN_MENU X11 window type
    q->setAttribute(Qt::WA_X11NetWmWindowTypeDropDownMenu, qobject_cast<QMenuBar *>(topCausedWidget()) != nullptr);
#endif

    emit q->aboutToShow();
    const bool actionListChanged = itemsDirty;

    QRect screen;
#if QT_CONFIG(graphicsview)
    bool isEmbedded = !bypassGraphicsProxyWidget(q) && QMenuPrivate::nearestGraphicsProxyWidget(q);
    if (isEmbedded)
        screen = popupGeometry();
    else
#endif
    screen = popupGeometry(QGuiApplication::screenAt(p));
    updateActionRects(screen);

    QPoint pos;
    QPushButton *causedButton = qobject_cast<QPushButton*>(causedPopup.widget);
    if (actionListChanged && causedButton)
        pos = QPushButtonPrivate::get(causedButton)->adjustedMenuPosition();
    else
        pos = p;
    popupScreen = QGuiApplication::screenAt(pos);

    const QSize menuSizeHint(q->sizeHint());
    QSize size = menuSizeHint;

    if (positionFunction)
        pos = positionFunction(menuSizeHint);

    const int desktopFrame = q->style()->pixelMetric(QStyle::PM_MenuDesktopFrameWidth, nullptr, q);
    bool adjustToDesktop = !q->window()->testAttribute(Qt::WA_DontShowOnScreen);

    // if the screens have very different geometries and the menu is too big, we have to recalculate
    if ((size.height() > screen.height() || size.width() > screen.width()) ||
        // Layout is not right, we might be able to save horizontal space
        (ncols >1 && size.height() < screen.height())) {
        size.setWidth(qMin(menuSizeHint.width(), screen.width() - desktopFrame * 2));
        size.setHeight(qMin(menuSizeHint.height(), screen.height() - desktopFrame * 2));
        adjustToDesktop = true;
    }

    if (ncols > 1) {
        pos.setY(screen.top() + desktopFrame);
    } else if (atAction) {
        for (int i = 0, above_height = 0; i < actions.size(); i++) {
            QAction *action = actions.at(i);
            if (action == atAction) {
                int newY = pos.y() - above_height;
                if (scroll && newY < desktopFrame) {
                    scroll->scrollFlags = scroll->scrollFlags
                                             | QMenuPrivate::QMenuScroller::ScrollUp;
                    scroll->scrollOffset = newY;
                    newY = desktopFrame;
                }
                pos.setY(newY);

                if (scroll && scroll->scrollFlags != QMenuPrivate::QMenuScroller::ScrollNone
                    && !q->style()->styleHint(QStyle::SH_Menu_FillScreenWithScroll, nullptr, q)) {
                    int below_height = above_height + scroll->scrollOffset;
                    for (int i2 = i; i2 < actionRects.size(); i2++)
                        below_height += actionRects.at(i2).height();
                    size.setHeight(below_height);
                }
                break;
            } else {
                above_height += actionRects.at(i).height();
            }
        }
    }

    // Do nothing if we don't have a valid size, e.g. when all actions are invisible
    // and there are no child widgets.
    const auto rectIsNull = [](const QRect &rect) { return rect.isNull(); };
    if (q->childrenRect().isEmpty()
     && std::all_of(actionRects.cbegin(), actionRects.cend(), rectIsNull)) {
        eventLoop = nullptr;
        syncAction = nullptr;
        return;
    }

    // Note that QGuiApplicationPrivate::lastCursorPosition isn't a QPointF,
    // so these two statements can't be simplified...
    const QPoint mouse = QGuiApplicationPrivate::lastCursorPosition.toPoint();
    mousePopupPos = QGuiApplicationPrivate::lastCursorPosition;
    const bool snapToMouse = !causedPopup.widget && (QRect(p.x() - 3, p.y() - 3, 6, 6).contains(mouse));

    if (adjustToDesktop) {
        // handle popup falling "off screen"
        if (q->isRightToLeft()) {
            if (snapToMouse) // position flowing left from the mouse
                pos.setX(mouse.x() - size.width());

#if QT_CONFIG(menubar)
            // if the menu is in a menubar or is a submenu, it should be right-aligned
            if (qobject_cast<QMenuBar*>(causedPopup.widget) || qobject_cast<QMenu*>(causedPopup.widget))
                pos.rx() -= size.width();
#endif // QT_CONFIG(menubar)

            if (pos.x() < screen.left() + desktopFrame)
                pos.setX(qMax(p.x(), screen.left() + desktopFrame));
            if (pos.x() + size.width() - 1 > screen.right() - desktopFrame)
                pos.setX(qMax(p.x() - size.width(), screen.right() - desktopFrame - size.width() + 1));
        } else {
            if (pos.x() + size.width() - 1 > screen.right() - desktopFrame)
                pos.setX(screen.right() - desktopFrame - size.width() + 1);
            if (pos.x() < screen.left() + desktopFrame)
                pos.setX(screen.left() + desktopFrame);
        }
        if (pos.y() + size.height() - 1 > screen.bottom() - desktopFrame) {
            if (snapToMouse)
                pos.setY(qMin(mouse.y() - (size.height() + desktopFrame), screen.bottom()-desktopFrame-size.height()+1));
            else
                pos.setY(qMax(p.y() - (size.height() + desktopFrame), screen.bottom()-desktopFrame-size.height()+1));
        }

        if (pos.y() < screen.top() + desktopFrame)
            pos.setY(screen.top() + desktopFrame);
        if (pos.y() + menuSizeHint.height() - 1 > screen.bottom() - desktopFrame) {
            if (scroll) {
                scroll->scrollFlags |= uint(QMenuPrivate::QMenuScroller::ScrollDown);
                int y = qMax(screen.y(),pos.y());
                size.setHeight(screen.bottom() - (desktopFrame * 2) - y);
            } else {
                // Too big for screen, bias to see bottom of menu (for some reason)
                pos.setY(screen.bottom() - size.height() + 1);
            }
        }
    }

    const int subMenuOffset = q->style()->pixelMetric(QStyle::PM_SubMenuOverlap, nullptr, q);
    QMenu *caused = qobject_cast<QMenu*>(causedPopup.widget);
    if (caused && caused->geometry().width() + menuSizeHint.width() + subMenuOffset < screen.width()) {
        QRect parentActionRect(caused->d_func()->actionRect(caused->d_func()->currentAction));
        const QPoint actionTopLeft = caused->mapToGlobal(parentActionRect.topLeft());
        parentActionRect.moveTopLeft(actionTopLeft);
        if (q->isRightToLeft()) {
            if ((pos.x() + menuSizeHint.width() > parentActionRect.left() - subMenuOffset)
                && (pos.x() < parentActionRect.right()))
            {
                pos.rx() = parentActionRect.left() - menuSizeHint.width();
                if (pos.x() < screen.x())
                    pos.rx() = parentActionRect.right();
                if (pos.x() + menuSizeHint.width() > screen.x() + screen.width())
                    pos.rx() = screen.x();
            }
        } else {
            if ((pos.x() < parentActionRect.right() + subMenuOffset)
                && (pos.x() + menuSizeHint.width() > parentActionRect.left()))
            {
                pos.rx() = parentActionRect.right();
                if (pos.x() + menuSizeHint.width() > screen.x() + screen.width())
                    pos.rx() = parentActionRect.left() - menuSizeHint.width();
                if (pos.x() < screen.x())
                    pos.rx() = screen.x() + screen.width() - menuSizeHint.width();
            }
        }
    }
    popupScreen = QGuiApplication::screenAt(pos);
    q->setGeometry(QRect(pos, size));

#if QT_CONFIG(wayland)
    q->create();
    if (auto waylandWindow = dynamic_cast<QNativeInterface::Private::QWaylandWindow*>(q->windowHandle()->handle())) {
        if (causedButton) {
            const QRect controlGeometry(causedButton->mapTo(causedButton->window(), QPoint(0, 0)), causedButton->size());
            waylandWindow->setParentControlGeometry(controlGeometry);
            waylandWindow->setExtendedWindowType(QNativeInterface::Private::QWaylandWindow::Menu);
        } else if (caused) {
            waylandWindow->setParentControlGeometry(caused->d_func()->actionRect(caused->d_func()->currentAction));
            waylandWindow->setExtendedWindowType(QNativeInterface::Private::QWaylandWindow::SubMenu);
        } else if (auto menubar = qobject_cast<QMenuBar*>(causedPopup.widget)) {
            QPoint menuBarWindowPosition = menubar->mapTo(menubar->window(), QPoint(0, 0));
            waylandWindow->setParentControlGeometry(menubar->actionGeometry(causedPopup.action).translated(menuBarWindowPosition));
            waylandWindow->setExtendedWindowType(QNativeInterface::Private::QWaylandWindow::Menu);
        }
    }
#endif

#if QT_CONFIG(effects)
    int hGuess = q->isRightToLeft() ? QEffects::LeftScroll : QEffects::RightScroll;
    int vGuess = QEffects::DownScroll;
    if (q->isRightToLeft()) {
        if ((snapToMouse && (pos.x() + size.width() / 2 > mouse.x())) ||
           (qobject_cast<QMenu*>(causedPopup.widget) && pos.x() + size.width() / 2 > causedPopup.widget->x()))
            hGuess = QEffects::RightScroll;
    } else {
        if ((snapToMouse && (pos.x() + size.width() / 2 < mouse.x())) ||
           (qobject_cast<QMenu*>(causedPopup.widget) && pos.x() + size.width() / 2 < causedPopup.widget->x()))
            hGuess = QEffects::LeftScroll;
    }

#if QT_CONFIG(menubar)
    if ((snapToMouse && (pos.y() + size.height() / 2 < mouse.y())) ||
       (qobject_cast<QMenuBar*>(causedPopup.widget) &&
        pos.y() + size.width() / 2 < causedPopup.widget->mapToGlobal(causedPopup.widget->pos()).y()))
       vGuess = QEffects::UpScroll;
#endif
    if (QApplication::isEffectEnabled(Qt::UI_AnimateMenu)) {
        bool doChildEffects = true;
#if QT_CONFIG(menubar)
        if (QMenuBar *mb = qobject_cast<QMenuBar*>(causedPopup.widget)) {
            doChildEffects = mb->d_func()->doChildEffects;
            mb->d_func()->doChildEffects = false;
        } else
#endif
        if (QMenu *m = qobject_cast<QMenu*>(causedPopup.widget)) {
            doChildEffects = m->d_func()->doChildEffects;
            m->d_func()->doChildEffects = false;
        }

        if (doChildEffects) {
            if (QApplication::isEffectEnabled(Qt::UI_FadeMenu))
                qFadeEffect(q);
            else if (causedPopup.widget)
                qScrollEffect(q, qobject_cast<QMenu*>(causedPopup.widget) ? hGuess : vGuess);
            else
                qScrollEffect(q, hGuess | vGuess);
        } else {
            // kill any running effect
            qFadeEffect(nullptr);
            qScrollEffect(nullptr);

            q->show();
        }
    } else
#endif
    {
        q->show();
    }

#if QT_CONFIG(accessibility)
    QAccessibleEvent event(q, QAccessible::PopupMenuStart);
    QAccessible::updateAccessibility(&event);
#endif
}

//  from src/widgets/widgets/qmenu.cpp, line 2670, as _ZN12QMenuPrivate4execERK6QPointP7QActionSt8functionIFS0_RK5QSizeEE
inline QAction *QMenuPrivate::exec(const QPoint &p, QAction *action, PositionFunction positionFunction)
{
    Q_Q(QMenu);
    q->ensurePolished();
    q->createWinId();
    QEventLoop evtLoop;
    eventLoop = &evtLoop;
    popup(p, action, positionFunction);

    QPointer<QObject> guard = q;
    if (eventLoop) // popup might have reset if there was nothing to show
        (void)eventLoop->exec();
    if (guard.isNull())
        return nullptr;

    action = syncAction;
    syncAction = nullptr;
    eventLoop = nullptr;
    popupScreen.clear();
    return action;
}

//  from src/widgets/widgets/qmenu.cpp, line 910, as _ZNK12QMenuPrivate15topCausedWidgetEv
inline QWidget *QMenuPrivate::topCausedWidget() const
{
    QWidget* top = causedPopup.widget;
    while (QMenu* m = qobject_cast<QMenu *>(top))
        top = m->d_func()->causedPopup.widget;
    return top;
}

//  from src/widgets/widgets/qmenu.cpp, line 918, as _ZNK12QMenuPrivate8actionAtE6QPoint
inline QAction *QMenuPrivate::actionAt(QPoint p) const
{
    if (!rect().contains(p))     //sanity check
       return nullptr;

    for(int i = 0; i < actionRects.size(); i++) {
        if (actionRects.at(i).contains(p))
            return actions.at(i);
    }
    return nullptr;
}

//  from src/widgets/widgets/qmenu.cpp, line 667, as _ZN12QMenuPrivate13setSyncActionEv
inline void QMenuPrivate::setSyncAction()
{
    Q_Q(QMenu);
    QAction *current = currentAction;
    if (current && (!current->isEnabled() || current->menu() || current->isSeparator()))
        current = nullptr;
    for(QWidget *caused = q; caused;) {
        if (QMenu *m = qobject_cast<QMenu*>(caused)) {
            caused = m->d_func()->causedPopup.widget;
            if (m->d_func()->eventLoop)
                m->d_func()->syncAction = current; // synchronous operation
        } else {
            break;
        }
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

//  from src/widgets/widgets/qmenu.cpp, line 625, as _ZNK12QMenuPrivate21transientParentWindowEv
inline QWindow *QMenuPrivate::transientParentWindow() const
{
    Q_Q(const QMenu);
    if (causedPopup.widget) {
        if (const QWidget *w = causedPopup.widget.data()) {
            if (const QWidget *ww = w->window())
                return ww->windowHandle();
        }
    }

    if (const QWidget *parent = q->nativeParentWidget()) {
        if (parent->windowHandle())
            return parent->windowHandle();
    }

    if (const QWindow *w = q->windowHandle()) {
        if (w->transientParent())
            return w->transientParent();
    }

    return nullptr;
}

//  from src/widgets/widgets/qmenu.cpp, line 930, as _ZN12QMenuPrivate21setOverrideMenuActionEP7QAction
inline void QMenuPrivate::setOverrideMenuAction(QAction *a)
{
    Q_Q(QMenu);
    QObject::disconnect(menuAction, SIGNAL(destroyed()), q, SLOT(_q_overrideMenuActionDestroyed()));
    if (a) {
        menuAction = a;
        QObject::connect(a, SIGNAL(destroyed()), q, SLOT(_q_overrideMenuActionDestroyed()));
    } else { //we revert back to the default action created by the QMenu itself
        menuAction = defaultMenuAction;
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 942, as _ZN12QMenuPrivate30_q_overrideMenuActionDestroyedEv
inline void QMenuPrivate::_q_overrideMenuActionDestroyed()
{
    menuAction=defaultMenuAction;
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

//  from src/widgets/widgets/qmenu.cpp, line 1550, as _ZN12QMenuPrivate16_q_actionHoveredEv
inline void QMenuPrivate::_q_actionHovered()
{
    Q_Q(QMenu);
    if (QAction * action = qobject_cast<QAction *>(q->sender())) {
        emit q->hovered(action);
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 1558, as _ZN12QMenuPrivate26_q_platformMenuAboutToShowEv
#if defined(Q_OS_LINUX)
inline void QMenuPrivate::_q_platformMenuAboutToShow()
{
    Q_Q(QMenu);

    emit q->aboutToShow();

#ifdef Q_OS_MACOS
    if (platformMenu) {
        const auto actions = q->actions();
        for (QAction *action : actions) {
            if (QWidget *widget = widgetItems.value(action))
                if (widget->parent() == q) {
                    QPlatformMenuItem *menuItem = platformMenu->menuItemForTag(reinterpret_cast<quintptr>(action));
                    moveWidgetToPlatformItem(widget, menuItem);
                    platformMenu->syncMenuItem(menuItem);
                }
        }
    }
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/widgets/widgets/qmenu.cpp, line 1579, as _ZNK12QMenuPrivate13hasMouseMovedERK7QPointF
inline bool QMenuPrivate::hasMouseMoved(const QPointF &globalPos) const
{
    //determines if the mouse has moved (ie its initial position has
    //changed by more than QApplication::startDragDistance()
    //or if there were at least 6 mouse motions)
    return motions > 6 ||
        QApplication::startDragDistance() < (mousePopupPos - globalPos).manhattanLength();
}

//  from src/widgets/widgets/qmenu.cpp, line 947, as _ZN12QMenuPrivate21updateLayoutDirectionEv
inline void QMenuPrivate::updateLayoutDirection()
{
    Q_Q(QMenu);
    //we need to mimic the cause of the popup's layout direction
    //to allow setting it on a mainwindow for example
    //we call setLayoutDirection_helper to not overwrite a user-defined value
    if (!q->testAttribute(Qt::WA_SetLayoutDirection)) {
        if (QWidget *w = causedPopup.widget)
            setLayoutDirection_helper(w->layoutDirection());
        else if (QWidget *w = q->parentWidget())
            setLayoutDirection_helper(w->layoutDirection());
        else
            setLayoutDirection_helper(QGuiApplication::layoutDirection());
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 963, as _ZN12QMenuPrivate12drawScrollerEP8QPainterNS_19ScrollerTearOffItem4TypeERK5QRect
inline void QMenuPrivate::drawScroller(QPainter *painter, QMenuPrivate::ScrollerTearOffItem::Type type, const QRect &rect)
{
    if (!painter || rect.isEmpty())
        return;

    if (!scroll || !(scroll->scrollFlags & (QMenuPrivate::QMenuScroller::ScrollUp
                                         | QMenuPrivate::QMenuScroller::ScrollDown)))
        return;

    Q_Q(QMenu);
    QStyleOptionMenuItem menuOpt;
    menuOpt.initFrom(q);
    menuOpt.state = QStyle::State_None;
    menuOpt.checkType = QStyleOptionMenuItem::NotCheckable;
    menuOpt.maxIconWidth = 0;
    menuOpt.reservedShortcutWidth = 0;
    menuOpt.rect = rect;
    menuOpt.menuItemType = QStyleOptionMenuItem::Scroller;
    menuOpt.state |= QStyle::State_Enabled;
    if (type == QMenuPrivate::ScrollerTearOffItem::ScrollDown)
        menuOpt.state |= QStyle::State_DownArrow;

    painter->setClipRect(menuOpt.rect);
    q->style()->drawControl(QStyle::CE_MenuScroller, &menuOpt, painter, q);
}

//  from src/widgets/widgets/qmenu.cpp, line 989, as _ZN12QMenuPrivate11drawTearOffEP8QPainterRK5QRect
inline void QMenuPrivate::drawTearOff(QPainter *painter, const QRect &rect)
{
    if (!painter || rect.isEmpty())
        return;

    if (!tearoff)
        return;

    Q_Q(QMenu);
    QStyleOptionMenuItem menuOpt;
    menuOpt.initFrom(q);
    menuOpt.state = QStyle::State_None;
    menuOpt.checkType = QStyleOptionMenuItem::NotCheckable;
    menuOpt.maxIconWidth = 0;
    menuOpt.reservedShortcutWidth = 0;
    menuOpt.rect = rect;
    menuOpt.menuItemType = QStyleOptionMenuItem::TearOff;
    if (tearoffHighlighted)
        menuOpt.state |= QStyle::State_Selected;

    painter->setClipRect(menuOpt.rect);
    q->style()->drawControl(QStyle::CE_MenuTearoff, &menuOpt, painter, q);
}

//  from src/widgets/widgets/qmenu.cpp, line 1013, as _ZNK12QMenuPrivate4rectEv
inline QRect QMenuPrivate::rect() const
{
    Q_Q(const QMenu);
    QStyle *style = q->style();
    QStyleOption opt(0);
    opt.initFrom(q);
    const int hmargin = style->pixelMetric(QStyle::PM_MenuHMargin, &opt, q);
    const int vmargin = style->pixelMetric(QStyle::PM_MenuVMargin, &opt, q);
    const int fw = style->pixelMetric(QStyle::PM_MenuPanelWidth, &opt, q);
    return (q->rect().adjusted(hmargin + fw + leftmargin, vmargin + fw + topmargin,
                               -(hmargin + fw + rightmargin), -(vmargin + fw + bottommargin)));
}
//  -----------------------------------------------------------------------

//  A QMenuPrivate that Python can take functions over in. Every QMenuPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMenuPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQMenuPrivateCall1)(const void *, int, int *);
typedef void (*CuteQMenuPrivateCall2)(const void *, int *);
typedef void (*CuteQMenuPrivateCall3)(const void *, int *);
typedef void * (*CuteQMenuPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQMenuPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQMenuPrivateCall6)(const void *, int *);
typedef int (*CuteQMenuPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQMenuPrivateCall8)(const void *, int *);
typedef void (*CuteQMenuPrivateCall9)(const void *, int *);
typedef void (*CuteQMenuPrivateCall10)(const void *, int *);
typedef void (*CuteQMenuPrivateCall11)(const void *, int *);
typedef void (*CuteQMenuPrivateCall12)(const void *, int *);
typedef void (*CuteQMenuPrivateCall13)(const void *, int *);
typedef void (*CuteQMenuPrivateCall14)(const void *, int *);
typedef void (*CuteQMenuPrivateCall15)(const void *, int *);
typedef bool (*CuteQMenuPrivateCall16)(const void *, int *);
typedef bool (*CuteQMenuPrivateCall17)(const void *, int *);
class CuteQMenuPrivate : public QMenuPrivate {
public:
  using QMenuPrivate::QMenuPrivate;
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
      CuteQMenuPrivateCall0 call = reinterpret_cast<CuteQMenuPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMenuPrivateCall1 call = reinterpret_cast<CuteQMenuPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQMenuPrivateCall2 call = reinterpret_cast<CuteQMenuPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMenuPrivateCall3 call = reinterpret_cast<CuteQMenuPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQMenuPrivateCall4 call = reinterpret_cast<CuteQMenuPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQMenuPrivateCall5 call = reinterpret_cast<CuteQMenuPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQMenuPrivateCall6 call = reinterpret_cast<CuteQMenuPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMenuPrivateCall7 call = reinterpret_cast<CuteQMenuPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQMenuPrivateCall8 call = reinterpret_cast<CuteQMenuPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQMenuPrivateCall9 call = reinterpret_cast<CuteQMenuPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQMenuPrivateCall10 call = reinterpret_cast<CuteQMenuPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQMenuPrivateCall11 call = reinterpret_cast<CuteQMenuPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQMenuPrivateCall12 call = reinterpret_cast<CuteQMenuPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQMenuPrivateCall13 call = reinterpret_cast<CuteQMenuPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQMenuPrivateCall14 call = reinterpret_cast<CuteQMenuPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQMenuPrivateCall15 call = reinterpret_cast<CuteQMenuPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQMenuPrivateCall16 call = reinterpret_cast<CuteQMenuPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQMenuPrivateCall17 call = reinterpret_cast<CuteQMenuPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QMenu *QMenuPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN12QMenuPrivate6q_funcEv(QMenuPrivate *self) {
  return self->q_func();
}

//  const QMenu *QMenuPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMenu *ritual_ZNK12QMenuPrivate6q_funcEv(const QMenuPrivate *self) {
  return self->q_func();
}

//  QMenuPrivate::~QMenuPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivateD1Ev(QMenuPrivate *self) {
  delete self;
}

//  void QMenuPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate4initEv(QMenuPrivate *self) {
  self->init();
}

//  QPlatformMenu *QMenuPrivate::createPlatformMenu()
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZN12QMenuPrivate18createPlatformMenuEv(
    QMenuPrivate *self) {
  return self->createPlatformMenu();
}

//  void QMenuPrivate::setPlatformMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate15setPlatformMenuEP13QPlatformMenu(
    QMenuPrivate *self,
    QPlatformMenu *menu) {
  self->setPlatformMenu(menu);
}

//  void QMenuPrivate::syncPlatformMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate16syncPlatformMenuEv(QMenuPrivate *self) {
  self->syncPlatformMenu();
}

//  void QMenuPrivate::copyActionToPlatformItem(const QAction *action,
//      QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate24copyActionToPlatformItemEPK7QActionP17QPlatformMenuItem(
    QMenuPrivate *self,
    const QAction *action,
    QPlatformMenuItem *item) {
  self->copyActionToPlatformItem(action, item);
}

//  QPlatformMenuItem *QMenuPrivate::insertActionInPlatformMenu(const QAction
//      *action, QPlatformMenuItem *beforeItem)
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZN12QMenuPrivate26insertActionInPlatformMenuEPK7QActionP17QPlatformMenuItem(
    QMenuPrivate *self,
    const QAction *action,
    QPlatformMenuItem *beforeItem) {
  return self->insertActionInPlatformMenu(action, beforeItem);
}

//  QMenuPrivate *QMenuPrivate::get(QMenu *m)
extern "C" Q_DECL_EXPORT
QMenuPrivate *ritual_ZN12QMenuPrivate3getEP5QMenu(QMenu *m) {
  return QMenuPrivate::get(m);
}

//  int QMenuPrivate::scrollerHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMenuPrivate14scrollerHeightEv(const QMenuPrivate *self) {
  return self->scrollerHeight();
}

//  bool QMenuPrivate::isContextMenu() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMenuPrivate13isContextMenuEv(const QMenuPrivate *self) {
  return self->isContextMenu();
}

//  QRect QMenuPrivate::actionRect(QAction *a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QMenuPrivate10actionRectEP7QAction(
    const QMenuPrivate *self,
    QAction *a0) {
  return new QRect(self->actionRect(a0));
}

//  void QMenuPrivate::updateActionRects() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QMenuPrivate17updateActionRectsEv(
    const QMenuPrivate *self) {
  self->updateActionRects();
}

//  void QMenuPrivate::updateActionRects(const QRect &screen) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QMenuPrivate17updateActionRectsERK5QRect(
    const QMenuPrivate *self,
    const QRect *screen) {
  self->updateActionRects(*screen);
}

//  QRect QMenuPrivate::popupGeometry(QScreen *screen) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QMenuPrivate13popupGeometryEP7QScreen(
    const QMenuPrivate *self,
    QScreen *screen) {
  return new QRect(self->popupGeometry(screen));
}

//  bool QMenuPrivate::useFullScreenForPopup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMenuPrivate21useFullScreenForPopupEv(
    const QMenuPrivate *self) {
  return self->useFullScreenForPopup();
}

//  int QMenuPrivate::getLastVisibleAction() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMenuPrivate20getLastVisibleActionEv(
    const QMenuPrivate *self) {
  return self->getLastVisibleAction();
}

#if QT_CONFIG(menu)
//  void QMenuPrivate::popup(const QPoint &p, QAction *atAction,
//      PositionFunction positionFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate5popupERK6QPointP7QActionSt8functionIFS0_RK5QSizeEE(
    QMenuPrivate *self,
    const QPoint *p,
    QAction *atAction,
    const QMenuPrivate::PositionFunction *positionFunction) {
  self->popup(*p, atAction, *positionFunction);
}
#endif  // QT_CONFIG(menu)

#if QT_CONFIG(menu)
//  QAction *QMenuPrivate::exec(const QPoint &p, QAction *action,
//      PositionFunction positionFunction)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QMenuPrivate4execERK6QPointP7QActionSt8functionIFS0_RK5QSizeEE(
    QMenuPrivate *self,
    const QPoint *p,
    QAction *action,
    const QMenuPrivate::PositionFunction *positionFunction) {
  return self->exec(*p, action, *positionFunction);
}
#endif  // QT_CONFIG(menu)

//  QWidget *QMenuPrivate::topCausedWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK12QMenuPrivate15topCausedWidgetEv(
    const QMenuPrivate *self) {
  return self->topCausedWidget();
}

//  QAction *QMenuPrivate::actionAt(QPoint p) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QMenuPrivate8actionAtE6QPoint(
    const QMenuPrivate *self,
    const QPoint *p) {
  return self->actionAt(*p);
}

//  void QMenuPrivate::setSyncAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate13setSyncActionEv(QMenuPrivate *self) {
  self->setSyncAction();
}

//  QList<QPointer<QWidget>> QMenuPrivate::calcCausedStack() const
extern "C" Q_DECL_EXPORT
QList<QPointer<QWidget>> *ritual_ZNK12QMenuPrivate15calcCausedStackEv(
    const QMenuPrivate *self) {
  return new QList<QPointer<QWidget>>(self->calcCausedStack());
}

//  void QMenuPrivate::hideMenu(QMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate8hideMenuEP5QMenu(
    QMenuPrivate *self,
    QMenu *menu) {
  self->hideMenu(menu);
}

//  QWindow *QMenuPrivate::transientParentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK12QMenuPrivate21transientParentWindowEv(
    const QMenuPrivate *self) {
  return self->transientParentWindow();
}

//  QAction *QMenuPrivate::actionAt(int i) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QMenuPrivate8actionAtEi(
    const QMenuPrivate *self,
    int i) {
  return self->actionAt(i);
}

//  int QMenuPrivate::indexOf(QAction *act) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QMenuPrivate7indexOfEP7QAction(
    const QMenuPrivate *self,
    QAction *act) {
  return self->indexOf(act);
}

//  void QMenuPrivate::setOverrideMenuAction(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate21setOverrideMenuActionEP7QAction(
    QMenuPrivate *self,
    QAction *a0) {
  self->setOverrideMenuAction(a0);
}

//  void QMenuPrivate::_q_overrideMenuActionDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate30_q_overrideMenuActionDestroyedEv(
    QMenuPrivate *self) {
  self->_q_overrideMenuActionDestroyed();
}

//  void QMenuPrivate::activateCausedStack(const QList<QPointer<QWidget>>
//      &a0, QAction *a1, QAction::ActionEvent a2, bool a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate19activateCausedStackERK5QListI8QPointerI7QWidgetEEP7QActionNS7_11ActionEventEb(
    QMenuPrivate *self,
    const QList<QPointer<QWidget>> *a0,
    QAction *a1,
    QAction::ActionEvent a2,
    bool a3) {
  self->activateCausedStack(*a0, a1, a2, a3);
}

//  void QMenuPrivate::_q_actionHovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate16_q_actionHoveredEv(QMenuPrivate *self) {
  self->_q_actionHovered();
}

#if defined(Q_OS_LINUX)
//  void QMenuPrivate::_q_platformMenuAboutToShow()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate26_q_platformMenuAboutToShowEv(
    QMenuPrivate *self) {
  self->_q_platformMenuAboutToShow();
}
#endif  // defined(Q_OS_LINUX)

//  bool QMenuPrivate::hasMouseMoved(const QPointF &globalPos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMenuPrivate13hasMouseMovedERK7QPointF(
    const QMenuPrivate *self,
    const QPointF *globalPos) {
  return self->hasMouseMoved(*globalPos);
}

//  void QMenuPrivate::updateLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate21updateLayoutDirectionEv(QMenuPrivate *self) {
  self->updateLayoutDirection();
}

//  void QMenuPrivate::drawScroller(QPainter *painter,
//      ScrollerTearOffItem::Type type, const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate12drawScrollerEP8QPainterNS_19ScrollerTearOffItem4TypeERK5QRect(
    QMenuPrivate *self,
    QPainter *painter,
    QMenuPrivate::ScrollerTearOffItem::Type type,
    const QRect *rect) {
  self->drawScroller(painter, type, *rect);
}

//  void QMenuPrivate::drawTearOff(QPainter *painter, const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate11drawTearOffEP8QPainterRK5QRect(
    QMenuPrivate *self,
    QPainter *painter,
    const QRect *rect) {
  self->drawTearOff(painter, *rect);
}

//  QRect QMenuPrivate::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QMenuPrivate4rectEv(const QMenuPrivate *self) {
  return new QRect(self->rect());
}

//  bool QMenuPrivate::considerAction(const QAction *action) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QMenuPrivate14considerActionEPK7QAction(
    const QMenuPrivate *self,
    const QAction *action) {
  return self->considerAction(action);
}

//  a Python function taken by a CuteQMenuPrivate, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMenuPrivate(
    QMenuPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMenuPrivate *>(self)->take(key, call);
}

//  a QList<QPointer<QWidget>> a ritual of QMenuPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMenuPrivate__QList_QPointer_QWidget(
    QList<QPointer<QWidget>> *self) {
  delete self;
}

#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(menu)
