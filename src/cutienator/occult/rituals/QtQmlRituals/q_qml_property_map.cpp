//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlpropertymap.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 1. Kept as it is when the
//  generator runs again.
#include <QtQml/QtQml>
#include <QtQml/qqmlpropertymap.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QQmlPropertyMap may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlPropertyMap : QQmlPropertyMap {
  using QQmlPropertyMap::updateValue;
};

//  A QQmlPropertyMap that Python can take functions over in. Every QQmlPropertyMap
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQmlPropertyMapCall0)(const void *, const QString *, const QVariant *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlPropertyMapCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlPropertyMapCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPropertyMapCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPropertyMapCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPropertyMapCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPropertyMapCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlPropertyMapCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlPropertyMap : public QQmlPropertyMap {
public:
  using QQmlPropertyMap::QQmlPropertyMap;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVariant")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVariant QQmlPropertyMap::updateValue(const QString &key, const
  //      QVariant &input)
  QVariant updateValue(const QString &key, const QVariant &input) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPropertyMapCall0 call = reinterpret_cast<CuteQQmlPropertyMapCall0>(taken[0]);
      const QVariant * given = call(this, &key, &input, &handled);
      if (handled && given) return *given;
    }
    return QQmlPropertyMap::updateValue(key, input);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlPropertyMapCall1 call = reinterpret_cast<CuteQQmlPropertyMapCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlPropertyMapCall2 call = reinterpret_cast<CuteQQmlPropertyMapCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlPropertyMapCall3 call = reinterpret_cast<CuteQQmlPropertyMapCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlPropertyMapCall4 call = reinterpret_cast<CuteQQmlPropertyMapCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlPropertyMapCall5 call = reinterpret_cast<CuteQQmlPropertyMapCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlPropertyMapCall6 call = reinterpret_cast<CuteQQmlPropertyMapCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlPropertyMapCall7 call = reinterpret_cast<CuteQQmlPropertyMapCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlPropertyMap::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlPropertyMap10metaObjectEv(
    const QQmlPropertyMap *self) {
  return self->metaObject();
}

//  void *QQmlPropertyMap::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQmlPropertyMap11qt_metacastEPKc(
    QQmlPropertyMap *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlPropertyMap::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlPropertyMap11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlPropertyMap *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlPropertyMap::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlPropertyMap2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlPropertyMap::tr(s, c, n));
}

//  void QQmlPropertyMap::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMap22qt_qmlMarker_anonymousEv(
    QQmlPropertyMap *self) {
  self->qt_qmlMarker_anonymous();
}

#if QT_DEPRECATED_SINCE(6, 11)
//  QQmlPropertyMap::QQmlPropertyMap(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlPropertyMap *ritual_ZN15QQmlPropertyMapC1EP7QObject(QObject *parent) {
  return new CuteQQmlPropertyMap(parent);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

//  QQmlPropertyMap *QQmlPropertyMap::create(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlPropertyMap *ritual_ZN15QQmlPropertyMap6createEP7QObject(
    QObject *parent) {
  return QQmlPropertyMap::create(parent);
}

//  QQmlPropertyMap::~QQmlPropertyMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMapD1Ev(QQmlPropertyMap *self) {
  delete self;
}

//  QVariant QQmlPropertyMap::value(const QString &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQmlPropertyMap5valueERK7QString(
    const QQmlPropertyMap *self,
    const QString *key) {
  return new QVariant(self->value(*key));
}

//  void QQmlPropertyMap::insert(const QString &key, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMap6insertERK7QStringRK8QVariant(
    QQmlPropertyMap *self,
    const QString *key,
    const QVariant *value) {
  self->insert(*key, *value);
}

//  void QQmlPropertyMap::insert(const QVariantHash &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMap6insertERK5QHashI7QString8QVariantE(
    QQmlPropertyMap *self,
    const QHash<QString, QVariant> *values) {
  self->insert(*values);
}

