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

//  A QGeoPathPrivateBase that Python can take functions over in. Every QGeoPathPrivateBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoPathPrivateBaseCall0)(const void *, int *);
typedef bool (*CuteQGeoPathPrivateBaseCall1)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoPathPrivateBaseCall2)(const void *, int *);
typedef const QGeoRectangle * (*CuteQGeoPathPrivateBaseCall3)(const void *, int *);
typedef size_t (*CuteQGeoPathPrivateBaseCall4)(const void *, size_t, int *);
typedef double (*CuteQGeoPathPrivateBaseCall5)(const void *, qsizetype, qsizetype, int *);
typedef qsizetype (*CuteQGeoPathPrivateBaseCall6)(const void *, int *);
typedef const QGeoCoordinate * (*CuteQGeoPathPrivateBaseCall7)(const void *, qsizetype, int *);
typedef bool (*CuteQGeoPathPrivateBaseCall8)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateBaseCall9)(const void *, double, double, int *);
typedef void (*CuteQGeoPathPrivateBaseCall10)(const void *, int *);
typedef void (*CuteQGeoPathPrivateBaseCall11)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateBaseCall12)(const void *, qsizetype, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateBaseCall13)(const void *, qsizetype, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateBaseCall14)(const void *, const QGeoCoordinate *, int *);
typedef void (*CuteQGeoPathPrivateBaseCall15)(const void *, qsizetype, int *);
typedef void (*CuteQGeoPathPrivateBaseCall16)(const void *, int *);
typedef bool (*CuteQGeoPathPrivateBaseCall17)(const void *, const QGeoCoordinate *, int *);
typedef void * (*CuteQGeoPathPrivateBaseCall18)(const void *, int *);
class CuteQGeoPathPrivateBase : public QGeoPathPrivateBase {
public:
  using QGeoPathPrivateBase::QGeoPathPrivateBase;
  CuteQGeoPathPrivateBase(const QGeoPathPrivateBase & other) : QGeoPathPrivateBase(other) {}
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isEmptyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate6centerEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate20boundingGeoRectangleEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate4hashEm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase6lengthExx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase4sizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase12coordinateAtEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordinate")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9translateEdd")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9clearPathEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordinate")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordinate")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinate")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase16removeCoordinateEx")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QGeoPathPrivateBase9markDirtyEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate5cloneEv")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  bool QGeoPathPrivateBase::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall0 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::isValid();
  }

  //  bool QGeoPathPrivateBase::isEmpty() const
  bool isEmpty() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall1 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::isEmpty();
  }

  //  QGeoCoordinate QGeoPathPrivateBase::center() const
  QGeoCoordinate center() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall2 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall2>(taken[2]);
      const QGeoCoordinate * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::center();
  }

  //  QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle() const
  QGeoRectangle boundingGeoRectangle() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall3 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall3>(taken[3]);
      const QGeoRectangle * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::boundingGeoRectangle();
  }

  //  size_t QGeoPathPrivateBase::hash(size_t seed) const
  size_t hash(size_t seed) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall4 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall4>(taken[4]);
      size_t given = call(this, seed, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::hash(seed);
  }

  //  double QGeoPathPrivateBase::length(qsizetype indexFrom, qsizetype
  //      indexTo) const
  double length(qsizetype indexFrom, qsizetype indexTo) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall5 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall5>(taken[5]);
      double given = call(this, indexFrom, indexTo, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::length(indexFrom, indexTo);
  }

  //  qsizetype QGeoPathPrivateBase::size() const
  qsizetype size() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall6 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall6>(taken[6]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::size();
  }

  //  QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype index)
  //      const
  QGeoCoordinate coordinateAt(qsizetype index) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall7 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall7>(taken[7]);
      const QGeoCoordinate * given = call(this, index, &handled);
      if (handled && given) return *given;
    }
    return QGeoPathPrivateBase::coordinateAt(index);
  }

  //  bool QGeoPathPrivateBase::containsCoordinate(const QGeoCoordinate
  //      &coordinate) const
  bool containsCoordinate(const QGeoCoordinate &coordinate) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall8 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall8>(taken[8]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoPathPrivateBase::containsCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::translate(double degreesLatitude, double
  //      degreesLongitude)
  void translate(double degreesLatitude, double degreesLongitude) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall9 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall9>(taken[9]);
      call(this, degreesLatitude, degreesLongitude, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::translate(degreesLatitude, degreesLongitude);
  }

  //  void QGeoPathPrivateBase::clearPath()
  void clearPath() override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall10 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::clearPath();
  }

  //  void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate
  //      &coordinate)
  void addCoordinate(const QGeoCoordinate &coordinate) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall11 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall12 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall13 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall13>(taken[13]);
      call(this, index, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::replaceCoordinate(index, coordinate);
  }

  //  void QGeoPathPrivateBase::removeCoordinate(const QGeoCoordinate
  //      &coordinate)
  void removeCoordinate(const QGeoCoordinate &coordinate) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall14 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall14>(taken[14]);
      call(this, &coordinate, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::removeCoordinate(coordinate);
  }

  //  void QGeoPathPrivateBase::removeCoordinate(qsizetype index)
  void removeCoordinate(qsizetype index) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall15 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall15>(taken[15]);
      call(this, index, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::removeCoordinate(index);
  }

  //  void QGeoPathPrivateBase::markDirty()
  void markDirty() override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall16 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoPathPrivateBase::markDirty();
  }

  //  bool QGeoShapePrivate::contains(const QGeoCoordinate &coordinate)
  //      const
  bool contains(const QGeoCoordinate &coordinate) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall17 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall17>(taken[17]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QGeoShapePrivate *QGeoShapePrivate::clone() const
  QGeoShapePrivate *clone() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoPathPrivateBaseCall18 call = reinterpret_cast<CuteQGeoPathPrivateBaseCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoShapePrivate *>(given);
    }
    return {};
  }
};

