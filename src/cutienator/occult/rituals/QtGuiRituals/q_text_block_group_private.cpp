//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qtextobject.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qtextobject.h"
#include "qtextobject_p.h"
#include "qtextcursor_p.h"
#include "qtextdocument.h"
#include "qtextformat_p.h"
#include "qtextdocument_p.h"
#include "qtextcursor.h"
#include "qtextlist.h"
#include "qabstracttextdocumentlayout.h"
#include "qtextengine_p.h"
#include "qdebug.h"
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextobject.cpp, line 166, as _ZN22QTextBlockGroupPrivate15markBlocksDirtyEv
inline void QTextBlockGroupPrivate::markBlocksDirty()
{
    for (int i = 0; i < blocks.size(); ++i) {
        const QTextBlock &block = blocks.at(i);
        pieceTable->documentChange(block.position(), block.length());
    }
}
//  -----------------------------------------------------------------------

//  QTextBlockGroup *QTextBlockGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextBlockGroup *ritual_ZN22QTextBlockGroupPrivate6q_funcEv(
    QTextBlockGroupPrivate *self) {
  return self->q_func();
}

//  const QTextBlockGroup *QTextBlockGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextBlockGroup *ritual_ZNK22QTextBlockGroupPrivate6q_funcEv(
    const QTextBlockGroupPrivate *self) {
  return self->q_func();
}

//  QTextBlockGroupPrivate::QTextBlockGroupPrivate(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextBlockGroupPrivate *ritual_ZN22QTextBlockGroupPrivateC1EP13QTextDocument(
    QTextDocument *doc) {
  return new QTextBlockGroupPrivate(doc);
}

//  void QTextBlockGroupPrivate::markBlocksDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTextBlockGroupPrivate15markBlocksDirtyEv(
    QTextBlockGroupPrivate *self) {
  self->markBlocksDirty();
}
