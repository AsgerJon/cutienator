//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtyperevision.h, Qt 6.12.0. Changes made here are lost.
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

//  QTypeRevision::~QTypeRevision()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTypeRevisionD1Ev(QTypeRevision *self) {
  delete self;
}
