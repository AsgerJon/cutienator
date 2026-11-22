//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qchar.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QByteArray::QByteArray()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArrayC1Ev() {
  return new QByteArray();
}

//  QByteArray::QByteArray(const char *a0, qsizetype size)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArrayC1EPKcx(const char *a0, qsizetype size) {
  return new QByteArray(a0, size);
}

//  QByteArray::QByteArray(qsizetype size, char c)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArrayC1Exc(qsizetype size, char c) {
  return new QByteArray(size, c);
}

//  QByteArray::QByteArray(qsizetype size, Qt::Initialization a1)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArrayC1ExN2Qt14InitializationE(
    qsizetype size,
    Qt::Initialization a1) {
  return new QByteArray(size, a1);
}

//  QByteArray::QByteArray(QByteArrayView v)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArrayC1E14QByteArrayView(
    const QByteArrayView *v) {
  return new QByteArray(*v);
}

//  QByteArray::QByteArray(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArrayC1ERKS_(const QByteArray *a0) {
  return new QByteArray(*a0);
}

//  QByteArray::~QByteArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArrayD1Ev(QByteArray *self) {
  delete self;
}

//  bool QByteArray::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray7isEmptyEv(const QByteArray *self) {
  return self->isEmpty();
}

//  void QByteArray::resize(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray6resizeEx(QByteArray *self, qsizetype size) {
  self->resize(size);
}

//  void QByteArray::resize(qsizetype size, char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray6resizeExc(
    QByteArray *self,
    qsizetype size,
    char c) {
  self->resize(size, c);
}

//  void QByteArray::resizeForOverwrite(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray18resizeForOverwriteEx(
    QByteArray *self,
    qsizetype size) {
  self->resizeForOverwrite(size);
}

//  qsizetype QByteArray::capacity() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray8capacityEv(const QByteArray *self) {
  return self->capacity();
}

//  void QByteArray::reserve(qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray7reserveEx(QByteArray *self, qsizetype size) {
  self->reserve(size);
}

//  void QByteArray::squeeze()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray7squeezeEv(QByteArray *self) {
  self->squeeze();
}

//  const char *QByteArray::operator const char *() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK10QByteArraycvPKcEv(const QByteArray *self) {
  return self->operator const char *();
}

//  const char *QByteArray::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK10QByteArray4dataEv(const QByteArray *self) {
  return self->data();
}

//  const char *QByteArray::constData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK10QByteArray9constDataEv(const QByteArray *self) {
  return self->constData();
}

//  void QByteArray::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray6detachEv(QByteArray *self) {
  self->detach();
}

//  bool QByteArray::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray10isDetachedEv(const QByteArray *self) {
  return self->isDetached();
}

//  bool QByteArray::isSharedWith(const QByteArray &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray12isSharedWithERKS_(
    const QByteArray *self,
    const QByteArray *other) {
  return self->isSharedWith(*other);
}

//  void QByteArray::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray5clearEv(QByteArray *self) {
  self->clear();
}

//  char QByteArray::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
char ritual_ZNK10QByteArray2atEx(const QByteArray *self, qsizetype i) {
  return self->at(i);
}

//  char QByteArray::operator[](qsizetype i) const
extern "C" Q_DECL_EXPORT
char ritual_ZNK10QByteArrayixEx(const QByteArray *self, qsizetype i) {
  return self->operator[](i);
}

//  char QByteArray::front() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK10QByteArray5frontEv(const QByteArray *self) {
  return self->front();
}

//  char QByteArray::back() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK10QByteArray4backEv(const QByteArray *self) {
  return self->back();
}

//  qsizetype QByteArray::indexOf(char c, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray7indexOfEcx(
    const QByteArray *self,
    char c,
    qsizetype from) {
  return self->indexOf(c, from);
}

//  qsizetype QByteArray::indexOf(QByteArrayView bv, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray7indexOfE14QByteArrayViewx(
    const QByteArray *self,
    const QByteArrayView *bv,
    qsizetype from) {
  return self->indexOf(*bv, from);
}

