//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>

//  QMetaSequence::QMetaSequence()
extern "C" Q_DECL_EXPORT
QMetaSequence *ritual_ZN13QMetaSequenceC1Ev() {
  return new QMetaSequence();
}

//  QMetaSequence::QMetaSequence(const
//      QtMetaContainerPrivate::QMetaSequenceInterface *d)
extern "C" Q_DECL_EXPORT
QMetaSequence *ritual_ZN13QMetaSequenceC1EPKN22QtMetaContainerPrivate22QMetaSequenceInterfaceE(
    const QtMetaContainerPrivate::QMetaSequenceInterface *d) {
  return new QMetaSequence(d);
}

//  QMetaType QMetaSequence::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK13QMetaSequence13valueMetaTypeEv(
    const QMetaSequence *self) {
  return new QMetaType(self->valueMetaType());
}

//  bool QMetaSequence::isSortable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence10isSortableEv(const QMetaSequence *self) {
  return self->isSortable();
}

//  bool QMetaSequence::canAddValueAtBegin() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence18canAddValueAtBeginEv(
    const QMetaSequence *self) {
  return self->canAddValueAtBegin();
}

//  void QMetaSequence::addValueAtBegin(void *container, const void *value)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence15addValueAtBeginEPvPKv(
    const QMetaSequence *self,
    void *container,
    const void *value) {
  self->addValueAtBegin(container, value);
}

//  bool QMetaSequence::canAddValueAtEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence16canAddValueAtEndEv(
    const QMetaSequence *self) {
  return self->canAddValueAtEnd();
}

//  void QMetaSequence::addValueAtEnd(void *container, const void *value)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence13addValueAtEndEPvPKv(
    const QMetaSequence *self,
    void *container,
    const void *value) {
  self->addValueAtEnd(container, value);
}

//  bool QMetaSequence::canRemoveValueAtBegin() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence21canRemoveValueAtBeginEv(
    const QMetaSequence *self) {
  return self->canRemoveValueAtBegin();
}

//  void QMetaSequence::removeValueAtBegin(void *container) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence18removeValueAtBeginEPv(
    const QMetaSequence *self,
    void *container) {
  self->removeValueAtBegin(container);
}

//  bool QMetaSequence::canRemoveValueAtEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence19canRemoveValueAtEndEv(
    const QMetaSequence *self) {
  return self->canRemoveValueAtEnd();
}

//  void QMetaSequence::removeValueAtEnd(void *container) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence16removeValueAtEndEPv(
    const QMetaSequence *self,
    void *container) {
  self->removeValueAtEnd(container);
}

//  bool QMetaSequence::canGetValueAtIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence18canGetValueAtIndexEv(
    const QMetaSequence *self) {
  return self->canGetValueAtIndex();
}

//  void QMetaSequence::valueAtIndex(const void *container, qsizetype index,
//      void *result) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence12valueAtIndexEPKvxPv(
    const QMetaSequence *self,
    const void *container,
    qsizetype index,
    void *result) {
  self->valueAtIndex(container, index, result);
}

//  bool QMetaSequence::canSetValueAtIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence18canSetValueAtIndexEv(
    const QMetaSequence *self) {
  return self->canSetValueAtIndex();
}

//  void QMetaSequence::setValueAtIndex(void *container, qsizetype index,
//      const void *value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence15setValueAtIndexEPvxPKv(
    const QMetaSequence *self,
    void *container,
    qsizetype index,
    const void *value) {
  self->setValueAtIndex(container, index, value);
}

//  bool QMetaSequence::canAddValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence11canAddValueEv(const QMetaSequence *self) {
  return self->canAddValue();
}

//  void QMetaSequence::addValue(void *container, const void *value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence8addValueEPvPKv(
    const QMetaSequence *self,
    void *container,
    const void *value) {
  self->addValue(container, value);
}

//  bool QMetaSequence::canRemoveValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence14canRemoveValueEv(const QMetaSequence *self) {
  return self->canRemoveValue();
}

//  void QMetaSequence::removeValue(void *container) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence11removeValueEPv(
    const QMetaSequence *self,
    void *container) {
  self->removeValue(container);
}

//  bool QMetaSequence::canGetValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence21canGetValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canGetValueAtIterator();
}

//  void QMetaSequence::valueAtIterator(const void *iterator, void *result)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence15valueAtIteratorEPKvPv(
    const QMetaSequence *self,
    const void *iterator,
    void *result) {
  self->valueAtIterator(iterator, result);
}

//  bool QMetaSequence::canSetValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence21canSetValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canSetValueAtIterator();
}

//  void QMetaSequence::setValueAtIterator(const void *iterator, const void
//      *value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence18setValueAtIteratorEPKvS1_(
    const QMetaSequence *self,
    const void *iterator,
    const void *value) {
  self->setValueAtIterator(iterator, value);
}

