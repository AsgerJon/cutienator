//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/6.12.0/QtWebView/private/qwebviewplugin_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebView/QtWebView>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebView/6.12.0/QtWebView/private/qwebviewplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebViewPlugin that Python can take functions over in. Every QWebViewPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQWebViewPluginCall0)(const void *, const QString *, QWebView *, int, int *);
typedef void (*CuteQWebViewPluginCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebViewPluginCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebViewPluginCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPluginCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPluginCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPluginCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebViewPluginCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebViewPlugin : public QWebViewPlugin {
public:
  using QWebViewPlugin::QWebViewPlugin;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QWebViewPlugin6createERK7QStringP8QWebViewN15QWebViewFactory4HintE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWebViewPlugin7prepareEv")) {
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

  //  QWebViewPrivate *QWebViewPlugin::create(const QString &key, QWebView
  //      *view, QWebViewFactory::Hint hint) const
  QWebViewPrivate *create(
      const QString &key,
      QWebView *view,
      QWebViewFactory::Hint hint) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebViewPluginCall0 call = reinterpret_cast<CuteQWebViewPluginCall0>(taken[0]);
      void * given = call(this, &key, view, static_cast<int>(hint), &handled);
      if (handled) return static_cast<QWebViewPrivate *>(given);
    }
    return {};
  }

  //  void QWebViewPlugin::prepare() const
  void prepare() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebViewPluginCall1 call = reinterpret_cast<CuteQWebViewPluginCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWebViewPlugin::prepare();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebViewPluginCall2 call = reinterpret_cast<CuteQWebViewPluginCall2>(taken[2]);
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
      CuteQWebViewPluginCall3 call = reinterpret_cast<CuteQWebViewPluginCall3>(taken[3]);
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
      CuteQWebViewPluginCall4 call = reinterpret_cast<CuteQWebViewPluginCall4>(taken[4]);
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
      CuteQWebViewPluginCall5 call = reinterpret_cast<CuteQWebViewPluginCall5>(taken[5]);
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
      CuteQWebViewPluginCall6 call = reinterpret_cast<CuteQWebViewPluginCall6>(taken[6]);
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
      CuteQWebViewPluginCall7 call = reinterpret_cast<CuteQWebViewPluginCall7>(taken[7]);
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
      CuteQWebViewPluginCall8 call = reinterpret_cast<CuteQWebViewPluginCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebViewPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWebViewPlugin10metaObjectEv(
    const QWebViewPlugin *self) {
  return self->metaObject();
}

//  QString QWebViewPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWebViewPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebViewPlugin::tr(s, c, n));
}

//  QWebViewPlugin::~QWebViewPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWebViewPluginD1Ev(QWebViewPlugin *self) {
  delete self;
}

//  QWebViewPrivate *QWebViewPlugin::create(const QString &key, QWebView
//      *view, QWebViewFactory::Hint hint) const
extern "C" Q_DECL_EXPORT
QWebViewPrivate *ritual_ZNK14QWebViewPlugin6createERK7QStringP8QWebViewN15QWebViewFactory4HintE(
    const QWebViewPlugin *self,
    const QString *key,
    QWebView *view,
    QWebViewFactory::Hint hint) {
  return self->create(*key, view, hint);
}

//  void QWebViewPlugin::prepare() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWebViewPlugin7prepareEv(const QWebViewPlugin *self) {
  self->prepare();
}

//  a Python function taken by a CuteQWebViewPlugin, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebViewPlugin(
    QWebViewPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebViewPlugin *>(self)->take(key, call);
}

//  void QWebViewPlugin::prepare() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QWebViewPlugin7prepareEv(const QWebViewPlugin *self) {
  self->QWebViewPlugin::prepare();
}
