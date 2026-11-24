//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeprovider_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimeprovider_p.h>
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/QFile>
#include <QtCore/QByteArrayMatcher>
#include <QtCore/QDebug>
#include <QtCore/QDateTime>
#include <QtCore/QtEndian>
#if QT_CONFIG(mimetype_database)
#  ifdef MIME_DATABASE_IS_ZSTD
#    include <zstd.h>
#  endif
#  ifdef MIME_DATABASE_IS_GZIP
#    include <zconf.h>
#    include <zlib.h>
#  endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 335, as _ZN19QMimeBinaryProvider7isValidEv
inline bool QMimeBinaryProvider::isValid()
{
    return m_cacheFile != nullptr;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 340, as _ZNK19QMimeBinaryProvider18isInternalDatabaseEv
inline bool QMimeBinaryProvider::isInternalDatabase() const
{
    return false;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 376, as _ZN19QMimeBinaryProvider13knowsMimeTypeERK7QString
inline bool QMimeBinaryProvider::knowsMimeType(const QString &name)
{
    if (!m_mimetypeListLoaded)
        loadMimeTypeList();
    return m_mimetypeNames.contains(name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 675, as _ZN19QMimeBinaryProvider16loadMimeTypeListEv
inline void QMimeBinaryProvider::loadMimeTypeList()
{
    if (!m_mimetypeListLoaded) {
        m_mimetypeListLoaded = true;
        m_mimetypeNames.clear();
        // Unfortunately mime.cache doesn't have a full list of all mimetypes.
        // So we have to parse the plain-text files called "types".
        QFile file(m_directory + QStringView(u"/types"));
        if (file.open(QIODevice::ReadOnly)) {
            QByteArray line;
            while (file.readLineInto(&line)) {
                auto lineView = QByteArrayView(line);
                if (lineView.endsWith('\n'))
                    lineView.chop(1);
                m_mimetypeNames.insert(QString::fromLatin1(lineView));
            }
        }
    }
}
//  -----------------------------------------------------------------------

//  bool QMimeBinaryProvider::isValid()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMimeBinaryProvider7isValidEv(QMimeBinaryProvider *self) {
  return self->isValid();
}

//  bool QMimeBinaryProvider::isInternalDatabase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QMimeBinaryProvider18isInternalDatabaseEv(
    const QMimeBinaryProvider *self) {
  return self->isInternalDatabase();
}

//  bool QMimeBinaryProvider::knowsMimeType(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMimeBinaryProvider13knowsMimeTypeERK7QString(
    QMimeBinaryProvider *self,
    const QString *name) {
  return self->knowsMimeType(*name);
}

//  void QMimeBinaryProvider::loadMimeTypeList()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeBinaryProvider16loadMimeTypeListEv(
    QMimeBinaryProvider *self) {
  self->loadMimeTypeList();
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
