//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qaction.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DInput/qaction.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DInput/Qt3DInput>

//  A Qt3DInput::QAction that Python can take functions over in. Every Qt3DInput::QAction
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QActionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QActionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QActionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QAction : public Qt3DInput::QAction {
public:
  using Qt3DInput::QAction::QAction;
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
      CuteQt3DInput_QActionCall0 call = reinterpret_cast<CuteQt3DInput_QActionCall0>(taken[0]);
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
      CuteQt3DInput_QActionCall1 call = reinterpret_cast<CuteQt3DInput_QActionCall1>(taken[1]);
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
      CuteQt3DInput_QActionCall2 call = reinterpret_cast<CuteQt3DInput_QActionCall2>(taken[2]);
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
      CuteQt3DInput_QActionCall3 call = reinterpret_cast<CuteQt3DInput_QActionCall3>(taken[3]);
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
      CuteQt3DInput_QActionCall4 call = reinterpret_cast<CuteQt3DInput_QActionCall4>(taken[4]);
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
      CuteQt3DInput_QActionCall5 call = reinterpret_cast<CuteQt3DInput_QActionCall5>(taken[5]);
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
      CuteQt3DInput_QActionCall6 call = reinterpret_cast<CuteQt3DInput_QActionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QAction::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput7QAction10metaObjectEv(
    const Qt3DInput::QAction *self) {
  return self->metaObject();
}

//  void *Qt3DInput::QAction::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput7QAction11qt_metacastEPKc(
    Qt3DInput::QAction *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QAction::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput7QAction11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QAction *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QAction::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput7QAction2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QAction::tr(s, c, n));
}

//  Qt3DInput::QAction::QAction(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAction *ritual_ZN9Qt3DInput7QActionC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DInput_QAction(parent);
}

//  Qt3DInput::QAction::~QAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput7QActionD1Ev(Qt3DInput::QAction *self) {
  delete self;
}

//  bool Qt3DInput::QAction::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput7QAction8isActiveEv(
    const Qt3DInput::QAction *self) {
  return self->isActive();
}

//  void Qt3DInput::QAction::addInput(QAbstractActionInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput7QAction8addInputEPNS_20QAbstractActionInputE(
    Qt3DInput::QAction *self,
    Qt3DInput::QAbstractActionInput *input) {
  self->addInput(input);
}

//  void Qt3DInput::QAction::removeInput(QAbstractActionInput *input)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput7QAction11removeInputEPNS_20QAbstractActionInputE(
    Qt3DInput::QAction *self,
    Qt3DInput::QAbstractActionInput *input) {
  self->removeInput(input);
}

//  QList<QAbstractActionInput *> Qt3DInput::QAction::inputs() const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QAbstractActionInput *> *ritual_ZNK9Qt3DInput7QAction6inputsEv(
    const Qt3DInput::QAction *self) {
  return new QList<Qt3DInput::QAbstractActionInput *>(self->inputs());
}

//  void Qt3DInput::QAction::activeChanged(bool isActive)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput7QAction13activeChangedEb(
    Qt3DInput::QAction *self,
    bool isActive) {
  self->activeChanged(isActive);
}

//  QActionPrivate *Qt3DInput::QAction::d_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QActionPrivate *ritual_ZN9Qt3DInput7QAction6d_funcEv(
    Qt3DInput::QAction *self) {
  return self->d_func();
}

//  const QActionPrivate *Qt3DInput::QAction::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QActionPrivate *ritual_ZNK9Qt3DInput7QAction6d_funcEv(
    const Qt3DInput::QAction *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DInput_QAction, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAction(
    Qt3DInput::QAction *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAction *>(self)->take(key, call);
}

//  a QList<Qt3DInput::QAbstractActionInput *> a ritual of Qt3DInput::QAction
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_QAction__QList_Qt3DInput_QAbstractActionInput(
    QList<Qt3DInput::QAbstractActionInput *> *self) {
  delete self;
}
