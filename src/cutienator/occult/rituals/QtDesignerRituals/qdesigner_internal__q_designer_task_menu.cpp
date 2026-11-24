//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_taskmenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_taskmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A qdesigner_internal::QDesignerTaskMenu that Python can take functions over in. Every qdesigner_internal::QDesignerTaskMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerTaskMenuCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*Cuteqdesigner_internal_QDesignerTaskMenuCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*Cuteqdesigner_internal_QDesignerTaskMenuCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*Cuteqdesigner_internal_QDesignerTaskMenuCall7)(const void *, int *);
class Cuteqdesigner_internal_QDesignerTaskMenu : public qdesigner_internal::QDesignerTaskMenu {
public:
  using qdesigner_internal::QDesignerTaskMenu::QDesignerTaskMenu;
  void *taken[8] = {};

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
    if (!std::strcmp(key, "_ZNK26QDesignerTaskMenuExtension19preferredEditActionEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall0 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall0>(taken[0]);
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
      Cuteqdesigner_internal_QDesignerTaskMenuCall1 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall1>(taken[1]);
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
      Cuteqdesigner_internal_QDesignerTaskMenuCall2 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall2>(taken[2]);
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
      Cuteqdesigner_internal_QDesignerTaskMenuCall3 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall3>(taken[3]);
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
      Cuteqdesigner_internal_QDesignerTaskMenuCall4 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall4>(taken[4]);
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
      Cuteqdesigner_internal_QDesignerTaskMenuCall5 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall5>(taken[5]);
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
      Cuteqdesigner_internal_QDesignerTaskMenuCall6 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QAction *QDesignerTaskMenuExtension::preferredEditAction() const
  QAction *preferredEditAction() const override {
    if (taken[7]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerTaskMenuCall7 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerTaskMenuCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return QDesignerTaskMenuExtension::preferredEditAction();
  }
};

//  const QMetaObject *qdesigner_internal::QDesignerTaskMenu::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal17QDesignerTaskMenu10metaObjectEv(
    const qdesigner_internal::QDesignerTaskMenu *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::QDesignerTaskMenu::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal17QDesignerTaskMenu2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QDesignerTaskMenu::tr(s, c, n));
}

//  qdesigner_internal::QDesignerTaskMenu as the QDesignerTaskMenuExtension
//      it is built on
extern "C" Q_DECL_EXPORT
QDesignerTaskMenuExtension *ritual_cast_qdesigner_internal_QDesignerTaskMenu_QDesignerTaskMenuExtension(
    qdesigner_internal::QDesignerTaskMenu *self) {
  return static_cast<QDesignerTaskMenuExtension *>(self);
}

//  a Python function taken by a Cuteqdesigner_internal_QDesignerTaskMenu,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QDesignerTaskMenu(
    qdesigner_internal::QDesignerTaskMenu *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QDesignerTaskMenu *>(self)->take(key, call);
}
