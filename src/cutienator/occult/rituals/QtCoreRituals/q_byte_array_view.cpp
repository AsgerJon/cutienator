//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbytearrayview.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again.
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qchar.h>
#include <QtCore/qlist.h>
#include <QtCore/QByteArrayView>
#include <string_view>

//  qsizetype QByteArrayView::lengthHelperCharArray(const char *data, size_t
//      size)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN14QByteArrayView21lengthHelperCharArrayEPKcm(
    const char *data,
    size_t size) {
  return QByteArrayView::lengthHelperCharArray(data, size);
}

//  const storage_type *QByteArrayView::castHelper(const storage_type *data)
extern "C" Q_DECL_EXPORT
const QByteArrayView::storage_type *ritual_ZN14QByteArrayView10castHelperEPKc(
    const QByteArrayView::storage_type *data) {
  return QByteArrayView::castHelper(data);
}

//  QByteArrayView::QByteArrayView()
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1Ev() {
  return new QByteArrayView();
}

//  QByteArrayView::QByteArrayView(std::nullptr_t a0)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1EDn() {
  return new QByteArrayView(nullptr);
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

//  const_pointer QByteArrayView::data() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_pointer ritual_ZNK14QByteArrayView4dataEv(
    const QByteArrayView *self) {
  return self->data();
}

//  const_pointer QByteArrayView::constData() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_pointer ritual_ZNK14QByteArrayView9constDataEv(
    const QByteArrayView *self) {
  return self->constData();
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

//  QByteArrayView &QByteArrayView::slice(qsizetype pos)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayView5sliceEx(
    QByteArrayView *self,
    qsizetype pos) {
  return &(self->slice(pos));
}

//  QByteArrayView &QByteArrayView::slice(qsizetype pos, qsizetype n)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayView5sliceExx(
    QByteArrayView *self,
    qsizetype pos,
    qsizetype n) {
  return &(self->slice(pos, n));
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

//  const_iterator QByteArrayView::begin() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_iterator ritual_ZNK14QByteArrayView5beginEv(
    const QByteArrayView *self) {
  return self->begin();
}

//  const_iterator QByteArrayView::end() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_iterator ritual_ZNK14QByteArrayView3endEv(
    const QByteArrayView *self) {
  return self->end();
}

//  const_iterator QByteArrayView::cbegin() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_iterator ritual_ZNK14QByteArrayView6cbeginEv(
    const QByteArrayView *self) {
  return self->cbegin();
}

//  const_iterator QByteArrayView::cend() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_iterator ritual_ZNK14QByteArrayView4cendEv(
    const QByteArrayView *self) {
  return self->cend();
}

