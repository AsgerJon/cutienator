//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qmetacontainer.h>

//  bool QV4::Heap::Sequence::isStoredInline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap8Sequence14isStoredInlineEv(
    const QV4::Heap::Sequence *self) {
  return self->isStoredInline();
}

//  bool QV4::Heap::Sequence::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap8Sequence10isReadOnlyEv(
    const QV4::Heap::Sequence *self) {
  return self->isReadOnly();
}

//  QMetaType QV4::Heap::Sequence::listType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap8Sequence8listTypeEv(
    const QV4::Heap::Sequence *self) {
  return new QMetaType(self->listType());
}

//  QMetaType QV4::Heap::Sequence::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV44Heap8Sequence13valueMetaTypeEv(
    const QV4::Heap::Sequence *self) {
  return new QMetaType(self->valueMetaType());
}

//  QMetaSequence QV4::Heap::Sequence::metaSequence() const
extern "C" Q_DECL_EXPORT
QMetaSequence *ritual_ZNK3QV44Heap8Sequence12metaSequenceEv(
    const QV4::Heap::Sequence *self) {
  return new QMetaSequence(self->metaSequence());
}
