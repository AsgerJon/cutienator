//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialiterable.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, instances of templates of the class: 5; on 2026-11-27: the
//  ritual of the destructor the compiler writes for the class, which its
//  cute class calls to remove what Python holds, and which the generator no
//  longer writes for it. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qsequentialiterable.h>
#include <QtCore/qmetacontainer.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/QSequentialIterable>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>

//  QSequentialIterable::QSequentialIterable()
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC1Ev() {
  return new QSequentialIterable();
}

//  QSequentialIterable::QSequentialIterable(const QMetaSequence
//      &metaSequence, const QMetaType &metaType, void *iterable)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC1ERK13QMetaSequenceRK9QMetaTypePv(
    const QMetaSequence *metaSequence,
    const QMetaType *metaType,
    void *iterable) {
  return new QSequentialIterable(*metaSequence, *metaType, iterable);
}

//  QSequentialIterable::QSequentialIterable(const QMetaSequence
//      &metaSequence, const QMetaType &metaType, const void *iterable)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC1ERK13QMetaSequenceRK9QMetaTypePKv(
    const QMetaSequence *metaSequence,
    const QMetaType *metaType,
    const void *iterable) {
  return new QSequentialIterable(*metaSequence, *metaType, iterable);
}

//  QSequentialIterable::QSequentialIterable(QIterable<QMetaSequence>
//      &&other)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC1EO9QIterableI13QMetaSequenceE(
    QIterable<QMetaSequence> *other) {
  return new QSequentialIterable(std::move(*other));
}

//  QSequentialIterable
//      &QSequentialIterable::operator=(QIterable<QMetaSequence> &&other)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableaSEO9QIterableI13QMetaSequenceE(
    QSequentialIterable *self,
    QIterable<QMetaSequence> *other) {
  return &(self->operator=(std::move(*other)));
}

//  const_iterator QSequentialIterable::begin() const
extern "C" Q_DECL_EXPORT
QSequentialIterable::const_iterator *ritual_ZNK19QSequentialIterable5beginEv(
    const QSequentialIterable *self) {
  return new QSequentialIterable::const_iterator(self->begin());
}

//  const_iterator QSequentialIterable::end() const
extern "C" Q_DECL_EXPORT
QSequentialIterable::const_iterator *ritual_ZNK19QSequentialIterable3endEv(
    const QSequentialIterable *self) {
  return new QSequentialIterable::const_iterator(self->end());
}

//  const_iterator QSequentialIterable::constBegin() const
extern "C" Q_DECL_EXPORT
QSequentialIterable::const_iterator *ritual_ZNK19QSequentialIterable10constBeginEv(
    const QSequentialIterable *self) {
  return new QSequentialIterable::const_iterator(self->constBegin());
}

//  const_iterator QSequentialIterable::constEnd() const
extern "C" Q_DECL_EXPORT
QSequentialIterable::const_iterator *ritual_ZNK19QSequentialIterable8constEndEv(
    const QSequentialIterable *self) {
  return new QSequentialIterable::const_iterator(self->constEnd());
}

//  iterator QSequentialIterable::mutableBegin()
extern "C" Q_DECL_EXPORT
QSequentialIterable::iterator *ritual_ZN19QSequentialIterable12mutableBeginEv(
    QSequentialIterable *self) {
  return new QSequentialIterable::iterator(self->mutableBegin());
}

//  iterator QSequentialIterable::mutableEnd()
extern "C" Q_DECL_EXPORT
QSequentialIterable::iterator *ritual_ZN19QSequentialIterable10mutableEndEv(
    QSequentialIterable *self) {
  return new QSequentialIterable::iterator(self->mutableEnd());
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

//  a QSequentialIterable::const_iterator a ritual of QSequentialIterable
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSequentialIterable__QSequentialIterable_const_iterator(
    QSequentialIterable::const_iterator *self) {
  delete self;
}

//  a QSequentialIterable::iterator a ritual of QSequentialIterable gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSequentialIterable__QSequentialIterable_iterator(
    QSequentialIterable::iterator *self) {
  delete self;
}

//  QSequentialIterable::QSequentialIterable(QList<QVariant> *p)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC2I5QListI8QVariantEEEPT_(
    QList<QVariant> *p) {
  return new QSequentialIterable(p);
}

//  QSequentialIterable::QSequentialIterable(const QList<QVariant> *p)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC2I5QListI8QVariantEEEPKT_(
    const QList<QVariant> *p) {
  return new QSequentialIterable(p);
}

//  QSequentialIterable::QSequentialIterable(QList<QString> *p)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC2I5QListI7QStringEEEPT_(
    QList<QString> *p) {
  return new QSequentialIterable(p);
}

//  QSequentialIterable::QSequentialIterable(const QList<QString> *p)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC2I5QListI7QStringEEEPKT_(
    const QList<QString> *p) {
  return new QSequentialIterable(p);
}

//  QSequentialIterable::QSequentialIterable(QList<int> *p)
extern "C" Q_DECL_EXPORT
QSequentialIterable *ritual_ZN19QSequentialIterableC2I5QListIiEEEPT_(
    QList<int> *p) {
  return new QSequentialIterable(p);
}

//  QSequentialIterable::~QSequentialIterable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSequentialIterableD1Ev(QSequentialIterable *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
