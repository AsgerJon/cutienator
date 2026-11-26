//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbuttongroup_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbuttongroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  Only a class built on QQuickButtonGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickButtonGroup : QQuickButtonGroup {
  using QQuickButtonGroup::classBegin;
  using QQuickButtonGroup::componentComplete;
};

//  A QQuickButtonGroup that Python can take functions over in. Every QQuickButtonGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickButtonGroupCall0)(const void *, int *);
typedef void (*CuteQQuickButtonGroupCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickButtonGroupCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickButtonGroupCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickButtonGroupCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickButtonGroupCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickButtonGroupCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickButtonGroupCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickButtonGroupCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickButtonGroup : public QQuickButtonGroup {
public:
  using QQuickButtonGroup::QQuickButtonGroup;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  void QQuickButtonGroup::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickButtonGroupCall0 call = reinterpret_cast<CuteQQuickButtonGroupCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickButtonGroup::classBegin();
  }

  //  void QQuickButtonGroup::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickButtonGroupCall1 call = reinterpret_cast<CuteQQuickButtonGroupCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickButtonGroup::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickButtonGroupCall2 call = reinterpret_cast<CuteQQuickButtonGroupCall2>(taken[2]);
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
      CuteQQuickButtonGroupCall3 call = reinterpret_cast<CuteQQuickButtonGroupCall3>(taken[3]);
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
      CuteQQuickButtonGroupCall4 call = reinterpret_cast<CuteQQuickButtonGroupCall4>(taken[4]);
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
      CuteQQuickButtonGroupCall5 call = reinterpret_cast<CuteQQuickButtonGroupCall5>(taken[5]);
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
      CuteQQuickButtonGroupCall6 call = reinterpret_cast<CuteQQuickButtonGroupCall6>(taken[6]);
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
      CuteQQuickButtonGroupCall7 call = reinterpret_cast<CuteQQuickButtonGroupCall7>(taken[7]);
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
      CuteQQuickButtonGroupCall8 call = reinterpret_cast<CuteQQuickButtonGroupCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickButtonGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickButtonGroup10metaObjectEv(
    const QQuickButtonGroup *self) {
  return self->metaObject();
}

//  void *QQuickButtonGroup::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickButtonGroup11qt_metacastEPKc(
    QQuickButtonGroup *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickButtonGroup::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickButtonGroup11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickButtonGroup *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickButtonGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickButtonGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickButtonGroup::tr(s, c, n));
}

//  void QQuickButtonGroup::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup21qt_qmlMarker_attachedEv(
    QQuickButtonGroup *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickButtonGroup::QQuickButtonGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickButtonGroup *ritual_ZN17QQuickButtonGroupC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickButtonGroup(parent);
}

//  QQuickButtonGroup::~QQuickButtonGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroupD1Ev(QQuickButtonGroup *self) {
  delete self;
}

//  QQuickButtonGroupAttached
//      *QQuickButtonGroup::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickButtonGroupAttached *ritual_ZN17QQuickButtonGroup21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickButtonGroup::qmlAttachedProperties(object);
}

//  QQuickAbstractButton *QQuickButtonGroup::checkedButton() const
extern "C" Q_DECL_EXPORT
QQuickAbstractButton *ritual_ZNK17QQuickButtonGroup13checkedButtonEv(
    const QQuickButtonGroup *self) {
  return self->checkedButton();
}

//  void QQuickButtonGroup::setCheckedButton(QQuickAbstractButton
//      *checkedButton)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup16setCheckedButtonEP20QQuickAbstractButton(
    QQuickButtonGroup *self,
    QQuickAbstractButton *checkedButton) {
  self->setCheckedButton(checkedButton);
}

//  QQmlListProperty<QQuickAbstractButton> QQuickButtonGroup::buttons()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickAbstractButton> *ritual_ZN17QQuickButtonGroup7buttonsEv(
    QQuickButtonGroup *self) {
  return new QQmlListProperty<QQuickAbstractButton>(self->buttons());
}

