//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieTrimPath that Python can take functions over in. Every QLottieTrimPath
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieTrimPathCall0)(const void *, int *);
typedef int (*CuteQLottieTrimPathCall1)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottieTrimPathCall2)(const void *, int, int *);
typedef bool (*CuteQLottieTrimPathCall3)(const void *, int *);
typedef void (*CuteQLottieTrimPathCall4)(const void *, const QLottieTrimPath *, int *);
typedef bool (*CuteQLottieTrimPathCall5)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieTrimPathCall6)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieTrimPathCall7)(const void *, int *);
typedef bool (*CuteQLottieTrimPathCall8)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieTrimPathCall9)(const void *, int, int *);
typedef void * (*CuteQLottieTrimPathCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieTrimPathCall11)(const void *, int *);
class CuteQLottieTrimPath : public QLottieTrimPath {
public:
  using QLottieTrimPath::QLottieTrimPath;
  CuteQLottieTrimPath(const QLottieTrimPath & other) : QLottieTrimPath(other) {}
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
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
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

  //  QLottieBase *QLottieTrimPath::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieTrimPathCall0 call = reinterpret_cast<CuteQLottieTrimPathCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieTrimPath::clone();
  }

  //  int QLottieTrimPath::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieTrimPathCall1 call = reinterpret_cast<CuteQLottieTrimPathCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieTrimPath::parse(definition);
  }

  //  void QLottieTrimPath::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieTrimPathCall2 call = reinterpret_cast<CuteQLottieTrimPathCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieTrimPath::updateProperties(frame);
  }

  //  bool QLottieTrimPath::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieTrimPathCall3 call = reinterpret_cast<CuteQLottieTrimPathCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieTrimPath::acceptsTrim();
  }

  //  void QLottieTrimPath::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieTrimPathCall4 call = reinterpret_cast<CuteQLottieTrimPathCall4>(taken[4]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieTrimPath::applyTrim(trimmer);
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieTrimPathCall5 call = reinterpret_cast<CuteQLottieTrimPathCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieTrimPathCall6 call = reinterpret_cast<CuteQLottieTrimPathCall6>(taken[6]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieTrimPathCall7 call = reinterpret_cast<CuteQLottieTrimPathCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQLottieTrimPathCall8 call = reinterpret_cast<CuteQLottieTrimPathCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieTrimPathCall9 call = reinterpret_cast<CuteQLottieTrimPathCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieTrimPathCall10 call = reinterpret_cast<CuteQLottieTrimPathCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieTrimPathCall11 call = reinterpret_cast<CuteQLottieTrimPathCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieTrimPath::QLottieTrimPath(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieTrimPath *ritual_ZN15QLottieTrimPathC1EP11QLottieBase(
    QLottieBase *parent) {
  return new CuteQLottieTrimPath(parent);
}

//  QLottieTrimPath::QLottieTrimPath(const QLottieTrimPath &other)
extern "C" Q_DECL_EXPORT
QLottieTrimPath *ritual_ZN15QLottieTrimPathC1ERKS_(
    const QLottieTrimPath *other) {
  return new CuteQLottieTrimPath(*other);
}

//  QLottieBase *QLottieTrimPath::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK15QLottieTrimPath5cloneEv(
    const QLottieTrimPath *self) {
  return self->clone();
}

//  int QLottieTrimPath::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QLottieTrimPath5parseERK11QJsonObject(
    QLottieTrimPath *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieTrimPath::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieTrimPath16updatePropertiesEi(
    QLottieTrimPath *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieTrimPath::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QLottieTrimPath6renderER15QLottieRenderer(
    const QLottieTrimPath *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  bool QLottieTrimPath::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QLottieTrimPath11acceptsTrimEv(
    const QLottieTrimPath *self) {
  return self->acceptsTrim();
}

//  void QLottieTrimPath::applyTrim(const QLottieTrimPath &trimmer)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieTrimPath9applyTrimERKS_(
    QLottieTrimPath *self,
    const QLottieTrimPath *trimmer) {
  self->applyTrim(*trimmer);
}

//  qreal QLottieTrimPath::start() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottieTrimPath5startEv(const QLottieTrimPath *self) {
  return self->start();
}

//  qreal QLottieTrimPath::end() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottieTrimPath3endEv(const QLottieTrimPath *self) {
  return self->end();
}

//  qreal QLottieTrimPath::offset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QLottieTrimPath6offsetEv(const QLottieTrimPath *self) {
  return self->offset();
}

//  bool QLottieTrimPath::isParallel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QLottieTrimPath10isParallelEv(const QLottieTrimPath *self) {
  return self->isParallel();
}

//  QPainterPath QLottieTrimPath::trim(const QPainterPath &path) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK15QLottieTrimPath4trimERK12QPainterPath(
    const QLottieTrimPath *self,
    const QPainterPath *path) {
  return new QPainterPath(self->trim(*path));
}

//  QLottieProperty<qreal> QLottieTrimPath::startProperty() const
extern "C" Q_DECL_EXPORT
QLottieProperty<qreal> *ritual_ZNK15QLottieTrimPath13startPropertyEv(
    const QLottieTrimPath *self) {
  return new QLottieProperty<qreal>(self->startProperty());
}

//  QLottieProperty<qreal> QLottieTrimPath::endProperty() const
extern "C" Q_DECL_EXPORT
QLottieProperty<qreal> *ritual_ZNK15QLottieTrimPath11endPropertyEv(
    const QLottieTrimPath *self) {
  return new QLottieProperty<qreal>(self->endProperty());
}

//  QLottieProperty<qreal> QLottieTrimPath::offsetProperty() const
extern "C" Q_DECL_EXPORT
QLottieProperty<qreal> *ritual_ZNK15QLottieTrimPath14offsetPropertyEv(
    const QLottieTrimPath *self) {
  return new QLottieProperty<qreal>(self->offsetProperty());
}

//  QLottieTrimPath::~QLottieTrimPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieTrimPathD1Ev(QLottieTrimPath *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieTrimPath, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieTrimPath(
    QLottieTrimPath *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieTrimPath *>(self)->take(key, call);
}

//  QLottieBase *QLottieTrimPath::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK15QLottieTrimPath5cloneEv(
    const QLottieTrimPath *self) {
  return self->QLottieTrimPath::clone();
}

//  int QLottieTrimPath::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN15QLottieTrimPath5parseERK11QJsonObject(
    QLottieTrimPath *self,
    const QJsonObject *definition) {
  return self->QLottieTrimPath::parse(*definition);
}

//  void QLottieTrimPath::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieTrimPath16updatePropertiesEi(
    QLottieTrimPath *self,
    int frame) {
  self->QLottieTrimPath::updateProperties(frame);
}

//  bool QLottieTrimPath::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QLottieTrimPath11acceptsTrimEv(
    const QLottieTrimPath *self) {
  return self->QLottieTrimPath::acceptsTrim();
}

//  void QLottieTrimPath::applyTrim(const QLottieTrimPath &trimmer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieTrimPath9applyTrimERKS_(
    QLottieTrimPath *self,
    const QLottieTrimPath *trimmer) {
  self->QLottieTrimPath::applyTrim(*trimmer);
}

//  a QLottieProperty<qreal> a ritual of QLottieTrimPath gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLottieTrimPath__QLottieProperty_qreal(
    QLottieProperty<qreal> *self) {
  delete self;
}
