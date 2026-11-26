//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickindicatorbutton_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickindicatorbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickIndicatorButton that Python can take functions over in. Every QQuickIndicatorButton
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickIndicatorButtonCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickIndicatorButtonCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIndicatorButtonCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIndicatorButtonCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIndicatorButtonCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIndicatorButtonCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickIndicatorButtonCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickIndicatorButton : public QQuickIndicatorButton {
public:
  using QQuickIndicatorButton::QQuickIndicatorButton;
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
      CuteQQuickIndicatorButtonCall0 call = reinterpret_cast<CuteQQuickIndicatorButtonCall0>(taken[0]);
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
      CuteQQuickIndicatorButtonCall1 call = reinterpret_cast<CuteQQuickIndicatorButtonCall1>(taken[1]);
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
      CuteQQuickIndicatorButtonCall2 call = reinterpret_cast<CuteQQuickIndicatorButtonCall2>(taken[2]);
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
      CuteQQuickIndicatorButtonCall3 call = reinterpret_cast<CuteQQuickIndicatorButtonCall3>(taken[3]);
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
      CuteQQuickIndicatorButtonCall4 call = reinterpret_cast<CuteQQuickIndicatorButtonCall4>(taken[4]);
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
      CuteQQuickIndicatorButtonCall5 call = reinterpret_cast<CuteQQuickIndicatorButtonCall5>(taken[5]);
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
      CuteQQuickIndicatorButtonCall6 call = reinterpret_cast<CuteQQuickIndicatorButtonCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickIndicatorButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickIndicatorButton10metaObjectEv(
    const QQuickIndicatorButton *self) {
  return self->metaObject();
}

//  void *QQuickIndicatorButton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickIndicatorButton11qt_metacastEPKc(
    QQuickIndicatorButton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickIndicatorButton::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickIndicatorButton11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickIndicatorButton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickIndicatorButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickIndicatorButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickIndicatorButton::tr(s, c, n));
}

//  void QQuickIndicatorButton::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton22qt_qmlMarker_anonymousEv(
    QQuickIndicatorButton *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickIndicatorButton::QQuickIndicatorButton(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickIndicatorButton *ritual_ZN21QQuickIndicatorButtonC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickIndicatorButton(parent);
}

//  QQuickIndicatorButton::~QQuickIndicatorButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButtonD1Ev(QQuickIndicatorButton *self) {
  delete self;
}

//  bool QQuickIndicatorButton::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickIndicatorButton9isPressedEv(
    const QQuickIndicatorButton *self) {
  return self->isPressed();
}

//  void QQuickIndicatorButton::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton10setPressedEb(
    QQuickIndicatorButton *self,
    bool pressed) {
  self->setPressed(pressed);
}

//  QQuickItem *QQuickIndicatorButton::indicator() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickIndicatorButton9indicatorEv(
    const QQuickIndicatorButton *self) {
  return self->indicator();
}

//  void QQuickIndicatorButton::setIndicator(QQuickItem *indicator)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton12setIndicatorEP10QQuickItem(
    QQuickIndicatorButton *self,
    QQuickItem *indicator) {
  self->setIndicator(indicator);
}

//  bool QQuickIndicatorButton::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickIndicatorButton9isHoveredEv(
    const QQuickIndicatorButton *self) {
  return self->isHovered();
}

//  void QQuickIndicatorButton::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton10setHoveredEb(
    QQuickIndicatorButton *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  qreal QQuickIndicatorButton::implicitIndicatorWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickIndicatorButton22implicitIndicatorWidthEv(
    const QQuickIndicatorButton *self) {
  return self->implicitIndicatorWidth();
}

//  qreal QQuickIndicatorButton::implicitIndicatorHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickIndicatorButton23implicitIndicatorHeightEv(
    const QQuickIndicatorButton *self) {
  return self->implicitIndicatorHeight();
}

//  void QQuickIndicatorButton::pressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton14pressedChangedEv(
    QQuickIndicatorButton *self) {
  self->pressedChanged();
}

//  void QQuickIndicatorButton::indicatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton16indicatorChangedEv(
    QQuickIndicatorButton *self) {
  self->indicatorChanged();
}

//  void QQuickIndicatorButton::hoveredChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton14hoveredChangedEv(
    QQuickIndicatorButton *self) {
  self->hoveredChanged();
}

//  void QQuickIndicatorButton::implicitIndicatorWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton29implicitIndicatorWidthChangedEv(
    QQuickIndicatorButton *self) {
  self->implicitIndicatorWidthChanged();
}

//  void QQuickIndicatorButton::implicitIndicatorHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickIndicatorButton30implicitIndicatorHeightChangedEv(
    QQuickIndicatorButton *self) {
  self->implicitIndicatorHeightChanged();
}

//  QQuickIndicatorButtonPrivate *QQuickIndicatorButton::d_func()
extern "C" Q_DECL_EXPORT
QQuickIndicatorButtonPrivate *ritual_ZN21QQuickIndicatorButton6d_funcEv(
    QQuickIndicatorButton *self) {
  return self->d_func();
}

//  const QQuickIndicatorButtonPrivate *QQuickIndicatorButton::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickIndicatorButtonPrivate *ritual_ZNK21QQuickIndicatorButton6d_funcEv(
    const QQuickIndicatorButton *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickIndicatorButton, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickIndicatorButton(
    QQuickIndicatorButton *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickIndicatorButton *>(self)->take(key, call);
}
