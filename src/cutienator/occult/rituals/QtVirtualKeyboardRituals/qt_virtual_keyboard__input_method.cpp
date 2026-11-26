//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputmethod_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/inputmethod_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QList>
#include <QtVirtualKeyboard/QVirtualKeyboardInputEngine>
#include <QtCore/QString>
#include <QtVirtualKeyboard/QVirtualKeyboardSelectionListModel>

//  A QtVirtualKeyboard::InputMethod that Python can take functions over in. Every QtVirtualKeyboard::InputMethod
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall0)(const void *, const QString *, int, int *);
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall1)(const void *, int, int *);
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall2)(const void *, int, const QString *, int, int *);
typedef int (*CuteQtVirtualKeyboard_InputMethodCall3)(const void *, int, int *);
typedef const QVariant * (*CuteQtVirtualKeyboard_InputMethodCall4)(const void *, int, int, int, int *);
typedef void (*CuteQtVirtualKeyboard_InputMethodCall5)(const void *, int, int, int *);
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall6)(const void *, QVirtualKeyboardTrace *, int *);
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall7)(const void *, int, int *);
typedef void (*CuteQtVirtualKeyboard_InputMethodCall8)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_InputMethodCall9)(const void *, int *);
typedef void (*CuteQtVirtualKeyboard_InputMethodCall10)(const void *, int *);
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall11)(const void *, int, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_InputMethodCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputMethodCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputMethodCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputMethodCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputMethodCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_InputMethodCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_InputMethod : public QtVirtualKeyboard::InputMethod {
public:
  using QtVirtualKeyboard::InputMethod::InputMethod;
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
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod22selectionListItemCountEN34QVirtualKeyboardSelectionListModel4TypeE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod17selectionListDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod25selectionListItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtualKeyboardTrace")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod5resetEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod6updateEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod14clearInputModeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemoveItemEN34QVirtualKeyboardSelectionListModel4TypeEi")) {
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

  //  bool QtVirtualKeyboard::InputMethod::setInputMode(const QString
  //      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
  bool setInputMode(
      const QString &locale,
      QVirtualKeyboardInputEngine::InputMode inputMode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall0>(taken[0]);
      bool given = call(this, &locale, static_cast<int>(inputMode), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::InputMethod::setInputMode(locale, inputMode);
  }

  //  bool QtVirtualKeyboard::InputMethod::setTextCase(QVirtualKeyboardInpu
  //      tEngine::TextCase textCase)
  bool setTextCase(QVirtualKeyboardInputEngine::TextCase textCase) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall1>(taken[1]);
      bool given = call(this, static_cast<int>(textCase), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::InputMethod::setTextCase(textCase);
  }

  //  bool QtVirtualKeyboard::InputMethod::keyEvent(Qt::Key key, const
  //      QString &text, Qt::KeyboardModifiers modifiers)
  bool keyEvent(
      Qt::Key key,
      const QString &text,
      Qt::KeyboardModifiers modifiers) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall2>(taken[2]);
      bool given = call(this, static_cast<int>(key), &text, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::InputMethod::keyEvent(key, text, modifiers);
  }

  //  int QtVirtualKeyboard::InputMethod::selectionListItemCount(QVirtualKe
  //      yboardSelectionListModel::Type type)
  int selectionListItemCount(
      QVirtualKeyboardSelectionListModel::Type type) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall3>(taken[3]);
      int given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::InputMethod::selectionListItemCount(type);
  }

  //  QVariant QtVirtualKeyboard::InputMethod::selectionListData(QVirtualKe
  //      yboardSelectionListModel::Type type, int index,
  //      QVirtualKeyboardSelectionListModel::Role role)
  QVariant selectionListData(
      QVirtualKeyboardSelectionListModel::Type type,
      int index,
      QVirtualKeyboardSelectionListModel::Role role) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(type), index, static_cast<int>(role), &handled);
      if (handled && given) return *given;
    }
    return QtVirtualKeyboard::InputMethod::selectionListData(type, index, role);
  }

  //  void QtVirtualKeyboard::InputMethod::selectionListItemSelected(QVirtu
  //      alKeyboardSelectionListModel::Type type, int index)
  void selectionListItemSelected(
      QVirtualKeyboardSelectionListModel::Type type,
      int index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall5>(taken[5]);
      call(this, static_cast<int>(type), index, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::InputMethod::selectionListItemSelected(type, index);
  }

  //  bool QtVirtualKeyboard::InputMethod::traceEnd(QVirtualKeyboardTrace
  //      *trace)
  bool traceEnd(QVirtualKeyboardTrace *trace) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall6>(taken[6]);
      bool given = call(this, trace, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::InputMethod::traceEnd(trace);
  }

  //  bool QtVirtualKeyboard::InputMethod::clickPreeditText(int
  //      cursorPosition)
  bool clickPreeditText(int cursorPosition) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall7 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall7>(taken[7]);
      bool given = call(this, cursorPosition, &handled);
      if (handled) return given;
    }
    return QtVirtualKeyboard::InputMethod::clickPreeditText(cursorPosition);
  }

  //  void QtVirtualKeyboard::InputMethod::reset()
  void reset() override {
    if (taken[8]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall8 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::InputMethod::reset();
  }

  //  void QtVirtualKeyboard::InputMethod::update()
  void update() override {
    if (taken[9]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall9 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::InputMethod::update();
  }

  //  void QtVirtualKeyboard::InputMethod::clearInputMode()
  void clearInputMode() override {
    if (taken[10]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall10 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QtVirtualKeyboard::InputMethod::clearInputMode();
  }

  //  bool QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(QVi
  //      rtualKeyboardSelectionListModel::Type type, int index)
  bool selectionListRemoveItem(
      QVirtualKeyboardSelectionListModel::Type type,
      int index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall11 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall11>(taken[11]);
      bool given = call(this, static_cast<int>(type), index, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(type, index);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQtVirtualKeyboard_InputMethodCall12 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall12>(taken[12]);
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
      CuteQtVirtualKeyboard_InputMethodCall13 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall13>(taken[13]);
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
      CuteQtVirtualKeyboard_InputMethodCall14 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall14>(taken[14]);
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
      CuteQtVirtualKeyboard_InputMethodCall15 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall15>(taken[15]);
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
      CuteQtVirtualKeyboard_InputMethodCall16 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall16>(taken[16]);
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
      CuteQtVirtualKeyboard_InputMethodCall17 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall17>(taken[17]);
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
      CuteQtVirtualKeyboard_InputMethodCall18 call = reinterpret_cast<CuteQtVirtualKeyboard_InputMethodCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::InputMethod::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard11InputMethod10metaObjectEv(
    const QtVirtualKeyboard::InputMethod *self) {
  return self->metaObject();
}

//  void *QtVirtualKeyboard::InputMethod::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QtVirtualKeyboard11InputMethod11qt_metacastEPKc(
    QtVirtualKeyboard::InputMethod *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtVirtualKeyboard::InputMethod::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard11InputMethod11qt_metacallEN11QMetaObject4CallEiPPv(
    QtVirtualKeyboard::InputMethod *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtVirtualKeyboard::InputMethod::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard11InputMethod2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::InputMethod::tr(s, c, n));
}

//  InputMethodPrivate *QtVirtualKeyboard::InputMethod::d_func()
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::InputMethodPrivate *ritual_ZN17QtVirtualKeyboard11InputMethod6d_funcEv(
    QtVirtualKeyboard::InputMethod *self) {
  return self->d_func();
}

//  const InputMethodPrivate *QtVirtualKeyboard::InputMethod::d_func() const
extern "C" Q_DECL_EXPORT
const QtVirtualKeyboard::InputMethodPrivate *ritual_ZNK17QtVirtualKeyboard11InputMethod6d_funcEv(
    const QtVirtualKeyboard::InputMethod *self) {
  return self->d_func();
}

//  QtVirtualKeyboard::InputMethod::InputMethod(QObject *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::InputMethod *ritual_ZN17QtVirtualKeyboard11InputMethodC1EP7QObject(
    QObject *parent) {
  return new CuteQtVirtualKeyboard_InputMethod(parent);
}

//  QtVirtualKeyboard::InputMethod::~InputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11InputMethodD1Ev(
    QtVirtualKeyboard::InputMethod *self) {
  delete self;
}

//  QList<QVirtualKeyboardInputEngine::InputMode>
//      QtVirtualKeyboard::InputMethod::inputModes(const QString &locale)
extern "C" Q_DECL_EXPORT
QList<QVirtualKeyboardInputEngine::InputMode> *ritual_ZN17QtVirtualKeyboard11InputMethod10inputModesERK7QString(
    QtVirtualKeyboard::InputMethod *self,
    const QString *locale) {
  return new QList<QVirtualKeyboardInputEngine::InputMode>(
      self->inputModes(
          *locale));
}

//  bool QtVirtualKeyboard::InputMethod::setInputMode(const QString &locale,
//      QVirtualKeyboardInputEngine::InputMode inputMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard11InputMethod12setInputModeERK7QStringN27QVirtualKeyboardInputEngine9InputModeE(
    QtVirtualKeyboard::InputMethod *self,
    const QString *locale,
    QVirtualKeyboardInputEngine::InputMode inputMode) {
  return self->setInputMode(*locale, inputMode);
}

//  bool QtVirtualKeyboard::InputMethod::setTextCase(QVirtualKeyboardInputEng
//      ine::TextCase textCase)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard11InputMethod11setTextCaseEN27QVirtualKeyboardInputEngine8TextCaseE(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardInputEngine::TextCase textCase) {
  return self->setTextCase(textCase);
}

