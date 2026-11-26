//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qgraphstheme_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qgraphstheme.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphstheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/qgraphstheme.h>
#include <QtGraphs/private/commonutils_p.h>
#include <QtGui/QGuiApplication>
#include <QtGui/QLinearGradient>
#include <QtQml/QQmlListProperty>
#include <QtGui/QStyleHints>
#include <QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/private/qgraphstheme_p.h>
#include <QtGraphs/private/qquickgraphscolor_p.h>
#include <QtQuick/private/qquickrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/common/theme/qgraphstheme.cpp, line 2253, as _ZN19QGraphsThemePrivateD1Ev
inline QGraphsThemePrivate::~QGraphsThemePrivate() {}

//  from ../qtgraphs/src/common/theme/qgraphstheme.cpp, line 2251, as _ZN19QGraphsThemePrivateC1Ev
inline QGraphsThemePrivate::QGraphsThemePrivate() {}
//  -----------------------------------------------------------------------

//  QGraphsThemePrivate::QGraphsThemePrivate()
extern "C" Q_DECL_EXPORT
QGraphsThemePrivate *ritual_ZN19QGraphsThemePrivateC1Ev() {
  return new QGraphsThemePrivate();
}

//  QGraphsThemePrivate::~QGraphsThemePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphsThemePrivateD1Ev(QGraphsThemePrivate *self) {
  delete self;
}

//  QGraphsTheme *QGraphsThemePrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZN19QGraphsThemePrivate6q_funcEv(
    QGraphsThemePrivate *self) {
  return self->q_func();
}

//  const QGraphsTheme *QGraphsThemePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphsTheme *ritual_ZNK19QGraphsThemePrivate6q_funcEv(
    const QGraphsThemePrivate *self) {
  return self->q_func();
}
