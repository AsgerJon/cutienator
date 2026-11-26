//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtyperevision.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 6. Kept as it is when the
//  generator runs again.
#include <QtCore/qtyperevision.h>

//  QTypeRevision QTypeRevision::zero()
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevision4zeroEv() {
  return new QTypeRevision(QTypeRevision::zero());
}

//  QTypeRevision::QTypeRevision()
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevisionC1Ev() {
  return new QTypeRevision();
}

//  bool QTypeRevision::hasMajorVersion() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTypeRevision15hasMajorVersionEv(
    const QTypeRevision *self) {
  return self->hasMajorVersion();
}

//  quint8 QTypeRevision::majorVersion() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK13QTypeRevision12majorVersionEv(const QTypeRevision *self) {
  return self->majorVersion();
}

//  bool QTypeRevision::hasMinorVersion() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTypeRevision15hasMinorVersionEv(
    const QTypeRevision *self) {
  return self->hasMinorVersion();
}

//  quint8 QTypeRevision::minorVersion() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK13QTypeRevision12minorVersionEv(const QTypeRevision *self) {
  return self->minorVersion();
}

//  bool QTypeRevision::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTypeRevision7isValidEv(const QTypeRevision *self) {
  return self->isValid();
}

//  bool operator==(const QTypeRevision &lhs, const QTypeRevision &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QTypeRevisionS1_(
    const QTypeRevision *lhs,
    const QTypeRevision *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QTypeRevision &lhs, const QTypeRevision &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QTypeRevisionS1_(
    const QTypeRevision *lhs,
    const QTypeRevision *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QTypeRevision &lhs, const QTypeRevision &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK13QTypeRevisionS1_(
    const QTypeRevision *lhs,
    const QTypeRevision *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QTypeRevision &lhs, const QTypeRevision &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK13QTypeRevisionS1_(
    const QTypeRevision *lhs,
    const QTypeRevision *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QTypeRevision &lhs, const QTypeRevision &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK13QTypeRevisionS1_(
    const QTypeRevision *lhs,
    const QTypeRevision *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QTypeRevision &lhs, const QTypeRevision &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK13QTypeRevisionS1_(
    const QTypeRevision *lhs,
    const QTypeRevision *rhs) {
  return operator>=(*lhs, *rhs);
}

#if Q_BYTE_ORDER == Q_LITTLE_ENDIAN
//  QTypeRevision::QTypeRevision(quint8 major, quint8 minor)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevisionC1Ehh(quint8 major, quint8 minor) {
  return new QTypeRevision(major, minor);
}
#endif  // Q_BYTE_ORDER == Q_LITTLE_ENDIAN

//  QTypeRevision::~QTypeRevision()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTypeRevisionD1Ev(QTypeRevision *self) {
  delete self;
}

//  bool QTypeRevision::isValidSegment<int>(int segment)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QTypeRevision14isValidSegmentIiLb1EEEbT_(
    int segment) {
  return QTypeRevision::isValidSegment<int>(segment);
}

//  QTypeRevision QTypeRevision::fromVersion<int, int>(int majorVersion,
//      int minorVersion)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevision11fromVersionIiiLb1ELb1EEES_T_T0_(
    int majorVersion,
    int minorVersion) {
  return new QTypeRevision(
      QTypeRevision::fromVersion<int, int>(majorVersion, minorVersion));
}

//  QTypeRevision QTypeRevision::fromMajorVersion<int>(int majorVersion)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevision16fromMajorVersionIiLb1EEES_T_(
    int majorVersion) {
  return new QTypeRevision(
      QTypeRevision::fromMajorVersion<int>(majorVersion));
}

//  QTypeRevision QTypeRevision::fromMinorVersion<int>(int minorVersion)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevision16fromMinorVersionIiLb1EEES_T_(
    int minorVersion) {
  return new QTypeRevision(
      QTypeRevision::fromMinorVersion<int>(minorVersion));
}

//  QTypeRevision QTypeRevision::fromEncodedVersion<int>(int value)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN13QTypeRevision18fromEncodedVersionIiLb1EEES_T_(
    int value) {
  return new QTypeRevision(QTypeRevision::fromEncodedVersion<int>(value));
}

//  int QTypeRevision::toEncodedVersion<int>() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTypeRevision16toEncodedVersionIiLb1EEET_v(
    const QTypeRevision *self) {
  return self->toEncodedVersion<int>();
}
