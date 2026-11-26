//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiepolystar_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiepolystar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottiePolyStar that Python can take functions over in. Every QLottiePolyStar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottiePolyStarCall0)(const void *, int *);
typedef int (*CuteQLottiePolyStarCall1)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottiePolyStarCall2)(const void *, int, int *);
typedef bool (*CuteQLottiePolyStarCall3)(const void *, int *);
typedef bool (*CuteQLottiePolyStarCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottiePolyStarCall5)(const void *, int *);
typedef const QPainterPath * (*CuteQLottiePolyStarCall6)(const void *, int *);
typedef void (*CuteQLottiePolyStarCall7)(const void *, const QLottieTrimPath *, int *);
typedef bool (*CuteQLottiePolyStarCall8)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottiePolyStarCall9)(const void *, int, int *);
typedef void * (*CuteQLottiePolyStarCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottiePolyStarCall11)(const void *, int *);
class CuteQLottiePolyStar : public QLottiePolyStar {
public:
  using QLottiePolyStar::QLottiePolyStar;
  CuteQLottiePolyStar(const QLottiePolyStar & other) : QLottiePolyStar(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottiePolyStar::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottiePolyStarCall0 call = reinterpret_cast<CuteQLottiePolyStarCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottiePolyStar::clone();
  }

  //  int QLottiePolyStar::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottiePolyStarCall1 call = reinterpret_cast<CuteQLottiePolyStarCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottiePolyStar::parse(definition);
  }

  //  void QLottiePolyStar::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottiePolyStarCall2 call = reinterpret_cast<CuteQLottiePolyStarCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottiePolyStar::updateProperties(frame);
  }

  //  bool QLottiePolyStar::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottiePolyStarCall3 call = reinterpret_cast<CuteQLottiePolyStarCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottiePolyStar::acceptsTrim();
  }

  //  bool QLottiePolyStar::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottiePolyStarCall4 call = reinterpret_cast<CuteQLottiePolyStarCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottiePolyStar::isAnimated();
  }

  //  QPainterPath QLottiePolyStar::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottiePolyStarCall5 call = reinterpret_cast<CuteQLottiePolyStarCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottiePolyStar::fallbackPath();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottiePolyStarCall6 call = reinterpret_cast<CuteQLottiePolyStarCall6>(taken[6]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottiePolyStarCall7 call = reinterpret_cast<CuteQLottiePolyStarCall7>(taken[7]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottiePolyStarCall8 call = reinterpret_cast<CuteQLottiePolyStarCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottiePolyStarCall9 call = reinterpret_cast<CuteQLottiePolyStarCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottiePolyStarCall10 call = reinterpret_cast<CuteQLottiePolyStarCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottiePolyStarCall11 call = reinterpret_cast<CuteQLottiePolyStarCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottiePolyStar::QLottiePolyStar(const QLottiePolyStar &other)
extern "C" Q_DECL_EXPORT
QLottiePolyStar *ritual_ZN15QLottiePolyStarC1ERKS_(
    const QLottiePolyStar *other) {
  return new CuteQLottiePolyStar(*other);
}

//  QLottiePolyStar::QLottiePolyStar(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottiePolyStar *ritual_ZN15QLottiePolyStarC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottiePolyStar(parent);
}

//  QLottieBase *QLottiePolyStar::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK15QLottiePolyStar5cloneEv(
    const QLottiePolyStar *self) {
  return self->clone();
}

//  int QLottiePolyStar::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QLottiePolyStar5parseERK11QJsonObject(
    QLottiePolyStar *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottiePolyStar::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottiePolyStar16updatePropertiesEi(
    QLottiePolyStar *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottiePolyStar::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QLottiePolyStar6renderER15QLottieRenderer(
    const QLottiePolyStar *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  bool QLottiePolyStar::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QLottiePolyStar11acceptsTrimEv(
    const QLottiePolyStar *self) {
  return self->acceptsTrim();
}

//  QPointF QLottiePolyStar::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QLottiePolyStar8positionEv(
    const QLottiePolyStar *self) {
  return new QPointF(self->position());
}

//  qreal QLottiePolyStar::outerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottiePolyStar11outerRadiusEv(
    const QLottiePolyStar *self) {
  return self->outerRadius();
}

