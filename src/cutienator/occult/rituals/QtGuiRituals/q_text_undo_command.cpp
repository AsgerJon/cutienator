//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qtools_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextformat.h>
#include <QtGui/private/qtextformat_p.h>
#include <QtGui/private/qtextobject_p.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/private/qtextimagehandler_p.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/qtexttable.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtCore/q20utility.h>
#include <stdlib.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextdocument_p.cpp, line 108, as _ZN16QTextUndoCommand8tryMergeERKS_
inline bool QTextUndoCommand::tryMerge(const QTextUndoCommand &other)
{
    if (command != other.command)
        return false;

    if (command == Inserted
        && (pos + length == other.pos)
        && (strPos + length == other.strPos)
        && format == other.format) {

        length += other.length;
        return true;
    }

    // removal to the 'right' using 'Delete' key
    if (command == Removed
        && pos == other.pos
        && (strPos + length == other.strPos)
        && format == other.format) {

        length += other.length;
        return true;
    }

    // removal to the 'left' using 'Backspace'
    if (command == Removed
        && (other.pos + other.length == pos)
        && (other.strPos + other.length == strPos)
        && (format == other.format)) {

        int l = length;
        (*this) = other;

        length += l;
        return true;
    }

    return false;
}
//  -----------------------------------------------------------------------

//  bool QTextUndoCommand::tryMerge(const QTextUndoCommand &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QTextUndoCommand8tryMergeERKS_(
    QTextUndoCommand *self,
    const QTextUndoCommand *other) {
  return self->tryMerge(*other);
}

//  QTextUndoCommand::~QTextUndoCommand()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextUndoCommandD1Ev(QTextUndoCommand *self) {
  delete self;
}
