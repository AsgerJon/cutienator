//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieshape_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieShape that Python can take functions over in. Every QLottieShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieShapeCall0)(const void *, int *);
typedef bool (*CuteQLottieShapeCall1)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieShapeCall2)(const void *, int *);
typedef bool (*CuteQLottieShapeCall3)(const void *, int *);
typedef void (*CuteQLottieShapeCall4)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieShapeCall5)(const void *, int *);
typedef bool (*CuteQLottieShapeCall6)(const void *, int, const QVariant *, int *);
typedef int (*CuteQLottieShapeCall7)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieShapeCall8)(const void *, int, int *);
typedef void * (*CuteQLottieShapeCall9)(const void *, const QString *, int *);
typedef void (*CuteQLottieShapeCall10)(const void *, int, int *);
typedef const QSize * (*CuteQLottieShapeCall11)(const void *, int *);
class CuteQLottieShape : public QLottieShape {
public:
  using QLottieShape::QLottieShape;
  CuteQLottieShape(const QLottieShape &other) : QLottieShape(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieShape::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieShapeCall0 call = reinterpret_cast<CuteQLottieShapeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieShape::clone();
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieShapeCall1 call = reinterpret_cast<CuteQLottieShapeCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieShapeCall2 call = reinterpret_cast<CuteQLottieShapeCall2>(taken[2]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  bool QLottieShape::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieShapeCall3 call = reinterpret_cast<CuteQLottieShapeCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::acceptsTrim();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieShapeCall4 call = reinterpret_cast<CuteQLottieShapeCall4>(taken[4]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieShapeCall5 call = reinterpret_cast<CuteQLottieShapeCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::fallbackPath();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieShapeCall6 call = reinterpret_cast<CuteQLottieShapeCall6>(taken[6]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  int QLottieBase::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieShapeCall7 call = reinterpret_cast<CuteQLottieShapeCall7>(taken[7]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBase::parse(definition);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieShapeCall8 call = reinterpret_cast<CuteQLottieShapeCall8>(taken[8]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieShapeCall9 call = reinterpret_cast<CuteQLottieShapeCall9>(taken[9]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  void QLottieBase::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieShapeCall10 call = reinterpret_cast<CuteQLottieShapeCall10>(taken[10]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieBase::updateProperties(frame);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieShapeCall11 call = reinterpret_cast<CuteQLottieShapeCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieShape::QLottieShape()
extern "C" Q_DECL_EXPORT
QLottieShape *ritual_ZN12QLottieShapeC1Ev() {
  return new CuteQLottieShape();
}

//  QLottieShape::~QLottieShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieShapeD1Ev(QLottieShape *self) {
  delete self;
}

//  QLottieShape::QLottieShape(const QLottieShape &other)
extern "C" Q_DECL_EXPORT
QLottieShape *ritual_ZN12QLottieShapeC1ERKS_(const QLottieShape *other) {
  return new CuteQLottieShape(*other);
}

//  QLottieBase *QLottieShape::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK12QLottieShape5cloneEv(const QLottieShape *self) {
  return self->clone();
}

//  QLottieShape *QLottieShape::construct(QJsonObject definition, QLottieBase
//      *parent)
extern "C" Q_DECL_EXPORT
QLottieShape *ritual_ZN12QLottieShape9constructE11QJsonObjectP11QLottieBase(
    const QJsonObject *definition,
    QLottieBase *parent) {
  return QLottieShape::construct(*definition, parent);
}

//  bool QLottieShape::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieShape10isAnimatedEv(const QLottieShape *self) {
  return self->isAnimated();
}

//  const QPainterPath &QLottieShape::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QLottieShape4pathEv(const QLottieShape *self) {
  return new QPainterPath(self->path());
}

//  bool QLottieShape::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieShape11acceptsTrimEv(const QLottieShape *self) {
  return self->acceptsTrim();
}

//  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieShape9applyTrimERK15QLottieTrimPath(
    QLottieShape *self,
    const QLottieTrimPath *trimmer) {
  self->applyTrim(*trimmer);
}

//  const QLottieTrimPath *QLottieShape::currentTrim() const
extern "C" Q_DECL_EXPORT
const QLottieTrimPath *ritual_ZNK12QLottieShape11currentTrimEv(
    const QLottieShape *self) {
  return self->currentTrim();
}

//  QPainterPath QLottieShape::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK12QLottieShape12fallbackPathEv(
    const QLottieShape *self) {
  return new QPainterPath(self->fallbackPath());
}

//  int QLottieShape::direction() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLottieShape9directionEv(const QLottieShape *self) {
  return self->direction();
}

//  bool QLottieShape::hasReversedDirection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieShape20hasReversedDirectionEv(
    const QLottieShape *self) {
  return self->hasReversedDirection();
}

//  a Python function taken by a CuteQLottieShape, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieShape(
    QLottieShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieShape *>(self)->take(key, call);
}

//  QLottieBase *QLottieShape::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK12QLottieShape5cloneEv(const QLottieShape *self) {
  return self->QLottieShape::clone();
}

//  bool QLottieShape::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLottieShape10isAnimatedEv(const QLottieShape *self) {
  return self->QLottieShape::isAnimated();
}

//  const QPainterPath &QLottieShape::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK12QLottieShape4pathEv(const QLottieShape *self) {
  return new QPainterPath(self->QLottieShape::path());
}

//  bool QLottieShape::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLottieShape11acceptsTrimEv(const QLottieShape *self) {
  return self->QLottieShape::acceptsTrim();
}

//  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLottieShape9applyTrimERK15QLottieTrimPath(
    QLottieShape *self,
    const QLottieTrimPath *trimmer) {
  self->QLottieShape::applyTrim(*trimmer);
}

//  QPainterPath QLottieShape::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK12QLottieShape12fallbackPathEv(
    const QLottieShape *self) {
  return new QPainterPath(self->QLottieShape::fallbackPath());
}
