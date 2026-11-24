//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacemanagerengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacemanagerengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtLocation/qplacecontentrequest.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacecategory.h>
#include <QtCore/qlocale.h>
#include <QtLocation/qplaceicon.h>
#include <QtCore/qsize.h>
#include <QtCore/qurl.h>
#include <QtLocation/qplacematchrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QPlaceManagerEngine that Python can take functions over in. Every QPlaceManagerEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlaceManagerEngineCall0)(const void *, const QString *, int *);
typedef void * (*CuteQPlaceManagerEngineCall1)(const void *, const QPlaceContentRequest *, int *);
typedef void * (*CuteQPlaceManagerEngineCall2)(const void *, const QPlaceSearchRequest *, int *);
typedef void * (*CuteQPlaceManagerEngineCall3)(const void *, const QPlaceSearchRequest *, int *);
typedef void * (*CuteQPlaceManagerEngineCall4)(const void *, const QPlace *, int *);
typedef void * (*CuteQPlaceManagerEngineCall5)(const void *, const QString *, int *);
typedef void * (*CuteQPlaceManagerEngineCall6)(const void *, const QPlaceCategory *, const QString *, int *);
typedef void * (*CuteQPlaceManagerEngineCall7)(const void *, const QString *, int *);
typedef void * (*CuteQPlaceManagerEngineCall8)(const void *, int *);
typedef QString * (*CuteQPlaceManagerEngineCall9)(const void *, const QString *, int *);
typedef const QPlaceCategory * (*CuteQPlaceManagerEngineCall10)(const void *, const QString *, int *);
typedef const QUrl * (*CuteQPlaceManagerEngineCall11)(const void *, const QPlaceIcon *, const QSize *, int *);
typedef const QPlace * (*CuteQPlaceManagerEngineCall12)(const void *, const QPlace *, int *);
typedef void * (*CuteQPlaceManagerEngineCall13)(const void *, const QPlaceMatchRequest *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceManagerEngineCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceManagerEngineCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerEngineCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerEngineCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerEngineCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerEngineCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerEngineCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceManagerEngine : public QPlaceManagerEngine {
public:
  using QPlaceManagerEngine::QPlaceManagerEngine;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine15getPlaceDetailsERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine15getPlaceContentERK20QPlaceContentRequest")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine6searchERK19QPlaceSearchRequest")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine17searchSuggestionsERK19QPlaceSearchRequest")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine9savePlaceERK6QPlace")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine11removePlaceERK7QString")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine12saveCategoryERK14QPlaceCategoryRK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine14removeCategoryERK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine20initializeCategoriesEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QPlaceManagerEngine16parentCategoryIdERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QPlaceManagerEngine8categoryERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QPlaceManagerEngine16constructIconUrlERK10QPlaceIconRK5QSize")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QPlaceManagerEngine15compatiblePlaceERK6QPlace")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlaceManagerEngine14matchingPlacesERK18QPlaceMatchRequest")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPlaceDetailsReply *QPlaceManagerEngine::getPlaceDetails(const
  //      QString &placeId)
  QPlaceDetailsReply *getPlaceDetails(const QString &placeId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall0 call = reinterpret_cast<CuteQPlaceManagerEngineCall0>(taken[0]);
      void * given = call(this, &placeId, &handled);
      if (handled) return static_cast<QPlaceDetailsReply *>(given);
    }
    return QPlaceManagerEngine::getPlaceDetails(placeId);
  }

  //  QPlaceContentReply *QPlaceManagerEngine::getPlaceContent(const
  //      QPlaceContentRequest &request)
  QPlaceContentReply *getPlaceContent(
      const QPlaceContentRequest &request) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall1 call = reinterpret_cast<CuteQPlaceManagerEngineCall1>(taken[1]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QPlaceContentReply *>(given);
    }
    return QPlaceManagerEngine::getPlaceContent(request);
  }

  //  QPlaceSearchReply *QPlaceManagerEngine::search(const
  //      QPlaceSearchRequest &request)
  QPlaceSearchReply *search(const QPlaceSearchRequest &request) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall2 call = reinterpret_cast<CuteQPlaceManagerEngineCall2>(taken[2]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QPlaceSearchReply *>(given);
    }
    return QPlaceManagerEngine::search(request);
  }

  //  QPlaceSearchSuggestionReply
  //      *QPlaceManagerEngine::searchSuggestions(const QPlaceSearchRequest
  //      &request)
  QPlaceSearchSuggestionReply *searchSuggestions(
      const QPlaceSearchRequest &request) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall3 call = reinterpret_cast<CuteQPlaceManagerEngineCall3>(taken[3]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QPlaceSearchSuggestionReply *>(given);
    }
    return QPlaceManagerEngine::searchSuggestions(request);
  }

  //  QPlaceIdReply *QPlaceManagerEngine::savePlace(const QPlace &place)
  QPlaceIdReply *savePlace(const QPlace &place) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall4 call = reinterpret_cast<CuteQPlaceManagerEngineCall4>(taken[4]);
      void * given = call(this, &place, &handled);
      if (handled) return static_cast<QPlaceIdReply *>(given);
    }
    return QPlaceManagerEngine::savePlace(place);
  }

  //  QPlaceIdReply *QPlaceManagerEngine::removePlace(const QString
  //      &placeId)
  QPlaceIdReply *removePlace(const QString &placeId) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall5 call = reinterpret_cast<CuteQPlaceManagerEngineCall5>(taken[5]);
      void * given = call(this, &placeId, &handled);
      if (handled) return static_cast<QPlaceIdReply *>(given);
    }
    return QPlaceManagerEngine::removePlace(placeId);
  }

  //  QPlaceIdReply *QPlaceManagerEngine::saveCategory(const QPlaceCategory
  //      &category, const QString &parentId)
  QPlaceIdReply *saveCategory(
      const QPlaceCategory &category,
      const QString &parentId) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall6 call = reinterpret_cast<CuteQPlaceManagerEngineCall6>(taken[6]);
      void * given = call(this, &category, &parentId, &handled);
      if (handled) return static_cast<QPlaceIdReply *>(given);
    }
    return QPlaceManagerEngine::saveCategory(category, parentId);
  }

  //  QPlaceIdReply *QPlaceManagerEngine::removeCategory(const QString
  //      &categoryId)
  QPlaceIdReply *removeCategory(const QString &categoryId) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall7 call = reinterpret_cast<CuteQPlaceManagerEngineCall7>(taken[7]);
      void * given = call(this, &categoryId, &handled);
      if (handled) return static_cast<QPlaceIdReply *>(given);
    }
    return QPlaceManagerEngine::removeCategory(categoryId);
  }

  //  QPlaceReply *QPlaceManagerEngine::initializeCategories()
  QPlaceReply *initializeCategories() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall8 call = reinterpret_cast<CuteQPlaceManagerEngineCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlaceReply *>(given);
    }
    return QPlaceManagerEngine::initializeCategories();
  }

  //  QString QPlaceManagerEngine::parentCategoryId(const QString
  //      &categoryId) const
  QString parentCategoryId(const QString &categoryId) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall9 call = reinterpret_cast<CuteQPlaceManagerEngineCall9>(taken[9]);
      QString * given = call(this, &categoryId, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlaceManagerEngine::parentCategoryId(categoryId);
  }

  //  QPlaceCategory QPlaceManagerEngine::category(const QString
  //      &categoryId) const
  QPlaceCategory category(const QString &categoryId) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall10 call = reinterpret_cast<CuteQPlaceManagerEngineCall10>(taken[10]);
      const QPlaceCategory * given = call(this, &categoryId, &handled);
      if (handled && given) return *given;
    }
    return QPlaceManagerEngine::category(categoryId);
  }

  //  QUrl QPlaceManagerEngine::constructIconUrl(const QPlaceIcon &icon,
  //      const QSize &size) const
  QUrl constructIconUrl(
      const QPlaceIcon &icon,
      const QSize &size) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall11 call = reinterpret_cast<CuteQPlaceManagerEngineCall11>(taken[11]);
      const QUrl * given = call(this, &icon, &size, &handled);
      if (handled && given) return *given;
    }
    return QPlaceManagerEngine::constructIconUrl(icon, size);
  }

  //  QPlace QPlaceManagerEngine::compatiblePlace(const QPlace &original)
  //      const
  QPlace compatiblePlace(const QPlace &original) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall12 call = reinterpret_cast<CuteQPlaceManagerEngineCall12>(taken[12]);
      const QPlace * given = call(this, &original, &handled);
      if (handled && given) return *given;
    }
    return QPlaceManagerEngine::compatiblePlace(original);
  }

  //  QPlaceMatchReply *QPlaceManagerEngine::matchingPlaces(const
  //      QPlaceMatchRequest &request)
  QPlaceMatchReply *matchingPlaces(
      const QPlaceMatchRequest &request) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall13 call = reinterpret_cast<CuteQPlaceManagerEngineCall13>(taken[13]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QPlaceMatchReply *>(given);
    }
    return QPlaceManagerEngine::matchingPlaces(request);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall14 call = reinterpret_cast<CuteQPlaceManagerEngineCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall15 call = reinterpret_cast<CuteQPlaceManagerEngineCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall16 call = reinterpret_cast<CuteQPlaceManagerEngineCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall17 call = reinterpret_cast<CuteQPlaceManagerEngineCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall18 call = reinterpret_cast<CuteQPlaceManagerEngineCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall19 call = reinterpret_cast<CuteQPlaceManagerEngineCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlaceManagerEngineCall20 call = reinterpret_cast<CuteQPlaceManagerEngineCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceManagerEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QPlaceManagerEngine10metaObjectEv(
    const QPlaceManagerEngine *self) {
  return self->metaObject();
}

