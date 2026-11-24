//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeoshape.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/qgeoshape.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeoshape.h"
#include "qgeoshape_p.h"
#include "qgeorectangle.h"
#include "qgeocircle.h"
#include "qgeopath.h"
#include "qgeopolygon.h"
#ifndef QT_NO_DEBUG_STREAM
#include <QtCore/QDebug>
#endif
#ifndef QT_NO_DATASTREAM
#include <QtCore/QDataStream>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 105, as _ZN9QGeoShape6d_funcEv
inline QGeoShapePrivate *QGeoShape::d_func()
{
    return static_cast<QGeoShapePrivate *>(d_ptr.data());
}

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 110, as _ZNK9QGeoShape6d_funcEv
inline const QGeoShapePrivate *QGeoShape::d_func() const
{
    return static_cast<const QGeoShapePrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QGeoShape::QGeoShape()
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZN9QGeoShapeC1Ev() {
  return new QGeoShape();
}

//  QGeoShape::QGeoShape(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZN9QGeoShapeC1ERKS_(const QGeoShape *other) {
  return new QGeoShape(*other);
}

//  QGeoShape::~QGeoShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoShapeD1Ev(QGeoShape *self) {
  delete self;
}

//  ShapeType QGeoShape::type() const
extern "C" Q_DECL_EXPORT
QGeoShape::ShapeType ritual_ZNK9QGeoShape4typeEv(const QGeoShape *self) {
  return self->type();
}

//  bool QGeoShape::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGeoShape7isValidEv(const QGeoShape *self) {
  return self->isValid();
}

//  bool QGeoShape::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGeoShape7isEmptyEv(const QGeoShape *self) {
  return self->isEmpty();
}

//  bool QGeoShape::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGeoShape8containsERK14QGeoCoordinate(
    const QGeoShape *self,
    const QGeoCoordinate *coordinate) {
  return self->contains(*coordinate);
}

//  QGeoRectangle QGeoShape::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK9QGeoShape20boundingGeoRectangleEv(
    const QGeoShape *self) {
  return new QGeoRectangle(self->boundingGeoRectangle());
}

//  QGeoCoordinate QGeoShape::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK9QGeoShape6centerEv(const QGeoShape *self) {
  return new QGeoCoordinate(self->center());
}

//  bool operator==(const QGeoShape &lhs, const QGeoShape &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QGeoShapeS1_(const QGeoShape *lhs, const QGeoShape *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoShape &lhs, const QGeoShape &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QGeoShapeS1_(const QGeoShape *lhs, const QGeoShape *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QGeoShape::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QGeoShape8toStringEv(const QGeoShape *self) {
  return new QString(self->toString());
}

//  QGeoShape::QGeoShape(QGeoShapePrivate *d)
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZN9QGeoShapeC1EP16QGeoShapePrivate(QGeoShapePrivate *d) {
  return new QGeoShape(d);
}

//  bool QGeoShape::equals(const QGeoShape &lhs, const QGeoShape &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QGeoShape6equalsERKS_S1_(
    const QGeoShape *lhs,
    const QGeoShape *rhs) {
  return QGeoShape::equals(*lhs, *rhs);
}

//  QGeoShapePrivate *QGeoShape::d_func()
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZN9QGeoShape6d_funcEv(QGeoShape *self) {
  return self->d_func();
}

//  const QGeoShapePrivate *QGeoShape::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoShapePrivate *ritual_ZNK9QGeoShape6d_funcEv(
    const QGeoShape *self) {
  return self->d_func();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK9QGeoShape(
    const QDebug *dbg,
    const QGeoShape *shape) {
  return new QDebug(operator<<(*dbg, *shape));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QGeoShape::debugStreaming(QDebug dbg, const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN9QGeoShape14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QGeoShape *shape) {
  return new QDebug(QGeoShape::debugStreaming(*dbg, *shape));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
