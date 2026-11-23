//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstring.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>

//  QString::QString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1Ev() {
  return new QString();
}

//  QString::QString(const QChar *unicode, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1EPK5QCharx(
    const QChar *unicode,
    qsizetype size) {
  return new QString(unicode, size);
}

//  QString::QString(QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1E5QChar(const QChar *c) {
  return new QString(*c);
}

//  QString::QString(qsizetype size, QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1Ex5QChar(qsizetype size, const QChar *c) {
  return new QString(size, *c);
}

//  QString::QString(QLatin1StringView latin1)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1E13QLatin1String(const QLatin1String *latin1) {
  return new QString(*latin1);
}

//  QString::QString(QStringView sv)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1E11QStringView(const QString *sv) {
  return new QString(QStringView(*sv));
}

//  QString::QString(const QString &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1ERKS_(const QString *a0) {
  return new QString(*a0);
}

//  QString::~QString()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringD1Ev(QString *self) {
  delete self;
}

//  qsizetype QString::maxSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN7QString7maxSizeEv() {
  return QString::maxSize();
}

//  qsizetype QString::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString4sizeEv(const QString *self) {
  return self->size();
}

//  qsizetype QString::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countEv(const QString *self) {
  return self->count();
}

//  qsizetype QString::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString6lengthEv(const QString *self) {
  return self->length();
}

//  bool QString::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString7isEmptyEv(const QString *self) {
  return self->isEmpty();
}

//  void QString::resize(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString6resizeEx(QString *self, qsizetype size) {
  self->resize(size);
}

//  void QString::resize(qsizetype size, QChar fillChar)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString6resizeEx5QChar(
    QString *self,
    qsizetype size,
    const QChar *fillChar) {
  self->resize(size, *fillChar);
}

//  void QString::resizeForOverwrite(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString18resizeForOverwriteEx(QString *self, qsizetype size) {
  self->resizeForOverwrite(size);
}

//  void QString::truncate(qsizetype pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString8truncateEx(QString *self, qsizetype pos) {
  self->truncate(pos);
}

//  void QString::chop(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString4chopEx(QString *self, qsizetype n) {
  self->chop(n);
}

//  qsizetype QString::capacity() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString8capacityEv(const QString *self) {
  return self->capacity();
}

//  void QString::reserve(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString7reserveEx(QString *self, qsizetype size) {
  self->reserve(size);
}

//  void QString::squeeze()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString7squeezeEv(QString *self) {
  self->squeeze();
}

//  const QChar *QString::unicode() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK7QString7unicodeEv(const QString *self) {
  return self->unicode();
}

//  QChar *QString::data()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN7QString4dataEv(QString *self) {
  return self->data();
}

//  const QChar *QString::data() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK7QString4dataEv(const QString *self) {
  return self->data();
}

//  const QChar *QString::constData() const
extern "C" Q_DECL_EXPORT
const QChar *ritual_ZNK7QString9constDataEv(const QString *self) {
  return self->constData();
}

//  void QString::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString6detachEv(QString *self) {
  self->detach();
}

//  bool QString::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString10isDetachedEv(const QString *self) {
  return self->isDetached();
}

//  bool QString::isSharedWith(const QString &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString12isSharedWithERKS_(
    const QString *self,
    const QString *other) {
  return self->isSharedWith(*other);
}

//  void QString::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString5clearEv(QString *self) {
  self->clear();
}

//  const QChar QString::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK7QString2atEx(const QString *self, qsizetype i) {
  return new QChar(self->at(i));
}

//  const QChar QString::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK7QStringixEx(const QString *self, qsizetype i) {
  return new QChar(self->operator[](i));
}

//  QChar QString::front() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK7QString5frontEv(const QString *self) {
  return new QChar(self->front());
}

//  QChar QString::back() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK7QString4backEv(const QString *self) {
  return new QChar(self->back());
}

//  qsizetype QString::indexOf(QChar c, qsizetype from, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString7indexOfE5QCharxN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*c, from, cs);
}

//  qsizetype QString::indexOf(QLatin1StringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString7indexOfE13QLatin1StringxN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*s, from, cs);
}

//  qsizetype QString::indexOf(const QString &s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString7indexOfERKS_xN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*s, from, cs);
}

//  qsizetype QString::indexOf(QStringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString7indexOfE11QStringViewxN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(QStringView(*s), from, cs);
}

//  qsizetype QString::lastIndexOf(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfE5QCharN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*c, cs);
}

//  qsizetype QString::lastIndexOf(QChar c, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfE5QCharxN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*c, from, cs);
}