//  void QQmlPropertyMap::clear(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMap5clearERK7QString(
    QQmlPropertyMap *self,
    const QString *key) {
  self->clear(*key);
}

//  void QQmlPropertyMap::freeze()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMap6freezeEv(QQmlPropertyMap *self) {
  self->freeze();
}

//  QStringList QQmlPropertyMap::keys() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QQmlPropertyMap4keysEv(
    const QQmlPropertyMap *self) {
  return new QList<QString>(self->keys());
}

//  int QQmlPropertyMap::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlPropertyMap5countEv(const QQmlPropertyMap *self) {
  return self->count();
}

//  int QQmlPropertyMap::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlPropertyMap4sizeEv(const QQmlPropertyMap *self) {
  return self->size();
}

//  bool QQmlPropertyMap::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlPropertyMap7isEmptyEv(const QQmlPropertyMap *self) {
  return self->isEmpty();
}

//  bool QQmlPropertyMap::contains(const QString &key) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlPropertyMap8containsERK7QString(
    const QQmlPropertyMap *self,
    const QString *key) {
  return self->contains(*key);
}

//  QVariant &QQmlPropertyMap::operator[](const QString &key)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QQmlPropertyMapixERK7QString(
    QQmlPropertyMap *self,
    const QString *key) {
  return &(self->operator[](*key));
}

//  QVariant QQmlPropertyMap::operator[](const QString &key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQmlPropertyMapixERK7QString(
    const QQmlPropertyMap *self,
    const QString *key) {
  return new QVariant(self->operator[](*key));
}

//  void QQmlPropertyMap::valueChanged(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlPropertyMap12valueChangedERK7QStringRK8QVariant(
    QQmlPropertyMap *self,
    const QString *key,
    const QVariant *value) {
  self->valueChanged(*key, *value);
}

//  QVariant QQmlPropertyMap::updateValue(const QString &key, const QVariant
//      &input)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVariant(
    QQmlPropertyMap *self,
    const QString *key,
    const QVariant *input) {
  return new QVariant(self->updateValue(*key, *input));
}

//  QQmlPropertyMap::QQmlPropertyMap(const QMetaObject *staticMetaObject,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlPropertyMap *ritual_ZN15QQmlPropertyMapC1EPK11QMetaObjectP7QObject(
    const QMetaObject *staticMetaObject,
    QObject *parent) {
  return new CuteQQmlPropertyMap(staticMetaObject, parent);
}

//  QQmlPropertyMapPrivate *QQmlPropertyMap::d_func()
extern "C" Q_DECL_EXPORT
QQmlPropertyMapPrivate *ritual_ZN15QQmlPropertyMap6d_funcEv(
    QQmlPropertyMap *self) {
  return self->d_func();
}

//  const QQmlPropertyMapPrivate *QQmlPropertyMap::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlPropertyMapPrivate *ritual_ZNK15QQmlPropertyMap6d_funcEv(
    const QQmlPropertyMap *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlPropertyMap, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPropertyMap(
    QQmlPropertyMap *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPropertyMap *>(self)->take(key, call);
}

//  QVariant QQmlPropertyMap::updateValue(const QString &key, const QVariant
//      &input)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN15QQmlPropertyMap11updateValueERK7QStringRK8QVariant(
    QQmlPropertyMap *self,
    const QString *key,
    const QVariant *input) {
  return new QVariant(
      static_cast<OwnQQmlPropertyMap *>(self)->OwnQQmlPropertyMap::updateValue(
          *key,
          *input));
}

//  QQmlPropertyMap::QQmlPropertyMap<QQmlPropertyMap>(QQmlPropertyMap
//      *derived, QObject *parentObj)
extern "C" Q_DECL_EXPORT
QQmlPropertyMap * ritual_ZN15QQmlPropertyMapC2IS_EEPT_P7QObject(
    QQmlPropertyMap *derived,
    QObject *parentObj) {
  return new QQmlPropertyMap(derived, parentObj);
}
