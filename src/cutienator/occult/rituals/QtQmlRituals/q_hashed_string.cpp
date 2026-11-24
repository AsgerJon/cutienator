//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qhashedstring_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QHashedString::QHashedString()
extern "C" Q_DECL_EXPORT
QHashedString *ritual_ZN13QHashedStringC1Ev() {
  return new QHashedString();
}

//  QHashedString::QHashedString(const QString &string)
extern "C" Q_DECL_EXPORT
QHashedString *ritual_ZN13QHashedStringC1ERK7QString(const QString *string) {
  return new QHashedString(*string);
}

//  QHashedString::QHashedString(const QString &string, quint32 a1)
extern "C" Q_DECL_EXPORT
QHashedString *ritual_ZN13QHashedStringC1ERK7QStringj(
    const QString *string,
    quint32 a1) {
  return new QHashedString(*string, a1);
}

//  QHashedString::QHashedString(const QHashedString &string)
extern "C" Q_DECL_EXPORT
QHashedString *ritual_ZN13QHashedStringC1ERKS_(const QHashedString *string) {
  return new QHashedString(*string);
}

//  bool QHashedString::operator==(const QHashedString &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QHashedStringeqERKS_(
    const QHashedString *self,
    const QHashedString *string) {
  return self->operator==(*string);
}

//  bool QHashedString::operator==(const QHashedStringRef &string) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QHashedStringeqERK16QHashedStringRef(
    const QHashedString *self,
    const QHashedStringRef *string) {
  return self->operator==(*string);
}

//  quint32 QHashedString::hash() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK13QHashedString4hashEv(const QHashedString *self) {
  return self->hash();
}

//  quint32 QHashedString::existingHash() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK13QHashedString12existingHashEv(
    const QHashedString *self) {
  return self->existingHash();
}

//  bool QHashedString::compare(const QChar *lhs, const char *rhs, int
//      length)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QHashedString7compareEPK5QCharPKci(
    const QChar *lhs,
    const char *rhs,
    int length) {
  return QHashedString::compare(lhs, rhs, length);
}

//  bool QHashedString::compare(const char *lhs, const char *rhs, int length)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QHashedString7compareEPKcS1_i(
    const char *lhs,
    const char *rhs,
    int length) {
  return QHashedString::compare(lhs, rhs, length);
}

//  quint32 QHashedString::stringHash(const QChar *data, int length)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN13QHashedString10stringHashEPK5QChari(
    const QChar *data,
    int length) {
  return QHashedString::stringHash(data, length);
}

//  quint32 QHashedString::stringHash(const char *data, int length)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN13QHashedString10stringHashEPKci(
    const char *data,
    int length) {
  return QHashedString::stringHash(data, length);
}

//  void QHashedString::computeHash() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QHashedString11computeHashEv(const QHashedString *self) {
  self->computeHash();
}

//  QHashedString::~QHashedString()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHashedStringD1Ev(QHashedString *self) {
  delete self;
}
