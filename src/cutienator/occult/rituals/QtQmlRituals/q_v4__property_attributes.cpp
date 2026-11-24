//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4global_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::PropertyAttributes::PropertyAttributes()
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV418PropertyAttributesC1Ev() {
  return new QV4::PropertyAttributes();
}

//  QV4::PropertyAttributes::PropertyAttributes(PropertyFlag f)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV418PropertyAttributesC1ENS_12PropertyFlagE(
    QV4::PropertyFlag f) {
  return new QV4::PropertyAttributes(f);
}

//  QV4::PropertyAttributes::PropertyAttributes(PropertyFlags f)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV418PropertyAttributesC1E6QFlagsINS_12PropertyFlagEE(
    int f) {
  return new QV4::PropertyAttributes(QFlags<QV4::PropertyFlag>::fromInt(f));
}

//  void QV4::PropertyAttributes::setType(Type t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes7setTypeENS0_4TypeE(
    QV4::PropertyAttributes *self,
    QV4::PropertyAttributes::Type t) {
  self->setType(t);
}

//  Type QV4::PropertyAttributes::type() const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes::Type ritual_ZNK3QV418PropertyAttributes4typeEv(
    const QV4::PropertyAttributes *self) {
  return self->type();
}

//  bool QV4::PropertyAttributes::isData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes6isDataEv(
    const QV4::PropertyAttributes *self) {
  return self->isData();
}

//  bool QV4::PropertyAttributes::isAccessor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes10isAccessorEv(
    const QV4::PropertyAttributes *self) {
  return self->isAccessor();
}

//  bool QV4::PropertyAttributes::isGeneric() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes9isGenericEv(
    const QV4::PropertyAttributes *self) {
  return self->isGeneric();
}

//  bool QV4::PropertyAttributes::hasType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes7hasTypeEv(
    const QV4::PropertyAttributes *self) {
  return self->hasType();
}

//  bool QV4::PropertyAttributes::hasWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes11hasWritableEv(
    const QV4::PropertyAttributes *self) {
  return self->hasWritable();
}

//  bool QV4::PropertyAttributes::hasConfigurable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes15hasConfigurableEv(
    const QV4::PropertyAttributes *self) {
  return self->hasConfigurable();
}

//  bool QV4::PropertyAttributes::hasEnumerable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes13hasEnumerableEv(
    const QV4::PropertyAttributes *self) {
  return self->hasEnumerable();
}

//  void QV4::PropertyAttributes::setWritable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes11setWritableEb(
    QV4::PropertyAttributes *self,
    bool b) {
  self->setWritable(b);
}

//  void QV4::PropertyAttributes::setConfigurable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes15setConfigurableEb(
    QV4::PropertyAttributes *self,
    bool b) {
  self->setConfigurable(b);
}

//  void QV4::PropertyAttributes::setEnumerable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes13setEnumerableEb(
    QV4::PropertyAttributes *self,
    bool b) {
  self->setEnumerable(b);
}

//  void QV4::PropertyAttributes::resolve()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes7resolveEv(
    QV4::PropertyAttributes *self) {
  self->resolve();
}

//  bool QV4::PropertyAttributes::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes10isWritableEv(
    const QV4::PropertyAttributes *self) {
  return self->isWritable();
}

//  bool QV4::PropertyAttributes::isEnumerable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes12isEnumerableEv(
    const QV4::PropertyAttributes *self) {
  return self->isEnumerable();
}

//  bool QV4::PropertyAttributes::isConfigurable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes14isConfigurableEv(
    const QV4::PropertyAttributes *self) {
  return self->isConfigurable();
}

//  void QV4::PropertyAttributes::clearType()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes9clearTypeEv(
    QV4::PropertyAttributes *self) {
  self->clearType();
}

//  void QV4::PropertyAttributes::clearWritable()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes13clearWritableEv(
    QV4::PropertyAttributes *self) {
  self->clearWritable();
}

//  void QV4::PropertyAttributes::clearEnumerable()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes15clearEnumerableEv(
    QV4::PropertyAttributes *self) {
  self->clearEnumerable();
}

//  void QV4::PropertyAttributes::clearConfigurable()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes17clearConfigurableEv(
    QV4::PropertyAttributes *self) {
  self->clearConfigurable();
}

//  void QV4::PropertyAttributes::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributes5clearEv(
    QV4::PropertyAttributes *self) {
  self->clear();
}

//  bool QV4::PropertyAttributes::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418PropertyAttributes7isEmptyEv(
    const QV4::PropertyAttributes *self) {
  return self->isEmpty();
}

//  uint QV4::PropertyAttributes::all() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV418PropertyAttributes3allEv(
    const QV4::PropertyAttributes *self) {
  return self->all();
}

//  bool QV4::PropertyAttributes::operator==(PropertyAttributes other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV418PropertyAttributeseqES0_(
    QV4::PropertyAttributes *self,
    const QV4::PropertyAttributes *other) {
  return self->operator==(*other);
}

//  bool QV4::PropertyAttributes::operator!=(PropertyAttributes other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV418PropertyAttributesneES0_(
    QV4::PropertyAttributes *self,
    const QV4::PropertyAttributes *other) {
  return self->operator!=(*other);
}

//  QV4::PropertyAttributes::~PropertyAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418PropertyAttributesD1Ev(QV4::PropertyAttributes *self) {
  delete self;
}
