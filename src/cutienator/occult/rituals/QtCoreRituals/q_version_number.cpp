//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qversionnumber.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 1. Kept as it is when the
//  generator runs again.
#include <QtCore/qversionnumber.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QSpan>
#include <QtCore/QList>
#include <QtCore/QVersionNumber>

//  QVersionNumber::QVersionNumber()
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1Ev() {
  return new QVersionNumber();
}

//  QVersionNumber::QVersionNumber(std::initializer_list<int> args)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1ESt16initializer_listIiE(
    const std::initializer_list<int> *args) {
  return new QVersionNumber(*args);
}

//  QVersionNumber::QVersionNumber(QSpan<const int> args)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1E5QSpanIKiLm18446744073709551615EE(
    const QSpan<const int> *args) {
  return new QVersionNumber(*args);
}

//  QVersionNumber::QVersionNumber(int maj)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1Ei(int maj) {
  return new QVersionNumber(maj);
}

//  QVersionNumber::QVersionNumber(int maj, int min)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1Eii(int maj, int min) {
  return new QVersionNumber(maj, min);
}

//  QVersionNumber::QVersionNumber(int maj, int min, int mic)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1Eiii(int maj, int min, int mic) {
  return new QVersionNumber(maj, min, mic);
}

//  bool QVersionNumber::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QVersionNumber6isNullEv(const QVersionNumber *self) {
  return self->isNull();
}

//  bool QVersionNumber::isNormalized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QVersionNumber12isNormalizedEv(const QVersionNumber *self) {
  return self->isNormalized();
}

//  int QVersionNumber::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QVersionNumber12majorVersionEv(const QVersionNumber *self) {
  return self->majorVersion();
}

//  int QVersionNumber::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QVersionNumber12minorVersionEv(const QVersionNumber *self) {
  return self->minorVersion();
}

//  int QVersionNumber::microVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QVersionNumber12microVersionEv(const QVersionNumber *self) {
  return self->microVersion();
}

//  QVersionNumber QVersionNumber::normalized() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK14QVersionNumber10normalizedEv(
    const QVersionNumber *self) {
  return new QVersionNumber(self->normalized());
}

//  QList<int> QVersionNumber::segments() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK14QVersionNumber8segmentsEv(
    const QVersionNumber *self) {
  return new QList<int>(self->segments());
}

//  int QVersionNumber::segmentAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QVersionNumber9segmentAtEx(
    const QVersionNumber *self,
    qsizetype index) {
  return self->segmentAt(index);
}

//  qsizetype QVersionNumber::segmentCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QVersionNumber12segmentCountEv(
    const QVersionNumber *self) {
  return self->segmentCount();
}

//  const_iterator QVersionNumber::begin() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_iterator *ritual_ZNK14QVersionNumber5beginEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_iterator(self->begin());
}

//  const_iterator QVersionNumber::end() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_iterator *ritual_ZNK14QVersionNumber3endEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_iterator(self->end());
}

//  const_iterator QVersionNumber::cbegin() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_iterator *ritual_ZNK14QVersionNumber6cbeginEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_iterator(self->cbegin());
}

//  const_iterator QVersionNumber::cend() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_iterator *ritual_ZNK14QVersionNumber4cendEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_iterator(self->cend());
}

//  const_reverse_iterator QVersionNumber::rbegin() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_reverse_iterator *ritual_ZNK14QVersionNumber6rbeginEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator QVersionNumber::rend() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_reverse_iterator *ritual_ZNK14QVersionNumber4rendEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator QVersionNumber::crbegin() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_reverse_iterator *ritual_ZNK14QVersionNumber7crbeginEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_reverse_iterator(self->crbegin());
}

//  const_reverse_iterator QVersionNumber::crend() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_reverse_iterator *ritual_ZNK14QVersionNumber5crendEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_reverse_iterator(self->crend());
}

//  const_iterator QVersionNumber::constBegin() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_iterator *ritual_ZNK14QVersionNumber10constBeginEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_iterator(self->constBegin());
}

//  const_iterator QVersionNumber::constEnd() const
extern "C" Q_DECL_EXPORT
QVersionNumber::const_iterator *ritual_ZNK14QVersionNumber8constEndEv(
    const QVersionNumber *self) {
  return new QVersionNumber::const_iterator(self->constEnd());
}

//  bool QVersionNumber::isPrefixOf(const QVersionNumber &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QVersionNumber10isPrefixOfERKS_(
    const QVersionNumber *self,
    const QVersionNumber *other) {
  return self->isPrefixOf(*other);
}

//  int QVersionNumber::compare(const QVersionNumber &v1, const
//      QVersionNumber &v2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QVersionNumber7compareERKS_S1_(
    const QVersionNumber *v1,
    const QVersionNumber *v2) {
  return QVersionNumber::compare(*v1, *v2);
}

//  QVersionNumber QVersionNumber::commonPrefix(const QVersionNumber &v1,
//      const QVersionNumber &v2)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumber12commonPrefixERKS_S1_(
    const QVersionNumber *v1,
    const QVersionNumber *v2) {
  return new QVersionNumber(QVersionNumber::commonPrefix(*v1, *v2));
}