//  qsizetype QByteArray::lastIndexOf(char c, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray11lastIndexOfEcx(
    const QByteArray *self,
    char c,
    qsizetype from) {
  return self->lastIndexOf(c, from);
}

//  qsizetype QByteArray::lastIndexOf(QByteArrayView bv) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray11lastIndexOfE14QByteArrayView(
    const QByteArray *self,
    const QByteArrayView *bv) {
  return self->lastIndexOf(*bv);
}

//  qsizetype QByteArray::lastIndexOf(QByteArrayView bv, qsizetype from)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray11lastIndexOfE14QByteArrayViewx(
    const QByteArray *self,
    const QByteArrayView *bv,
    qsizetype from) {
  return self->lastIndexOf(*bv, from);
}

//  bool QByteArray::contains(char c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray8containsEc(const QByteArray *self, char c) {
  return self->contains(c);
}

//  bool QByteArray::contains(QByteArrayView bv) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray8containsE14QByteArrayView(
    const QByteArray *self,
    const QByteArrayView *bv) {
  return self->contains(*bv);
}

//  qsizetype QByteArray::count(char c) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray5countEc(const QByteArray *self, char c) {
  return self->count(c);
}

//  qsizetype QByteArray::count(QByteArrayView bv) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray5countE14QByteArrayView(
    const QByteArray *self,
    const QByteArrayView *bv) {
  return self->count(*bv);
}

//  int QByteArray::compare(QByteArrayView a) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QByteArray7compareE14QByteArrayView(
    const QByteArray *self,
    const QByteArrayView *a) {
  return self->compare(*a);
}

//  int QByteArray::compare(QByteArrayView a, Qt::CaseSensitivity cs) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QByteArray7compareE14QByteArrayViewN2Qt15CaseSensitivityE(
    const QByteArray *self,
    const QByteArrayView *a,
    Qt::CaseSensitivity cs) {
  return self->compare(*a, cs);
}

//  QByteArray QByteArray::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray4leftEx(
    const QByteArray *self,
    qsizetype n) {
  return new QByteArray(self->left(n));
}

//  QByteArray QByteArray::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray5rightEx(
    const QByteArray *self,
    qsizetype n) {
  return new QByteArray(self->right(n));
}

//  QByteArray QByteArray::mid(qsizetype index, qsizetype len) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray3midExx(
    const QByteArray *self,
    qsizetype index,
    qsizetype len) {
  return new QByteArray(self->mid(index, len));
}

//  QByteArray QByteArray::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray5firstEx(
    const QByteArray *self,
    qsizetype n) {
  return new QByteArray(self->first(n));
}

//  QByteArray QByteArray::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray4lastEx(
    const QByteArray *self,
    qsizetype n) {
  return new QByteArray(self->last(n));
}

//  QByteArray QByteArray::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray6slicedEx(
    const QByteArray *self,
    qsizetype pos) {
  return new QByteArray(self->sliced(pos));
}

//  QByteArray QByteArray::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray6slicedExx(
    const QByteArray *self,
    qsizetype pos,
    qsizetype n) {
  return new QByteArray(self->sliced(pos, n));
}

//  QByteArray QByteArray::chopped(qsizetype len) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray7choppedEx(
    const QByteArray *self,
    qsizetype len) {
  return new QByteArray(self->chopped(len));
}

//  bool QByteArray::startsWith(QByteArrayView bv) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray10startsWithE14QByteArrayView(
    const QByteArray *self,
    const QByteArrayView *bv) {
  return self->startsWith(*bv);
}

//  bool QByteArray::startsWith(char c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray10startsWithEc(const QByteArray *self, char c) {
  return self->startsWith(c);
}

//  bool QByteArray::endsWith(char c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray8endsWithEc(const QByteArray *self, char c) {
  return self->endsWith(c);
}

//  bool QByteArray::endsWith(QByteArrayView bv) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray8endsWithE14QByteArrayView(
    const QByteArray *self,
    const QByteArrayView *bv) {
  return self->endsWith(*bv);
}