//  qreal QLottiePolyStar::innerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottiePolyStar11innerRadiusEv(
    const QLottiePolyStar *self) {
  return self->innerRadius();
}

//  qreal QLottiePolyStar::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottiePolyStar10startAngleEv(
    const QLottiePolyStar *self) {
  return self->startAngle();
}

//  int QLottiePolyStar::pointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QLottiePolyStar10pointCountEv(const QLottiePolyStar *self) {
  return self->pointCount();
}

//  bool QLottiePolyStar::isPolygonModeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QLottiePolyStar20isPolygonModeEnabledEv(
    const QLottiePolyStar *self) {
  return self->isPolygonModeEnabled();
}

//  bool QLottiePolyStar::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QLottiePolyStar10isAnimatedEv(const QLottiePolyStar *self) {
  return self->isAnimated();
}

//  const QLottieProperty<qreal> &QLottiePolyStar::outerRadiusProperty()
//      const
extern "C" Q_DECL_EXPORT
const QLottieProperty<qreal> *ritual_ZNK15QLottiePolyStar19outerRadiusPropertyEv(
    const QLottiePolyStar *self) {
  return &(self->outerRadiusProperty());
}

//  const QLottieProperty<qreal> &QLottiePolyStar::innerRadiusProperty()
//      const
extern "C" Q_DECL_EXPORT
const QLottieProperty<qreal> *ritual_ZNK15QLottiePolyStar19innerRadiusPropertyEv(
    const QLottiePolyStar *self) {
  return &(self->innerRadiusProperty());
}

//  const QLottieSpatialProperty &QLottiePolyStar::positionProperty() const
extern "C" Q_DECL_EXPORT
QLottieSpatialProperty *ritual_ZNK15QLottiePolyStar16positionPropertyEv(
    const QLottiePolyStar *self) {
  return new QLottieSpatialProperty(self->positionProperty());
}

//  QPainterPath QLottiePolyStar::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK15QLottiePolyStar12fallbackPathEv(
    const QLottiePolyStar *self) {
  return new QPainterPath(self->fallbackPath());
}

//  void QLottiePolyStar::buildPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottiePolyStar9buildPathEv(QLottiePolyStar *self) {
  self->buildPath();
}

//  QLottiePolyStar::~QLottiePolyStar()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottiePolyStarD1Ev(QLottiePolyStar *self) {
  delete self;
}

//  a Python function taken by a CuteQLottiePolyStar, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottiePolyStar(
    QLottiePolyStar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottiePolyStar *>(self)->take(key, call);
}

//  QLottieBase *QLottiePolyStar::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK15QLottiePolyStar5cloneEv(
    const QLottiePolyStar *self) {
  return self->QLottiePolyStar::clone();
}

//  int QLottiePolyStar::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN15QLottiePolyStar5parseERK11QJsonObject(
    QLottiePolyStar *self,
    const QJsonObject *definition) {
  return self->QLottiePolyStar::parse(*definition);
}

//  void QLottiePolyStar::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottiePolyStar16updatePropertiesEi(
    QLottiePolyStar *self,
    int frame) {
  self->QLottiePolyStar::updateProperties(frame);
}

//  bool QLottiePolyStar::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QLottiePolyStar11acceptsTrimEv(
    const QLottiePolyStar *self) {
  return self->QLottiePolyStar::acceptsTrim();
}

//  bool QLottiePolyStar::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QLottiePolyStar10isAnimatedEv(
    const QLottiePolyStar *self) {
  return self->QLottiePolyStar::isAnimated();
}

//  QPainterPath QLottiePolyStar::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK15QLottiePolyStar12fallbackPathEv(
    const QLottiePolyStar *self) {
  return new QPainterPath(self->QLottiePolyStar::fallbackPath());
}
