//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboardinputengine.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboardinputengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QVirtualKeyboardInputEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQVirtualKeyboardInputEngine : QVirtualKeyboardInputEngine {
  using QVirtualKeyboardInputEngine::timerEvent;
};

//  A QVirtualKeyboardInputEngine that Python can take functions over in. Every QVirtualKeyboardInputEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputEngineCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardInputEngineCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardInputEngineCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVirtualKeyboardInputEngine : public QVirtualKeyboardInputEngine {
public:
  using QVirtualKeyboardInputEngine::QVirtualKeyboardInputEngine;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
  //  void QVirtualKeyboardInputEngine::timerEvent(QTimerEvent *timerEvent)
  void timerEvent(QTimerEvent *timerEvent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQVirtualKeyboardInputEngineCall0 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall0>(taken[0]);
      call(this, timerEvent, &handled);
      if (handled) return;
    }
    QVirtualKeyboardInputEngine::timerEvent(timerEvent);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQVirtualKeyboardInputEngineCall1 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQVirtualKeyboardInputEngineCall2 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVirtualKeyboardInputEngineCall3 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall3>(taken[3]);
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
      CuteQVirtualKeyboardInputEngineCall4 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall4>(taken[4]);
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
      CuteQVirtualKeyboardInputEngineCall5 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall5>(taken[5]);
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
      CuteQVirtualKeyboardInputEngineCall6 call = reinterpret_cast<CuteQVirtualKeyboardInputEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVirtualKeyboardInputEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QVirtualKeyboardInputEngine10metaObjectEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardInputEngine::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QVirtualKeyboardInputEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardInputEngine::tr(s, c, n));
}

//  void QVirtualKeyboardInputEngine::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine24qt_qmlMarker_uncreatableEv(
    QVirtualKeyboardInputEngine *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QVirtualKeyboardInputEngine::QVirtualKeyboardInputEngine(QVirtualKeyboard
//      InputContext *parent)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputEngine *ritual_ZN27QVirtualKeyboardInputEngineC1EP28QVirtualKeyboardInputContext(
    QVirtualKeyboardInputContext *parent) {
  return new CuteQVirtualKeyboardInputEngine(parent);
}

//  void QVirtualKeyboardInputEngine::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine4initEv(
    QVirtualKeyboardInputEngine *self) {
  self->init();
}

//  QVirtualKeyboardInputEngine::~QVirtualKeyboardInputEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngineD1Ev(
    QVirtualKeyboardInputEngine *self) {
  delete self;
}

//  bool QVirtualKeyboardInputEngine::virtualKeyPress(Qt::Key key, const
//      QString &text, Qt::KeyboardModifiers modifiers, bool repeat)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QVirtualKeyboardInputEngine15virtualKeyPressEN2Qt3KeyERK7QString6QFlagsINS0_16KeyboardModifierEEb(
    QVirtualKeyboardInputEngine *self,
    Qt::Key key,
    const QString *text,
    int modifiers,
    bool repeat) {
  return self->virtualKeyPress(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      repeat);
}

//  void QVirtualKeyboardInputEngine::virtualKeyCancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine16virtualKeyCancelEv(
    QVirtualKeyboardInputEngine *self) {
  self->virtualKeyCancel();
}

//  bool QVirtualKeyboardInputEngine::virtualKeyRelease(Qt::Key key, const
//      QString &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QVirtualKeyboardInputEngine17virtualKeyReleaseEN2Qt3KeyERK7QString6QFlagsINS0_16KeyboardModifierEE(
    QVirtualKeyboardInputEngine *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->virtualKeyRelease(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QVirtualKeyboardInputEngine::virtualKeyClick(Qt::Key key, const
//      QString &text, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QVirtualKeyboardInputEngine15virtualKeyClickEN2Qt3KeyERK7QString6QFlagsINS0_16KeyboardModifierEE(
    QVirtualKeyboardInputEngine *self,
    Qt::Key key,
    const QString *text,
    int modifiers) {
  return self->virtualKeyClick(
      key,
      *text,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QVirtualKeyboardInputContext *QVirtualKeyboardInputEngine::inputContext()
//      const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContext *ritual_ZNK27QVirtualKeyboardInputEngine12inputContextEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->inputContext();
}

//  Qt::Key QVirtualKeyboardInputEngine::activeKey() const
extern "C" Q_DECL_EXPORT
Qt::Key ritual_ZNK27QVirtualKeyboardInputEngine9activeKeyEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->activeKey();
}

//  Qt::Key QVirtualKeyboardInputEngine::previousKey() const
extern "C" Q_DECL_EXPORT
Qt::Key ritual_ZNK27QVirtualKeyboardInputEngine11previousKeyEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->previousKey();
}

