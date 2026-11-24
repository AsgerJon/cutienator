//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativeplace_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativeplace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplaceratings.h>
#include <QtLocation/qplacesupplier.h>
#include <QtLocation/qplaceicon.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDeclarativePlace that Python can take functions over in. Every QDeclarativePlace
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePlaceCall0)(const void *, int *);
typedef void (*CuteQDeclarativePlaceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePlaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePlaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativePlace : public QDeclarativePlace {
public:
  using QDeclarativePlace::QDeclarativePlace;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDeclarativePlace::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePlaceCall0 call = reinterpret_cast<CuteQDeclarativePlaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePlace::classBegin();
  }

  //  void QDeclarativePlace::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePlaceCall1 call = reinterpret_cast<CuteQDeclarativePlaceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePlace::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePlaceCall2 call = reinterpret_cast<CuteQDeclarativePlaceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePlaceCall3 call = reinterpret_cast<CuteQDeclarativePlaceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePlaceCall4 call = reinterpret_cast<CuteQDeclarativePlaceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePlaceCall5 call = reinterpret_cast<CuteQDeclarativePlaceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePlaceCall6 call = reinterpret_cast<CuteQDeclarativePlaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePlaceCall7 call = reinterpret_cast<CuteQDeclarativePlaceCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativePlaceCall8 call = reinterpret_cast<CuteQDeclarativePlaceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativePlace::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QDeclarativePlace10metaObjectEv(
    const QDeclarativePlace *self) {
  return self->metaObject();
}

//  QString QDeclarativePlace::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QDeclarativePlace2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativePlace::tr(s, c, n));
}

//  QDeclarativePlace::QDeclarativePlace(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativePlace *ritual_ZN17QDeclarativePlaceC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativePlace(parent);
}

//  QDeclarativePlace::QDeclarativePlace(const QPlace &src,
//      QDeclarativeGeoServiceProvider *plugin, QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativePlace *ritual_ZN17QDeclarativePlaceC1ERK6QPlaceP30QDeclarativeGeoServiceProviderP7QObject(
    const QPlace *src,
    QDeclarativeGeoServiceProvider *plugin,
    QObject *parent) {
  return new CuteQDeclarativePlace(*src, plugin, parent);
}

//  QDeclarativePlace::~QDeclarativePlace()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlaceD1Ev(QDeclarativePlace *self) {
  delete self;
}

//  void QDeclarativePlace::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace10classBeginEv(QDeclarativePlace *self) {
  self->classBegin();
}

//  void QDeclarativePlace::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace17componentCompleteEv(
    QDeclarativePlace *self) {
  self->componentComplete();
}

//  void QDeclarativePlace::setPlugin(QDeclarativeGeoServiceProvider *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace9setPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativePlace *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setPlugin(plugin);
}

//  QDeclarativeGeoServiceProvider *QDeclarativePlace::plugin() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK17QDeclarativePlace6pluginEv(
    const QDeclarativePlace *self) {
  return self->plugin();
}

//  QDeclarativePlaceReviewModel *QDeclarativePlace::reviewModel()
extern "C" Q_DECL_EXPORT
QDeclarativePlaceReviewModel *ritual_ZN17QDeclarativePlace11reviewModelEv(
    QDeclarativePlace *self) {
  return self->reviewModel();
}

//  QDeclarativePlaceImageModel *QDeclarativePlace::imageModel()
extern "C" Q_DECL_EXPORT
QDeclarativePlaceImageModel *ritual_ZN17QDeclarativePlace10imageModelEv(
    QDeclarativePlace *self) {
  return self->imageModel();
}

//  QDeclarativePlaceEditorialModel *QDeclarativePlace::editorialModel()
extern "C" Q_DECL_EXPORT
QDeclarativePlaceEditorialModel *ritual_ZN17QDeclarativePlace14editorialModelEv(
    QDeclarativePlace *self) {
  return self->editorialModel();
}

//  QPlace QDeclarativePlace::place() const
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZNK17QDeclarativePlace5placeEv(
    const QDeclarativePlace *self) {
  return new QPlace(self->place());
}

//  void QDeclarativePlace::setPlace(const QPlace &src)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace8setPlaceERK6QPlace(
    QDeclarativePlace *self,
    const QPlace *src) {
  self->setPlace(*src);
}

//  QDeclarativeGeoLocation *QDeclarativePlace::location() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoLocation *ritual_ZNK17QDeclarativePlace8locationEv(
    const QDeclarativePlace *self) {
  return self->location();
}

