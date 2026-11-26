//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimeglobpattern_p.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/QRegularExpression>
#endif
#include <QtCore/QStringList>
#include <QtCore/QDebug>
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

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 207, as _ZN20QMimeAllGlobPatterns14removeMimeTypeERK7QString
inline void QMimeAllGlobPatterns::removeMimeType(const QString &mimeType)
{
    for (auto &x : m_fastPatterns)
        x.removeAll(mimeType);
    m_highWeightGlobs.removeMimeType(mimeType);
    m_lowWeightGlobs.removeMimeType(mimeType);
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

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 255, as _ZN20QMimeAllGlobPatterns5clearEv
inline void QMimeAllGlobPatterns::clear()
{
    m_fastPatterns.clear();
    m_highWeightGlobs.clear();
    m_lowWeightGlobs.clear();
}
//  -----------------------------------------------------------------------

//  void QMimeAllGlobPatterns::addGlob(const QMimeGlobPattern &glob)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatterns7addGlobERK16QMimeGlobPattern(
    QMimeAllGlobPatterns *self,
    const QMimeGlobPattern *glob) {
  self->addGlob(*glob);
}

//  void QMimeAllGlobPatterns::removeMimeType(const QString &mimeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatterns14removeMimeTypeERK7QString(
    QMimeAllGlobPatterns *self,
    const QString *mimeType) {
  self->removeMimeType(*mimeType);
}

//  void QMimeAllGlobPatterns::matchingGlobs(const QString &fileName,
//      QMimeGlobMatchResult &result, const AddMatchFilterFunc &filterFunc)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QMimeAllGlobPatterns13matchingGlobsERK7QStringR20QMimeGlobMatchResultRKSt8functionIFbS2_EE(
    const QMimeAllGlobPatterns *self,
    const QString *fileName,
    QMimeGlobMatchResult *result,
    const AddMatchFilterFunc *filterFunc) {
  self->matchingGlobs(*fileName, *result, *filterFunc);
}

//  void QMimeAllGlobPatterns::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatterns5clearEv(QMimeAllGlobPatterns *self) {
  self->clear();
}

//  QMimeAllGlobPatterns::~QMimeAllGlobPatterns()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatternsD1Ev(QMimeAllGlobPatterns *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
