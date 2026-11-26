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
#include <QtCore/qstringview.h>
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
//  -----------------------------------------------------------------------

//  bool QMimeGlobPatternList::hasPattern(QStringView mimeType, QStringView
//      pattern) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMimeGlobPatternList10hasPatternE11QStringViewS0_(
    const QMimeGlobPatternList *self,
    const QString *mimeType,
    const QString *pattern) {
  return self->hasPattern(QStringView(*mimeType), QStringView(*pattern));
}

//  void QMimeGlobPatternList::removeMimeType(QStringView mimeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeGlobPatternList14removeMimeTypeE11QStringView(
    QMimeGlobPatternList *self,
    const QString *mimeType) {
  self->removeMimeType(QStringView(*mimeType));
}

//  void QMimeGlobPatternList::match(QMimeGlobMatchResult &result, const
//      QString &fileName, const AddMatchFilterFunc &filterFunc) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QMimeGlobPatternList5matchER20QMimeGlobMatchResultRK7QStringRKSt8functionIFbS4_EE(
    const QMimeGlobPatternList *self,
    QMimeGlobMatchResult *result,
    const QString *fileName,
    const AddMatchFilterFunc *filterFunc) {
  self->match(*result, *fileName, *filterFunc);
}

//  QMimeGlobPatternList::~QMimeGlobPatternList()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeGlobPatternListD1Ev(QMimeGlobPatternList *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