//  void QDeclarativePlace::setLocation(QDeclarativeGeoLocation *location)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace11setLocationEP23QDeclarativeGeoLocation(
    QDeclarativePlace *self,
    QDeclarativeGeoLocation *location) {
  self->setLocation(location);
}

//  QPlaceRatings QDeclarativePlace::ratings() const
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_ZNK17QDeclarativePlace7ratingsEv(
    const QDeclarativePlace *self) {
  return new QPlaceRatings(self->ratings());
}

//  void QDeclarativePlace::setRatings(const QPlaceRatings &ratings)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace10setRatingsERK13QPlaceRatings(
    QDeclarativePlace *self,
    const QPlaceRatings *ratings) {
  self->setRatings(*ratings);
}

//  QPlaceSupplier QDeclarativePlace::supplier() const
extern "C" Q_DECL_EXPORT
QPlaceSupplier *ritual_ZNK17QDeclarativePlace8supplierEv(
    const QDeclarativePlace *self) {
  return new QPlaceSupplier(self->supplier());
}

//  void QDeclarativePlace::setSupplier(const QPlaceSupplier &supplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace11setSupplierERK14QPlaceSupplier(
    QDeclarativePlace *self,
    const QPlaceSupplier *supplier) {
  self->setSupplier(*supplier);
}

//  QPlaceIcon QDeclarativePlace::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK17QDeclarativePlace4iconEv(
    const QDeclarativePlace *self) {
  return new QPlaceIcon(self->icon());
}

//  void QDeclarativePlace::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace7setIconERK10QPlaceIcon(
    QDeclarativePlace *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  QString QDeclarativePlace::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace4nameEv(
    const QDeclarativePlace *self) {
  return new QString(self->name());
}

//  void QDeclarativePlace::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace7setNameERK7QString(
    QDeclarativePlace *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QDeclarativePlace::placeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace7placeIdEv(
    const QDeclarativePlace *self) {
  return new QString(self->placeId());
}

//  void QDeclarativePlace::setPlaceId(const QString &placeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace10setPlaceIdERK7QString(
    QDeclarativePlace *self,
    const QString *placeId) {
  self->setPlaceId(*placeId);
}

//  QString QDeclarativePlace::attribution() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace11attributionEv(
    const QDeclarativePlace *self) {
  return new QString(self->attribution());
}

//  void QDeclarativePlace::setAttribution(const QString &attribution)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace14setAttributionERK7QString(
    QDeclarativePlace *self,
    const QString *attribution) {
  self->setAttribution(*attribution);
}

//  bool QDeclarativePlace::detailsFetched() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDeclarativePlace14detailsFetchedEv(
    const QDeclarativePlace *self) {
  return self->detailsFetched();
}

//  Status QDeclarativePlace::status() const
extern "C" Q_DECL_EXPORT
QDeclarativePlace::Status ritual_ZNK17QDeclarativePlace6statusEv(
    const QDeclarativePlace *self) {
  return self->status();
}

//  void QDeclarativePlace::setStatus(Status status, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace9setStatusENS_6StatusERK7QString(
    QDeclarativePlace *self,
    QDeclarativePlace::Status status,
    const QString *errorString) {
  self->setStatus(status, *errorString);
}

//  void QDeclarativePlace::getDetails()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace10getDetailsEv(QDeclarativePlace *self) {
  self->getDetails();
}

//  void QDeclarativePlace::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace4saveEv(QDeclarativePlace *self) {
  self->save();
}

//  void QDeclarativePlace::remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace6removeEv(QDeclarativePlace *self) {
  self->remove();
}

//  QString QDeclarativePlace::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace11errorStringEv(
    const QDeclarativePlace *self) {
  return new QString(self->errorString());
}

//  QString QDeclarativePlace::primaryPhone() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace12primaryPhoneEv(
    const QDeclarativePlace *self) {
  return new QString(self->primaryPhone());
}

//  QString QDeclarativePlace::primaryFax() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace10primaryFaxEv(
    const QDeclarativePlace *self) {
  return new QString(self->primaryFax());
}

//  QString QDeclarativePlace::primaryEmail() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace12primaryEmailEv(
    const QDeclarativePlace *self) {
  return new QString(self->primaryEmail());
}

//  QUrl QDeclarativePlace::primaryWebsite() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK17QDeclarativePlace14primaryWebsiteEv(
    const QDeclarativePlace *self) {
  return new QUrl(self->primaryWebsite());
}

