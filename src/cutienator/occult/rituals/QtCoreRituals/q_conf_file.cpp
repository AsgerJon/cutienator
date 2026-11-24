//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(settings)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/private/qtools_p.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qsavefile.h>
#include <QtCore/qlockfile.h>
#endif
#ifdef Q_OS_VXWORKS
#  include <ioLib.h>
#endif
#include <algorithm>
#include <stdlib.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
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

#endif  // QT_CONFIG(settings)
