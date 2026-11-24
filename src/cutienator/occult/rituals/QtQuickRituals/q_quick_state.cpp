//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlanybinding_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickState that Python can take functions over in. Every QQuickState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickState : public QQuickState {
public:
  using QQuickState::QQuickState;
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
      CuteQQuickStateCall0 call = reinterpret_cast<CuteQQuickStateCall0>(taken[0]);
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
      CuteQQuickStateCall1 call = reinterpret_cast<CuteQQuickStateCall1>(taken[1]);
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
      CuteQQuickStateCall2 call = reinterpret_cast<CuteQQuickStateCall2>(taken[2]);
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
      CuteQQuickStateCall3 call = reinterpret_cast<CuteQQuickStateCall3>(taken[3]);
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
      CuteQQuickStateCall4 call = reinterpret_cast<CuteQQuickStateCall4>(taken[4]);
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
      CuteQQuickStateCall5 call = reinterpret_cast<CuteQQuickStateCall5>(taken[5]);
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
      CuteQQuickStateCall6 call = reinterpret_cast<CuteQQuickStateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickState10metaObjectEv(
    const QQuickState *self) {
  return self->metaObject();
}

//  QString QQuickState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickState::tr(s, c, n));
}

//  QQuickState::QQuickState(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickState *ritual_ZN11QQuickStateC1EP7QObject(QObject *parent) {
  return new CuteQQuickState(parent);
}

//  QQuickState::~QQuickState()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickStateD1Ev(QQuickState *self) {
  delete self;
}

//  QString QQuickState::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQuickState4nameEv(const QQuickState *self) {
  return new QString(self->name());
}

//  void QQuickState::setName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState7setNameERK7QString(
    QQuickState *self,
    const QString *a0) {
  self->setName(*a0);
}

//  bool QQuickState::isNamed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickState7isNamedEv(const QQuickState *self) {
  return self->isNamed();
}

//  bool QQuickState::isWhenKnown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickState11isWhenKnownEv(const QQuickState *self) {
  return self->isWhenKnown();
}

//  bool QQuickState::when() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickState4whenEv(const QQuickState *self) {
  return self->when();
}

//  void QQuickState::setWhen(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState7setWhenEb(QQuickState *self, bool a0) {
  self->setWhen(a0);
}

//  QString QQuickState::extends() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQuickState7extendsEv(const QQuickState *self) {
  return new QString(self->extends());
}

//  void QQuickState::setExtends(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState10setExtendsERK7QString(
    QQuickState *self,
    const QString *a0) {
  self->setExtends(*a0);
}

//  int QQuickState::operationCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QQuickState14operationCountEv(const QQuickState *self) {
  return self->operationCount();
}

//  QQuickStateOperation *QQuickState::operationAt(int a0) const
extern "C" Q_DECL_EXPORT
QQuickStateOperation *ritual_ZNK11QQuickState11operationAtEi(
    const QQuickState *self,
    int a0) {
  return self->operationAt(a0);
}

//  void QQuickState::apply(QQuickTransition *a0, QQuickState *revert)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState5applyEP16QQuickTransitionPS_(
    QQuickState *self,
    QQuickTransition *a0,
    QQuickState *revert) {
  self->apply(a0, revert);
}

//  void QQuickState::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState6cancelEv(QQuickState *self) {
  self->cancel();
}

//  QQuickStateGroup *QQuickState::stateGroup() const
extern "C" Q_DECL_EXPORT
QQuickStateGroup *ritual_ZNK11QQuickState10stateGroupEv(
    const QQuickState *self) {
  return self->stateGroup();
}

//  void QQuickState::setStateGroup(QQuickStateGroup *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState13setStateGroupEP16QQuickStateGroup(
    QQuickState *self,
    QQuickStateGroup *a0) {
  self->setStateGroup(a0);
}

