//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmldatamodelplugin_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmldatamodelplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScxmlDataModelPlugin that Python can take functions over in. Every QScxmlDataModelPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScxmlDataModelPluginCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlDataModelPluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlDataModelPluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelPluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelPluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelPluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlDataModelPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlDataModelPlugin : public QScxmlDataModelPlugin {
public:
  using QScxmlDataModelPlugin::QScxmlDataModelPlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QScxmlDataModelPlugin20createScxmlDataModelEv")) {
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

  //  QScxmlDataModel *QScxmlDataModelPlugin::createScxmlDataModel() const
  QScxmlDataModel *createScxmlDataModel() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlDataModelPluginCall0 call = reinterpret_cast<CuteQScxmlDataModelPluginCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QScxmlDataModel *>(given);
    }
    return QScxmlDataModelPlugin::createScxmlDataModel();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScxmlDataModelPluginCall1 call = reinterpret_cast<CuteQScxmlDataModelPluginCall1>(taken[1]);
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
      CuteQScxmlDataModelPluginCall2 call = reinterpret_cast<CuteQScxmlDataModelPluginCall2>(taken[2]);
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
      CuteQScxmlDataModelPluginCall3 call = reinterpret_cast<CuteQScxmlDataModelPluginCall3>(taken[3]);
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
      CuteQScxmlDataModelPluginCall4 call = reinterpret_cast<CuteQScxmlDataModelPluginCall4>(taken[4]);
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
      CuteQScxmlDataModelPluginCall5 call = reinterpret_cast<CuteQScxmlDataModelPluginCall5>(taken[5]);
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
      CuteQScxmlDataModelPluginCall6 call = reinterpret_cast<CuteQScxmlDataModelPluginCall6>(taken[6]);
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
      CuteQScxmlDataModelPluginCall7 call = reinterpret_cast<CuteQScxmlDataModelPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlDataModelPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QScxmlDataModelPlugin10metaObjectEv(
    const QScxmlDataModelPlugin *self) {
  return self->metaObject();
}

//  QString QScxmlDataModelPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QScxmlDataModelPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlDataModelPlugin::tr(s, c, n));
}

//  QScxmlDataModel *QScxmlDataModelPlugin::createScxmlDataModel() const
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_ZNK21QScxmlDataModelPlugin20createScxmlDataModelEv(
    const QScxmlDataModelPlugin *self) {
  return self->createScxmlDataModel();
}

//  a Python function taken by a CuteQScxmlDataModelPlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlDataModelPlugin(
    QScxmlDataModelPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlDataModelPlugin *>(self)->take(key, call);
}

//  QScxmlDataModel *QScxmlDataModelPlugin::createScxmlDataModel() const
extern "C" Q_DECL_EXPORT
QScxmlDataModel *ritual_own_ZNK21QScxmlDataModelPlugin20createScxmlDataModelEv(
    const QScxmlDataModelPlugin *self) {
  return self->QScxmlDataModelPlugin::createScxmlDataModel();
}
