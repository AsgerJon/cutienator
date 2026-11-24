//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::CompiledData::Alias::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData5Alias10isReadOnlyEv(
    const QV4::CompiledData::Alias *self) {
  return self->isReadOnly();
}

//  void QV4::CompiledData::Alias::setIsReadOnly(bool isReadOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5Alias13setIsReadOnlyEb(
    QV4::CompiledData::Alias *self,
    bool isReadOnly) {
  self->setIsReadOnly(isReadOnly);
}

//  quint32 QV4::CompiledData::Alias::nameIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData5Alias9nameIndexEv(
    const QV4::CompiledData::Alias *self) {
  return self->nameIndex();
}

//  void QV4::CompiledData::Alias::setNameIndex(quint32 nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5Alias12setNameIndexEj(
    QV4::CompiledData::Alias *self,
    quint32 nameIndex) {
  self->setNameIndex(nameIndex);
}

//  quint32 QV4::CompiledData::Alias::idIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData5Alias7idIndexEv(
    const QV4::CompiledData::Alias *self) {
  return self->idIndex();
}

//  void QV4::CompiledData::Alias::setIdIndex(quint32 idIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5Alias10setIdIndexEj(
    QV4::CompiledData::Alias *self,
    quint32 idIndex) {
  self->setIdIndex(idIndex);
}

//  quint32 QV4::CompiledData::Alias::propertyNameIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData5Alias17propertyNameIndexEv(
    const QV4::CompiledData::Alias *self) {
  return self->propertyNameIndex();
}

//  void QV4::CompiledData::Alias::setPropertyNameIndex(quint32
//      propertyNameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5Alias20setPropertyNameIndexEj(
    QV4::CompiledData::Alias *self,
    quint32 propertyNameIndex) {
  self->setPropertyNameIndex(propertyNameIndex);
}

//  Location QV4::CompiledData::Alias::location() const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Location *ritual_ZNK3QV412CompiledData5Alias8locationEv(
    const QV4::CompiledData::Alias *self) {
  return new QV4::CompiledData::Location(self->location());
}

//  void QV4::CompiledData::Alias::setLocation(Location location)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5Alias11setLocationENS0_8LocationE(
    QV4::CompiledData::Alias *self,
    const QV4::CompiledData::Location *location) {
  self->setLocation(*location);
}

//  Location QV4::CompiledData::Alias::referenceLocation() const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Location *ritual_ZNK3QV412CompiledData5Alias17referenceLocationEv(
    const QV4::CompiledData::Alias *self) {
  return new QV4::CompiledData::Location(self->referenceLocation());
}

//  void QV4::CompiledData::Alias::setReferenceLocation(Location
//      referenceLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5Alias20setReferenceLocationENS0_8LocationE(
    QV4::CompiledData::Alias *self,
    const QV4::CompiledData::Location *referenceLocation) {
  self->setReferenceLocation(*referenceLocation);
}

//  QV4::CompiledData::Alias::~Alias()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData5AliasD1Ev(QV4::CompiledData::Alias *self) {
  delete self;
}
