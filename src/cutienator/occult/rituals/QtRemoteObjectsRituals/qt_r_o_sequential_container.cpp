//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qremoteobjectcontainers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetasequence.h>
#include <QtCore/qbytearray.h>

//  QtROSequentialContainer::QtROSequentialContainer()
extern "C" Q_DECL_EXPORT
QtROSequentialContainer *ritual_ZN23QtROSequentialContainerC1Ev() {
  return new QtROSequentialContainer();
}

//  QtROSequentialContainer::QtROSequentialContainer(const
//      QMetaSequence::Iterable &lst)
extern "C" Q_DECL_EXPORT
QtROSequentialContainer *ritual_ZN23QtROSequentialContainerC1ERKN22QtMetaContainerPrivate8SequenceE(
    const QtMetaContainerPrivate::Sequence *lst) {
  return new QtROSequentialContainer(*lst);
}

//  void QtROSequentialContainer::setValueType(const QByteArray
//      &valueTypeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QtROSequentialContainer12setValueTypeERK10QByteArray(
    QtROSequentialContainer *self,
    const QByteArray *valueTypeName) {
  self->setValueType(*valueTypeName);
}

//  QtROSequentialContainer::~QtROSequentialContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QtROSequentialContainerD1Ev(QtROSequentialContainer *self) {
  delete self;
}
