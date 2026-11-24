//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QV4::VTable *QV4::String::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV46String12staticVTableEv() {
  return QV4::String::staticVTable();
}

//  void QV4::String::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46String10__dataTestEv(QV4::String *self) {
  self->__dataTest();
}

//  QV4::Heap::String *QV4::String::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV46String11d_uncheckedEv(
    const QV4::String *self) {
  return self->d_unchecked();
}

//  QV4::Heap::String *QV4::String::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV46String1dEv(const QV4::String *self) {
  return self->d();
}

//  Heap::InternalClass *QV4::String::defaultInternalClass(QV4::EngineBase
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV46String20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::String::defaultInternalClass(e);
}

//  uchar QV4::String::subtype() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK3QV46String7subtypeEv(const QV4::String *self) {
  return self->subtype();
}

//  void QV4::String::setSubtype(uchar subtype) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV46String10setSubtypeEh(
    const QV4::String *self,
    uchar subtype) {
  self->setSubtype(subtype);
}

//  bool QV4::String::equals(String *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46String6equalsEPS0_(
    const QV4::String *self,
    QV4::String *other) {
  return self->equals(other);
}

//  bool QV4::String::isEqualTo(const String *other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46String9isEqualToEPKS0_(
    const QV4::String *self,
    const QV4::String *other) {
  return self->isEqualTo(other);
}

//  bool QV4::String::lessThan(const String *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46String8lessThanEPKS0_(
    QV4::String *self,
    const QV4::String *other) {
  return self->lessThan(other);
}

//  QString QV4::String::toQString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV46String9toQStringEv(const QV4::String *self) {
  return new QString(self->toQString());
}

//  unsigned int QV4::String::hashValue() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK3QV46String9hashValueEv(const QV4::String *self) {
  return self->hashValue();
}

//  uint QV4::String::createHashValue(const QChar *ch, int length, uint
//      *subtype)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV46String15createHashValueEPK5QChariPj(
    const QChar *ch,
    int length,
    uint *subtype) {
  return QV4::String::createHashValue(ch, length, subtype);
}

//  uint QV4::String::createHashValueDisallowingArrayIndex(const QChar *ch,
//      int length, uint *subtype)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV46String36createHashValueDisallowingArrayIndexEPK5QChariPj(
    const QChar *ch,
    int length,
    uint *subtype) {
  return QV4::String::createHashValueDisallowingArrayIndex(
      ch,
      length,
      subtype);
}

//  uint QV4::String::createHashValue(const char *ch, int length, uint
//      *subtype)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV46String15createHashValueEPKciPj(
    const char *ch,
    int length,
    uint *subtype) {
  return QV4::String::createHashValue(ch, length, subtype);
}

//  bool QV4::String::startsWithUpper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46String15startsWithUpperEv(const QV4::String *self) {
  return self->startsWithUpper();
}