//  QGeoPathPrivateBase::QGeoPathPrivateBase()
extern "C" Q_DECL_EXPORT
QGeoPathPrivateBase *ritual_ZN19QGeoPathPrivateBaseC1Ev() {
  return new CuteQGeoPathPrivateBase();
}

//  QGeoPathPrivateBase::QGeoPathPrivateBase(const QList<QGeoCoordinate>
//      &path)
extern "C" Q_DECL_EXPORT
QGeoPathPrivateBase *ritual_ZN19QGeoPathPrivateBaseC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *path) {
  return new CuteQGeoPathPrivateBase(*path);
}

//  QGeoPathPrivateBase::QGeoPathPrivateBase(const QGeoPathPrivateBase
//      &other)
extern "C" Q_DECL_EXPORT
QGeoPathPrivateBase *ritual_ZN19QGeoPathPrivateBaseC1ERKS_(
    const QGeoPathPrivateBase *other) {
  return new CuteQGeoPathPrivateBase(*other);
}

//  QGeoPathPrivateBase::~QGeoPathPrivateBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBaseD1Ev(QGeoPathPrivateBase *self) {
  delete self;
}

//  bool QGeoPathPrivateBase::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoPathPrivateBase7isValidEv(
    const QGeoPathPrivateBase *self) {
  return self->isValid();
}

//  bool QGeoPathPrivateBase::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoPathPrivateBase7isEmptyEv(
    const QGeoPathPrivateBase *self) {
  return self->isEmpty();
}

//  QGeoCoordinate QGeoPathPrivateBase::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK19QGeoPathPrivateBase6centerEv(
    const QGeoPathPrivateBase *self) {
  return new QGeoCoordinate(self->center());
}

//  bool QGeoPathPrivateBase::operator==(const QGeoShapePrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoPathPrivateBaseeqERK16QGeoShapePrivate(
    const QGeoPathPrivateBase *self,
    const QGeoShapePrivate *other) {
  return self->operator==(*other);
}

//  QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK19QGeoPathPrivateBase20boundingGeoRectangleEv(
    const QGeoPathPrivateBase *self) {
  return new QGeoRectangle(self->boundingGeoRectangle());
}

//  size_t QGeoPathPrivateBase::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK19QGeoPathPrivateBase4hashEm(
    const QGeoPathPrivateBase *self,
    size_t seed) {
  return self->hash(seed);
}

//  const QList<QGeoCoordinate> &QGeoPathPrivateBase::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK19QGeoPathPrivateBase4pathEv(
    const QGeoPathPrivateBase *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  double QGeoPathPrivateBase::length(qsizetype indexFrom, qsizetype
//      indexTo) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK19QGeoPathPrivateBase6lengthExx(
    const QGeoPathPrivateBase *self,
    qsizetype indexFrom,
    qsizetype indexTo) {
  return self->length(indexFrom, indexTo);
}

//  qsizetype QGeoPathPrivateBase::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19QGeoPathPrivateBase4sizeEv(
    const QGeoPathPrivateBase *self) {
  return self->size();
}

//  QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK19QGeoPathPrivateBase12coordinateAtEx(
    const QGeoPathPrivateBase *self,
    qsizetype index) {
  return new QGeoCoordinate(self->coordinateAt(index));
}

//  bool QGeoPathPrivateBase::containsCoordinate(const QGeoCoordinate
//      &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordinate(
    const QGeoPathPrivateBase *self,
    const QGeoCoordinate *coordinate) {
  return self->containsCoordinate(*coordinate);
}

//  void QGeoPathPrivateBase::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase9translateEdd(
    QGeoPathPrivateBase *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  void QGeoPathPrivateBase::setPath(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase7setPathERK5QListI14QGeoCoordinateE(
    QGeoPathPrivateBase *self,
    const QList<QGeoCoordinate> *path) {
  self->setPath(*path);
}

//  void QGeoPathPrivateBase::clearPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase9clearPathEv(QGeoPathPrivateBase *self) {
  self->clearPath();
}

//  void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    const QGeoCoordinate *coordinate) {
  self->addCoordinate(*coordinate);
}

//  void QGeoPathPrivateBase::insertCoordinate(qsizetype index, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->insertCoordinate(index, *coordinate);
}

//  void QGeoPathPrivateBase::replaceCoordinate(qsizetype index, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->replaceCoordinate(index, *coordinate);
}

