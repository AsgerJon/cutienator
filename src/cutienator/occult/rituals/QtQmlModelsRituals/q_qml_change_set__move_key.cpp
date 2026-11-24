//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlchangeset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlChangeSet::MoveKey::MoveKey()
extern "C" Q_DECL_EXPORT
QQmlChangeSet::MoveKey *ritual_ZN13QQmlChangeSet7MoveKeyC1Ev() {
  return new QQmlChangeSet::MoveKey();
}

//  QQmlChangeSet::MoveKey::MoveKey(int moveId, int offset)
extern "C" Q_DECL_EXPORT
QQmlChangeSet::MoveKey *ritual_ZN13QQmlChangeSet7MoveKeyC1Eii(
    int moveId,
    int offset) {
  return new QQmlChangeSet::MoveKey(moveId, offset);
}

//  QQmlChangeSet::MoveKey::~MoveKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlChangeSet7MoveKeyD1Ev(QQmlChangeSet::MoveKey *self) {
  delete self;
}
