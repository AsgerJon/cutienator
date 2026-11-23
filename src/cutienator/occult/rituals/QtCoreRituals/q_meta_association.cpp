//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>

//  QMetaAssociation::QMetaAssociation()
extern "C" Q_DECL_EXPORT
QMetaAssociation *ritual_ZN16QMetaAssociationC1Ev() {
  return new QMetaAssociation();
}

//  QMetaAssociation::QMetaAssociation(const
//      QtMetaContainerPrivate::QMetaAssociationInterface *d)
extern "C" Q_DECL_EXPORT
QMetaAssociation *ritual_ZN16QMetaAssociationC1EPKN22QtMetaContainerPrivate25QMetaAssociationInterfaceE(
    const QtMetaContainerPrivate::QMetaAssociationInterface *d) {
  return new QMetaAssociation(d);
}

//  QMetaType QMetaAssociation::keyMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK16QMetaAssociation11keyMetaTypeEv(
    const QMetaAssociation *self) {
  return new QMetaType(self->keyMetaType());
}

//  QMetaType QMetaAssociation::mappedMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK16QMetaAssociation14mappedMetaTypeEv(
    const QMetaAssociation *self) {
  return new QMetaType(self->mappedMetaType());
}

//  bool QMetaAssociation::canInsertKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation12canInsertKeyEv(
    const QMetaAssociation *self) {
  return self->canInsertKey();
}

//  bool QMetaAssociation::canRemoveKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation12canRemoveKeyEv(
    const QMetaAssociation *self) {
  return self->canRemoveKey();
}

//  bool QMetaAssociation::canContainsKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation14canContainsKeyEv(
    const QMetaAssociation *self) {
  return self->canContainsKey();
}

//  bool QMetaAssociation::canGetMappedAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation17canGetMappedAtKeyEv(
    const QMetaAssociation *self) {
  return self->canGetMappedAtKey();
}

//  bool QMetaAssociation::canSetMappedAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation17canSetMappedAtKeyEv(
    const QMetaAssociation *self) {
  return self->canSetMappedAtKey();
}

//  bool QMetaAssociation::canGetKeyAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation19canGetKeyAtIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetKeyAtIterator();
}

//  bool QMetaAssociation::canGetKeyAtConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation24canGetKeyAtConstIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetKeyAtConstIterator();
}

//  bool QMetaAssociation::canGetMappedAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation22canGetMappedAtIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetMappedAtIterator();
}

//  bool QMetaAssociation::canGetMappedAtConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation27canGetMappedAtConstIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetMappedAtConstIterator();
}

//  bool QMetaAssociation::canSetMappedAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation22canSetMappedAtIteratorEv(
    const QMetaAssociation *self) {
  return self->canSetMappedAtIterator();
}

//  bool QMetaAssociation::canCreateIteratorAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation22canCreateIteratorAtKeyEv(
    const QMetaAssociation *self) {
  return self->canCreateIteratorAtKey();
}

//  bool QMetaAssociation::canCreateConstIteratorAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation27canCreateConstIteratorAtKeyEv(
    const QMetaAssociation *self) {
  return self->canCreateConstIteratorAtKey();
}

//  const QtMetaContainerPrivate::QMetaAssociationInterface
//      *QMetaAssociation::iface() const
extern "C" Q_DECL_EXPORT
const QtMetaContainerPrivate::QMetaAssociationInterface *ritual_ZNK16QMetaAssociation5ifaceEv(
    const QMetaAssociation *self) {
  return self->iface();
}

//  bool operator==(const QMetaAssociation &lhs, const QMetaAssociation &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QMetaAssociationS1_(
    const QMetaAssociation *lhs,
    const QMetaAssociation *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMetaAssociation &lhs, const QMetaAssociation &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QMetaAssociationS1_(
    const QMetaAssociation *lhs,
    const QMetaAssociation *rhs) {
  return operator!=(*lhs, *rhs);
}

//  const QtMetaContainerPrivate::QMetaAssociationInterface
//      *QMetaAssociation::d() const
extern "C" Q_DECL_EXPORT
const QtMetaContainerPrivate::QMetaAssociationInterface *ritual_ZNK16QMetaAssociation1dEv(
    const QMetaAssociation *self) {
  return self->d();
}

//  QMetaAssociation::~QMetaAssociation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMetaAssociationD1Ev(QMetaAssociation *self) {
  delete self;
}
