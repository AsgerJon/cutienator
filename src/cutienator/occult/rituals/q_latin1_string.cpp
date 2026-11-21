//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qlatin1stringview.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtCore/qstringview.h>

//  QLatin1String::QLatin1String()
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN13QLatin1StringC1Ev() {
  return new QLatin1String();
}

//  QLatin1String::QLatin1String(const char *s)
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN13QLatin1StringC1EPKc(const char *s) {
  return new QLatin1String(s);
}

//  QLatin1String::QLatin1String(const char *f, const char *l)
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN13QLatin1StringC1EPKcS1_(
    const char *f,
    const char *l) {
  return new QLatin1String(f, l);
}

//  QLatin1String::QLatin1String(const char *s, qsizetype sz)
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN13QLatin1StringC1EPKcx(const char *s, qsizetype sz) {
  return new QLatin1String(s, sz);
}

//  QLatin1String::QLatin1String(const QByteArray &s)
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN13QLatin1StringC1ERK10QByteArray(
    const QByteArray *s) {
  return new QLatin1String(*s);
}

//  QLatin1String::QLatin1String(QByteArrayView s)
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN13QLatin1StringC1E14QByteArrayView(
    const QByteArrayView *s) {
  return new QLatin1String(*s);
}

//  QString QLatin1String::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QLatin1String8toStringEv(const QLatin1String *self) {
  return new QString(self->toString());
}

//  QByteArray QLatin1String::toUtf8() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QLatin1String6toUtf8Ev(const QLatin1String *self) {
  return new QByteArray(self->toUtf8());
}

//  const char *QLatin1String::latin1() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QLatin1String6latin1Ev(const QLatin1String *self) {
  return self->latin1();
}

//  qsizetype QLatin1String::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String4sizeEv(const QLatin1String *self) {
  return self->size();
}

//  const char *QLatin1String::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QLatin1String4dataEv(const QLatin1String *self) {
  return self->data();
}

//  const char *QLatin1String::constData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QLatin1String9constDataEv(
    const QLatin1String *self) {
  return self->constData();
}

//  const char *QLatin1String::constBegin() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QLatin1String10constBeginEv(
    const QLatin1String *self) {
  return self->constBegin();
}

//  const char *QLatin1String::constEnd() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK13QLatin1String8constEndEv(const QLatin1String *self) {
  return self->constEnd();
}

//  QLatin1Char QLatin1String::first() const
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZNK13QLatin1String5firstEv(const QLatin1String *self) {
  return new QLatin1Char(self->first());
}

//  QLatin1Char QLatin1String::last() const
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZNK13QLatin1String4lastEv(const QLatin1String *self) {
  return new QLatin1Char(self->last());
}

//  qsizetype QLatin1String::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String6lengthEv(const QLatin1String *self) {
  return self->length();
}

//  bool QLatin1String::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String6isNullEv(const QLatin1String *self) {
  return self->isNull();
}

//  bool QLatin1String::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String7isEmptyEv(const QLatin1String *self) {
  return self->isEmpty();
}

//  bool QLatin1String::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String5emptyEv(const QLatin1String *self) {
  return self->empty();
}

//  QLatin1Char QLatin1String::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZNK13QLatin1String2atEx(
    const QLatin1String *self,
    qsizetype i) {
  return new QLatin1Char(self->at(i));
}

//  QLatin1Char QLatin1String::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZNK13QLatin1StringixEx(
    const QLatin1String *self,
    qsizetype i) {
  return new QLatin1Char(self->operator[](i));
}

//  QLatin1Char QLatin1String::front() const
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZNK13QLatin1String5frontEv(const QLatin1String *self) {
  return new QLatin1Char(self->front());
}

//  QLatin1Char QLatin1String::back() const
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZNK13QLatin1String4backEv(const QLatin1String *self) {
  return new QLatin1Char(self->back());
}

//  int QLatin1String::compare(QStringView other, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin1String7compareE11QStringViewN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *other,
    Qt::CaseSensitivity cs) {
  return self->compare(QStringView(*other), cs);
}

