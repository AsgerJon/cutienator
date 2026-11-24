//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativecategory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativecategory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtLocation/qplacecategory.h>
#include <QtLocation/qplaceicon.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDeclarativeCategory that Python can take functions over in. Every QDeclarativeCategory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeCategoryCall0)(const void *, int *);
typedef void (*CuteQDeclarativeCategoryCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeCategoryCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeCategoryCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCategoryCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCategoryCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCategoryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCategoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeCategoryCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeCategory : public QDeclarativeCategory {
public:
  using QDeclarativeCategory::QDeclarativeCategory;
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

  //  void QDeclarativeCategory::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeCategoryCall0 call = reinterpret_cast<CuteQDeclarativeCategoryCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCategory::classBegin();
  }

  //  void QDeclarativeCategory::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeCategoryCall1 call = reinterpret_cast<CuteQDeclarativeCategoryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeCategory::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeCategoryCall2 call = reinterpret_cast<CuteQDeclarativeCategoryCall2>(taken[2]);
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
      CuteQDeclarativeCategoryCall3 call = reinterpret_cast<CuteQDeclarativeCategoryCall3>(taken[3]);
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
      CuteQDeclarativeCategoryCall4 call = reinterpret_cast<CuteQDeclarativeCategoryCall4>(taken[4]);
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
      CuteQDeclarativeCategoryCall5 call = reinterpret_cast<CuteQDeclarativeCategoryCall5>(taken[5]);
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
      CuteQDeclarativeCategoryCall6 call = reinterpret_cast<CuteQDeclarativeCategoryCall6>(taken[6]);
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
      CuteQDeclarativeCategoryCall7 call = reinterpret_cast<CuteQDeclarativeCategoryCall7>(taken[7]);
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
      CuteQDeclarativeCategoryCall8 call = reinterpret_cast<CuteQDeclarativeCategoryCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeCategory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QDeclarativeCategory10metaObjectEv(
    const QDeclarativeCategory *self) {
  return self->metaObject();
}

//  QString QDeclarativeCategory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDeclarativeCategory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeCategory::tr(s, c, n));
}

//  QDeclarativeCategory::QDeclarativeCategory(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeCategory *ritual_ZN20QDeclarativeCategoryC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeCategory(parent);
}

//  QDeclarativeCategory::QDeclarativeCategory(const QPlaceCategory
//      &category, QDeclarativeGeoServiceProvider *plugin, QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeCategory *ritual_ZN20QDeclarativeCategoryC1ERK14QPlaceCategoryP30QDeclarativeGeoServiceProviderP7QObject(
    const QPlaceCategory *category,
    QDeclarativeGeoServiceProvider *plugin,
    QObject *parent) {
  return new CuteQDeclarativeCategory(*category, plugin, parent);
}

//  QDeclarativeCategory::~QDeclarativeCategory()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategoryD1Ev(QDeclarativeCategory *self) {
  delete self;
}

//  void QDeclarativeCategory::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory10classBeginEv(
    QDeclarativeCategory *self) {
  self->classBegin();
}

//  void QDeclarativeCategory::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory17componentCompleteEv(
    QDeclarativeCategory *self) {
  self->componentComplete();
}

//  void QDeclarativeCategory::setPlugin(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory9setPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeCategory *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setPlugin(plugin);
}

//  QDeclarativeGeoServiceProvider *QDeclarativeCategory::plugin() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK20QDeclarativeCategory6pluginEv(
    const QDeclarativeCategory *self) {
  return self->plugin();
}

//  QPlaceCategory QDeclarativeCategory::category()
extern "C" Q_DECL_EXPORT
QPlaceCategory *ritual_ZN20QDeclarativeCategory8categoryEv(
    QDeclarativeCategory *self) {
  return new QPlaceCategory(self->category());
}

//  void QDeclarativeCategory::setCategory(const QPlaceCategory &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory11setCategoryERK14QPlaceCategory(
    QDeclarativeCategory *self,
    const QPlaceCategory *category) {
  self->setCategory(*category);
}

