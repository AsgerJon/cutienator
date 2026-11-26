//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoPathPrivate that Python can take functions over in. Every QGeoPathPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGeoPathPrivateCall0)(const void *, int *);
typedef bool (*CuteQGeoPathPrivateCall1)(const void *, const QGeoCoordinate *, int *);
typedef size_t (*CuteQGeoPathPrivateCall2)(const void *, size_t, int *);
typedef bool (*CuteQGeoPathPrivateCall3)(const void *, int *);
typedef bool (*CuteQGeoPathPrivateCall4)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoPathPrivateCall5)(const void *, int *);
typedef const QGeoRectangle * (*CuteQGeoPathPrivateCall6)(const void *, int *);
typedef double (*CuteQGeoPathPrivateCall7)(const void *, qsizetype, qsizetype, int *);
typedef qsizetype (*CuteQGeoPathPrivateCall8)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoPathPrivateCall9)(const void *, qsizetype, int *);
typedef bool (*CuteQGeoPathPrivateCall10)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateCall11)(const void *, double, double, int *);
typedef void (*CuteQGeoPathPrivateCall12)(const void *, int *);
typedef void (*CuteQGeoPathPrivateCall13)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateCall14)(const void *, qsizetype, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateCall15)(const void *, qsizetype, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateCall16)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateCall17)(const void *, qsizetype, int *);
typedef void (*CuteQGeoPathPrivateCall18)(const void *, int *);
class CuteQGeoPathPrivate : public QGeoPathPrivate {
public:
  using QGeoPathPrivate::QGeoPathPrivate;
  CuteQGeoPathPrivate(const QGeoPathPrivate & other) : QGeoPathPrivate(other) {}
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate4hashEm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isValidEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isEmptyEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate6centerEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate20boundingGeoRectangleEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase6lengthExx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase4sizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase12coordinateAtEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordinate")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9translateEdd")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9clearPathEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordinate")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordinate")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinate")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16removeCoordinateEx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9markDirtyEv")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  QGeoShapePrivate *QGeoPathPrivate::clone() const
  QGeoShapePrivate *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoPathPrivateCall0 call = reinterpret_cast<CuteQGeoPathPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoShapePrivate *>(given);
    }
    return QGeoPathPrivate::clone();
  }

  //  bool QGeoPathPrivate::contains(const QGeoCoordinate &coordinate)
  //      const
  bool contains(const QGeoCoordinate &coordinate) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoPathPrivateCall1 call = reinterpret_cast<CuteQGeoPathPrivateCall1>(taken[1]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivate::contains(coordinate);
  }

  //  size_t QGeoPathPrivate::hash(size_t seed) const
  size_t hash(size_t seed) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoPathPrivateCall2 call = reinterpret_cast<CuteQGeoPathPrivateCall2>(taken[2]);
      size_t given = call(this, seed, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivate::hash(seed);
  }

  //  bool QGeoPathPrivateBase::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoPathPrivateCall3 call = reinterpret_cast<CuteQGeoPathPrivateCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::isValid();
  }

  //  bool QGeoPathPrivateBase::isEmpty() const
  bool isEmpty() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoPathPrivateCall4 call = reinterpret_cast<CuteQGeoPathPrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::isEmpty();
  }

  //  QGeoCoordinate QGeoPathPrivateBase::center() const
  QGeoCoordinate center() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoPathPrivateCall5 call = reinterpret_cast<CuteQGeoPathPrivateCall5>(taken[5]);
      const QGeoCoordinate * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::center();
  }

  //  QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle() const
  QGeoRectangle boundingGeoRectangle() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoPathPrivateCall6 call = reinterpret_cast<CuteQGeoPathPrivateCall6>(taken[6]);
      const QGeoRectangle * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::boundingGeoRectangle();
  }

  //  double QGeoPathPrivateBase::length(qsizetype indexFrom, qsizetype
  //      indexTo) const
  double length(qsizetype indexFrom, qsizetype indexTo) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoPathPrivateCall7 call = reinterpret_cast<CuteQGeoPathPrivateCall7>(taken[7]);
      double given = call(this, indexFrom, indexTo, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::length(indexFrom, indexTo);
  }

  //  qsizetype QGeoPathPrivateBase::size() const
  qsizetype size() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoPathPrivateCall8 call = reinterpret_cast<CuteQGeoPathPrivateCall8>(taken[8]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::size();
  }

  //  QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype index)
  //      const
  QGeoCoordinate coordinateAt(qsizetype index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoPathPrivateCall9 call = reinterpret_cast<CuteQGeoPathPrivateCall9>(taken[9]);
      const QGeoCoordinate * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::coordinateAt(index);
  }

  //  bool QGeoPathPrivateBase::containsCoordinate(const QGeoCoordinate
  //      &coordinate) const
  bool containsCoordinate(const QGeoCoordinate &coordinate) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoPathPrivateCall10 call = reinterpret_cast<CuteQGeoPathPrivateCall10>(taken[10]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::containsCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::translate(double degreesLatitude, double
  //      degreesLongitude)
  void translate(double degreesLatitude, double degreesLongitude) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoPathPrivateCall11 call = reinterpret_cast<CuteQGeoPathPrivateCall11>(taken[11]);
      call(this, degreesLatitude, degreesLongitude, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::translate(degreesLatitude, degreesLongitude);
  }

  //  void QGeoPathPrivateBase::clearPath()
  void clearPath() override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoPathPrivateCall12 call = reinterpret_cast<CuteQGeoPathPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::clearPath();
  }

  //  void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate
  //      &coordinate)
  void addCoordinate(const QGeoCoordinate &coordinate) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoPathPrivateCall13 call = reinterpret_cast<CuteQGeoPathPrivateCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQGeoPathPrivateCall14 call = reinterpret_cast<CuteQGeoPathPrivateCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQGeoPathPrivateCall15 call = reinterpret_cast<CuteQGeoPathPrivateCall15>(taken[15]);
      call(this, index, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::replaceCoordinate(index, coordinate);
  }

  //  void QGeoPathPrivateBase::removeCoordinate(const QGeoCoordinate
  //      &coordinate)
  void removeCoordinate(const QGeoCoordinate &coordinate) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoPathPrivateCall16 call = reinterpret_cast<CuteQGeoPathPrivateCall16>(taken[16]);
      call(this, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::removeCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::removeCoordinate(qsizetype index)
  void removeCoordinate(qsizetype index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoPathPrivateCall17 call = reinterpret_cast<CuteQGeoPathPrivateCall17>(taken[17]);
      call(this, index, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::removeCoordinate(index);
  }

  //  void QGeoPathPrivateBase::markDirty()
  void markDirty() override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoPathPrivateCall18 call = reinterpret_cast<CuteQGeoPathPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::markDirty();
  }
};

//  QGeoPathPrivate::QGeoPathPrivate()
extern "C" Q_DECL_EXPORT
QGeoPathPrivate *ritual_ZN15QGeoPathPrivateC1Ev() {
  return new CuteQGeoPathPrivate();
}

//  QGeoPathPrivate::QGeoPathPrivate(const QList<QGeoCoordinate> &path, const
//      qreal width)
extern "C" Q_DECL_EXPORT
QGeoPathPrivate *ritual_ZN15QGeoPathPrivateC1ERK5QListI14QGeoCoordinateEd(
    const QList<QGeoCoordinate> *path,
    qreal width) {
  return new CuteQGeoPathPrivate(*path, width);
}

//  QGeoPathPrivate::~QGeoPathPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoPathPrivateD1Ev(QGeoPathPrivate *self) {
  delete self;
}

