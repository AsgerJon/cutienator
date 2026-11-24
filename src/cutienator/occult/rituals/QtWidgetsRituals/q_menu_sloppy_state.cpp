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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
