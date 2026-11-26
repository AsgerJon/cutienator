//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoPolygonPrivate that Python can take functions over in. Every QGeoPolygonPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGeoPolygonPrivateCall0)(const void *, int *);
typedef bool (*CuteQGeoPolygonPrivateCall1)(const void *, int *);
typedef bool (*CuteQGeoPolygonPrivateCall2)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPolygonPrivateCall3)(const void *, double, double, int *);
typedef size_t (*CuteQGeoPolygonPrivateCall4)(const void *, size_t, int *);
typedef void (*CuteQGeoPolygonPrivateCall5)(const void *, int *);
typedef bool (*CuteQGeoPolygonPrivateCall6)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoPolygonPrivateCall7)(const void *, int *);
typedef const QGeoRectangle * (*CuteQGeoPolygonPrivateCall8)(const void *, int *);
typedef double (*CuteQGeoPolygonPrivateCall9)(const void *, qsizetype, qsizetype, int *);
typedef qsizetype (*CuteQGeoPolygonPrivateCall10)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoPolygonPrivateCall11)(const void *, qsizetype, int *);
typedef bool (*CuteQGeoPolygonPrivateCall12)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPolygonPrivateCall13)(const void *, int *);
typedef void (*CuteQGeoPolygonPrivateCall14)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPolygonPrivateCall15)(const void *, qsizetype, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPolygonPrivateCall16)(const void *, qsizetype, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPolygonPrivateCall17)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPolygonPrivateCall18)(const void *, qsizetype, int *);
class CuteQGeoPolygonPrivate : public QGeoPolygonPrivate {
public:
  using QGeoPolygonPrivate::QGeoPolygonPrivate;
  CuteQGeoPolygonPrivate(const QGeoPolygonPrivate & other) : QGeoPolygonPrivate(other) {}
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isValidEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9translateEdd")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate4hashEm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9markDirtyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isEmptyEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate6centerEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate20boundingGeoRectangleEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase6lengthExx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase4sizeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase12coordinateAtEx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordinate")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9clearPathEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordinate")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordinate")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinate")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16removeCoordinateEx")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  QGeoShapePrivate *QGeoPolygonPrivate::clone() const
  QGeoShapePrivate *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall0 call = reinterpret_cast<CuteQGeoPolygonPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoShapePrivate *>(given);
    }
    return QGeoPolygonPrivate::clone();
  }

  //  bool QGeoPolygonPrivate::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall1 call = reinterpret_cast<CuteQGeoPolygonPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPolygonPrivate::isValid();
  }

  //  bool QGeoPolygonPrivate::contains(const QGeoCoordinate &coordinate)
  //      const
  bool contains(const QGeoCoordinate &coordinate) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall2 call = reinterpret_cast<CuteQGeoPolygonPrivateCall2>(taken[2]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoPolygonPrivate::contains(coordinate);
  }

  //  void QGeoPolygonPrivate::translate(double degreesLatitude, double
  //      degreesLongitude)
  void translate(double degreesLatitude, double degreesLongitude) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall3 call = reinterpret_cast<CuteQGeoPolygonPrivateCall3>(taken[3]);
      call(this, degreesLatitude, degreesLongitude, &handled);
      if (handled) return;
    }
    QGeoPolygonPrivate::translate(degreesLatitude, degreesLongitude);
  }

  //  size_t QGeoPolygonPrivate::hash(size_t seed) const
  size_t hash(size_t seed) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall4 call = reinterpret_cast<CuteQGeoPolygonPrivateCall4>(taken[4]);
      size_t given = call(this, seed, &handled);
      if (handled) return given;
    }
    return QGeoPolygonPrivate::hash(seed);
  }

  //  void QGeoPolygonPrivate::markDirty()
  void markDirty() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall5 call = reinterpret_cast<CuteQGeoPolygonPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoPolygonPrivate::markDirty();
  }

  //  bool QGeoPathPrivateBase::isEmpty() const
  bool isEmpty() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall6 call = reinterpret_cast<CuteQGeoPolygonPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::isEmpty();
  }

  //  QGeoCoordinate QGeoPathPrivateBase::center() const
  QGeoCoordinate center() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall7 call = reinterpret_cast<CuteQGeoPolygonPrivateCall7>(taken[7]);
      const QGeoCoordinate * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::center();
  }

  //  QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle() const
  QGeoRectangle boundingGeoRectangle() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall8 call = reinterpret_cast<CuteQGeoPolygonPrivateCall8>(taken[8]);
      const QGeoRectangle * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::boundingGeoRectangle();
  }

  //  double QGeoPathPrivateBase::length(qsizetype indexFrom, qsizetype
  //      indexTo) const
  double length(qsizetype indexFrom, qsizetype indexTo) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall9 call = reinterpret_cast<CuteQGeoPolygonPrivateCall9>(taken[9]);
      double given = call(this, indexFrom, indexTo, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::length(indexFrom, indexTo);
  }

  //  qsizetype QGeoPathPrivateBase::size() const
  qsizetype size() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall10 call = reinterpret_cast<CuteQGeoPolygonPrivateCall10>(taken[10]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::size();
  }

  //  QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype index)
  //      const
  QGeoCoordinate coordinateAt(qsizetype index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall11 call = reinterpret_cast<CuteQGeoPolygonPrivateCall11>(taken[11]);
      const QGeoCoordinate * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::coordinateAt(index);
  }

  //  bool QGeoPathPrivateBase::containsCoordinate(const QGeoCoordinate
  //      &coordinate) const
  bool containsCoordinate(const QGeoCoordinate &coordinate) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall12 call = reinterpret_cast<CuteQGeoPolygonPrivateCall12>(taken[12]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::containsCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::clearPath()
  void clearPath() override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall13 call = reinterpret_cast<CuteQGeoPolygonPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::clearPath();
  }

  //  void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate
  //      &coordinate)
  void addCoordinate(const QGeoCoordinate &coordinate) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall14 call = reinterpret_cast<CuteQGeoPolygonPrivateCall14>(taken[14]);
      call(this, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::addCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::insertCoordinate(qsizetype index, const
  //      QGeoCoordinate &coordinate)
  void insertCoordinate(
      qsizetype index,
      const QGeoCoordinate &coordinate) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall15 call = reinterpret_cast<CuteQGeoPolygonPrivateCall15>(taken[15]);
      call(this, index, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::insertCoordinate(index, coordinate);
  }

  //  void QGeoPathPrivateBase::replaceCoordinate(qsizetype index, const
  //      QGeoCoordinate &coordinate)
  void replaceCoordinate(
      qsizetype index,
      const QGeoCoordinate &coordinate) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall16 call = reinterpret_cast<CuteQGeoPolygonPrivateCall16>(taken[16]);
      call(this, index, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::replaceCoordinate(index, coordinate);
  }

  //  void QGeoPathPrivateBase::removeCoordinate(const QGeoCoordinate
  //      &coordinate)
  void removeCoordinate(const QGeoCoordinate &coordinate) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall17 call = reinterpret_cast<CuteQGeoPolygonPrivateCall17>(taken[17]);
      call(this, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::removeCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::removeCoordinate(qsizetype index)
  void removeCoordinate(qsizetype index) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoPolygonPrivateCall18 call = reinterpret_cast<CuteQGeoPolygonPrivateCall18>(taken[18]);
      call(this, index, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::removeCoordinate(index);
  }
};

//  QGeoPolygonPrivate::QGeoPolygonPrivate()
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivate *ritual_ZN18QGeoPolygonPrivateC1Ev() {
  return new CuteQGeoPolygonPrivate();
}

//  QGeoPolygonPrivate::QGeoPolygonPrivate(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivate *ritual_ZN18QGeoPolygonPrivateC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *path) {
  return new CuteQGeoPolygonPrivate(*path);
}

//  QGeoPolygonPrivate::QGeoPolygonPrivate(const QGeoPolygonPrivate &other)
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivate *ritual_ZN18QGeoPolygonPrivateC1ERKS_(
    const QGeoPolygonPrivate *other) {
  return new CuteQGeoPolygonPrivate(*other);
}

//  QGeoPolygonPrivate::~QGeoPolygonPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoPolygonPrivateD1Ev(QGeoPolygonPrivate *self) {
  delete self;
}