//  bool QByteArray::isUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray7isUpperEv(const QByteArray *self) {
  return self->isUpper();
}

//  bool QByteArray::isLower() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray7isLowerEv(const QByteArray *self) {
  return self->isLower();
}

//  bool QByteArray::isValidUtf8() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray11isValidUtf8Ev(const QByteArray *self) {
  return self->isValidUtf8();
}

//  void QByteArray::truncate(qsizetype pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray8truncateEx(QByteArray *self, qsizetype pos) {
  self->truncate(pos);
}

//  void QByteArray::chop(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray4chopEx(QByteArray *self, qsizetype n) {
  self->chop(n);
}

//  QByteArray QByteArray::toLower() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray7toLowerEv(const QByteArray *self) {
  return new QByteArray(self->toLower());
}

//  QByteArray QByteArray::toUpper() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray7toUpperEv(const QByteArray *self) {
  return new QByteArray(self->toUpper());
}

//  QByteArray QByteArray::trimmed() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray7trimmedEv(const QByteArray *self) {
  return new QByteArray(self->trimmed());
}

//  QByteArray QByteArray::simplified() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray10simplifiedEv(const QByteArray *self) {
  return new QByteArray(self->simplified());
}

//  QByteArray QByteArray::leftJustified(qsizetype width, char fill, bool
//      truncate) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QByteArray13leftJustifiedExcb(
    const QByteArray *self,
    qsizetype width,
    char fill,
    bool truncate) {
  return new QByteArray(self->leftJustified(width, fill, truncate));
}

//  QByteArray QByteArray::rightJustified(qsizetype width, char fill, bool
//      truncate) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QByteArray14rightJustifiedExcb(
    const QByteArray *self,
    qsizetype width,
    char fill,
    bool truncate) {
  return new QByteArray(self->rightJustified(width, fill, truncate));
}

//  QByteArray &QByteArray::operator+=(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArraypLEc(QByteArray *self, char c) {
  self->operator+=(c);
}

//  QByteArray &QByteArray::operator+=(const char *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArraypLEPKc(QByteArray *self, const char *s) {
  self->operator+=(s);
}

//  QByteArray &QByteArray::operator+=(const QByteArray &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArraypLERKS_(QByteArray *self, const QByteArray *a) {
  self->operator+=(*a);
}

//  QByteArray &QByteArray::operator+=(QByteArrayView a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArraypLE14QByteArrayView(
    QByteArray *self,
    const QByteArrayView *a) {
  self->operator+=(*a);
}

//  QList<QByteArray> QByteArray::split(char sep) const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK10QByteArray5splitEc(
    const QByteArray *self,
    char sep) {
  return new QList<QByteArray>(self->split(sep));
}

//  QByteArray QByteArray::repeated(qsizetype times) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QByteArray8repeatedEx(
    const QByteArray *self,
    qsizetype times) {
  return new QByteArray(self->repeated(times));
}

//  short QByteArray::toShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK10QByteArray7toShortEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toShort(ok, base);
}

//  ushort QByteArray::toUShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK10QByteArray8toUShortEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toUShort(ok, base);
}

//  int QByteArray::toInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QByteArray5toIntEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toInt(ok, base);
}

//  uint QByteArray::toUInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10QByteArray6toUIntEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toUInt(ok, base);
}

//  long QByteArray::toLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK10QByteArray6toLongEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toLong(ok, base);
}

//  ulong QByteArray::toULong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK10QByteArray7toULongEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toULong(ok, base);
}

//  qlonglong QByteArray::toLongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK10QByteArray10toLongLongEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toLongLong(ok, base);
}

//  qulonglong QByteArray::toULongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK10QByteArray11toULongLongEPbi(
    const QByteArray *self,
    bool *ok,
    int base) {
  return self->toULongLong(ok, base);
}

//  float QByteArray::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QByteArray7toFloatEPb(const QByteArray *self, bool *ok) {
  return self->toFloat(ok);
}

//  double QByteArray::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QByteArray8toDoubleEPb(const QByteArray *self, bool *ok) {
  return self->toDouble(ok);
}