//  int QLatin1String::compare(QLatin1StringView other, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin1String7compareES_N2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *other,
    Qt::CaseSensitivity cs) {
  return self->compare(*other, cs);
}

//  int QLatin1String::compare(QChar c) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin1String7compareE5QChar(
    const QLatin1String *self,
    const QChar *c) {
  return self->compare(*c);
}

//  int QLatin1String::compare(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin1String7compareE5QCharN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->compare(*c, cs);
}

//  bool QLatin1String::startsWith(QStringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String10startsWithE11QStringViewN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(QStringView(*s), cs);
}

//  bool QLatin1String::startsWith(QLatin1StringView s, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String10startsWithES_N2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*s, cs);
}

//  bool QLatin1String::startsWith(QChar c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String10startsWithE5QChar(
    const QLatin1String *self,
    const QChar *c) {
  return self->startsWith(*c);
}

//  bool QLatin1String::startsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String10startsWithE5QCharN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->startsWith(*c, cs);
}

//  bool QLatin1String::endsWith(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8endsWithE11QStringViewN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(QStringView(*s), cs);
}

//  bool QLatin1String::endsWith(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8endsWithES_N2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*s, cs);
}

//  bool QLatin1String::endsWith(QChar c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8endsWithE5QChar(
    const QLatin1String *self,
    const QChar *c) {
  return self->endsWith(*c);
}

//  bool QLatin1String::endsWith(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8endsWithE5QCharN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->endsWith(*c, cs);
}

//  qsizetype QLatin1String::indexOf(QStringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String7indexOfE11QStringViewxN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(QStringView(*s), from, cs);
}

//  qsizetype QLatin1String::indexOf(QLatin1StringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String7indexOfES_xN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*s, from, cs);
}

//  qsizetype QLatin1String::indexOf(QChar c, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String7indexOfE5QCharx(
    const QLatin1String *self,
    const QChar *c,
    qsizetype from) {
  return self->indexOf(*c, from);
}

//  qsizetype QLatin1String::indexOf(QChar c, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String7indexOfE5QCharxN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->indexOf(*c, from, cs);
}

//  bool QLatin1String::contains(QStringView s, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8containsE11QStringViewN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->contains(QStringView(*s), cs);
}

//  bool QLatin1String::contains(QLatin1StringView s, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8containsES_N2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->contains(*s, cs);
}

//  bool QLatin1String::contains(QChar c, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLatin1String8containsE5QCharN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->contains(*c, cs);
}

//  qsizetype QLatin1String::lastIndexOf(QStringView s, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfE11QStringViewN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), cs);
}

//  qsizetype QLatin1String::lastIndexOf(QStringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfE11QStringViewxN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(QStringView(*s), from, cs);
}

//  qsizetype QLatin1String::lastIndexOf(QLatin1StringView s,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfES_N2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *s,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, cs);
}

//  qsizetype QLatin1String::lastIndexOf(QLatin1StringView s, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfES_xN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *s,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*s, from, cs);
}

//  qsizetype QLatin1String::lastIndexOf(QChar c) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfE5QChar(
    const QLatin1String *self,
    const QChar *c) {
  return self->lastIndexOf(*c);
}

//  qsizetype QLatin1String::lastIndexOf(QChar c, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfE5QCharN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*c, cs);
}

//  qsizetype QLatin1String::lastIndexOf(QChar c, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfE5QCharx(
    const QLatin1String *self,
    const QChar *c,
    qsizetype from) {
  return self->lastIndexOf(*c, from);
}

//  qsizetype QLatin1String::lastIndexOf(QChar c, qsizetype from,
//      Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String11lastIndexOfE5QCharxN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *c,
    qsizetype from,
    Qt::CaseSensitivity cs) {
  return self->lastIndexOf(*c, from, cs);
}

//  qsizetype QLatin1String::count(QStringView str, Qt::CaseSensitivity cs)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String5countE11QStringViewN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QString *str,
    Qt::CaseSensitivity cs) {
  return self->count(QStringView(*str), cs);
}

