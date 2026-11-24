//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplace_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacecategory.h>
#include <QtPositioning/qgeolocation.h>
#include <QtLocation/qplaceratings.h>
#include <QtLocation/qplacesupplier.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplaceicon.h>
#include <QtLocation/qplaceattribute.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QPlacePrivate that Python can take functions over in. Every QPlacePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlacePrivateCall0)(const void *, int *);
typedef bool (*CuteQPlacePrivateCall1)(const void *, int *);
typedef const QGeoLocation * (*CuteQPlacePrivateCall2)(const void *, int *);
typedef void (*CuteQPlacePrivateCall3)(const void *, const QGeoLocation *, int *);
typedef const QPlaceRatings * (*CuteQPlacePrivateCall4)(const void *, int *);
typedef void (*CuteQPlacePrivateCall5)(const void *, const QPlaceRatings *, int *);
typedef const QPlaceSupplier * (*CuteQPlacePrivateCall6)(const void *, int *);
typedef void (*CuteQPlacePrivateCall7)(const void *, const QPlaceSupplier *, int *);
typedef QString * (*CuteQPlacePrivateCall8)(const void *, int *);
typedef void (*CuteQPlacePrivateCall9)(const void *, const QString *, int *);
typedef QString * (*CuteQPlacePrivateCall10)(const void *, int *);
typedef void (*CuteQPlacePrivateCall11)(const void *, const QString *, int *);
typedef QString * (*CuteQPlacePrivateCall12)(const void *, int *);
typedef void (*CuteQPlacePrivateCall13)(const void *, const QString *, int *);
typedef int (*CuteQPlacePrivateCall14)(const void *, int *);
typedef void (*CuteQPlacePrivateCall15)(const void *, int, int *);
typedef const QPlaceIcon * (*CuteQPlacePrivateCall16)(const void *, int *);
typedef void (*CuteQPlacePrivateCall17)(const void *, const QPlaceIcon *, int *);
typedef bool (*CuteQPlacePrivateCall18)(const void *, int *);
typedef void (*CuteQPlacePrivateCall19)(const void *, bool, int *);
typedef const QPlaceAttribute * (*CuteQPlacePrivateCall20)(const void *, const QString *, int *);
class CuteQPlacePrivate : public QPlacePrivate {
public:
  using QPlacePrivate::QPlacePrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QPlacePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate7isEmptyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate8locationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate11setLocationERK12QGeoLocation")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate7ratingsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate10setRatingsERK13QPlaceRatings")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate8supplierEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate11setSupplierERK14QPlaceSupplier")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate4nameEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate7setNameERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate7placeIdEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate10setPlaceIdERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate11attributionEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate14setAttributionERK7QString")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate10visibilityEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate13setVisibilityEN9QLocation10VisibilityE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate4iconEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate7setIconERK10QPlaceIcon")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate14detailsFetchedEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate17setDetailsFetchedEb")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate17extendedAttributeERK7QString")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  QPlacePrivate *QPlacePrivate::clone()
  QPlacePrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlacePrivateCall0 call = reinterpret_cast<CuteQPlacePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlacePrivate *>(given);
    }
    return {};
  }

  //  bool QPlacePrivate::isEmpty() const
  bool isEmpty() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlacePrivateCall1 call = reinterpret_cast<CuteQPlacePrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlacePrivate::isEmpty();
  }

  //  QGeoLocation QPlacePrivate::location() const
  QGeoLocation location() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlacePrivateCall2 call = reinterpret_cast<CuteQPlacePrivateCall2>(taken[2]);
      const QGeoLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QPlacePrivate::setLocation(const QGeoLocation &location)
  void setLocation(const QGeoLocation &location) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlacePrivateCall3 call = reinterpret_cast<CuteQPlacePrivateCall3>(taken[3]);
      call(this, &location, &handled);
      if (handled) return;
    }
  }

  //  QPlaceRatings QPlacePrivate::ratings() const
  QPlaceRatings ratings() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlacePrivateCall4 call = reinterpret_cast<CuteQPlacePrivateCall4>(taken[4]);
      const QPlaceRatings * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QPlacePrivate::setRatings(const QPlaceRatings &ratings)
  void setRatings(const QPlaceRatings &ratings) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlacePrivateCall5 call = reinterpret_cast<CuteQPlacePrivateCall5>(taken[5]);
      call(this, &ratings, &handled);
      if (handled) return;
    }
  }

  //  QPlaceSupplier QPlacePrivate::supplier() const
  QPlaceSupplier supplier() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlacePrivateCall6 call = reinterpret_cast<CuteQPlacePrivateCall6>(taken[6]);
      const QPlaceSupplier * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QPlacePrivate::setSupplier(const QPlaceSupplier &supplier)
  void setSupplier(const QPlaceSupplier &supplier) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlacePrivateCall7 call = reinterpret_cast<CuteQPlacePrivateCall7>(taken[7]);
      call(this, &supplier, &handled);
      if (handled) return;
    }
  }

  //  QString QPlacePrivate::name() const
  QString name() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlacePrivateCall8 call = reinterpret_cast<CuteQPlacePrivateCall8>(taken[8]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QPlacePrivate::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlacePrivateCall9 call = reinterpret_cast<CuteQPlacePrivateCall9>(taken[9]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }

  //  QString QPlacePrivate::placeId() const
  QString placeId() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlacePrivateCall10 call = reinterpret_cast<CuteQPlacePrivateCall10>(taken[10]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QPlacePrivate::setPlaceId(const QString &placeIdentifier)
  void setPlaceId(const QString &placeIdentifier) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlacePrivateCall11 call = reinterpret_cast<CuteQPlacePrivateCall11>(taken[11]);
      call(this, &placeIdentifier, &handled);
      if (handled) return;
    }
  }

  //  QString QPlacePrivate::attribution() const
  QString attribution() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlacePrivateCall12 call = reinterpret_cast<CuteQPlacePrivateCall12>(taken[12]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QPlacePrivate::setAttribution(const QString &attribution)
  void setAttribution(const QString &attribution) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlacePrivateCall13 call = reinterpret_cast<CuteQPlacePrivateCall13>(taken[13]);
      call(this, &attribution, &handled);
      if (handled) return;
    }
  }

  //  QLocation::Visibility QPlacePrivate::visibility() const
  QLocation::Visibility visibility() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlacePrivateCall14 call = reinterpret_cast<CuteQPlacePrivateCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLocation::Visibility>(given);
    }
    return {};
  }

  //  void QPlacePrivate::setVisibility(QLocation::Visibility visibility)
  void setVisibility(QLocation::Visibility visibility) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlacePrivateCall15 call = reinterpret_cast<CuteQPlacePrivateCall15>(taken[15]);
      call(this, static_cast<int>(visibility), &handled);
      if (handled) return;
    }
  }

  //  QPlaceIcon QPlacePrivate::icon() const
  QPlaceIcon icon() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlacePrivateCall16 call = reinterpret_cast<CuteQPlacePrivateCall16>(taken[16]);
      const QPlaceIcon * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QPlacePrivate::setIcon(const QPlaceIcon &icon)
  void setIcon(const QPlaceIcon &icon) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlacePrivateCall17 call = reinterpret_cast<CuteQPlacePrivateCall17>(taken[17]);
      call(this, &icon, &handled);
      if (handled) return;
    }
  }

  //  bool QPlacePrivate::detailsFetched() const
  bool detailsFetched() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlacePrivateCall18 call = reinterpret_cast<CuteQPlacePrivateCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlacePrivate::setDetailsFetched(bool fetched)
  void setDetailsFetched(bool fetched) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlacePrivateCall19 call = reinterpret_cast<CuteQPlacePrivateCall19>(taken[19]);
      call(this, fetched, &handled);
      if (handled) return;
    }
  }

  //  QPlaceAttribute QPlacePrivate::extendedAttribute(const QString
  //      &attributeType) const
  QPlaceAttribute extendedAttribute(
      const QString &attributeType) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlacePrivateCall20 call = reinterpret_cast<CuteQPlacePrivateCall20>(taken[20]);
      const QPlaceAttribute * given = call(this, &attributeType, &handled);
      if (handled && given) return *given;
    }
    return QPlacePrivate::extendedAttribute(attributeType);
  }
};

