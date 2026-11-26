//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlogging.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qglobal.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlogging.h>
#include <QtCore/private/qlogging_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>
#include <QtCore/private/qgettid_p.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstring.h>
#include <QtCore/qthread.h>
#include <QtCore/qvarlengtharray.h>
#ifdef Q_CC_MSVC
#include <intrin.h>
#endif
#if QT_CONFIG(slog2)
#endif
#if __has_include(<paths.h>)
#include <paths.h>
#endif
#ifdef Q_OS_ANDROID
#include <android/log.h>
#endif
#ifdef Q_OS_HARMONY
#include <QtCore/private/qohoslogger_p.h>
#endif
#ifdef Q_OS_DARWIN
#include <QtCore/private/qcore_mac_p.h>
#endif
#if QT_CONFIG(journald)
# include <systemd/sd-journal.h>
# include <syslog.h>
#endif
#if QT_CONFIG(syslog)
# include <syslog.h>
#endif
#ifdef Q_OS_UNIX
# include <sys/types.h>
# include <sys/stat.h>
# include <unistd.h>
# include <QtCore/private/qcore_unix_p.h>
#endif
#ifdef Q_OS_WASM
#include <emscripten/emscripten.h>
#endif
#ifdef QLOGGING_HAVE_BACKTRACE
#  include <QtCore/qregularexpression.h>
#endif
#ifdef QLOGGING_USE_EXECINFO_BACKTRACE
#  if QT_CONFIG(dladdr)
#    include <dlfcn.h>
#  endif
#  include <cxxabi.h>
#endif
#include <cstdlib>
#include <algorithm>
#include <chrono>
#include <memory>
#include <vector>
#include <stdio.h>
#ifdef Q_OS_WIN
#include <QtCore/qt_windows.h>
#include <processthreadsapi.h>
#include <QtCore/qfunctionpointer.h>
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

using namespace Qt::StringLiterals;

//  from src/corelib/global/qlogging.cpp, line 2479, as local:qlogging.cpp:copyInternalContext
static void copyInternalContext(QInternalMessageLogContext *self,
                                const QMessageLogContext &logContext) noexcept
{
    if (logContext.version == self->version) {
        auto other = static_cast<const QInternalMessageLogContext *>(&logContext);
        self->backtrace = other->backtrace;
    }
}

//  from src/corelib/global/qlogging.cpp, line 2518, as _ZN18QMessageLogContext15copyContextFromERKS_
inline QMessageLogContext &QMessageLogContext::copyContextFrom(const QMessageLogContext &logContext) noexcept
{
    this->category = logContext.category;
    this->file = logContext.file;
    this->line = logContext.line;
    this->function = logContext.function;
    if (Q_UNLIKELY(version == CurrentVersion + 1))
        copyInternalContext(static_cast<QInternalMessageLogContext *>(this), logContext);
    return *this;
}
//  -----------------------------------------------------------------------

//  QMessageLogContext::QMessageLogContext()
extern "C" Q_DECL_EXPORT
QMessageLogContext *ritual_ZN18QMessageLogContextC1Ev() {
  return new QMessageLogContext();
}

//  QMessageLogContext::QMessageLogContext(const char *fileName, int
//      lineNumber, const char *functionName, const char *categoryName)
extern "C" Q_DECL_EXPORT
QMessageLogContext *ritual_ZN18QMessageLogContextC1EPKciS1_S1_(
    const char *fileName,
    int lineNumber,
    const char *functionName,
    const char *categoryName) {
  return new QMessageLogContext(
      fileName,
      lineNumber,
      functionName,
      categoryName);
}

//  QMessageLogContext &QMessageLogContext::copyContextFrom(const
//      QMessageLogContext &logContext)
extern "C" Q_DECL_EXPORT
QMessageLogContext *ritual_ZN18QMessageLogContext15copyContextFromERKS_(
    QMessageLogContext *self,
    const QMessageLogContext *logContext) {
  return &(self->copyContextFrom(*logContext));
}