//  QString QDeclarativeCategory::categoryId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDeclarativeCategory10categoryIdEv(
    const QDeclarativeCategory *self) {
  return new QString(self->categoryId());
}

//  void QDeclarativeCategory::setCategoryId(const QString &catID)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory13setCategoryIdERK7QString(
    QDeclarativeCategory *self,
    const QString *catID) {
  self->setCategoryId(*catID);
}

//  QString QDeclarativeCategory::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDeclarativeCategory4nameEv(
    const QDeclarativeCategory *self) {
  return new QString(self->name());
}

//  void QDeclarativeCategory::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory7setNameERK7QString(
    QDeclarativeCategory *self,
    const QString *name) {
  self->setName(*name);
}

//  Visibility QDeclarativeCategory::visibility() const
extern "C" Q_DECL_EXPORT
QDeclarativeCategory::Visibility ritual_ZNK20QDeclarativeCategory10visibilityEv(
    const QDeclarativeCategory *self) {
  return self->visibility();
}

//  void QDeclarativeCategory::setVisibility(Visibility visibility)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory13setVisibilityENS_10VisibilityE(
    QDeclarativeCategory *self,
    QDeclarativeCategory::Visibility visibility) {
  self->setVisibility(visibility);
}

//  QPlaceIcon QDeclarativeCategory::icon() const
extern "C" Q_DECL_EXPORT
QPlaceIcon *ritual_ZNK20QDeclarativeCategory4iconEv(
    const QDeclarativeCategory *self) {
  return new QPlaceIcon(self->icon());
}

//  void QDeclarativeCategory::setIcon(const QPlaceIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory7setIconERK10QPlaceIcon(
    QDeclarativeCategory *self,
    const QPlaceIcon *icon) {
  self->setIcon(*icon);
}

//  QString QDeclarativeCategory::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QDeclarativeCategory11errorStringEv(
    const QDeclarativeCategory *self) {
  return new QString(self->errorString());
}

//  Status QDeclarativeCategory::status() const
extern "C" Q_DECL_EXPORT
QDeclarativeCategory::Status ritual_ZNK20QDeclarativeCategory6statusEv(
    const QDeclarativeCategory *self) {
  return self->status();
}

//  void QDeclarativeCategory::setStatus(Status status, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory9setStatusENS_6StatusERK7QString(
    QDeclarativeCategory *self,
    QDeclarativeCategory::Status status,
    const QString *errorString) {
  self->setStatus(status, *errorString);
}

//  void QDeclarativeCategory::save(const QString &parentId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory4saveERK7QString(
    QDeclarativeCategory *self,
    const QString *parentId) {
  self->save(*parentId);
}

//  void QDeclarativeCategory::remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory6removeEv(QDeclarativeCategory *self) {
  self->remove();
}

//  void QDeclarativeCategory::replyFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory13replyFinishedEv(
    QDeclarativeCategory *self) {
  self->replyFinished();
}

//  void QDeclarativeCategory::pluginReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDeclarativeCategory11pluginReadyEv(
    QDeclarativeCategory *self) {
  self->pluginReady();
}

//  QPlaceManager *QDeclarativeCategory::manager()
extern "C" Q_DECL_EXPORT
QPlaceManager *ritual_ZN20QDeclarativeCategory7managerEv(
    QDeclarativeCategory *self) {
  return self->manager();
}

//  QDeclarativeCategory as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeCategory_QQmlParserStatus(
    QDeclarativeCategory *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativeCategory, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeCategory(
    QDeclarativeCategory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeCategory *>(self)->take(key, call);
}

//  void QDeclarativeCategory::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDeclarativeCategory10classBeginEv(
    QDeclarativeCategory *self) {
  self->QDeclarativeCategory::classBegin();
}

//  void QDeclarativeCategory::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDeclarativeCategory17componentCompleteEv(
    QDeclarativeCategory *self) {
  self->QDeclarativeCategory::componentComplete();
}