//  QString QPlaceManagerEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QPlaceManagerEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceManagerEngine::tr(s, c, n));
}

//  QPlaceManagerEngine::QPlaceManagerEngine(const QVariantMap &parameters,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QPlaceManagerEngine *ritual_ZN19QPlaceManagerEngineC1ERK4QMapI7QString8QVariantEP7QObject(
    const QMap<QString, QVariant> *parameters,
    QObject *parent) {
  return new CuteQPlaceManagerEngine(*parameters, parent);
}

//  QPlaceManagerEngine::~QPlaceManagerEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceManagerEngineD1Ev(QPlaceManagerEngine *self) {
  delete self;
}

//  QString QPlaceManagerEngine::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QPlaceManagerEngine11managerNameEv(
    const QPlaceManagerEngine *self) {
  return new QString(self->managerName());
}

//  int QPlaceManagerEngine::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QPlaceManagerEngine14managerVersionEv(
    const QPlaceManagerEngine *self) {
  return self->managerVersion();
}

//  QPlaceDetailsReply *QPlaceManagerEngine::getPlaceDetails(const QString
//      &placeId)
extern "C" Q_DECL_EXPORT
QPlaceDetailsReply *ritual_ZN19QPlaceManagerEngine15getPlaceDetailsERK7QString(
    QPlaceManagerEngine *self,
    const QString *placeId) {
  return self->getPlaceDetails(*placeId);
}

