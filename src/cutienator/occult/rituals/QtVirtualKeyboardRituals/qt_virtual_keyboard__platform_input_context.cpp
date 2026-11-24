//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/platforminputcontext_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/platforminputcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtVirtualKeyboard::PlatformInputContext that Python can take functions over in. Every QtVirtualKeyboard::PlatformInputContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall0)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall1)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall2)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall3)(const void *, int, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall4)(const void *, int, int, int *);
typedef const QRectF * (*CuteQtVirtualKeyboard_PlatformInputContextCall5)(const void *, int *);
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall6)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall7)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall8)(const void *, int *);
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall9)(const void *, int *);
typedef const QLocale * (*CuteQtVirtualKeyboard_PlatformInputContextCall10)(const void *, int *);
typedef int (*CuteQtVirtualKeyboard_PlatformInputContextCall11)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall12)(const void *, QObject *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall14)(const void *, int, int *);
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall15)(const void *, const QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_PlatformInputContextCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlatformInputContextCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_PlatformInputContext : public QtVirtualKeyboard::PlatformInputContext {
public:
  using QtVirtualKeyboard::PlatformInputContext::PlatformInputContext;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext5resetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext6commitEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQueryEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext12invokeActionEN12QInputMethod6ActionEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext12keyboardRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext11isAnimatingEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext14showInputPanelEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext14hideInputPanelEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext19isInputPanelVisibleEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext6localeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext14inputDirectionEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext14setFocusObjectEP7QObject")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK21QPlatformInputContext13hasCapabilityENS_10CapabilityE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformInputContext11filterEventEPK6QEvent")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QtVirtualKeyboard::PlatformInputContext::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlatformInputContext::isValid();
  }

  //  void QtVirtualKeyboard::PlatformInputContext::reset()
  void reset() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::reset();
  }

  //  void QtVirtualKeyboard::PlatformInputContext::commit()
  void commit() override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::commit();
  }

  //  void QtVirtualKeyboard::PlatformInputContext::update(Qt::InputMethodQ
  //      ueries queries)
  void update(Qt::InputMethodQueries queries) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall3>(taken[3]);
      call(this, static_cast<int>(queries.toInt()), &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::update(queries);
  }

  //  void QtVirtualKeyboard::PlatformInputContext::invokeAction(QInputMeth
  //      od::Action action, int cursorPosition)
  void invokeAction(
      QInputMethod::Action action,
      int cursorPosition) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall4>(taken[4]);
      call(this, static_cast<int>(action), cursorPosition, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::invokeAction(action, cursorPosition);
  }

  //  QRectF QtVirtualKeyboard::PlatformInputContext::keyboardRect() const
  QRectF keyboardRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QtVirtualKeyboard::PlatformInputContext::keyboardRect();
  }

  //  bool QtVirtualKeyboard::PlatformInputContext::isAnimating() const
  bool isAnimating() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlatformInputContext::isAnimating();
  }

  //  void QtVirtualKeyboard::PlatformInputContext::showInputPanel()
  void showInputPanel() override {
    if (taken[7]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::showInputPanel();
  }

  //  void QtVirtualKeyboard::PlatformInputContext::hideInputPanel()
  void hideInputPanel() override {
    if (taken[8]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::hideInputPanel();
  }

  //  bool QtVirtualKeyboard::PlatformInputContext::isInputPanelVisible()
  //      const
  bool isInputPanelVisible() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlatformInputContext::isInputPanelVisible();
  }

  //  QLocale QtVirtualKeyboard::PlatformInputContext::locale() const
  QLocale locale() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall10>(taken[10]);
      const QLocale * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QtVirtualKeyboard::PlatformInputContext::locale();
  }

  //  Qt::LayoutDirection
  //      QtVirtualKeyboard::PlatformInputContext::inputDirection() const
  Qt::LayoutDirection inputDirection() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::LayoutDirection>(given);
    }
    return QtVirtualKeyboard::PlatformInputContext::inputDirection();
  }

  //  void QtVirtualKeyboard::PlatformInputContext::setFocusObject(QObject
  //      *object)
  void setFocusObject(QObject *object) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall12>(taken[12]);
      call(this, object, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlatformInputContext::setFocusObject(object);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QtVirtualKeyboard::PlatformInputContext::eventFilter(QObject
  //      *object, QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall13 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall13>(taken[13]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlatformInputContext::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  bool QPlatformInputContext::hasCapability(Capability capability)
  //      const
  bool hasCapability(
      QPlatformInputContext::Capability capability) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall14 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall14>(taken[14]);
      bool given = call(this, static_cast<int>(capability), &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::hasCapability(capability);
  }

  //  bool QPlatformInputContext::filterEvent(const QEvent *event)
  bool filterEvent(const QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall15 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QPlatformInputContext::filterEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall16 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall17 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall18 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall19 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall20 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlatformInputContextCall21 call = reinterpret_cast<CuteQtVirtualKeyboard_PlatformInputContextCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::PlatformInputContext::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard20PlatformInputContext10metaObjectEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::PlatformInputContext::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard20PlatformInputContext2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::PlatformInputContext::tr(s, c, n));
}

//  a Python function taken by a CuteQtVirtualKeyboard_PlatformInputContext,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_PlatformInputContext(
    QtVirtualKeyboard::PlatformInputContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_PlatformInputContext *>(self)->take(key, call);
}

