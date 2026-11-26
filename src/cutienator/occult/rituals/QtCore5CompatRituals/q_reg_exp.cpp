//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qregexp.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qregexp.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QRegExp::QRegExp()
extern "C" Q_DECL_EXPORT
QRegExp *ritual_ZN7QRegExpC1Ev() {
  return new QRegExp();
}

//  QRegExp::QRegExp(const QString &pattern, Qt::CaseSensitivity cs,
//      PatternSyntax syntax)
extern "C" Q_DECL_EXPORT
QRegExp *ritual_ZN7QRegExpC1ERK7QStringN2Qt15CaseSensitivityENS_13PatternSyntaxE(
    const QString *pattern,
    Qt::CaseSensitivity cs,
    QRegExp::PatternSyntax syntax) {
  return new QRegExp(*pattern, cs, syntax);
}

//  QRegExp::QRegExp(const QRegExp &rx)
extern "C" Q_DECL_EXPORT
QRegExp *ritual_ZN7QRegExpC1ERKS_(const QRegExp *rx) {
  return new QRegExp(*rx);
}

//  QRegExp::~QRegExp()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegExpD1Ev(QRegExp *self) {
  delete self;
}

//  QRegExp &QRegExp::operator=(const QRegExp &rx)
extern "C" Q_DECL_EXPORT
QRegExp *ritual_ZN7QRegExpaSERKS_(QRegExp *self, const QRegExp *rx) {
  return &(self->operator=(*rx));
}

//  QRegExp &QRegExp::operator=(QRegExp &&other)
extern "C" Q_DECL_EXPORT
QRegExp *ritual_ZN7QRegExpaSEOS_(QRegExp *self, QRegExp *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QRegExp::swap(QRegExp &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegExp4swapERS_(QRegExp *self, QRegExp *other) {
  self->swap(*other);
}

//  bool QRegExp::operator==(const QRegExp &rx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExpeqERKS_(const QRegExp *self, const QRegExp *rx) {
  return self->operator==(*rx);
}

//  bool QRegExp::operator!=(const QRegExp &rx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExpneERKS_(const QRegExp *self, const QRegExp *rx) {
  return self->operator!=(*rx);
}

//  bool QRegExp::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExp7isEmptyEv(const QRegExp *self) {
  return self->isEmpty();
}

//  bool QRegExp::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExp7isValidEv(const QRegExp *self) {
  return self->isValid();
}

//  QString QRegExp::pattern() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QRegExp7patternEv(const QRegExp *self) {
  return new QString(self->pattern());
}

//  void QRegExp::setPattern(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegExp10setPatternERK7QString(
    QRegExp *self,
    const QString *pattern) {
  self->setPattern(*pattern);
}

//  Qt::CaseSensitivity QRegExp::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK7QRegExp15caseSensitivityEv(
    const QRegExp *self) {
  return self->caseSensitivity();
}

//  void QRegExp::setCaseSensitivity(Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegExp18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QRegExp *self,
    Qt::CaseSensitivity cs) {
  self->setCaseSensitivity(cs);
}

//  PatternSyntax QRegExp::patternSyntax() const
extern "C" Q_DECL_EXPORT
QRegExp::PatternSyntax ritual_ZNK7QRegExp13patternSyntaxEv(
    const QRegExp *self) {
  return self->patternSyntax();
}

//  void QRegExp::setPatternSyntax(PatternSyntax syntax)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegExp16setPatternSyntaxENS_13PatternSyntaxE(
    QRegExp *self,
    QRegExp::PatternSyntax syntax) {
  self->setPatternSyntax(syntax);
}

//  bool QRegExp::isMinimal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExp9isMinimalEv(const QRegExp *self) {
  return self->isMinimal();
}

//  void QRegExp::setMinimal(bool minimal)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegExp10setMinimalEb(QRegExp *self, bool minimal) {
  self->setMinimal(minimal);
}

//  bool QRegExp::exactMatch(const QString &str) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExp10exactMatchERK7QString(
    const QRegExp *self,
    const QString *str) {
  return self->exactMatch(*str);
}

//  QVariant QRegExp::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QRegExpcv8QVariantEv(const QRegExp *self) {
  return new QVariant(self->operator QVariant());
}

//  int QRegExp::indexIn(const QString &str, int offset, CaretMode caretMode)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp7indexInERK7QStringiNS_9CaretModeE(
    const QRegExp *self,
    const QString *str,
    int offset,
    QRegExp::CaretMode caretMode) {
  return self->indexIn(*str, offset, caretMode);
}