//  bool QtVirtualKeyboard::InputMethod::keyEvent(Qt::Key key, const QString
//      &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard11InputMethod8keyEventEN2Qt3KeyERK7QString6QFlagsINS1_16KeyboardModifierEE(
    QtVirtualKeyboard::InputMethod *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->keyEvent(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QList<QVirtualKeyboardSelectionListModel::Type>
//      QtVirtualKeyboard::InputMethod::selectionLists()
extern "C" Q_DECL_EXPORT
QList<QVirtualKeyboardSelectionListModel::Type> *ritual_ZN17QtVirtualKeyboard11InputMethod14selectionListsEv(
    QtVirtualKeyboard::InputMethod *self) {
  return new QList<QVirtualKeyboardSelectionListModel::Type>(
      self->selectionLists());
}

//  int QtVirtualKeyboard::InputMethod::selectionListItemCount(QVirtualKeyboa
//      rdSelectionListModel::Type type)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QtVirtualKeyboard11InputMethod22selectionListItemCountEN34QVirtualKeyboardSelectionListModel4TypeE(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type) {
  return self->selectionListItemCount(type);
}

//  QVariant QtVirtualKeyboard::InputMethod::selectionListData(QVirtualKeyboa
//      rdSelectionListModel::Type type, int index,
//      QVirtualKeyboardSelectionListModel::Role role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QtVirtualKeyboard11InputMethod17selectionListDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS1_4RoleE(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index,
    QVirtualKeyboardSelectionListModel::Role role) {
  return new QVariant(self->selectionListData(type, index, role));
}