//  QQmlPropertyMap *QDeclarativePlace::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QQmlPropertyMap *ritual_ZNK17QDeclarativePlace18extendedAttributesEv(
    const QDeclarativePlace *self) {
  return self->extendedAttributes();
}

//  QDeclarativeContactDetails *QDeclarativePlace::contactDetails() const
extern "C" Q_DECL_EXPORT
QDeclarativeContactDetails *ritual_ZNK17QDeclarativePlace14contactDetailsEv(
    const QDeclarativePlace *self) {
  return self->contactDetails();
}

//  Visibility QDeclarativePlace::visibility() const
extern "C" Q_DECL_EXPORT
QDeclarativePlace::Visibility ritual_ZNK17QDeclarativePlace10visibilityEv(
    const QDeclarativePlace *self) {
  return self->visibility();
}

//  void QDeclarativePlace::setVisibility(Visibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace13setVisibilityENS_10VisibilityE(
    QDeclarativePlace *self,
    QDeclarativePlace::Visibility visibility) {
  self->setVisibility(visibility);
}

//  QDeclarativePlace *QDeclarativePlace::favorite() const
extern "C" Q_DECL_EXPORT
QDeclarativePlace *ritual_ZNK17QDeclarativePlace8favoriteEv(
    const QDeclarativePlace *self) {
  return self->favorite();
}

//  void QDeclarativePlace::setFavorite(QDeclarativePlace *favorite)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace11setFavoriteEPS_(
    QDeclarativePlace *self,
    QDeclarativePlace *favorite) {
  self->setFavorite(favorite);
}

//  void QDeclarativePlace::copyFrom(QDeclarativePlace *original)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace8copyFromEPS_(
    QDeclarativePlace *self,
    QDeclarativePlace *original) {
  self->copyFrom(original);
}

//  void QDeclarativePlace::initializeFavorite(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace18initializeFavoriteEP30QDeclarativeGeoServiceProvider(
    QDeclarativePlace *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->initializeFavorite(plugin);
}

//  void QDeclarativePlace::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace8finishedEv(QDeclarativePlace *self) {
  self->finished();
}

//  void QDeclarativePlace::contactsModified(const QString &a0, const
//      QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace16contactsModifiedERK7QStringRK8QVariant(
    QDeclarativePlace *self,
    const QString *a0,
    const QVariant *a1) {
  self->contactsModified(*a0, *a1);
}

//  void QDeclarativePlace::pluginReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace11pluginReadyEv(QDeclarativePlace *self) {
  self->pluginReady();
}

//  void QDeclarativePlace::cleanupDeletedCategories()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace24cleanupDeletedCategoriesEv(
    QDeclarativePlace *self) {
  self->cleanupDeletedCategories();
}

//  void QDeclarativePlace::synchronizeCategories()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace21synchronizeCategoriesEv(
    QDeclarativePlace *self) {
  self->synchronizeCategories();
}

//  void QDeclarativePlace::pullExtendedAttributes()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace22pullExtendedAttributesEv(
    QDeclarativePlace *self) {
  self->pullExtendedAttributes();
}

//  void QDeclarativePlace::synchronizeContacts()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace19synchronizeContactsEv(
    QDeclarativePlace *self) {
  self->synchronizeContacts();
}

//  void QDeclarativePlace::primarySignalsEmission(const QString &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDeclarativePlace22primarySignalsEmissionERK7QString(
    QDeclarativePlace *self,
    const QString *type) {
  self->primarySignalsEmission(*type);
}

//  QString QDeclarativePlace::primaryValue(const QString &contactType) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDeclarativePlace12primaryValueERK7QString(
    const QDeclarativePlace *self,
    const QString *contactType) {
  return new QString(self->primaryValue(*contactType));
}

//  QPlaceManager *QDeclarativePlace::manager()
extern "C" Q_DECL_EXPORT
QPlaceManager *ritual_ZN17QDeclarativePlace7managerEv(
    QDeclarativePlace *self) {
  return self->manager();
}

//  QDeclarativePlace as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativePlace_QQmlParserStatus(
    QDeclarativePlace *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativePlace, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePlace(
    QDeclarativePlace *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePlace *>(self)->take(key, call);
}

//  void QDeclarativePlace::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDeclarativePlace10classBeginEv(
    QDeclarativePlace *self) {
  self->QDeclarativePlace::classBegin();
}

//  void QDeclarativePlace::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDeclarativePlace17componentCompleteEv(
    QDeclarativePlace *self) {
  self->QDeclarativePlace::componentComplete();
}
