//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlatin1stringmatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlatin1stringmatcher.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

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