//  void QtVirtualKeyboard::InputMethod::selectionListItemSelected(QVirtualKe
//      yboardSelectionListModel::Type type, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11InputMethod25selectionListItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index) {
  self->selectionListItemSelected(type, index);
}

//  QList<QVirtualKeyboardInputEngine::PatternRecognitionMode>
//      QtVirtualKeyboard::InputMethod::patternRecognitionModes() const
extern "C" Q_DECL_EXPORT
QList<QVirtualKeyboardInputEngine::PatternRecognitionMode> *ritual_ZNK17QtVirtualKeyboard11InputMethod23patternRecognitionModesEv(
    const QtVirtualKeyboard::InputMethod *self) {
  return new QList<QVirtualKeyboardInputEngine::PatternRecognitionMode>(
      self->patternRecognitionModes());
}

//  QVirtualKeyboardTrace *QtVirtualKeyboard::InputMethod::traceBegin(int
//      traceId, QVirtualKeyboardInputEngine::PatternRecognitionMode
//      patternRecognitionMode, const QVariantMap &traceCaptureDeviceInfo,
//      const QVariantMap &traceScreenInfo)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardTrace *ritual_ZN17QtVirtualKeyboard11InputMethod10traceBeginEiN27QVirtualKeyboardInputEngine22PatternRecognitionModeERK4QMapI7QString8QVariantES8_(
    QtVirtualKeyboard::InputMethod *self,
    int traceId,
    QVirtualKeyboardInputEngine::PatternRecognitionMode patternRecognitionMode,
    const QMap<QString, QVariant> *traceCaptureDeviceInfo,
    const QMap<QString, QVariant> *traceScreenInfo) {
  return self->traceBegin(
      traceId,
      patternRecognitionMode,
      *traceCaptureDeviceInfo,
      *traceScreenInfo);
}

