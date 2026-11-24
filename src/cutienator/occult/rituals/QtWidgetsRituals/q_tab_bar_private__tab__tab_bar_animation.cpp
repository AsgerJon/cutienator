//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tabbar)
#if QT_CONFIG(animation)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "private/qlayoutengine_p.h"
#if QT_CONFIG(itemviews)
#include "qabstractitemdelegate.h"
#endif
#include "qapplication.h"
#include "qevent.h"
#include "qpainter.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qstylepainter.h"
#if QT_CONFIG(tabwidget)
#include "qtabwidget.h"
#endif
#if QT_CONFIG(tooltip)
#include "qtooltip.h"
#endif
#if QT_CONFIG(whatsthis)
#include "qwhatsthis.h"
#endif
#include "private/qtextengine_p.h"
#if QT_CONFIG(accessibility)
#include "qaccessible.h"
#endif
#ifdef Q_OS_MACOS
#include <qpa/qplatformnativeinterface.h>
#endif
#include "qmainwindow.h"
#include "private/qmainwindowlayout_p.h"
#include "qdebug.h"
#include "private/qapplication_p.h"
#include "private/qtabbar_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qtabbar.cpp, line 2979, as _ZN14QTabBarPrivate3Tab15TabBarAnimation18updateCurrentValueERK8QVariant
#if QT_CONFIG(animation)
inline void QTabBarPrivate::Tab::TabBarAnimation::updateCurrentValue(const QVariant &current)
{
    priv->moveTab(priv->tabList.indexOf(tab), current.toInt());
}
#endif  // QT_CONFIG(animation)

//  from src/widgets/widgets/qtabbar.cpp, line 2984, as _ZN14QTabBarPrivate3Tab15TabBarAnimation11updateStateEN18QAbstractAnimation5StateES3_
#if QT_CONFIG(animation)
inline void QTabBarPrivate::Tab::TabBarAnimation::updateState(QAbstractAnimation::State newState, QAbstractAnimation::State)
{
    if (newState == Stopped) priv->moveTabFinished(priv->tabList.indexOf(tab));
}
#endif  // QT_CONFIG(animation)
//  -----------------------------------------------------------------------

#if QT_CONFIG(animation)
//  QTabBarPrivate::Tab::TabBarAnimation::TabBarAnimation(Tab *t,
//      QTabBarPrivate *_priv)
extern "C" Q_DECL_EXPORT
QTabBarPrivate::Tab::TabBarAnimation *ritual_ZN14QTabBarPrivate3Tab15TabBarAnimationC1EPS0_PS_(
    QTabBarPrivate::Tab *t,
    QTabBarPrivate *_priv) {
  return new QTabBarPrivate::Tab::TabBarAnimation(t, _priv);
}
#endif  // QT_CONFIG(animation)

//  void QTabBarPrivate::Tab::TabBarAnimation::updateCurrentValue(const
//      QVariant &current)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate3Tab15TabBarAnimation18updateCurrentValueERK8QVariant(
    QTabBarPrivate::Tab::TabBarAnimation *self,
    const QVariant *current) {
  self->updateCurrentValue(*current);
}

//  void QTabBarPrivate::Tab::TabBarAnimation::updateState(State newState,
//      State a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate3Tab15TabBarAnimation11updateStateEN18QAbstractAnimation5StateES3_(
    QTabBarPrivate::Tab::TabBarAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State a1) {
  self->updateState(newState, a1);
}

#if QT_CONFIG(animation)
//  void QTabBarPrivate::Tab::TabBarAnimation::updateCurrentValue(const
//      QVariant &current)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QTabBarPrivate3Tab15TabBarAnimation18updateCurrentValueERK8QVariant(
    QTabBarPrivate::Tab::TabBarAnimation *self,
    const QVariant *current) {
  self->QTabBarPrivate::Tab::TabBarAnimation::updateCurrentValue(*current);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QTabBarPrivate::Tab::TabBarAnimation::updateState(State newState,
//      State a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QTabBarPrivate3Tab15TabBarAnimation11updateStateEN18QAbstractAnimation5StateES3_(
    QTabBarPrivate::Tab::TabBarAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State a1) {
  self->QTabBarPrivate::Tab::TabBarAnimation::updateState(newState, a1);
}
#endif  // QT_CONFIG(animation)

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(tabbar)
