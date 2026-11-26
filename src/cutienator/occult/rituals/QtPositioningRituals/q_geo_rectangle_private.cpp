//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeorectangle_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeorectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeoshape.h>
#include <QtPositioning/private/qgeoshape_p.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtPositioning/qgeocircle.h>
#include <QtPositioning/qgeopath.h>
#include <QtPositioning/qgeopolygon.h>
#ifndef QT_NO_DEBUG_STREAM
#include <QtCore/QDebug>
#endif
#ifndef QT_NO_DATASTREAM
#include <QtCore/QDataStream>
#endif
#include <QtPositioning/qgeorectangle.h>
#include <QtPositioning/private/qgeorectangle_p.h>
#include <QtPositioning/private/qwebmercator_p.h>
#include <QtPositioning/private/qdoublevector2d_p.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qnumeric.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtCore/QList>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 25, as _ZN16QGeoShapePrivateC2EN9QGeoShape9ShapeTypeE
inline QGeoShapePrivate::QGeoShapePrivate(QGeoShape::ShapeType type)
:   type(type)
{
}

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 30, as _ZN16QGeoShapePrivateD2Ev
inline QGeoShapePrivate::~QGeoShapePrivate()
{
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 590, as _ZNK20QGeoRectanglePrivate20boundingGeoRectangleEv
inline QGeoRectangle QGeoRectanglePrivate::boundingGeoRectangle() const
{
    return QGeoRectangle(topLeft, bottomRight);
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 915, as _ZNK20QGeoRectanglePrivate4hashEm
inline size_t QGeoRectanglePrivate::hash(size_t seed) const
{
    return qHashMulti(seed, topLeft, bottomRight);
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 900, as _ZNK20QGeoRectanglePrivate5cloneEv
inline QGeoShapePrivate *QGeoRectanglePrivate::clone() const
{
    return new QGeoRectanglePrivate(*this);
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 575, as _ZNK20QGeoRectanglePrivate6centerEv
inline QGeoCoordinate QGeoRectanglePrivate::center() const
{
    if (!isValid())
        return QGeoCoordinate();

    double cLat = (topLeft.latitude() + bottomRight.latitude()) / 2.0;
    double cLon = (bottomRight.longitude() + topLeft.longitude()) / 2.0;

    if (topLeft.longitude() > bottomRight.longitude())
        cLon = cLon - 180.0;

    cLon = QLocationUtils::wrapLong(cLon);
    return QGeoCoordinate(cLat, cLon);
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 254, as _ZNK20QGeoRectanglePrivate7isEmptyEv
inline bool QGeoRectanglePrivate::isEmpty() const
{
    if (!isValid())
        return true;

    return topLeft.latitude() == bottomRight.latitude() ||
           topLeft.longitude() == bottomRight.longitude();
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 248, as _ZNK20QGeoRectanglePrivate7isValidEv
inline bool QGeoRectanglePrivate::isValid() const
{
    return topLeft.isValid() && bottomRight.isValid() &&
           topLeft.latitude() >= bottomRight.latitude();
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 540, as _ZNK20QGeoRectanglePrivate8containsERK14QGeoCoordinate
inline bool QGeoRectanglePrivate::contains(const QGeoCoordinate &coordinate) const
{
    if (!isValid() || !coordinate.isValid())
        return false;

    double left = topLeft.longitude();
    double right = bottomRight.longitude();
    double top = topLeft.latitude();
    double bottom = bottomRight.latitude();

    double lon = coordinate.longitude();
    double lat = coordinate.latitude();

    if (lat > top)
        return false;
    if (lat < bottom)
        return false;

    if ((lat == 90.0) && (top == 90.0))
        return true;

    if ((lat == -90.0) && (bottom == -90.0))
        return true;

    if (left <= right) {
        if ((lon < left) || (lon > right))
            return false;
    } else {
        if ((lon < left) && (lon > right))
            return false;
    }

    return true;
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 905, as _ZNK20QGeoRectanglePrivateeqERK16QGeoShapePrivate
inline bool QGeoRectanglePrivate::operator==(const QGeoShapePrivate &other) const
{
    if (!QGeoShapePrivate::operator==(other))
        return false;

    const QGeoRectanglePrivate &otherBox = static_cast<const QGeoRectanglePrivate &>(other);

    return topLeft == otherBox.topLeft && bottomRight == otherBox.bottomRight;
}

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 34, as _ZNK16QGeoShapePrivateeqERKS_
inline bool QGeoShapePrivate::operator==(const QGeoShapePrivate &other) const
{
    return type == other.type;
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 881, as _ZN20QGeoRectanglePrivateC1Ev
inline QGeoRectanglePrivate::QGeoRectanglePrivate()
:   QGeoShapePrivate(QGeoShape::RectangleType)
{
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 886, as _ZN20QGeoRectanglePrivateC1ERK14QGeoCoordinateS2_
inline QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoCoordinate &topLeft,
                                               const QGeoCoordinate &bottomRight)
:   QGeoShapePrivate(QGeoShape::RectangleType), topLeft(topLeft), bottomRight(bottomRight)
{
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 892, as _ZN20QGeoRectanglePrivateC1ERKS_
inline QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoRectanglePrivate &other)
:   QGeoShapePrivate(QGeoShape::RectangleType), topLeft(other.topLeft),
    bottomRight(other.bottomRight)
{
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 898, as _ZN20QGeoRectanglePrivateD1Ev
inline QGeoRectanglePrivate::~QGeoRectanglePrivate() {}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 753, as _ZN20QGeoRectanglePrivate15extendRectangleERK14QGeoCoordinate
inline void QGeoRectanglePrivate::extendRectangle(const QGeoCoordinate &coordinate)
{
    if (!isValid() || !coordinate.isValid() || contains(coordinate))
        return;

    double left = topLeft.longitude();
    double right = bottomRight.longitude();
    double top = topLeft.latitude();
    double bottom = bottomRight.latitude();

    double inputLat = coordinate.latitude();
    double inputLon = coordinate.longitude();

    top = qMax(top, inputLat);
    bottom = qMin(bottom, inputLat);

    bool wrap = left > right;

    if (wrap && inputLon > right && inputLon < left) {
        if (qAbs(left - inputLon) < qAbs(right - inputLon))
            left = inputLon;
        else
            right = inputLon;
    } else if (!wrap) {
        if (inputLon < left) {
            if (360 - (right - inputLon) < left - inputLon)
                right = inputLon;
            else
                left = inputLon;
        } else if (inputLon > right) {
            if (360 - (inputLon - left) < inputLon - right)
                left = inputLon;
            else
                right = inputLon;
        }
    }
    topLeft = QGeoCoordinate(top, left);
    bottomRight = QGeoCoordinate(bottom, right);
}
//  -----------------------------------------------------------------------

//  A QGeoRectanglePrivate that Python can take functions over in. Every QGeoRectanglePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoRectanglePrivateCall0)(const void *, int *);
typedef bool (*CuteQGeoRectanglePrivateCall1)(const void *, int *);
typedef bool (*CuteQGeoRectanglePrivateCall2)(const void *, const QGeoCoordinate *, int *);
typedef const QGeoCoordinate * (*CuteQGeoRectanglePrivateCall3)(const void *, int *);
typedef const QGeoRectangle * (*CuteQGeoRectanglePrivateCall4)(const void *, int *);
typedef void * (*CuteQGeoRectanglePrivateCall5)(const void *, int *);
typedef size_t (*CuteQGeoRectanglePrivateCall6)(const void *, size_t, int *);
class CuteQGeoRectanglePrivate : public QGeoRectanglePrivate {
public:
  using QGeoRectanglePrivate::QGeoRectanglePrivate;
  CuteQGeoRectanglePrivate(const QGeoRectanglePrivate & other) : QGeoRectanglePrivate(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isEmptyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate6centerEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate20boundingGeoRectangleEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate5cloneEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate4hashEm")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QGeoRectanglePrivate::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall0 call = reinterpret_cast<CuteQGeoRectanglePrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoRectanglePrivate::isValid();
  }

  //  bool QGeoRectanglePrivate::isEmpty() const
  bool isEmpty() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall1 call = reinterpret_cast<CuteQGeoRectanglePrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoRectanglePrivate::isEmpty();
  }

  //  bool QGeoRectanglePrivate::contains(const QGeoCoordinate &coordinate)
  //      const
  bool contains(const QGeoCoordinate &coordinate) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall2 call = reinterpret_cast<CuteQGeoRectanglePrivateCall2>(taken[2]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoRectanglePrivate::contains(coordinate);
  }

  //  QGeoCoordinate QGeoRectanglePrivate::center() const
  QGeoCoordinate center() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall3 call = reinterpret_cast<CuteQGeoRectanglePrivateCall3>(taken[3]);
      const QGeoCoordinate * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoRectanglePrivate::center();
  }

  //  QGeoRectangle QGeoRectanglePrivate::boundingGeoRectangle() const
  QGeoRectangle boundingGeoRectangle() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall4 call = reinterpret_cast<CuteQGeoRectanglePrivateCall4>(taken[4]);
      const QGeoRectangle * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoRectanglePrivate::boundingGeoRectangle();
  }

  //  QGeoShapePrivate *QGeoRectanglePrivate::clone() const
  QGeoShapePrivate *clone() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall5 call = reinterpret_cast<CuteQGeoRectanglePrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoShapePrivate *>(given);
    }
    return QGeoRectanglePrivate::clone();
  }

  //  size_t QGeoRectanglePrivate::hash(size_t seed) const
  size_t hash(size_t seed) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoRectanglePrivateCall6 call = reinterpret_cast<CuteQGeoRectanglePrivateCall6>(taken[6]);
      size_t given = call(this, seed, &handled);
      if (handled) return given;
    }
    return QGeoRectanglePrivate::hash(seed);
  }
};

//  QGeoRectanglePrivate::QGeoRectanglePrivate()
extern "C" Q_DECL_EXPORT
QGeoRectanglePrivate *ritual_ZN20QGeoRectanglePrivateC1Ev() {
  return new CuteQGeoRectanglePrivate();
}

//  QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoCoordinate &topLeft,
//      const QGeoCoordinate &bottomRight)
extern "C" Q_DECL_EXPORT
QGeoRectanglePrivate *ritual_ZN20QGeoRectanglePrivateC1ERK14QGeoCoordinateS2_(
    const QGeoCoordinate *topLeft,
    const QGeoCoordinate *bottomRight) {
  return new CuteQGeoRectanglePrivate(*topLeft, *bottomRight);
}

//  QGeoRectanglePrivate::QGeoRectanglePrivate(const QGeoRectanglePrivate
//      &other)
extern "C" Q_DECL_EXPORT
QGeoRectanglePrivate *ritual_ZN20QGeoRectanglePrivateC1ERKS_(
    const QGeoRectanglePrivate *other) {
  return new CuteQGeoRectanglePrivate(*other);
}

//  QGeoRectanglePrivate::~QGeoRectanglePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoRectanglePrivateD1Ev(QGeoRectanglePrivate *self) {
  delete self;
}

//  bool QGeoRectanglePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGeoRectanglePrivate7isValidEv(
    const QGeoRectanglePrivate *self) {
  return self->isValid();
}

//  bool QGeoRectanglePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGeoRectanglePrivate7isEmptyEv(
    const QGeoRectanglePrivate *self) {
  return self->isEmpty();
}

