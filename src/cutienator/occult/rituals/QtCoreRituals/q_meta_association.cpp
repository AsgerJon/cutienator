//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

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

//  void QMetaAssociation::insertKey(void *container, const void *key) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation9insertKeyEPvPKv(
    const QMetaAssociation *self,
    void *container,
    const void *key) {
  self->insertKey(container, key);
}

//  bool QMetaAssociation::canRemoveKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation12canRemoveKeyEv(
    const QMetaAssociation *self) {
  return self->canRemoveKey();
}

//  void QMetaAssociation::removeKey(void *container, const void *key) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation9removeKeyEPvPKv(
    const QMetaAssociation *self,
    void *container,
    const void *key) {
  self->removeKey(container, key);
}

//  bool QMetaAssociation::canContainsKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation14canContainsKeyEv(
    const QMetaAssociation *self) {
  return self->canContainsKey();
}

//  bool QMetaAssociation::containsKey(const void *container, const void
//      *key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation11containsKeyEPKvS1_(
    const QMetaAssociation *self,
    const void *container,
    const void *key) {
  return self->containsKey(container, key);
}

//  bool QMetaAssociation::canGetMappedAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation17canGetMappedAtKeyEv(
    const QMetaAssociation *self) {
  return self->canGetMappedAtKey();
}

//  void QMetaAssociation::mappedAtKey(const void *container, const void
//      *key, void *mapped) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation11mappedAtKeyEPKvS1_Pv(
    const QMetaAssociation *self,
    const void *container,
    const void *key,
    void *mapped) {
  self->mappedAtKey(container, key, mapped);
}

//  bool QMetaAssociation::canSetMappedAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation17canSetMappedAtKeyEv(
    const QMetaAssociation *self) {
  return self->canSetMappedAtKey();
}

//  void QMetaAssociation::setMappedAtKey(void *container, const void *key,
//      const void *mapped) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation14setMappedAtKeyEPvPKvS2_(
    const QMetaAssociation *self,
    void *container,
    const void *key,
    const void *mapped) {
  self->setMappedAtKey(container, key, mapped);
}

//  bool QMetaAssociation::canGetKeyAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation19canGetKeyAtIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetKeyAtIterator();
}

//  void QMetaAssociation::keyAtIterator(const void *iterator, void *key)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation13keyAtIteratorEPKvPv(
    const QMetaAssociation *self,
    const void *iterator,
    void *key) {
  self->keyAtIterator(iterator, key);
}

//  bool QMetaAssociation::canGetKeyAtConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation24canGetKeyAtConstIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetKeyAtConstIterator();
}

//  void QMetaAssociation::keyAtConstIterator(const void *iterator, void
//      *key) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation18keyAtConstIteratorEPKvPv(
    const QMetaAssociation *self,
    const void *iterator,
    void *key) {
  self->keyAtConstIterator(iterator, key);
}

//  bool QMetaAssociation::canGetMappedAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation22canGetMappedAtIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetMappedAtIterator();
}

//  void QMetaAssociation::mappedAtIterator(const void *iterator, void
//      *mapped) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation16mappedAtIteratorEPKvPv(
    const QMetaAssociation *self,
    const void *iterator,
    void *mapped) {
  self->mappedAtIterator(iterator, mapped);
}

//  bool QMetaAssociation::canGetMappedAtConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation27canGetMappedAtConstIteratorEv(
    const QMetaAssociation *self) {
  return self->canGetMappedAtConstIterator();
}

//  void QMetaAssociation::mappedAtConstIterator(const void *iterator, void
//      *mapped) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation21mappedAtConstIteratorEPKvPv(
    const QMetaAssociation *self,
    const void *iterator,
    void *mapped) {
  self->mappedAtConstIterator(iterator, mapped);
}

//  bool QMetaAssociation::canSetMappedAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation22canSetMappedAtIteratorEv(
    const QMetaAssociation *self) {
  return self->canSetMappedAtIterator();
}

//  void QMetaAssociation::setMappedAtIterator(const void *iterator, const
//      void *mapped) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QMetaAssociation19setMappedAtIteratorEPKvS1_(
    const QMetaAssociation *self,
    const void *iterator,
    const void *mapped) {
  self->setMappedAtIterator(iterator, mapped);
}

//  bool QMetaAssociation::canCreateIteratorAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation22canCreateIteratorAtKeyEv(
    const QMetaAssociation *self) {
  return self->canCreateIteratorAtKey();
}

//  void *QMetaAssociation::createIteratorAtKey(void *container, const void
//      *key) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK16QMetaAssociation19createIteratorAtKeyEPvPKv(
    const QMetaAssociation *self,
    void *container,
    const void *key) {
  return self->createIteratorAtKey(container, key);
}

//  bool QMetaAssociation::canCreateConstIteratorAtKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QMetaAssociation27canCreateConstIteratorAtKeyEv(
    const QMetaAssociation *self) {
  return self->canCreateConstIteratorAtKey();
}

//  void *QMetaAssociation::createConstIteratorAtKey(const void *container,
//      const void *key) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK16QMetaAssociation24createConstIteratorAtKeyEPKvS1_(
    const QMetaAssociation *self,
    const void *container,
    const void *key) {
  return self->createConstIteratorAtKey(container, key);
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

//  static constexpr QMetaAssociation
//      QMetaAssociation::fromContainer<QMap<QString, QVariant>>()
extern "C" Q_DECL_EXPORT
QMetaAssociation * ritual_ZN16QMetaAssociation13fromContainerI4QMapI7QString8QVariantEEES_v() {
  return new QMetaAssociation(
      QMetaAssociation::fromContainer<QMap<QString, QVariant>>());
}

//  static constexpr QMetaAssociation
//      QMetaAssociation::fromContainer<QHash<QString, QVariant>>()
extern "C" Q_DECL_EXPORT
QMetaAssociation * ritual_ZN16QMetaAssociation13fromContainerI5QHashI7QString8QVariantEEES_v() {
  return new QMetaAssociation(
      QMetaAssociation::fromContainer<QHash<QString, QVariant>>());
}

//  static constexpr QMetaAssociation
//      QMetaAssociation::fromContainer<QMap<QString, QString>>()
extern "C" Q_DECL_EXPORT
QMetaAssociation * ritual_ZN16QMetaAssociation13fromContainerI4QMapI7QStringS2_EEES_v() {
  return new QMetaAssociation(
      QMetaAssociation::fromContainer<QMap<QString, QString>>());
}

//  static constexpr QMetaAssociation
//      QMetaAssociation::fromContainer<QHash<QString, QString>>()
extern "C" Q_DECL_EXPORT
QMetaAssociation * ritual_ZN16QMetaAssociation13fromContainerI5QHashI7QStringS2_EEES_v() {
  return new QMetaAssociation(
      QMetaAssociation::fromContainer<QHash<QString, QString>>());
}

//  static constexpr QMetaAssociation
//      QMetaAssociation::fromContainer<QMap<QString, int>>()
extern "C" Q_DECL_EXPORT
QMetaAssociation * ritual_ZN16QMetaAssociation13fromContainerI4QMapI7QStringiEEES_v() {
  return new QMetaAssociation(
      QMetaAssociation::fromContainer<QMap<QString, int>>());
}
