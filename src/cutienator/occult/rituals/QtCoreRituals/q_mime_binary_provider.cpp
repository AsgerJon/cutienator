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
#include <QtCore/qlist.h>
#include <QtCore/QString>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 241, as local:qmimeprovider.cpp:appendIfNew
static inline void appendIfNew(QStringList &list, const QString &str)
{
    if (!list.contains(str))
        list.push_back(str);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 734, as _ZN19QMimeBinaryProvider17loadMimeTypeExtraERK7QString
inline QMimeBinaryProvider::MimeTypeExtraMap::const_iterator
QMimeBinaryProvider::loadMimeTypeExtra(const QString &mimeName)
{
#if QT_CONFIG(xmlstreamreader)
    auto [it, insertionOccurred] = m_mimetypeExtra.try_emplace(mimeName);
    if (insertionOccurred) {
        // load comment and globPatterns

        // shared-mime-info since 1.3 lowercases the xml files
        QFile qfile;
        const QString mimeFile = m_directory + u'/' + mimeName.toLower() + ".xml"_L1;
        qfile.setFileName(mimeFile);
        if (!qfile.open(QFile::ReadOnly)) {
            const QString fallbackMimeFile = m_directory + u'/' + mimeName + ".xml"_L1; // pre-1.3
            qfile.setFileName(fallbackMimeFile);
            if (!qfile.open(QFile::ReadOnly))
                return it;
        }

        MimeTypeExtra &extra = it->second;
        QString mainPattern;

        QXmlStreamReader xml(&qfile);
        if (xml.readNextStartElement()) {
            if (xml.name() != "mime-type"_L1) {
                return m_mimetypeExtra.cend();
            }
            const auto name = xml.attributes().value("type"_L1);
            if (name.isEmpty())
                return m_mimetypeExtra.cend();
            if (name.compare(mimeName, Qt::CaseInsensitive))
                qWarning() << "Got name" << name << "in file" << mimeFile << "expected" << mimeName;

            while (xml.readNextStartElement()) {
                const auto tag = xml.name();
                if (tag == "comment"_L1) {
                    QString lang = xml.attributes().value("xml:lang"_L1).toString();
                    const QString text = xml.readElementText();
                    if (lang.isEmpty()) {
                        lang = "default"_L1; // no locale attribute provided, treat it as default.
                    }
                    extra.localeComments.insert(lang, text);
                    continue; // we called readElementText, so we're at the EndElement already.
                } else if (tag == "glob-deleteall"_L1) { // as written out by shared-mime-info >= 0.70
                    extra.hasGlobDeleteAll = true;
                } else if (tag == "glob"_L1) { // as written out by shared-mime-info >= 0.70
                    const QString pattern = xml.attributes().value("pattern"_L1).toString();
                    if (mainPattern.isEmpty() && pattern.startsWith(u'*')) {
                        mainPattern = pattern;
                    }
                    appendIfNew(extra.globPatterns, pattern);
                }
                xml.skipCurrentElement();
            }
            Q_ASSERT(xml.name() == "mime-type"_L1);
        }

        // Let's assume that shared-mime-info is at least version 0.70
        // Otherwise we would need 1) a version check, and 2) code for parsing patterns from the globs file.
        if (!mainPattern.isEmpty() &&
                (extra.globPatterns.isEmpty() || extra.globPatterns.constFirst() != mainPattern)) {
            // ensure it's first in the list of patterns
            extra.globPatterns.removeAll(mainPattern);
            extra.globPatterns.prepend(mainPattern);
        }
    }
    return it;
#else
    Q_UNUSED(mimeName);
    qWarning("Cannot load mime type since QXmlStreamReader is not available.");
    return m_mimetypeExtra.cend();
#endif // feature xmlstreamreader
}

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

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 695, as _ZN19QMimeBinaryProvider15addAllMimeTypesER5QListI9QMimeTypeE
inline void QMimeBinaryProvider::addAllMimeTypes(QList<QMimeType> &result)
{
    loadMimeTypeList();
    if (result.isEmpty()) {
        result.reserve(m_mimetypeNames.size());
        for (const QString &name : std::as_const(m_mimetypeNames))
            result.append(QMimeType(QMimeTypePrivate(name)));
    } else {
        for (const QString &name : std::as_const(m_mimetypeNames))
            if (std::find_if(result.constBegin(), result.constEnd(), [name](const QMimeType &mime) -> bool { return mime.name() == name; })
                    == result.constEnd())
                result.append(QMimeType(QMimeTypePrivate(name)));
    }
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 710, as _ZN19QMimeBinaryProvider14localeCommentsERK7QString
inline QMimeTypePrivate::LocaleHash QMimeBinaryProvider::localeComments(const QString &name)
{
    MimeTypeExtraMap::const_iterator it = loadMimeTypeExtra(name);
    if (it != m_mimetypeExtra.cend())
        return it->second.localeComments;
    return {};
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 718, as _ZN19QMimeBinaryProvider16hasGlobDeleteAllERK7QString
inline bool QMimeBinaryProvider::hasGlobDeleteAll(const QString &name)
{
    MimeTypeExtraMap::const_iterator it = loadMimeTypeExtra(name);
    if (it != m_mimetypeExtra.cend())
        return it->second.hasGlobDeleteAll;
    return {};
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 726, as _ZN19QMimeBinaryProvider12globPatternsERK7QString
inline QStringList QMimeBinaryProvider::globPatterns(const QString &name)
{
    MimeTypeExtraMap::const_iterator it = loadMimeTypeExtra(name);
    if (it != m_mimetypeExtra.cend())
        return it->second.globPatterns;
    return {};
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

//  void QMimeBinaryProvider::addAllMimeTypes(QList<QMimeType> &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeBinaryProvider15addAllMimeTypesER5QListI9QMimeTypeE(
    QMimeBinaryProvider *self,
    QList<QMimeType> *result) {
  self->addAllMimeTypes(*result);
}

//  QMimeTypePrivate::LocaleHash QMimeBinaryProvider::localeComments(const
//      QString &name)
extern "C" Q_DECL_EXPORT
QMimeTypePrivate::LocaleHash *ritual_ZN19QMimeBinaryProvider14localeCommentsERK7QString(
    QMimeBinaryProvider *self,
    const QString *name) {
  return new QMimeTypePrivate::LocaleHash(self->localeComments(*name));
}

//  bool QMimeBinaryProvider::hasGlobDeleteAll(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMimeBinaryProvider16hasGlobDeleteAllERK7QString(
    QMimeBinaryProvider *self,
    const QString *name) {
  return self->hasGlobDeleteAll(*name);
}

//  QStringList QMimeBinaryProvider::globPatterns(const QString &name)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QMimeBinaryProvider12globPatternsERK7QString(
    QMimeBinaryProvider *self,
    const QString *name) {
  return new QList<QString>(self->globPatterns(*name));
}

//  void QMimeBinaryProvider::loadMimeTypeList()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeBinaryProvider16loadMimeTypeListEv(
    QMimeBinaryProvider *self) {
  self->loadMimeTypeList();
}

//  a QMimeTypePrivate::LocaleHash a ritual of QMimeBinaryProvider gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMimeBinaryProvider__QMimeTypePrivate_LocaleHash(
    QMimeTypePrivate::LocaleHash *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
