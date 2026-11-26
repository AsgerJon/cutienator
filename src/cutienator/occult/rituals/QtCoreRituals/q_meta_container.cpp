//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetacontainer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetacontainer.h>

//  QMetaContainer::QMetaContainer()
extern "C" Q_DECL_EXPORT
QMetaContainer *ritual_ZN14QMetaContainerC1Ev() {
  return new QMetaContainer();
}

//  QMetaContainer::QMetaContainer(const
//      QtMetaContainerPrivate::QMetaContainerInterface *d)
extern "C" Q_DECL_EXPORT
QMetaContainer *ritual_ZN14QMetaContainerC1EPKN22QtMetaContainerPrivate23QMetaContainerInterfaceE(
    const QtMetaContainerPrivate::QMetaContainerInterface *d) {
  return new QMetaContainer(d);
}

//  bool QMetaContainer::hasInputIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer16hasInputIteratorEv(
    const QMetaContainer *self) {
  return self->hasInputIterator();
}

//  bool QMetaContainer::hasForwardIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer18hasForwardIteratorEv(
    const QMetaContainer *self) {
  return self->hasForwardIterator();
}

//  bool QMetaContainer::hasBidirectionalIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer24hasBidirectionalIteratorEv(
    const QMetaContainer *self) {
  return self->hasBidirectionalIterator();
}

//  bool QMetaContainer::hasRandomAccessIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer23hasRandomAccessIteratorEv(
    const QMetaContainer *self) {
  return self->hasRandomAccessIterator();
}

//  bool QMetaContainer::hasSize() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer7hasSizeEv(const QMetaContainer *self) {
  return self->hasSize();
}

//  qsizetype QMetaContainer::size(const void *container) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QMetaContainer4sizeEPKv(
    const QMetaContainer *self,
    const void *container) {
  return self->size(container);
}

//  bool QMetaContainer::canClear() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer8canClearEv(const QMetaContainer *self) {
  return self->canClear();
}

//  void QMetaContainer::clear(void *container) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer5clearEPv(
    const QMetaContainer *self,
    void *container) {
  self->clear(container);
}

//  bool QMetaContainer::hasIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer11hasIteratorEv(const QMetaContainer *self) {
  return self->hasIterator();
}

//  void *QMetaContainer::begin(void *container) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QMetaContainer5beginEPv(
    const QMetaContainer *self,
    void *container) {
  return self->begin(container);
}

//  void *QMetaContainer::end(void *container) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QMetaContainer3endEPv(
    const QMetaContainer *self,
    void *container) {
  return self->end(container);
}

//  void QMetaContainer::destroyIterator(const void *iterator) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer15destroyIteratorEPKv(
    const QMetaContainer *self,
    const void *iterator) {
  self->destroyIterator(iterator);
}

//  bool QMetaContainer::compareIterator(const void *i, const void *j) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer15compareIteratorEPKvS1_(
    const QMetaContainer *self,
    const void *i,
    const void *j) {
  return self->compareIterator(i, j);
}

//  void QMetaContainer::copyIterator(void *target, const void *source) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer12copyIteratorEPvPKv(
    const QMetaContainer *self,
    void *target,
    const void *source) {
  self->copyIterator(target, source);
}

//  void QMetaContainer::advanceIterator(void *iterator, qsizetype step)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer15advanceIteratorEPvx(
    const QMetaContainer *self,
    void *iterator,
    qsizetype step) {
  self->advanceIterator(iterator, step);
}

//  qsizetype QMetaContainer::diffIterator(const void *i, const void *j)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QMetaContainer12diffIteratorEPKvS1_(
    const QMetaContainer *self,
    const void *i,
    const void *j) {
  return self->diffIterator(i, j);
}

//  bool QMetaContainer::hasConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer16hasConstIteratorEv(
    const QMetaContainer *self) {
  return self->hasConstIterator();
}

//  void *QMetaContainer::constBegin(const void *container) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QMetaContainer10constBeginEPKv(
    const QMetaContainer *self,
    const void *container) {
  return self->constBegin(container);
}

//  void *QMetaContainer::constEnd(const void *container) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QMetaContainer8constEndEPKv(
    const QMetaContainer *self,
    const void *container) {
  return self->constEnd(container);
}

//  void QMetaContainer::destroyConstIterator(const void *iterator) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer20destroyConstIteratorEPKv(
    const QMetaContainer *self,
    const void *iterator) {
  self->destroyConstIterator(iterator);
}

//  bool QMetaContainer::compareConstIterator(const void *i, const void *j)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer20compareConstIteratorEPKvS1_(
    const QMetaContainer *self,
    const void *i,
    const void *j) {
  return self->compareConstIterator(i, j);
}

//  void QMetaContainer::copyConstIterator(void *target, const void *source)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer17copyConstIteratorEPvPKv(
    const QMetaContainer *self,
    void *target,
    const void *source) {
  self->copyConstIterator(target, source);
}

//  void QMetaContainer::advanceConstIterator(void *iterator, qsizetype step)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QMetaContainer20advanceConstIteratorEPvx(
    const QMetaContainer *self,
    void *iterator,
    qsizetype step) {
  self->advanceConstIterator(iterator, step);
}

//  qsizetype QMetaContainer::diffConstIterator(const void *i, const void *j)
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK14QMetaContainer17diffConstIteratorEPKvS1_(
    const QMetaContainer *self,
    const void *i,
    const void *j) {
  return self->diffConstIterator(i, j);
}

//  QMetaContainer::~QMetaContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMetaContainerD1Ev(QMetaContainer *self) {
  delete self;
}
