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
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QList>
#include <QtLocation/QPlaceContactDetail>

//  A QPlacePrivateDefault that Python can take functions over in. Every QPlacePrivateDefault
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlacePrivateDefaultCall0)(const void *, int *);
typedef const QGeoLocation * (*CuteQPlacePrivateDefaultCall1)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall2)(const void *, const QGeoLocation *, int *);
typedef const QPlaceRatings * (*CuteQPlacePrivateDefaultCall3)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall4)(const void *, const QPlaceRatings *, int *);
typedef const QPlaceSupplier * (*CuteQPlacePrivateDefaultCall5)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall6)(const void *, const QPlaceSupplier *, int *);
typedef QString * (*CuteQPlacePrivateDefaultCall7)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall8)(const void *, const QString *, int *);
typedef QString * (*CuteQPlacePrivateDefaultCall9)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall10)(const void *, const QString *, int *);
typedef QString * (*CuteQPlacePrivateDefaultCall11)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall12)(const void *, const QString *, int *);
typedef int (*CuteQPlacePrivateDefaultCall13)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall14)(const void *, int, int *);
typedef const QPlaceIcon * (*CuteQPlacePrivateDefaultCall15)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall16)(const void *, const QPlaceIcon *, int *);
typedef bool (*CuteQPlacePrivateDefaultCall17)(const void *, int *);
typedef void (*CuteQPlacePrivateDefaultCall18)(const void *, bool, int *);
typedef bool (*CuteQPlacePrivateDefaultCall19)(const void *, int *);
typedef const QPlaceAttribute * (*CuteQPlacePrivateDefaultCall20)(const void *, const QString *, int *);
class CuteQPlacePrivateDefault : public QPlacePrivateDefault {
public:
  using QPlacePrivateDefault::QPlacePrivateDefault;
  CuteQPlacePrivateDefault(const QPlacePrivateDefault & other) : QPlacePrivateDefault(other) {}
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QPlacePrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate8locationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate11setLocationERK12QGeoLocation")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate7ratingsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate10setRatingsERK13QPlaceRatings")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate8supplierEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate11setSupplierERK14QPlaceSupplier")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate4nameEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate7setNameERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate7placeIdEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate10setPlaceIdERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate11attributionEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate14setAttributionERK7QString")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate10visibilityEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate13setVisibilityEN9QLocation10VisibilityE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate4iconEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate7setIconERK10QPlaceIcon")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate14detailsFetchedEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlacePrivate17setDetailsFetchedEb")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate7isEmptyEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlacePrivate17extendedAttributeERK7QString")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  QPlacePrivate *QPlacePrivateDefault::clone()
  QPlacePrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall0 call = reinterpret_cast<CuteQPlacePrivateDefaultCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlacePrivate *>(given);
    }
    return QPlacePrivateDefault::clone();
  }

  //  QGeoLocation QPlacePrivateDefault::location() const
  QGeoLocation location() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall1 call = reinterpret_cast<CuteQPlacePrivateDefaultCall1>(taken[1]);
      const QGeoLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlacePrivateDefault::location();
  }

  //  void QPlacePrivateDefault::setLocation(const QGeoLocation &location)
  void setLocation(const QGeoLocation &location) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall2 call = reinterpret_cast<CuteQPlacePrivateDefaultCall2>(taken[2]);
      call(this, &location, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setLocation(location);
  }

  //  QPlaceRatings QPlacePrivateDefault::ratings() const
  QPlaceRatings ratings() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall3 call = reinterpret_cast<CuteQPlacePrivateDefaultCall3>(taken[3]);
      const QPlaceRatings * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlacePrivateDefault::ratings();
  }

  //  void QPlacePrivateDefault::setRatings(const QPlaceRatings &ratings)
  void setRatings(const QPlaceRatings &ratings) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall4 call = reinterpret_cast<CuteQPlacePrivateDefaultCall4>(taken[4]);
      call(this, &ratings, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setRatings(ratings);
  }

  //  QPlaceSupplier QPlacePrivateDefault::supplier() const
  QPlaceSupplier supplier() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall5 call = reinterpret_cast<CuteQPlacePrivateDefaultCall5>(taken[5]);
      const QPlaceSupplier * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlacePrivateDefault::supplier();
  }

  //  void QPlacePrivateDefault::setSupplier(const QPlaceSupplier
  //      &supplier)
  void setSupplier(const QPlaceSupplier &supplier) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall6 call = reinterpret_cast<CuteQPlacePrivateDefaultCall6>(taken[6]);
      call(this, &supplier, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setSupplier(supplier);
  }

  //  QString QPlacePrivateDefault::name() const
  QString name() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall7 call = reinterpret_cast<CuteQPlacePrivateDefaultCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlacePrivateDefault::name();
  }

  //  void QPlacePrivateDefault::setName(const QString &name)
  void setName(const QString &name) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall8 call = reinterpret_cast<CuteQPlacePrivateDefaultCall8>(taken[8]);
      call(this, &name, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setName(name);
  }

  //  QString QPlacePrivateDefault::placeId() const
  QString placeId() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall9 call = reinterpret_cast<CuteQPlacePrivateDefaultCall9>(taken[9]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlacePrivateDefault::placeId();
  }

  //  void QPlacePrivateDefault::setPlaceId(const QString &placeIdentifier)
  void setPlaceId(const QString &placeIdentifier) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall10 call = reinterpret_cast<CuteQPlacePrivateDefaultCall10>(taken[10]);
      call(this, &placeIdentifier, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setPlaceId(placeIdentifier);
  }

  //  QString QPlacePrivateDefault::attribution() const
  QString attribution() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall11 call = reinterpret_cast<CuteQPlacePrivateDefaultCall11>(taken[11]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlacePrivateDefault::attribution();
  }

  //  void QPlacePrivateDefault::setAttribution(const QString &attribution)
  void setAttribution(const QString &attribution) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall12 call = reinterpret_cast<CuteQPlacePrivateDefaultCall12>(taken[12]);
      call(this, &attribution, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setAttribution(attribution);
  }

  //  QLocation::Visibility QPlacePrivateDefault::visibility() const
  QLocation::Visibility visibility() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall13 call = reinterpret_cast<CuteQPlacePrivateDefaultCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLocation::Visibility>(given);
    }
    return QPlacePrivateDefault::visibility();
  }

  //  void QPlacePrivateDefault::setVisibility(QLocation::Visibility
  //      visibility)
  void setVisibility(QLocation::Visibility visibility) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall14 call = reinterpret_cast<CuteQPlacePrivateDefaultCall14>(taken[14]);
      call(this, static_cast<int>(visibility), &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setVisibility(visibility);
  }

  //  QPlaceIcon QPlacePrivateDefault::icon() const
  QPlaceIcon icon() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall15 call = reinterpret_cast<CuteQPlacePrivateDefaultCall15>(taken[15]);
      const QPlaceIcon * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlacePrivateDefault::icon();
  }

  //  void QPlacePrivateDefault::setIcon(const QPlaceIcon &icon)
  void setIcon(const QPlaceIcon &icon) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall16 call = reinterpret_cast<CuteQPlacePrivateDefaultCall16>(taken[16]);
      call(this, &icon, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setIcon(icon);
  }

  //  bool QPlacePrivateDefault::detailsFetched() const
  bool detailsFetched() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall17 call = reinterpret_cast<CuteQPlacePrivateDefaultCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlacePrivateDefault::detailsFetched();
  }

  //  void QPlacePrivateDefault::setDetailsFetched(bool fetched)
  void setDetailsFetched(bool fetched) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall18 call = reinterpret_cast<CuteQPlacePrivateDefaultCall18>(taken[18]);
      call(this, fetched, &handled);
      if (handled) return;
    }
    QPlacePrivateDefault::setDetailsFetched(fetched);
  }

  //  bool QPlacePrivate::isEmpty() const
  bool isEmpty() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall19 call = reinterpret_cast<CuteQPlacePrivateDefaultCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlacePrivate::isEmpty();
  }

  //  QPlaceAttribute QPlacePrivate::extendedAttribute(const QString
  //      &attributeType) const
  QPlaceAttribute extendedAttribute(
      const QString &attributeType) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlacePrivateDefaultCall20 call = reinterpret_cast<CuteQPlacePrivateDefaultCall20>(taken[20]);
      const QPlaceAttribute * given = call(this, &attributeType, &handled);
      if (handled && given) return *given;
    }
    return QPlacePrivate::extendedAttribute(attributeType);
  }
};

