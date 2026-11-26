//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainterpath_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainterpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVectorPathConverter::QVectorPathConverter(const
//      QList<QPainterPath::Element> &path, bool hasWindingFill, bool convex)
extern "C" Q_DECL_EXPORT
QVectorPathConverter *ritual_ZN20QVectorPathConverterC1ERK5QListIN12QPainterPath7ElementEEbb(
    const QList<QPainterPath::Element> *path,
    bool hasWindingFill,
    bool convex) {
  return new QVectorPathConverter(*path, hasWindingFill, convex);
}

//  const QVectorPath &QVectorPathConverter::vectorPath()
extern "C" Q_DECL_EXPORT
const QVectorPath *ritual_ZN20QVectorPathConverter10vectorPathEv(
    QVectorPathConverter *self) {
  return &(self->vectorPath());
}
