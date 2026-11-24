//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfont.h"
#include "qdebug.h"
#include "qpaintdevice.h"
#include "qfontdatabase.h"
#include "qfontmetrics.h"
#include "qfontinfo.h"
#include "qpainter.h"
#include "qhash.h"
#include "qdatastream.h"
#include "qguiapplication.h"
#include "qstringlist.h"
#include "qscreen.h"
#include "qthread.h"
#include "qthreadstorage.h"
#include "qfont_p.h"
#include <private/qfontengine_p.h>
#include <private/qpainter_p.h>
#include <private/qtextengine_p.h>
#include <limits.h>
#include <qpa/qplatformscreen.h>
#include <qpa/qplatformintegration.h>
#include <qpa/qplatformfontdatabase.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/QMutexLocker>
#include <QtCore/QMutex>
#include <algorithm>
#include <array>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qfont.cpp, line 400, as _ZN15QFontEngineDataC1Ev
inline QFontEngineData::QFontEngineData()
    : ref(0), fontCacheId(QFontCache::instance()->id())
{
    memset(engines, 0, QFontDatabasePrivate::ScriptCount * sizeof(QFontEngine *));
}

//  from src/gui/text/qfont.cpp, line 406, as _ZN15QFontEngineDataD1Ev
inline QFontEngineData::~QFontEngineData()
{
    Q_ASSERT(ref.loadRelaxed() == 0);
    for (int i = 0; i < QFontDatabasePrivate::ScriptCount; ++i) {
        if (engines[i]) {
            if (!engines[i]->ref.deref())
                delete engines[i];
            engines[i] = nullptr;
        }
    }
}
//  -----------------------------------------------------------------------

//  QFontEngineData::QFontEngineData()
extern "C" Q_DECL_EXPORT
QFontEngineData *ritual_ZN15QFontEngineDataC1Ev() {
  return new QFontEngineData();
}

//  QFontEngineData::~QFontEngineData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QFontEngineDataD1Ev(QFontEngineData *self) {
  delete self;
}