//  QPlacePrivateDefault::QPlacePrivateDefault()
extern "C" Q_DECL_EXPORT
QPlacePrivateDefault *ritual_ZN20QPlacePrivateDefaultC1Ev() {
  return new CuteQPlacePrivateDefault();
}

//  QPlacePrivateDefault::QPlacePrivateDefault(const QPlacePrivateDefault
//      &other)
extern "C" Q_DECL_EXPORT
QPlacePrivateDefault *ritual_ZN20QPlacePrivateDefaultC1ERKS_(
    const QPlacePrivateDefault *other) {
  return new CuteQPlacePrivateDefault(*other);
}

//  QPlacePrivateDefault::~QPlacePrivateDefault()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefaultD1Ev(QPlacePrivateDefault *self) {
  delete self;
}

//  QPlacePrivate *QPlacePrivateDefault::clone()
extern "C" Q_DECL_EXPORT
QPlacePrivate *ritual_ZN20QPlacePrivateDefault5cloneEv(
    QPlacePrivateDefault *self) {
  return self->clone();
}

//  QList<QPlaceCategory> QPlacePrivateDefault::categories() const
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_ZNK20QPlacePrivateDefault10categoriesEv(
    const QPlacePrivateDefault *self) {
  return new QList<QPlaceCategory>(self->categories());
}

