//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(menu)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/widgets/qmenu.cpp, line 279, as _ZNK12QMenuPrivate14scrollerHeightEv
inline int QMenuPrivate::scrollerHeight() const
{
    Q_Q(const QMenu);
    return q->style()->pixelMetric(QStyle::PM_MenuScrollerHeight, nullptr, q);
}

//  from src/widgets/widgets/qmenu.cpp, line 1026, as _ZN12QMenuPrivate19ScrollerTearOffItemC1ENS0_4TypeEPS_P7QWidget6QFlagsIN2Qt10WindowTypeEE
inline QMenuPrivate::ScrollerTearOffItem::ScrollerTearOffItem(QMenuPrivate::ScrollerTearOffItem::Type type, QMenuPrivate *mPrivate, QWidget *parent, Qt::WindowFlags f)
    : QWidget(parent, f), menuPrivate(mPrivate), scrollType(type)
{
    if (parent)
        setMouseTracking(parent->style()->styleHint(QStyle::SH_Menu_MouseTracking, nullptr, parent));
}

//  from src/widgets/widgets/qmenu.cpp, line 1033, as _ZN12QMenuPrivate19ScrollerTearOffItem10paintEventEP11QPaintEvent
inline void QMenuPrivate::ScrollerTearOffItem::paintEvent(QPaintEvent *e)
{
    if (!e->rect().intersects(rect()))
        return;

    QPainter p(this);
    QWidget *parent = parentWidget();

    //paint scroll up / down arrows
    menuPrivate->drawScroller(&p, scrollType, QRect(0, 0, width(), menuPrivate->scrollerHeight()));
    //paint the tear off
    if (scrollType == QMenuPrivate::ScrollerTearOffItem::ScrollUp) {
        QRect rect(0, 0, width(), parent->style()->pixelMetric(QStyle::PM_MenuTearoffHeight, nullptr, parent));
        if (menuPrivate->scroll && menuPrivate->scroll->scrollFlags & QMenuPrivate::QMenuScroller::ScrollUp)
            rect.translate(0, menuPrivate->scrollerHeight());
        menuPrivate->drawTearOff(&p, rect);
    }
}

//  from src/widgets/widgets/qmenu.cpp, line 1052, as _ZN12QMenuPrivate19ScrollerTearOffItem19updateScrollerRectsERK5QRect
inline void QMenuPrivate::ScrollerTearOffItem::updateScrollerRects(const QRect &rect)
{
    if (rect.isEmpty())
        setVisible(false);
    else {
        setGeometry(rect);
        raise();
        setVisible(true);
    }
}
//  -----------------------------------------------------------------------

//  QMenuPrivate::ScrollerTearOffItem::ScrollerTearOffItem(Type type,
//      QMenuPrivate *mPrivate, QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QMenuPrivate::ScrollerTearOffItem *ritual_ZN12QMenuPrivate19ScrollerTearOffItemC1ENS0_4TypeEPS_P7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QMenuPrivate::ScrollerTearOffItem::Type type,
    QMenuPrivate *mPrivate,
    QWidget *parent,
    int f) {
  return new QMenuPrivate::ScrollerTearOffItem(
      type,
      mPrivate,
      parent,
      QFlags<Qt::WindowType>::fromInt(f));
}

//  void QMenuPrivate::ScrollerTearOffItem::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate19ScrollerTearOffItem10paintEventEP11QPaintEvent(
    QMenuPrivate::ScrollerTearOffItem *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QMenuPrivate::ScrollerTearOffItem::updateScrollerRects(const QRect
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QMenuPrivate19ScrollerTearOffItem19updateScrollerRectsERK5QRect(
    QMenuPrivate::ScrollerTearOffItem *self,
    const QRect *rect) {
  self->updateScrollerRects(*rect);
}

//  void QMenuPrivate::ScrollerTearOffItem::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QMenuPrivate19ScrollerTearOffItem10paintEventEP11QPaintEvent(
    QMenuPrivate::ScrollerTearOffItem *self,
    QPaintEvent *e) {
  self->QMenuPrivate::ScrollerTearOffItem::paintEvent(e);
}

#endif  // QT_CONFIG(menu)