//  qsizetype QLatin1String::count(QLatin1StringView str, Qt::CaseSensitivity
//      cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String5countES_N2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QLatin1String *str,
    Qt::CaseSensitivity cs) {
  return self->count(*str, cs);
}

//  qsizetype QLatin1String::count(QChar ch, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String5countE5QCharN2Qt15CaseSensitivityE(
    const QLatin1String *self,
    const QChar *ch,
    Qt::CaseSensitivity cs) {
  return self->count(*ch, cs);
}

//  short QLatin1String::toShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK13QLatin1String7toShortEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toShort(ok, base);
}

//  ushort QLatin1String::toUShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK13QLatin1String8toUShortEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toUShort(ok, base);
}

//  int QLatin1String::toInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QLatin1String5toIntEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toInt(ok, base);
}

//  uint QLatin1String::toUInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QLatin1String6toUIntEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toUInt(ok, base);
}

//  long QLatin1String::toLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK13QLatin1String6toLongEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toLong(ok, base);
}

//  ulong QLatin1String::toULong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK13QLatin1String7toULongEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toULong(ok, base);
}

//  qlonglong QLatin1String::toLongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK13QLatin1String10toLongLongEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toLongLong(ok, base);
}

//  qulonglong QLatin1String::toULongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK13QLatin1String11toULongLongEPbi(
    const QLatin1String *self,
    bool *ok,
    int base) {
  return self->toULongLong(ok, base);
}

//  float QLatin1String::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QLatin1String7toFloatEPb(
    const QLatin1String *self,
    bool *ok) {
  return self->toFloat(ok);
}

//  double QLatin1String::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QLatin1String8toDoubleEPb(
    const QLatin1String *self,
    bool *ok) {
  return self->toDouble(ok);
}

//  qsizetype QLatin1String::max_size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QLatin1String8max_sizeEv(const QLatin1String *self) {
  return self->max_size();
}

//  qsizetype QLatin1String::maxSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13QLatin1String7maxSizeEv() {
  return QLatin1String::maxSize();
}

//  QLatin1StringView QLatin1String::mid(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String3midExx(
    const QLatin1String *self,
    qsizetype pos,
    qsizetype n) {
  return new QLatin1String(self->mid(pos, n));
}

//  QLatin1StringView QLatin1String::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String4leftEx(
    const QLatin1String *self,
    qsizetype n) {
  return new QLatin1String(self->left(n));
}

//  QLatin1StringView QLatin1String::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String5rightEx(
    const QLatin1String *self,
    qsizetype n) {
  return new QLatin1String(self->right(n));
}

//  QLatin1StringView QLatin1String::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String6slicedEx(
    const QLatin1String *self,
    qsizetype pos) {
  return new QLatin1String(self->sliced(pos));
}

//  QLatin1StringView QLatin1String::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String6slicedExx(
    const QLatin1String *self,
    qsizetype pos,
    qsizetype n) {
  return new QLatin1String(self->sliced(pos, n));
}

//  QLatin1StringView QLatin1String::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String5firstEx(
    const QLatin1String *self,
    qsizetype n) {
  return new QLatin1String(self->first(n));
}

//  QLatin1StringView QLatin1String::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String4lastEx(
    const QLatin1String *self,
    qsizetype n) {
  return new QLatin1String(self->last(n));
}

//  QLatin1StringView QLatin1String::chopped(qsizetype n) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String7choppedEx(
    const QLatin1String *self,
    qsizetype n) {
  return new QLatin1String(self->chopped(n));
}

//  void QLatin1String::chop(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLatin1String4chopEx(QLatin1String *self, qsizetype n) {
  self->chop(n);
}

//  void QLatin1String::truncate(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLatin1String8truncateEx(QLatin1String *self, qsizetype n) {
  self->truncate(n);
}

//  QLatin1StringView QLatin1String::trimmed() const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK13QLatin1String7trimmedEv(
    const QLatin1String *self) {
  return new QLatin1String(self->trimmed());
}

//  QLatin1String::~QLatin1String()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLatin1StringD1Ev(QLatin1String *self) {
  delete self;
}