//  int QRegExp::lastIndexIn(const QString &str, int offset, CaretMode
//      caretMode) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp11lastIndexInERK7QStringiNS_9CaretModeE(
    const QRegExp *self,
    const QString *str,
    int offset,
    QRegExp::CaretMode caretMode) {
  return self->lastIndexIn(*str, offset, caretMode);
}

//  int QRegExp::matchedLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp13matchedLengthEv(const QRegExp *self) {
  return self->matchedLength();
}

#if !defined(QT_NO_REGEXP_CAPTURE)
//  int QRegExp::captureCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp12captureCountEv(const QRegExp *self) {
  return self->captureCount();
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  QStringList QRegExp::capturedTexts() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QRegExp13capturedTextsEv(const QRegExp *self) {
  return new QList<QString>(self->capturedTexts());
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  QStringList QRegExp::capturedTexts()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN7QRegExp13capturedTextsEv(QRegExp *self) {
  return new QList<QString>(self->capturedTexts());
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  QString QRegExp::cap(int nth) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QRegExp3capEi(const QRegExp *self, int nth) {
  return new QString(self->cap(nth));
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  QString QRegExp::cap(int nth)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QRegExp3capEi(QRegExp *self, int nth) {
  return new QString(self->cap(nth));
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  int QRegExp::pos(int nth) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp3posEi(const QRegExp *self, int nth) {
  return self->pos(nth);
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  int QRegExp::pos(int nth)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QRegExp3posEi(QRegExp *self, int nth) {
  return self->pos(nth);
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  QString QRegExp::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QRegExp11errorStringEv(const QRegExp *self) {
  return new QString(self->errorString());
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

#if !defined(QT_NO_REGEXP_CAPTURE)
//  QString QRegExp::errorString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QRegExp11errorStringEv(QRegExp *self) {
  return new QString(self->errorString());
}
#endif  // !defined(QT_NO_REGEXP_CAPTURE)

//  QString QRegExp::replaceIn(const QString &str, const QString &after)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QRegExp9replaceInERK7QStringS2_(
    const QRegExp *self,
    const QString *str,
    const QString *after) {
  return new QString(self->replaceIn(*str, *after));
}

//  QString QRegExp::removeIn(const QString &str) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QRegExp8removeInERK7QString(
    const QRegExp *self,
    const QString *str) {
  return new QString(self->removeIn(*str));
}

//  bool QRegExp::containedIn(const QString &str) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegExp11containedInERK7QString(
    const QRegExp *self,
    const QString *str) {
  return self->containedIn(*str);
}

//  int QRegExp::countIn(const QString &str) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp7countInERK7QString(
    const QRegExp *self,
    const QString *str) {
  return self->countIn(*str);
}

//  QStringList QRegExp::splitString(const QString &str, Qt::SplitBehavior
//      behavior) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QRegExp11splitStringERK7QString6QFlagsIN2Qt18SplitBehaviorFlagsEE(
    const QRegExp *self,
    const QString *str,
    int behavior) {
  return new QList<QString>(
      self->splitString(
          *str,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior)));
}

//  int QRegExp::indexIn(const QStringList &list, int from) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp7indexInERK5QListI7QStringEi(
    const QRegExp *self,
    const QList<QString> *list,
    int from) {
  return self->indexIn(*list, from);
}

//  int QRegExp::lastIndexIn(const QStringList &list, int from) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegExp11lastIndexInERK5QListI7QStringEi(
    const QRegExp *self,
    const QList<QString> *list,
    int from) {
  return self->lastIndexIn(*list, from);
}

//  QStringList QRegExp::replaceIn(const QStringList &stringList, const
//      QString &after) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QRegExp9replaceInERK5QListI7QStringERKS1_(
    const QRegExp *self,
    const QList<QString> *stringList,
    const QString *after) {
  return new QList<QString>(self->replaceIn(*stringList, *after));
}

//  QStringList QRegExp::filterList(const QStringList &stringList) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QRegExp10filterListERK5QListI7QStringE(
    const QRegExp *self,
    const QList<QString> *stringList) {
  return new QList<QString>(self->filterList(*stringList));
}

//  QString QRegExp::escape(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QRegExp6escapeERK7QString(const QString *str) {
  return new QString(QRegExp::escape(*str));
}