//  qsizetype QString::lastIndexOf(QLatin1StringView s, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfE13QLatin1StringN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, cs);
}

//  qsizetype QString::lastIndexOf(QLatin1StringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfE13QLatin1StringxN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, from, cs);
}

//  qsizetype QString::lastIndexOf(const QString &s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfERKS_N2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, cs);
}

//  qsizetype QString::lastIndexOf(const QString &s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfERKS_xN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, from, cs);
}

//  qsizetype QString::lastIndexOf(QStringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfE11QStringViewN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), cs);
}

//  qsizetype QString::lastIndexOf(QStringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfE11QStringViewxN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), from, cs);
}

//  bool QString::contains(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8containsE5QCharN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->contains(*c, cs);
}

//  bool QString::contains(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8containsERKS_N2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->contains(*s, cs);
}

//  bool QString::contains(QLatin1StringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8containsE13QLatin1StringN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->contains(*s, cs);
}

//  bool QString::contains(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8containsE11QStringViewN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->contains(QStringView(*s), cs);
}

//  qsizetype QString::count(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countE5QCharN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->count(*c, cs);
}

//  qsizetype QString::count(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countERKS_N2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->count(*s, cs);
}

//  qsizetype QString::count(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countE11QStringViewN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->count(QStringView(*s), cs);
}

//  qsizetype QString::indexOf(const QRegularExpression &re, qsizetype from,
//      QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString7indexOfERK18QRegularExpressionxP23QRegularExpressionMatch(
    const QString *self,
    const QRegularExpression *re,
    qsizetype from,
    QRegularExpressionMatch *rmatch) {
  return self->indexOf(*re, from, rmatch);
}

//  qsizetype QString::lastIndexOf(const QRegularExpression &re, qsizetype
//      from, QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfERK18QRegularExpressionxP23QRegularExpressionMatch(
    const QString *self,
    const QRegularExpression *re,
    qsizetype from,
    QRegularExpressionMatch *rmatch) {
  return self->lastIndexOf(*re, from, rmatch);
}

//  bool QString::contains(const QRegularExpression &re,
//      QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8containsERK18QRegularExpressionP23QRegularExpressionMatch(
    const QString *self,
    const QRegularExpression *re,
    QRegularExpressionMatch *rmatch) {
  return self->contains(*re, rmatch);
}

//  qsizetype QString::count(const QRegularExpression &re) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countERK18QRegularExpression(
    const QString *self,
    const QRegularExpression *re) {
  return self->count(*re);
}

//  QString QString::section(QChar sep, qsizetype start, qsizetype end,
//      SectionFlags flags) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString7sectionE5QCharxx6QFlagsINS_11SectionFlagEE(
    const QString *self,
    const QChar *sep,
    qsizetype start,
    qsizetype end,
    int flags) {
  return new QString(
      self->section(
          *sep,
          start,
          end,
          QFlags<QString::SectionFlag>::fromInt(flags)));
}

//  QString QString::section(const QString &in_sep, qsizetype start,
//      qsizetype end, SectionFlags flags) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString7sectionERKS_xx6QFlagsINS_11SectionFlagEE(
    const QString *self,
    const QString *in_sep,
    qsizetype start,
    qsizetype end,
    int flags) {
  return new QString(
      self->section(
          *in_sep,
          start,
          end,
          QFlags<QString::SectionFlag>::fromInt(flags)));
}

//  QString QString::section(const QRegularExpression &re, qsizetype start,
//      qsizetype end, SectionFlags flags) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString7sectionERK18QRegularExpressionxx6QFlagsINS_11SectionFlagEE(
    const QString *self,
    const QRegularExpression *re,
    qsizetype start,
    qsizetype end,
    int flags) {
  return new QString(
      self->section(
          *re,
          start,
          end,
          QFlags<QString::SectionFlag>::fromInt(flags)));
}

//  QString QString::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString4leftEx(const QString *self, qsizetype n) {
  return new QString(self->left(n));
}

//  QString QString::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString5rightEx(const QString *self, qsizetype n) {
  return new QString(self->right(n));
}

//  QString QString::mid(qsizetype position, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString3midExx(
    const QString *self,
    qsizetype position,
    qsizetype n) {
  return new QString(self->mid(position, n));
}

//  QString QString::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString5firstEx(const QString *self, qsizetype n) {
  return new QString(self->first(n));
}

//  QString QString::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString4lastEx(const QString *self, qsizetype n) {
  return new QString(self->last(n));
}

//  QString QString::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString6slicedEx(const QString *self, qsizetype pos) {
  return new QString(self->sliced(pos));
}