//  QByteArray QByteArray::toBase64(Base64Options options) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QByteArray8toBase64E6QFlagsINS_12Base64OptionEE(
    const QByteArray *self,
    int options) {
  return new QByteArray(
      self->toBase64(
          QFlags<QByteArray::Base64Option>::fromInt(options)));
}

//  QByteArray QByteArray::toHex(char separator) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QByteArray5toHexEc(
    const QByteArray *self,
    char separator) {
  return new QByteArray(self->toHex(separator));
}

//  QByteArray QByteArray::toPercentEncoding(const QByteArray &exclude, const
//      QByteArray &include, char percent) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK10QByteArray17toPercentEncodingERKS_S1_c(
    const QByteArray *self,
    const QByteArray *exclude,
    const QByteArray *include,
    char percent) {
  return new QByteArray(
      self->toPercentEncoding(
          *exclude,
          *include,
          percent));
}

//  QByteArray QByteArray::percentDecoded(char percent) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray14percentDecodedEc(
    const QByteArray *self,
    char percent) {
  return new QByteArray(self->percentDecoded(percent));
}

//  QByteArray QByteArray::number(int a0, int base)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberEii(int a0, int base) {
  return new QByteArray(QByteArray::number(a0, base));
}

//  QByteArray QByteArray::number(uint a0, int base)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberEji(uint a0, int base) {
  return new QByteArray(QByteArray::number(a0, base));
}

//  QByteArray QByteArray::number(long a0, int base)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberEli(long a0, int base) {
  return new QByteArray(QByteArray::number(a0, base));
}

//  QByteArray QByteArray::number(ulong a0, int base)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberEmi(ulong a0, int base) {
  return new QByteArray(QByteArray::number(a0, base));
}

//  QByteArray QByteArray::number(qlonglong a0, int base)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberExi(qlonglong a0, int base) {
  return new QByteArray(QByteArray::number(a0, base));
}

//  QByteArray QByteArray::number(qulonglong a0, int base)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberEyi(qulonglong a0, int base) {
  return new QByteArray(QByteArray::number(a0, base));
}

//  QByteArray QByteArray::number(double a0, char format, int precision)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray6numberEdci(
    double a0,
    char format,
    int precision) {
  return new QByteArray(QByteArray::number(a0, format, precision));
}

//  QByteArray QByteArray::fromRawData(const char *data, qsizetype size)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray11fromRawDataEPKcx(
    const char *data,
    qsizetype size) {
  return new QByteArray(QByteArray::fromRawData(data, size));
}

//  FromBase64Result QByteArray::fromBase64Encoding(const QByteArray &base64,
//      Base64Options options)
extern "C" Q_DECL_EXPORT
QByteArray::FromBase64Result *ritual_ZN10QByteArray18fromBase64EncodingERKS_6QFlagsINS_12Base64OptionEE(
    const QByteArray *base64,
    int options) {
  return new QByteArray::FromBase64Result(
      QByteArray::fromBase64Encoding(
          *base64,
          QFlags<QByteArray::Base64Option>::fromInt(options)));
}

//  QByteArray QByteArray::fromBase64(const QByteArray &base64, Base64Options
//      options)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray10fromBase64ERKS_6QFlagsINS_12Base64OptionEE(
    const QByteArray *base64,
    int options) {
  return new QByteArray(
      QByteArray::fromBase64(
          *base64,
          QFlags<QByteArray::Base64Option>::fromInt(options)));
}

//  QByteArray QByteArray::fromHex(const QByteArray &hexEncoded)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray7fromHexERKS_(
    const QByteArray *hexEncoded) {
  return new QByteArray(QByteArray::fromHex(*hexEncoded));
}

//  QByteArray QByteArray::fromPercentEncoding(const QByteArray &pctEncoded,
//      char percent)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN10QByteArray19fromPercentEncodingERKS_c(
    const QByteArray *pctEncoded,
    char percent) {
  return new QByteArray(
      QByteArray::fromPercentEncoding(
          *pctEncoded,
          percent));
}