//  bool QQuickButtonGroup::isExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickButtonGroup11isExclusiveEv(
    const QQuickButtonGroup *self) {
  return self->isExclusive();
}

//  void QQuickButtonGroup::setExclusive(bool exclusive)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup12setExclusiveEb(
    QQuickButtonGroup *self,
    bool exclusive) {
  self->setExclusive(exclusive);
}

//  Qt::CheckState QQuickButtonGroup::checkState() const
extern "C" Q_DECL_EXPORT
Qt::CheckState ritual_ZNK17QQuickButtonGroup10checkStateEv(
    const QQuickButtonGroup *self) {
  return self->checkState();
}

//  void QQuickButtonGroup::setCheckState(Qt::CheckState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup13setCheckStateEN2Qt10CheckStateE(
    QQuickButtonGroup *self,
    Qt::CheckState state) {
  self->setCheckState(state);
}

//  void QQuickButtonGroup::addButton(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup9addButtonEP20QQuickAbstractButton(
    QQuickButtonGroup *self,
    QQuickAbstractButton *button) {
  self->addButton(button);
}

//  void QQuickButtonGroup::removeButton(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup12removeButtonEP20QQuickAbstractButton(
    QQuickButtonGroup *self,
    QQuickAbstractButton *button) {
  self->removeButton(button);
}

//  void QQuickButtonGroup::checkedButtonChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup20checkedButtonChangedEv(
    QQuickButtonGroup *self) {
  self->checkedButtonChanged();
}

//  void QQuickButtonGroup::buttonsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup14buttonsChangedEv(
    QQuickButtonGroup *self) {
  self->buttonsChanged();
}

//  void QQuickButtonGroup::clicked(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup7clickedEP20QQuickAbstractButton(
    QQuickButtonGroup *self,
    QQuickAbstractButton *button) {
  self->clicked(button);
}

//  void QQuickButtonGroup::exclusiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup16exclusiveChangedEv(
    QQuickButtonGroup *self) {
  self->exclusiveChanged();
}

//  void QQuickButtonGroup::checkStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup17checkStateChangedEv(
    QQuickButtonGroup *self) {
  self->checkStateChanged();
}

//  void QQuickButtonGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup10classBeginEv(QQuickButtonGroup *self) {
  self->classBegin();
}

//  void QQuickButtonGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickButtonGroup17componentCompleteEv(
    QQuickButtonGroup *self) {
  self->componentComplete();
}

//  QQuickButtonGroupPrivate *QQuickButtonGroup::d_func()
extern "C" Q_DECL_EXPORT
QQuickButtonGroupPrivate *ritual_ZN17QQuickButtonGroup6d_funcEv(
    QQuickButtonGroup *self) {
  return self->d_func();
}

//  const QQuickButtonGroupPrivate *QQuickButtonGroup::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickButtonGroupPrivate *ritual_ZNK17QQuickButtonGroup6d_funcEv(
    const QQuickButtonGroup *self) {
  return self->d_func();
}

//  QQuickButtonGroup as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickButtonGroup_QQmlParserStatus(
    QQuickButtonGroup *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickButtonGroup, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickButtonGroup(
    QQuickButtonGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickButtonGroup *>(self)->take(key, call);
}

//  void QQuickButtonGroup::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickButtonGroup10classBeginEv(
    QQuickButtonGroup *self) {
  static_cast<OwnQQuickButtonGroup *>(self)->OwnQQuickButtonGroup::classBegin();
}

//  void QQuickButtonGroup::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickButtonGroup17componentCompleteEv(
    QQuickButtonGroup *self) {
  static_cast<OwnQQuickButtonGroup *>(self)->OwnQQuickButtonGroup::componentComplete();
}

//  a QQmlListProperty<QQuickAbstractButton> a ritual of QQuickButtonGroup
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickButtonGroup__QQmlListProperty_QQuickAbstractButton(
    QQmlListProperty<QQuickAbstractButton> *self) {
  delete self;
}