//  QPlaceContentReply *QPlaceManagerEngine::getPlaceContent(const
//      QPlaceContentRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceContentReply *ritual_ZN19QPlaceManagerEngine15getPlaceContentERK20QPlaceContentRequest(
    QPlaceManagerEngine *self,
    const QPlaceContentRequest *request) {
  return self->getPlaceContent(*request);
}

//  QPlaceSearchReply *QPlaceManagerEngine::search(const QPlaceSearchRequest
//      &request)
extern "C" Q_DECL_EXPORT
QPlaceSearchReply *ritual_ZN19QPlaceManagerEngine6searchERK19QPlaceSearchRequest(
    QPlaceManagerEngine *self,
    const QPlaceSearchRequest *request) {
  return self->search(*request);
}

//  QPlaceSearchSuggestionReply *QPlaceManagerEngine::searchSuggestions(const
//      QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceSearchSuggestionReply *ritual_ZN19QPlaceManagerEngine17searchSuggestionsERK19QPlaceSearchRequest(
    QPlaceManagerEngine *self,
    const QPlaceSearchRequest *request) {
  return self->searchSuggestions(*request);
}

//  QPlaceIdReply *QPlaceManagerEngine::savePlace(const QPlace &place)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN19QPlaceManagerEngine9savePlaceERK6QPlace(
    QPlaceManagerEngine *self,
    const QPlace *place) {
  return self->savePlace(*place);
}

//  QPlaceIdReply *QPlaceManagerEngine::removePlace(const QString &placeId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN19QPlaceManagerEngine11removePlaceERK7QString(
    QPlaceManagerEngine *self,
    const QString *placeId) {
  return self->removePlace(*placeId);
}

//  QPlaceIdReply *QPlaceManagerEngine::saveCategory(const QPlaceCategory
//      &category, const QString &parentId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN19QPlaceManagerEngine12saveCategoryERK14QPlaceCategoryRK7QString(
    QPlaceManagerEngine *self,
    const QPlaceCategory *category,
    const QString *parentId) {
  return self->saveCategory(*category, *parentId);
}

//  QPlaceIdReply *QPlaceManagerEngine::removeCategory(const QString
//      &categoryId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN19QPlaceManagerEngine14removeCategoryERK7QString(
    QPlaceManagerEngine *self,
    const QString *categoryId) {
  return self->removeCategory(*categoryId);
}

//  QPlaceReply *QPlaceManagerEngine::initializeCategories()
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN19QPlaceManagerEngine20initializeCategoriesEv(
    QPlaceManagerEngine *self) {
  return self->initializeCategories();
}

