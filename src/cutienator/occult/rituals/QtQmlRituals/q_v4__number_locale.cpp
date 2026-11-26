//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4numberobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4numberobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4numberobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qmath.h>
#include <QtCore/QDebug>
#include <cassert>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 28, as _ZN3QV412NumberLocaleC1Ev
namespace QV4 {
inline NumberLocale::NumberLocale() : QLocale(QLocale::C),
    // -128 means shortest string that can accurately represent the number.
    defaultDoublePrecision(0xffffff80)
{
    setNumberOptions(QLocale::OmitGroupSeparator |
                     QLocale::OmitLeadingZeroInExponent |
                     QLocale::IncludeTrailingZeroesAfterDot);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::NumberLocale::NumberLocale()
extern "C" Q_DECL_EXPORT
QV4::NumberLocale *ritual_ZN3QV412NumberLocaleC1Ev() {
  return new QV4::NumberLocale();
}

//  QV4::NumberLocale::~NumberLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412NumberLocaleD1Ev(QV4::NumberLocale *self) {
  delete self;
}
