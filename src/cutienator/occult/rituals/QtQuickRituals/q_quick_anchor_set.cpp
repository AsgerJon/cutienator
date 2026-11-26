//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlscriptstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickAnchorSet that Python can take functions over in. Every QQuickAnchorSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnchorSetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnchorSetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorSetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorSetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorSetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorSetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnchorSetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickAnchorSet : public QQuickAnchorSet {
public:
  using QQuickAnchorSet::QQuickAnchorSet;
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
      CuteQQuickAnchorSetCall0 call = reinterpret_cast<CuteQQuickAnchorSetCall0>(taken[0]);
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
      CuteQQuickAnchorSetCall1 call = reinterpret_cast<CuteQQuickAnchorSetCall1>(taken[1]);
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
      CuteQQuickAnchorSetCall2 call = reinterpret_cast<CuteQQuickAnchorSetCall2>(taken[2]);
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
      CuteQQuickAnchorSetCall3 call = reinterpret_cast<CuteQQuickAnchorSetCall3>(taken[3]);
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
      CuteQQuickAnchorSetCall4 call = reinterpret_cast<CuteQQuickAnchorSetCall4>(taken[4]);
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
      CuteQQuickAnchorSetCall5 call = reinterpret_cast<CuteQQuickAnchorSetCall5>(taken[5]);
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
      CuteQQuickAnchorSetCall6 call = reinterpret_cast<CuteQQuickAnchorSetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickAnchorSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickAnchorSet10metaObjectEv(
    const QQuickAnchorSet *self) {
  return self->metaObject();
}

//  void *QQuickAnchorSet::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickAnchorSet11qt_metacastEPKc(
    QQuickAnchorSet *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAnchorSet::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickAnchorSet11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAnchorSet *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickAnchorSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickAnchorSet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAnchorSet::tr(s, c, n));
}

//  void QQuickAnchorSet::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet22qt_qmlMarker_anonymousEv(
    QQuickAnchorSet *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickAnchorSet::QQuickAnchorSet(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickAnchorSet *ritual_ZN15QQuickAnchorSetC1EP7QObject(QObject *parent) {
  return new CuteQQuickAnchorSet(parent);
}

//  QQuickAnchorSet::~QQuickAnchorSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSetD1Ev(QQuickAnchorSet *self) {
  delete self;
}

//  QQmlScriptString QQuickAnchorSet::left() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet4leftEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->left());
}

//  void QQuickAnchorSet::setLeft(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet7setLeftERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setLeft(*edge);
}

//  void QQuickAnchorSet::resetLeft()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet9resetLeftEv(QQuickAnchorSet *self) {
  self->resetLeft();
}

//  QQmlScriptString QQuickAnchorSet::right() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet5rightEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->right());
}

//  void QQuickAnchorSet::setRight(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet8setRightERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setRight(*edge);
}

//  void QQuickAnchorSet::resetRight()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet10resetRightEv(QQuickAnchorSet *self) {
  self->resetRight();
}

//  QQmlScriptString QQuickAnchorSet::horizontalCenter() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet16horizontalCenterEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->horizontalCenter());
}

//  void QQuickAnchorSet::setHorizontalCenter(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet19setHorizontalCenterERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setHorizontalCenter(*edge);
}

//  void QQuickAnchorSet::resetHorizontalCenter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet21resetHorizontalCenterEv(
    QQuickAnchorSet *self) {
  self->resetHorizontalCenter();
}

//  QQmlScriptString QQuickAnchorSet::top() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet3topEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->top());
}

//  void QQuickAnchorSet::setTop(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet6setTopERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setTop(*edge);
}

//  void QQuickAnchorSet::resetTop()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet8resetTopEv(QQuickAnchorSet *self) {
  self->resetTop();
}

//  QQmlScriptString QQuickAnchorSet::bottom() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet6bottomEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->bottom());
}

//  void QQuickAnchorSet::setBottom(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet9setBottomERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setBottom(*edge);
}

//  void QQuickAnchorSet::resetBottom()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet11resetBottomEv(QQuickAnchorSet *self) {
  self->resetBottom();
}

//  QQmlScriptString QQuickAnchorSet::verticalCenter() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet14verticalCenterEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->verticalCenter());
}

//  void QQuickAnchorSet::setVerticalCenter(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet17setVerticalCenterERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setVerticalCenter(*edge);
}

//  void QQuickAnchorSet::resetVerticalCenter()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet19resetVerticalCenterEv(
    QQuickAnchorSet *self) {
  self->resetVerticalCenter();
}

//  QQmlScriptString QQuickAnchorSet::baseline() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK15QQuickAnchorSet8baselineEv(
    const QQuickAnchorSet *self) {
  return new QQmlScriptString(self->baseline());
}

//  void QQuickAnchorSet::setBaseline(const QQmlScriptString &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet11setBaselineERK16QQmlScriptString(
    QQuickAnchorSet *self,
    const QQmlScriptString *edge) {
  self->setBaseline(*edge);
}

//  void QQuickAnchorSet::resetBaseline()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickAnchorSet13resetBaselineEv(QQuickAnchorSet *self) {
  self->resetBaseline();
}

//  QQuickAnchorSetPrivate *QQuickAnchorSet::d_func()
extern "C" Q_DECL_EXPORT
QQuickAnchorSetPrivate *ritual_ZN15QQuickAnchorSet6d_funcEv(
    QQuickAnchorSet *self) {
  return self->d_func();
}

//  const QQuickAnchorSetPrivate *QQuickAnchorSet::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnchorSetPrivate *ritual_ZNK15QQuickAnchorSet6d_funcEv(
    const QQuickAnchorSet *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickAnchorSet, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnchorSet(
    QQuickAnchorSet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnchorSet *>(self)->take(key, call);
}
