//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstring.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand:
//  'ritual_ZN7QString8asprintfEPKcz'. Kept as it is when the generator runs
//  again. Also added by hand on 2026-11-25, instances of templates of the
//  class: 5.
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstringview.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qlist.h>
#include <QtCore/QUtf8StringView>
#include <QtCore/QList>
#include <QtCore/QString>
#include <string>
#include <string_view>

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

//  QString &QString::operator=(QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringaSE5QChar(QString *self, const QChar *c) {
  return &(self->operator=(*c));
}

//  QString &QString::operator=(const QString &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringaSERKS_(QString *self, const QString *a0) {
  return &(self->operator=(*a0));
}

//  QString &QString::operator=(QLatin1StringView latin1)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringaSE13QLatin1String(
    QString *self,
    const QLatin1String *latin1) {
  return &(self->operator=(*latin1));
}

//  QString::QString(QString &&other)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1EOS_(QString *other) {
  return new QString(std::move(*other));
}

//  QString &QString::operator=(QString &&other)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringaSEOS_(QString *self, QString *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QString::swap(QString &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString4swapERS_(QString *self, QString *other) {
  self->swap(*other);
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

#if QT_DEPRECATED_SINCE(6, 4)
//  qsizetype QString::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countEv(const QString *self) {
  return self->count();
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

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

//  QString &QString::fill(QChar c, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString4fillE5QCharx(
    QString *self,
    const QChar *c,
    qsizetype size) {
  return &(self->fill(*c, size));
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

//  QString &QString::slice(qsizetype pos)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString5sliceEx(QString *self, qsizetype pos) {
  return &(self->slice(pos));
}

//  QString &QString::slice(qsizetype pos, qsizetype n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString5sliceExx(
    QString *self,
    qsizetype pos,
    qsizetype n) {
  return &(self->slice(pos, n));
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

//  QChar &QString::operator[](qsizetype i)
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN7QStringixEx(QString *self, qsizetype i) {
  return &(self->operator[](i));
}

//  QChar QString::front() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK7QString5frontEv(const QString *self) {
  return new QChar(self->front());
}

//  QChar &QString::front()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN7QString5frontEv(QString *self) {
  return &(self->front());
}

//  QChar QString::back() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK7QString4backEv(const QString *self) {
  return new QChar(self->back());
}

//  QChar &QString::back()
extern "C" Q_DECL_EXPORT
QChar *ritual_ZN7QString4backEv(QString *self) {
  return &(self->back());
}

//  QString QString::arg_impl(qlonglong a, int fieldwidth, int base, QChar
//      fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString8arg_implExii5QChar(
    const QString *self,
    qlonglong a,
    int fieldwidth,
    int base,
    const QChar *fillChar) {
  return new QString(self->arg_impl(a, fieldwidth, base, *fillChar));
}

//  QString QString::arg_impl(qulonglong a, int fieldwidth, int base, QChar
//      fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString8arg_implEyii5QChar(
    const QString *self,
    qulonglong a,
    int fieldwidth,
    int base,
    const QChar *fillChar) {
  return new QString(self->arg_impl(a, fieldwidth, base, *fillChar));
}

//  QString QString::arg_impl(double a, int fieldWidth, char format, int
//      precision, QChar fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString8arg_implEdici5QChar(
    const QString *self,
    double a,
    int fieldWidth,
    char format,
    int precision,
    const QChar *fillChar) {
  return new QString(
      self->arg_impl(
          a,
          fieldWidth,
          format,
          precision,
          *fillChar));
}

//  QString QString::arg_impl(QAnyStringView a, int fieldWidth, QChar
//      fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString8arg_implE14QAnyStringViewi5QChar(
    const QString *self,
    const QString *a,
    int fieldWidth,
    const QChar *fillChar) {
  return new QString(
      self->arg_impl(
          QAnyStringView(*a),
          fieldWidth,
          *fillChar));
}