//  const_reverse_iterator QByteArrayView::rbegin() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_reverse_iterator *ritual_ZNK14QByteArrayView6rbeginEv(
    const QByteArrayView *self) {
  return new QByteArrayView::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator QByteArrayView::rend() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_reverse_iterator *ritual_ZNK14QByteArrayView4rendEv(
    const QByteArrayView *self) {
  return new QByteArrayView::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator QByteArrayView::crbegin() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_reverse_iterator *ritual_ZNK14QByteArrayView7crbeginEv(
    const QByteArrayView *self) {
  return new QByteArrayView::const_reverse_iterator(self->crbegin());
}

//  const_reverse_iterator QByteArrayView::crend() const
extern "C" Q_DECL_EXPORT
QByteArrayView::const_reverse_iterator *ritual_ZNK14QByteArrayView5crendEv(
    const QByteArrayView *self) {
  return new QByteArrayView::const_reverse_iterator(self->crend());
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

//  std::string_view QByteArrayView::operator basic_string_view() const
extern "C" Q_DECL_EXPORT
std::string_view *ritual_ZNK14QByteArrayViewcvSt17basic_string_viewIcSt11char_traitsIcEEEv(
    const QByteArrayView *self) {
  return new std::string_view(self->operator std::string_view());
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

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator==(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator<(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator>(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QByteArrayView &lhs, const QChar &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewRK5QChar(
    const QByteArrayView *lhs,
    const QChar *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator==(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator<(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator>(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QChar &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK5QCharRK14QByteArrayView(
    const QChar *lhs,
    const QByteArrayView *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const QByteArrayView &lhs, const char16_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QByteArrayViewRKDs(
    const QByteArrayView *lhs,
    char16_t rhs) {
  return operator==(*lhs, rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const QByteArrayView &lhs, const char16_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QByteArrayViewRKDs(
    const QByteArrayView *lhs,
    char16_t rhs) {
  return operator!=(*lhs, rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const QByteArrayView &lhs, const char16_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QByteArrayViewRKDs(
    const QByteArrayView *lhs,
    char16_t rhs) {
  return operator<(*lhs, rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const QByteArrayView &lhs, const char16_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QByteArrayViewRKDs(
    const QByteArrayView *lhs,
    char16_t rhs) {
  return operator>(*lhs, rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const QByteArrayView &lhs, const char16_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QByteArrayViewRKDs(
    const QByteArrayView *lhs,
    char16_t rhs) {
  return operator<=(*lhs, rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const QByteArrayView &lhs, const char16_t &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QByteArrayViewRKDs(
    const QByteArrayView *lhs,
    char16_t rhs) {
  return operator>=(*lhs, rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator==(const char16_t &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKDsRK14QByteArrayView(
    char16_t lhs,
    const QByteArrayView *rhs) {
  return operator==(lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator!=(const char16_t &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKDsRK14QByteArrayView(
    char16_t lhs,
    const QByteArrayView *rhs) {
  return operator!=(lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<(const char16_t &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKDsRK14QByteArrayView(
    char16_t lhs,
    const QByteArrayView *rhs) {
  return operator<(lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>(const char16_t &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKDsRK14QByteArrayView(
    char16_t lhs,
    const QByteArrayView *rhs) {
  return operator>(lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator<=(const char16_t &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKDsRK14QByteArrayView(
    char16_t lhs,
    const QByteArrayView *rhs) {
  return operator<=(lhs, *rhs);
}
#endif

#if !defined(QT_NO_CAST_FROM_ASCII) && \
    !defined(QT_RESTRICTED_CAST_FROM_ASCII)
//  bool operator>=(const char16_t &lhs, const QByteArrayView &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKDsRK14QByteArrayView(
    char16_t lhs,
    const QByteArrayView *rhs) {
  return operator>=(lhs, *rhs);
}
#endif

//  QByteArrayView::~QByteArrayView()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QByteArrayViewD1Ev(QByteArrayView *self) {
  delete self;
}

//  QList<QByteArrayView>::QList()
extern "C" Q_DECL_EXPORT
QList<QByteArrayView> *ritual_list_make_QByteArrayView() {
  return new QList<QByteArrayView>();
}

//  void QList<QByteArrayView>::append(const QByteArrayView &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QByteArrayView(
    QList<QByteArrayView> *self,
    const QByteArrayView *element) {
  self->append(*element);
}

//  qsizetype QList<QByteArrayView>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QByteArrayView(
    const QList<QByteArrayView> *self) {
  return self->size();
}

//  const QByteArrayView &QList<QByteArrayView>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_list_at_QByteArrayView(
    const QList<QByteArrayView> *self,
    long long index) {
  return new QByteArrayView(self->at(index));
}

//  QList<QByteArrayView>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QByteArrayView(QList<QByteArrayView> *self) {
  delete self;
}

//  a QByteArrayView::const_reverse_iterator a ritual of QByteArrayView gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QByteArrayView__QByteArrayView_const_reverse_iterator(
    QByteArrayView::const_reverse_iterator *self) {
  delete self;
}

//  a std::string_view a ritual of QByteArrayView gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QByteArrayView__std_string_view(std::string_view *self) {
  delete self;
}

//  template <typename Byte, if_compatible_byte<Byte> = true>
//  constexpr QByteArrayView::QByteArrayView<char, true>(const char *data,
//      qsizetype len)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1IcLb1EEEPKT_x(
    const char *data,
    qsizetype len) {
  return new QByteArrayView(data, len);
}

//  template <typename Byte, if_compatible_byte<Byte> = true>
//  constexpr QByteArrayView::QByteArrayView<char, true>(const char *first,
//      const char *last)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1IcLb1EEEPKT_S3_(
    const char *first,
    const char *last) {
  return new QByteArrayView(first, last);
}

//  template <typename Pointer, if_compatible_pointer<Pointer> = true>
//  constexpr QByteArrayView::QByteArrayView<const char *, true>(
//      const char *const &data)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1IPKcLb1EEERKT_(
    const char *data) {
  return new QByteArrayView(data);
}

//  template <typename ByteArray, if_compatible_qbytearray_like<ByteArray>
//  = true> QByteArrayView::QByteArrayView<QByteArray, true>(
//      const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QByteArrayView *ritual_ZN14QByteArrayViewC1I10QByteArrayLb1EEERKT_(
    const QByteArray *ba) {
  return new QByteArrayView(*ba);
}