//  QString QString::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString6slicedExx(
    const QString *self,
    qsizetype pos,
    qsizetype n) {
  return new QString(self->sliced(pos, n));
}

//  QString QString::chopped(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7choppedEx(const QString *self, qsizetype n) {
  return new QString(self->chopped(n));
}

//  bool QString::startsWith(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString10startsWithERKS_N2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*s, cs);
}

//  bool QString::startsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString10startsWithE11QStringViewN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(QStringView(*s), cs);
}

//  bool QString::startsWith(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString10startsWithE13QLatin1StringN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*s, cs);
}

//  bool QString::startsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString10startsWithE5QCharN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*c, cs);
}

//  bool QString::endsWith(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8endsWithERKS_N2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*s, cs);
}

//  bool QString::endsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8endsWithE11QStringViewN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(QStringView(*s), cs);
}

//  bool QString::endsWith(QLatin1StringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8endsWithE13QLatin1StringN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*s, cs);
}

//  bool QString::endsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8endsWithE5QCharN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*c, cs);
}

//  bool QString::isUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString7isUpperEv(const QString *self) {
  return self->isUpper();
}

//  bool QString::isLower() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString7isLowerEv(const QString *self) {
  return self->isLower();
}

//  QString QString::leftJustified(qsizetype width, QChar fill, bool trunc)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString13leftJustifiedEx5QCharb(
    const QString *self,
    qsizetype width,
    const QChar *fill,
    bool trunc) {
  return new QString(self->leftJustified(width, *fill, trunc));
}

//  QString QString::rightJustified(qsizetype width, QChar fill, bool trunc)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString14rightJustifiedEx5QCharb(
    const QString *self,
    qsizetype width,
    const QChar *fill,
    bool trunc) {
  return new QString(self->rightJustified(width, *fill, trunc));
}

//  QString QString::toLower() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7toLowerEv(const QString *self) {
  return new QString(self->toLower());
}

//  QString QString::toUpper() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7toUpperEv(const QString *self) {
  return new QString(self->toUpper());
}

//  QString QString::toCaseFolded() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString12toCaseFoldedEv(const QString *self) {
  return new QString(self->toCaseFolded());
}

//  QString QString::trimmed() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7trimmedEv(const QString *self) {
  return new QString(self->trimmed());
}

//  QString QString::simplified() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString10simplifiedEv(const QString *self) {
  return new QString(self->simplified());
}

//  QString QString::toHtmlEscaped() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString13toHtmlEscapedEv(const QString *self) {
  return new QString(self->toHtmlEscaped());
}

//  QString QString::normalized(NormalizationForm mode, QChar::UnicodeVersion
//      version) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString10normalizedENS_17NormalizationFormEN5QChar14UnicodeVersionE(
    const QString *self,
    QString::NormalizationForm mode,
    QChar::UnicodeVersion version) {
  return new QString(self->normalized(mode, version));
}

//  QString QString::repeated(qsizetype times) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString8repeatedEx(
    const QString *self,
    qsizetype times) {
  return new QString(self->repeated(times));
}

//  QString QString::nullTerminated() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString14nullTerminatedEv(const QString *self) {
  return new QString(self->nullTerminated());
}

//  QByteArray QString::toLatin1() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR7QString8toLatin1Ev(const QString *self) {
  return new QByteArray(self->toLatin1());
}

//  QByteArray QString::toUtf8() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR7QString6toUtf8Ev(const QString *self) {
  return new QByteArray(self->toUtf8());
}

//  QByteArray QString::toLocal8Bit() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR7QString11toLocal8BitEv(const QString *self) {
  return new QByteArray(self->toLocal8Bit());
}

//  QString QString::fromLatin1(QByteArrayView ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString10fromLatin1E14QByteArrayView(
    const QByteArrayView *ba) {
  return new QString(QString::fromLatin1(*ba));
}

//  QString QString::fromLatin1(const char *str, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString10fromLatin1EPKcx(
    const char *str,
    qsizetype size) {
  return new QString(QString::fromLatin1(str, size));
}

//  QString QString::fromUtf8(QByteArrayView utf8)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8fromUtf8E14QByteArrayView(
    const QByteArrayView *utf8) {
  return new QString(QString::fromUtf8(*utf8));
}

//  QString QString::fromUtf8(const char *utf8, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8fromUtf8EPKcx(const char *utf8, qsizetype size) {
  return new QString(QString::fromUtf8(utf8, size));
}

//  QString QString::fromLocal8Bit(QByteArrayView ba)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString13fromLocal8BitE14QByteArrayView(
    const QByteArrayView *ba) {
  return new QString(QString::fromLocal8Bit(*ba));
}

