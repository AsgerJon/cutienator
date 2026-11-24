//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdistancefield_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdistancefield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qpainterpath.h>

//  QDistanceFieldData::QDistanceFieldData()
extern "C" Q_DECL_EXPORT
QDistanceFieldData *ritual_ZN18QDistanceFieldDataC1Ev() {
  return new QDistanceFieldData();
}

//  QDistanceFieldData::QDistanceFieldData(const QDistanceFieldData &other)
extern "C" Q_DECL_EXPORT
QDistanceFieldData *ritual_ZN18QDistanceFieldDataC1ERKS_(
    const QDistanceFieldData *other) {
  return new QDistanceFieldData(*other);
}

//  QDistanceFieldData::~QDistanceFieldData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDistanceFieldDataD1Ev(QDistanceFieldData *self) {
  delete self;
}

//  QDistanceFieldData *QDistanceFieldData::create(const QSize &size)
extern "C" Q_DECL_EXPORT
QDistanceFieldData *ritual_ZN18QDistanceFieldData6createERK5QSize(
    const QSize *size) {
  return QDistanceFieldData::create(*size);
}

//  QDistanceFieldData *QDistanceFieldData::create(const QPainterPath &path,
//      bool doubleResolution)
extern "C" Q_DECL_EXPORT
QDistanceFieldData *ritual_ZN18QDistanceFieldData6createERK12QPainterPathb(
    const QPainterPath *path,
    bool doubleResolution) {
  return QDistanceFieldData::create(*path, doubleResolution);
}

//  QDistanceFieldData *QDistanceFieldData::create(QSize size, const
//      QPainterPath &path, bool doubleResolution)
extern "C" Q_DECL_EXPORT
QDistanceFieldData *ritual_ZN18QDistanceFieldData6createE5QSizeRK12QPainterPathb(
    const QSize *size,
    const QPainterPath *path,
    bool doubleResolution) {
  return QDistanceFieldData::create(*size, *path, doubleResolution);
}
