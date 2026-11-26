//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qregularexpression.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(regularexpression)
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qlist.h>

//  QRegularExpressionMatch::QRegularExpressionMatch()
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN23QRegularExpressionMatchC1Ev() {
  return new QRegularExpressionMatch();
}

//  QRegularExpressionMatch::~QRegularExpressionMatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRegularExpressionMatchD1Ev(QRegularExpressionMatch *self) {
  delete self;
}

//  QRegularExpressionMatch::QRegularExpressionMatch(const
//      QRegularExpressionMatch &match)
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN23QRegularExpressionMatchC1ERKS_(
    const QRegularExpressionMatch *match) {
  return new QRegularExpressionMatch(*match);
}

//  QRegularExpressionMatch::QRegularExpressionMatch(QRegularExpressionMatch
//      &&match)
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN23QRegularExpressionMatchC1EOS_(
    QRegularExpressionMatch *match) {
  return new QRegularExpressionMatch(std::move(*match));
}

//  QRegularExpressionMatch &QRegularExpressionMatch::operator=(const
//      QRegularExpressionMatch &match)
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN23QRegularExpressionMatchaSERKS_(
    QRegularExpressionMatch *self,
    const QRegularExpressionMatch *match) {
  return &(self->operator=(*match));
}

//  QRegularExpressionMatch
//      &QRegularExpressionMatch::operator=(QRegularExpressionMatch &&match)
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN23QRegularExpressionMatchaSEOS_(
    QRegularExpressionMatch *self,
    QRegularExpressionMatch *match) {
  return &(self->operator=(std::move(*match)));
}

//  void QRegularExpressionMatch::swap(QRegularExpressionMatch &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRegularExpressionMatch4swapERS_(
    QRegularExpressionMatch *self,
    QRegularExpressionMatch *other) {
  self->swap(*other);
}

//  QRegularExpression QRegularExpressionMatch::regularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK23QRegularExpressionMatch17regularExpressionEv(
    const QRegularExpressionMatch *self) {
  return new QRegularExpression(self->regularExpression());
}

//  QRegularExpression::MatchType QRegularExpressionMatch::matchType() const
extern "C" Q_DECL_EXPORT
QRegularExpression::MatchType ritual_ZNK23QRegularExpressionMatch9matchTypeEv(
    const QRegularExpressionMatch *self) {
  return self->matchType();
}

//  QRegularExpression::MatchOptions QRegularExpressionMatch::matchOptions()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QRegularExpressionMatch12matchOptionsEv(
    const QRegularExpressionMatch *self) {
  return static_cast<int>(self->matchOptions().toInt());
}

//  bool QRegularExpressionMatch::hasMatch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRegularExpressionMatch8hasMatchEv(
    const QRegularExpressionMatch *self) {
  return self->hasMatch();
}

//  bool QRegularExpressionMatch::hasPartialMatch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRegularExpressionMatch15hasPartialMatchEv(
    const QRegularExpressionMatch *self) {
  return self->hasPartialMatch();
}

//  bool QRegularExpressionMatch::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRegularExpressionMatch7isValidEv(
    const QRegularExpressionMatch *self) {
  return self->isValid();
}

//  int QRegularExpressionMatch::lastCapturedIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QRegularExpressionMatch17lastCapturedIndexEv(
    const QRegularExpressionMatch *self) {
  return self->lastCapturedIndex();
}

//  bool QRegularExpressionMatch::hasCaptured(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRegularExpressionMatch11hasCapturedE14QAnyStringView(
    const QRegularExpressionMatch *self,
    const QString *name) {
  return self->hasCaptured(QAnyStringView(*name));
}

//  bool QRegularExpressionMatch::hasCaptured(int nth) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QRegularExpressionMatch11hasCapturedEi(
    const QRegularExpressionMatch *self,
    int nth) {
  return self->hasCaptured(nth);
}

//  QString QRegularExpressionMatch::captured(int nth) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRegularExpressionMatch8capturedEi(
    const QRegularExpressionMatch *self,
    int nth) {
  return new QString(self->captured(nth));
}

//  QStringView QRegularExpressionMatch::capturedView(int nth) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRegularExpressionMatch12capturedViewEi(
    const QRegularExpressionMatch *self,
    int nth) {
  return new QString(self->capturedView(nth).toString());
}

//  QString QRegularExpressionMatch::captured(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRegularExpressionMatch8capturedE14QAnyStringView(
    const QRegularExpressionMatch *self,
    const QString *name) {
  return new QString(self->captured(QAnyStringView(*name)));
}

//  QStringView QRegularExpressionMatch::capturedView(QAnyStringView name)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QRegularExpressionMatch12capturedViewE14QAnyStringView(
    const QRegularExpressionMatch *self,
    const QString *name) {
  return new QString(self->capturedView(QAnyStringView(*name)).toString());
}

//  QStringList QRegularExpressionMatch::capturedTexts() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK23QRegularExpressionMatch13capturedTextsEv(
    const QRegularExpressionMatch *self) {
  return new QList<QString>(self->capturedTexts());
}

//  qsizetype QRegularExpressionMatch::capturedStart(int nth) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QRegularExpressionMatch13capturedStartEi(
    const QRegularExpressionMatch *self,
    int nth) {
  return self->capturedStart(nth);
}

//  qsizetype QRegularExpressionMatch::capturedLength(int nth) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QRegularExpressionMatch14capturedLengthEi(
    const QRegularExpressionMatch *self,
    int nth) {
  return self->capturedLength(nth);
}

//  qsizetype QRegularExpressionMatch::capturedEnd(int nth) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QRegularExpressionMatch11capturedEndEi(
    const QRegularExpressionMatch *self,
    int nth) {
  return self->capturedEnd(nth);
}

//  qsizetype QRegularExpressionMatch::capturedStart(QAnyStringView name)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QRegularExpressionMatch13capturedStartE14QAnyStringView(
    const QRegularExpressionMatch *self,
    const QString *name) {
  return self->capturedStart(QAnyStringView(*name));
}

//  qsizetype QRegularExpressionMatch::capturedLength(QAnyStringView name)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QRegularExpressionMatch14capturedLengthE14QAnyStringView(
    const QRegularExpressionMatch *self,
    const QString *name) {
  return self->capturedLength(QAnyStringView(*name));
}

//  qsizetype QRegularExpressionMatch::capturedEnd(QAnyStringView name) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QRegularExpressionMatch11capturedEndE14QAnyStringView(
    const QRegularExpressionMatch *self,
    const QString *name) {
  return self->capturedEnd(QAnyStringView(*name));
}

//  QRegularExpressionMatch::QRegularExpressionMatch(QRegularExpressionMatchP
//      rivate &dd)
extern "C" Q_DECL_EXPORT
QRegularExpressionMatch *ritual_ZN23QRegularExpressionMatchC1ER30QRegularExpressionMatchPrivate(
    QRegularExpressionMatchPrivate *dd) {
  return new QRegularExpressionMatch(*dd);
}

#endif  // QT_CONFIG(regularexpression)
#endif  // QT_CONFIG(regularexpression)
