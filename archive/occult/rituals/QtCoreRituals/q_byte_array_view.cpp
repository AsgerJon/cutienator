//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearrayview.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qchar.h>

//  qsizetype QByteArrayView::lengthHelperCharArray(const char *data, size_t
//      size)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QByteArrayView21lengthHelperCharArrayEPKcm(
    const char *data,
    size_t size) {
  return QByteArrayView::lengthHelperCharArray(data, size);
}

//  QByteArrayView::QByteArrayView()
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1Ev() {
  return new QByteArrayView();
}

//  QByteArray QByteArrayView::toByteArray() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QByteArrayView11toByteArrayEv(
    const QByteArrayView *self) {
  return new QByteArray(self->toByteArray());
}

//  qsizetype QByteArrayView::maxSize()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QByteArrayView7maxSizeEv() {
  return QByteArrayView::maxSize();
}

//  qsizetype QByteArrayView::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView4sizeEv(const QByteArrayView *self) {
  return self->size();
}

//  char QByteArrayView::operator[](qsizetype n) const
extern "C" Q_DECL_EXPORT
char ritual_ZNK14QByteArrayViewixEx(
    const QByteArrayView *self,
    qsizetype n) {
  return self->operator[](n);
}

//  char QByteArrayView::at(qsizetype n) const
extern "C" Q_DECL_EXPORT
char ritual_ZNK14QByteArrayView2atEx(
    const QByteArrayView *self,
    qsizetype n) {
  return self->at(n);
}

//  QByteArrayView QByteArrayView::first(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView5firstEx(
    const QByteArrayView *self,
    qsizetype n) {
  return new QByteArrayView(self->first(n));
}

//  QByteArrayView QByteArrayView::last(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView4lastEx(
    const QByteArrayView *self,
    qsizetype n) {
  return new QByteArrayView(self->last(n));
}

//  QByteArrayView QByteArrayView::sliced(qsizetype pos) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView6slicedEx(
    const QByteArrayView *self,
    qsizetype pos) {
  return new QByteArrayView(self->sliced(pos));
}

//  QByteArrayView QByteArrayView::sliced(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView6slicedExx(
    const QByteArrayView *self,
    qsizetype pos,
    qsizetype n) {
  return new QByteArrayView(self->sliced(pos, n));
}

//  QByteArrayView QByteArrayView::chopped(qsizetype len) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView7choppedEx(
    const QByteArrayView *self,
    qsizetype len) {
  return new QByteArrayView(self->chopped(len));
}

//  QByteArrayView QByteArrayView::left(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView4leftEx(
    const QByteArrayView *self,
    qsizetype n) {
  return new QByteArrayView(self->left(n));
}

//  QByteArrayView QByteArrayView::right(qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView5rightEx(
    const QByteArrayView *self,
    qsizetype n) {
  return new QByteArrayView(self->right(n));
}

//  QByteArrayView QByteArrayView::mid(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView3midExx(
    const QByteArrayView *self,
    qsizetype pos,
    qsizetype n) {
  return new QByteArrayView(self->mid(pos, n));
}

//  void QByteArrayView::truncate(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QByteArrayView8truncateEx(
    QByteArrayView *self,
    qsizetype n) {
  self->truncate(n);
}

//  void QByteArrayView::chop(qsizetype n)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QByteArrayView4chopEx(QByteArrayView *self, qsizetype n) {
  self->chop(n);
}

//  QByteArrayView QByteArrayView::trimmed() const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZNK14QByteArrayView7trimmedEv(
    const QByteArrayView *self) {
  return new QByteArrayView(self->trimmed());
}

//  short QByteArrayView::toShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
short ritual_ZNK14QByteArrayView7toShortEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toShort(ok, base);
}

//  ushort QByteArrayView::toUShort(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK14QByteArrayView8toUShortEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toUShort(ok, base);
}

//  int QByteArrayView::toInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QByteArrayView5toIntEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toInt(ok, base);
}

//  uint QByteArrayView::toUInt(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK14QByteArrayView6toUIntEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toUInt(ok, base);
}

//  long QByteArrayView::toLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
long ritual_ZNK14QByteArrayView6toLongEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toLong(ok, base);
}

//  ulong QByteArrayView::toULong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
ulong ritual_ZNK14QByteArrayView7toULongEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toULong(ok, base);
}

//  qlonglong QByteArrayView::toLongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qlonglong ritual_ZNK14QByteArrayView10toLongLongEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toLongLong(ok, base);
}

//  qulonglong QByteArrayView::toULongLong(bool *ok, int base) const
extern "C" Q_DECL_EXPORT
qulonglong ritual_ZNK14QByteArrayView11toULongLongEPbi(
    const QByteArrayView *self,
    bool *ok,
    int base) {
  return self->toULongLong(ok, base);
}

//  float QByteArrayView::toFloat(bool *ok) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QByteArrayView7toFloatEPb(
    const QByteArrayView *self,
    bool *ok) {
  return self->toFloat(ok);
}

//  double QByteArrayView::toDouble(bool *ok) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QByteArrayView8toDoubleEPb(
    const QByteArrayView *self,
    bool *ok) {
  return self->toDouble(ok);
}

//  bool QByteArrayView::startsWith(QByteArrayView other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView10startsWithES_(
    const QByteArrayView *self,
    const QByteArrayView *other) {
  return self->startsWith(*other);
}

//  bool QByteArrayView::startsWith(char c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView10startsWithEc(
    const QByteArrayView *self,
    char c) {
  return self->startsWith(c);
}

//  bool QByteArrayView::endsWith(QByteArrayView other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView8endsWithES_(
    const QByteArrayView *self,
    const QByteArrayView *other) {
  return self->endsWith(*other);
}