//  bool QGeoRectanglePrivate::contains(const QGeoCoordinate &coordinate)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGeoRectanglePrivate8containsERK14QGeoCoordinate(
    const QGeoRectanglePrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->contains(*coordinate);
}

//  QGeoCoordinate QGeoRectanglePrivate::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK20QGeoRectanglePrivate6centerEv(
    const QGeoRectanglePrivate *self) {
  return new QGeoCoordinate(self->center());
}

//  QGeoRectangle QGeoRectanglePrivate::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK20QGeoRectanglePrivate20boundingGeoRectangleEv(
    const QGeoRectanglePrivate *self) {
  return new QGeoRectangle(self->boundingGeoRectangle());
}

//  void QGeoRectanglePrivate::extendRectangle(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoRectanglePrivate15extendRectangleERK14QGeoCoordinate(
    QGeoRectanglePrivate *self,
    const QGeoCoordinate *coordinate) {
  self->extendRectangle(*coordinate);
}

//  QGeoShapePrivate *QGeoRectanglePrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK20QGeoRectanglePrivate5cloneEv(
    const QGeoRectanglePrivate *self) {
  return self->clone();
}

//  bool QGeoRectanglePrivate::operator==(const QGeoShapePrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGeoRectanglePrivateeqERK16QGeoShapePrivate(
    const QGeoRectanglePrivate *self,
    const QGeoShapePrivate *other) {
  return self->operator==(*other);
}

