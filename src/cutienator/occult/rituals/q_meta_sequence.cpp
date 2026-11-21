//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>

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

//  bool QMetaSequence::canAddValueAtEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence16canAddValueAtEndEv(
    const QMetaSequence *self) {
  return self->canAddValueAtEnd();
}

//  bool QMetaSequence::canRemoveValueAtBegin() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence21canRemoveValueAtBeginEv(
    const QMetaSequence *self) {
  return self->canRemoveValueAtBegin();
}

//  bool QMetaSequence::canRemoveValueAtEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence19canRemoveValueAtEndEv(
    const QMetaSequence *self) {
  return self->canRemoveValueAtEnd();
}

//  bool QMetaSequence::canGetValueAtIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence18canGetValueAtIndexEv(
    const QMetaSequence *self) {
  return self->canGetValueAtIndex();
}

//  bool QMetaSequence::canSetValueAtIndex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence18canSetValueAtIndexEv(
    const QMetaSequence *self) {
  return self->canSetValueAtIndex();
}

//  bool QMetaSequence::canAddValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence11canAddValueEv(const QMetaSequence *self) {
  return self->canAddValue();
}

//  bool QMetaSequence::canRemoveValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence14canRemoveValueEv(const QMetaSequence *self) {
  return self->canRemoveValue();
}

//  bool QMetaSequence::canGetValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence21canGetValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canGetValueAtIterator();
}

//  bool QMetaSequence::canSetValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence21canSetValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canSetValueAtIterator();
}

//  bool QMetaSequence::canInsertValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence24canInsertValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canInsertValueAtIterator();
}

//  bool QMetaSequence::canEraseValueAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence23canEraseValueAtIteratorEv(
    const QMetaSequence *self) {
  return self->canEraseValueAtIterator();
}

//  bool QMetaSequence::canEraseRangeAtIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence23canEraseRangeAtIteratorEv(
    const QMetaSequence *self) {
  return self->canEraseRangeAtIterator();
}

//  bool QMetaSequence::canGetValueAtConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMetaSequence26canGetValueAtConstIteratorEv(
    const QMetaSequence *self) {
  return self->canGetValueAtConstIterator();
}

//  const QtMetaContainerPrivate::QMetaSequenceInterface
//      *QMetaSequence::iface() const
extern "C" Q_DECL_EXPORT
const QtMetaContainerPrivate::QMetaSequenceInterface *ritual_ZNK13QMetaSequence5ifaceEv(
    const QMetaSequence *self) {
  return self->iface();
}

//  QMetaSequence::~QMetaSequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMetaSequenceD1Ev(QMetaSequence *self) {
  delete self;
}
