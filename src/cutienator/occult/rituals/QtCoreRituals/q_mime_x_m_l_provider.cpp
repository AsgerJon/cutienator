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
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimetypeparser_p.h>
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
#include <QtCore/6.12.0/QtCore/private/qmimemagicrulematcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/private/qmimetype_p.h>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QDebug>
#include <QtCore/QDir>
#include <QtCore/QXmlStreamReader>
#include <QtCore/QXmlStreamWriter>
#include <QtCore/QStack>
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
#include <QtCore/private/qmimeglobpattern_p.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/QRegularExpression>
#endif
#include <QtCore/QStringList>
#include <QtCore/QDebug>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/private/qmimetype_p.h>
#include <QtCore/private/qmimemagicrule_p.h>
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/QList>
#include <QtCore/QDebug>
#include <QtCore/qendian.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtCore/private/qtools_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 158, as local:qmimeglobpattern.cpp:isSimplePattern
static bool isSimplePattern(QStringView pattern)
{
   // starts with "*.", has no other '*'
   return pattern.lastIndexOf(u'*') == 0
      && pattern.size() > 1
      && pattern.at(1) == u'.' // (other dots are OK, like *.tar.bz2)
      // and contains no other special character
      && !pattern.contains(u'?')
      && !pattern.contains(u'[')
      ;
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 170, as local:qmimeglobpattern.cpp:isFastPattern
static bool isFastPattern(QStringView pattern)
{
   // starts with "*.", has no other '*' and no other '.'
   return pattern.lastIndexOf(u'*') == 0
      && pattern.lastIndexOf(u'.') == 1
      // and contains no other special character
      && !pattern.contains(u'?')
      && !pattern.contains(u'[')
      ;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 241, as local:qmimeprovider.cpp:appendIfNew
static inline void appendIfNew(QStringList &list, const QString &str)
{
    if (!list.contains(str))
        list.push_back(str);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 852, as local:qmimeprovider.cpp:internalMimeFileName
#if QT_CONFIG(mimetype_database)
static QString internalMimeFileName()
{
    return QStringLiteral("<internal MIME data>");
}
#endif  // QT_CONFIG(mimetype_database)

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 26, as local:qmimetypeparser.cpp:mimeTypeAttributeC
static const char mimeTypeAttributeC[] = "type";

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 31, as local:qmimetypeparser.cpp:nameAttributeC
static const char nameAttributeC[] = "name";

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 61, as _ZN15QMimeTypeParserD1Ev
inline QMimeTypeParser::~QMimeTypeParser()
    = default;

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 247, as _ZN17QMimeProviderBaseC2EP20QMimeDatabasePrivateRK7QString
inline QMimeProviderBase::QMimeProviderBase(QMimeDatabasePrivate *db, const QString &directory)
    : m_db(db), m_directory(directory)
{
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 255, as _ZN20QMimeAllGlobPatterns5clearEv
inline void QMimeAllGlobPatterns::clear()
{
    m_fastPatterns.clear();
    m_highWeightGlobs.clear();
    m_lowWeightGlobs.clear();
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 262, as _ZNK17QMimeProviderBase23isMimeTypeGlobsExcludedERK7QString
inline bool QMimeProviderBase::isMimeTypeGlobsExcluded(const QString &name) const
{
    if (m_overrideProvider) {
        if (m_overrideProvider->hasGlobDeleteAll(name))
            return true;
        return m_overrideProvider->isMimeTypeGlobsExcluded(name);
    }
    return false;
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 227, as _ZNK20QMimeAllGlobPatterns13matchingGlobsERK7QStringR20QMimeGlobMatchResultRKSt8functionIFbS2_EE
inline void QMimeAllGlobPatterns::matchingGlobs(const QString &fileName, QMimeGlobMatchResult &result,
                                         const AddMatchFilterFunc &filterFunc) const
{
    // First try the high weight matches (>50), if any.
    m_highWeightGlobs.match(result, fileName, filterFunc);

    // Now use the "fast patterns" dict, for simple *.foo patterns with weight 50
    // (which is most of them, so this optimization is definitely worth it)
    const qsizetype lastDot = fileName.lastIndexOf(u'.');
    if (lastDot != -1) { // if no '.', skip the extension lookup
        const qsizetype ext_len = fileName.size() - lastDot - 1;
        const QString simpleExtension = fileName.right(ext_len).toLower();
        // (toLower because fast patterns are always case-insensitive and saved as lowercase)

        const QStringList matchingMimeTypes = m_fastPatterns.value(simpleExtension);
        const QString simplePattern = "*."_L1 + simpleExtension;
        for (const QString &mime : matchingMimeTypes) {
            if (filterFunc(mime))
                result.addMatch(mime, 50, simplePattern, simpleExtension.size());
        }
        // Can't return yet; *.tar.bz2 has to win over *.bz2, so we need the
        // low-weight mimetypes anyway, at least those with weight 50.
    }

    // Finally, try the low weight matches (<=50)
    m_lowWeightGlobs.match(result, fileName, filterFunc);
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 55, as _ZNK21QMimeMagicRuleMatcher7matchesERK10QByteArray
inline bool QMimeMagicRuleMatcher::matches(const QByteArray &data) const
{
    for (const QMimeMagicRule &magicRule : m_list) {
        if (magicRule.matches(data))
            return true;
    }

    return false;
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 66, as _ZNK21QMimeMagicRuleMatcher8priorityEv
inline unsigned QMimeMagicRuleMatcher::priority() const
{
    return m_priority;
}

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 76, as _ZN19QMimeTypeParserBaseD1Ev
inline QMimeTypeParserBase::~QMimeTypeParserBase()
    = default;

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 181, as _ZN20QMimeAllGlobPatterns7addGlobERK16QMimeGlobPattern
inline void QMimeAllGlobPatterns::addGlob(const QMimeGlobPattern &glob)
{
    const QString &pattern = glob.pattern();
    Q_ASSERT(!pattern.isEmpty());

    // Store each patterns into either m_fastPatternDict (*.txt, *.html
    // etc. with default weight 50) or for the rest, like core.*, *.tar.bz2, *~,
    // into highWeightPatternOffset (>50) or lowWeightPatternOffset (<=50).

    if (glob.weight() == 50 && isFastPattern(pattern) && !glob.isCaseSensitive()) {
        // The bulk of the patterns is *.foo with weight 50 --> those go into the fast patterns hash.
        const QString extension = pattern.mid(2).toLower();
        QStringList &patterns = m_fastPatterns[extension]; // find or create
        if (!patterns.contains(glob.mimeType()))
            patterns.append(glob.mimeType());
    } else {
        if (glob.weight() > 50) {
            if (!m_highWeightGlobs.hasPattern(glob.mimeType(), glob.pattern()))
                m_highWeightGlobs.append(glob);
        } else {
            if (!m_lowWeightGlobs.hasPattern(glob.mimeType(), glob.pattern()))
                m_lowWeightGlobs.append(glob);
        }
    }
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 26, as _ZN20QMimeGlobMatchResult8addMatchERK7QStringiS2_x
inline void QMimeGlobMatchResult::addMatch(const QString &mimeType, int weight, const QString &pattern,
                                    qsizetype knownSuffixLength)
{
    if (m_allMatchingMimeTypes.contains(mimeType))
        return;
    // Is this a lower-weight pattern than the last match? Skip this match then.
    if (weight < m_weight) {
        m_allMatchingMimeTypes.append(mimeType);
        return;
    }
    bool replace = weight > m_weight;
    if (!replace) {
        // Compare the length of the match
        if (pattern.size() < m_matchingPatternLength)
            return; // too short, ignore
        else if (pattern.size() > m_matchingPatternLength) {
            // longer: clear any previous match (like *.bz2, when pattern is *.tar.bz2)
            replace = true;
        }
    }
    if (replace) {
        m_matchingMimeTypes.clear();
        // remember the new "longer" length
        m_matchingPatternLength = pattern.size();
        m_weight = weight;
    }
    if (!m_matchingMimeTypes.contains(mimeType)) {
        m_matchingMimeTypes.append(mimeType);
        if (replace)
            m_allMatchingMimeTypes.prepend(mimeType); // highest-weight first
        else
            m_allMatchingMimeTypes.append(mimeType);
        m_knownSuffixLength = knownSuffixLength;
    }
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 215, as _ZNK20QMimeGlobPatternList5matchER20QMimeGlobMatchResultRK7QStringRKSt8functionIFbS4_EE
inline void QMimeGlobPatternList::match(QMimeGlobMatchResult &result, const QString &fileName,
                                 const AddMatchFilterFunc &filterFunc) const
{
    for (const QMimeGlobPattern &glob : *this) {
        if (glob.matchFileName(fileName) && filterFunc(glob.mimeType())) {
            const QString pattern = glob.pattern();
            const qsizetype suffixLen = isSimplePattern(pattern) ? pattern.size() - strlen("*.") : 0;
            result.addMatch(glob.mimeType(), glob.weight(), pattern, suffixLen);
        }
    }
}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 325, as _ZNK14QMimeMagicRule7matchesERK10QByteArray
inline bool QMimeMagicRule::matches(const QByteArray &data) const
{
    const bool ok = m_matchFunction && (this->*m_matchFunction)(data);
    if (!ok)
        return false;

    // No submatch? Then we are done.
    if (m_subMatches.isEmpty())
        return true;

    //qDebug() << "Checking" << m_subMatches.count() << "sub-rules";
    // Check that one of the submatches matches too
    for ( QList<QMimeMagicRule>::const_iterator it = m_subMatches.begin(), end = m_subMatches.end() ;
          it != end ; ++it ) {
        if ((*it).matches(data)) {
            // One of the hierarchies matched -> mimetype recognized.
            return true;
        }
    }
    return false;


}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 105, as _ZNK16QMimeGlobPattern13matchFileNameERK7QString
inline bool QMimeGlobPattern::matchFileName(const QString &fileName) const
{
    // "Applications MUST match globs case-insensitively, except when the case-sensitive
    // attribute is set to true."

    const qsizetype patternLength = m_pattern.size();
    if (!patternLength)
        return false;
    const qsizetype fileNameLength = fileName.size();

    switch (m_patternType) {
    case SuffixPattern: {
        if (fileNameLength + 1 < patternLength)
            return false;
        // m_pattern is *.txt, skip the *
        return fileName.endsWith(QStringView(m_pattern).mid(1), m_caseSensitivity);
    }
    case PrefixPattern: {
        if (fileNameLength + 1 < patternLength)
            return false;
        // m_pattern ends with *, stop just before
        return fileName.startsWith(QStringView(m_pattern).chopped(1), m_caseSensitivity);
    }
    case LiteralPattern:
        return m_pattern.compare(fileName, m_caseSensitivity) == 0;
    case VdrPattern: // "[0-9][0-9][0-9].vdr" case
        return fileNameLength == 7
                && fileName.at(0).isDigit() && fileName.at(1).isDigit() && fileName.at(2).isDigit()
                && QStringView{fileName}.mid(3, 4).compare(".vdr"_L1, m_caseSensitivity) == 0;
    case AnimPattern: { // "*.anim[1-9j]" case
        if (fileNameLength < 6)
            return false;
        QChar lastChar = fileName.at(fileNameLength - 1);
        if (m_caseSensitivity == Qt::CaseInsensitive)
            lastChar = lastChar.toLower();
        const bool lastCharOK = (lastChar.isDigit() && lastChar != u'0')
                              || lastChar == u'j';
        return lastCharOK && QStringView{fileName}.mid(fileNameLength - 6, 5).compare(".anim"_L1, m_caseSensitivity) == 0;
    }
    case OtherPattern:
        // Other fallback patterns: slow but correct method
#if QT_CONFIG(regularexpression)
        auto rx = QRegularExpression::fromWildcard(m_pattern);
        if (m_caseSensitivity == Qt::CaseInsensitive)
            rx.setPatternOptions(QRegularExpression::CaseInsensitiveOption);
        return rx.match(fileName).hasMatch();
#else
        return false;
#endif
    }
    return false;
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

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 922, as _ZNK16QMimeXMLProvider18isInternalDatabaseEv
inline bool QMimeXMLProvider::isInternalDatabase() const
{
#if QT_CONFIG(mimetype_database)
    return m_directory == internalMimeFileName();
#else
    return false;
#endif
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 931, as _ZN16QMimeXMLProvider13knowsMimeTypeERK7QString
inline bool QMimeXMLProvider::knowsMimeType(const QString &name)
{
    return m_nameMimeTypeMap.contains(name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 936, as _ZN16QMimeXMLProvider18addFileNameMatchesERK7QStringR20QMimeGlobMatchResult
inline void QMimeXMLProvider::addFileNameMatches(const QString &fileName, QMimeGlobMatchResult &result)
{
    auto filterFunc = [this](const QString &name) { return !isMimeTypeGlobsExcluded(name); };
    m_mimeTypeGlobs.matchingGlobs(fileName, result, filterFunc);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1050, as _ZN16QMimeXMLProvider10addParentsERK7QStringR5QListIS0_E
inline void QMimeXMLProvider::addParents(const QString &mime, QStringList &result)
{
    const QStringList parents = m_parents.value(mime);
    for (const QString &parent : parents) {
        if (!result.contains(parent))
            result.append(parent);
    }
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1073, as _ZN16QMimeXMLProvider12resolveAliasERK7QString
inline QString QMimeXMLProvider::resolveAlias(const QString &name)
{
    return m_aliases.value(name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1064, as _ZN16QMimeXMLProvider10addAliasesERK7QStringR5QListIS0_E
inline void QMimeXMLProvider::addAliases(const QString &name, QStringList &result)
{
    // Iterate through the whole hash. This method is rarely used.
    for (const auto &[alias, mimeName] : std::as_const(m_aliases).asKeyValueRange()) {
        if (mimeName == name)
            appendIfNew(result, alias);
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

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 979, as _ZN16QMimeXMLProvider14localeCommentsERK7QString
inline QMimeTypePrivate::LocaleHash QMimeXMLProvider::localeComments(const QString &name)
{
    return m_nameMimeTypeMap.value(name).localeComments;
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

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1040, as _ZN16QMimeXMLProvider14addGlobPatternERK16QMimeGlobPattern
inline void QMimeXMLProvider::addGlobPattern(const QMimeGlobPattern &glob)
{
    m_mimeTypeGlobs.addGlob(glob);
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

//  bool QMimeXMLProvider::isInternalDatabase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMimeXMLProvider18isInternalDatabaseEv(
    const QMimeXMLProvider *self) {
  return self->isInternalDatabase();
}

//  bool QMimeXMLProvider::knowsMimeType(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QMimeXMLProvider13knowsMimeTypeERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return self->knowsMimeType(*name);
}

//  void QMimeXMLProvider::addFileNameMatches(const QString &fileName,
//      QMimeGlobMatchResult &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider18addFileNameMatchesERK7QStringR20QMimeGlobMatchResult(
    QMimeXMLProvider *self,
    const QString *fileName,
    QMimeGlobMatchResult *result) {
  self->addFileNameMatches(*fileName, *result);
}

//  void QMimeXMLProvider::addParents(const QString &mime, QStringList
//      &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider10addParentsERK7QStringR5QListIS0_E(
    QMimeXMLProvider *self,
    const QString *mime,
    QStringList *result) {
  self->addParents(*mime, *result);
}

//  QString QMimeXMLProvider::resolveAlias(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QMimeXMLProvider12resolveAliasERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return new QString(self->resolveAlias(*name));
}

//  void QMimeXMLProvider::addAliases(const QString &name, QStringList
//      &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider10addAliasesERK7QStringR5QListIS0_E(
    QMimeXMLProvider *self,
    const QString *name,
    QStringList *result) {
  self->addAliases(*name, *result);
}

//  void QMimeXMLProvider::findByMagic(const QByteArray &data,
//      QMimeMagicResult &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider11findByMagicERK10QByteArrayR16QMimeMagicResult(
    QMimeXMLProvider *self,
    const QByteArray *data,
    QMimeMagicResult *result) {
  self->findByMagic(*data, *result);
}

//  void QMimeXMLProvider::addAllMimeTypes(QList<QMimeType> &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider15addAllMimeTypesER5QListI9QMimeTypeE(
    QMimeXMLProvider *self,
    QList<QMimeType> *result) {
  self->addAllMimeTypes(*result);
}

//  QMimeTypePrivate::LocaleHash QMimeXMLProvider::localeComments(const
//      QString &name)
extern "C" Q_DECL_EXPORT
QMimeTypePrivate::LocaleHash *ritual_ZN16QMimeXMLProvider14localeCommentsERK7QString(
    QMimeXMLProvider *self,
    const QString *name) {
  return new QMimeTypePrivate::LocaleHash(self->localeComments(*name));
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

//  void QMimeXMLProvider::addGlobPattern(const QMimeGlobPattern &glob)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeXMLProvider14addGlobPatternERK16QMimeGlobPattern(
    QMimeXMLProvider *self,
    const QMimeGlobPattern *glob) {
  self->addGlobPattern(*glob);
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

//  a QMimeTypePrivate::LocaleHash a ritual of QMimeXMLProvider gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMimeXMLProvider__QMimeTypePrivate_LocaleHash(
    QMimeTypePrivate::LocaleHash *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
