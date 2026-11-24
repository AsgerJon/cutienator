//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieellipse_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieellipse_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QLottieEllipse that Python can take functions over in. Every QLottieEllipse
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieEllipseCall0)(const void *, int *);
typedef void (*CuteQLottieEllipseCall1)(const void *, int, int *);
typedef int (*CuteQLottieEllipseCall2)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieEllipseCall3)(const void *, int *);
typedef bool (*CuteQLottieEllipseCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieEllipseCall5)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieEllipseCall6)(const void *, int *);
typedef void (*CuteQLottieEllipseCall7)(const void *, const QLottieTrimPath *, int *);
typedef bool (*CuteQLottieEllipseCall8)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieEllipseCall9)(const void *, int, int *);
typedef void * (*CuteQLottieEllipseCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieEllipseCall11)(const void *, int *);
class CuteQLottieEllipse : public QLottieEllipse {
public:
  using QLottieEllipse::QLottieEllipse;
  CuteQLottieEllipse(const QLottieEllipse &other) : QLottieEllipse(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
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

  //  QLottieBase *QLottieEllipse::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieEllipseCall0 call = reinterpret_cast<CuteQLottieEllipseCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieEllipse::clone();
  }

  //  void QLottieEllipse::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieEllipseCall1 call = reinterpret_cast<CuteQLottieEllipseCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieEllipse::updateProperties(frame);
  }

  //  int QLottieEllipse::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieEllipseCall2 call = reinterpret_cast<CuteQLottieEllipseCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieEllipse::parse(definition);
  }

  //  bool QLottieEllipse::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieEllipseCall3 call = reinterpret_cast<CuteQLottieEllipseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieEllipse::acceptsTrim();
  }

  //  bool QLottieEllipse::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieEllipseCall4 call = reinterpret_cast<CuteQLottieEllipseCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieEllipse::isAnimated();
  }

  //  QPainterPath QLottieEllipse::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieEllipseCall5 call = reinterpret_cast<CuteQLottieEllipseCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieEllipse::fallbackPath();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieEllipseCall6 call = reinterpret_cast<CuteQLottieEllipseCall6>(taken[6]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieEllipseCall7 call = reinterpret_cast<CuteQLottieEllipseCall7>(taken[7]);
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
      CuteQLottieEllipseCall8 call = reinterpret_cast<CuteQLottieEllipseCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieEllipseCall9 call = reinterpret_cast<CuteQLottieEllipseCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieEllipseCall10 call = reinterpret_cast<CuteQLottieEllipseCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieEllipseCall11 call = reinterpret_cast<CuteQLottieEllipseCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieEllipse::QLottieEllipse(const QLottieEllipse &other)
extern "C" Q_DECL_EXPORT
QLottieEllipse *ritual_ZN14QLottieEllipseC1ERKS_(
    const QLottieEllipse *other) {
  return new CuteQLottieEllipse(*other);
}

//  QLottieEllipse::QLottieEllipse(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieEllipse *ritual_ZN14QLottieEllipseC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieEllipse(parent);
}

//  QLottieBase *QLottieEllipse::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK14QLottieEllipse5cloneEv(const QLottieEllipse *self) {
  return self->clone();
}

//  void QLottieEllipse::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLottieEllipse16updatePropertiesEi(
    QLottieEllipse *self,
    int frame) {
  self->updateProperties(frame);
}

//  int QLottieEllipse::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QLottieEllipse5parseERK11QJsonObject(
    QLottieEllipse *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  bool QLottieEllipse::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QLottieEllipse11acceptsTrimEv(const QLottieEllipse *self) {
  return self->acceptsTrim();
}

//  QPointF QLottieEllipse::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14QLottieEllipse8positionEv(const QLottieEllipse *self) {
  return new QPointF(self->position());
}

//  QSizeF QLottieEllipse::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK14QLottieEllipse4sizeEv(const QLottieEllipse *self) {
  return new QSizeF(self->size());
}

//  bool QLottieEllipse::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QLottieEllipse10isAnimatedEv(const QLottieEllipse *self) {
  return self->isAnimated();
}

//  QPainterPath QLottieEllipse::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK14QLottieEllipse12fallbackPathEv(
    const QLottieEllipse *self) {
  return new QPainterPath(self->fallbackPath());
}

//  const QLottieSpatialProperty &QLottieEllipse::positionProperty() const
extern "C" Q_DECL_EXPORT
QLottieSpatialProperty *ritual_ZNK14QLottieEllipse16positionPropertyEv(
    const QLottieEllipse *self) {
  return new QLottieSpatialProperty(self->positionProperty());
}

//  QLottieEllipse::~QLottieEllipse()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLottieEllipseD1Ev(QLottieEllipse *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieEllipse, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieEllipse(
    QLottieEllipse *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieEllipse *>(self)->take(key, call);
}

//  QLottieBase *QLottieEllipse::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK14QLottieEllipse5cloneEv(
    const QLottieEllipse *self) {
  return self->QLottieEllipse::clone();
}

//  void QLottieEllipse::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QLottieEllipse16updatePropertiesEi(
    QLottieEllipse *self,
    int frame) {
  self->QLottieEllipse::updateProperties(frame);
}

//  int QLottieEllipse::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN14QLottieEllipse5parseERK11QJsonObject(
    QLottieEllipse *self,
    const QJsonObject *definition) {
  return self->QLottieEllipse::parse(*definition);
}

//  bool QLottieEllipse::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QLottieEllipse11acceptsTrimEv(
    const QLottieEllipse *self) {
  return self->QLottieEllipse::acceptsTrim();
}

//  bool QLottieEllipse::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QLottieEllipse10isAnimatedEv(
    const QLottieEllipse *self) {
  return self->QLottieEllipse::isAnimated();
}

//  QPainterPath QLottieEllipse::fallbackPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK14QLottieEllipse12fallbackPathEv(
    const QLottieEllipse *self) {
  return new QPainterPath(self->QLottieEllipse::fallbackPath());
}