//  QPlacePrivate::~QPlacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivateD1Ev(QPlacePrivate *self) {
  delete self;
}

//  QPlacePrivate *QPlacePrivate::clone()
extern "C" Q_DECL_EXPORT
QPlacePrivate *ritual_ZN13QPlacePrivate5cloneEv(QPlacePrivate *self) {
  return self->clone();
}

//  bool QPlacePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlacePrivate7isEmptyEv(const QPlacePrivate *self) {
  return self->isEmpty();
}

//  QList<QPlaceCategory> QPlacePrivate::categories() const
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_ZNK13QPlacePrivate10categoriesEv(
    const QPlacePrivate *self) {
  return new QList<QPlaceCategory>(self->categories());
}

//  void QPlacePrivate::setCategories(const QList<QPlaceCategory>
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate13setCategoriesERK5QListI14QPlaceCategoryE(
    QPlacePrivate *self,
    const QList<QPlaceCategory> *categories) {
  self->setCategories(*categories);
}

//  QGeoLocation QPlacePrivate::location() const
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZNK13QPlacePrivate8locationEv(
    const QPlacePrivate *self) {
  return new QGeoLocation(self->location());
}

//  void QPlacePrivate::setLocation(const QGeoLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate11setLocationERK12QGeoLocation(
    QPlacePrivate *self,
    const QGeoLocation *location) {
  self->setLocation(*location);
}

