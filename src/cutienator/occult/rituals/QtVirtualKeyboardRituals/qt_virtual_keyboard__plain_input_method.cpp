//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/plaininputmethod_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/plaininputmethod_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <QtVirtualKeyboard/QVirtualKeyboardInputEngine>
#include <QtCore/QString>

//  A QtVirtualKeyboard::PlainInputMethod that Python can take functions over in. Every QtVirtualKeyboard::PlainInputMethod
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall0)(const void *, const QString *, int, int *);
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall1)(const void *, int, int *);
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall2)(const void *, int, const QString *, int, int *);
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall3)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall4)(const void *, int *);
typedef int (*CuteQtVirtualKeyboard_PlainInputMethodCall5)(const void *, int, int *);
typedef const QVariant * (*CuteQtVirtualKeyboard_PlainInputMethodCall6)(const void *, int, int, int, int *);
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall7)(const void *, int, int, int *);
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall8)(const void *, int, int, int *);
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall9)(const void *, QVirtualKeyboardTrace *, int *);
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall10)(const void *, int, int *);
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_PlainInputMethodCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_PlainInputMethodCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_PlainInputMethod : public QtVirtualKeyboard::PlainInputMethod {
public:
  using QtVirtualKeyboard::PlainInputMethod::PlainInputMethod;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod12setInputModeERK7QStringN27QVirtualKeyboardInputEngine9InputModeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod11setTextCaseEN27QVirtualKeyboardInputEngine8TextCaseE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod8keyEventEN2Qt3KeyERK7QString6QFlagsINS0_16KeyboardModifierEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod5resetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod6updateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod22selectionListItemCountEN34QVirtualKeyboardSelectionListModel4TypeE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod17selectionListDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod25selectionListItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemoveItemEN34QVirtualKeyboardSelectionListModel4TypeEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtualKeyboardTrace")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod14clearInputModeEv")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QtVirtualKeyboard::PlainInputMethod::setInputMode(const QString
  //      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
  bool setInputMode(
      const QString &locale,
      QVirtualKeyboardInputEngine::InputMode inputMode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall0>(taken[0]);
      bool given = call(this, &locale, static_cast<int>(inputMode), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlainInputMethod::setInputMode(locale, inputMode);
  }

  //  bool QtVirtualKeyboard::PlainInputMethod::setTextCase(QVirtualKeyboar
  //      dInputEngine::TextCase textCase)
  bool setTextCase(QVirtualKeyboardInputEngine::TextCase textCase) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall1>(taken[1]);
      bool given = call(this, static_cast<int>(textCase), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlainInputMethod::setTextCase(textCase);
  }

  //  bool QtVirtualKeyboard::PlainInputMethod::keyEvent(Qt::Key key, const
  //      QString &text, Qt::KeyboardModifiers modifiers)
  bool keyEvent(
      Qt::Key key,
      const QString &text,
      Qt::KeyboardModifiers modifiers) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall2>(taken[2]);
      bool given = call(this, static_cast<int>(key), &text, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::PlainInputMethod::keyEvent(key, text, modifiers);
  }

  //  void QtVirtualKeyboard::PlainInputMethod::reset()
  void reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlainInputMethod::reset();
  }

  //  void QtVirtualKeyboard::PlainInputMethod::update()
  void update() override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::PlainInputMethod::update();
  }

  //  int QVirtualKeyboardAbstractInputMethod::selectionListItemCount(QVirt
  //      ualKeyboardSelectionListModel::Type type)
  int selectionListItemCount(
      QVirtualKeyboardSelectionListModel::Type type) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall5>(taken[5]);
      int given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::selectionListItemCount(type);
  }

  //  QVariant QVirtualKeyboardAbstractInputMethod::selectionListData(QVirt
  //      ualKeyboardSelectionListModel::Type type, int index,
  //      QVirtualKeyboardSelectionListModel::Role role)
  QVariant selectionListData(
      QVirtualKeyboardSelectionListModel::Type type,
      int index,
      QVirtualKeyboardSelectionListModel::Role role) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall6>(taken[6]);
      const QVariant * given = call(this, static_cast<int>(type), index, static_cast<int>(role), &handled);
      if (handled && given) return *given;
    }
    return QVirtualKeyboardAbstractInputMethod::selectionListData(type, index, role);
  }

  //  void QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(Q
  //      VirtualKeyboardSelectionListModel::Type type, int index)
  void selectionListItemSelected(
      QVirtualKeyboardSelectionListModel::Type type,
      int index) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall7>(taken[7]);
      call(this, static_cast<int>(type), index, &handled);
      if (handled) return;
    }
    QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(type, index);
  }

  //  bool QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(QVi
  //      rtualKeyboardSelectionListModel::Type type, int index)
  bool selectionListRemoveItem(
      QVirtualKeyboardSelectionListModel::Type type,
      int index) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall8>(taken[8]);
      bool given = call(this, static_cast<int>(type), index, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(type, index);
  }

  //  bool
  //      QVirtualKeyboardAbstractInputMethod::traceEnd(QVirtualKeyboardTra
  //      ce *trace)
  bool traceEnd(QVirtualKeyboardTrace *trace) override {
    if (taken[9]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall9>(taken[9]);
      bool given = call(this, trace, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::traceEnd(trace);
  }

  //  bool QVirtualKeyboardAbstractInputMethod::clickPreeditText(int
  //      cursorPosition)
  bool clickPreeditText(int cursorPosition) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall10>(taken[10]);
      bool given = call(this, cursorPosition, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::clickPreeditText(cursorPosition);
  }

  //  void QVirtualKeyboardAbstractInputMethod::clearInputMode()
  void clearInputMode() override {
    if (taken[11]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QVirtualKeyboardAbstractInputMethod::clearInputMode();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall13 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall14 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall15 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall16 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall17 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQtVirtualKeyboard_PlainInputMethodCall18 call = reinterpret_cast<CuteQtVirtualKeyboard_PlainInputMethodCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::PlainInputMethod::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard16PlainInputMethod10metaObjectEv(
    const QtVirtualKeyboard::PlainInputMethod *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::PlainInputMethod::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard16PlainInputMethod11qt_metacastEPKc(
    QtVirtualKeyboard::PlainInputMethod *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::PlainInputMethod::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard16PlainInputMethod11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::PlainInputMethod *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::PlainInputMethod::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard16PlainInputMethod2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::PlainInputMethod::tr(s, c, n));
}

//  QtVirtualKeyboard::PlainInputMethod::PlainInputMethod(QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::PlainInputMethod *ritual_ZN17QtVirtualKeyboard16PlainInputMethodC1EP7QObject(
    QObject *parent) {
  return new CuteQtVirtualKeyboard_PlainInputMethod(parent);
}

//  QtVirtualKeyboard::PlainInputMethod::~PlainInputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard16PlainInputMethodD1Ev(
    QtVirtualKeyboard::PlainInputMethod *self) {
  delete self;
}

//  QList<QVirtualKeyboardInputEngine::InputMode>
//      QtVirtualKeyboard::PlainInputMethod::inputModes(const QString
//      &locale)
extern "C" Q_DECL_EXPORT
QList<QVirtualKeyboardInputEngine::InputMode> *ritual_ZN17QtVirtualKeyboard16PlainInputMethod10inputModesERK7QString(
    QtVirtualKeyboard::PlainInputMethod *self,
    const QString *locale) {
  return new QList<QVirtualKeyboardInputEngine::InputMode>(
      self->inputModes(
          *locale));
}

//  bool QtVirtualKeyboard::PlainInputMethod::setInputMode(const QString
//      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard16PlainInputMethod12setInputModeERK7QStringN27QVirtualKeyboardInputEngine9InputModeE(
    QtVirtualKeyboard::PlainInputMethod *self,
    const QString *locale,
    QVirtualKeyboardInputEngine::InputMode inputMode) {
  return self->setInputMode(*locale, inputMode);
}

//  bool QtVirtualKeyboard::PlainInputMethod::setTextCase(QVirtualKeyboardInp
//      utEngine::TextCase textCase)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard16PlainInputMethod11setTextCaseEN27QVirtualKeyboardInputEngine8TextCaseE(
    QtVirtualKeyboard::PlainInputMethod *self,
    QVirtualKeyboardInputEngine::TextCase textCase) {
  return self->setTextCase(textCase);
}

