//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtextstream_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtextstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qtextstream.h"
#include "private/qtextstream_p.h"
#include "qbuffer.h"
#include "qfile.h"
#include "qnumeric.h"
#include "qvarlengtharray.h"
#include <private/qdebug_p.h>
#include <private/qnumeric_p.h>
#include <private/qtools_p.h>
#include <locale.h>
#include "private/qlocale_p.h"
#include "private/qstringconverter_p.h"
#include <stdlib.h>
#include <limits.h>
#include <new>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