//  QString QString::vasprintf(const char *format, __va_list_tag *ap)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString9vasprintfEPKcP13__va_list_tag(
    const char *format,
    va_list ap) {
  return new QString(QString::vasprintf(format, ap));
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

#if QT_CONFIG(regularexpression)
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
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
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
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  bool QString::contains(const QRegularExpression &re,
//      QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QString8containsERK18QRegularExpressionP23QRegularExpressionMatch(
    const QString *self,
    const QRegularExpression *re,
    QRegularExpressionMatch *rmatch) {
  return self->contains(*re, rmatch);
}
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  qsizetype QString::count(const QRegularExpression &re) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString5countERK18QRegularExpression(
    const QString *self,
    const QRegularExpression *re) {
  return self->count(*re);
}
#endif  // QT_CONFIG(regularexpression)

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

#if QT_CONFIG(regularexpression)
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
#endif  // QT_CONFIG(regularexpression)

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString4leftEx(const QString *self, qsizetype n) {
  return new QString(self->left(n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString5rightEx(const QString *self, qsizetype n) {
  return new QString(self->right(n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::mid(qsizetype position, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString3midExx(
    const QString *self,
    qsizetype position,
    qsizetype n) {
  return new QString(self->mid(position, n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString5firstEx(const QString *self, qsizetype n) {
  return new QString(self->first(n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString4lastEx(const QString *self, qsizetype n) {
  return new QString(self->last(n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString6slicedEx(const QString *self, qsizetype pos) {
  return new QString(self->sliced(pos));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString6slicedExx(
    const QString *self,
    qsizetype pos,
    qsizetype n) {
  return new QString(self->sliced(pos, n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

#if !(QT_CORE_REMOVED_SINCE(6, 7))
//  QString QString::chopped(qsizetype n) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7choppedEx(const QString *self, qsizetype n) {
  return new QString(self->chopped(n));
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 7))

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

#if !defined(Q_QDOC)
//  QString QString::toLower() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7toLowerEv(const QString *self) {
  return new QString(self->toLower());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QString QString::toUpper() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7toUpperEv(const QString *self) {
  return new QString(self->toUpper());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QString QString::toCaseFolded() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString12toCaseFoldedEv(const QString *self) {
  return new QString(self->toCaseFolded());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QString QString::trimmed() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString7trimmedEv(const QString *self) {
  return new QString(self->trimmed());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QString QString::simplified() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString10simplifiedEv(const QString *self) {
  return new QString(self->simplified());
}
#endif  // !defined(Q_QDOC)

//  QString QString::toHtmlEscaped() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString13toHtmlEscapedEv(const QString *self) {
  return new QString(self->toHtmlEscaped());
}

//  QString &QString::insert(qsizetype i, QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertEx5QChar(
    QString *self,
    qsizetype i,
    const QChar *c) {
  return &(self->insert(i, *c));
}

//  QString &QString::insert(qsizetype i, const QChar *uc, qsizetype len)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertExPK5QCharx(
    QString *self,
    qsizetype i,
    const QChar *uc,
    qsizetype len) {
  return &(self->insert(i, uc, len));
}

//  QString &QString::insert(qsizetype i, const QString &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertExRKS_(
    QString *self,
    qsizetype i,
    const QString *s) {
  return &(self->insert(i, *s));
}

//  QString &QString::insert(qsizetype i, QStringView v)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertEx11QStringView(
    QString *self,
    qsizetype i,
    const QString *v) {
  return &(self->insert(i, QStringView(*v)));
}

//  QString &QString::insert(qsizetype i, QLatin1StringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertEx13QLatin1String(
    QString *self,
    qsizetype i,
    const QLatin1String *s) {
  return &(self->insert(i, *s));
}

//  QString &QString::insert(qsizetype i, QUtf8StringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertEx20QBasicUtf8StringViewILb0EE(
    QString *self,
    qsizetype i,
    const QUtf8StringView *s) {
  return &(self->insert(i, *s));
}

//  QString &QString::append(QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendE5QChar(QString *self, const QChar *c) {
  return &(self->append(*c));
}

//  QString &QString::append(const QChar *uc, qsizetype len)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendEPK5QCharx(
    QString *self,
    const QChar *uc,
    qsizetype len) {
  return &(self->append(uc, len));
}

//  QString &QString::append(const QString &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendERKS_(QString *self, const QString *s) {
  return &(self->append(*s));
}

//  QString &QString::append(QStringView v)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendE11QStringView(
    QString *self,
    const QString *v) {
  return &(self->append(QStringView(*v)));
}

//  QString &QString::append(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendE13QLatin1String(
    QString *self,
    const QLatin1String *s) {
  return &(self->append(*s));
}

//  QString &QString::append(QUtf8StringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendE20QBasicUtf8StringViewILb0EE(
    QString *self,
    const QUtf8StringView *s) {
  return &(self->append(*s));
}

//  QString &QString::prepend(QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependE5QChar(QString *self, const QChar *c) {
  return &(self->prepend(*c));
}

//  QString &QString::prepend(const QChar *uc, qsizetype len)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependEPK5QCharx(
    QString *self,
    const QChar *uc,
    qsizetype len) {
  return &(self->prepend(uc, len));
}

//  QString &QString::prepend(const QString &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependERKS_(QString *self, const QString *s) {
  return &(self->prepend(*s));
}

//  QString &QString::prepend(QStringView v)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependE11QStringView(
    QString *self,
    const QString *v) {
  return &(self->prepend(QStringView(*v)));
}

//  QString &QString::prepend(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependE13QLatin1String(
    QString *self,
    const QLatin1String *s) {
  return &(self->prepend(*s));
}

//  QString &QString::prepend(QUtf8StringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependE20QBasicUtf8StringViewILb0EE(
    QString *self,
    const QUtf8StringView *s) {
  return &(self->prepend(*s));
}

//  QString &QString::assign(QAnyStringView s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6assignE14QAnyStringView(
    QString *self,
    const QString *s) {
  return &(self->assign(QAnyStringView(*s)));
}

//  QString &QString::assign(qsizetype n, QChar c)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6assignEx5QChar(
    QString *self,
    qsizetype n,
    const QChar *c) {
  return &(self->assign(n, *c));
}

//  QString &QString::operator+=(QChar c)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLE5QChar(QString *self, const QChar *c) {
  self->operator+=(*c);
}

//  QString &QString::operator+=(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLERKS_(QString *self, const QString *s) {
  self->operator+=(*s);
}

//  QString &QString::operator+=(QStringView v)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLE11QStringView(QString *self, const QString *v) {
  self->operator+=(QStringView(*v));
}

//  QString &QString::operator+=(QLatin1StringView s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLE13QLatin1String(
    QString *self,
    const QLatin1String *s) {
  self->operator+=(*s);
}