//  bool QtVirtualKeyboard::PlatformInputContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext7isValidEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return self->QtVirtualKeyboard::PlatformInputContext::isValid();
}

//  void QtVirtualKeyboard::PlatformInputContext::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext5resetEv(
    QtVirtualKeyboard::PlatformInputContext *self) {
  self->QtVirtualKeyboard::PlatformInputContext::reset();
}

//  void QtVirtualKeyboard::PlatformInputContext::commit()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext6commitEv(
    QtVirtualKeyboard::PlatformInputContext *self) {
  self->QtVirtualKeyboard::PlatformInputContext::commit();
}

//  void
//      QtVirtualKeyboard::PlatformInputContext::update(Qt::InputMethodQuerie
//      s queries)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QtVirtualKeyboard::PlatformInputContext *self,
    int queries) {
  self->QtVirtualKeyboard::PlatformInputContext::update(
      QFlags<Qt::InputMethodQuery>::fromInt(queries));
}

//  void QtVirtualKeyboard::PlatformInputContext::invokeAction(QInputMethod::
//      Action action, int cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext12invokeActionEN12QInputMethod6ActionEi(
    QtVirtualKeyboard::PlatformInputContext *self,
    QInputMethod::Action action,
    int cursorPosition) {
  self->QtVirtualKeyboard::PlatformInputContext::invokeAction(
      action,
      cursorPosition);
}

//  QRectF QtVirtualKeyboard::PlatformInputContext::keyboardRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext12keyboardRectEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return new QRectF(
      self->QtVirtualKeyboard::PlatformInputContext::keyboardRect());
}

//  bool QtVirtualKeyboard::PlatformInputContext::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext11isAnimatingEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return self->QtVirtualKeyboard::PlatformInputContext::isAnimating();
}

//  void QtVirtualKeyboard::PlatformInputContext::showInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext14showInputPanelEv(
    QtVirtualKeyboard::PlatformInputContext *self) {
  self->QtVirtualKeyboard::PlatformInputContext::showInputPanel();
}

//  void QtVirtualKeyboard::PlatformInputContext::hideInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext14hideInputPanelEv(
    QtVirtualKeyboard::PlatformInputContext *self) {
  self->QtVirtualKeyboard::PlatformInputContext::hideInputPanel();
}

//  bool QtVirtualKeyboard::PlatformInputContext::isInputPanelVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext19isInputPanelVisibleEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return self->QtVirtualKeyboard::PlatformInputContext::isInputPanelVisible();
}

//  QLocale QtVirtualKeyboard::PlatformInputContext::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext6localeEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return new QLocale(
      self->QtVirtualKeyboard::PlatformInputContext::locale());
}

//  Qt::LayoutDirection
//      QtVirtualKeyboard::PlatformInputContext::inputDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_own_ZNK17QtVirtualKeyboard20PlatformInputContext14inputDirectionEv(
    const QtVirtualKeyboard::PlatformInputContext *self) {
  return self->QtVirtualKeyboard::PlatformInputContext::inputDirection();
}

//  void QtVirtualKeyboard::PlatformInputContext::setFocusObject(QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext14setFocusObjectEP7QObject(
    QtVirtualKeyboard::PlatformInputContext *self,
    QObject *object) {
  self->QtVirtualKeyboard::PlatformInputContext::setFocusObject(object);
}

//  bool QtVirtualKeyboard::PlatformInputContext::eventFilter(QObject
//      *object, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard20PlatformInputContext11eventFilterEP7QObjectP6QEvent(
    QtVirtualKeyboard::PlatformInputContext *self,
    QObject *object,
    QEvent *event) {
  return self->QtVirtualKeyboard::PlatformInputContext::eventFilter(
      object,
      event);
}