//  void QPlacePrivateDefault::setCategories(const QList<QPlaceCategory>
//      &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault13setCategoriesERK5QListI14QPlaceCategoryE(
    QPlacePrivateDefault *self,
    const QList<QPlaceCategory> *categories) {
  self->setCategories(*categories);
}

//  QGeoLocation QPlacePrivateDefault::location() const
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZNK20QPlacePrivateDefault8locationEv(
    const QPlacePrivateDefault *self) {
  return new QGeoLocation(self->location());
}

//  void QPlacePrivateDefault::setLocation(const QGeoLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault11setLocationERK12QGeoLocation(
    QPlacePrivateDefault *self,
    const QGeoLocation *location) {
  self->setLocation(*location);
}

//  QPlaceRatings QPlacePrivateDefault::ratings() const
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_ZNK20QPlacePrivateDefault7ratingsEv(
    const QPlacePrivateDefault *self) {
  return new QPlaceRatings(self->ratings());
}

//  void QPlacePrivateDefault::setRatings(const QPlaceRatings &ratings)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault10setRatingsERK13QPlaceRatings(
    QPlacePrivateDefault *self,
    const QPlaceRatings *ratings) {
  self->setRatings(*ratings);
}

//  QPlaceSupplier QPlacePrivateDefault::supplier() const
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZNK20QPlacePrivateDefault8supplierEv(
    const QPlacePrivateDefault *self) {
  return new QPlaceSupplier(self->supplier());
}

//  void QPlacePrivateDefault::setSupplier(const QPlaceSupplier &supplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault11setSupplierERK14QPlaceSupplier(
    QPlacePrivateDefault *self,
    const QPlaceSupplier *supplier) {
  self->setSupplier(*supplier);
}

//  QString QPlacePrivateDefault::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlacePrivateDefault4nameEv(
    const QPlacePrivateDefault *self) {
  return new QString(self->name());
}

//  void QPlacePrivateDefault::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault7setNameERK7QString(
    QPlacePrivateDefault *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QPlacePrivateDefault::placeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlacePrivateDefault7placeIdEv(
    const QPlacePrivateDefault *self) {
  return new QString(self->placeId());
}

//  void QPlacePrivateDefault::setPlaceId(const QString &placeIdentifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault10setPlaceIdERK7QString(
    QPlacePrivateDefault *self,
    const QString *placeIdentifier) {
  self->setPlaceId(*placeIdentifier);
}

//  QString QPlacePrivateDefault::attribution() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlacePrivateDefault11attributionEv(
    const QPlacePrivateDefault *self) {
  return new QString(self->attribution());
}

