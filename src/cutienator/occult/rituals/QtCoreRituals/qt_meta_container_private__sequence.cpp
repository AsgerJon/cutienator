//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetasequence.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 8. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetasequence.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>

//  QtMetaContainerPrivate::Sequence::Sequence()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence *ritual_ZN22QtMetaContainerPrivate8SequenceC1Ev() {
  return new QtMetaContainerPrivate::Sequence();
}

//  QtMetaContainerPrivate::Sequence::Sequence(const QMetaSequence
//      &metaSequence, QMetaType metaType, void *iterable)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence *ritual_ZN22QtMetaContainerPrivate8SequenceC1ERK13QMetaSequence9QMetaTypePv(
    const QMetaSequence *metaSequence,
    const QMetaType *metaType,
    void *iterable) {
  return new QtMetaContainerPrivate::Sequence(
      *metaSequence,
      *metaType,
      iterable);
}

//  QtMetaContainerPrivate::Sequence::Sequence(const QMetaSequence
//      &metaSequence, QMetaType metaType, const void *iterable)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence *ritual_ZN22QtMetaContainerPrivate8SequenceC1ERK13QMetaSequence9QMetaTypePKv(
    const QMetaSequence *metaSequence,
    const QMetaType *metaType,
    const void *iterable) {
  return new QtMetaContainerPrivate::Sequence(
      *metaSequence,
      *metaType,
      iterable);
}

//  QtMetaContainerPrivate::Sequence::Sequence(QIterable<QMetaSequence>
//      &&other)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence *ritual_ZN22QtMetaContainerPrivate8SequenceC1EO9QIterableI13QMetaSequenceE(
    QIterable<QMetaSequence> *other) {
  return new QtMetaContainerPrivate::Sequence(std::move(*other));
}

//  Sequence
//      &QtMetaContainerPrivate::Sequence::operator=(QIterable<QMetaSequence>
//      &&other)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence *ritual_ZN22QtMetaContainerPrivate8SequenceaSEO9QIterableI13QMetaSequenceE(
    QtMetaContainerPrivate::Sequence *self,
    QIterable<QMetaSequence> *other) {
  return &(self->operator=(std::move(*other)));
}

//  ConstIterator QtMetaContainerPrivate::Sequence::begin() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence::ConstIterator *ritual_ZNK22QtMetaContainerPrivate8Sequence5beginEv(
    const QtMetaContainerPrivate::Sequence *self) {
  return new QtMetaContainerPrivate::Sequence::ConstIterator(self->begin());
}

//  ConstIterator QtMetaContainerPrivate::Sequence::end() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence::ConstIterator *ritual_ZNK22QtMetaContainerPrivate8Sequence3endEv(
    const QtMetaContainerPrivate::Sequence *self) {
  return new QtMetaContainerPrivate::Sequence::ConstIterator(self->end());
}

//  ConstIterator QtMetaContainerPrivate::Sequence::constBegin() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence::ConstIterator *ritual_ZNK22QtMetaContainerPrivate8Sequence10constBeginEv(
    const QtMetaContainerPrivate::Sequence *self) {
  return new QtMetaContainerPrivate::Sequence::ConstIterator(
      self->constBegin());
}

//  ConstIterator QtMetaContainerPrivate::Sequence::constEnd() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence::ConstIterator *ritual_ZNK22QtMetaContainerPrivate8Sequence8constEndEv(
    const QtMetaContainerPrivate::Sequence *self) {
  return new QtMetaContainerPrivate::Sequence::ConstIterator(
      self->constEnd());
}

//  Iterator QtMetaContainerPrivate::Sequence::mutableBegin()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence::Iterator *ritual_ZN22QtMetaContainerPrivate8Sequence12mutableBeginEv(
    QtMetaContainerPrivate::Sequence *self) {
  return new QtMetaContainerPrivate::Sequence::Iterator(
      self->mutableBegin());
}

//  Iterator QtMetaContainerPrivate::Sequence::mutableEnd()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence::Iterator *ritual_ZN22QtMetaContainerPrivate8Sequence10mutableEndEv(
    QtMetaContainerPrivate::Sequence *self) {
  return new QtMetaContainerPrivate::Sequence::Iterator(self->mutableEnd());
}