//  QString QString::fromLocal8Bit(const char *str, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString13fromLocal8BitEPKcx(
    const char *str,
    qsizetype size) {
  return new QString(QString::fromLocal8Bit(str, size));
}

//  QString QString::fromRawData(const QChar *a0, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString11fromRawDataEPK5QCharx(
    const QChar *a0,
    qsizetype size) {
  return new QString(QString::fromRawData(a0, size));
}

//  int QString::compare(const QString &s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString7compareERKS_N2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->compare(*s, cs);
}

//  int QString::compare(QLatin1StringView other, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString7compareE13QLatin1StringN2Qt15CaseSensitivityE(
    const QString *self,
    const QLatin1String *other,
    Qt::CaseSensitivity cs) {
  return self->compare(*other, cs);
}

//  int QString::compare(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString7compareE11QStringViewN2Qt15CaseSensitivityE(
    const QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->compare(QStringView(*s), cs);
}

//  int QString::compare(QChar ch, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString7compareE5QCharN2Qt15CaseSensitivityE(
    const QString *self,
    const QChar *ch,
    Qt::CaseSensitivity cs) {
  return self->compare(*ch, cs);
}

//  int QString::compare(const QString &s1, const QString &s2,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString7compareERKS_S1_N2Qt15CaseSensitivityE(
    const QString *s1,
    const QString *s2,
    Qt::CaseSensitivity cs) {
  return QString::compare(*s1, *s2, cs);
}

//  int QString::compare(const QString &s1, QLatin1StringView s2,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString7compareERKS_13QLatin1StringN2Qt15CaseSensitivityE(
    const QString *s1,
    const QLatin1String *s2,
    Qt::CaseSensitivity cs) {
  return QString::compare(*s1, *s2, cs);
}

//  int QString::compare(QLatin1StringView s1, const QString &s2,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString7compareE13QLatin1StringRKS_N2Qt15CaseSensitivityE(
    const QLatin1String *s1,
    const QString *s2,
    Qt::CaseSensitivity cs) {
  return QString::compare(*s1, *s2, cs);
}

//  int QString::compare(const QString &s1, QStringView s2,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString7compareERKS_11QStringViewN2Qt15CaseSensitivityE(
    const QString *s1,
    const QString *s2,
    Qt::CaseSensitivity cs) {
  return QString::compare(*s1, QStringView(*s2), cs);
}

//  int QString::compare(QStringView s1, const QString &s2,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString7compareE11QStringViewRKS_N2Qt15CaseSensitivityE(
    const QString *s1,
    const QString *s2,
    Qt::CaseSensitivity cs) {
  return QString::compare(QStringView(*s1), *s2, cs);
}

//  int QString::localeAwareCompare(const QString &s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString18localeAwareCompareERKS_(
    const QString *self,
    const QString *s) {
  return self->localeAwareCompare(*s);
}

//  int QString::localeAwareCompare(QStringView s) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString18localeAwareCompareE11QStringView(
    const QString *self,
    const QString *s) {
  return self->localeAwareCompare(QStringView(*s));
}

//  int QString::localeAwareCompare(const QString &s1, const QString &s2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString18localeAwareCompareERKS_S1_(
    const QString *s1,
    const QString *s2) {
  return QString::localeAwareCompare(*s1, *s2);
}

//  int QString::localeAwareCompare(QStringView s1, QStringView s2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString18localeAwareCompareE11QStringViewS0_(
    const QString *s1,
    const QString *s2) {
  return QString::localeAwareCompare(QStringView(*s1), QStringView(*s2));
}

//  short QString::toShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK7QString7toShortEPbi(
    const QString *self,
    bool *ok,
    int base) {
  return self->toShort(ok, base);
}

//  ushort QString::toUShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK7QString8toUShortEPbi(
    const QString *self,
    bool *ok,
    int base) {
  return self->toUShort(ok, base);
}

//  int QString::toInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QString5toIntEPbi(const QString *self, bool *ok, int base) {
  return self->toInt(ok, base);
}

//  uint QString::toUInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QString6toUIntEPbi(const QString *self, bool *ok, int base) {
  return self->toUInt(ok, base);
}

//  long QString::toLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK7QString6toLongEPbi(const QString *self, bool *ok, int base) {
  return self->toLong(ok, base);
}

//  ulong QString::toULong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK7QString7toULongEPbi(
    const QString *self,
    bool *ok,
    int base) {
  return self->toULong(ok, base);
}

