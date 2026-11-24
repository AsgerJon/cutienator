//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlatin1stringmatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qlatin1stringmatcher.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringmatcher.h>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/text/qlatin1stringmatcher.cpp, line 77, as _ZN20QLatin1StringMatcher11setSearcherEv
inline void QLatin1StringMatcher::setSearcher() noexcept
{
    if (m_cs == Qt::CaseSensitive) {
        new (&m_caseSensitiveSearcher) CaseSensitiveSearcher(m_pattern.data(), m_pattern.end());
    } else {
        QtPrivate::QCaseInsensitiveLatin1Hash foldCase;
        qsizetype bufferSize = std::min(m_pattern.size(), qsizetype(sizeof m_foldBuffer));
        for (qsizetype i = 0; i < bufferSize; ++i)
            m_foldBuffer[i] = static_cast<char>(foldCase(m_pattern[i].toLatin1()));

        new (&m_caseInsensitiveSearcher)
                CaseInsensitiveSearcher(m_foldBuffer, &m_foldBuffer[bufferSize]);
    }
}

//  from src/corelib/text/qlatin1stringmatcher.cpp, line 95, as _ZN20QLatin1StringMatcher12freeSearcherEv
inline void QLatin1StringMatcher::freeSearcher() noexcept
{
    if (m_cs == Qt::CaseSensitive)
        m_caseSensitiveSearcher.~CaseSensitiveSearcher();
    else
        m_caseInsensitiveSearcher.~CaseInsensitiveSearcher();
}
//  -----------------------------------------------------------------------

//  QLatin1StringMatcher::QLatin1StringMatcher()
extern "C" Q_DECL_EXPORT
QLatin1StringMatcher *ritual_ZN20QLatin1StringMatcherC1Ev() {
  return new QLatin1StringMatcher();
}

//  QLatin1StringMatcher::QLatin1StringMatcher(QLatin1StringView pattern,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QLatin1StringMatcher *ritual_ZN20QLatin1StringMatcherC1E13QLatin1StringN2Qt15CaseSensitivityE(
    const QLatin1String *pattern,
    Qt::CaseSensitivity cs) {
  return new QLatin1StringMatcher(*pattern, cs);
}

//  QLatin1StringMatcher::~QLatin1StringMatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLatin1StringMatcherD1Ev(QLatin1StringMatcher *self) {
  delete self;
}

//  void QLatin1StringMatcher::setPattern(QLatin1StringView pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLatin1StringMatcher10setPatternE13QLatin1String(
    QLatin1StringMatcher *self,
    const QLatin1String *pattern) {
  self->setPattern(*pattern);
}

//  QLatin1StringView QLatin1StringMatcher::pattern() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK20QLatin1StringMatcher7patternEv(
    const QLatin1StringMatcher *self) {
  return new QLatin1String(self->pattern());
}

//  void QLatin1StringMatcher::setCaseSensitivity(Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLatin1StringMatcher18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QLatin1StringMatcher *self,
    Qt::CaseSensitivity cs) {
  self->setCaseSensitivity(cs);
}

//  Qt::CaseSensitivity QLatin1StringMatcher::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK20QLatin1StringMatcher15caseSensitivityEv(
    const QLatin1StringMatcher *self) {
  return self->caseSensitivity();
}

//  qsizetype QLatin1StringMatcher::indexIn(QLatin1StringView haystack,
//      qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QLatin1StringMatcher7indexInE13QLatin1Stringx(
    const QLatin1StringMatcher *self,
    const QLatin1String *haystack,
    qsizetype from) {
  return self->indexIn(*haystack, from);
}

//  qsizetype QLatin1StringMatcher::indexIn(QStringView haystack, qsizetype
//      from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QLatin1StringMatcher7indexInE11QStringViewx(
    const QLatin1StringMatcher *self,
    const QString *haystack,
    qsizetype from) {
  return self->indexIn(QStringView(*haystack), from);
}

//  void QLatin1StringMatcher::setSearcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLatin1StringMatcher11setSearcherEv(
    QLatin1StringMatcher *self) {
  self->setSearcher();
}

//  void QLatin1StringMatcher::freeSearcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLatin1StringMatcher12freeSearcherEv(
    QLatin1StringMatcher *self) {
  self->freeSearcher();
}
