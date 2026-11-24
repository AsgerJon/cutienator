//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicktextinput_p.h"
#include "qquicktextinput_p_p.h"
#include "qquickwindow.h"
#include <private/qqmlglobal_p.h>
#include <private/qv4scopedvalue_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmimedata.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qevent.h>
#include <QTextBoundaryFinder>
#include "qsginternaltextnode_p.h"
#include <QtQuick/qsgsimplerectnode.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qinputmethod.h>
#include <QtCore/qmath.h>
#if QT_CONFIG(accessibility)
#include "qaccessible.h"
#include "qquickaccessibleattached_p.h"
#endif
#include <QtGui/private/qtextengine_p.h>
#include <QtGui/private/qinputcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextinput.cpp, line 2865, as _ZN22QQuickTextInputPrivate9ExtraDataC1Ev
inline QQuickTextInputPrivate::ExtraData::ExtraData()
    : padding(0)
    , topPadding(0)
    , leftPadding(0)
    , rightPadding(0)
    , bottomPadding(0)
    , explicitTopPadding(false)
    , explicitLeftPadding(false)
    , explicitRightPadding(false)
    , explicitBottomPadding(false)
    , implicitResize(true)
{
}
//  -----------------------------------------------------------------------

//  QQuickTextInputPrivate::ExtraData::ExtraData()
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate::ExtraData *ritual_ZN22QQuickTextInputPrivate9ExtraDataC1Ev() {
  return new QQuickTextInputPrivate::ExtraData();
}

//  QQuickTextInputPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate9ExtraDataD1Ev(
    QQuickTextInputPrivate::ExtraData *self) {
  delete self;
}
