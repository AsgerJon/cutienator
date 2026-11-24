//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsettings.h"
#include "qsettings_p.h"
#include "qcache.h"
#include "qcoreapplication.h"
#include "qdatastream.h"
#include "qdir.h"
#include "qfile.h"
#include "qfileinfo.h"
#include "qlibraryinfo.h"
#include "private/qlocking_p.h"
#include "qmutex.h"
#include "qpoint.h"
#include "qrect.h"
#include "qsize.h"
#include "qstandardpaths.h"
#include "private/qstringconverter_p.h"
#include "qtemporaryfile.h"
#include "private/qtools_p.h"
#ifndef QT_BOOTSTRAPPED
#include "qsavefile.h"
#include "qlockfile.h"
#endif
#ifdef Q_OS_VXWORKS
#  include <ioLib.h>
#endif
#include <algorithm>
#include <stdlib.h>
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#  include <shlobj.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qsettings.cpp, line 123, as _ZNK9QConfFile10isWritableEv
inline bool QConfFile::isWritable() const
{
    QFileInfo fileInfo(name);

#if QT_CONFIG(temporaryfile)
    if (fileInfo.exists()) {
#endif
        QFile file(name);
        return file.open(QFile::ReadWrite);
#if QT_CONFIG(temporaryfile)
    } else {
        // Create the directories to the file.
        QDir dir(fileInfo.absolutePath());
        if (!dir.exists()) {
            if (!dir.mkpath(dir.absolutePath()))
                return false;
        }

        // we use a temporary file to avoid race conditions
        QTemporaryFile file(name);
        return file.open();
    }
#endif
}
//  -----------------------------------------------------------------------

//  bool QConfFile::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QConfFile10isWritableEv(const QConfFile *self) {
  return self->isWritable();
}

//  QList<QConfFile *>::QList()
extern "C" Q_DECL_EXPORT
QList<QConfFile *> *ritual_list_make_QConfFile_ptr() {
  return new QList<QConfFile *>();
}

//  void QList<QConfFile *>::append(const QConfFile * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QConfFile_ptr(
    QList<QConfFile *> *self,
    QConfFile *element) {
  self->append(element);
}

//  qsizetype QList<QConfFile *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QConfFile_ptr(const QList<QConfFile *> *self) {
  return self->size();
}

//  const QConfFile * &QList<QConfFile *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QConfFile *ritual_list_at_QConfFile_ptr(
    const QList<QConfFile *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QConfFile *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QConfFile_ptr(QList<QConfFile *> *self) {
  delete self;
}