//  bool QMetaSequence::canInsertValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence24canInsertValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canInsertValueAtIterator();
}

//  void QMetaSequence::insertValueAtIterator(void *container, const void
//      *iterator, const void *value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence21insertValueAtIteratorEPvPKvS2_(
    const QMetaSequence *self,
    void *container,
    const void *iterator,
    const void *value) {
  self->insertValueAtIterator(container, iterator, value);
}

//  bool QMetaSequence::canEraseValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence23canEraseValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canEraseValueAtIterator();
}

//  void QMetaSequence::eraseValueAtIterator(void *container, const void
//      *iterator) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence20eraseValueAtIteratorEPvPKv(
    const QMetaSequence *self,
    void *container,
    const void *iterator) {
  self->eraseValueAtIterator(container, iterator);
}

//  bool QMetaSequence::canEraseRangeAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence23canEraseRangeAtIteratorEv(
    const QMetaSequence *self) {
  return self->canEraseRangeAtIterator();
}

//  void QMetaSequence::eraseRangeAtIterator(void *container, const void
//      *iterator1, const void *iterator2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence20eraseRangeAtIteratorEPvPKvS2_(
    const QMetaSequence *self,
    void *container,
    const void *iterator1,
    const void *iterator2) {
  self->eraseRangeAtIterator(container, iterator1, iterator2);
}

//  bool QMetaSequence::canGetValueAtConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence26canGetValueAtConstIteratorEv(
    const QMetaSequence *self) {
  return self->canGetValueAtConstIterator();
}

//  void QMetaSequence::valueAtConstIterator(const void *iterator, void
//      *result) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QMetaSequence20valueAtConstIteratorEPKvPv(
    const QMetaSequence *self,
    const void *iterator,
    void *result) {
  self->valueAtConstIterator(iterator, result);
}

//  const QtMetaContainerPrivate::QMetaSequenceInterface
//      *QMetaSequence::iface() const
extern "C" Q_DECL_EXPORT
const QtMetaContainerPrivate::QMetaSequenceInterface *ritual_ZNK13QMetaSequence5ifaceEv(
    const QMetaSequence *self) {
  return self->iface();
}

//  bool operator==(const QMetaSequence &lhs, const QMetaSequence &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QMetaSequenceS1_(
    const QMetaSequence *lhs,
    const QMetaSequence *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMetaSequence &lhs, const QMetaSequence &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QMetaSequenceS1_(
    const QMetaSequence *lhs,
    const QMetaSequence *rhs) {
  return operator!=(*lhs, *rhs);
}

//  const QtMetaContainerPrivate::QMetaSequenceInterface *QMetaSequence::d()
//      const
extern "C" Q_DECL_EXPORT
const QtMetaContainerPrivate::QMetaSequenceInterface *ritual_ZNK13QMetaSequence1dEv(
    const QMetaSequence *self) {
  return self->d();
}

//  QMetaSequence::~QMetaSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMetaSequenceD1Ev(QMetaSequence *self) {
  delete self;
}

//  static constexpr QMetaSequence
//      QMetaSequence::fromContainer<QList<int>>()
extern "C" Q_DECL_EXPORT
QMetaSequence * ritual_ZN13QMetaSequence13fromContainerI5QListIiEEES_v() {
  return new QMetaSequence(QMetaSequence::fromContainer<QList<int>>());
}

//  static constexpr QMetaSequence
//      QMetaSequence::fromContainer<QList<double>>()
extern "C" Q_DECL_EXPORT
QMetaSequence * ritual_ZN13QMetaSequence13fromContainerI5QListIdEEES_v() {
  return new QMetaSequence(QMetaSequence::fromContainer<QList<double>>());
}

//  static constexpr QMetaSequence
//      QMetaSequence::fromContainer<QList<QString>>()
extern "C" Q_DECL_EXPORT
QMetaSequence * ritual_ZN13QMetaSequence13fromContainerI5QListI7QStringEEES_v() {
  return new QMetaSequence(QMetaSequence::fromContainer<QList<QString>>());
}

//  static constexpr QMetaSequence
//      QMetaSequence::fromContainer<QList<QVariant>>()
extern "C" Q_DECL_EXPORT
QMetaSequence * ritual_ZN13QMetaSequence13fromContainerI5QListI8QVariantEEES_v() {
  return new QMetaSequence(
      QMetaSequence::fromContainer<QList<QVariant>>());
}

//  static constexpr QMetaSequence
//      QMetaSequence::fromContainer<QList<QByteArray>>()
extern "C" Q_DECL_EXPORT
QMetaSequence * ritual_ZN13QMetaSequence13fromContainerI5QListI10QByteArrayEEES_v() {
  return new QMetaSequence(
      QMetaSequence::fromContainer<QList<QByteArray>>());
}