//  bool QtVirtualKeyboard::InputMethod::traceEnd(QVirtualKeyboardTrace
//      *trace)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard11InputMethod8traceEndEP21QVirtualKeyboardTrace(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardTrace *trace) {
  return self->traceEnd(trace);
}

//  bool QtVirtualKeyboard::InputMethod::reselect(int cursorPosition, const
//      QVirtualKeyboardInputEngine::ReselectFlags &reselectFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard11InputMethod8reselectEiRK6QFlagsIN27QVirtualKeyboardInputEngine12ReselectFlagEE(
    QtVirtualKeyboard::InputMethod *self,
    int cursorPosition,
    const QVirtualKeyboardInputEngine::ReselectFlags *reselectFlags) {
  return self->reselect(cursorPosition, *reselectFlags);
}

//  bool QtVirtualKeyboard::InputMethod::clickPreeditText(int cursorPosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtVirtualKeyboard11InputMethod16clickPreeditTextEi(
    QtVirtualKeyboard::InputMethod *self,
    int cursorPosition) {
  return self->clickPreeditText(cursorPosition);
}

//  void QtVirtualKeyboard::InputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11InputMethod5resetEv(
    QtVirtualKeyboard::InputMethod *self) {
  self->reset();
}

//  void QtVirtualKeyboard::InputMethod::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11InputMethod6updateEv(
    QtVirtualKeyboard::InputMethod *self) {
  self->update();
}

//  void QtVirtualKeyboard::InputMethod::clearInputMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard11InputMethod14clearInputModeEv(
    QtVirtualKeyboard::InputMethod *self) {
  self->clearInputMode();
}

//  a Python function taken by a CuteQtVirtualKeyboard_InputMethod, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_InputMethod(
    QtVirtualKeyboard::InputMethod *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_InputMethod *>(self)->take(key, call);
}

//  bool QtVirtualKeyboard::InputMethod::setInputMode(const QString &locale,
//      QVirtualKeyboardInputEngine::InputMode inputMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard11InputMethod12setInputModeERK7QStringN27QVirtualKeyboardInputEngine9InputModeE(
    QtVirtualKeyboard::InputMethod *self,
    const QString *locale,
    QVirtualKeyboardInputEngine::InputMode inputMode) {
  return self->QtVirtualKeyboard::InputMethod::setInputMode(
      *locale,
      inputMode);
}

//  bool QtVirtualKeyboard::InputMethod::setTextCase(QVirtualKeyboardInputEng
//      ine::TextCase textCase)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard11InputMethod11setTextCaseEN27QVirtualKeyboardInputEngine8TextCaseE(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardInputEngine::TextCase textCase) {
  return self->QtVirtualKeyboard::InputMethod::setTextCase(textCase);
}

