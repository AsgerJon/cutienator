//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpropertychanges_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpropertychanges_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickPropertyChanges that Python can take functions over in. Every QQuickPropertyChanges
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPropertyChangesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPropertyChangesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyChangesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyChangesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyChangesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyChangesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPropertyChangesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPropertyChanges : public QQuickPropertyChanges {
public:
  using QQuickPropertyChanges::QQuickPropertyChanges;
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
      CuteQQuickPropertyChangesCall0 call = reinterpret_cast<CuteQQuickPropertyChangesCall0>(taken[0]);
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
      CuteQQuickPropertyChangesCall1 call = reinterpret_cast<CuteQQuickPropertyChangesCall1>(taken[1]);
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
      CuteQQuickPropertyChangesCall2 call = reinterpret_cast<CuteQQuickPropertyChangesCall2>(taken[2]);
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
      CuteQQuickPropertyChangesCall3 call = reinterpret_cast<CuteQQuickPropertyChangesCall3>(taken[3]);
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
      CuteQQuickPropertyChangesCall4 call = reinterpret_cast<CuteQQuickPropertyChangesCall4>(taken[4]);
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
      CuteQQuickPropertyChangesCall5 call = reinterpret_cast<CuteQQuickPropertyChangesCall5>(taken[5]);
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
      CuteQQuickPropertyChangesCall6 call = reinterpret_cast<CuteQQuickPropertyChangesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPropertyChanges::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickPropertyChanges10metaObjectEv(
    const QQuickPropertyChanges *self) {
  return self->metaObject();
}

//  void *QQuickPropertyChanges::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickPropertyChanges11qt_metacastEPKc(
    QQuickPropertyChanges *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPropertyChanges::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickPropertyChanges11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPropertyChanges *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPropertyChanges::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickPropertyChanges2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPropertyChanges::tr(s, c, n));
}

//  QQuickPropertyChangesPrivate *QQuickPropertyChanges::d_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyChangesPrivate *ritual_ZN21QQuickPropertyChanges6d_funcEv(
    QQuickPropertyChanges *self) {
  return self->d_func();
}

//  const QQuickPropertyChangesPrivate *QQuickPropertyChanges::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPropertyChangesPrivate *ritual_ZNK21QQuickPropertyChanges6d_funcEv(
    const QQuickPropertyChanges *self) {
  return self->d_func();
}

//  QQuickPropertyChanges::QQuickPropertyChanges()
extern "C" Q_DECL_EXPORT
QQuickPropertyChanges *ritual_ZN21QQuickPropertyChangesC1Ev() {
  return new CuteQQuickPropertyChanges();
}

//  QQuickPropertyChanges::~QQuickPropertyChanges()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChangesD1Ev(QQuickPropertyChanges *self) {
  delete self;
}

//  QObject *QQuickPropertyChanges::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK21QQuickPropertyChanges6objectEv(
    const QQuickPropertyChanges *self) {
  return self->object();
}

//  void QQuickPropertyChanges::setObject(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges9setObjectEP7QObject(
    QQuickPropertyChanges *self,
    QObject *a0) {
  self->setObject(a0);
}

//  bool QQuickPropertyChanges::restoreEntryValues() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPropertyChanges18restoreEntryValuesEv(
    const QQuickPropertyChanges *self) {
  return self->restoreEntryValues();
}

//  void QQuickPropertyChanges::setRestoreEntryValues(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges21setRestoreEntryValuesEb(
    QQuickPropertyChanges *self,
    bool a0) {
  self->setRestoreEntryValues(a0);
}

//  bool QQuickPropertyChanges::isExplicit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPropertyChanges10isExplicitEv(
    const QQuickPropertyChanges *self) {
  return self->isExplicit();
}

//  void QQuickPropertyChanges::setIsExplicit(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges13setIsExplicitEb(
    QQuickPropertyChanges *self,
    bool a0) {
  self->setIsExplicit(a0);
}

//  ActionList QQuickPropertyChanges::actions()
extern "C" Q_DECL_EXPORT
QList<QQuickStateAction> *ritual_ZN21QQuickPropertyChanges7actionsEv(
    QQuickPropertyChanges *self) {
  return new QList<QQuickStateAction>(self->actions());
}

//  bool QQuickPropertyChanges::containsProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPropertyChanges16containsPropertyERK7QString(
    const QQuickPropertyChanges *self,
    const QString *name) {
  return self->containsProperty(*name);
}

//  bool QQuickPropertyChanges::containsValue(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPropertyChanges13containsValueERK7QString(
    const QQuickPropertyChanges *self,
    const QString *name) {
  return self->containsValue(*name);
}

//  bool QQuickPropertyChanges::containsExpression(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPropertyChanges18containsExpressionERK7QString(
    const QQuickPropertyChanges *self,
    const QString *name) {
  return self->containsExpression(*name);
}

//  void QQuickPropertyChanges::changeValue(const QString &name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges11changeValueERK7QStringRK8QVariant(
    QQuickPropertyChanges *self,
    const QString *name,
    const QVariant *value) {
  self->changeValue(*name, *value);
}

//  void QQuickPropertyChanges::changeExpression(const QString &name, const
//      QString &expression)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges16changeExpressionERK7QStringS2_(
    QQuickPropertyChanges *self,
    const QString *name,
    const QString *expression) {
  self->changeExpression(*name, *expression);
}

//  void QQuickPropertyChanges::removeProperty(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges14removePropertyERK7QString(
    QQuickPropertyChanges *self,
    const QString *name) {
  self->removeProperty(*name);
}

//  QVariant QQuickPropertyChanges::value(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickPropertyChanges5valueERK7QString(
    const QQuickPropertyChanges *self,
    const QString *name) {
  return new QVariant(self->value(*name));
}

//  QString QQuickPropertyChanges::expression(const QString &name) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickPropertyChanges10expressionERK7QString(
    const QQuickPropertyChanges *self,
    const QString *name) {
  return new QString(self->expression(*name));
}

//  void QQuickPropertyChanges::detachFromState()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges15detachFromStateEv(
    QQuickPropertyChanges *self) {
  self->detachFromState();
}

//  void QQuickPropertyChanges::attachToState()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges13attachToStateEv(
    QQuickPropertyChanges *self) {
  self->attachToState();
}

//  QVariant QQuickPropertyChanges::property(const QString &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickPropertyChanges8propertyERK7QString(
    const QQuickPropertyChanges *self,
    const QString *name) {
  return new QVariant(self->property(*name));
}

//  void QQuickPropertyChanges::objectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges13objectChangedEv(
    QQuickPropertyChanges *self) {
  self->objectChanged();
}

//  void QQuickPropertyChanges::restoreEntryValuesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges25restoreEntryValuesChangedEv(
    QQuickPropertyChanges *self) {
  self->restoreEntryValuesChanged();
}

//  void QQuickPropertyChanges::isExplicitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPropertyChanges17isExplicitChangedEv(
    QQuickPropertyChanges *self) {
  self->isExplicitChanged();
}

//  a Python function taken by a CuteQQuickPropertyChanges, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPropertyChanges(
    QQuickPropertyChanges *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPropertyChanges *>(self)->take(key, call);
}