//  QString &QString::operator+=(QUtf8StringView s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLE20QBasicUtf8StringViewILb0EE(
    QString *self,
    const QUtf8StringView *s) {
  self->operator+=(*s);
}

//  QString &QString::remove(qsizetype i, qsizetype len)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6removeExx(
    QString *self,
    qsizetype i,
    qsizetype len) {
  return &(self->remove(i, len));
}

//  QString &QString::remove(QChar c, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6removeE5QCharN2Qt15CaseSensitivityE(
    QString *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return &(self->remove(*c, cs));
}

//  QString &QString::remove(QLatin1StringView s, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6removeE13QLatin1StringN2Qt15CaseSensitivityE(
    QString *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return &(self->remove(*s, cs));
}

//  QString &QString::remove(const QString &s, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6removeERKS_N2Qt15CaseSensitivityE(
    QString *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return &(self->remove(*s, cs));
}

//  QString &QString::removeAt(qsizetype pos)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8removeAtEx(QString *self, qsizetype pos) {
  return &(self->removeAt(pos));
}

//  QString &QString::removeFirst()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString11removeFirstEv(QString *self) {
  return &(self->removeFirst());
}

//  QString &QString::removeLast()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString10removeLastEv(QString *self) {
  return &(self->removeLast());
}

//  QString &QString::replace(qsizetype i, qsizetype len, QChar after)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceExx5QChar(
    QString *self,
    qsizetype i,
    qsizetype len,
    const QChar *after) {
  return &(self->replace(i, len, *after));
}

//  QString &QString::replace(qsizetype i, qsizetype len, const QChar *s,
//      qsizetype slen)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceExxPK5QCharx(
    QString *self,
    qsizetype i,
    qsizetype len,
    const QChar *s,
    qsizetype slen) {
  return &(self->replace(i, len, s, slen));
}

//  QString &QString::replace(qsizetype i, qsizetype len, const QString
//      &after)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceExxRKS_(
    QString *self,
    qsizetype i,
    qsizetype len,
    const QString *after) {
  return &(self->replace(i, len, *after));
}

//  QString &QString::replace(QChar before, QChar after, Qt::CaseSensitivity
//      cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceE5QCharS0_N2Qt15CaseSensitivityE(
    QString *self,
    const QChar *before,
    const QChar *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*before, *after, cs));
}

//  QString &QString::replace(const QChar *before, qsizetype blen, const
//      QChar *after, qsizetype alen, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceEPK5QCharxS2_xN2Qt15CaseSensitivityE(
    QString *self,
    const QChar *before,
    qsizetype blen,
    const QChar *after,
    qsizetype alen,
    Qt::CaseSensitivity cs) {
  return &(self->replace(before, blen, after, alen, cs));
}

//  QString &QString::replace(QLatin1StringView before, QLatin1StringView
//      after, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceE13QLatin1StringS0_N2Qt15CaseSensitivityE(
    QString *self,
    const QLatin1String *before,
    const QLatin1String *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*before, *after, cs));
}

//  QString &QString::replace(QLatin1StringView before, const QString &after,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceE13QLatin1StringRKS_N2Qt15CaseSensitivityE(
    QString *self,
    const QLatin1String *before,
    const QString *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*before, *after, cs));
}

//  QString &QString::replace(const QString &before, QLatin1StringView after,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceERKS_13QLatin1StringN2Qt15CaseSensitivityE(
    QString *self,
    const QString *before,
    const QLatin1String *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*before, *after, cs));
}

//  QString &QString::replace(const QString &before, const QString &after,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceERKS_S1_N2Qt15CaseSensitivityE(
    QString *self,
    const QString *before,
    const QString *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*before, *after, cs));
}

//  QString &QString::replace(QChar c, const QString &after,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceE5QCharRKS_N2Qt15CaseSensitivityE(
    QString *self,
    const QChar *c,
    const QString *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*c, *after, cs));
}

//  QString &QString::replace(QChar c, QLatin1StringView after,
//      Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceE5QChar13QLatin1StringN2Qt15CaseSensitivityE(
    QString *self,
    const QChar *c,
    const QLatin1String *after,
    Qt::CaseSensitivity cs) {
  return &(self->replace(*c, *after, cs));
}

#if QT_CONFIG(regularexpression)
//  QString &QString::replace(const QRegularExpression &re, const QString
//      &after)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7replaceERK18QRegularExpressionRKS_(
    QString *self,
    const QRegularExpression *re,
    const QString *after) {
  return &(self->replace(*re, *after));
}
#endif  // QT_CONFIG(regularexpression)

#if QT_CONFIG(regularexpression)
//  QString &QString::remove(const QRegularExpression &re)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6removeERK18QRegularExpression(
    QString *self,
    const QRegularExpression *re) {
  return &(self->remove(*re));
}
#endif  // QT_CONFIG(regularexpression)

//  QStringList QString::split(const QString &sep, Qt::SplitBehavior
//      behavior, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QString5splitERKS_6QFlagsIN2Qt18SplitBehaviorFlagsEENS3_15CaseSensitivityE(
    const QString *self,
    const QString *sep,
    int behavior,
    Qt::CaseSensitivity cs) {
  return new QList<QString>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior),
          cs));
}

//  QStringList QString::split(QChar sep, Qt::SplitBehavior behavior,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QString5splitE5QChar6QFlagsIN2Qt18SplitBehaviorFlagsEENS2_15CaseSensitivityE(
    const QString *self,
    const QChar *sep,
    int behavior,
    Qt::CaseSensitivity cs) {
  return new QList<QString>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior),
          cs));
}

