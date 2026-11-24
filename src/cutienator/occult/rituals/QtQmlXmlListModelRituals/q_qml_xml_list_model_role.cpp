//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qtqmlxmllistmodelglobal_p.h>
#include <QtQmlXmlListModel/QtQmlXmlListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlXmlListModelRole that Python can take functions over in. Every QQmlXmlListModelRole
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlXmlListModelRoleCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlXmlListModelRoleCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelRoleCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelRoleCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelRoleCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelRoleCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelRoleCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlXmlListModelRole : public QQmlXmlListModelRole {
public:
  using QQmlXmlListModelRole::QQmlXmlListModelRole;
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
      CuteQQmlXmlListModelRoleCall0 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall0>(taken[0]);
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
      CuteQQmlXmlListModelRoleCall1 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall1>(taken[1]);
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
      CuteQQmlXmlListModelRoleCall2 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall2>(taken[2]);
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
      CuteQQmlXmlListModelRoleCall3 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall3>(taken[3]);
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
      CuteQQmlXmlListModelRoleCall4 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall4>(taken[4]);
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
      CuteQQmlXmlListModelRoleCall5 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall5>(taken[5]);
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
      CuteQQmlXmlListModelRoleCall6 call = reinterpret_cast<CuteQQmlXmlListModelRoleCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlXmlListModelRole::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlXmlListModelRole10metaObjectEv(
    const QQmlXmlListModelRole *self) {
  return self->metaObject();
}

//  QString QQmlXmlListModelRole::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlXmlListModelRole2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlXmlListModelRole::tr(s, c, n));
}

//  QQmlXmlListModelRole::QQmlXmlListModelRole()
extern "C" Q_DECL_EXPORT
QQmlXmlListModelRole *ritual_ZN20QQmlXmlListModelRoleC1Ev() {
  return new CuteQQmlXmlListModelRole();
}

//  QQmlXmlListModelRole::~QQmlXmlListModelRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlXmlListModelRoleD1Ev(QQmlXmlListModelRole *self) {
  delete self;
}

//  QString QQmlXmlListModelRole::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlXmlListModelRole4nameEv(
    const QQmlXmlListModelRole *self) {
  return new QString(self->name());
}

//  void QQmlXmlListModelRole::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlXmlListModelRole7setNameERK7QString(
    QQmlXmlListModelRole *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QQmlXmlListModelRole::elementName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlXmlListModelRole11elementNameEv(
    const QQmlXmlListModelRole *self) {
  return new QString(self->elementName());
}

//  void QQmlXmlListModelRole::setElementName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlXmlListModelRole14setElementNameERK7QString(
    QQmlXmlListModelRole *self,
    const QString *name) {
  self->setElementName(*name);
}

//  QString QQmlXmlListModelRole::attributeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlXmlListModelRole13attributeNameEv(
    const QQmlXmlListModelRole *self) {
  return new QString(self->attributeName());
}

//  void QQmlXmlListModelRole::setAttributeName(const QString &attributeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlXmlListModelRole16setAttributeNameERK7QString(
    QQmlXmlListModelRole *self,
    const QString *attributeName) {
  self->setAttributeName(*attributeName);
}

//  bool QQmlXmlListModelRole::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlXmlListModelRole7isValidEv(
    const QQmlXmlListModelRole *self) {
  return self->isValid();
}

//  a Python function taken by a CuteQQmlXmlListModelRole, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlXmlListModelRole(
    QQmlXmlListModelRole *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlXmlListModelRole *>(self)->take(key, call);
}
