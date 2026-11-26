//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainterpath_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainterpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVectorPathConverter::QVectorPathData::QVectorPathData(const
//      QList<QPainterPath::Element> &path, bool hasWindingFill, bool convex)
extern "C" Q_DECL_EXPORT
QVectorPathConverter::QVectorPathData *ritual_ZN20QVectorPathConverter15QVectorPathDataC1ERK5QListIN12QPainterPath7ElementEEbb(
    const QList<QPainterPath::Element> *path,
    bool hasWindingFill,
    bool convex) {
  return new QVectorPathConverter::QVectorPathData(
      *path,
      hasWindingFill,
      convex);
}

//  QVectorPathConverter::QVectorPathData::~QVectorPathData()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVectorPathConverter15QVectorPathDataD1Ev(
    QVectorPathConverter::QVectorPathData *self) {
  delete self;
}
