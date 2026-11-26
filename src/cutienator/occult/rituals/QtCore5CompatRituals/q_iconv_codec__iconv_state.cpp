//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(iconv) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
#if QT_CONFIG(iconv)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qiconvcodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qglobal_p.h>
#include <QtCore5Compat/private/qiconvcodec_p.h>
#include <QtCore5Compat/private/qtextcodec_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qthreadstorage.h>
#include <errno.h>
#include <locale.h>
#include <stdio.h>
#include <dlfcn.h>
#include <unistd.h>
#if defined(_XOPEN_UNIX) && !defined(Q_OS_QNX)
#  include <langinfo.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 63, as _ZN11QIconvCodec10IconvStateC1EPv
inline QIconvCodec::IconvState::IconvState(iconv_t x)
    : buffer(array), bufferLen(sizeof array), cd(x)
{
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 68, as _ZN11QIconvCodec10IconvStateD1Ev
inline QIconvCodec::IconvState::~IconvState()
{
    if (cd != reinterpret_cast<iconv_t>(-1))
        iconv_close(cd);
    if (buffer != array)
        delete[] buffer;
}

//  from ../qt5compat/src/core5/codecs/qiconvcodec.cpp, line 76, as _ZN11QIconvCodec10IconvState9saveCharsEPKci
inline void QIconvCodec::IconvState::saveChars(const char *c, int count)
{
    if (count > bufferLen) {
        if (buffer != array)
            delete[] buffer;
        buffer = new char[bufferLen = count];
    }

    memcpy(buffer, c, count);
}
//  -----------------------------------------------------------------------

//  QIconvCodec::IconvState::IconvState(iconv_t x)
extern "C" Q_DECL_EXPORT
QIconvCodec::IconvState *ritual_ZN11QIconvCodec10IconvStateC1EPv(iconv_t x) {
  return new QIconvCodec::IconvState(x);
}

//  QIconvCodec::IconvState::~IconvState()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconvCodec10IconvStateD1Ev(QIconvCodec::IconvState *self) {
  delete self;
}

//  void QIconvCodec::IconvState::saveChars(const char *c, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QIconvCodec10IconvState9saveCharsEPKci(
    QIconvCodec::IconvState *self,
    const char *c,
    int count) {
  self->saveChars(c, count);
}

#endif  // QT_CONFIG(iconv)
#endif  // QT_CONFIG(iconv) && QT_CONFIG(textcodec) && !QT_CONFIG(icu)
