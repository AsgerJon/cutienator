//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qlayoutengine_p.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemdelegate.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#if QT_CONFIG(tabwidget)
#include <QtWidgets/qtabwidget.h>
#endif
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtGui/private/qtextengine_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qtabbar_p.h>
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

//  QTabBarPrivate::Tab::Tab(const QIcon &ico, const QString &txt)
extern "C" Q_DECL_EXPORT
QTabBarPrivate::Tab *ritual_ZN14QTabBarPrivate3TabC1ERK5QIconRK7QString(
    const QIcon *ico,
    const QString *txt) {
  return new QTabBarPrivate::Tab(*ico, *txt);
}

#if QT_CONFIG(animation)
//  void QTabBarPrivate::Tab::startAnimation(QTabBarPrivate *priv, int
//      duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate3Tab14startAnimationEPS_i(
    QTabBarPrivate::Tab *self,
    QTabBarPrivate *priv,
    int duration) {
  self->startAnimation(priv, duration);
}
#endif  // QT_CONFIG(animation)

#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(tabbar)
