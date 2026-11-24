//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qabstractvideobuffer.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMultimedia/qabstractvideobuffer.h>

//  QAbstractVideoBuffer::MapData::~MapData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAbstractVideoBuffer7MapDataD1Ev(
    QAbstractVideoBuffer::MapData *self) {
  delete self;
}
