//  Written by dev_tooling.RitualGenerator from the records of
//  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
#include <QtTaskTree/qtasktree.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QtTaskTree::QTaskTree may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtTaskTree_QTaskTree : QtTaskTree::QTaskTree {
  using QtTaskTree::QTaskTree::event;
};

//  A QtTaskTree::QTaskTree that Python can take functions over in. Every QtTaskTree::QTaskTree
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QTaskTreeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtTaskTree_QTaskTreeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTaskTreeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTaskTreeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTaskTreeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTaskTreeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtTaskTree_QTaskTreeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtTaskTree_QTaskTree : public QtTaskTree::QTaskTree {
public:
  using QtTaskTree::QTaskTree::QTaskTree;
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
  //  bool QtTaskTree::QTaskTree::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtTaskTree_QTaskTreeCall0 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QtTaskTree::QTaskTree::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtTaskTree_QTaskTreeCall1 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall1>(taken[1]);
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
      CuteQtTaskTree_QTaskTreeCall2 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall2>(taken[2]);
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
      CuteQtTaskTree_QTaskTreeCall3 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall3>(taken[3]);
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
      CuteQtTaskTree_QTaskTreeCall4 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall4>(taken[4]);
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
      CuteQtTaskTree_QTaskTreeCall5 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall5>(taken[5]);
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
      CuteQtTaskTree_QTaskTreeCall6 call = reinterpret_cast<CuteQtTaskTree_QTaskTreeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtTaskTree::QTaskTree::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QtTaskTree9QTaskTree10metaObjectEv(
    const QtTaskTree::QTaskTree *self) {
  return self->metaObject();
}

//  QString QtTaskTree::QTaskTree::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QtTaskTree9QTaskTree2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtTaskTree::QTaskTree::tr(s, c, n));
}

//  QtTaskTree::QTaskTree::QTaskTree()
extern "C" Q_DECL_EXPORT
QtTaskTree::QTaskTree *ritual_ZN10QtTaskTree9QTaskTreeC1Ev() {
  return new CuteQtTaskTree_QTaskTree();
}

//  qsizetype QtTaskTree::QTaskTree::progressMaximum() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QtTaskTree9QTaskTree15progressMaximumEv(
    const QtTaskTree::QTaskTree *self) {
  return self->progressMaximum();
}

//  a Python function taken by a CuteQtTaskTree_QTaskTree, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtTaskTree_QTaskTree(
    QtTaskTree::QTaskTree *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtTaskTree_QTaskTree *>(self)->take(key, call);
}

//  bool QtTaskTree::QTaskTree::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QtTaskTree9QTaskTree5eventEP6QEvent(
    QtTaskTree::QTaskTree *self,
    QEvent *event) {
  return static_cast<OwnQtTaskTree_QTaskTree *>(self)->OwnQtTaskTree_QTaskTree::event(
      event);
}