//  QString QPlaceManagerEngine::parentCategoryId(const QString &categoryId)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QPlaceManagerEngine16parentCategoryIdERK7QString(
    const QPlaceManagerEngine *self,
    const QString *categoryId) {
  return new QString(self->parentCategoryId(*categoryId));
}

//  QStringList QPlaceManagerEngine::childCategoryIds(const QString
//      &categoryId) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QPlaceManagerEngine16childCategoryIdsERK7QString(
    const QPlaceManagerEngine *self,
    const QString *categoryId) {
  return new QList<QString>(self->childCategoryIds(*categoryId));
}

//  QPlaceCategory QPlaceManagerEngine::category(const QString &categoryId)
//      const
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZNK19QPlaceManagerEngine8categoryERK7QString(
    const QPlaceManagerEngine *self,
    const QString *categoryId) {
  return new QPlaceCategory(self->category(*categoryId));
}

//  QList<QPlaceCategory> QPlaceManagerEngine::childCategories(const QString
//      &parentId) const
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_ZNK19QPlaceManagerEngine15childCategoriesERK7QString(
    const QPlaceManagerEngine *self,
    const QString *parentId) {
  return new QList<QPlaceCategory>(self->childCategories(*parentId));
}

//  QList<QLocale> QPlaceManagerEngine::locales() const
extern "C" Q_DECL_EXPORT
QList<QLocale> *ritual_ZNK19QPlaceManagerEngine7localesEv(
    const QPlaceManagerEngine *self) {
  return new QList<QLocale>(self->locales());
}

//  void QPlaceManagerEngine::setLocales(const QList<QLocale> &locales)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceManagerEngine10setLocalesERK5QListI7QLocaleE(
    QPlaceManagerEngine *self,
    const QList<QLocale> *locales) {
  self->setLocales(*locales);
}

//  QUrl QPlaceManagerEngine::constructIconUrl(const QPlaceIcon &icon, const
//      QSize &size) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QPlaceManagerEngine16constructIconUrlERK10QPlaceIconRK5QSize(
    const QPlaceManagerEngine *self,
    const QPlaceIcon *icon,
    const QSize *size) {
  return new QUrl(self->constructIconUrl(*icon, *size));
}

//  QPlace QPlaceManagerEngine::compatiblePlace(const QPlace &original) const
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZNK19QPlaceManagerEngine15compatiblePlaceERK6QPlace(
    const QPlaceManagerEngine *self,
    const QPlace *original) {
  return new QPlace(self->compatiblePlace(*original));
}

//  QPlaceMatchReply *QPlaceManagerEngine::matchingPlaces(const
//      QPlaceMatchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceMatchReply *ritual_ZN19QPlaceManagerEngine14matchingPlacesERK18QPlaceMatchRequest(
    QPlaceManagerEngine *self,
    const QPlaceMatchRequest *request) {
  return self->matchingPlaces(*request);
}

//  QPlaceManager *QPlaceManagerEngine::manager() const
extern "C" Q_DECL_EXPORT
QPlaceManager *ritual_ZNK19QPlaceManagerEngine7managerEv(
    const QPlaceManagerEngine *self) {
  return self->manager();
}

//  void QPlaceManagerEngine::setManagerName(const QString &managerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceManagerEngine14setManagerNameERK7QString(
    QPlaceManagerEngine *self,
    const QString *managerName) {
  self->setManagerName(*managerName);
}

//  void QPlaceManagerEngine::setManagerVersion(int managerVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlaceManagerEngine17setManagerVersionEi(
    QPlaceManagerEngine *self,
    int managerVersion) {
  self->setManagerVersion(managerVersion);
}

//  a Python function taken by a CuteQPlaceManagerEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceManagerEngine(
    QPlaceManagerEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceManagerEngine *>(self)->take(key, call);
}

//  QPlaceDetailsReply *QPlaceManagerEngine::getPlaceDetails(const QString
//      &placeId)
extern "C" Q_DECL_EXPORT
QPlaceDetailsReply *ritual_own_ZN19QPlaceManagerEngine15getPlaceDetailsERK7QString(
    QPlaceManagerEngine *self,
    const QString *placeId) {
  return self->QPlaceManagerEngine::getPlaceDetails(*placeId);
}

//  QPlaceContentReply *QPlaceManagerEngine::getPlaceContent(const
//      QPlaceContentRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceContentReply *ritual_own_ZN19QPlaceManagerEngine15getPlaceContentERK20QPlaceContentRequest(
    QPlaceManagerEngine *self,
    const QPlaceContentRequest *request) {
  return self->QPlaceManagerEngine::getPlaceContent(*request);
}