//  const_iterator QByteArray::begin() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK10QByteArray5beginEv(
    const QByteArray *self) {
  return self->begin();
}

//  const_iterator QByteArray::cbegin() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK10QByteArray6cbeginEv(
    const QByteArray *self) {
  return self->cbegin();
}

//  const_iterator QByteArray::constBegin() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK10QByteArray10constBeginEv(
    const QByteArray *self) {
  return self->constBegin();
}

//  const_iterator QByteArray::end() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK10QByteArray3endEv(
    const QByteArray *self) {
  return self->end();
}

//  const_iterator QByteArray::cend() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK10QByteArray4cendEv(
    const QByteArray *self) {
  return self->cend();
}

//  const_iterator QByteArray::constEnd() const
extern "C" Q_DECL_EXPORT
QByteArray::const_iterator ritual_ZNK10QByteArray8constEndEv(
    const QByteArray *self) {
  return self->constEnd();
}

//  void QByteArray::push_back(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray9push_backEc(QByteArray *self, char c) {
  self->push_back(c);
}

//  void QByteArray::push_back(const char *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray9push_backEPKc(QByteArray *self, const char *s) {
  self->push_back(s);
}

//  void QByteArray::push_back(const QByteArray &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray9push_backERKS_(
    QByteArray *self,
    const QByteArray *a) {
  self->push_back(*a);
}

//  void QByteArray::push_back(QByteArrayView a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray9push_backE14QByteArrayView(
    QByteArray *self,
    const QByteArrayView *a) {
  self->push_back(*a);
}

//  void QByteArray::push_front(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray10push_frontEc(QByteArray *self, char c) {
  self->push_front(c);
}

//  void QByteArray::push_front(const char *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray10push_frontEPKc(QByteArray *self, const char *c) {
  self->push_front(c);
}

//  void QByteArray::push_front(const QByteArray &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray10push_frontERKS_(
    QByteArray *self,
    const QByteArray *a) {
  self->push_front(*a);
}

//  void QByteArray::push_front(QByteArrayView a)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray10push_frontE14QByteArrayView(
    QByteArray *self,
    const QByteArrayView *a) {
  self->push_front(*a);
}

//  void QByteArray::shrink_to_fit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QByteArray13shrink_to_fitEv(QByteArray *self) {
  self->shrink_to_fit();
}

//  qsizetype QByteArray::max_size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray8max_sizeEv(const QByteArray *self) {
  return self->max_size();
}

//  qsizetype QByteArray::maxSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN10QByteArray7maxSizeEv() {
  return QByteArray::maxSize();
}

//  qsizetype QByteArray::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray4sizeEv(const QByteArray *self) {
  return self->size();
}

//  qsizetype QByteArray::count() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray5countEv(const QByteArray *self) {
  return self->count();
}

//  qsizetype QByteArray::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QByteArray6lengthEv(const QByteArray *self) {
  return self->length();
}

//  bool QByteArray::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QByteArray6isNullEv(const QByteArray *self) {
  return self->isNull();
}

//  QByteArray QByteArray::nullTerminated() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR10QByteArray14nullTerminatedEv(
    const QByteArray *self) {
  return new QByteArray(self->nullTerminated());
}