//  QPlaceRatings QPlacePrivate::ratings() const
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_ZNK13QPlacePrivate7ratingsEv(
    const QPlacePrivate *self) {
  return new QPlaceRatings(self->ratings());
}

//  void QPlacePrivate::setRatings(const QPlaceRatings &ratings)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate10setRatingsERK13QPlaceRatings(
    QPlacePrivate *self,
    const QPlaceRatings *ratings) {
  self->setRatings(*ratings);
}

//  QPlaceSupplier QPlacePrivate::supplier() const
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZNK13QPlacePrivate8supplierEv(
    const QPlacePrivate *self) {
  return new QPlaceSupplier(self->supplier());
}

//  void QPlacePrivate::setSupplier(const QPlaceSupplier &supplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate11setSupplierERK14QPlaceSupplier(
    QPlacePrivate *self,
    const QPlaceSupplier *supplier) {
  self->setSupplier(*supplier);
}

//  QString QPlacePrivate::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlacePrivate4nameEv(const QPlacePrivate *self) {
  return new QString(self->name());
}

//  void QPlacePrivate::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate7setNameERK7QString(
    QPlacePrivate *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QPlacePrivate::placeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlacePrivate7placeIdEv(const QPlacePrivate *self) {
  return new QString(self->placeId());
}

//  void QPlacePrivate::setPlaceId(const QString &placeIdentifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate10setPlaceIdERK7QString(
    QPlacePrivate *self,
    const QString *placeIdentifier) {
  self->setPlaceId(*placeIdentifier);
}

//  QString QPlacePrivate::attribution() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlacePrivate11attributionEv(
    const QPlacePrivate *self) {
  return new QString(self->attribution());
}

//  void QPlacePrivate::setAttribution(const QString &attribution)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate14setAttributionERK7QString(
    QPlacePrivate *self,
    const QString *attribution) {
  self->setAttribution(*attribution);
}

//  QLocation::Visibility QPlacePrivate::visibility() const
extern "C" Q_DECL_EXPORT
QLocation::Visibility ritual_ZNK13QPlacePrivate10visibilityEv(
    const QPlacePrivate *self) {
  return self->visibility();
}

//  void QPlacePrivate::setVisibility(QLocation::Visibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate13setVisibilityEN9QLocation10VisibilityE(
    QPlacePrivate *self,
    QLocation::Visibility visibility) {
  self->setVisibility(visibility);
}

//  QPlaceIcon QPlacePrivate::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK13QPlacePrivate4iconEv(const QPlacePrivate *self) {
  return new QPlaceIcon(self->icon());
}

//  void QPlacePrivate::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate7setIconERK10QPlaceIcon(
    QPlacePrivate *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  bool QPlacePrivate::detailsFetched() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlacePrivate14detailsFetchedEv(const QPlacePrivate *self) {
  return self->detailsFetched();
}

//  void QPlacePrivate::setDetailsFetched(bool fetched)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlacePrivate17setDetailsFetchedEb(
    QPlacePrivate *self,
    bool fetched) {
  self->setDetailsFetched(fetched);
}

//  QMap<QString, QPlaceAttribute> QPlacePrivate::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QPlaceAttribute> *ritual_ZNK13QPlacePrivate18extendedAttributesEv(
    const QPlacePrivate *self) {
  return new QMap<QString, QPlaceAttribute>(self->extendedAttributes());
}

//  QPlaceAttribute QPlacePrivate::extendedAttribute(const QString
//      &attributeType) const
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_ZNK13QPlacePrivate17extendedAttributeERK7QString(
    const QPlacePrivate *self,
    const QString *attributeType) {
  return new QPlaceAttribute(self->extendedAttribute(*attributeType));
}

//  a Python function taken by a CuteQPlacePrivate, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlacePrivate(
    QPlacePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlacePrivate *>(self)->take(key, call);
}

//  bool QPlacePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QPlacePrivate7isEmptyEv(const QPlacePrivate *self) {
  return self->QPlacePrivate::isEmpty();
}

//  QPlaceAttribute QPlacePrivate::extendedAttribute(const QString
//      &attributeType) const
extern "C" Q_DECL_EXPORT
QPlaceAttribute *ritual_own_ZNK13QPlacePrivate17extendedAttributeERK7QString(
    const QPlacePrivate *self,
    const QString *attributeType) {
  return new QPlaceAttribute(
      self->QPlacePrivate::extendedAttribute(
          *attributeType));
}