//  QGeoShapePrivate *QGeoPolygonPrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK18QGeoPolygonPrivate5cloneEv(
    const QGeoPolygonPrivate *self) {
  return self->clone();
}

//  bool QGeoPolygonPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGeoPolygonPrivate7isValidEv(
    const QGeoPolygonPrivate *self) {
  return self->isValid();
}

//  bool QGeoPolygonPrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGeoPolygonPrivate8containsERK14QGeoCoordinate(
    const QGeoPolygonPrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->contains(*coordinate);
}

//  void QGeoPolygonPrivate::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoPolygonPrivate9translateEdd(
    QGeoPolygonPrivate *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  bool QGeoPolygonPrivate::operator==(const QGeoShapePrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGeoPolygonPrivateeqERK16QGeoShapePrivate(
    const QGeoPolygonPrivate *self,
    const QGeoShapePrivate *other) {
  return self->operator==(*other);
}

//  size_t QGeoPolygonPrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK18QGeoPolygonPrivate4hashEm(
    const QGeoPolygonPrivate *self,
    size_t seed) {
  return self->hash(seed);
}

//  void QGeoPolygonPrivate::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoPolygonPrivate9markDirtyEv(QGeoPolygonPrivate *self) {
  self->markDirty();
}

//  qsizetype QGeoPolygonPrivate::holesCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QGeoPolygonPrivate10holesCountEv(
    const QGeoPolygonPrivate *self) {
  return self->holesCount();
}