//  void QGeoPathPrivateBase::removeCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    const QGeoCoordinate *coordinate) {
  self->removeCoordinate(*coordinate);
}

//  void QGeoPathPrivateBase::removeCoordinate(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase16removeCoordinateEx(
    QGeoPathPrivateBase *self,
    qsizetype index) {
  self->removeCoordinate(index);
}

//  void QGeoPathPrivateBase::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoPathPrivateBase9markDirtyEv(QGeoPathPrivateBase *self) {
  self->markDirty();
}

//  void QGeoPathPrivateBase::ensureBoundingBoxUpdated() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QGeoPathPrivateBase24ensureBoundingBoxUpdatedEv(
    const QGeoPathPrivateBase *self) {
  self->ensureBoundingBoxUpdated();
}

//  a Python function taken by a CuteQGeoPathPrivateBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoPathPrivateBase(
    QGeoPathPrivateBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoPathPrivateBase *>(self)->take(key, call);
}

//  bool QGeoPathPrivateBase::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGeoPathPrivateBase7isValidEv(
    const QGeoPathPrivateBase *self) {
  return self->QGeoPathPrivateBase::isValid();
}

//  bool QGeoPathPrivateBase::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGeoPathPrivateBase7isEmptyEv(
    const QGeoPathPrivateBase *self) {
  return self->QGeoPathPrivateBase::isEmpty();
}

//  QGeoCoordinate QGeoPathPrivateBase::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK19QGeoPathPrivateBase6centerEv(
    const QGeoPathPrivateBase *self) {
  return new QGeoCoordinate(self->QGeoPathPrivateBase::center());
}

//  QGeoRectangle QGeoPathPrivateBase::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_own_ZNK19QGeoPathPrivateBase20boundingGeoRectangleEv(
    const QGeoPathPrivateBase *self) {
  return new QGeoRectangle(
      self->QGeoPathPrivateBase::boundingGeoRectangle());
}

//  size_t QGeoPathPrivateBase::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_own_ZNK19QGeoPathPrivateBase4hashEm(
    const QGeoPathPrivateBase *self,
    size_t seed) {
  return self->QGeoPathPrivateBase::hash(seed);
}

//  double QGeoPathPrivateBase::length(qsizetype indexFrom, qsizetype
//      indexTo) const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK19QGeoPathPrivateBase6lengthExx(
    const QGeoPathPrivateBase *self,
    qsizetype indexFrom,
    qsizetype indexTo) {
  return self->QGeoPathPrivateBase::length(indexFrom, indexTo);
}

//  qsizetype QGeoPathPrivateBase::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK19QGeoPathPrivateBase4sizeEv(
    const QGeoPathPrivateBase *self) {
  return self->QGeoPathPrivateBase::size();
}

//  QGeoCoordinate QGeoPathPrivateBase::coordinateAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK19QGeoPathPrivateBase12coordinateAtEx(
    const QGeoPathPrivateBase *self,
    qsizetype index) {
  return new QGeoCoordinate(self->QGeoPathPrivateBase::coordinateAt(index));
}

//  bool QGeoPathPrivateBase::containsCoordinate(const QGeoCoordinate
//      &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QGeoPathPrivateBase18containsCoordinateERK14QGeoCoordinate(
    const QGeoPathPrivateBase *self,
    const QGeoCoordinate *coordinate) {
  return self->QGeoPathPrivateBase::containsCoordinate(*coordinate);
}

//  void QGeoPathPrivateBase::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase9translateEdd(
    QGeoPathPrivateBase *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->QGeoPathPrivateBase::translate(degreesLatitude, degreesLongitude);
}

//  void QGeoPathPrivateBase::clearPath()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase9clearPathEv(
    QGeoPathPrivateBase *self) {
  self->QGeoPathPrivateBase::clearPath();
}

//  void QGeoPathPrivateBase::addCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase13addCoordinateERK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    const QGeoCoordinate *coordinate) {
  self->QGeoPathPrivateBase::addCoordinate(*coordinate);
}

//  void QGeoPathPrivateBase::insertCoordinate(qsizetype index, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase16insertCoordinateExRK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->QGeoPathPrivateBase::insertCoordinate(index, *coordinate);
}

//  void QGeoPathPrivateBase::replaceCoordinate(qsizetype index, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase17replaceCoordinateExRK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->QGeoPathPrivateBase::replaceCoordinate(index, *coordinate);
}

//  void QGeoPathPrivateBase::removeCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase16removeCoordinateERK14QGeoCoordinate(
    QGeoPathPrivateBase *self,
    const QGeoCoordinate *coordinate) {
  self->QGeoPathPrivateBase::removeCoordinate(*coordinate);
}

//  void QGeoPathPrivateBase::removeCoordinate(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase16removeCoordinateEx(
    QGeoPathPrivateBase *self,
    qsizetype index) {
  self->QGeoPathPrivateBase::removeCoordinate(index);
}

//  void QGeoPathPrivateBase::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGeoPathPrivateBase9markDirtyEv(
    QGeoPathPrivateBase *self) {
  self->QGeoPathPrivateBase::markDirty();
}
