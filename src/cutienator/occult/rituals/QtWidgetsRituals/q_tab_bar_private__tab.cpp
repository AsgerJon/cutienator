//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
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

//  QTabBarPrivate::Tab::Tab(const QIcon &ico, const QString &txt)
extern "C" Q_DECL_EXPORT
QTabBarPrivate::Tab *ritual_ZN14QTabBarPrivate3TabC1ERK5QIconRK7QString(
    const QIcon *ico,
    const QString *txt) {
  return new QTabBarPrivate::Tab(*ico, *txt);
}

#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(tabbar)