//  bool QGeoPolygonPrivate::polygonContains(const QGeoCoordinate
//      &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGeoPolygonPrivate15polygonContainsERK14QGeoCoordinate(
    const QGeoPolygonPrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->polygonContains(*coordinate);
}

//  const QList<QGeoCoordinate> QGeoPolygonPrivate::holePath(qsizetype index)
//      const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK18QGeoPolygonPrivate8holePathEx(
    const QGeoPolygonPrivate *self,
    qsizetype index) {
  return new QList<QGeoCoordinate>(self->holePath(index));
}

//  void QGeoPolygonPrivate::addHole(const QList<QGeoCoordinate> &holePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoPolygonPrivate7addHoleERK5QListI14QGeoCoordinateE(
    QGeoPolygonPrivate *self,
    const QList<QGeoCoordinate> *holePath) {
  self->addHole(*holePath);
}

//  void QGeoPolygonPrivate::removeHole(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoPolygonPrivate10removeHoleEx(
    QGeoPolygonPrivate *self,
    qsizetype index) {
  self->removeHole(index);
}

//  void QGeoPolygonPrivate::ensureClipperPathUpdated() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QGeoPolygonPrivate24ensureClipperPathUpdatedEv(
    const QGeoPolygonPrivate *self) {
  self->ensureClipperPathUpdated();
}

//  a Python function taken by a CuteQGeoPolygonPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoPolygonPrivate(
    QGeoPolygonPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoPolygonPrivate *>(self)->take(key, call);
}

//  QGeoShapePrivate *QGeoPolygonPrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_own_ZNK18QGeoPolygonPrivate5cloneEv(
    const QGeoPolygonPrivate *self) {
  return self->QGeoPolygonPrivate::clone();
}

//  bool QGeoPolygonPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QGeoPolygonPrivate7isValidEv(
    const QGeoPolygonPrivate *self) {
  return self->QGeoPolygonPrivate::isValid();
}

//  bool QGeoPolygonPrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QGeoPolygonPrivate8containsERK14QGeoCoordinate(
    const QGeoPolygonPrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->QGeoPolygonPrivate::contains(*coordinate);
}

//  void QGeoPolygonPrivate::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QGeoPolygonPrivate9translateEdd(
    QGeoPolygonPrivate *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->QGeoPolygonPrivate::translate(degreesLatitude, degreesLongitude);
}

//  size_t QGeoPolygonPrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_own_ZNK18QGeoPolygonPrivate4hashEm(
    const QGeoPolygonPrivate *self,
    size_t seed) {
  return self->QGeoPolygonPrivate::hash(seed);
}

//  void QGeoPolygonPrivate::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QGeoPolygonPrivate9markDirtyEv(
    QGeoPolygonPrivate *self) {
  self->QGeoPolygonPrivate::markDirty();
}
