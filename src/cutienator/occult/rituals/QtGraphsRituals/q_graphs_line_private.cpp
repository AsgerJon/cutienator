//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qgraphstheme_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
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

//  from ../qtgraphs/src/common/theme/qgraphstheme.cpp, line 2244, as _ZN18QGraphsLinePrivate15resetCustomBitsEv
inline void QGraphsLinePrivate::resetCustomBits()
{
    m_bits.mainColorCustom = false;
    m_bits.subColorCustom = false;
    m_bits.labelTextColorCustom = false;
}
//  -----------------------------------------------------------------------

//  void QGraphsLinePrivate::resetCustomBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphsLinePrivate15resetCustomBitsEv(
    QGraphsLinePrivate *self) {
  self->resetCustomBits();
}