//  bool QQuickState::containsPropertyInRevertList(QObject *target, const
//      QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickState28containsPropertyInRevertListEP7QObjectRK7QString(
    const QQuickState *self,
    QObject *target,
    const QString *name) {
  return self->containsPropertyInRevertList(target, *name);
}

//  bool QQuickState::changeValueInRevertList(QObject *target, const QString
//      &name, const QVariant &revertValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickState23changeValueInRevertListEP7QObjectRK7QStringRK8QVariant(
    QQuickState *self,
    QObject *target,
    const QString *name,
    const QVariant *revertValue) {
  return self->changeValueInRevertList(target, *name, *revertValue);
}

//  bool QQuickState::changeBindingInRevertList(QObject *target, const
//      QString &name, QQmlAnyBinding binding)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickState25changeBindingInRevertListEP7QObjectRK7QString14QQmlAnyBinding(
    QQuickState *self,
    QObject *target,
    const QString *name,
    const QQmlAnyBinding *binding) {
  return self->changeBindingInRevertList(target, *name, *binding);
}

//  bool QQuickState::removeEntryFromRevertList(QObject *target, const
//      QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQuickState25removeEntryFromRevertListEP7QObjectRK7QString(
    QQuickState *self,
    QObject *target,
    const QString *name) {
  return self->removeEntryFromRevertList(target, *name);
}

//  void QQuickState::addEntryToRevertList(const QQuickStateAction &action)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState20addEntryToRevertListERK17QQuickStateAction(
    QQuickState *self,
    const QQuickStateAction *action) {
  self->addEntryToRevertList(*action);
}

//  void QQuickState::removeAllEntriesFromRevertList(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState30removeAllEntriesFromRevertListEP7QObject(
    QQuickState *self,
    QObject *target) {
  self->removeAllEntriesFromRevertList(target);
}

//  void QQuickState::addEntriesToRevertList(const QList<QQuickStateAction>
//      &actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickState22addEntriesToRevertListERK5QListI17QQuickStateActionE(
    QQuickState *self,
    const QList<QQuickStateAction> *actions) {
  self->addEntriesToRevertList(*actions);
}

//  QVariant QQuickState::valueInRevertList(QObject *target, const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QQuickState17valueInRevertListEP7QObjectRK7QString(
    const QQuickState *self,
    QObject *target,
    const QString *name) {
  return new QVariant(self->valueInRevertList(target, *name));
}

//  QQmlAnyBinding QQuickState::bindingInRevertList(QObject *target, const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QQmlAnyBinding *ritual_ZNK11QQuickState19bindingInRevertListEP7QObjectRK7QString(
    const QQuickState *self,
    QObject *target,
    const QString *name) {
  return new QQmlAnyBinding(self->bindingInRevertList(target, *name));
}

//  bool QQuickState::isStateActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickState13isStateActiveEv(const QQuickState *self) {
  return self->isStateActive();
}

//  QQuickStatePrivate *QQuickState::d_func()
extern "C" Q_DECL_EXPORT
QQuickStatePrivate *ritual_ZN11QQuickState6d_funcEv(QQuickState *self) {
  return self->d_func();
}

//  const QQuickStatePrivate *QQuickState::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickStatePrivate *ritual_ZNK11QQuickState6d_funcEv(
    const QQuickState *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickState, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickState(
    QQuickState *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickState *>(self)->take(key, call);
}

//  QList<QQuickState *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickState *> *ritual_list_make_QQuickState_ptr() {
  return new QList<QQuickState *>();
}

//  void QList<QQuickState *>::append(const QQuickState * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickState_ptr(
    QList<QQuickState *> *self,
    QQuickState *element) {
  self->append(element);
}

//  qsizetype QList<QQuickState *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickState_ptr(
    const QList<QQuickState *> *self) {
  return self->size();
}

//  const QQuickState * &QList<QQuickState *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuickState *ritual_list_at_QQuickState_ptr(
    const QList<QQuickState *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickState *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickState_ptr(QList<QQuickState *> *self) {
  delete self;
}
