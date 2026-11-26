//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativemargins_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativemargins_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A DeclarativeMargins that Python can take functions over in. Every DeclarativeMargins
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeMarginsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeMarginsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeMarginsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeMarginsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeMarginsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeMarginsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeMarginsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeMargins : public DeclarativeMargins {
public:
  using DeclarativeMargins::DeclarativeMargins;
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
      CuteDeclarativeMarginsCall0 call = reinterpret_cast<CuteDeclarativeMarginsCall0>(taken[0]);
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
      CuteDeclarativeMarginsCall1 call = reinterpret_cast<CuteDeclarativeMarginsCall1>(taken[1]);
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
      CuteDeclarativeMarginsCall2 call = reinterpret_cast<CuteDeclarativeMarginsCall2>(taken[2]);
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
      CuteDeclarativeMarginsCall3 call = reinterpret_cast<CuteDeclarativeMarginsCall3>(taken[3]);
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
      CuteDeclarativeMarginsCall4 call = reinterpret_cast<CuteDeclarativeMarginsCall4>(taken[4]);
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
      CuteDeclarativeMarginsCall5 call = reinterpret_cast<CuteDeclarativeMarginsCall5>(taken[5]);
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
      CuteDeclarativeMarginsCall6 call = reinterpret_cast<CuteDeclarativeMarginsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeMargins::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18DeclarativeMargins10metaObjectEv(
    const DeclarativeMargins *self) {
  return self->metaObject();
}

//  void *DeclarativeMargins::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18DeclarativeMargins11qt_metacastEPKc(
    DeclarativeMargins *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeMargins::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18DeclarativeMargins11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeMargins *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeMargins::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18DeclarativeMargins2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeMargins::tr(s, c, n));
}

//  void DeclarativeMargins::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins24qt_qmlMarker_uncreatableEv(
    DeclarativeMargins *self) {
  self->qt_qmlMarker_uncreatable();
}

//  DeclarativeMargins::DeclarativeMargins(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeMargins *ritual_ZN18DeclarativeMarginsC1EP7QObject(
    QObject *parent) {
  return new CuteDeclarativeMargins(parent);
}

//  void DeclarativeMargins::setTop(int top)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins6setTopEi(
    DeclarativeMargins *self,
    int top) {
  self->setTop(top);
}

//  void DeclarativeMargins::setBottom(int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins9setBottomEi(
    DeclarativeMargins *self,
    int bottom) {
  self->setBottom(bottom);
}

//  void DeclarativeMargins::setLeft(int left)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins7setLeftEi(
    DeclarativeMargins *self,
    int left) {
  self->setLeft(left);
}

//  void DeclarativeMargins::setRight(int right)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins8setRightEi(
    DeclarativeMargins *self,
    int right) {
  self->setRight(right);
}

//  void DeclarativeMargins::topChanged(int top, int bottom, int left, int
//      right)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins10topChangedEiiii(
    DeclarativeMargins *self,
    int top,
    int bottom,
    int left,
    int right) {
  self->topChanged(top, bottom, left, right);
}

//  void DeclarativeMargins::bottomChanged(int top, int bottom, int left, int
//      right)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins13bottomChangedEiiii(
    DeclarativeMargins *self,
    int top,
    int bottom,
    int left,
    int right) {
  self->bottomChanged(top, bottom, left, right);
}

//  void DeclarativeMargins::leftChanged(int top, int bottom, int left, int
//      right)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins11leftChangedEiiii(
    DeclarativeMargins *self,
    int top,
    int bottom,
    int left,
    int right) {
  self->leftChanged(top, bottom, left, right);
}

//  void DeclarativeMargins::rightChanged(int top, int bottom, int left, int
//      right)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DeclarativeMargins12rightChangedEiiii(
    DeclarativeMargins *self,
    int top,
    int bottom,
    int left,
    int right) {
  self->rightChanged(top, bottom, left, right);
}

//  DeclarativeMargins as the QMargins it is built on
extern "C" Q_DECL_EXPORT
QMargins *ritual_cast_DeclarativeMargins_QMargins(DeclarativeMargins *self) {
  return static_cast<QMargins *>(self);
}

//  a Python function taken by a CuteDeclarativeMargins, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeMargins(
    DeclarativeMargins *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeMargins *>(self)->take(key, call);
}