//  bool operator==(const QByteArray &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QByteArrayS1_(
    const QByteArray *lhs,
    const QByteArray *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QByteArray &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QByteArrayS1_(
    const QByteArray *lhs,
    const QByteArray *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QByteArray &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QByteArrayS1_(
    const QByteArray *lhs,
    const QByteArray *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QByteArray &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QByteArrayS1_(
    const QByteArray *lhs,
    const QByteArray *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QByteArray &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QByteArrayS1_(
    const QByteArray *lhs,
    const QByteArray *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QByteArray &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QByteArrayS1_(
    const QByteArray *lhs,
    const QByteArray *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QByteArray &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QByteArrayRKc(const QByteArray *lhs, char rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const QByteArray &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QByteArrayRKc(const QByteArray *lhs, char rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const QByteArray &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QByteArrayRKc(const QByteArray *lhs, char rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const QByteArray &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QByteArrayRKc(const QByteArray *lhs, char rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const QByteArray &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QByteArrayRKc(const QByteArray *lhs, char rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const QByteArray &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QByteArrayRKc(const QByteArray *lhs, char rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const char &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKcRK10QByteArray(char lhs, const QByteArray *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const char &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKcRK10QByteArray(char lhs, const QByteArray *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const char &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKcRK10QByteArray(char lhs, const QByteArray *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const char &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKcRK10QByteArray(char lhs, const QByteArray *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const char &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKcRK10QByteArray(char lhs, const QByteArray *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const char &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKcRK10QByteArray(char lhs, const QByteArray *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const QByteArray &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK10QByteArrayRK5QChar(
    const QByteArray *lhs,
    const QChar *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QByteArray &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK10QByteArrayRK5QChar(
    const QByteArray *lhs,
    const QChar *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QByteArray &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK10QByteArrayRK5QChar(
    const QByteArray *lhs,
    const QChar *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QByteArray &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK10QByteArrayRK5QChar(
    const QByteArray *lhs,
    const QChar *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QByteArray &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK10QByteArrayRK5QChar(
    const QByteArray *lhs,
    const QChar *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QByteArray &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK10QByteArrayRK5QChar(
    const QByteArray *lhs,
    const QChar *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QChar &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharRK10QByteArray(
    const QChar *lhs,
    const QByteArray *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QChar &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharRK10QByteArray(
    const QChar *lhs,
    const QByteArray *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QChar &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharRK10QByteArray(
    const QChar *lhs,
    const QByteArray *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QChar &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharRK10QByteArray(
    const QChar *lhs,
    const QByteArray *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QChar &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharRK10QByteArray(
    const QChar *lhs,
    const QByteArray *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QChar &lhs, const QByteArray &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharRK10QByteArray(
    const QChar *lhs,
    const QByteArray *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QList<QByteArray>::QList()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_list_make_QByteArray() {
  return new QList<QByteArray>();
}

//  void QList<QByteArray>::append(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QByteArray(
    QList<QByteArray> *self,
    const QByteArray *element) {
  self->append(*element);
}

//  qsizetype QList<QByteArray>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QByteArray(const QList<QByteArray> *self) {
  return self->size();
}

//  const QByteArray &QList<QByteArray>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_list_at_QByteArray(
    const QList<QByteArray> *self,
    long long index) {
  return new QByteArray(self->at(index));
}

//  QList<QByteArray>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QByteArray(QList<QByteArray> *self) {
  delete self;
}

//  QHash<int, QByteArray>: QHash<int, QByteArray>()
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_map_make_QHash_int_QByteArray() {
  return new QHash<int, QByteArray>();
}

//  QHash<int, QByteArray>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QHash_int_QByteArray(
    QHash<int, QByteArray> *self,
    int key,
    const QByteArray *value) {
  self->insert(key, *value);
}

//  QHash<int, QByteArray>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QHash_int_QByteArray(
    const QHash<int, QByteArray> *self) {
  return self->size();
}

//  QHash<int, QByteArray>: the key at a place
extern "C" Q_DECL_EXPORT
int ritual_map_key_QHash_int_QByteArray(
    const QHash<int, QByteArray> *self,
    long long index) {
  return *std::next(self->keyBegin(), index);
}

//  QHash<int, QByteArray>: the value at a place
extern "C" Q_DECL_EXPORT
QByteArray *ritual_map_value_QHash_int_QByteArray(
    const QHash<int, QByteArray> *self,
    long long index) {
  return new QByteArray(*std::next(self->constBegin(), index));
}

//  QHash<int, QByteArray>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QHash_int_QByteArray(
    const QHash<int, QByteArray> *self,
    int key) {
  return self->contains(key);
}

//  QHash<int, QByteArray>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_map_get_QHash_int_QByteArray(
    const QHash<int, QByteArray> *self,
    int key) {
  return new QByteArray(self->value(key));
}

//  QHash<int, QByteArray>: ~QHash()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QHash_int_QByteArray(QHash<int, QByteArray> *self) {
  delete self;
}
