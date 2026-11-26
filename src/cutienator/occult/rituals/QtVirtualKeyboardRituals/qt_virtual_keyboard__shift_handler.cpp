//  Written by hand on 2026-11-25 from
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shifthandler_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Left out: nothing. The constructor is private, and is written,
//  as private members may be named.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shifthandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtVirtualKeyboard::ShiftHandler that Python can take functions over in. Every QtVirtualKeyboard::ShiftHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_ShiftHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_ShiftHandlerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShiftHandlerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShiftHandlerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShiftHandlerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShiftHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShiftHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_ShiftHandler : public QtVirtualKeyboard::ShiftHandler {
public:
  using QtVirtualKeyboard::ShiftHandler::ShiftHandler;
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
      CuteQtVirtualKeyboard_ShiftHandlerCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall0>(taken[0]);
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
      CuteQtVirtualKeyboard_ShiftHandlerCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall1>(taken[1]);
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
      CuteQtVirtualKeyboard_ShiftHandlerCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall2>(taken[2]);
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
      CuteQtVirtualKeyboard_ShiftHandlerCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall3>(taken[3]);
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
      CuteQtVirtualKeyboard_ShiftHandlerCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall4>(taken[4]);
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
      CuteQtVirtualKeyboard_ShiftHandlerCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall5>(taken[5]);
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
      CuteQtVirtualKeyboard_ShiftHandlerCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_ShiftHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::ShiftHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard12ShiftHandler10metaObjectEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::ShiftHandler::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard12ShiftHandler2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::ShiftHandler::tr(s, c, n));
}

//  void QtVirtualKeyboard::ShiftHandler::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler24qt_qmlMarker_uncreatableEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->qt_qmlMarker_uncreatable();
}

//  void QtVirtualKeyboard::ShiftHandler::toggleShift()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler11toggleShiftEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->toggleShift();
}

//  QtVirtualKeyboard::ShiftHandler::ShiftHandler(QVirtualKeyboardInputContext
//      *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::ShiftHandler *ritual_ZN17QtVirtualKeyboard12ShiftHandlerC1EP28QVirtualKeyboardInputContext(
    QVirtualKeyboardInputContext *parent) {
  return new CuteQtVirtualKeyboard_ShiftHandler(parent);
}

//  void QtVirtualKeyboard::ShiftHandler::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler4initEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->init();
}

//  QtVirtualKeyboard::ShiftHandler::~ShiftHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandlerD1Ev(
    QtVirtualKeyboard::ShiftHandler *self) {
  delete self;
}

//  QString QtVirtualKeyboard::ShiftHandler::sentenceEndingCharacters() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QtVirtualKeyboard12ShiftHandler24sentenceEndingCharactersEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return new QString(self->sentenceEndingCharacters());
}

//  void QtVirtualKeyboard::ShiftHandler::setSentenceEndingCharacters(const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler27setSentenceEndingCharactersERK7QString(
    QtVirtualKeyboard::ShiftHandler *self,
    const QString *value) {
  self->setSentenceEndingCharacters(*value);
}

//  bool QtVirtualKeyboard::ShiftHandler::isAutoCapitalizationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard12ShiftHandler27isAutoCapitalizationEnabledEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->isAutoCapitalizationEnabled();
}

//  bool QtVirtualKeyboard::ShiftHandler::isToggleShiftEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard12ShiftHandler20isToggleShiftEnabledEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->isToggleShiftEnabled();
}

//  bool QtVirtualKeyboard::ShiftHandler::isShiftActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard12ShiftHandler13isShiftActiveEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->isShiftActive();
}

//  bool QtVirtualKeyboard::ShiftHandler::isCapsLockActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard12ShiftHandler16isCapsLockActiveEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->isCapsLockActive();
}

//  bool QtVirtualKeyboard::ShiftHandler::isUppercase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard12ShiftHandler11isUppercaseEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->isUppercase();
}

//  void QtVirtualKeyboard::ShiftHandler::setShiftActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler14setShiftActiveEb(
    QtVirtualKeyboard::ShiftHandler *self,
    bool active) {
  self->setShiftActive(active);
}

//  void QtVirtualKeyboard::ShiftHandler::setCapsLockActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler17setCapsLockActiveEb(
    QtVirtualKeyboard::ShiftHandler *self,
    bool active) {
  self->setCapsLockActive(active);
}

//  void QtVirtualKeyboard::ShiftHandler::clearToggleShiftTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler21clearToggleShiftTimerEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->clearToggleShiftTimer();
}

//  void QtVirtualKeyboard::ShiftHandler::sentenceEndingCharactersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler31sentenceEndingCharactersChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->sentenceEndingCharactersChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::toggleShiftEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler25toggleShiftEnabledChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->toggleShiftEnabledChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::autoCapitalizationEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler32autoCapitalizationEnabledChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->autoCapitalizationEnabledChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::shiftActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler18shiftActiveChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->shiftActiveChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::capsLockActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler21capsLockActiveChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->capsLockActiveChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::uppercaseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler16uppercaseChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->uppercaseChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler5resetEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->reset();
}

//  void QtVirtualKeyboard::ShiftHandler::autoCapitalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler14autoCapitalizeEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->autoCapitalize();
}

//  void QtVirtualKeyboard::ShiftHandler::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler7restartEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->restart();
}

//  void QtVirtualKeyboard::ShiftHandler::localeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler13localeChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->localeChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::inputMethodVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler25inputMethodVisibleChangedEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  self->inputMethodVisibleChanged();
}

//  void QtVirtualKeyboard::ShiftHandler::setAutoCapitalizationEnabled(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler28setAutoCapitalizationEnabledEb(
    QtVirtualKeyboard::ShiftHandler *self,
    bool enabled) {
  self->setAutoCapitalizationEnabled(enabled);
}

//  void QtVirtualKeyboard::ShiftHandler::setToggleShiftEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard12ShiftHandler21setToggleShiftEnabledEb(
    QtVirtualKeyboard::ShiftHandler *self,
    bool enabled) {
  self->setToggleShiftEnabled(enabled);
}

//  QtVirtualKeyboard::ShiftHandlerPrivate
//      *QtVirtualKeyboard::ShiftHandler::d_func()
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::ShiftHandlerPrivate *ritual_ZN17QtVirtualKeyboard12ShiftHandler6d_funcEv(
    QtVirtualKeyboard::ShiftHandler *self) {
  return self->d_func();
}

//  const QtVirtualKeyboard::ShiftHandlerPrivate
//      *QtVirtualKeyboard::ShiftHandler::d_func() const
extern "C" Q_DECL_EXPORT
const QtVirtualKeyboard::ShiftHandlerPrivate *ritual_ZNK17QtVirtualKeyboard12ShiftHandler6d_funcEv(
    const QtVirtualKeyboard::ShiftHandler *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtVirtualKeyboard_ShiftHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_ShiftHandler(
    QtVirtualKeyboard::ShiftHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_ShiftHandler *>(self)->take(key, call);
}
