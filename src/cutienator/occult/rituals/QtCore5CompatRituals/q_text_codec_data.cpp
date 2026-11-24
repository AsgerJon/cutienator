//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qtextcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qtextcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include "qtextcodec.h"
#include "qtextcodec_p.h"
#include "qbytearraymatcher.h"
#include "qendian.h"
#include "qfile.h"
#include "qlist.h"
#include <private/qlocking_p.h>
#include <QtCore/qloggingcategory.h>
#include "qstringlist.h"
#include "qvarlengtharray.h"
#include <private/qcoreapplication_p.h>
#include "qutfcodec_p.h"
#include "qlatincodec_p.h"
#if QT_CONFIG(codecs)
#  include "qtsciicodec_p.h"
#  include "qisciicodec_p.h"
#endif
#if QT_CONFIG(icu)
#include "qicucodec_p.h"
#else
#if QT_CONFIG(iconv)
#  include "qiconvcodec_p.h"
#endif
#ifdef Q_OS_WIN
#  include "qwindowscodec_p.h"
#endif
#  include "qsimplecodec_p.h"
#if QT_CONFIG(big_codecs) && QT_CONFIG(textcodec)
#  ifndef Q_OS_INTEGRITY
#    include "qgb18030codec_p.h"
#    include "qeucjpcodec_p.h"
#    include "qjiscodec_p.h"
#    include "qsjiscodec_p.h"
#    include "qeuckrcodec_p.h"
#    include "qbig5codec_p.h"
#  endif
#endif
#endif
#include <mutex>
#include <stdlib.h>
#include <ctype.h>
#include <locale.h>
#if defined (_XOPEN_UNIX) && !defined(Q_OS_QNX) && !defined(Q_OS_ANDROID)
# include <langinfo.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qtextcodec.cpp, line 85, as _ZN14QTextCodecDataC1Ev
inline QTextCodecData::QTextCodecData()
    : codecForLocale(nullptr)
{
}

//  from ../qt5compat/src/core5/codecs/qtextcodec.cpp, line 90, as _ZN14QTextCodecDataD1Ev
inline QTextCodecData::~QTextCodecData()
{
    codecForLocale.storeRelease(nullptr);
    QList<QTextCodec *> tmp = allCodecs;
    allCodecs.clear();
    codecCache.clear();
    for (QList<QTextCodec *>::const_iterator it = tmp.constBegin(); it != tmp.constEnd(); ++it)
        delete *it;
}
//  -----------------------------------------------------------------------

//  QTextCodecData::QTextCodecData()
extern "C" Q_DECL_EXPORT
QTextCodecData *ritual_ZN14QTextCodecDataC1Ev() {
  return new QTextCodecData();
}

//  QTextCodecData::~QTextCodecData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextCodecDataD1Ev(QTextCodecData *self) {
  delete self;
}

#endif  // QT_CONFIG(textcodec)