//  void QPlacePrivateDefault::setAttribution(const QString &attribution)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault14setAttributionERK7QString(
    QPlacePrivateDefault *self,
    const QString *attribution) {
  self->setAttribution(*attribution);
}

//  QLocation::Visibility QPlacePrivateDefault::visibility() const
extern "C" Q_DECL_EXPORT
QLocation::Visibility ritual_ZNK20QPlacePrivateDefault10visibilityEv(
    const QPlacePrivateDefault *self) {
  return self->visibility();
}

//  void QPlacePrivateDefault::setVisibility(QLocation::Visibility
//      visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault13setVisibilityEN9QLocation10VisibilityE(
    QPlacePrivateDefault *self,
    QLocation::Visibility visibility) {
  self->setVisibility(visibility);
}

//  QPlaceIcon QPlacePrivateDefault::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK20QPlacePrivateDefault4iconEv(
    const QPlacePrivateDefault *self) {
  return new QPlaceIcon(self->icon());
}

//  void QPlacePrivateDefault::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault7setIconERK10QPlaceIcon(
    QPlacePrivateDefault *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  bool QPlacePrivateDefault::detailsFetched() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlacePrivateDefault14detailsFetchedEv(
    const QPlacePrivateDefault *self) {
  return self->detailsFetched();
}

//  void QPlacePrivateDefault::setDetailsFetched(bool fetched)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlacePrivateDefault17setDetailsFetchedEb(
    QPlacePrivateDefault *self,
    bool fetched) {
  self->setDetailsFetched(fetched);
}

//  QMap<QString, QPlaceAttribute> QPlacePrivateDefault::extendedAttributes()
//      const
extern "C" Q_DECL_EXPORT
QMap<QString, QPlaceAttribute> *ritual_ZNK20QPlacePrivateDefault18extendedAttributesEv(
    const QPlacePrivateDefault *self) {
  return new QMap<QString, QPlaceAttribute>(self->extendedAttributes());
}

//  QMap<QString, QPlaceAttribute>
//      &QPlacePrivateDefault::extendedAttributes()
extern "C" Q_DECL_EXPORT
QMap<QString, QPlaceAttribute> *ritual_ZN20QPlacePrivateDefault18extendedAttributesEv(
    QPlacePrivateDefault *self) {
  return &(self->extendedAttributes());
}

//  QMap<QString, QList<QPlaceContactDetail>>
//      QPlacePrivateDefault::contacts() const
extern "C" Q_DECL_EXPORT
QMap<QString, QList<QPlaceContactDetail>> *ritual_ZNK20QPlacePrivateDefault8contactsEv(
    const QPlacePrivateDefault *self) {
  return new QMap<QString, QList<QPlaceContactDetail>>(self->contacts());
}

//  QMap<QString, QList<QPlaceContactDetail>>
//      &QPlacePrivateDefault::contacts()
extern "C" Q_DECL_EXPORT
QMap<QString, QList<QPlaceContactDetail>> *ritual_ZN20QPlacePrivateDefault8contactsEv(
    QPlacePrivateDefault *self) {
  return &(self->contacts());
}

//  a Python function taken by a CuteQPlacePrivateDefault, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlacePrivateDefault(
    QPlacePrivateDefault *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlacePrivateDefault *>(self)->take(key, call);
}

//  QPlacePrivate *QPlacePrivateDefault::clone()
extern "C" Q_DECL_EXPORT
QPlacePrivate *ritual_own_ZN20QPlacePrivateDefault5cloneEv(
    QPlacePrivateDefault *self) {
  return self->QPlacePrivateDefault::clone();
}

//  QGeoLocation QPlacePrivateDefault::location() const
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_own_ZNK20QPlacePrivateDefault8locationEv(
    const QPlacePrivateDefault *self) {
  return new QGeoLocation(self->QPlacePrivateDefault::location());
}

//  void QPlacePrivateDefault::setLocation(const QGeoLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault11setLocationERK12QGeoLocation(
    QPlacePrivateDefault *self,
    const QGeoLocation *location) {
  self->QPlacePrivateDefault::setLocation(*location);
}

//  QPlaceRatings QPlacePrivateDefault::ratings() const
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_own_ZNK20QPlacePrivateDefault7ratingsEv(
    const QPlacePrivateDefault *self) {
  return new QPlaceRatings(self->QPlacePrivateDefault::ratings());
}

