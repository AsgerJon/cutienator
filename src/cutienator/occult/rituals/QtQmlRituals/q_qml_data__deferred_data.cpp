//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldata_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmldata_p.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtQml/private/qqmlabstractbinding_p.h>
#include <QtQml/private/qqmlboundsignal_p.h>
#include <QtQml/private/qqmlcontextdata_p.h>
#include <QtQml/private/qqmlnotifier_p.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/private/qthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmldata.cpp, line 202, as _ZN8QQmlData12DeferredDataC1Ev
inline QQmlData::DeferredData::DeferredData() = default;

//  from ../qtdeclarative/src/qml/qml/qqmldata.cpp, line 203, as _ZN8QQmlData12DeferredDataD1Ev
inline QQmlData::DeferredData::~DeferredData() = default;
//  -----------------------------------------------------------------------

//  QQmlData::DeferredData::DeferredData()
extern "C" Q_DECL_EXPORT
QQmlData::DeferredData *ritual_ZN8QQmlData12DeferredDataC1Ev() {
  return new QQmlData::DeferredData();
}

//  QQmlData::DeferredData::~DeferredData()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlData12DeferredDataD1Ev(QQmlData::DeferredData *self) {
  delete self;
}