//  bool QtVirtualKeyboard::InputMethod::keyEvent(Qt::Key key, const QString
//      &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard11InputMethod8keyEventEN2Qt3KeyERK7QString6QFlagsINS1_16KeyboardModifierEE(
    QtVirtualKeyboard::InputMethod *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->QtVirtualKeyboard::InputMethod::keyEvent(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  int QtVirtualKeyboard::InputMethod::selectionListItemCount(QVirtualKeyboa
//      rdSelectionListModel::Type type)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN17QtVirtualKeyboard11InputMethod22selectionListItemCountEN34QVirtualKeyboardSelectionListModel4TypeE(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type) {
  return self->QtVirtualKeyboard::InputMethod::selectionListItemCount(type);
}

//  QVariant QtVirtualKeyboard::InputMethod::selectionListData(QVirtualKeyboa
//      rdSelectionListModel::Type type, int index,
//      QVirtualKeyboardSelectionListModel::Role role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QtVirtualKeyboard11InputMethod17selectionListDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS1_4RoleE(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index,
    QVirtualKeyboardSelectionListModel::Role role) {
  return new QVariant(
      self->QtVirtualKeyboard::InputMethod::selectionListData(
          type,
          index,
          role));
}

//  void QtVirtualKeyboard::InputMethod::selectionListItemSelected(QVirtualKe
//      yboardSelectionListModel::Type type, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard11InputMethod25selectionListItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index) {
  self->QtVirtualKeyboard::InputMethod::selectionListItemSelected(
      type,
      index);
}

//  bool QtVirtualKeyboard::InputMethod::traceEnd(QVirtualKeyboardTrace
//      *trace)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard11InputMethod8traceEndEP21QVirtualKeyboardTrace(
    QtVirtualKeyboard::InputMethod *self,
    QVirtualKeyboardTrace *trace) {
  return self->QtVirtualKeyboard::InputMethod::traceEnd(trace);
}

//  bool QtVirtualKeyboard::InputMethod::clickPreeditText(int cursorPosition)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QtVirtualKeyboard11InputMethod16clickPreeditTextEi(
    QtVirtualKeyboard::InputMethod *self,
    int cursorPosition) {
  return self->QtVirtualKeyboard::InputMethod::clickPreeditText(
      cursorPosition);
}

//  void QtVirtualKeyboard::InputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard11InputMethod5resetEv(
    QtVirtualKeyboard::InputMethod *self) {
  self->QtVirtualKeyboard::InputMethod::reset();
}

//  void QtVirtualKeyboard::InputMethod::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard11InputMethod6updateEv(
    QtVirtualKeyboard::InputMethod *self) {
  self->QtVirtualKeyboard::InputMethod::update();
}

//  void QtVirtualKeyboard::InputMethod::clearInputMode()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QtVirtualKeyboard11InputMethod14clearInputModeEv(
    QtVirtualKeyboard::InputMethod *self) {
  self->QtVirtualKeyboard::InputMethod::clearInputMode();
}

//  a QList<QVirtualKeyboardInputEngine::InputMode> a ritual of
//      QtVirtualKeyboard::InputMethod gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtVirtualKeyboard_InputMethod__QList_QVirtualKeyboardInputEngine_InputMode(
    QList<QVirtualKeyboardInputEngine::InputMode> *self) {
  delete self;
}

//  a QList<QVirtualKeyboardSelectionListModel::Type> a ritual of
//      QtVirtualKeyboard::InputMethod gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtVirtualKeyboard_InputMethod__QList_QVirtualKeyboardSelectionListModel_Type(
    QList<QVirtualKeyboardSelectionListModel::Type> *self) {
  delete self;
}

//  a QList<QVirtualKeyboardInputEngine::PatternRecognitionMode> a ritual of
//      QtVirtualKeyboard::InputMethod gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtVirtualKeyboard_InputMethod__QList_QVirtualKeyboardInputEngine_PatternRecognitionMode(
    QList<QVirtualKeyboardInputEngine::PatternRecognitionMode> *self) {
  delete self;
}
