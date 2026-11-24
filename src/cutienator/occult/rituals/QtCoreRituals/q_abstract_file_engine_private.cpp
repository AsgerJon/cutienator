//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAbstractFileEnginePrivate::~QAbstractFileEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractFileEnginePrivateD1Ev(
    QAbstractFileEnginePrivate *self) {
  delete self;
}

//  QAbstractFileEngine *QAbstractFileEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_ZN26QAbstractFileEnginePrivate6q_funcEv(
    QAbstractFileEnginePrivate *self) {
  return self->q_func();
}

//  const QAbstractFileEngine *QAbstractFileEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractFileEngine *ritual_ZNK26QAbstractFileEnginePrivate6q_funcEv(
    const QAbstractFileEnginePrivate *self) {
  return self->q_func();
}