//  void QPlacePrivateDefault::setRatings(const QPlaceRatings &ratings)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault10setRatingsERK13QPlaceRatings(
    QPlacePrivateDefault *self,
    const QPlaceRatings *ratings) {
  self->QPlacePrivateDefault::setRatings(*ratings);
}

//  QPlaceSupplier QPlacePrivateDefault::supplier() const
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_own_ZNK20QPlacePrivateDefault8supplierEv(
    const QPlacePrivateDefault *self) {
  return new QPlaceSupplier(self->QPlacePrivateDefault::supplier());
}

//  void QPlacePrivateDefault::setSupplier(const QPlaceSupplier &supplier)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault11setSupplierERK14QPlaceSupplier(
    QPlacePrivateDefault *self,
    const QPlaceSupplier *supplier) {
  self->QPlacePrivateDefault::setSupplier(*supplier);
}

//  QString QPlacePrivateDefault::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlacePrivateDefault4nameEv(
    const QPlacePrivateDefault *self) {
  return new QString(self->QPlacePrivateDefault::name());
}

//  void QPlacePrivateDefault::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault7setNameERK7QString(
    QPlacePrivateDefault *self,
    const QString *name) {
  self->QPlacePrivateDefault::setName(*name);
}

//  QString QPlacePrivateDefault::placeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlacePrivateDefault7placeIdEv(
    const QPlacePrivateDefault *self) {
  return new QString(self->QPlacePrivateDefault::placeId());
}

//  void QPlacePrivateDefault::setPlaceId(const QString &placeIdentifier)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault10setPlaceIdERK7QString(
    QPlacePrivateDefault *self,
    const QString *placeIdentifier) {
  self->QPlacePrivateDefault::setPlaceId(*placeIdentifier);
}

//  QString QPlacePrivateDefault::attribution() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlacePrivateDefault11attributionEv(
    const QPlacePrivateDefault *self) {
  return new QString(self->QPlacePrivateDefault::attribution());
}

//  void QPlacePrivateDefault::setAttribution(const QString &attribution)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault14setAttributionERK7QString(
    QPlacePrivateDefault *self,
    const QString *attribution) {
  self->QPlacePrivateDefault::setAttribution(*attribution);
}

//  QLocation::Visibility QPlacePrivateDefault::visibility() const
extern "C" Q_DECL_EXPORT
QLocation::Visibility ritual_own_ZNK20QPlacePrivateDefault10visibilityEv(
    const QPlacePrivateDefault *self) {
  return self->QPlacePrivateDefault::visibility();
}

//  void QPlacePrivateDefault::setVisibility(QLocation::Visibility
//      visibility)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault13setVisibilityEN9QLocation10VisibilityE(
    QPlacePrivateDefault *self,
    QLocation::Visibility visibility) {
  self->QPlacePrivateDefault::setVisibility(visibility);
}

//  QPlaceIcon QPlacePrivateDefault::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_own_ZNK20QPlacePrivateDefault4iconEv(
    const QPlacePrivateDefault *self) {
  return new QPlaceIcon(self->QPlacePrivateDefault::icon());
}

//  void QPlacePrivateDefault::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault7setIconERK10QPlaceIcon(
    QPlacePrivateDefault *self,
    const QPlaceIcon *icon) {
  self->QPlacePrivateDefault::setIcon(*icon);
}

//  bool QPlacePrivateDefault::detailsFetched() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlacePrivateDefault14detailsFetchedEv(
    const QPlacePrivateDefault *self) {
  return self->QPlacePrivateDefault::detailsFetched();
}

//  void QPlacePrivateDefault::setDetailsFetched(bool fetched)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlacePrivateDefault17setDetailsFetchedEb(
    QPlacePrivateDefault *self,
    bool fetched) {
  self->QPlacePrivateDefault::setDetailsFetched(fetched);
}

//  a QMap<QString, QList<QPlaceContactDetail>> a ritual of
//      QPlacePrivateDefault gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlacePrivateDefault__QMap_QString_QList_QPlaceContactDetail(
    QMap<QString, QList<QPlaceContactDetail>> *self) {
  delete self;
}