//  QString QVersionNumber::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QVersionNumber8toStringEv(const QVersionNumber *self) {
  return new QString(self->toString());
}

//  QVersionNumber QVersionNumber::fromString(QAnyStringView string,
//      qsizetype *suffixIndex)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumber10fromStringE14QAnyStringViewPx(
    const QString *string,
    qsizetype *suffixIndex) {
  return new QVersionNumber(
      QVersionNumber::fromString(
          QAnyStringView(*string),
          suffixIndex));
}

//  bool operator==(const QVersionNumber &lhs, const QVersionNumber &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QVersionNumberS1_(
    const QVersionNumber *lhs,
    const QVersionNumber *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QVersionNumber &lhs, const QVersionNumber &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QVersionNumberS1_(
    const QVersionNumber *lhs,
    const QVersionNumber *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QVersionNumber &lhs, const QVersionNumber &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QVersionNumberS1_(
    const QVersionNumber *lhs,
    const QVersionNumber *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QVersionNumber &lhs, const QVersionNumber &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QVersionNumberS1_(
    const QVersionNumber *lhs,
    const QVersionNumber *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QVersionNumber &lhs, const QVersionNumber &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QVersionNumberS1_(
    const QVersionNumber *lhs,
    const QVersionNumber *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QVersionNumber &lhs, const QVersionNumber &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QVersionNumberS1_(
    const QVersionNumber *lhs,
    const QVersionNumber *rhs) {
  return operator>=(*lhs, *rhs);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &in, QVersionNumber &version)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR14QVersionNumber(
    QDataStream *in,
    QVersionNumber *version) {
  return &(operator>>(*in, *version));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QVersionNumber::~QVersionNumber()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QVersionNumberD1Ev(QVersionNumber *self) {
  delete self;
}

//  QList<QVersionNumber>::QList()
extern "C" Q_DECL_EXPORT
QList<QVersionNumber> *ritual_list_make_QVersionNumber() {
  return new QList<QVersionNumber>();
}

//  void QList<QVersionNumber>::append(const QVersionNumber &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QVersionNumber(
    QList<QVersionNumber> *self,
    const QVersionNumber *element) {
  self->append(*element);
}

//  qsizetype QList<QVersionNumber>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QVersionNumber(
    const QList<QVersionNumber> *self) {
  return self->size();
}

//  const QVersionNumber &QList<QVersionNumber>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_list_at_QVersionNumber(
    const QList<QVersionNumber> *self,
    long long index) {
  return new QVersionNumber(self->at(index));
}

//  QList<QVersionNumber>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QVersionNumber(QList<QVersionNumber> *self) {
  delete self;
}

//  QMap<QString, QVersionNumber>: QMap<QString, QVersionNumber>()
extern "C" Q_DECL_EXPORT
QMap<QString, QVersionNumber> *ritual_map_make_QMap_QString_QVersionNumber() {
  return new QMap<QString, QVersionNumber>();
}

//  QMap<QString, QVersionNumber>: insert(const Key &key, const T &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_QString_QVersionNumber(
    QMap<QString, QVersionNumber> *self,
    const QString *key,
    const QVersionNumber *value) {
  self->insert(*key, *value);
}

//  QMap<QString, QVersionNumber>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_QString_QVersionNumber(
    const QMap<QString, QVersionNumber> *self) {
  return self->size();
}

//  QMap<QString, QVersionNumber>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QMap_QString_QVersionNumber(
    const QMap<QString, QVersionNumber> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QMap<QString, QVersionNumber>: the value at a place
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_map_value_QMap_QString_QVersionNumber(
    const QMap<QString, QVersionNumber> *self,
    long long index) {
  return new QVersionNumber(*std::next(self->constBegin(), index));
}

//  QMap<QString, QVersionNumber>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_QString_QVersionNumber(
    const QMap<QString, QVersionNumber> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QMap<QString, QVersionNumber>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_map_get_QMap_QString_QVersionNumber(
    const QMap<QString, QVersionNumber> *self,
    const QString *key) {
  return new QVersionNumber(self->value(*key));
}

//  QMap<QString, QVersionNumber>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_QString_QVersionNumber(
    QMap<QString, QVersionNumber> *self) {
  delete self;
}

//  a QList<int> a ritual of QVersionNumber gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVersionNumber__QList_int(QList<int> *self) {
  delete self;
}

//  a QVersionNumber::const_iterator a ritual of QVersionNumber gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVersionNumber__QVersionNumber_const_iterator(
    QVersionNumber::const_iterator *self) {
  delete self;
}

//  a QVersionNumber::const_reverse_iterator a ritual of QVersionNumber gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QVersionNumber__QVersionNumber_const_reverse_iterator(
    QVersionNumber::const_reverse_iterator *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 4) && QT_POINTER_SIZE != 4
//  static QVersionNumber QVersionNumber::fromString<void>(
//      QAnyStringView string, int *suffixIndex)
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumber10fromStringIvEES_14QAnyStringViewPi(
    const QString *string,
    int *suffixIndex) {
  return new QVersionNumber(
      QVersionNumber::fromString<void>(
          QAnyStringView(*string),
          suffixIndex));
}
#endif
