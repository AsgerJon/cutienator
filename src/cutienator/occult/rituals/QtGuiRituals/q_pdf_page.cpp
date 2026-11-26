//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpdf_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_PDF)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpdf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qpdf_p.h>
#ifndef QT_NO_PDF
#include "qplatformdefs.h"
#include <QtGui/private/qcmyk_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtGui/qimagewriter.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qtimezone.h>
#include <QtCore/quuid.h>
#include <QtCore/qxmlstream.h>
#include <cstdio>
#include <map>
#ifndef QT_NO_COMPRESS
#include <zlib.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/painting/qpdf.cpp, line 193, as _ZN4QPdf10ByteStreamC2Eb
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::ByteStream(bool fileBacking)
            : dev(new QBuffer(&ba)),
            fileBackingEnabled(fileBacking),
            fileBackingActive(false),
            handleDirty(false)
    {
        dev->open(QIODevice::ReadWrite);
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 202, as _ZN4QPdf10ByteStreamD2Ev
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::~ByteStream()
    {
        delete dev;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 749, as _ZN8QPdfPageC1Ev
#if !defined(QT_NO_PDF)
inline QPdfPage::QPdfPage()
    : QPdf::ByteStream(true) // Enable file backing
{
}
#endif  // !defined(QT_NO_PDF)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_PDF)
//  QPdfPage::QPdfPage()
extern "C" Q_DECL_EXPORT
QPdfPage *ritual_ZN8QPdfPageC1Ev() {
  return new QPdfPage();
}
#endif  // !defined(QT_NO_PDF)

//  QPdfPage::~QPdfPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPdfPageD1Ev(QPdfPage *self) {
  delete self;
}

#endif  // !defined(QT_NO_PDF)
