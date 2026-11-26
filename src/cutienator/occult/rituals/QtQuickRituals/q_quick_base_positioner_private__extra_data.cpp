//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickpositioners_p.h>
#include <QtQuick/private/qquickpositioners_p_p.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qcoreapplication.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 633, as _ZN27QQuickBasePositionerPrivate9ExtraDataC1Ev
inline QQuickBasePositionerPrivate::ExtraData::ExtraData()
    : padding(0)
    , topPadding(0)
    , leftPadding(0)
    , rightPadding(0)
    , bottomPadding(0)
    , explicitTopPadding(false)
    , explicitLeftPadding(false)
    , explicitRightPadding(false)
    , explicitBottomPadding(false)
{
}
//  -----------------------------------------------------------------------

//  QQuickBasePositionerPrivate::ExtraData::ExtraData()
extern "C" Q_DECL_EXPORT
QQuickBasePositionerPrivate::ExtraData *ritual_ZN27QQuickBasePositionerPrivate9ExtraDataC1Ev() {
  return new QQuickBasePositionerPrivate::ExtraData();
}

//  QQuickBasePositionerPrivate::ExtraData::~ExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate9ExtraDataD1Ev(
    QQuickBasePositionerPrivate::ExtraData *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_positioners)
#endif  // QT_CONFIG(quick_positioners)