//  size_t QGeoRectanglePrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK20QGeoRectanglePrivate4hashEm(
    const QGeoRectanglePrivate *self,
    size_t seed) {
  return self->hash(seed);
}

//  a Python function taken by a CuteQGeoRectanglePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRectanglePrivate(
    QGeoRectanglePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRectanglePrivate *>(self)->take(key, call);
}

//  bool QGeoRectanglePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QGeoRectanglePrivate7isValidEv(
    const QGeoRectanglePrivate *self) {
  return self->QGeoRectanglePrivate::isValid();
}

//  bool QGeoRectanglePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QGeoRectanglePrivate7isEmptyEv(
    const QGeoRectanglePrivate *self) {
  return self->QGeoRectanglePrivate::isEmpty();
}

//  bool QGeoRectanglePrivate::contains(const QGeoCoordinate &coordinate)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QGeoRectanglePrivate8containsERK14QGeoCoordinate(
    const QGeoRectanglePrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->QGeoRectanglePrivate::contains(*coordinate);
}

//  QGeoCoordinate QGeoRectanglePrivate::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK20QGeoRectanglePrivate6centerEv(
    const QGeoRectanglePrivate *self) {
  return new QGeoCoordinate(self->QGeoRectanglePrivate::center());
}

//  QGeoRectangle QGeoRectanglePrivate::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_own_ZNK20QGeoRectanglePrivate20boundingGeoRectangleEv(
    const QGeoRectanglePrivate *self) {
  return new QGeoRectangle(
      self->QGeoRectanglePrivate::boundingGeoRectangle());
}

//  QGeoShapePrivate *QGeoRectanglePrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_own_ZNK20QGeoRectanglePrivate5cloneEv(
    const QGeoRectanglePrivate *self) {
  return self->QGeoRectanglePrivate::clone();
}

//  size_t QGeoRectanglePrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_own_ZNK20QGeoRectanglePrivate4hashEm(
    const QGeoRectanglePrivate *self,
    size_t seed) {
  return self->QGeoRectanglePrivate::hash(seed);
}
