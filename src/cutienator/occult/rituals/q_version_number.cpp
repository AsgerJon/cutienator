//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qversionnumber.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qversionnumber.h>
#include <QtCore/qstring.h>
#include <QtCore/qanystringview.h>

//  QVersionNumber::QVersionNumber()
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZN14QVersionNumberC1Ev() {
  return new QVersionNumber();
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

//  QVersionNumber::~QVersionNumber()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QVersionNumberD1Ev(QVersionNumber *self) {
  delete self;
}