//  qlonglong QString::toLongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK7QString10toLongLongEPbi(
    const QString *self,
    bool *ok,
    int base) {
  return self->toLongLong(ok, base);
}

//  qulonglong QString::toULongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK7QString11toULongLongEPbi(
    const QString *self,
    bool *ok,
    int base) {
  return self->toULongLong(ok, base);
}

//  float QString::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK7QString7toFloatEPb(const QString *self, bool *ok) {
  return self->toFloat(ok);
}

//  double QString::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK7QString8toDoubleEPb(const QString *self, bool *ok) {
  return self->toDouble(ok);
}

//  QString QString::number(int a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberEii(int a0, int base) {
  return new QString(QString::number(a0, base));
}

//  QString QString::number(uint a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberEji(uint a0, int base) {
  return new QString(QString::number(a0, base));
}

//  QString QString::number(long a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberEli(long a0, int base) {
  return new QString(QString::number(a0, base));
}

//  QString QString::number(ulong a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberEmi(ulong a0, int base) {
  return new QString(QString::number(a0, base));
}

//  QString QString::number(qlonglong a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberExi(qlonglong a0, int base) {
  return new QString(QString::number(a0, base));
}

//  QString QString::number(qulonglong a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberEyi(qulonglong a0, int base) {
  return new QString(QString::number(a0, base));
}

//  QString QString::number(double a0, char format, int precision)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6numberEdci(
    double a0,
    char format,
    int precision) {
  return new QString(QString::number(a0, format, precision));
}

//  QString::QString(const char *ch)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1EPKc(const char *ch) {
  return new QString(ch);
}

//  QString::QString(const QByteArray &a)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1ERK10QByteArray(const QByteArray *a) {
  return new QString(*a);
}

//  iterator QString::begin()
extern "C" Q_DECL_EXPORT
QString::iterator ritual_ZN7QString5beginEv(QString *self) {
  return self->begin();
}

//  const_iterator QString::begin() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK7QString5beginEv(const QString *self) {
  return self->begin();
}

//  const_iterator QString::cbegin() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK7QString6cbeginEv(const QString *self) {
  return self->cbegin();
}

//  const_iterator QString::constBegin() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK7QString10constBeginEv(
    const QString *self) {
  return self->constBegin();
}

//  iterator QString::end()
extern "C" Q_DECL_EXPORT
QString::iterator ritual_ZN7QString3endEv(QString *self) {
  return self->end();
}

//  const_iterator QString::end() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK7QString3endEv(const QString *self) {
  return self->end();
}

//  const_iterator QString::cend() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK7QString4cendEv(const QString *self) {
  return self->cend();
}

//  const_iterator QString::constEnd() const
extern "C" Q_DECL_EXPORT
QString::const_iterator ritual_ZNK7QString8constEndEv(const QString *self) {
  return self->constEnd();
}

//  void QString::push_back(QChar c)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString9push_backE5QChar(QString *self, const QChar *c) {
  self->push_back(*c);
}

//  void QString::push_back(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString9push_backERKS_(QString *self, const QString *s) {
  self->push_back(*s);
}

//  void QString::push_front(QChar c)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString10push_frontE5QChar(QString *self, const QChar *c) {
  self->push_front(*c);
}

//  void QString::push_front(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString10push_frontERKS_(QString *self, const QString *s) {
  self->push_front(*s);
}

//  void QString::shrink_to_fit()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString13shrink_to_fitEv(QString *self) {
  self->shrink_to_fit();
}

//  iterator QString::erase(const_iterator first, const_iterator last)
extern "C" Q_DECL_EXPORT
QString::iterator ritual_ZN7QString5eraseEPK5QCharS2_(
    QString *self,
    QString::const_iterator first,
    QString::const_iterator last) {
  return self->erase(first, last);
}

//  iterator QString::erase(const_iterator it)
extern "C" Q_DECL_EXPORT
QString::iterator ritual_ZN7QString5eraseEPK5QChar(
    QString *self,
    QString::const_iterator it) {
  return self->erase(it);
}

//  qsizetype QString::max_size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString8max_sizeEv(const QString *self) {
  return self->max_size();
}

//  bool QString::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString6isNullEv(const QString *self) {
  return self->isNull();
}

//  bool QString::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString13isRightToLeftEv(const QString *self) {
  return self->isRightToLeft();
}

//  bool QString::isValidUtf16() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString12isValidUtf16Ev(const QString *self) {
  return self->isValidUtf16();
}

//  QString::QString(qsizetype size, Qt::Initialization a1)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1ExN2Qt14InitializationE(
    qsizetype size,
    Qt::Initialization a1) {
  return new QString(size, a1);
}