//  QPlaceSearchReply *QPlaceManagerEngine::search(const QPlaceSearchRequest
//      &request)
extern "C" Q_DECL_EXPORT
QPlaceSearchReply *ritual_own_ZN19QPlaceManagerEngine6searchERK19QPlaceSearchRequest(
    QPlaceManagerEngine *self,
    const QPlaceSearchRequest *request) {
  return self->QPlaceManagerEngine::search(*request);
}

//  QPlaceSearchSuggestionReply *QPlaceManagerEngine::searchSuggestions(const
//      QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceSearchSuggestionReply *ritual_own_ZN19QPlaceManagerEngine17searchSuggestionsERK19QPlaceSearchRequest(
    QPlaceManagerEngine *self,
    const QPlaceSearchRequest *request) {
  return self->QPlaceManagerEngine::searchSuggestions(*request);
}

//  QPlaceIdReply *QPlaceManagerEngine::savePlace(const QPlace &place)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_own_ZN19QPlaceManagerEngine9savePlaceERK6QPlace(
    QPlaceManagerEngine *self,
    const QPlace *place) {
  return self->QPlaceManagerEngine::savePlace(*place);
}

//  QPlaceIdReply *QPlaceManagerEngine::removePlace(const QString &placeId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_own_ZN19QPlaceManagerEngine11removePlaceERK7QString(
    QPlaceManagerEngine *self,
    const QString *placeId) {
  return self->QPlaceManagerEngine::removePlace(*placeId);
}

//  QPlaceIdReply *QPlaceManagerEngine::saveCategory(const QPlaceCategory
//      &category, const QString &parentId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_own_ZN19QPlaceManagerEngine12saveCategoryERK14QPlaceCategoryRK7QString(
    QPlaceManagerEngine *self,
    const QPlaceCategory *category,
    const QString *parentId) {
  return self->QPlaceManagerEngine::saveCategory(*category, *parentId);
}

//  QPlaceIdReply *QPlaceManagerEngine::removeCategory(const QString
//      &categoryId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_own_ZN19QPlaceManagerEngine14removeCategoryERK7QString(
    QPlaceManagerEngine *self,
    const QString *categoryId) {
  return self->QPlaceManagerEngine::removeCategory(*categoryId);
}

//  QPlaceReply *QPlaceManagerEngine::initializeCategories()
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_own_ZN19QPlaceManagerEngine20initializeCategoriesEv(
    QPlaceManagerEngine *self) {
  return self->QPlaceManagerEngine::initializeCategories();
}

//  QString QPlaceManagerEngine::parentCategoryId(const QString &categoryId)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QPlaceManagerEngine16parentCategoryIdERK7QString(
    const QPlaceManagerEngine *self,
    const QString *categoryId) {
  return new QString(
      self->QPlaceManagerEngine::parentCategoryId(
          *categoryId));
}

//  QPlaceCategory QPlaceManagerEngine::category(const QString &categoryId)
//      const
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_own_ZNK19QPlaceManagerEngine8categoryERK7QString(
    const QPlaceManagerEngine *self,
    const QString *categoryId) {
  return new QPlaceCategory(
      self->QPlaceManagerEngine::category(
          *categoryId));
}

//  QUrl QPlaceManagerEngine::constructIconUrl(const QPlaceIcon &icon, const
//      QSize &size) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK19QPlaceManagerEngine16constructIconUrlERK10QPlaceIconRK5QSize(
    const QPlaceManagerEngine *self,
    const QPlaceIcon *icon,
    const QSize *size) {
  return new QUrl(self->QPlaceManagerEngine::constructIconUrl(*icon, *size));
}

//  QPlace QPlaceManagerEngine::compatiblePlace(const QPlace &original) const
extern "C" Q_DECL_EXPORT
QPlace *ritual_own_ZNK19QPlaceManagerEngine15compatiblePlaceERK6QPlace(
    const QPlaceManagerEngine *self,
    const QPlace *original) {
  return new QPlace(self->QPlaceManagerEngine::compatiblePlace(*original));
}

//  QPlaceMatchReply *QPlaceManagerEngine::matchingPlaces(const
//      QPlaceMatchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceMatchReply *ritual_own_ZN19QPlaceManagerEngine14matchingPlacesERK18QPlaceMatchRequest(
    QPlaceManagerEngine *self,
    const QPlaceMatchRequest *request) {
  return self->QPlaceManagerEngine::matchingPlaces(*request);
}
