//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qtools_p.h>
#include <qdebug.h>
#include <qscopedvaluerollback.h>
#include "qtextdocument_p.h"
#include "qtextdocument.h"
#include <qtextformat.h>
#include "qtextformat_p.h"
#include "qtextobject_p.h"
#include "qtextcursor.h"
#include "qtextimagehandler_p.h"
#include "qtextcursor_p.h"
#include "qtextdocumentlayout_p.h"
#include "qtexttable.h"
#include "qtextengine_p.h"
#include <QtCore/q20utility.h>
#include <stdlib.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextdocument_p.cpp, line 88, as _ZNK14QTextBlockData10invalidateEv
inline void QTextBlockData::invalidate() const
{
    if (layout)
        layout->engine()->invalidate();
}
//  -----------------------------------------------------------------------

//  void QTextBlockData::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextBlockData10initializeEv(QTextBlockData *self) {
  self->initialize();
}

//  void QTextBlockData::invalidate() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QTextBlockData10invalidateEv(const QTextBlockData *self) {
  self->invalidate();
}

//  void QTextBlockData::free()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextBlockData4freeEv(QTextBlockData *self) {
  self->free();
}

//  QTextBlockData::~QTextBlockData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextBlockDataD1Ev(QTextBlockData *self) {
  delete self;
}
