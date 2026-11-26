//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeoshape_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeoshape_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 30, as _ZN16QGeoShapePrivateD2Ev
inline QGeoShapePrivate::~QGeoShapePrivate()
{
}

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 34, as _ZNK16QGeoShapePrivateeqERKS_
inline bool QGeoShapePrivate::operator==(const QGeoShapePrivate &other) const
{
    return type == other.type;
}
//  -----------------------------------------------------------------------

//  A QGeoShapePrivate that Python can take functions over in. Every QGeoShapePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoShapePrivateCall0)(const void *, int *);
typedef bool (*CuteQGeoShapePrivateCall1)(const void *, int *);
typedef bool (*CuteQGeoShapePrivateCall2)(const void *, const QGeoCoordinate *, int *);
typedef const QGeoCoordinate * (*CuteQGeoShapePrivateCall3)(const void *, int *);
typedef const QGeoRectangle * (*CuteQGeoShapePrivateCall4)(const void *, int *);
typedef void * (*CuteQGeoShapePrivateCall5)(const void *, int *);
typedef size_t (*CuteQGeoShapePrivateCall6)(const void *, size_t, int *);
class CuteQGeoShapePrivate : public QGeoShapePrivate {
public:
  using QGeoShapePrivate::QGeoShapePrivate;
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

  //  bool QGeoShapePrivate::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoShapePrivateCall0 call = reinterpret_cast<CuteQGeoShapePrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QGeoShapePrivate::isEmpty() const
  bool isEmpty() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoShapePrivateCall1 call = reinterpret_cast<CuteQGeoShapePrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QGeoShapePrivate::contains(const QGeoCoordinate &coordinate)
  //      const
  bool contains(const QGeoCoordinate &coordinate) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoShapePrivateCall2 call = reinterpret_cast<CuteQGeoShapePrivateCall2>(taken[2]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QGeoCoordinate QGeoShapePrivate::center() const
  QGeoCoordinate center() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoShapePrivateCall3 call = reinterpret_cast<CuteQGeoShapePrivateCall3>(taken[3]);
      const QGeoCoordinate * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QGeoRectangle QGeoShapePrivate::boundingGeoRectangle() const
  QGeoRectangle boundingGeoRectangle() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoShapePrivateCall4 call = reinterpret_cast<CuteQGeoShapePrivateCall4>(taken[4]);
      const QGeoRectangle * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QGeoShapePrivate *QGeoShapePrivate::clone() const
  QGeoShapePrivate *clone() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoShapePrivateCall5 call = reinterpret_cast<CuteQGeoShapePrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoShapePrivate *>(given);
    }
    return {};
  }

  //  size_t QGeoShapePrivate::hash(size_t seed) const
  size_t hash(size_t seed) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoShapePrivateCall6 call = reinterpret_cast<CuteQGeoShapePrivateCall6>(taken[6]);
      size_t given = call(this, seed, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QGeoShapePrivate::~QGeoShapePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoShapePrivateD1Ev(QGeoShapePrivate *self) {
  delete self;
}

//  bool QGeoShapePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoShapePrivate7isValidEv(const QGeoShapePrivate *self) {
  return self->isValid();
}

//  bool QGeoShapePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoShapePrivate7isEmptyEv(const QGeoShapePrivate *self) {
  return self->isEmpty();
}

//  bool QGeoShapePrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate(
    const QGeoShapePrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->contains(*coordinate);
}

//  QGeoCoordinate QGeoShapePrivate::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK16QGeoShapePrivate6centerEv(
    const QGeoShapePrivate *self) {
  return new QGeoCoordinate(self->center());
}

//  QGeoRectangle QGeoShapePrivate::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK16QGeoShapePrivate20boundingGeoRectangleEv(
    const QGeoShapePrivate *self) {
  return new QGeoRectangle(self->boundingGeoRectangle());
}

//  QGeoShapePrivate *QGeoShapePrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK16QGeoShapePrivate5cloneEv(
    const QGeoShapePrivate *self) {
  return self->clone();
}

//  bool QGeoShapePrivate::operator==(const QGeoShapePrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoShapePrivateeqERKS_(
    const QGeoShapePrivate *self,
    const QGeoShapePrivate *other) {
  return self->operator==(*other);
}

//  size_t QGeoShapePrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK16QGeoShapePrivate4hashEm(
    const QGeoShapePrivate *self,
    size_t seed) {
  return self->hash(seed);
}

//  a Python function taken by a CuteQGeoShapePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoShapePrivate(
    QGeoShapePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoShapePrivate *>(self)->take(key, call);
}
