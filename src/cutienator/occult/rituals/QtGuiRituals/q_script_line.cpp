//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qflatmap_p.h>
#include <QtGui/private/qtguiglobal_p.h>
#include "qdebug.h"
#include "qtextformat.h"
#include "qtextformat_p.h"
#include "qtextengine_p.h"
#include "qabstracttextdocumentlayout.h"
#include "qabstracttextdocumentlayout_p.h"
#include "qtextlayout.h"
#include "qtextboundaryfinder.h"
#include <QtCore/private/qunicodetables_p.h>
#include "qvarlengtharray.h"
#include "qfont.h"
#include "qfont_p.h"
#include "qfontengine_p.h"
#include "qstring.h"
#include "qtextdocument_p.h"
#include "qrawfont.h"
#include "qrawfont_p.h"
#include <qguiapplication.h>
#include <qinputmethod.h>
#include <qlocale.h>
#include <algorithm>
#include <stdlib.h>
#if QT_CONFIG(harfbuzz)
#include "qharfbuzzng_p.h"
#endif
#if !defined(QT_NO_EMOJISEGMENTER)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextengine.cpp, line 2833, as _ZN11QScriptLine16setDefaultHeightEP11QTextEngine
inline void QScriptLine::setDefaultHeight(QTextEngine *eng)
{
    QFont f;
    QFontEngine *e;

    if (QTextDocumentPrivate::get(eng->block) != nullptr && QTextDocumentPrivate::get(eng->block)->layout() != nullptr) {
        f = eng->block.charFormat().font();
        // Make sure we get the right dpi on printers
        QPaintDevice *pdev = QTextDocumentPrivate::get(eng->block)->layout()->paintDevice();
        if (pdev)
            f = QFont(f, pdev);
        e = f.d->engineForScript(QChar::Script_Common);
    } else {
        e = eng->fnt.d->engineForScript(QChar::Script_Common);
    }

    QFixed other_ascent = e->ascent();
    QFixed other_descent = e->descent();
    QFixed other_leading = e->leading();
    leading = qMax(leading + ascent, other_leading + other_ascent) - qMax(ascent, other_ascent);
    ascent = qMax(ascent, other_ascent);
    descent = qMax(descent, other_descent);
}
//  -----------------------------------------------------------------------

//  QScriptLine::QScriptLine()
extern "C" Q_DECL_EXPORT
QScriptLine *ritual_ZN11QScriptLineC1Ev() {
  return new QScriptLine();
}

//  QFixed QScriptLine::height() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QScriptLine6heightEv(const QScriptLine *self) {
  return new QFixed(self->height());
}

//  QFixed QScriptLine::base() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK11QScriptLine4baseEv(const QScriptLine *self) {
  return new QFixed(self->base());
}

//  void QScriptLine::setDefaultHeight(QTextEngine *eng)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScriptLine16setDefaultHeightEP11QTextEngine(
    QScriptLine *self,
    QTextEngine *eng) {
  self->setDefaultHeight(eng);
}

//  void QScriptLine::operator+=(const QScriptLine &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScriptLinepLERKS_(
    QScriptLine *self,
    const QScriptLine *other) {
  self->operator+=(*other);
}

//  QScriptLine::~QScriptLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QScriptLineD1Ev(QScriptLine *self) {
  delete self;
}
