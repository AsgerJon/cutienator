//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpengine.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  the config header of QtTools is included before the first #if,
//  as QT_CONFIG(fullqthelp) is defined there. Kept as it is when
//  the generator runs again.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHelpEngine that Python can take functions over in. Every QHelpEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpEngine : public QHelpEngine {
public:
  using QHelpEngine::QHelpEngine;
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
      CuteQHelpEngineCall0 call = reinterpret_cast<CuteQHelpEngineCall0>(taken[0]);
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
      CuteQHelpEngineCall1 call = reinterpret_cast<CuteQHelpEngineCall1>(taken[1]);
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
      CuteQHelpEngineCall2 call = reinterpret_cast<CuteQHelpEngineCall2>(taken[2]);
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
      CuteQHelpEngineCall3 call = reinterpret_cast<CuteQHelpEngineCall3>(taken[3]);
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
      CuteQHelpEngineCall4 call = reinterpret_cast<CuteQHelpEngineCall4>(taken[4]);
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
      CuteQHelpEngineCall5 call = reinterpret_cast<CuteQHelpEngineCall5>(taken[5]);
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
      CuteQHelpEngineCall6 call = reinterpret_cast<CuteQHelpEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QHelpEngine10metaObjectEv(
    const QHelpEngine *self) {
  return self->metaObject();
}

//  void *QHelpEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QHelpEngine11qt_metacastEPKc(
    QHelpEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QHelpEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpEngine::tr(s, c, n));
}

//  QHelpEngine::QHelpEngine(const QString &collectionFile, QObject *parent)
extern "C" Q_DECL_EXPORT
QHelpEngine *ritual_ZN11QHelpEngineC1ERK7QStringP7QObject(
    const QString *collectionFile,
    QObject *parent) {
  return new CuteQHelpEngine(*collectionFile, parent);
}

//  QHelpEngine::~QHelpEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHelpEngineD1Ev(QHelpEngine *self) {
  delete self;
}

//  QHelpContentModel *QHelpEngine::contentModel() const
extern "C" Q_DECL_EXPORT
QHelpContentModel *ritual_ZNK11QHelpEngine12contentModelEv(
    const QHelpEngine *self) {
  return self->contentModel();
}

//  QHelpIndexModel *QHelpEngine::indexModel() const
extern "C" Q_DECL_EXPORT
QHelpIndexModel *ritual_ZNK11QHelpEngine10indexModelEv(
    const QHelpEngine *self) {
  return self->indexModel();
}

//  QHelpContentWidget *QHelpEngine::contentWidget()
extern "C" Q_DECL_EXPORT
QHelpContentWidget *ritual_ZN11QHelpEngine13contentWidgetEv(
    QHelpEngine *self) {
  return self->contentWidget();
}

//  QHelpIndexWidget *QHelpEngine::indexWidget()
extern "C" Q_DECL_EXPORT
QHelpIndexWidget *ritual_ZN11QHelpEngine11indexWidgetEv(QHelpEngine *self) {
  return self->indexWidget();
}

//  QHelpSearchEngine *QHelpEngine::searchEngine()
extern "C" Q_DECL_EXPORT
QHelpSearchEngine *ritual_ZN11QHelpEngine12searchEngineEv(
    QHelpEngine *self) {
  return self->searchEngine();
}

//  a Python function taken by a CuteQHelpEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpEngine(
    QHelpEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpEngine *>(self)->take(key, call);
}

#endif  // QT_CONFIG(fullqthelp)