#if !defined(QT_NO_REGULAREXPRESSION)
//  QStringList QString::split(const QRegularExpression &sep,
//      Qt::SplitBehavior behavior) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK7QString5splitERK18QRegularExpression6QFlagsIN2Qt18SplitBehaviorFlagsEE(
    const QString *self,
    const QRegularExpression *sep,
    int behavior) {
  return new QList<QString>(
      self->split(
          *sep,
          QFlags<Qt::SplitBehaviorFlags>::fromInt(behavior)));
}
#endif  // !defined(QT_NO_REGULAREXPRESSION)

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

//  const ushort *QString::utf16() const
extern "C" Q_DECL_EXPORT
const ushort *ritual_ZNK7QString5utf16Ev(const QString *self) {
  return self->utf16();
}

//  QString QString::nullTerminated() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNKR7QString14nullTerminatedEv(const QString *self) {
  return new QString(self->nullTerminated());
}

//  QString &QString::nullTerminate()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString13nullTerminateEv(QString *self) {
  return &(self->nullTerminate());
}

#if !defined(Q_QDOC)
//  QByteArray QString::toLatin1() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR7QString8toLatin1Ev(const QString *self) {
  return new QByteArray(self->toLatin1());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QByteArray QString::toUtf8() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR7QString6toUtf8Ev(const QString *self) {
  return new QByteArray(self->toUtf8());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QByteArray QString::toLocal8Bit() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR7QString11toLocal8BitEv(const QString *self) {
  return new QByteArray(self->toLocal8Bit());
}
#endif  // !defined(Q_QDOC)

//  QList<uint> QString::toUcs4() const
extern "C" Q_DECL_EXPORT
QList<uint> *ritual_ZNK7QString6toUcs4Ev(const QString *self) {
  return new QList<uint>(self->toUcs4());
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

//  QString QString::fromUtf16(const char16_t *a0, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString9fromUtf16EPKDsx(
    const char16_t *a0,
    qsizetype size) {
  return new QString(QString::fromUtf16(a0, size));
}

//  QString QString::fromUcs4(const char32_t *a0, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8fromUcs4EPKDix(
    const char32_t *a0,
    qsizetype size) {
  return new QString(QString::fromUcs4(a0, size));
}

//  QString QString::fromRawData(const char16_t *unicode, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString11fromRawDataEPKDsx(
    const char16_t *unicode,
    qsizetype size) {
  return new QString(QString::fromRawData(unicode, size));
}

//  QString QString::fromRawData(const QChar *a0, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString11fromRawDataEPK5QCharx(
    const QChar *a0,
    qsizetype size) {
  return new QString(QString::fromRawData(a0, size));
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QString QString::fromUtf16(const ushort *str, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString9fromUtf16EPKtx(
    const ushort *str,
    qsizetype size) {
  return new QString(QString::fromUtf16(str, size));
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  QString QString::fromUcs4(const uint *str, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8fromUcs4EPKjx(const uint *str, qsizetype size) {
  return new QString(QString::fromUcs4(str, size));
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  qsizetype QString::toWCharArray(wchar_t *array) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString12toWCharArrayEPw(
    const QString *self,
    wchar_t *array) {
  return self->toWCharArray(array);
}

//  QString QString::fromWCharArray(const wchar_t *string, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14fromWCharArrayEPKwx(
    const wchar_t *string,
    qsizetype size) {
  return new QString(QString::fromWCharArray(string, size));
}

//  QString &QString::setRawData(const QChar *unicode, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString10setRawDataEPK5QCharx(
    QString *self,
    const QChar *unicode,
    qsizetype size) {
  return &(self->setRawData(unicode, size));
}

//  QString &QString::setUnicode(const QChar *unicode, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString10setUnicodeEPK5QCharx(
    QString *self,
    const QChar *unicode,
    qsizetype size) {
  return &(self->setUnicode(unicode, size));
}

//  QString &QString::setUtf16(const char16_t *utf16, qsizetype size)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8setUtf16EPKDsx(
    QString *self,
    const char16_t *utf16,
    qsizetype size) {
  return &(self->setUtf16(utf16, size));
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

//  QString &QString::setNum(short a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEsi(QString *self, short a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(ushort a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEti(QString *self, ushort a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(int a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEii(QString *self, int a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(uint a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEji(QString *self, uint a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(long a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEli(QString *self, long a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(ulong a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEmi(QString *self, ulong a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(qlonglong a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumExi(QString *self, qlonglong a0, int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(qulonglong a0, int base)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEyi(
    QString *self,
    qulonglong a0,
    int base) {
  return &(self->setNum(a0, base));
}

//  QString &QString::setNum(float a0, char format, int precision)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEfci(
    QString *self,
    float a0,
    char format,
    int precision) {
  return &(self->setNum(a0, format, precision));
}

