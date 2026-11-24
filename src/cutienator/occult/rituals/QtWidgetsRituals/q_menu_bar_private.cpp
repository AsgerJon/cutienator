//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmenubar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(menubar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qmenubar.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmenubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmenu.h"
#include <QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/private/qwidgetwindow_p.h>
#include "qactiongroup.h"
#include "qdebug.h"
#include "qstyle.h"
#include "qevent.h"
#include "qtimer.h"
#include "qlayout.h"
#include "qstylepainter.h"
#include <qpa/qplatformtheme.h>
#include "qapplication.h"
#if QT_CONFIG(accessibility)
# include "qaccessible.h"
#endif
#if QT_CONFIG(effects)
# include <private/qeffects_p.h>
#endif
#if QT_CONFIG(whatsthis)
# include <qwhatsthis.h>
#endif
#include "qmenu_p.h"
#if QT_CONFIG(menubar)
#include "qmenubar_p.h"
#endif
#include "qwidgetaction.h"
#include "qpushbutton.h"
#if QT_CONFIG(tooltip)
#include "qtooltip.h"
#endif
#include <qwindow.h>
#include <private/qpushbutton_p.h>
#include <private/qaction_p.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme.h>
#include <qpa/qplatformwindow.h>
#include <qpa/qplatformwindow_p.h>
#include <private/qstyle_p.h>
#include "qstyle.h"
#include "qapplication.h"
#include "qpainter.h"
#include "qwidget.h"
#include "qbitmap.h"
#include "qpixmapcache.h"
#include "qset.h"
#include "qstyleoption.h"
#include "private/qstyle_p.h"
#include "private/qstylehelper_p.h"
#include "private/qguiapplication_p.h"
#include <qpa/qplatformtheme.h>
#ifndef QT_NO_DEBUG
#include "qdebug.h"
#endif
#include <QtCore/q20utility.h>
#include <limits.h>
#include <algorithm>
#include <qmenubar.h>
#include <qstyle.h>
#include <qlayout.h>
#include <qapplication.h>
#if QT_CONFIG(accessibility)
# include <qaccessible.h>
#endif
#include <qpainter.h>
#include <qstylepainter.h>
#include <qevent.h>
#if QT_CONFIG(mainwindow)
#include <qmainwindow.h>
#endif
#if QT_CONFIG(toolbutton)
#include <qtoolbutton.h>
#endif
#if QT_CONFIG(whatsthis)
#include <qwhatsthis.h>
#endif
#include <qpa/qplatformtheme.h>
#include "private/qguiapplication_p.h"
#include "qpa/qplatformintegration.h"
#include "qmenu_p.h"
#include "qmenubar_p.h"
#include <private/qscreen_p.h>
#include <private/qstyle_p.h>
#include "qdebug.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  void QMenuBarPrivate::calcActionRects(int max_width, int start) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QMenuBarPrivate15calcActionRectsEii(
    const QMenuBarPrivate *self,
    int max_width,
    int start) {
  self->calcActionRects(max_width, start);
}

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
