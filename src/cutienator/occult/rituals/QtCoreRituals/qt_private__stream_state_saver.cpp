//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdatastream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(QT_NO_DATASTREAM)
#include <QtCore/qdatastream.h>

//  QtPrivate::StreamStateSaver::StreamStateSaver(QDataStream *s)
extern "C" Q_DECL_EXPORT
QtPrivate::StreamStateSaver *ritual_ZN9QtPrivate16StreamStateSaverC1EP11QDataStream(
    QDataStream *s) {
  return new QtPrivate::StreamStateSaver(s);
}

//  QtPrivate::StreamStateSaver::~StreamStateSaver()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate16StreamStateSaverD1Ev(
    QtPrivate::StreamStateSaver *self) {
  delete self;
}

#endif  // !defined(QT_NO_DATASTREAM)
