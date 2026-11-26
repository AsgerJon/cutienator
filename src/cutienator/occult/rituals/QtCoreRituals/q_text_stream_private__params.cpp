//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtextstream_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtextstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtextstream.h>
#include <QtCore/private/qtextstream_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qfile.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/private/qdebug_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qtools_p.h>
#include <locale.h>
#include <QtCore/private/qlocale_p.h>
#include <QtCore/private/qstringconverter_p.h>
#include <stdlib.h>
#include <limits.h>
#include <new>
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

//  from src/corelib/serialization/qtextstream.cpp, line 281, as _ZN18QTextStreamPrivate6Params5resetEv
inline void QTextStreamPrivate::Params::reset()
{
    realNumberPrecision = 6;
    integerBase = 0;
    fieldWidth = 0;
    padChar = u' ';
    fieldAlignment = QTextStream::AlignRight;
    realNumberNotation = QTextStream::SmartNotation;
    numberFlags = { };
}
//  -----------------------------------------------------------------------

//  void QTextStreamPrivate::Params::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate6Params5resetEv(
    QTextStreamPrivate::Params *self) {
  self->reset();
}

//  QTextStreamPrivate::Params::~Params()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextStreamPrivate6ParamsD1Ev(
    QTextStreamPrivate::Params *self) {
  delete self;
}
