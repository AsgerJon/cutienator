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

//  bool QMetaContainer::canClear() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer8canClearEv(const QMetaContainer *self) {
  return self->canClear();
}

//  bool QMetaContainer::hasIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer11hasIteratorEv(const QMetaContainer *self) {
  return self->hasIterator();
}

//  bool QMetaContainer::hasConstIterator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QMetaContainer16hasConstIteratorEv(
    const QMetaContainer *self) {
  return self->hasConstIterator();
}

//  QMetaContainer::~QMetaContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QMetaContainerD1Ev(QMetaContainer *self) {
  delete self;
}
