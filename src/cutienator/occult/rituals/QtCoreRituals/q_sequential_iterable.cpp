//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialiterable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsequentialiterable.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetatype.h>

//  QSequentialIterable::QSequentialIterable()
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC1Ev() {
  return new QSequentialIterable();
}

//  QVariant QSequentialIterable::at(qsizetype idx) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QSequentialIterable2atEx(
    const QSequentialIterable *self,
    qsizetype idx) {
  return new QVariant(self->at(idx));
}

//  void QSequentialIterable::set(qsizetype idx, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSequentialIterable3setExRK8QVariant(
    QSequentialIterable *self,
    qsizetype idx,
    const QVariant *value) {
  self->set(idx, *value);
}

//  void QSequentialIterable::addValue(const QVariant &value, Position
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSequentialIterable8addValueERK8QVariantNS_8PositionE(
    QSequentialIterable *self,
    const QVariant *value,
    QSequentialIterable::Position position) {
  self->addValue(*value, position);
}

//  void QSequentialIterable::removeValue(Position position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSequentialIterable11removeValueENS_8PositionE(
    QSequentialIterable *self,
    QSequentialIterable::Position position) {
  self->removeValue(position);
}

//  QMetaType QSequentialIterable::valueMetaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK19QSequentialIterable13valueMetaTypeEv(
    const QSequentialIterable *self) {
  return new QMetaType(self->valueMetaType());
}

//  bool QSequentialIterable::canRandomAccessIterate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSequentialIterable22canRandomAccessIterateEv(
    const QSequentialIterable *self) {
  return self->canRandomAccessIterate();
}

//  QSequentialIterable::~QSequentialIterable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSequentialIterableD1Ev(QSequentialIterable *self) {
  delete self;
}