//  QVariant QtMetaContainerPrivate::Sequence::at(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate8Sequence2atEx(
    const QtMetaContainerPrivate::Sequence *self,
    qsizetype idx) {
  return new QVariant(self->at(idx));
}

//  void QtMetaContainerPrivate::Sequence::setAt(qsizetype idx, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence5setAtExRK8QVariant(
    QtMetaContainerPrivate::Sequence *self,
    qsizetype idx,
    const QVariant *value) {
  self->setAt(idx, *value);
}

//  void QtMetaContainerPrivate::Sequence::append(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence6appendERK8QVariant(
    QtMetaContainerPrivate::Sequence *self,
    const QVariant *value) {
  self->append(*value);
}

//  void QtMetaContainerPrivate::Sequence::prepend(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence7prependERK8QVariant(
    QtMetaContainerPrivate::Sequence *self,
    const QVariant *value) {
  self->prepend(*value);
}

//  void QtMetaContainerPrivate::Sequence::removeLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence10removeLastEv(
    QtMetaContainerPrivate::Sequence *self) {
  self->removeLast();
}

//  void QtMetaContainerPrivate::Sequence::removeFirst()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence11removeFirstEv(
    QtMetaContainerPrivate::Sequence *self) {
  self->removeFirst();
}

#if QT_DEPRECATED_SINCE(6, 11)
//  void QtMetaContainerPrivate::Sequence::addValue(const QVariant &value,
//      Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence8addValueERK8QVariantNS0_8PositionE(
    QtMetaContainerPrivate::Sequence *self,
    const QVariant *value,
    QtMetaContainerPrivate::Sequence::Position position) {
  self->addValue(*value, position);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  void QtMetaContainerPrivate::Sequence::removeValue(Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8Sequence11removeValueENS0_8PositionE(
    QtMetaContainerPrivate::Sequence *self,
    QtMetaContainerPrivate::Sequence::Position position) {
  self->removeValue(position);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QMetaType QtMetaContainerPrivate::Sequence::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK22QtMetaContainerPrivate8Sequence13valueMetaTypeEv(
    const QtMetaContainerPrivate::Sequence *self) {
  return new QMetaType(self->valueMetaType());
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

//  QtMetaContainerPrivate::Sequence::~Sequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate8SequenceD1Ev(
    QtMetaContainerPrivate::Sequence *self) {
  delete self;
}

//  a QtMetaContainerPrivate::Sequence::ConstIterator a ritual of
//      QtMetaContainerPrivate::Sequence gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_Sequence__QtMetaContainerPrivate_Sequence_ConstIterator(
    QtMetaContainerPrivate::Sequence::ConstIterator *self) {
  delete self;
}

//  a QtMetaContainerPrivate::Sequence::Iterator a ritual of
//      QtMetaContainerPrivate::Sequence gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_Sequence__QtMetaContainerPrivate_Sequence_Iterator(
    QtMetaContainerPrivate::Sequence::Iterator *self) {
  delete self;
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<int>>(const QList<int>
//      *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListIiEEEPKT_(
    const QList<int> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<double>>(const
//      QList<double> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListIdEEEPKT_(
    const QList<double> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<QString>>(const
//      QList<QString> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListI7QStringEEEPKT_(
    const QList<QString> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<QVariant>>(const
//      QList<QVariant> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListI8QVariantEEEPKT_(
    const QList<QVariant> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<int>>(QList<int> *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListIiEEEPT_(
    QList<int> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<double>>(QList<double>
//      *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListIdEEEPT_(
    QList<double> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  QtMetaContainerPrivate::Sequence::Sequence<QList<QString>>(QList<QString>
//      *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListI7QStringEEEPT_(
    QList<QString> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}

//  
//      QtMetaContainerPrivate::Sequence::Sequence<QList<QVariant>>(QList<QVariant>
//      *p)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence * ritual_ZN22QtMetaContainerPrivate8SequenceC2I5QListI8QVariantEEEPT_(
    QList<QVariant> *p) {
  return new QtMetaContainerPrivate::Sequence(p);
}
