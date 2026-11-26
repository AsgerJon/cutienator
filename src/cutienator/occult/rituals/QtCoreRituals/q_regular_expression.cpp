//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(regularexpression)
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>

//  PatternOptions QRegularExpression::patternOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QRegularExpression14patternOptionsEv(
    const QRegularExpression *self) {
  return static_cast<int>(self->patternOptions().toInt());
}

//  void QRegularExpression::setPatternOptions(PatternOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRegularExpression17setPatternOptionsE6QFlagsINS_13PatternOptionEE(
    QRegularExpression *self,
    int options) {
  self->setPatternOptions(
      QFlags<QRegularExpression::PatternOption>::fromInt(options));
}

//  QRegularExpression::QRegularExpression()
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionC1Ev() {
  return new QRegularExpression();
}

//  QRegularExpression::QRegularExpression(const QString &pattern,
//      PatternOptions options)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionC1ERK7QString6QFlagsINS_13PatternOptionEE(
    const QString *pattern,
    int options) {
  return new QRegularExpression(
      *pattern,
      QFlags<QRegularExpression::PatternOption>::fromInt(options));
}

//  QRegularExpression::QRegularExpression(const QRegularExpression &re)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionC1ERKS_(
    const QRegularExpression *re) {
  return new QRegularExpression(*re);
}

//  QRegularExpression::QRegularExpression(QRegularExpression &&re)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionC1EOS_(
    QRegularExpression *re) {
  return new QRegularExpression(std::move(*re));
}

//  QRegularExpression::~QRegularExpression()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRegularExpressionD1Ev(QRegularExpression *self) {
  delete self;
}

//  QRegularExpression &QRegularExpression::operator=(const
//      QRegularExpression &re)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionaSERKS_(
    QRegularExpression *self,
    const QRegularExpression *re) {
  return &(self->operator=(*re));
}

//  QRegularExpression &QRegularExpression::operator=(QRegularExpression
//      &&other)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionaSEOS_(
    QRegularExpression *self,
    QRegularExpression *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QRegularExpression::swap(QRegularExpression &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRegularExpression4swapERS_(
    QRegularExpression *self,
    QRegularExpression *other) {
  self->swap(*other);
}

//  QString QRegularExpression::pattern() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QRegularExpression7patternEv(
    const QRegularExpression *self) {
  return new QString(self->pattern());
}

//  void QRegularExpression::setPattern(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QRegularExpression10setPatternERK7QString(
    QRegularExpression *self,
    const QString *pattern) {
  self->setPattern(*pattern);
}

//  bool QRegularExpression::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QRegularExpression7isValidEv(
    const QRegularExpression *self) {
  return self->isValid();
}

//  qsizetype QRegularExpression::patternErrorOffset() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QRegularExpression18patternErrorOffsetEv(
    const QRegularExpression *self) {
  return self->patternErrorOffset();
}

//  QString QRegularExpression::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QRegularExpression11errorStringEv(
    const QRegularExpression *self) {
  return new QString(self->errorString());
}

//  int QRegularExpression::captureCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QRegularExpression12captureCountEv(
    const QRegularExpression *self) {
  return self->captureCount();
}

//  QStringList QRegularExpression::namedCaptureGroups() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QRegularExpression18namedCaptureGroupsEv(
    const QRegularExpression *self) {
  return new QList<QString>(self->namedCaptureGroups());
}

//  QRegularExpressionMatch QRegularExpression::match(const QString &subject,
//      qsizetype offset, MatchType matchType, MatchOptions matchOptions)
//      const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZNK18QRegularExpression5matchERK7QStringxNS_9MatchTypeE6QFlagsINS_11MatchOptionEE(
    const QRegularExpression *self,
    const QString *subject,
    qsizetype offset,
    QRegularExpression::MatchType matchType,
    int matchOptions) {
  return new QRegularExpressionMatch(
      self->match(
          *subject,
          offset,
          matchType,
          QFlags<QRegularExpression::MatchOption>::fromInt(matchOptions)));
}

#if QT_DEPRECATED_SINCE(6, 8)
//  QRegularExpressionMatch QRegularExpression::match(QStringView
//      subjectView, qsizetype offset, MatchType matchType, MatchOptions
//      matchOptions) const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZNK18QRegularExpression5matchE11QStringViewxNS_9MatchTypeE6QFlagsINS_11MatchOptionEE(
    const QRegularExpression *self,
    const QString *subjectView,
    qsizetype offset,
    QRegularExpression::MatchType matchType,
    int matchOptions) {
  return new QRegularExpressionMatch(
      self->match(
          QStringView(*subjectView),
          offset,
          matchType,
          QFlags<QRegularExpression::MatchOption>::fromInt(matchOptions)));
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  QRegularExpressionMatch QRegularExpression::matchView(QStringView
//      subjectView, qsizetype offset, MatchType matchType, MatchOptions
//      matchOptions) const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZNK18QRegularExpression9matchViewE11QStringViewxNS_9MatchTypeE6QFlagsINS_11MatchOptionEE(
    const QRegularExpression *self,
    const QString *subjectView,
    qsizetype offset,
    QRegularExpression::MatchType matchType,
    int matchOptions) {
  return new QRegularExpressionMatch(
      self->matchView(
          QStringView(*subjectView),
          offset,
          matchType,
          QFlags<QRegularExpression::MatchOption>::fromInt(matchOptions)));
}

//  QRegularExpressionMatchIterator QRegularExpression::globalMatch(const
//      QString &subject, qsizetype offset, MatchType matchType, MatchOptions
//      matchOptions) const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatchIterator *ritual_ZNK18QRegularExpression11globalMatchERK7QStringxNS_9MatchTypeE6QFlagsINS_11MatchOptionEE(
    const QRegularExpression *self,
    const QString *subject,
    qsizetype offset,
    QRegularExpression::MatchType matchType,
    int matchOptions) {
  return new QRegularExpressionMatchIterator(
      self->globalMatch(
          *subject,
          offset,
          matchType,
          QFlags<QRegularExpression::MatchOption>::fromInt(matchOptions)));
}