//  QVirtualKeyboardAbstractInputMethod
//      *QVirtualKeyboardInputEngine::inputMethod() const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardAbstractInputMethod *ritual_ZNK27QVirtualKeyboardInputEngine11inputMethodEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->inputMethod();
}

//  void QVirtualKeyboardInputEngine::setInputMethod(QVirtualKeyboardAbstract
//      InputMethod *inputMethod)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine14setInputMethodEP35QVirtualKeyboardAbstractInputMethod(
    QVirtualKeyboardInputEngine *self,
    QVirtualKeyboardAbstractInputMethod *inputMethod) {
  self->setInputMethod(inputMethod);
}

//  InputMode QVirtualKeyboardInputEngine::inputMode() const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputEngine::InputMode ritual_ZNK27QVirtualKeyboardInputEngine9inputModeEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->inputMode();
}

//  void QVirtualKeyboardInputEngine::setInputMode(InputMode inputMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine12setInputModeENS_9InputModeE(
    QVirtualKeyboardInputEngine *self,
    QVirtualKeyboardInputEngine::InputMode inputMode) {
  self->setInputMode(inputMode);
}

//  QVirtualKeyboardSelectionListModel
//      *QVirtualKeyboardInputEngine::wordCandidateListModel() const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardSelectionListModel *ritual_ZNK27QVirtualKeyboardInputEngine22wordCandidateListModelEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->wordCandidateListModel();
}

//  bool QVirtualKeyboardInputEngine::wordCandidateListVisibleHint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QVirtualKeyboardInputEngine28wordCandidateListVisibleHintEv(
    const QVirtualKeyboardInputEngine *self) {
  return self->wordCandidateListVisibleHint();
}

//  QVirtualKeyboardTrace *QVirtualKeyboardInputEngine::traceBegin(int
//      traceId, PatternRecognitionMode patternRecognitionMode, const
//      QVariantMap &traceCaptureDeviceInfo, const QVariantMap
//      &traceScreenInfo)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardTrace *ritual_ZN27QVirtualKeyboardInputEngine10traceBeginEiNS_22PatternRecognitionModeERK4QMapI7QString8QVariantES6_(
    QVirtualKeyboardInputEngine *self,
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

//  bool QVirtualKeyboardInputEngine::traceEnd(QVirtualKeyboardTrace *trace)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QVirtualKeyboardInputEngine8traceEndEP21QVirtualKeyboardTrace(
    QVirtualKeyboardInputEngine *self,
    QVirtualKeyboardTrace *trace) {
  return self->traceEnd(trace);
}

//  bool QVirtualKeyboardInputEngine::clickPreeditText(int cursorPosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QVirtualKeyboardInputEngine16clickPreeditTextEi(
    QVirtualKeyboardInputEngine *self,
    int cursorPosition) {
  return self->clickPreeditText(cursorPosition);
}

//  void QVirtualKeyboardInputEngine::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine5resetEv(
    QVirtualKeyboardInputEngine *self) {
  self->reset();
}

//  void QVirtualKeyboardInputEngine::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine6updateEv(
    QVirtualKeyboardInputEngine *self) {
  self->update();
}

//  void QVirtualKeyboardInputEngine::shiftChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine12shiftChangedEv(
    QVirtualKeyboardInputEngine *self) {
  self->shiftChanged();
}

//  void QVirtualKeyboardInputEngine::updateSelectionListModels()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine25updateSelectionListModelsEv(
    QVirtualKeyboardInputEngine *self) {
  self->updateSelectionListModels();
}

//  void QVirtualKeyboardInputEngine::updateInputModes()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine16updateInputModesEv(
    QVirtualKeyboardInputEngine *self) {
  self->updateInputModes();
}

//  void QVirtualKeyboardInputEngine::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardInputEngine10timerEventEP11QTimerEvent(
    QVirtualKeyboardInputEngine *self,
    QTimerEvent *timerEvent) {
  self->timerEvent(timerEvent);
}

//  a Python function taken by a CuteQVirtualKeyboardInputEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVirtualKeyboardInputEngine(
    QVirtualKeyboardInputEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVirtualKeyboardInputEngine *>(self)->take(key, call);
}

//  void QVirtualKeyboardInputEngine::timerEvent(QTimerEvent *timerEvent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QVirtualKeyboardInputEngine10timerEventEP11QTimerEvent(
    QVirtualKeyboardInputEngine *self,
    QTimerEvent *timerEvent) {
  static_cast<OwnQVirtualKeyboardInputEngine *>(self)->OwnQVirtualKeyboardInputEngine::timerEvent(
      timerEvent);
}
