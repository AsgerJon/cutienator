//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlfileselector.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlfileselector.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlFileSelector that Python can take functions over in. Every QQmlFileSelector
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlFileSelectorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlFileSelectorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFileSelectorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFileSelectorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFileSelectorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFileSelectorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlFileSelectorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlFileSelector : public QQmlFileSelector {
public:
  using QQmlFileSelector::QQmlFileSelector;
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
      CuteQQmlFileSelectorCall0 call = reinterpret_cast<CuteQQmlFileSelectorCall0>(taken[0]);
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
      CuteQQmlFileSelectorCall1 call = reinterpret_cast<CuteQQmlFileSelectorCall1>(taken[1]);
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
      CuteQQmlFileSelectorCall2 call = reinterpret_cast<CuteQQmlFileSelectorCall2>(taken[2]);
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
      CuteQQmlFileSelectorCall3 call = reinterpret_cast<CuteQQmlFileSelectorCall3>(taken[3]);
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
      CuteQQmlFileSelectorCall4 call = reinterpret_cast<CuteQQmlFileSelectorCall4>(taken[4]);
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
      CuteQQmlFileSelectorCall5 call = reinterpret_cast<CuteQQmlFileSelectorCall5>(taken[5]);
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
      CuteQQmlFileSelectorCall6 call = reinterpret_cast<CuteQQmlFileSelectorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlFileSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlFileSelector10metaObjectEv(
    const QQmlFileSelector *self) {
  return self->metaObject();
}

//  QString QQmlFileSelector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlFileSelector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlFileSelector::tr(s, c, n));
}

//  QQmlFileSelectorPrivate *QQmlFileSelector::d_func()
extern "C" Q_DECL_EXPORT
QQmlFileSelectorPrivate *ritual_ZN16QQmlFileSelector6d_funcEv(
    QQmlFileSelector *self) {
  return self->d_func();
}

//  const QQmlFileSelectorPrivate *QQmlFileSelector::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlFileSelectorPrivate *ritual_ZNK16QQmlFileSelector6d_funcEv(
    const QQmlFileSelector *self) {
  return self->d_func();
}

//  QQmlFileSelector::QQmlFileSelector(QQmlEngine *engine, QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlFileSelector *ritual_ZN16QQmlFileSelectorC1EP10QQmlEngineP7QObject(
    QQmlEngine *engine,
    QObject *parent) {
  return new CuteQQmlFileSelector(engine, parent);
}

//  QQmlFileSelector::~QQmlFileSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlFileSelectorD1Ev(QQmlFileSelector *self) {
  delete self;
}

//  QFileSelector *QQmlFileSelector::selector() const
extern "C" Q_DECL_EXPORT
QFileSelector *ritual_ZNK16QQmlFileSelector8selectorEv(
    const QQmlFileSelector *self) {
  return self->selector();
}

//  void QQmlFileSelector::setSelector(QFileSelector *selector)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlFileSelector11setSelectorEP13QFileSelector(
    QQmlFileSelector *self,
    QFileSelector *selector) {
  self->setSelector(selector);
}

//  void QQmlFileSelector::setExtraSelectors(const QStringList &strings)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlFileSelector17setExtraSelectorsERK5QListI7QStringE(
    QQmlFileSelector *self,
    const QList<QString> *strings) {
  self->setExtraSelectors(*strings);
}

#if QT_DEPRECATED_SINCE(6, 0)
//  QQmlFileSelector *QQmlFileSelector::get(QQmlEngine *a0)
extern "C" Q_DECL_EXPORT
QQmlFileSelector *ritual_ZN16QQmlFileSelector3getEP10QQmlEngine(
    QQmlEngine *a0) {
  return QQmlFileSelector::get(a0);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

//  a Python function taken by a CuteQQmlFileSelector, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlFileSelector(
    QQmlFileSelector *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlFileSelector *>(self)->take(key, call);
}