//  bool QByteArrayView::endsWith(char c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView8endsWithEc(
    const QByteArrayView *self,
    char c) {
  return self->endsWith(c);
}

//  qsizetype QByteArrayView::indexOf(QByteArrayView a, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView7indexOfES_x(
    const QByteArrayView *self,
    const QByteArrayView *a,
    qsizetype from) {
  return self->indexOf(*a, from);
}

//  qsizetype QByteArrayView::indexOf(char ch, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView7indexOfEcx(
    const QByteArrayView *self,
    char ch,
    qsizetype from) {
  return self->indexOf(ch, from);
}

//  bool QByteArrayView::contains(QByteArrayView a) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView8containsES_(
    const QByteArrayView *self,
    const QByteArrayView *a) {
  return self->contains(*a);
}

//  bool QByteArrayView::contains(char c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView8containsEc(
    const QByteArrayView *self,
    char c) {
  return self->contains(c);
}

//  qsizetype QByteArrayView::lastIndexOf(QByteArrayView a) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView11lastIndexOfES_(
    const QByteArrayView *self,
    const QByteArrayView *a) {
  return self->lastIndexOf(*a);
}

//  qsizetype QByteArrayView::lastIndexOf(QByteArrayView a, qsizetype from)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView11lastIndexOfES_x(
    const QByteArrayView *self,
    const QByteArrayView *a,
    qsizetype from) {
  return self->lastIndexOf(*a, from);
}

//  qsizetype QByteArrayView::lastIndexOf(char ch, qsizetype from) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView11lastIndexOfEcx(
    const QByteArrayView *self,
    char ch,
    qsizetype from) {
  return self->lastIndexOf(ch, from);
}

//  qsizetype QByteArrayView::count(QByteArrayView a) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView5countES_(
    const QByteArrayView *self,
    const QByteArrayView *a) {
  return self->count(*a);
}

//  qsizetype QByteArrayView::count(char ch) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView5countEc(
    const QByteArrayView *self,
    char ch) {
  return self->count(ch);
}

//  int QByteArrayView::compare(QByteArrayView a) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QByteArrayView7compareES_(
    const QByteArrayView *self,
    const QByteArrayView *a) {
  return self->compare(*a);
}

//  int QByteArrayView::compare(QByteArrayView a, Qt::CaseSensitivity a1)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QByteArrayView7compareES_N2Qt15CaseSensitivityE(
    const QByteArrayView *self,
    const QByteArrayView *a,
    Qt::CaseSensitivity a1) {
  return self->compare(*a, a1);
}

//  bool QByteArrayView::isValidUtf8() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView11isValidUtf8Ev(const QByteArrayView *self) {
  return self->isValidUtf8();
}

//  bool QByteArrayView::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView5emptyEv(const QByteArrayView *self) {
  return self->empty();
}

//  char QByteArrayView::front() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK14QByteArrayView5frontEv(const QByteArrayView *self) {
  return self->front();
}

//  char QByteArrayView::back() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK14QByteArrayView4backEv(const QByteArrayView *self) {
  return self->back();
}

//  qsizetype QByteArrayView::max_size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView8max_sizeEv(const QByteArrayView *self) {
  return self->max_size();
}

//  bool QByteArrayView::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView6isNullEv(const QByteArrayView *self) {
  return self->isNull();
}

//  bool QByteArrayView::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QByteArrayView7isEmptyEv(const QByteArrayView *self) {
  return self->isEmpty();
}

//  qsizetype QByteArrayView::length() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QByteArrayView6lengthEv(const QByteArrayView *self) {
  return self->length();
}

//  char QByteArrayView::first() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK14QByteArrayView5firstEv(const QByteArrayView *self) {
  return self->first();
}

//  char QByteArrayView::last() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK14QByteArrayView4lastEv(const QByteArrayView *self) {
  return self->last();
}

//  void QByteArrayView::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QByteArrayView6verifyExx(
    const QByteArrayView *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}

//  bool operator==(const QByteArrayView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewS1_(
    const QByteArrayView *lhs,
    const QByteArrayView *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QByteArrayView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewS1_(
    const QByteArrayView *lhs,
    const QByteArrayView *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QByteArrayView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewS1_(
    const QByteArrayView *lhs,
    const QByteArrayView *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QByteArrayView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewS1_(
    const QByteArrayView *lhs,
    const QByteArrayView *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QByteArrayView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewS1_(
    const QByteArrayView *lhs,
    const QByteArrayView *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QByteArrayView &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewS1_(
    const QByteArrayView *lhs,
    const QByteArrayView *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QByteArrayView &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewRKc(const QByteArrayView *lhs, char rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const QByteArrayView &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewRKc(const QByteArrayView *lhs, char rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const QByteArrayView &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewRKc(const QByteArrayView *lhs, char rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const QByteArrayView &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewRKc(const QByteArrayView *lhs, char rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const QByteArrayView &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewRKc(const QByteArrayView *lhs, char rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const QByteArrayView &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewRKc(const QByteArrayView *lhs, char rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const char &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKcRK14QByteArrayView(char lhs, const QByteArrayView *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const char &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKcRK14QByteArrayView(char lhs, const QByteArrayView *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const char &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKcRK14QByteArrayView(char lhs, const QByteArrayView *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const char &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKcRK14QByteArrayView(char lhs, const QByteArrayView *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const char &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKcRK14QByteArrayView(char lhs, const QByteArrayView *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const char &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKcRK14QByteArrayView(char lhs, const QByteArrayView *rhs) {
  return operator>=(lhs, *rhs);
}

//  bool operator==(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QByteArrayView::~QByteArrayView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QByteArrayViewD1Ev(QByteArrayView *self) {
  delete self;
}