#if QT_DEPRECATED_SINCE(6, 8)
//  QRegularExpressionMatchIterator
//      QRegularExpression::globalMatch(QStringView subjectView, qsizetype
//      offset, MatchType matchType, MatchOptions matchOptions) const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatchIterator *ritual_ZNK18QRegularExpression11globalMatchE11QStringViewxNS_9MatchTypeE6QFlagsINS_11MatchOptionEE(
    const QRegularExpression *self,
    const QString *subjectView,
    qsizetype offset,
    QRegularExpression::MatchType matchType,
    int matchOptions) {
  return new QRegularExpressionMatchIterator(
      self->globalMatch(
          QStringView(*subjectView),
          offset,
          matchType,
          QFlags<QRegularExpression::MatchOption>::fromInt(matchOptions)));
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  QRegularExpressionMatchIterator
//      QRegularExpression::globalMatchView(QStringView subjectView,
//      qsizetype offset, MatchType matchType, MatchOptions matchOptions)
//      const
extern "C" Q_DECL_EXPORT
QRegularExpressionMatchIterator *ritual_ZNK18QRegularExpression15globalMatchViewE11QStringViewxNS_9MatchTypeE6QFlagsINS_11MatchOptionEE(
    const QRegularExpression *self,
    const QString *subjectView,
    qsizetype offset,
    QRegularExpression::MatchType matchType,
    int matchOptions) {
  return new QRegularExpressionMatchIterator(
      self->globalMatchView(
          QStringView(*subjectView),
          offset,
          matchType,
          QFlags<QRegularExpression::MatchOption>::fromInt(matchOptions)));
}

//  void QRegularExpression::optimize() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QRegularExpression8optimizeEv(
    const QRegularExpression *self) {
  self->optimize();
}

//  QString QRegularExpression::escape(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRegularExpression6escapeERK7QString(
    const QString *str) {
  return new QString(QRegularExpression::escape(*str));
}

//  QString QRegularExpression::wildcardToRegularExpression(const QString
//      &str, WildcardConversionOptions options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRegularExpression27wildcardToRegularExpressionERK7QString6QFlagsINS_24WildcardConversionOptionEE(
    const QString *str,
    int options) {
  return new QString(
      QRegularExpression::wildcardToRegularExpression(
          *str,
          QFlags<QRegularExpression::WildcardConversionOption>::fromInt(options)));
}

//  QString QRegularExpression::anchoredPattern(const QString &expression)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRegularExpression15anchoredPatternERK7QString(
    const QString *expression) {
  return new QString(QRegularExpression::anchoredPattern(*expression));
}

//  QString QRegularExpression::escape(QStringView str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRegularExpression6escapeE11QStringView(
    const QString *str) {
  return new QString(QRegularExpression::escape(QStringView(*str)));
}

//  QString QRegularExpression::wildcardToRegularExpression(QStringView str,
//      WildcardConversionOptions options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRegularExpression27wildcardToRegularExpressionE11QStringView6QFlagsINS_24WildcardConversionOptionEE(
    const QString *str,
    int options) {
  return new QString(
      QRegularExpression::wildcardToRegularExpression(
          QStringView(*str),
          QFlags<QRegularExpression::WildcardConversionOption>::fromInt(options)));
}

//  QString QRegularExpression::anchoredPattern(QStringView expression)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QRegularExpression15anchoredPatternE11QStringView(
    const QString *expression) {
  return new QString(
      QRegularExpression::anchoredPattern(
          QStringView(*expression)));
}

//  QRegularExpression QRegularExpression::fromWildcard(QStringView pattern,
//      Qt::CaseSensitivity cs, WildcardConversionOptions options)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpression12fromWildcardE11QStringViewN2Qt15CaseSensitivityE6QFlagsINS_24WildcardConversionOptionEE(
    const QString *pattern,
    Qt::CaseSensitivity cs,
    int options) {
  return new QRegularExpression(
      QRegularExpression::fromWildcard(
          QStringView(*pattern),
          cs,
          QFlags<QRegularExpression::WildcardConversionOption>::fromInt(options)));
}

//  bool operator==(const QRegularExpression &lhs, const QRegularExpression
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QRegularExpressionS1_(
    const QRegularExpression *lhs,
    const QRegularExpression *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QRegularExpression &lhs, const QRegularExpression
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QRegularExpressionS1_(
    const QRegularExpression *lhs,
    const QRegularExpression *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QRegularExpression::QRegularExpression(QRegularExpressionPrivate &dd)
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZN18QRegularExpressionC1ER25QRegularExpressionPrivate(
    QRegularExpressionPrivate *dd) {
  return new QRegularExpression(*dd);
}

#endif  // QT_CONFIG(regularexpression)
#endif  // QT_CONFIG(regularexpression)
