//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboardabstractinputmethod.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboardabstractinputmethod.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QVirtualKeyboardAbstractInputMethod that Python can take functions over in. Every QVirtualKeyboardAbstractInputMethod
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall0)(const void *, const QString *, int, int *);
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall1)(const void *, int, int *);
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall2)(const void *, int, const QString *, int, int *);
typedef int (*CuteQVirtualKeyboardAbstractInputMethodCall3)(const void *, int, int *);
typedef const QVariant * (*CuteQVirtualKeyboardAbstractInputMethodCall4)(const void *, int, int, int, int *);
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall5)(const void *, int, int, int *);
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall6)(const void *, int, int, int *);
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall7)(const void *, QVirtualKeyboardTrace *, int *);
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall8)(const void *, int, int *);
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall9)(const void *, int *);
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall10)(const void *, int *);
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall11)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardAbstractInputMethodCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardAbstractInputMethodCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVirtualKeyboardAbstractInputMethod : public QVirtualKeyboardAbstractInputMethod {
public:
  using QVirtualKeyboardAbstractInputMethod::QVirtualKeyboardAbstractInputMethod;
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
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemoveItemEN34QVirtualKeyboardSelectionListModel4TypeEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtualKeyboardTrace")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod5resetEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN35QVirtualKeyboardAbstractInputMethod6updateEv")) {
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

  //  bool QVirtualKeyboardAbstractInputMethod::setInputMode(const QString
  //      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
  bool setInputMode(
      const QString &locale,
      QVirtualKeyboardInputEngine::InputMode inputMode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall0 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall0>(taken[0]);
      bool given = call(this, &locale, static_cast<int>(inputMode), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QVirtualKeyboardAbstractInputMethod::setTextCase(QVirtualKeyboar
  //      dInputEngine::TextCase textCase)
  bool setTextCase(QVirtualKeyboardInputEngine::TextCase textCase) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall1 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall1>(taken[1]);
      bool given = call(this, static_cast<int>(textCase), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QVirtualKeyboardAbstractInputMethod::keyEvent(Qt::Key key, const
  //      QString &text, Qt::KeyboardModifiers modifiers)
  bool keyEvent(
      Qt::Key key,
      const QString &text,
      Qt::KeyboardModifiers modifiers) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall2 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall2>(taken[2]);
      bool given = call(this, static_cast<int>(key), &text, static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QVirtualKeyboardAbstractInputMethod::selectionListItemCount(QVirt
  //      ualKeyboardSelectionListModel::Type type)
  int selectionListItemCount(
      QVirtualKeyboardSelectionListModel::Type type) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall3 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall4 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall5 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall6 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall6>(taken[6]);
      bool given = call(this, static_cast<int>(type), index, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(type, index);
  }

  //  bool
  //      QVirtualKeyboardAbstractInputMethod::traceEnd(QVirtualKeyboardTra
  //      ce *trace)
  bool traceEnd(QVirtualKeyboardTrace *trace) override {
    if (taken[7]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall7 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall7>(taken[7]);
      bool given = call(this, trace, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::traceEnd(trace);
  }

  //  bool QVirtualKeyboardAbstractInputMethod::clickPreeditText(int
  //      cursorPosition)
  bool clickPreeditText(int cursorPosition) override {
    if (taken[8]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall8 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall8>(taken[8]);
      bool given = call(this, cursorPosition, &handled);
      if (handled) return given;
    }
    return QVirtualKeyboardAbstractInputMethod::clickPreeditText(cursorPosition);
  }

  //  void QVirtualKeyboardAbstractInputMethod::reset()
  void reset() override {
    if (taken[9]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall9 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QVirtualKeyboardAbstractInputMethod::reset();
  }

  //  void QVirtualKeyboardAbstractInputMethod::update()
  void update() override {
    if (taken[10]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall10 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QVirtualKeyboardAbstractInputMethod::update();
  }

  //  void QVirtualKeyboardAbstractInputMethod::clearInputMode()
  void clearInputMode() override {
    if (taken[11]) {
      int handled = 0;
      CuteQVirtualKeyboardAbstractInputMethodCall11 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall11>(taken[11]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall12 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall12>(taken[12]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall13 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall13>(taken[13]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall14 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall14>(taken[14]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall15 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall15>(taken[15]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall16 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall16>(taken[16]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall17 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall17>(taken[17]);
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
      CuteQVirtualKeyboardAbstractInputMethodCall18 call = reinterpret_cast<CuteQVirtualKeyboardAbstractInputMethodCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVirtualKeyboardAbstractInputMethod::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK35QVirtualKeyboardAbstractInputMethod10metaObjectEv(
    const QVirtualKeyboardAbstractInputMethod *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardAbstractInputMethod::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN35QVirtualKeyboardAbstractInputMethod2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardAbstractInputMethod::tr(s, c, n));
}

//  QVirtualKeyboardAbstractInputMethodPrivate
//      *QVirtualKeyboardAbstractInputMethod::d_func()
extern "C" Q_DECL_EXPORT
QVirtualKeyboardAbstractInputMethodPrivate *ritual_ZN35QVirtualKeyboardAbstractInputMethod6d_funcEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  return self->d_func();
}

//  const QVirtualKeyboardAbstractInputMethodPrivate
//      *QVirtualKeyboardAbstractInputMethod::d_func() const
extern "C" Q_DECL_EXPORT
const QVirtualKeyboardAbstractInputMethodPrivate *ritual_ZNK35QVirtualKeyboardAbstractInputMethod6d_funcEv(
    const QVirtualKeyboardAbstractInputMethod *self) {
  return self->d_func();
}

//  void QVirtualKeyboardAbstractInputMethod::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethod22qt_qmlMarker_anonymousEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->qt_qmlMarker_anonymous();
}

//  QVirtualKeyboardAbstractInputMethod::~QVirtualKeyboardAbstractInputMethod
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethodD1Ev(
    QVirtualKeyboardAbstractInputMethod *self) {
  delete self;
}

//  QVirtualKeyboardInputContext
//      *QVirtualKeyboardAbstractInputMethod::inputContext() const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContext *ritual_ZNK35QVirtualKeyboardAbstractInputMethod12inputContextEv(
    const QVirtualKeyboardAbstractInputMethod *self) {
  return self->inputContext();
}

//  QVirtualKeyboardInputEngine
//      *QVirtualKeyboardAbstractInputMethod::inputEngine() const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputEngine *ritual_ZNK35QVirtualKeyboardAbstractInputMethod11inputEngineEv(
    const QVirtualKeyboardAbstractInputMethod *self) {
  return self->inputEngine();
}

//  bool QVirtualKeyboardAbstractInputMethod::setInputMode(const QString
//      &locale, QVirtualKeyboardInputEngine::InputMode inputMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardAbstractInputMethod12setInputModeERK7QStringN27QVirtualKeyboardInputEngine9InputModeE(
    QVirtualKeyboardAbstractInputMethod *self,
    const QString *locale,
    QVirtualKeyboardInputEngine::InputMode inputMode) {
  return self->setInputMode(*locale, inputMode);
}

//  bool QVirtualKeyboardAbstractInputMethod::setTextCase(QVirtualKeyboardInp
//      utEngine::TextCase textCase)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardAbstractInputMethod11setTextCaseEN27QVirtualKeyboardInputEngine8TextCaseE(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardInputEngine::TextCase textCase) {
  return self->setTextCase(textCase);
}

//  bool QVirtualKeyboardAbstractInputMethod::keyEvent(Qt::Key key, const
//      QString &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardAbstractInputMethod8keyEventEN2Qt3KeyERK7QString6QFlagsINS0_16KeyboardModifierEE(
    QVirtualKeyboardAbstractInputMethod *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->keyEvent(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  int QVirtualKeyboardAbstractInputMethod::selectionListItemCount(QVirtualK
//      eyboardSelectionListModel::Type type)
extern "C" Q_DECL_EXPORT
int ritual_ZN35QVirtualKeyboardAbstractInputMethod22selectionListItemCountEN34QVirtualKeyboardSelectionListModel4TypeE(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type) {
  return self->selectionListItemCount(type);
}

//  QVariant QVirtualKeyboardAbstractInputMethod::selectionListData(QVirtualK
//      eyboardSelectionListModel::Type type, int index,
//      QVirtualKeyboardSelectionListModel::Role role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN35QVirtualKeyboardAbstractInputMethod17selectionListDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index,
    QVirtualKeyboardSelectionListModel::Role role) {
  return new QVariant(self->selectionListData(type, index, role));
}

//  void QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(QVirt
//      ualKeyboardSelectionListModel::Type type, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethod25selectionListItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index) {
  self->selectionListItemSelected(type, index);
}

//  bool QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(QVirtua
//      lKeyboardSelectionListModel::Type type, int index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemoveItemEN34QVirtualKeyboardSelectionListModel4TypeEi(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index) {
  return self->selectionListRemoveItem(type, index);
}

//  QVirtualKeyboardTrace
//      *QVirtualKeyboardAbstractInputMethod::traceBegin(int traceId,
//      QVirtualKeyboardInputEngine::PatternRecognitionMode
//      patternRecognitionMode, const QVariantMap &traceCaptureDeviceInfo,
//      const QVariantMap &traceScreenInfo)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardTrace *ritual_ZN35QVirtualKeyboardAbstractInputMethod10traceBeginEiN27QVirtualKeyboardInputEngine22PatternRecognitionModeERK4QMapI7QString8QVariantES7_(
    QVirtualKeyboardAbstractInputMethod *self,
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

//  bool QVirtualKeyboardAbstractInputMethod::traceEnd(QVirtualKeyboardTrace
//      *trace)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtualKeyboardTrace(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardTrace *trace) {
  return self->traceEnd(trace);
}

//  bool QVirtualKeyboardAbstractInputMethod::clickPreeditText(int
//      cursorPosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi(
    QVirtualKeyboardAbstractInputMethod *self,
    int cursorPosition) {
  return self->clickPreeditText(cursorPosition);
}

//  void QVirtualKeyboardAbstractInputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethod5resetEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->reset();
}

//  void QVirtualKeyboardAbstractInputMethod::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethod6updateEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->update();
}

//  void QVirtualKeyboardAbstractInputMethod::clearInputMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethod14clearInputModeEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->clearInputMode();
}

//  void QVirtualKeyboardAbstractInputMethod::setInputEngine(QVirtualKeyboard
//      InputEngine *inputEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardAbstractInputMethod14setInputEngineEP27QVirtualKeyboardInputEngine(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardInputEngine *inputEngine) {
  self->setInputEngine(inputEngine);
}

//  a Python function taken by a CuteQVirtualKeyboardAbstractInputMethod, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVirtualKeyboardAbstractInputMethod(
    QVirtualKeyboardAbstractInputMethod *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVirtualKeyboardAbstractInputMethod *>(self)->take(key, call);
}

//  int QVirtualKeyboardAbstractInputMethod::selectionListItemCount(QVirtualK
//      eyboardSelectionListModel::Type type)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN35QVirtualKeyboardAbstractInputMethod22selectionListItemCountEN34QVirtualKeyboardSelectionListModel4TypeE(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type) {
  return self->QVirtualKeyboardAbstractInputMethod::selectionListItemCount(
      type);
}

//  QVariant QVirtualKeyboardAbstractInputMethod::selectionListData(QVirtualK
//      eyboardSelectionListModel::Type type, int index,
//      QVirtualKeyboardSelectionListModel::Role role)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN35QVirtualKeyboardAbstractInputMethod17selectionListDataEN34QVirtualKeyboardSelectionListModel4TypeEiNS0_4RoleE(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index,
    QVirtualKeyboardSelectionListModel::Role role) {
  return new QVariant(
      self->QVirtualKeyboardAbstractInputMethod::selectionListData(
          type,
          index,
          role));
}

//  void QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(QVirt
//      ualKeyboardSelectionListModel::Type type, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QVirtualKeyboardAbstractInputMethod25selectionListItemSelectedEN34QVirtualKeyboardSelectionListModel4TypeEi(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index) {
  self->QVirtualKeyboardAbstractInputMethod::selectionListItemSelected(
      type,
      index);
}

//  bool QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(QVirtua
//      lKeyboardSelectionListModel::Type type, int index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN35QVirtualKeyboardAbstractInputMethod23selectionListRemoveItemEN34QVirtualKeyboardSelectionListModel4TypeEi(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardSelectionListModel::Type type,
    int index) {
  return self->QVirtualKeyboardAbstractInputMethod::selectionListRemoveItem(
      type,
      index);
}

//  bool QVirtualKeyboardAbstractInputMethod::traceEnd(QVirtualKeyboardTrace
//      *trace)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN35QVirtualKeyboardAbstractInputMethod8traceEndEP21QVirtualKeyboardTrace(
    QVirtualKeyboardAbstractInputMethod *self,
    QVirtualKeyboardTrace *trace) {
  return self->QVirtualKeyboardAbstractInputMethod::traceEnd(trace);
}

//  bool QVirtualKeyboardAbstractInputMethod::clickPreeditText(int
//      cursorPosition)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN35QVirtualKeyboardAbstractInputMethod16clickPreeditTextEi(
    QVirtualKeyboardAbstractInputMethod *self,
    int cursorPosition) {
  return self->QVirtualKeyboardAbstractInputMethod::clickPreeditText(
      cursorPosition);
}

//  void QVirtualKeyboardAbstractInputMethod::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QVirtualKeyboardAbstractInputMethod5resetEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->QVirtualKeyboardAbstractInputMethod::reset();
}

//  void QVirtualKeyboardAbstractInputMethod::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QVirtualKeyboardAbstractInputMethod6updateEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->QVirtualKeyboardAbstractInputMethod::update();
}

//  void QVirtualKeyboardAbstractInputMethod::clearInputMode()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN35QVirtualKeyboardAbstractInputMethod14clearInputModeEv(
    QVirtualKeyboardAbstractInputMethod *self) {
  self->QVirtualKeyboardAbstractInputMethod::clearInputMode();
}
