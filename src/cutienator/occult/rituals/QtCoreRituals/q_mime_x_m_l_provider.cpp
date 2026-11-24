//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeprovider_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimetypeparser_p.h>
#include <QtCore/6.12.0/QtCore/private/qmimemagicrulematcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmimeprovider_p.h"
#include "qmimetypeparser_p.h"
#include <qstandardpaths.h>
#include "qmimemagicrulematcher_p.h"
#include <QXmlStreamReader>
#include <QBuffer>
#include <QDir>
#include <QFile>
#include <QByteArrayMatcher>
#include <QDebug>
#include <QDateTime>
#include <QtEndian>
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

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1050, as _ZN16QMimeXMLProvider10addParentsERK7QStringR5QListIS0_E
inline void QMimeXMLProvider::addParents(const QString &mime, QStringList &result)
{
    const QStringList parents = m_parents.value(mime);
    for (const QString &parent : parents) {
        if (!result.contains(parent))
            result.append(parent);
    }
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 942, as _ZN16QMimeXMLProvider11findByMagicERK10QByteArrayR16QMimeMagicResult
inline void QMimeXMLProvider::findByMagic(const QByteArray &data, QMimeMagicResult &result)
{
    for (const QMimeMagicRuleMatcher &matcher : std::as_const(m_magicMatchers)) {
        if (matcher.matches(data)) {
            const int priority = matcher.priority();
            if (priority > result.accuracy) {
                result.accuracy = priority;
                result.candidate = matcher.mimetype();
            }
        }
    }
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 979, as _ZN16QMimeXMLProvider14localeCommentsERK7QString
inline QMimeTypePrivate::LocaleHash QMimeXMLProvider::localeComments(const QString &name)
{
    return m_nameMimeTypeMap.value(name).localeComments;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1083, as _ZN16QMimeXMLProvider15addAllMimeTypesER5QListI9QMimeTypeE
inline void QMimeXMLProvider::addAllMimeTypes(QList<QMimeType> &result)
{
    if (result.isEmpty()) { // fast path
        for (auto it = m_nameMimeTypeMap.constBegin(), end = m_nameMimeTypeMap.constEnd();
             it != end; ++it) {
            result.append(QMimeType(QMimeTypePrivate(it.value().name)));
        }
    } else {
        for (auto it = m_nameMimeTypeMap.constBegin(), end = m_nameMimeTypeMap.constEnd() ; it != end ; ++it) {
            const QString newMime = it.key();
            if (std::find_if(result.constBegin(), result.constEnd(), [newMime](const QMimeType &mime) -> bool { return mime.name() == newMime; })
                    == result.constEnd())
                result.append(QMimeType(QMimeTypePrivate(it.value().name)));
        }
    }
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 936, as _ZN16QMimeXMLProvider18addFileNameMatchesERK7QStringR20QMimeGlobMatchResult
inline void QMimeXMLProvider::addFileNameMatches(const QString &fileName, QMimeGlobMatchResult &result)
{
    auto filterFunc = [this](const QString &name) { return !isMimeTypeGlobsExcluded(name); };
    m_mimeTypeGlobs.matchingGlobs(fileName, result, filterFunc);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 911, as _ZN16QMimeXMLProviderD1Ev
inline QMimeXMLProvider::~QMimeXMLProvider()
{
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 915, as _ZN16QMimeXMLProvider7isValidEv
inline bool QMimeXMLProvider::isValid()
{
    // If you change this method, adjust the logic in QMimeDatabasePrivate::loadProviders,
    // which assumes isValid==false is only possible in QMimeBinaryProvider.
    return true;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 931, as _ZN16QMimeXMLProvider13knowsMimeTypeERK7QString
inline bool QMimeXMLProvider::knowsMimeType(const QString &name)
{
    return m_nameMimeTypeMap.contains(name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1073, as _ZN16QMimeXMLProvider12resolveAliasERK7QString
inline QString QMimeXMLProvider::resolveAlias(const QString &name)
{
    return m_aliases.value(name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 984, as _ZN16QMimeXMLProvider16hasGlobDeleteAllERK7QString
inline bool QMimeXMLProvider::hasGlobDeleteAll(const QString &name)
{
    return m_nameMimeTypeMap.value(name).hasGlobDeleteAll;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 989, as _ZN16QMimeXMLProvider12globPatternsERK7QString
inline QStringList QMimeXMLProvider::globPatterns(const QString &name)
{
    return m_nameMimeTypeMap.value(name).globPatterns;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 994, as _ZN16QMimeXMLProvider4iconERK7QString
inline QString QMimeXMLProvider::icon(const QString &name)
{
    return m_nameMimeTypeMap.value(name).iconName;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 999, as _ZN16QMimeXMLProvider11genericIconERK7QString
inline QString QMimeXMLProvider::genericIcon(const QString &name)
{
    return m_nameMimeTypeMap.value(name).genericIconName;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1045, as _ZN16QMimeXMLProvider11addMimeTypeERK16QMimeTypeXMLData
inline void QMimeXMLProvider::addMimeType(const QMimeTypeXMLData &mt)
{
    m_nameMimeTypeMap.insert(mt.name, mt);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1059, as _ZN16QMimeXMLProvider9addParentERK7QStringS2_
inline void QMimeXMLProvider::addParent(const QString &child, const QString &parent)
{
    m_parents[child].append(parent);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1078, as _ZN16QMimeXMLProvider8addAliasERK7QStringS2_
inline void QMimeXMLProvider::addAlias(const QString &alias, const QString &name)
{
    m_aliases.insert(alias, name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1100, as _ZN16QMimeXMLProvider15addMagicMatcherERK21QMimeMagicRuleMatcher
inline void QMimeXMLProvider::addMagicMatcher(const QMimeMagicRuleMatcher &matcher)
{
    m_magicMatchers.append(matcher);
}
//  -----------------------------------------------------------------------

//  QMimeXMLProvider::~QMimeXMLProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProviderD1Ev(QMimeXMLProvider *self) {
  delete self;
}

//  bool QMimeXMLProvider::isValid()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QMimeXMLProvider7isValidEv(QMimeXMLProvider *self) {
  return self->isValid();
}

//  bool QMimeXMLProvider::knowsMimeType(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QMimeXMLProvider13knowsMimeTypeERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return self->knowsMimeType(*name);
}

//  QString QMimeXMLProvider::resolveAlias(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QMimeXMLProvider12resolveAliasERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return new QString(self->resolveAlias(*name));
}

//  bool QMimeXMLProvider::hasGlobDeleteAll(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QMimeXMLProvider16hasGlobDeleteAllERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return self->hasGlobDeleteAll(*name);
}

//  QStringList QMimeXMLProvider::globPatterns(const QString &name)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QMimeXMLProvider12globPatternsERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return new QList<QString>(self->globPatterns(*name));
}

//  QString QMimeXMLProvider::icon(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QMimeXMLProvider4iconERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return new QString(self->icon(*name));
}

//  QString QMimeXMLProvider::genericIcon(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QMimeXMLProvider11genericIconERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return new QString(self->genericIcon(*name));
}

//  void QMimeXMLProvider::addMimeType(const QMimeTypeXMLData &mt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider11addMimeTypeERK16QMimeTypeXMLData(
    QMimeXMLProvider *self,
    const QMimeTypeXMLData *mt) {
  self->addMimeType(*mt);
}

//  void QMimeXMLProvider::addParent(const QString &child, const QString
//      &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider9addParentERK7QStringS2_(
    QMimeXMLProvider *self,
    const QString *child,
    const QString *parent) {
  self->addParent(*child, *parent);
}

//  void QMimeXMLProvider::addAlias(const QString &alias, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider8addAliasERK7QStringS2_(
    QMimeXMLProvider *self,
    const QString *alias,
    const QString *name) {
  self->addAlias(*alias, *name);
}

//  void QMimeXMLProvider::addMagicMatcher(const QMimeMagicRuleMatcher
//      &matcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider15addMagicMatcherERK21QMimeMagicRuleMatcher(
    QMimeXMLProvider *self,
    const QMimeMagicRuleMatcher *matcher) {
  self->addMagicMatcher(*matcher);
}

#endif  // QT_CONFIG(mimetype)
