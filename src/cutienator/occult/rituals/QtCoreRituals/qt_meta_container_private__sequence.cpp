//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetasequence.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetasequence.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetatype.h>

//  QtMetaContainerPrivate::Sequence::Sequence()
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::Sequence *ritual_ZN22QtMetaContainerPrivate8SequenceC1Ev() {
  return new QtMetaContainerPrivate::Sequence();
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
