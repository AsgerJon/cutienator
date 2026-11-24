//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplacemanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplacemanager.h>
#include <QtCore/qstring.h>
#include <QtLocation/qplacecontentrequest.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacecategory.h>
#include <QtCore/qlocale.h>
#include <QtLocation/qplacematchrequest.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlaceManager that Python can take functions over in. Every QPlaceManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlaceManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlaceManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlaceManager : public QPlaceManager {
public:
  using QPlaceManager::QPlaceManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlaceManagerCall0 call = reinterpret_cast<CuteQPlaceManagerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlaceManagerCall1 call = reinterpret_cast<CuteQPlaceManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlaceManagerCall2 call = reinterpret_cast<CuteQPlaceManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlaceManagerCall3 call = reinterpret_cast<CuteQPlaceManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlaceManagerCall4 call = reinterpret_cast<CuteQPlaceManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlaceManagerCall5 call = reinterpret_cast<CuteQPlaceManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlaceManagerCall6 call = reinterpret_cast<CuteQPlaceManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlaceManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPlaceManager10metaObjectEv(
    const QPlaceManager *self) {
  return self->metaObject();
}

//  QString QPlaceManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPlaceManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlaceManager::tr(s, c, n));
}

//  QPlaceManager::~QPlaceManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceManagerD1Ev(QPlaceManager *self) {
  delete self;
}

//  QString QPlaceManager::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlaceManager11managerNameEv(
    const QPlaceManager *self) {
  return new QString(self->managerName());
}

//  int QPlaceManager::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPlaceManager14managerVersionEv(const QPlaceManager *self) {
  return self->managerVersion();
}

//  QPlaceDetailsReply *QPlaceManager::getPlaceDetails(const QString
//      &placeId) const
extern "C" Q_DECL_EXPORT
QPlaceDetailsReply *ritual_ZNK13QPlaceManager15getPlaceDetailsERK7QString(
    const QPlaceManager *self,
    const QString *placeId) {
  return self->getPlaceDetails(*placeId);
}

//  QPlaceContentReply *QPlaceManager::getPlaceContent(const
//      QPlaceContentRequest &request) const
extern "C" Q_DECL_EXPORT
QPlaceContentReply *ritual_ZNK13QPlaceManager15getPlaceContentERK20QPlaceContentRequest(
    const QPlaceManager *self,
    const QPlaceContentRequest *request) {
  return self->getPlaceContent(*request);
}

//  QPlaceSearchReply *QPlaceManager::search(const QPlaceSearchRequest
//      &query) const
extern "C" Q_DECL_EXPORT
QPlaceSearchReply *ritual_ZNK13QPlaceManager6searchERK19QPlaceSearchRequest(
    const QPlaceManager *self,
    const QPlaceSearchRequest *query) {
  return self->search(*query);
}

//  QPlaceSearchSuggestionReply *QPlaceManager::searchSuggestions(const
//      QPlaceSearchRequest &request) const
extern "C" Q_DECL_EXPORT
QPlaceSearchSuggestionReply *ritual_ZNK13QPlaceManager17searchSuggestionsERK19QPlaceSearchRequest(
    const QPlaceManager *self,
    const QPlaceSearchRequest *request) {
  return self->searchSuggestions(*request);
}

//  QPlaceIdReply *QPlaceManager::savePlace(const QPlace &place)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN13QPlaceManager9savePlaceERK6QPlace(
    QPlaceManager *self,
    const QPlace *place) {
  return self->savePlace(*place);
}

//  QPlaceIdReply *QPlaceManager::removePlace(const QString &placeId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN13QPlaceManager11removePlaceERK7QString(
    QPlaceManager *self,
    const QString *placeId) {
  return self->removePlace(*placeId);
}

//  QPlaceIdReply *QPlaceManager::saveCategory(const QPlaceCategory
//      &category, const QString &parentId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN13QPlaceManager12saveCategoryERK14QPlaceCategoryRK7QString(
    QPlaceManager *self,
    const QPlaceCategory *category,
    const QString *parentId) {
  return self->saveCategory(*category, *parentId);
}

//  QPlaceIdReply *QPlaceManager::removeCategory(const QString &categoryId)
extern "C" Q_DECL_EXPORT
QPlaceIdReply *ritual_ZN13QPlaceManager14removeCategoryERK7QString(
    QPlaceManager *self,
    const QString *categoryId) {
  return self->removeCategory(*categoryId);
}

//  QPlaceReply *QPlaceManager::initializeCategories()
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN13QPlaceManager20initializeCategoriesEv(
    QPlaceManager *self) {
  return self->initializeCategories();
}

//  QString QPlaceManager::parentCategoryId(const QString &categoryId) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QPlaceManager16parentCategoryIdERK7QString(
    const QPlaceManager *self,
    const QString *categoryId) {
  return new QString(self->parentCategoryId(*categoryId));
}

//  QStringList QPlaceManager::childCategoryIds(const QString &parentId)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QPlaceManager16childCategoryIdsERK7QString(
    const QPlaceManager *self,
    const QString *parentId) {
  return new QList<QString>(self->childCategoryIds(*parentId));
}

//  QPlaceCategory QPlaceManager::category(const QString &categoryId) const
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZNK13QPlaceManager8categoryERK7QString(
    const QPlaceManager *self,
    const QString *categoryId) {
  return new QPlaceCategory(self->category(*categoryId));
}

//  QList<QPlaceCategory> QPlaceManager::childCategories(const QString
//      &parentId) const
extern "C" Q_DECL_EXPORT
QList<QPlaceCategory> *ritual_ZNK13QPlaceManager15childCategoriesERK7QString(
    const QPlaceManager *self,
    const QString *parentId) {
  return new QList<QPlaceCategory>(self->childCategories(*parentId));
}

//  QList<QLocale> QPlaceManager::locales() const
extern "C" Q_DECL_EXPORT
QList<QLocale> *ritual_ZNK13QPlaceManager7localesEv(
    const QPlaceManager *self) {
  return new QList<QLocale>(self->locales());
}

//  void QPlaceManager::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceManager9setLocaleERK7QLocale(
    QPlaceManager *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void QPlaceManager::setLocales(const QList<QLocale> &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceManager10setLocalesERK5QListI7QLocaleE(
    QPlaceManager *self,
    const QList<QLocale> *locale) {
  self->setLocales(*locale);
}

//  QPlace QPlaceManager::compatiblePlace(const QPlace &place) const
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZNK13QPlaceManager15compatiblePlaceERK6QPlace(
    const QPlaceManager *self,
    const QPlace *place) {
  return new QPlace(self->compatiblePlace(*place));
}

//  QPlaceMatchReply *QPlaceManager::matchingPlaces(const QPlaceMatchRequest
//      &request) const
extern "C" Q_DECL_EXPORT
QPlaceMatchReply *ritual_ZNK13QPlaceManager14matchingPlacesERK18QPlaceMatchRequest(
    const QPlaceManager *self,
    const QPlaceMatchRequest *request) {
  return self->matchingPlaces(*request);
}

//  QPlaceManager::QPlaceManager(QPlaceManagerEngine *engine, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QPlaceManager *ritual_ZN13QPlaceManagerC1EP19QPlaceManagerEngineP7QObject(
    QPlaceManagerEngine *engine,
    QObject *parent) {
  return new CuteQPlaceManager(engine, parent);
}

//  a Python function taken by a CuteQPlaceManager, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlaceManager(
    QPlaceManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlaceManager *>(self)->take(key, call);
}