//  QGeoShapePrivate *QGeoPathPrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK15QGeoPathPrivate5cloneEv(
    const QGeoPathPrivate *self) {
  return self->clone();
}

//  bool QGeoPathPrivate::operator==(const QGeoShapePrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGeoPathPrivateeqERK16QGeoShapePrivate(
    const QGeoPathPrivate *self,
    const QGeoShapePrivate *other) {
  return self->operator==(*other);
}

//  bool QGeoPathPrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGeoPathPrivate8containsERK14QGeoCoordinate(
    const QGeoPathPrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->contains(*coordinate);
}

//  size_t QGeoPathPrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK15QGeoPathPrivate4hashEm(
    const QGeoPathPrivate *self,
    size_t seed) {
  return self->hash(seed);
}

//  bool QGeoPathPrivate::lineContains(const QGeoCoordinate &coordinate)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGeoPathPrivate12lineContainsERK14QGeoCoordinate(
    const QGeoPathPrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->lineContains(*coordinate);
}

//  qreal QGeoPathPrivate::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QGeoPathPrivate5widthEv(const QGeoPathPrivate *self) {
  return self->width();
}

//  void QGeoPathPrivate::setWidth(const qreal &width)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoPathPrivate8setWidthERKd(
    QGeoPathPrivate *self,
    qreal width) {
  self->setWidth(width);
}

//  a Python function taken by a CuteQGeoPathPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoPathPrivate(
    QGeoPathPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoPathPrivate *>(self)->take(key, call);
}

//  QGeoShapePrivate *QGeoPathPrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_own_ZNK15QGeoPathPrivate5cloneEv(
    const QGeoPathPrivate *self) {
  return self->QGeoPathPrivate::clone();
}

//  bool QGeoPathPrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QGeoPathPrivate8containsERK14QGeoCoordinate(
    const QGeoPathPrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->QGeoPathPrivate::contains(*coordinate);
}

//  size_t QGeoPathPrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_own_ZNK15QGeoPathPrivate4hashEm(
    const QGeoPathPrivate *self,
    size_t seed) {
  return self->QGeoPathPrivate::hash(seed);
}