//  QString &QString::setNum(double a0, char format, int precision)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6setNumEdci(
    QString *self,
    double a0,
    char format,
    int precision) {
  return &(self->setNum(a0, format, precision));
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

//  bool operator==(const QString &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringS1_(const QString *lhs, const QString *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QString &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringS1_(const QString *lhs, const QString *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QString &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringS1_(const QString *lhs, const QString *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QString &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringS1_(const QString *lhs, const QString *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QString &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringS1_(const QString *lhs, const QString *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QString &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringS1_(const QString *lhs, const QString *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QString &lhs, const QLatin1StringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRK13QLatin1String(
    const QString *lhs,
    const QLatin1String *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QString &lhs, const QLatin1StringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRK13QLatin1String(
    const QString *lhs,
    const QLatin1String *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QString &lhs, const QLatin1StringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRK13QLatin1String(
    const QString *lhs,
    const QLatin1String *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QString &lhs, const QLatin1StringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRK13QLatin1String(
    const QString *lhs,
    const QLatin1String *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QString &lhs, const QLatin1StringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRK13QLatin1String(
    const QString *lhs,
    const QLatin1String *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QString &lhs, const QLatin1StringView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRK13QLatin1String(
    const QString *lhs,
    const QLatin1String *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QLatin1StringView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QLatin1StringRK7QString(
    const QLatin1String *lhs,
    const QString *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QLatin1StringView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QLatin1StringRK7QString(
    const QLatin1String *lhs,
    const QString *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QLatin1StringView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK13QLatin1StringRK7QString(
    const QLatin1String *lhs,
    const QString *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QLatin1StringView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK13QLatin1StringRK7QString(
    const QLatin1String *lhs,
    const QString *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QLatin1StringView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK13QLatin1StringRK7QString(
    const QLatin1String *lhs,
    const QString *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QLatin1StringView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK13QLatin1StringRK7QString(
    const QLatin1String *lhs,
    const QString *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QString &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRKDn(const QString *lhs) {
  return operator==(*lhs, nullptr);
}

//  bool operator!=(const QString &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRKDn(const QString *lhs) {
  return operator!=(*lhs, nullptr);
}

//  bool operator<(const QString &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRKDn(const QString *lhs) {
  return operator<(*lhs, nullptr);
}

//  bool operator>(const QString &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRKDn(const QString *lhs) {
  return operator>(*lhs, nullptr);
}

//  bool operator<=(const QString &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRKDn(const QString *lhs) {
  return operator<=(*lhs, nullptr);
}

//  bool operator>=(const QString &lhs, const std::nullptr_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRKDn(const QString *lhs) {
  return operator>=(*lhs, nullptr);
}

//  bool operator==(const std::nullptr_t &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKDnRK7QString(const QString *rhs) {
  return operator==(nullptr, *rhs);
}

//  bool operator!=(const std::nullptr_t &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKDnRK7QString(const QString *rhs) {
  return operator!=(nullptr, *rhs);
}

//  bool operator<(const std::nullptr_t &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKDnRK7QString(const QString *rhs) {
  return operator<(nullptr, *rhs);
}

//  bool operator>(const std::nullptr_t &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKDnRK7QString(const QString *rhs) {
  return operator>(nullptr, *rhs);
}

//  bool operator<=(const std::nullptr_t &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKDnRK7QString(const QString *rhs) {
  return operator<=(nullptr, *rhs);
}

//  bool operator>=(const std::nullptr_t &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKDnRK7QString(const QString *rhs) {
  return operator>=(nullptr, *rhs);
}

//  bool operator==(const QString &lhs, const char16_t *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRKPKDs(
    const QString *lhs,
    const char16_t *const *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QString &lhs, const char16_t *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRKPKDs(
    const QString *lhs,
    const char16_t *const *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QString &lhs, const char16_t *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRKPKDs(
    const QString *lhs,
    const char16_t *const *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QString &lhs, const char16_t *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRKPKDs(
    const QString *lhs,
    const char16_t *const *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QString &lhs, const char16_t *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRKPKDs(
    const QString *lhs,
    const char16_t *const *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QString &lhs, const char16_t *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRKPKDs(
    const QString *lhs,
    const char16_t *const *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const char16_t *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKPKDsRK7QString(
    const char16_t *const *lhs,
    const QString *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const char16_t *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKPKDsRK7QString(
    const char16_t *const *lhs,
    const QString *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const char16_t *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKPKDsRK7QString(
    const char16_t *const *lhs,
    const QString *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const char16_t *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKPKDsRK7QString(
    const char16_t *const *lhs,
    const QString *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const char16_t *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKPKDsRK7QString(
    const char16_t *const *lhs,
    const QString *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const char16_t *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKPKDsRK7QString(
    const char16_t *const *lhs,
    const QString *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QString &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRK5QChar(const QString *lhs, const QChar *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QString &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRK5QChar(const QString *lhs, const QChar *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QString &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRK5QChar(const QString *lhs, const QChar *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QString &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRK5QChar(const QString *lhs, const QChar *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QString &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRK5QChar(const QString *lhs, const QChar *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QString &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRK5QChar(const QString *lhs, const QChar *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QChar &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharRK7QString(const QChar *lhs, const QString *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QChar &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharRK7QString(const QChar *lhs, const QString *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QChar &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharRK7QString(const QChar *lhs, const QString *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QChar &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharRK7QString(const QChar *lhs, const QString *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QChar &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharRK7QString(const QChar *lhs, const QString *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QChar &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharRK7QString(const QChar *lhs, const QString *rhs) {
  return operator>=(*lhs, *rhs);
}

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString::QString(const char *ch)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1EPKc(const char *ch) {
  return new QString(ch);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString::QString(const QByteArray &a)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1ERK10QByteArray(const QByteArray *a) {
  return new QString(*a);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::operator=(const char *ch)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringaSEPKc(QString *self, const char *ch) {
  return &(self->operator=(ch));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::operator=(const QByteArray &a)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringaSERK10QByteArray(
    QString *self,
    const QByteArray *a) {
  return &(self->operator=(*a));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::prepend(const char *s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependEPKc(QString *self, const char *s) {
  return &(self->prepend(s));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::prepend(const QByteArray &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString7prependERK10QByteArray(
    QString *self,
    const QByteArray *s) {
  return &(self->prepend(*s));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::append(const char *s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendEPKc(QString *self, const char *s) {
  return &(self->append(s));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::append(const QByteArray &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6appendERK10QByteArray(
    QString *self,
    const QByteArray *s) {
  return &(self->append(*s));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::insert(qsizetype i, const char *s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertExPKc(
    QString *self,
    qsizetype i,
    const char *s) {
  return &(self->insert(i, s));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::insert(qsizetype i, const QByteArray &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString6insertExRK10QByteArray(
    QString *self,
    qsizetype i,
    const QByteArray *s) {
  return &(self->insert(i, *s));
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::operator+=(const char *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLEPKc(QString *self, const char *s) {
  self->operator+=(s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  QString &QString::operator+=(const QByteArray &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QStringpLERK10QByteArray(QString *self, const QByteArray *s) {
  self->operator+=(*s);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const QString &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const QString &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const QString &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const QString &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const QString &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const QString &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRK14QByteArrayView(
    const QString *lhs,
    const QByteArrayView *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const QByteArrayView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewRK7QString(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const QByteArrayView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewRK7QString(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const QByteArrayView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewRK7QString(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const QByteArrayView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewRK7QString(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const QByteArrayView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewRK7QString(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const QByteArrayView &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewRK7QString(
    const QByteArrayView *lhs,
    const QString *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const QString &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const QString &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const QString &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const QString &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const QString &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const QString &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRK10QByteArray(
    const QString *lhs,
    const QByteArray *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const QByteArray &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QByteArrayRK7QString(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const QByteArray &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QByteArrayRK7QString(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const QByteArray &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QByteArrayRK7QString(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const QByteArray &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QByteArrayRK7QString(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const QByteArray &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QByteArrayRK7QString(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const QByteArray &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QByteArrayRK7QString(
    const QByteArray *lhs,
    const QString *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const QString &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QStringRKPKc(const QString *lhs, const char *const *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const QString &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QStringRKPKc(const QString *lhs, const char *const *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const QString &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK7QStringRKPKc(const QString *lhs, const char *const *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const QString &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK7QStringRKPKc(const QString *lhs, const char *const *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const QString &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK7QStringRKPKc(const QString *lhs, const char *const *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const QString &lhs, const char *const &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK7QStringRKPKc(const QString *lhs, const char *const *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator==(const char *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKPKcRK7QString(const char *const *lhs, const QString *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator!=(const char *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKPKcRK7QString(const char *const *lhs, const QString *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<(const char *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKPKcRK7QString(const char *const *lhs, const QString *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>(const char *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKPKcRK7QString(const char *const *lhs, const QString *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator<=(const char *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKPKcRK7QString(const char *const *lhs, const QString *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
#if !(QT_CORE_REMOVED_SINCE(6, 8))
//  bool operator>=(const char *const &lhs, const QString &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKPKcRK7QString(const char *const *lhs, const QString *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !(QT_CORE_REMOVED_SINCE(6, 8))
#endif

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

//  reverse_iterator QString::rbegin()
extern "C" Q_DECL_EXPORT
QString::reverse_iterator *ritual_ZN7QString6rbeginEv(QString *self) {
  return new QString::reverse_iterator(self->rbegin());
}

//  reverse_iterator QString::rend()
extern "C" Q_DECL_EXPORT
QString::reverse_iterator *ritual_ZN7QString4rendEv(QString *self) {
  return new QString::reverse_iterator(self->rend());
}

//  const_reverse_iterator QString::rbegin() const
extern "C" Q_DECL_EXPORT
QString::const_reverse_iterator *ritual_ZNK7QString6rbeginEv(
    const QString *self) {
  return new QString::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator QString::rend() const
extern "C" Q_DECL_EXPORT
QString::const_reverse_iterator *ritual_ZNK7QString4rendEv(
    const QString *self) {
  return new QString::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator QString::crbegin() const
extern "C" Q_DECL_EXPORT
QString::const_reverse_iterator *ritual_ZNK7QString7crbeginEv(
    const QString *self) {
  return new QString::const_reverse_iterator(self->crbegin());
}

//  const_reverse_iterator QString::crend() const
extern "C" Q_DECL_EXPORT
QString::const_reverse_iterator *ritual_ZNK7QString5crendEv(
    const QString *self) {
  return new QString::const_reverse_iterator(self->crend());
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

//  QString QString::fromStdString(const std::string &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString13fromStdStringERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE(
    const std::string *s) {
  return new QString(QString::fromStdString(*s));
}

//  std::string QString::toStdString() const
extern "C" Q_DECL_EXPORT
std::string *ritual_ZNK7QString11toStdStringB5cxx11Ev(const QString *self) {
  return new std::string(self->toStdString());
}

//  QString QString::fromStdWString(const std::wstring &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14fromStdWStringERKNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEEE(
    const std::wstring *s) {
  return new QString(QString::fromStdWString(*s));
}

//  std::wstring QString::toStdWString() const
extern "C" Q_DECL_EXPORT
std::wstring *ritual_ZNK7QString12toStdWStringB5cxx11Ev(
    const QString *self) {
  return new std::wstring(self->toStdWString());
}

//  QString QString::fromStdU16String(const std::u16string &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString16fromStdU16StringERKNSt7__cxx1112basic_stringIDsSt11char_traitsIDsESaIDsEEE(
    const std::u16string *s) {
  return new QString(QString::fromStdU16String(*s));
}

//  std::u16string QString::toStdU16String() const
extern "C" Q_DECL_EXPORT
std::u16string *ritual_ZNK7QString14toStdU16StringB5cxx11Ev(
    const QString *self) {
  return new std::u16string(self->toStdU16String());
}

//  QString QString::fromStdU32String(const std::u32string &s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString16fromStdU32StringERKNSt7__cxx1112basic_stringIDiSt11char_traitsIDiESaIDiEEE(
    const std::u32string *s) {
  return new QString(QString::fromStdU32String(*s));
}

//  std::u32string QString::toStdU32String() const
extern "C" Q_DECL_EXPORT
std::u32string *ritual_ZNK7QString14toStdU32StringB5cxx11Ev(
    const QString *self) {
  return new std::u32string(self->toStdU32String());
}

//  std::u16string_view QString::operator basic_string_view() const
extern "C" Q_DECL_EXPORT
std::u16string_view *ritual_ZNK7QStringcvSt17basic_string_viewIDsSt11char_traitsIDsEEEv(
    const QString *self) {
  return new std::u16string_view(self->operator std::u16string_view());
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

//  QString::QString(DataPointer &&dd)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QStringC1EO17QArrayDataPointerIDsE(
    QString::DataPointer *dd) {
  return new QString(std::move(*dd));
}

//  void QString::reallocData(qsizetype alloc, QArrayData::AllocationOption
//      option)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString11reallocDataExN10QArrayData16AllocationOptionE(
    QString *self,
    qsizetype alloc,
    QArrayData::AllocationOption option) {
  self->reallocData(alloc, option);
}

//  void QString::reallocGrowData(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QString15reallocGrowDataEx(QString *self, qsizetype n) {
  self->reallocGrowData(n);
}

//  QString &QString::assign_helper(const char32_t *data, qsizetype len)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString13assign_helperEPKDix(
    QString *self,
    const char32_t *data,
    qsizetype len) {
  return &(self->assign_helper(data, len));
}

//  int QString::compare_helper(const QChar *data1, qsizetype length1, const
//      QChar *data2, qsizetype length2, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString14compare_helperEPK5QCharxS2_xN2Qt15CaseSensitivityE(
    const QChar *data1,
    qsizetype length1,
    const QChar *data2,
    qsizetype length2,
    Qt::CaseSensitivity cs) {
  return QString::compare_helper(data1, length1, data2, length2, cs);
}

//  int QString::compare_helper(const QChar *data1, qsizetype length1, const
//      char *data2, qsizetype length2, Qt::CaseSensitivity cs)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString14compare_helperEPK5QCharxPKcxN2Qt15CaseSensitivityE(
    const QChar *data1,
    qsizetype length1,
    const char *data2,
    qsizetype length2,
    Qt::CaseSensitivity cs) {
  return QString::compare_helper(data1, length1, data2, length2, cs);
}

//  int QString::localeAwareCompare_helper(const QChar *data1, qsizetype
//      length1, const QChar *data2, qsizetype length2)
extern "C" Q_DECL_EXPORT
int ritual_ZN7QString25localeAwareCompare_helperEPK5QCharxS2_x(
    const QChar *data1,
    qsizetype length1,
    const QChar *data2,
    qsizetype length2) {
  return QString::localeAwareCompare_helper(data1, length1, data2, length2);
}

//  QString QString::sliced_helper(QString &str, qsizetype pos, qsizetype n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString13sliced_helperERS_xx(
    QString *str,
    qsizetype pos,
    qsizetype n) {
  return new QString(QString::sliced_helper(*str, pos, n));
}

//  QString QString::toLower_helper(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14toLower_helperERKS_(const QString *str) {
  return new QString(QString::toLower_helper(*str));
}

//  QString QString::toLower_helper(QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14toLower_helperERS_(QString *str) {
  return new QString(QString::toLower_helper(*str));
}

//  QString QString::toUpper_helper(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14toUpper_helperERKS_(const QString *str) {
  return new QString(QString::toUpper_helper(*str));
}

//  QString QString::toUpper_helper(QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14toUpper_helperERS_(QString *str) {
  return new QString(QString::toUpper_helper(*str));
}

//  QString QString::toCaseFolded_helper(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString19toCaseFolded_helperERKS_(const QString *str) {
  return new QString(QString::toCaseFolded_helper(*str));
}

//  QString QString::toCaseFolded_helper(QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString19toCaseFolded_helperERS_(QString *str) {
  return new QString(QString::toCaseFolded_helper(*str));
}

//  QString QString::trimmed_helper(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14trimmed_helperERKS_(const QString *str) {
  return new QString(QString::trimmed_helper(*str));
}

//  QString QString::trimmed_helper(QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString14trimmed_helperERS_(QString *str) {
  return new QString(QString::trimmed_helper(*str));
}

//  QString QString::simplified_helper(const QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString17simplified_helperERKS_(const QString *str) {
  return new QString(QString::simplified_helper(*str));
}

//  QString QString::simplified_helper(QString &str)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString17simplified_helperERS_(QString *str) {
  return new QString(QString::simplified_helper(*str));
}

//  QByteArray QString::toLatin1_helper(const QString &a0)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QString15toLatin1_helperERKS_(const QString *a0) {
  return new QByteArray(QString::toLatin1_helper(*a0));
}

//  QByteArray QString::toLatin1_helper_inplace(QString &a0)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QString23toLatin1_helper_inplaceERS_(QString *a0) {
  return new QByteArray(QString::toLatin1_helper_inplace(*a0));
}

//  QByteArray QString::toUtf8_helper(const QString &a0)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QString13toUtf8_helperERKS_(const QString *a0) {
  return new QByteArray(QString::toUtf8_helper(*a0));
}

//  QByteArray QString::toLocal8Bit_helper(const QChar *data, qsizetype size)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN7QString18toLocal8Bit_helperEPK5QCharx(
    const QChar *data,
    qsizetype size) {
  return new QByteArray(QString::toLocal8Bit_helper(data, size));
}

//  qsizetype QString::toUcs4_helper(const char16_t *uc, qsizetype length,
//      char32_t *out)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN7QString13toUcs4_helperEPKDsxPDi(
    const char16_t *uc,
    qsizetype length,
    char32_t *out) {
  return QString::toUcs4_helper(uc, length, out);
}

//  qlonglong QString::toIntegral_helper(QStringView string, bool *ok, int
//      base)
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZN7QString17toIntegral_helperE11QStringViewPbi(
    const QString *string,
    bool *ok,
    int base) {
  return QString::toIntegral_helper(QStringView(*string), ok, base);
}

//  qulonglong QString::toIntegral_helper(QStringView string, bool *ok, uint
//      base)
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZN7QString17toIntegral_helperE11QStringViewPbj(
    const QString *string,
    bool *ok,
    uint base) {
  return QString::toIntegral_helper(QStringView(*string), ok, base);
}

//  void QString::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QString6verifyExx(
    const QString *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}

//  DataPointer &QString::data_ptr()
extern "C" Q_DECL_EXPORT
QString::DataPointer *ritual_ZN7QString8data_ptrEv(QString *self) {
  return &(self->data_ptr());
}

//  const DataPointer &QString::data_ptr() const
extern "C" Q_DECL_EXPORT
const QString::DataPointer *ritual_ZNK7QString8data_ptrEv(
    const QString *self) {
  return &(self->data_ptr());
}

//  a QList<uint> a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__QList_uint(QList<uint> *self) {
  delete self;
}

//  a QString::reverse_iterator a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__QString_reverse_iterator(
    QString::reverse_iterator *self) {
  delete self;
}

//  a QString::const_reverse_iterator a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__QString_const_reverse_iterator(
    QString::const_reverse_iterator *self) {
  delete self;
}

//  a std::string a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__std_string(std::string *self) {
  delete self;
}

//  a std::wstring a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__std_wstring(std::wstring *self) {
  delete self;
}

//  a std::u16string a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__std_u16string(std::u16string *self) {
  delete self;
}

//  a std::u32string a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__std_u32string(std::u32string *self) {
  delete self;
}

//  a std::u16string_view a ritual of QString gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QString__std_u16string_view(std::u16string_view *self) {
  delete self;
}

//  static QString QString::asprintf(const char *format, ...)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QString8asprintfEPKcz(const char *text) {
  return new QString(QString::asprintf("%s", text));
}

//  QString QString::arg<int>(int a, int fieldWidth, int base, QChar
//      fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString3argIiLb1EEES_T_ii5QChar(
    const QString *self,
    int a,
    int fieldWidth,
    int base,
    const QChar *fillChar) {
  return new QString(self->arg<int>(a, fieldWidth, base, *fillChar));
}

//  QString QString::arg<bool>(bool a, int fieldWidth, int base, QChar
//      fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString3argIbLb1EEES_T_ii5QChar(
    const QString *self,
    bool a,
    int fieldWidth,
    int base,
    const QChar *fillChar) {
  return new QString(self->arg<bool>(a, fieldWidth, base, *fillChar));
}

//  QString QString::arg<double>(double a, int fieldWidth, char format,
//      int precision, QChar fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString3argIdLb1EEES_T_ici5QChar(
    const QString *self,
    double a,
    int fieldWidth,
    char format,
    int precision,
    const QChar *fillChar) {
  return new QString(
      self->arg<double>(a, fieldWidth, format, precision, *fillChar));
}

//  QString QString::arg<QString>(const QString &a, int fieldWidth,
//      QChar fillChar) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK7QString3argIS_Lb1EEES_RKT_i5QChar(
    const QString *self,
    const QString *a,
    int fieldWidth,
    const QChar *fillChar) {
  return new QString(self->arg<QString>(*a, fieldWidth, *fillChar));
}

#if QT_CONFIG(regularexpression)
//  qsizetype QString::lastIndexOf<QRegularExpressionMatch>(const
//      QRegularExpression &re, QRegularExpressionMatch *rmatch) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK7QString11lastIndexOfI23QRegularExpressionMatchLb0EEExRK18QRegularExpressionPT_(
    const QString *self,
    const QRegularExpression *re,
    QRegularExpressionMatch *rmatch) {
  return self->lastIndexOf<QRegularExpressionMatch>(*re, rmatch);
}
#endif  // QT_CONFIG(regularexpression)
