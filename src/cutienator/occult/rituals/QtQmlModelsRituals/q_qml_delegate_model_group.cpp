//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlDelegateModelGroup that Python can take functions over in. Every QQmlDelegateModelGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelGroupCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelegateModelGroupCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelGroupCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelGroupCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelGroupCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelGroupCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelegateModelGroupCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDelegateModelGroup : public QQmlDelegateModelGroup {
public:
  using QQmlDelegateModelGroup::QQmlDelegateModelGroup;
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
      CuteQQmlDelegateModelGroupCall0 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall0>(taken[0]);
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
      CuteQQmlDelegateModelGroupCall1 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall1>(taken[1]);
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
      CuteQQmlDelegateModelGroupCall2 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall2>(taken[2]);
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
      CuteQQmlDelegateModelGroupCall3 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall3>(taken[3]);
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
      CuteQQmlDelegateModelGroupCall4 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall4>(taken[4]);
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
      CuteQQmlDelegateModelGroupCall5 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall5>(taken[5]);
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
      CuteQQmlDelegateModelGroupCall6 call = reinterpret_cast<CuteQQmlDelegateModelGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDelegateModelGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlDelegateModelGroup10metaObjectEv(
    const QQmlDelegateModelGroup *self) {
  return self->metaObject();
}

//  QString QQmlDelegateModelGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQmlDelegateModelGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDelegateModelGroup::tr(s, c, n));
}

//  QQmlDelegateModelGroup::QQmlDelegateModelGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroup *ritual_ZN22QQmlDelegateModelGroupC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlDelegateModelGroup(parent);
}

//  QQmlDelegateModelGroup::QQmlDelegateModelGroup(const QString &name,
//      QQmlDelegateModel *model, int compositorType, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroup *ritual_ZN22QQmlDelegateModelGroupC1ERK7QStringP17QQmlDelegateModeliP7QObject(
    const QString *name,
    QQmlDelegateModel *model,
    int compositorType,
    QObject *parent) {
  return new CuteQQmlDelegateModelGroup(
      *name,
      model,
      compositorType,
      parent);
}

//  QQmlDelegateModelGroup::~QQmlDelegateModelGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroupD1Ev(QQmlDelegateModelGroup *self) {
  delete self;
}

//  QString QQmlDelegateModelGroup::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQmlDelegateModelGroup4nameEv(
    const QQmlDelegateModelGroup *self) {
  return new QString(self->name());
}

//  void QQmlDelegateModelGroup::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup7setNameERK7QString(
    QQmlDelegateModelGroup *self,
    const QString *name) {
  self->setName(*name);
}

//  int QQmlDelegateModelGroup::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQmlDelegateModelGroup5countEv(
    const QQmlDelegateModelGroup *self) {
  return self->count();
}

//  bool QQmlDelegateModelGroup::defaultInclude() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQmlDelegateModelGroup14defaultIncludeEv(
    const QQmlDelegateModelGroup *self) {
  return self->defaultInclude();
}

//  void QQmlDelegateModelGroup::setDefaultInclude(bool include)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup17setDefaultIncludeEb(
    QQmlDelegateModelGroup *self,
    bool include) {
  self->setDefaultInclude(include);
}

//  QJSValue QQmlDelegateModelGroup::get(int index)
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN22QQmlDelegateModelGroup3getEi(
    QQmlDelegateModelGroup *self,
    int index) {
  return new QJSValue(self->get(index));
}

//  void QQmlDelegateModelGroup::insert(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup6insertEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->insert(a0);
}

//  void QQmlDelegateModelGroup::create(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup6createEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->create(a0);
}

//  void QQmlDelegateModelGroup::resolve(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup7resolveEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->resolve(a0);
}

//  void QQmlDelegateModelGroup::remove(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup6removeEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->remove(a0);
}

//  void QQmlDelegateModelGroup::addGroups(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup9addGroupsEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->addGroups(a0);
}

//  void QQmlDelegateModelGroup::removeGroups(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup12removeGroupsEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->removeGroups(a0);
}

//  void QQmlDelegateModelGroup::setGroups(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup9setGroupsEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->setGroups(a0);
}

//  void QQmlDelegateModelGroup::move(QQmlV4FunctionPtr a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlDelegateModelGroup4moveEP14QQmlV4Function(
    QQmlDelegateModelGroup *self,
    QQmlV4FunctionPtr a0) {
  self->move(a0);
}

//  QQmlDelegateModelGroupPrivate *QQmlDelegateModelGroup::d_func()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroupPrivate *ritual_ZN22QQmlDelegateModelGroup6d_funcEv(
    QQmlDelegateModelGroup *self) {
  return self->d_func();
}

//  const QQmlDelegateModelGroupPrivate *QQmlDelegateModelGroup::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlDelegateModelGroupPrivate *ritual_ZNK22QQmlDelegateModelGroup6d_funcEv(
    const QQmlDelegateModelGroup *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlDelegateModelGroup, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelegateModelGroup(
    QQmlDelegateModelGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelegateModelGroup *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
