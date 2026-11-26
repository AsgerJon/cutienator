//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcollator.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcollator.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>

//  QCollator::QCollator()
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZN9QCollatorC1Ev() {
  return new QCollator();
}

//  QCollator::QCollator(const QLocale &locale)
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZN9QCollatorC1ERK7QLocale(const QLocale *locale) {
  return new QCollator(*locale);
}

//  QCollator::QCollator(const QCollator &a0)
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZN9QCollatorC1ERKS_(const QCollator *a0) {
  return new QCollator(*a0);
}

//  QCollator::~QCollator()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollatorD1Ev(QCollator *self) {
  delete self;
}

//  QCollator &QCollator::operator=(const QCollator &a0)
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZN9QCollatoraSERKS_(QCollator *self, const QCollator *a0) {
  return &(self->operator=(*a0));
}

//  QCollator::QCollator(QCollator &&other)
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZN9QCollatorC1EOS_(QCollator *other) {
  return new QCollator(std::move(*other));
}

//  QCollator &QCollator::operator=(QCollator &&other)
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZN9QCollatoraSEOS_(QCollator *self, QCollator *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCollator::swap(QCollator &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollator4swapERS_(QCollator *self, QCollator *other) {
  self->swap(*other);
}

//  void QCollator::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollator9setLocaleERK7QLocale(
    QCollator *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QCollator::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK9QCollator6localeEv(const QCollator *self) {
  return new QLocale(self->locale());
}

//  Qt::CaseSensitivity QCollator::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK9QCollator15caseSensitivityEv(
    const QCollator *self) {
  return self->caseSensitivity();
}

//  void QCollator::setCaseSensitivity(Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollator18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QCollator *self,
    Qt::CaseSensitivity cs) {
  self->setCaseSensitivity(cs);
}

//  void QCollator::setNumericMode(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollator14setNumericModeEb(QCollator *self, bool on) {
  self->setNumericMode(on);
}

//  bool QCollator::numericMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCollator11numericModeEv(const QCollator *self) {
  return self->numericMode();
}

//  void QCollator::setIgnorePunctuation(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollator20setIgnorePunctuationEb(QCollator *self, bool on) {
  self->setIgnorePunctuation(on);
}

//  bool QCollator::ignorePunctuation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCollator17ignorePunctuationEv(const QCollator *self) {
  return self->ignorePunctuation();
}

//  int QCollator::compare(const QString &s1, const QString &s2) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCollator7compareERK7QStringS2_(
    const QCollator *self,
    const QString *s1,
    const QString *s2) {
  return self->compare(*s1, *s2);
}

//  int QCollator::compare(const QChar *s1, qsizetype len1, const QChar *s2,
//      qsizetype len2) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCollator7compareEPK5QCharxS2_x(
    const QCollator *self,
    const QChar *s1,
    qsizetype len1,
    const QChar *s2,
    qsizetype len2) {
  return self->compare(s1, len1, s2, len2);
}

//  bool QCollator::operator()(const QString &s1, const QString &s2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCollatorclERK7QStringS2_(
    const QCollator *self,
    const QString *s1,
    const QString *s2) {
  return self->operator()(*s1, *s2);
}

//  int QCollator::compare(QStringView s1, QStringView s2) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QCollator7compareE11QStringViewS0_(
    const QCollator *self,
    const QString *s1,
    const QString *s2) {
  return self->compare(QStringView(*s1), QStringView(*s2));
}

//  bool QCollator::operator()(QStringView s1, QStringView s2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QCollatorclE11QStringViewS0_(
    const QCollator *self,
    const QString *s1,
    const QString *s2) {
  return self->operator()(QStringView(*s1), QStringView(*s2));
}

//  QCollatorSortKey QCollator::sortKey(const QString &string) const
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZNK9QCollator7sortKeyERK7QString(
    const QCollator *self,
    const QString *string) {
  return new QCollatorSortKey(self->sortKey(*string));
}

//  int QCollator::defaultCompare(QStringView s1, QStringView s2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QCollator14defaultCompareE11QStringViewS0_(
    const QString *s1,
    const QString *s2) {
  return QCollator::defaultCompare(QStringView(*s1), QStringView(*s2));
}

//  QCollatorSortKey QCollator::defaultSortKey(QStringView key)
extern "C" Q_DECL_EXPORT
QCollatorSortKey *ritual_ZN9QCollator14defaultSortKeyE11QStringView(
    const QString *key) {
  return new QCollatorSortKey(QCollator::defaultSortKey(QStringView(*key)));
}

//  bool operator==(const QCollator &lhs, const QCollator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QCollatorS1_(const QCollator *lhs, const QCollator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCollator &lhs, const QCollator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QCollatorS1_(const QCollator *lhs, const QCollator *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QCollator::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QCollator6detachEv(QCollator *self) {
  self->detach();
}