//  bool QtVirtualKeyboard::PlainInputMethod::keyEvent(Qt::Key key, const
//      QString &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard16PlainInputMethod8keyEventEN2Qt3KeyERK7QString6QFlagsINS1_16KeyboardModifierEE(
    QtVirtualKeyboard::PlainInputMethod *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->keyEvent(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  void QtVirtualKeyboard::PlainInputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard16PlainInputMethod5resetEv(
    QtVirtualKeyboard::PlainInputMethod *self) {
  self->reset();
}

//  void QtVirtualKeyboard::PlainInputMethod::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard16PlainInputMethod6updateEv(
    QtVirtualKeyboard::PlainInputMethod *self) {
  self->update();
}

//  a Python function taken by a CuteQtVirtualKeyboard_PlainInputMethod, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_PlainInputMethod(
    QtVirtualKeyboard::PlainInputMethod *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_PlainInputMethod *>(self)->take(key, call);
}

//  bool QtVirtualKeyboard::PlainInputMethod::setInputMode(const QString
//      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod12setInputModeERK7QStringN27QVirtualKeyboardInputEngine9InputModeE(
    QtVirtualKeyboard::PlainInputMethod *self,
    const QString *locale,
    QVirtualKeyboardInputEngine::InputMode inputMode) {
  return self->QtVirtualKeyboard::PlainInputMethod::setInputMode(
      *locale,
      inputMode);
}

//  bool QtVirtualKeyboard::PlainInputMethod::setTextCase(QVirtualKeyboardInp
//      utEngine::TextCase textCase)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod11setTextCaseEN27QVirtualKeyboardInputEngine8TextCaseE(
    QtVirtualKeyboard::PlainInputMethod *self,
    QVirtualKeyboardInputEngine::TextCase textCase) {
  return self->QtVirtualKeyboard::PlainInputMethod::setTextCase(textCase);
}

//  bool QtVirtualKeyboard::PlainInputMethod::keyEvent(Qt::Key key, const
//      QString &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod8keyEventEN2Qt3KeyERK7QString6QFlagsINS1_16KeyboardModifierEE(
    QtVirtualKeyboard::PlainInputMethod *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->QtVirtualKeyboard::PlainInputMethod::keyEvent(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  void QtVirtualKeyboard::PlainInputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod5resetEv(
    QtVirtualKeyboard::PlainInputMethod *self) {
  self->QtVirtualKeyboard::PlainInputMethod::reset();
}

//  void QtVirtualKeyboard::PlainInputMethod::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard16PlainInputMethod6updateEv(
    QtVirtualKeyboard::PlainInputMethod *self) {
  self->QtVirtualKeyboard::PlainInputMethod::update();
}

//  a QList<QVirtualKeyboardInputEngine::InputMode> a ritual of
//      QtVirtualKeyboard::PlainInputMethod gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtVirtualKeyboard_PlainInputMethod__QList_QVirtualKeyboardInputEngine_InputMode(
    QList<QVirtualKeyboardInputEngine::InputMode> *self) {
  delete self;
}
