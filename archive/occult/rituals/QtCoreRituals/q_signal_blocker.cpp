//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobject.h>

//  QSignalBlocker::QSignalBlocker(QObject *o)
extern "C" Q_DECL_EXPORT
QSignalBlocker *ritual_ZN14QSignalBlockerC1EP7QObject(QObject *o) {
  return new QSignalBlocker(o);
}

//  QSignalBlocker::~QSignalBlocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSignalBlockerD1Ev(QSignalBlocker *self) {
  delete self;
}

//  void QSignalBlocker::reblock()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSignalBlocker7reblockEv(QSignalBlocker *self) {
  self->reblock();
}

//  void QSignalBlocker::unblock()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSignalBlocker7unblockEv(QSignalBlocker *self) {
  self->unblock();
}

//  void QSignalBlocker::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSignalBlocker7dismissEv(QSignalBlocker *self) {
  self->dismiss();
}
