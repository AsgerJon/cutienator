//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringmatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstringmatcher.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QStringMatcher::QStringMatcher()
extern "C" Q_DECL_EXPORT
QStringMatcher *ritual_ZN14QStringMatcherC1Ev() {
  return new QStringMatcher();
}

//  QStringMatcher::QStringMatcher(const QString &pattern,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QStringMatcher *ritual_ZN14QStringMatcherC1ERK7QStringN2Qt15CaseSensitivityE(
    const QString *pattern,
    Qt::CaseSensitivity cs) {
  return new QStringMatcher(*pattern, cs);
}

//  QStringMatcher::QStringMatcher(const QChar *uc, qsizetype len,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QStringMatcher *ritual_ZN14QStringMatcherC1EPK5QCharxN2Qt15CaseSensitivityE(
    const QChar *uc,
    qsizetype len,
    Qt::CaseSensitivity cs) {
  return new QStringMatcher(uc, len, cs);
}

//  QStringMatcher::QStringMatcher(QStringView pattern, Qt::CaseSensitivity
//      cs)
extern "C" Q_DECL_EXPORT
QStringMatcher *ritual_ZN14QStringMatcherC1E11QStringViewN2Qt15CaseSensitivityE(
    const QString *pattern,
    Qt::CaseSensitivity cs) {
  return new QStringMatcher(QStringView(*pattern), cs);
}

//  QStringMatcher::QStringMatcher(const QStringMatcher &other)
extern "C" Q_DECL_EXPORT
QStringMatcher *ritual_ZN14QStringMatcherC1ERKS_(
    const QStringMatcher *other) {
  return new QStringMatcher(*other);
}

//  QStringMatcher::~QStringMatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStringMatcherD1Ev(QStringMatcher *self) {
  delete self;
}

//  void QStringMatcher::setPattern(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStringMatcher10setPatternERK7QString(
    QStringMatcher *self,
    const QString *pattern) {
  self->setPattern(*pattern);
}

//  void QStringMatcher::setCaseSensitivity(Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QStringMatcher18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QStringMatcher *self,
    Qt::CaseSensitivity cs) {
  self->setCaseSensitivity(cs);
}

//  qsizetype QStringMatcher::indexIn(const QString &str, qsizetype from)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QStringMatcher7indexInERK7QStringx(
    const QStringMatcher *self,
    const QString *str,
    qsizetype from) {
  return self->indexIn(*str, from);
}

//  qsizetype QStringMatcher::indexIn(const QChar *str, qsizetype length,
//      qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QStringMatcher7indexInEPK5QCharxx(
    const QStringMatcher *self,
    const QChar *str,
    qsizetype length,
    qsizetype from) {
  return self->indexIn(str, length, from);
}

//  qsizetype QStringMatcher::indexIn(QStringView str, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QStringMatcher7indexInE11QStringViewx(
    const QStringMatcher *self,
    const QString *str,
    qsizetype from) {
  return self->indexIn(QStringView(*str), from);
}

//  QString QStringMatcher::pattern() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QStringMatcher7patternEv(const QStringMatcher *self) {
  return new QString(self->pattern());
}

//  QStringView QStringMatcher::patternView() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QStringMatcher11patternViewEv(
    const QStringMatcher *self) {
  return new QString(self->patternView().toString());
}

//  Qt::CaseSensitivity QStringMatcher::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK14QStringMatcher15caseSensitivityEv(
    const QStringMatcher *self) {
  return self->caseSensitivity();
}
