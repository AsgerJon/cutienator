//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieprecomposition_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieprecomposition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QLottiePrecomposition that Python can take functions over in. Every QLottiePrecomposition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottiePrecompositionCall0)(const void *, int *);
typedef int (*CuteQLottiePrecompositionCall1)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottiePrecompositionCall2)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottiePrecompositionCall3)(const void *, int, int *);
typedef void * (*CuteQLottiePrecompositionCall4)(const void *, const QString *, int *);
typedef void (*CuteQLottiePrecompositionCall5)(const void *, int, int *);
typedef const QSize * (*CuteQLottiePrecompositionCall6)(const void *, int *);
class CuteQLottiePrecomposition : public QLottiePrecomposition {
public:
  using QLottiePrecomposition::QLottiePrecomposition;
  CuteQLottiePrecomposition(const QLottiePrecomposition &other) : QLottiePrecomposition(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottiePrecomposition::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottiePrecompositionCall0 call = reinterpret_cast<CuteQLottiePrecompositionCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottiePrecomposition::clone();
  }

  //  int QLottiePrecomposition::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottiePrecompositionCall1 call = reinterpret_cast<CuteQLottiePrecompositionCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottiePrecomposition::parse(definition);
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottiePrecompositionCall2 call = reinterpret_cast<CuteQLottiePrecompositionCall2>(taken[2]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottiePrecompositionCall3 call = reinterpret_cast<CuteQLottiePrecompositionCall3>(taken[3]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottiePrecompositionCall4 call = reinterpret_cast<CuteQLottiePrecompositionCall4>(taken[4]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  void QLottieBase::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottiePrecompositionCall5 call = reinterpret_cast<CuteQLottiePrecompositionCall5>(taken[5]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieBase::updateProperties(frame);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottiePrecompositionCall6 call = reinterpret_cast<CuteQLottiePrecompositionCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottiePrecomposition::QLottiePrecomposition()
extern "C" Q_DECL_EXPORT
QLottiePrecomposition *ritual_ZN21QLottiePrecompositionC1Ev() {
  return new CuteQLottiePrecomposition();
}

//  QLottiePrecomposition::QLottiePrecomposition(const QLottiePrecomposition
//      &other)
extern "C" Q_DECL_EXPORT
QLottiePrecomposition *ritual_ZN21QLottiePrecompositionC1ERKS_(
    const QLottiePrecomposition *other) {
  return new CuteQLottiePrecomposition(*other);
}

//  QLottieBase *QLottiePrecomposition::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK21QLottiePrecomposition5cloneEv(
    const QLottiePrecomposition *self) {
  return self->clone();
}

//  QLottiePrecomposition *QLottiePrecomposition::construct(const QJsonObject
//      &definition, const QMap<QString, QJsonObject> &assets)
extern "C" Q_DECL_EXPORT
QLottiePrecomposition *ritual_ZN21QLottiePrecomposition9constructERK11QJsonObjectRK4QMapI7QStringS0_E(
    const QJsonObject *definition,
    const QMap<QString, QJsonObject> *assets) {
  return QLottiePrecomposition::construct(*definition, *assets);
}

//  int QLottiePrecomposition::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QLottiePrecomposition5parseERK11QJsonObject(
    QLottiePrecomposition *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QString QLottiePrecomposition::refId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QLottiePrecomposition5refIdEv(
    const QLottiePrecomposition *self) {
  return new QString(self->refId());
}

//  QLottiePrecomposition::~QLottiePrecomposition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottiePrecompositionD1Ev(QLottiePrecomposition *self) {
  delete self;
}

//  a Python function taken by a CuteQLottiePrecomposition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottiePrecomposition(
    QLottiePrecomposition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottiePrecomposition *>(self)->take(key, call);
}

//  QLottieBase *QLottiePrecomposition::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK21QLottiePrecomposition5cloneEv(
    const QLottiePrecomposition *self) {
  return self->QLottiePrecomposition::clone();
}

//  int QLottiePrecomposition::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN21QLottiePrecomposition5parseERK11QJsonObject(
    QLottiePrecomposition *self,
    const QJsonObject *definition) {
  return self->QLottiePrecomposition::parse(*definition);
}

//  QMap<QString, QLottiePrecomposition *>: QMap<QString,
//      QLottiePrecomposition *>()
extern "C" Q_DECL_EXPORT
QMap<QString, QLottiePrecomposition *> *ritual_map_make_QMap_QString_QLottiePrecomposition_ptr() {
  return new QMap<QString, QLottiePrecomposition *>();
}

//  QMap<QString, QLottiePrecomposition *>: insert(const Key &key, const T
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_map_put_QMap_QString_QLottiePrecomposition_ptr(
    QMap<QString, QLottiePrecomposition *> *self,
    const QString *key,
    QLottiePrecomposition *value) {
  self->insert(*key, value);
}

//  QMap<QString, QLottiePrecomposition *>: size() const
extern "C" Q_DECL_EXPORT
long long ritual_map_size_QMap_QString_QLottiePrecomposition_ptr(
    const QMap<QString, QLottiePrecomposition *> *self) {
  return self->size();
}

//  QMap<QString, QLottiePrecomposition *>: the key at a place
extern "C" Q_DECL_EXPORT
QString *ritual_map_key_QMap_QString_QLottiePrecomposition_ptr(
    const QMap<QString, QLottiePrecomposition *> *self,
    long long index) {
  return new QString(*std::next(self->keyBegin(), index));
}

//  QMap<QString, QLottiePrecomposition *>: the value at a place
extern "C" Q_DECL_EXPORT
QLottiePrecomposition *ritual_map_value_QMap_QString_QLottiePrecomposition_ptr(
    const QMap<QString, QLottiePrecomposition *> *self,
    long long index) {
  return *std::next(self->constBegin(), index);
}

//  QMap<QString, QLottiePrecomposition *>: contains(const Key &key) const
extern "C" Q_DECL_EXPORT
bool ritual_map_has_QMap_QString_QLottiePrecomposition_ptr(
    const QMap<QString, QLottiePrecomposition *> *self,
    const QString *key) {
  return self->contains(*key);
}

//  QMap<QString, QLottiePrecomposition *>: value(const Key &key) const
extern "C" Q_DECL_EXPORT
QLottiePrecomposition *ritual_map_get_QMap_QString_QLottiePrecomposition_ptr(
    const QMap<QString, QLottiePrecomposition *> *self,
    const QString *key) {
  return self->value(*key);
}

//  QMap<QString, QLottiePrecomposition *>: ~QMap()
extern "C" Q_DECL_EXPORT
void ritual_map_drop_QMap_QString_QLottiePrecomposition_ptr(
    QMap<QString, QLottiePrecomposition *> *self) {
  delete self;
}
