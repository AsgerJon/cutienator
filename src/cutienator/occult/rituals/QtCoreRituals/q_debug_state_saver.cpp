//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdebug.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdebug.h>

//  QDebugStateSaver::QDebugStateSaver(QDebug &dbg)
extern "C" Q_DECL_EXPORT
QDebugStateSaver *ritual_ZN16QDebugStateSaverC1ER6QDebug(QDebug *dbg) {
  return new QDebugStateSaver(*dbg);
}

//  QDebugStateSaver::~QDebugStateSaver()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDebugStateSaverD1Ev(QDebugStateSaver *self) {
  delete self;
}
