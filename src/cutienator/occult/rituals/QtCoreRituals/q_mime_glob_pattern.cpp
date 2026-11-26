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
#include <QtCore/qstringview.h>
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

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 62, as _ZNK16QMimeGlobPattern17detectPatternTypeE11QStringView
inline QMimeGlobPattern::PatternType QMimeGlobPattern::detectPatternType(QStringView pattern) const
{
    const qsizetype patternLength = pattern.size();
    if (!patternLength)
        return OtherPattern;

    const qsizetype starCount = pattern.count(u'*');
    const bool hasSquareBracket = pattern.indexOf(u'[') != -1;
    const bool hasQuestionMark = pattern.indexOf(u'?') != -1;

    if (!hasSquareBracket && !hasQuestionMark) {
        if (starCount == 1) {
            // Patterns like "*~", "*.extension"
            if (pattern.at(0) == u'*')
                return SuffixPattern;
            // Patterns like "README*" (well this is currently the only one like that...)
            if (pattern.at(patternLength - 1) == u'*')
                return PrefixPattern;
        } else if (starCount == 0) {
            // Names without any wildcards like "README"
            return LiteralPattern;
        }
    }

    if (pattern == "[0-9][0-9][0-9].vdr"_L1)
        return VdrPattern;

    if (pattern == "*.anim[1-9j]"_L1)
        return AnimPattern;

    return OtherPattern;
}
//  -----------------------------------------------------------------------

//  QMimeGlobPattern::QMimeGlobPattern(const QString &thePattern, const
//      QString &theMimeType, unsigned int theWeight, Qt::CaseSensitivity s)
extern "C" Q_DECL_EXPORT
QMimeGlobPattern *ritual_ZN16QMimeGlobPatternC1ERK7QStringS2_jN2Qt15CaseSensitivityE(
    const QString *thePattern,
    const QString *theMimeType,
    unsigned int theWeight,
    Qt::CaseSensitivity s) {
  return new QMimeGlobPattern(*thePattern, *theMimeType, theWeight, s);
}

//  void QMimeGlobPattern::swap(QMimeGlobPattern &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeGlobPattern4swapERS_(
    QMimeGlobPattern *self,
    QMimeGlobPattern *other) {
  self->swap(*other);
}

//  bool QMimeGlobPattern::matchFileName(const QString &fileName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMimeGlobPattern13matchFileNameERK7QString(
    const QMimeGlobPattern *self,
    const QString *fileName) {
  return self->matchFileName(*fileName);
}

//  const QString &QMimeGlobPattern::pattern() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QMimeGlobPattern7patternEv(
    const QMimeGlobPattern *self) {
  return new QString(self->pattern());
}

//  unsigned int QMimeGlobPattern::weight() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK16QMimeGlobPattern6weightEv(
    const QMimeGlobPattern *self) {
  return self->weight();
}

//  const QString &QMimeGlobPattern::mimeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QMimeGlobPattern8mimeTypeEv(
    const QMimeGlobPattern *self) {
  return new QString(self->mimeType());
}

//  bool QMimeGlobPattern::isCaseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMimeGlobPattern15isCaseSensitiveEv(
    const QMimeGlobPattern *self) {
  return self->isCaseSensitive();
}

//  PatternType QMimeGlobPattern::detectPatternType(QStringView pattern)
//      const
extern "C" Q_DECL_EXPORT
QMimeGlobPattern::PatternType ritual_ZNK16QMimeGlobPattern17detectPatternTypeE11QStringView(
    const QMimeGlobPattern *self,
    const QString *pattern) {
  return self->detectPatternType(QStringView(*pattern));
}

//  QMimeGlobPattern::~QMimeGlobPattern()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeGlobPatternD1Ev(QMimeGlobPattern *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
