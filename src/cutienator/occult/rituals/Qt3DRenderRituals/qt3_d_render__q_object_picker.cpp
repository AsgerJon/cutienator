//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qobjectpicker.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qobjectpicker.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QObjectPicker that Python can take functions over in. Every Qt3DRender::QObjectPicker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QObjectPickerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QObjectPickerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QObjectPickerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QObjectPickerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QObjectPickerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QObjectPickerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QObjectPickerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QObjectPicker : public Qt3DRender::QObjectPicker {
public:
  using Qt3DRender::QObjectPicker::QObjectPicker;
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
      CuteQt3DRender_QObjectPickerCall0 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall0>(taken[0]);
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
      CuteQt3DRender_QObjectPickerCall1 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall1>(taken[1]);
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
      CuteQt3DRender_QObjectPickerCall2 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall2>(taken[2]);
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
      CuteQt3DRender_QObjectPickerCall3 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall3>(taken[3]);
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
      CuteQt3DRender_QObjectPickerCall4 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall4>(taken[4]);
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
      CuteQt3DRender_QObjectPickerCall5 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall5>(taken[5]);
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
      CuteQt3DRender_QObjectPickerCall6 call = reinterpret_cast<CuteQt3DRender_QObjectPickerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QObjectPicker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender13QObjectPicker10metaObjectEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QObjectPicker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender13QObjectPicker11qt_metacastEPKc(
    Qt3DRender::QObjectPicker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QObjectPicker::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender13QObjectPicker11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QObjectPicker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QObjectPicker::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QObjectPicker2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QObjectPicker::tr(s, c, n));
}

//  Qt3DRender::QObjectPicker::QObjectPicker(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QObjectPicker *ritual_ZN10Qt3DRender13QObjectPickerC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QObjectPicker(parent);
}

//  Qt3DRender::QObjectPicker::~QObjectPicker()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPickerD1Ev(
    Qt3DRender::QObjectPicker *self) {
  delete self;
}

//  bool Qt3DRender::QObjectPicker::isHoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QObjectPicker14isHoverEnabledEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->isHoverEnabled();
}

//  bool Qt3DRender::QObjectPicker::isDragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QObjectPicker13isDragEnabledEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->isDragEnabled();
}

//  bool Qt3DRender::QObjectPicker::containsMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QObjectPicker13containsMouseEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->containsMouse();
}

//  bool Qt3DRender::QObjectPicker::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QObjectPicker9isPressedEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->isPressed();
}

//  int Qt3DRender::QObjectPicker::priority() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender13QObjectPicker8priorityEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->priority();
}

//  void Qt3DRender::QObjectPicker::setHoverEnabled(bool hoverEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker15setHoverEnabledEb(
    Qt3DRender::QObjectPicker *self,
    bool hoverEnabled) {
  self->setHoverEnabled(hoverEnabled);
}

//  void Qt3DRender::QObjectPicker::setDragEnabled(bool dragEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker14setDragEnabledEb(
    Qt3DRender::QObjectPicker *self,
    bool dragEnabled) {
  self->setDragEnabled(dragEnabled);
}

//  void Qt3DRender::QObjectPicker::setPriority(int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker11setPriorityEi(
    Qt3DRender::QObjectPicker *self,
    int priority) {
  self->setPriority(priority);
}

//  void Qt3DRender::QObjectPicker::pressed(Qt3DRender::QPickEvent *pick)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker7pressedEPNS_10QPickEventE(
    Qt3DRender::QObjectPicker *self,
    Qt3DRender::QPickEvent *pick) {
  self->pressed(pick);
}

//  void Qt3DRender::QObjectPicker::released(Qt3DRender::QPickEvent *pick)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker8releasedEPNS_10QPickEventE(
    Qt3DRender::QObjectPicker *self,
    Qt3DRender::QPickEvent *pick) {
  self->released(pick);
}

//  void Qt3DRender::QObjectPicker::clicked(Qt3DRender::QPickEvent *pick)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker7clickedEPNS_10QPickEventE(
    Qt3DRender::QObjectPicker *self,
    Qt3DRender::QPickEvent *pick) {
  self->clicked(pick);
}

//  void Qt3DRender::QObjectPicker::moved(Qt3DRender::QPickEvent *pick)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker5movedEPNS_10QPickEventE(
    Qt3DRender::QObjectPicker *self,
    Qt3DRender::QPickEvent *pick) {
  self->moved(pick);
}

//  void Qt3DRender::QObjectPicker::entered()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker7enteredEv(
    Qt3DRender::QObjectPicker *self) {
  self->entered();
}

//  void Qt3DRender::QObjectPicker::exited()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker6exitedEv(
    Qt3DRender::QObjectPicker *self) {
  self->exited();
}

//  void Qt3DRender::QObjectPicker::hoverEnabledChanged(bool hoverEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker19hoverEnabledChangedEb(
    Qt3DRender::QObjectPicker *self,
    bool hoverEnabled) {
  self->hoverEnabledChanged(hoverEnabled);
}

//  void Qt3DRender::QObjectPicker::dragEnabledChanged(bool dragEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker18dragEnabledChangedEb(
    Qt3DRender::QObjectPicker *self,
    bool dragEnabled) {
  self->dragEnabledChanged(dragEnabled);
}

//  void Qt3DRender::QObjectPicker::pressedChanged(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker14pressedChangedEb(
    Qt3DRender::QObjectPicker *self,
    bool pressed) {
  self->pressedChanged(pressed);
}

//  void Qt3DRender::QObjectPicker::containsMouseChanged(bool containsMouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker20containsMouseChangedEb(
    Qt3DRender::QObjectPicker *self,
    bool containsMouse) {
  self->containsMouseChanged(containsMouse);
}

//  void Qt3DRender::QObjectPicker::priorityChanged(int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QObjectPicker15priorityChangedEi(
    Qt3DRender::QObjectPicker *self,
    int priority) {
  self->priorityChanged(priority);
}

//  QObjectPickerPrivate *Qt3DRender::QObjectPicker::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QObjectPickerPrivate *ritual_ZN10Qt3DRender13QObjectPicker6d_funcEv(
    Qt3DRender::QObjectPicker *self) {
  return self->d_func();
}

//  const QObjectPickerPrivate *Qt3DRender::QObjectPicker::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QObjectPickerPrivate *ritual_ZNK10Qt3DRender13QObjectPicker6d_funcEv(
    const Qt3DRender::QObjectPicker *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QObjectPicker, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QObjectPicker(
    Qt3DRender::QObjectPicker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QObjectPicker *>(self)->take(key, call);
}
