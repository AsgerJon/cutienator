//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprinterinfo_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: the '#if' the whole file
//  stands under now also asks '__has_include(<cups/ppd.h>)' where Qt's
//  'qprint_p.h', which 'qprinterinfo_p.h' includes through
//  'qprintdevice_p.h', includes that header of CUPS, on macOS and on
//  Unix with 'QT_CONFIG(cups)', since a machine without the headers of
//  CUPS, as GitHub's Linux, refused the file. Kept as it is when the
//  generator runs again.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER) && \
    (!(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups))) || \
     __has_include(<cups/ppd.h>))
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprinterinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/qprinterinfo.h>
#include <QtPrintSupport/private/qprinterinfo_p.h>
#include <QtPrintSupport/private/qprintdevice_p.h>
#ifndef QT_NO_PRINTER
#include <QtCore/qdebug.h>
#include <QtPrintSupport/qpa/qplatformprintplugin.h>
#include <QtPrintSupport/qpa/qplatformprintersupport.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/printsupport/kernel/qprinterinfo.cpp, line 30, as _ZN19QPrinterInfoPrivateC1ERK7QString
#if !defined(QT_NO_PRINTER)
inline QPrinterInfoPrivate::QPrinterInfoPrivate(const QString &id)
{
    if (!id.isEmpty()) {
        QPlatformPrinterSupport *ps = QPlatformPrinterSupportPlugin::get();
        if (ps)
            m_printDevice = ps->createPrintDevice(id);
    }
}
#endif  // !defined(QT_NO_PRINTER)
//  -----------------------------------------------------------------------

//  QPrinterInfoPrivate::QPrinterInfoPrivate(const QString &id)
extern "C" Q_DECL_EXPORT
QPrinterInfoPrivate *ritual_ZN19QPrinterInfoPrivateC1ERK7QString(
    const QString *id) {
  return new QPrinterInfoPrivate(*id);
}

//  QPrinterInfoPrivate::~QPrinterInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPrinterInfoPrivateD1Ev(QPrinterInfoPrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_PRINTER) && (!(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups))) || __has_include(<cups/ppd.h>))
