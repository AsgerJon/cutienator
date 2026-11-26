//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottierect_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottierect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QLottieRect that Python can take functions over in. Every QLottieRect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieRectCall0)(const void *, int *);
typedef bool (*CuteQLottieRectCall1)(const void *, int, const QVariant *, int *);
typedef void (*CuteQLottieRectCall2)(const void *, int, int *);
typedef bool (*CuteQLottieRectCall3)(const void *, int *);
typedef int (*CuteQLottieRectCall4)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieRectCall5)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieRectCall6)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieRectCall7)(const void *, int *);
typedef void (*CuteQLottieRectCall8)(const void *, const QLottieTrimPath *, int *);
typedef bool (*CuteQLottieRectCall9)(const void *, int, int *);
typedef void * (*CuteQLottieRectCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieRectCall11)(const void *, int *);
class CuteQLottieRect : public QLottieRect {
public:
  using QLottieRect::QLottieRect;
  CuteQLottieRect(const QLottieRect & other) : QLottieRect(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
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
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
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

  //  QLottieBase *QLottieRect::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRectCall0 call = reinterpret_cast<CuteQLottieRectCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieRect::clone();
  }

  //  bool QLottieRect::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRectCall1 call = reinterpret_cast<CuteQLottieRectCall1>(taken[1]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieRect::setProperty(propertyType, value);
  }

  //  void QLottieRect::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRectCall2 call = reinterpret_cast<CuteQLottieRectCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieRect::updateProperties(frame);
  }

  //  bool QLottieRect::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRectCall3 call = reinterpret_cast<CuteQLottieRectCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieRect::acceptsTrim();
  }

  //  int QLottieRect::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRectCall4 call = reinterpret_cast<CuteQLottieRectCall4>(taken[4]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieRect::parse(definition);
  }

  //  bool QLottieRect::isAnimated() const
  bool isAnimated() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRectCall5 call = reinterpret_cast<CuteQLottieRectCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieRect::isAnimated();
  }

  //  QPainterPath QLottieRect::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRectCall6 call = reinterpret_cast<CuteQLottieRectCall6>(taken[6]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieRect::fallbackPath();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieRectCall7 call = reinterpret_cast<CuteQLottieRectCall7>(taken[7]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieRectCall8 call = reinterpret_cast<CuteQLottieRectCall8>(taken[8]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieRectCall9 call = reinterpret_cast<CuteQLottieRectCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieRectCall10 call = reinterpret_cast<CuteQLottieRectCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieRectCall11 call = reinterpret_cast<CuteQLottieRectCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieRect::QLottieRect(const QLottieRect &other)
extern "C" Q_DECL_EXPORT
QLottieRect *ritual_ZN11QLottieRectC1ERKS_(const QLottieRect *other) {
  return new CuteQLottieRect(*other);
}

//  QLottieRect::QLottieRect(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieRect *ritual_ZN11QLottieRectC1EP11QLottieBase(QLottieBase *parent) {
  return new CuteQLottieRect(parent);
}

//  QLottieBase *QLottieRect::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK11QLottieRect5cloneEv(const QLottieRect *self) {
  return self->clone();
}

//  bool QLottieRect::setProperty(QLottieLiteral::PropertyType propertyType,
//      QVariant value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QLottieRect11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant(
    QLottieRect *self,
    QLottieLiteral::PropertyType propertyType,
    const QVariant *value) {
  return self->setProperty(propertyType, *value);
}

//  void QLottieRect::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieRect16updatePropertiesEi(
    QLottieRect *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieRect::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QLottieRect6renderER15QLottieRenderer(
    const QLottieRect *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  bool QLottieRect::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieRect11acceptsTrimEv(const QLottieRect *self) {
  return self->acceptsTrim();
}

//  int QLottieRect::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QLottieRect5parseERK11QJsonObject(
    QLottieRect *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QPointF QLottieRect::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QLottieRect8positionEv(const QLottieRect *self) {
  return new QPointF(self->position());
}

//  QSizeF QLottieRect::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK11QLottieRect4sizeEv(const QLottieRect *self) {
  return new QSizeF(self->size());
}

//  qreal QLottieRect::roundness() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QLottieRect9roundnessEv(const QLottieRect *self) {
  return self->roundness();
}

//  bool QLottieRect::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLottieRect10isAnimatedEv(const QLottieRect *self) {
  return self->isAnimated();
}

//  QPainterPath QLottieRect::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK11QLottieRect12fallbackPathEv(
    const QLottieRect *self) {
  return new QPainterPath(self->fallbackPath());
}

//  const QLottieProperty2D<QSizeF> &QLottieRect::sizeProperty() const
extern "C" Q_DECL_EXPORT
const QLottieProperty2D<QSizeF> *ritual_ZNK11QLottieRect12sizePropertyEv(
    const QLottieRect *self) {
  return &(self->sizeProperty());
}

//  const QLottieSpatialProperty &QLottieRect::positionProperty() const
extern "C" Q_DECL_EXPORT
QLottieSpatialProperty *ritual_ZNK11QLottieRect16positionPropertyEv(
    const QLottieRect *self) {
  return new QLottieSpatialProperty(self->positionProperty());
}

//  QLottieRect::~QLottieRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieRectD1Ev(QLottieRect *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieRect, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRect(
    QLottieRect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRect *>(self)->take(key, call);
}

//  QLottieBase *QLottieRect::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK11QLottieRect5cloneEv(const QLottieRect *self) {
  return self->QLottieRect::clone();
}

//  bool QLottieRect::setProperty(QLottieLiteral::PropertyType propertyType,
//      QVariant value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QLottieRect11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant(
    QLottieRect *self,
    QLottieLiteral::PropertyType propertyType,
    const QVariant *value) {
  return self->QLottieRect::setProperty(propertyType, *value);
}

//  void QLottieRect::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLottieRect16updatePropertiesEi(
    QLottieRect *self,
    int frame) {
  self->QLottieRect::updateProperties(frame);
}

//  bool QLottieRect::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QLottieRect11acceptsTrimEv(const QLottieRect *self) {
  return self->QLottieRect::acceptsTrim();
}

//  int QLottieRect::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN11QLottieRect5parseERK11QJsonObject(
    QLottieRect *self,
    const QJsonObject *definition) {
  return self->QLottieRect::parse(*definition);
}

//  bool QLottieRect::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QLottieRect10isAnimatedEv(const QLottieRect *self) {
  return self->QLottieRect::isAnimated();
}

//  QPainterPath QLottieRect::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK11QLottieRect12fallbackPathEv(
    const QLottieRect *self) {
  return new QPainterPath(self->QLottieRect::fallbackPath());
}
