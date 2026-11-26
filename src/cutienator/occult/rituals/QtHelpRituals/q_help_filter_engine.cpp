//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpfilterengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelpfilterengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qversionnumber.h>
#include <QtHelp/qhelpfilterdata.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QMap>
#include <QtCore/QString>

//  A QHelpFilterEngine that Python can take functions over in. Every QHelpFilterEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpFilterEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpFilterEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpFilterEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpFilterEngine : public QHelpFilterEngine {
public:
  using QHelpFilterEngine::QHelpFilterEngine;
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
      CuteQHelpFilterEngineCall0 call = reinterpret_cast<CuteQHelpFilterEngineCall0>(taken[0]);
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
      CuteQHelpFilterEngineCall1 call = reinterpret_cast<CuteQHelpFilterEngineCall1>(taken[1]);
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
      CuteQHelpFilterEngineCall2 call = reinterpret_cast<CuteQHelpFilterEngineCall2>(taken[2]);
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
      CuteQHelpFilterEngineCall3 call = reinterpret_cast<CuteQHelpFilterEngineCall3>(taken[3]);
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
      CuteQHelpFilterEngineCall4 call = reinterpret_cast<CuteQHelpFilterEngineCall4>(taken[4]);
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
      CuteQHelpFilterEngineCall5 call = reinterpret_cast<CuteQHelpFilterEngineCall5>(taken[5]);
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
      CuteQHelpFilterEngineCall6 call = reinterpret_cast<CuteQHelpFilterEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpFilterEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QHelpFilterEngine10metaObjectEv(
    const QHelpFilterEngine *self) {
  return self->metaObject();
}

//  void *QHelpFilterEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QHelpFilterEngine11qt_metacastEPKc(
    QHelpFilterEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHelpFilterEngine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QHelpFilterEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QHelpFilterEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHelpFilterEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QHelpFilterEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpFilterEngine::tr(s, c, n));
}

//  QMap<QString, QString> QHelpFilterEngine::namespaceToComponent() const
extern "C" Q_DECL_EXPORT
QMap<QString, QString> *ritual_ZNK17QHelpFilterEngine20namespaceToComponentEv(
    const QHelpFilterEngine *self) {
  return new QMap<QString, QString>(self->namespaceToComponent());
}

//  QMap<QString, QVersionNumber> QHelpFilterEngine::namespaceToVersion()
//      const
extern "C" Q_DECL_EXPORT
QMap<QString, QVersionNumber> *ritual_ZNK17QHelpFilterEngine18namespaceToVersionEv(
    const QHelpFilterEngine *self) {
  return new QMap<QString, QVersionNumber>(self->namespaceToVersion());
}

//  QStringList QHelpFilterEngine::filters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QHelpFilterEngine7filtersEv(
    const QHelpFilterEngine *self) {
  return new QList<QString>(self->filters());
}

//  QString QHelpFilterEngine::activeFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHelpFilterEngine12activeFilterEv(
    const QHelpFilterEngine *self) {
  return new QString(self->activeFilter());
}

//  bool QHelpFilterEngine::setActiveFilter(const QString &filterName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHelpFilterEngine15setActiveFilterERK7QString(
    QHelpFilterEngine *self,
    const QString *filterName) {
  return self->setActiveFilter(*filterName);
}

//  QStringList QHelpFilterEngine::availableComponents() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QHelpFilterEngine19availableComponentsEv(
    const QHelpFilterEngine *self) {
  return new QList<QString>(self->availableComponents());
}

//  QList<QVersionNumber> QHelpFilterEngine::availableVersions() const
extern "C" Q_DECL_EXPORT
QList<QVersionNumber> *ritual_ZNK17QHelpFilterEngine17availableVersionsEv(
    const QHelpFilterEngine *self) {
  return new QList<QVersionNumber>(self->availableVersions());
}

//  QHelpFilterData QHelpFilterEngine::filterData(const QString &filterName)
//      const
extern "C" Q_DECL_EXPORT
QHelpFilterData *ritual_ZNK17QHelpFilterEngine10filterDataERK7QString(
    const QHelpFilterEngine *self,
    const QString *filterName) {
  return new QHelpFilterData(self->filterData(*filterName));
}

//  bool QHelpFilterEngine::setFilterData(const QString &filterName, const
//      QHelpFilterData &filterData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHelpFilterEngine13setFilterDataERK7QStringRK15QHelpFilterData(
    QHelpFilterEngine *self,
    const QString *filterName,
    const QHelpFilterData *filterData) {
  return self->setFilterData(*filterName, *filterData);
}

//  bool QHelpFilterEngine::removeFilter(const QString &filterName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QHelpFilterEngine12removeFilterERK7QString(
    QHelpFilterEngine *self,
    const QString *filterName) {
  return self->removeFilter(*filterName);
}

//  QStringList QHelpFilterEngine::namespacesForFilter(const QString
//      &filterName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QHelpFilterEngine19namespacesForFilterERK7QString(
    const QHelpFilterEngine *self,
    const QString *filterName) {
  return new QList<QString>(self->namespacesForFilter(*filterName));
}

//  QStringList QHelpFilterEngine::indices() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QHelpFilterEngine7indicesEv(
    const QHelpFilterEngine *self) {
  return new QList<QString>(self->indices());
}

//  QStringList QHelpFilterEngine::indices(const QString &filterName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QHelpFilterEngine7indicesERK7QString(
    const QHelpFilterEngine *self,
    const QString *filterName) {
  return new QList<QString>(self->indices(*filterName));
}

//  void QHelpFilterEngine::filterActivated(const QString &newFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpFilterEngine15filterActivatedERK7QString(
    QHelpFilterEngine *self,
    const QString *newFilter) {
  self->filterActivated(*newFilter);
}

//  QHelpFilterEngine::QHelpFilterEngine(QHelpEngineCore *helpEngine)
extern "C" Q_DECL_EXPORT
QHelpFilterEngine *ritual_ZN17QHelpFilterEngineC1EP15QHelpEngineCore(
    QHelpEngineCore *helpEngine) {
  return new CuteQHelpFilterEngine(helpEngine);
}

//  QHelpFilterEngine::~QHelpFilterEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpFilterEngineD1Ev(QHelpFilterEngine *self) {
  delete self;
}

//  void QHelpFilterEngine::setCollectionHandler(QHelpCollectionHandler
//      *collectionHandler)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpFilterEngine20setCollectionHandlerEP22QHelpCollectionHandler(
    QHelpFilterEngine *self,
    QHelpCollectionHandler *collectionHandler) {
  self->setCollectionHandler(collectionHandler);
}

//  a Python function taken by a CuteQHelpFilterEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpFilterEngine(
    QHelpFilterEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpFilterEngine *>(self)->take(key, call);
}

//  a QMap<QString, QString> a ritual of QHelpFilterEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpFilterEngine__QMap_QString_QString(
    QMap<QString, QString> *self) {
  delete self;
}
