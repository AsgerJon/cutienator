//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qactiongroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(action)
#if QT_CONFIG(action)
#include <QtGui/qactiongroup.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#if QT_CONFIG(action)
#include <QtGui/qaction.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QActionGroup that Python can take functions over in. Every QActionGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQActionGroupCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQActionGroupCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionGroupCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionGroupCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionGroupCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionGroupCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQActionGroupCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQActionGroup : public QActionGroup {
public:
  using QActionGroup::QActionGroup;
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
      CuteQActionGroupCall0 call = reinterpret_cast<CuteQActionGroupCall0>(taken[0]);
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
      CuteQActionGroupCall1 call = reinterpret_cast<CuteQActionGroupCall1>(taken[1]);
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
      CuteQActionGroupCall2 call = reinterpret_cast<CuteQActionGroupCall2>(taken[2]);
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
      CuteQActionGroupCall3 call = reinterpret_cast<CuteQActionGroupCall3>(taken[3]);
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
      CuteQActionGroupCall4 call = reinterpret_cast<CuteQActionGroupCall4>(taken[4]);
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
      CuteQActionGroupCall5 call = reinterpret_cast<CuteQActionGroupCall5>(taken[5]);
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
      CuteQActionGroupCall6 call = reinterpret_cast<CuteQActionGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QActionGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QActionGroup10metaObjectEv(
    const QActionGroup *self) {
  return self->metaObject();
}

//  void *QActionGroup::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QActionGroup11qt_metacastEPKc(
    QActionGroup *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QActionGroup::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QActionGroup11qt_metacallEN11QMetaObject4CallEiPPv(
    QActionGroup *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QActionGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QActionGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QActionGroup::tr(s, c, n));
}

//  QActionGroupPrivate *QActionGroup::d_func()
extern "C" Q_DECL_EXPORT
QActionGroupPrivate *ritual_ZN12QActionGroup6d_funcEv(QActionGroup *self) {
  return self->d_func();
}

//  const QActionGroupPrivate *QActionGroup::d_func() const
extern "C" Q_DECL_EXPORT
const QActionGroupPrivate *ritual_ZNK12QActionGroup6d_funcEv(
    const QActionGroup *self) {
  return self->d_func();
}

//  QActionGroup::QActionGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN12QActionGroupC1EP7QObject(QObject *parent) {
  return new CuteQActionGroup(parent);
}

//  QActionGroup::~QActionGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroupD1Ev(QActionGroup *self) {
  delete self;
}

//  QAction *QActionGroup::addAction(QAction *a)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QActionGroup9addActionEP7QAction(
    QActionGroup *self,
    QAction *a) {
  return self->addAction(a);
}

//  QAction *QActionGroup::addAction(const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QActionGroup9addActionERK7QString(
    QActionGroup *self,
    const QString *text) {
  return self->addAction(*text);
}

//  QAction *QActionGroup::addAction(const QIcon &icon, const QString &text)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN12QActionGroup9addActionERK5QIconRK7QString(
    QActionGroup *self,
    const QIcon *icon,
    const QString *text) {
  return self->addAction(*icon, *text);
}

//  void QActionGroup::removeAction(QAction *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup12removeActionEP7QAction(
    QActionGroup *self,
    QAction *a) {
  self->removeAction(a);
}

//  QList<QAction *> QActionGroup::actions() const
extern "C" Q_DECL_EXPORT
QList<QAction *> *ritual_ZNK12QActionGroup7actionsEv(
    const QActionGroup *self) {
  return new QList<QAction *>(self->actions());
}

//  QAction *QActionGroup::checkedAction() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK12QActionGroup13checkedActionEv(
    const QActionGroup *self) {
  return self->checkedAction();
}

//  bool QActionGroup::isExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QActionGroup11isExclusiveEv(const QActionGroup *self) {
  return self->isExclusive();
}

//  bool QActionGroup::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QActionGroup9isEnabledEv(const QActionGroup *self) {
  return self->isEnabled();
}

//  bool QActionGroup::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QActionGroup9isVisibleEv(const QActionGroup *self) {
  return self->isVisible();
}

//  ExclusionPolicy QActionGroup::exclusionPolicy() const
extern "C" Q_DECL_EXPORT
QActionGroup::ExclusionPolicy ritual_ZNK12QActionGroup15exclusionPolicyEv(
    const QActionGroup *self) {
  return self->exclusionPolicy();
}

//  void QActionGroup::setEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup10setEnabledEb(QActionGroup *self, bool a0) {
  self->setEnabled(a0);
}

//  void QActionGroup::setDisabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup11setDisabledEb(QActionGroup *self, bool b) {
  self->setDisabled(b);
}

//  void QActionGroup::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup10setVisibleEb(QActionGroup *self, bool a0) {
  self->setVisible(a0);
}

//  void QActionGroup::setExclusive(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup12setExclusiveEb(QActionGroup *self, bool a0) {
  self->setExclusive(a0);
}

//  void QActionGroup::setExclusionPolicy(ExclusionPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup18setExclusionPolicyENS_15ExclusionPolicyE(
    QActionGroup *self,
    QActionGroup::ExclusionPolicy policy) {
  self->setExclusionPolicy(policy);
}

//  void QActionGroup::triggered(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup9triggeredEP7QAction(
    QActionGroup *self,
    QAction *a0) {
  self->triggered(a0);
}

//  void QActionGroup::hovered(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup7hoveredEP7QAction(
    QActionGroup *self,
    QAction *a0) {
  self->hovered(a0);
}

//  void QActionGroup::_q_actionTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup18_q_actionTriggeredEv(QActionGroup *self) {
  self->_q_actionTriggered();
}

//  void QActionGroup::_q_actionHovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup16_q_actionHoveredEv(QActionGroup *self) {
  self->_q_actionHovered();
}

//  void QActionGroup::_q_actionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QActionGroup16_q_actionChangedEv(QActionGroup *self) {
  self->_q_actionChanged();
}

//  QActionGroup::QActionGroup(QActionGroupPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QActionGroup *ritual_ZN12QActionGroupC1ER19QActionGroupPrivateP7QObject(
    QActionGroupPrivate *dd,
    QObject *parent) {
  return new CuteQActionGroup(*dd, parent);
}

//  a Python function taken by a CuteQActionGroup, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QActionGroup(
    QActionGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQActionGroup *>(self)->take(key, call);
}

#endif  // QT_CONFIG(action)
#endif  // QT_CONFIG(action)
