//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qproxystyle_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if !defined(QT_NO_STYLE_PROXY)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qproxystyle.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qproxystyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qstyle.h>
#include <QtWidgets/private/qproxystyle_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/qproxystyle.h>
#include <QtWidgets/qstylefactory.h>
#include <QtWidgets/private/qstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/styles/qproxystyle.cpp, line 54, as _ZNK18QProxyStylePrivate15ensureBaseStyleEv
#if !defined(QT_NO_STYLE_PROXY) || defined(QT_PLUGIN)
inline void QProxyStylePrivate::ensureBaseStyle() const
{
    Q_Q(const QProxyStyle);

    if (baseStyle)
        return;

    if (!baseStyle && !QApplicationPrivate::styleOverride.isEmpty()) {
        baseStyle = QStyleFactory::create(QApplicationPrivate::styleOverride);
        if (baseStyle) {
            // If baseStyle is an instance of the same proxyStyle
            // we destroy it and fall back to the desktop style
            if (qstrcmp(baseStyle->metaObject()->className(),
                        q->metaObject()->className()) == 0) {
                delete baseStyle;
                baseStyle = nullptr;
            }
        }
    }

    if (!baseStyle) // Use application desktop style
        baseStyle = QStyleFactory::create(QApplicationPrivate::desktopStyleKey());

    if (!baseStyle) // Fallback to windows style
        baseStyle = QStyleFactory::create("windows"_L1);

    baseStyle->setProxy(const_cast<QProxyStyle*>(q));
    baseStyle->setParent(const_cast<QProxyStyle*>(q)); // Take ownership
}
#endif  // !defined(QT_NO_STYLE_PROXY) || defined(QT_PLUGIN)
//  -----------------------------------------------------------------------

//  QProxyStyle *QProxyStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QProxyStyle *ritual_ZN18QProxyStylePrivate6q_funcEv(
    QProxyStylePrivate *self) {
  return self->q_func();
}

//  const QProxyStyle *QProxyStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QProxyStyle *ritual_ZNK18QProxyStylePrivate6q_funcEv(
    const QProxyStylePrivate *self) {
  return self->q_func();
}

#if !defined(QT_NO_STYLE_PROXY) || defined(QT_PLUGIN)
//  void QProxyStylePrivate::ensureBaseStyle() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QProxyStylePrivate15ensureBaseStyleEv(
    const QProxyStylePrivate *self) {
  self->ensureBaseStyle();
}
#endif  // !defined(QT_NO_STYLE_PROXY) || defined(QT_PLUGIN)

//  QProxyStylePrivate::QProxyStylePrivate()
extern "C" Q_DECL_EXPORT
QProxyStylePrivate *ritual_ZN18QProxyStylePrivateC1Ev() {
  return new QProxyStylePrivate();
}

#endif  // !defined(QT_NO_STYLE_PROXY)
