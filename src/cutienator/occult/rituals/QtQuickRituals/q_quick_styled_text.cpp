//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstyledtext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstyledtext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QStack>
#include <QtCore/QList>
#include <QtGui/QPainter>
#include <QtGui/QTextLayout>
#include <QtCore/QDebug>
#include <QtCore/qmath.h>
#include <QtQuick/private/qquickstyledtext_p.h>
#include <QtQml/QQmlContext>
#include <QtGui/private/qtexthtmlparser_p.h>
#include <QtGui/private/qoutlinemapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 158, as _ZN16QQuickStyledTextD1Ev
inline QQuickStyledText::~QQuickStyledText()
{
    delete d;
}
//  -----------------------------------------------------------------------

//  QQuickStyledText::~QQuickStyledText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStyledTextD1Ev(QQuickStyledText *self) {
  delete self;
}
