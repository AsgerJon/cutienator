//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboardinputcontext.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qurl.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QVirtualKeyboardInputContextPrivate that Python can take functions over in. Every QVirtualKeyboardInputContextPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardInputContextPrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardInputContextPrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextPrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVirtualKeyboardInputContextPrivate : public QVirtualKeyboardInputContextPrivate {
public:
  using QVirtualKeyboardInputContextPrivate::QVirtualKeyboardInputContextPrivate;
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
      CuteQVirtualKeyboardInputContextPrivateCall0 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall0>(taken[0]);
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
      CuteQVirtualKeyboardInputContextPrivateCall1 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall1>(taken[1]);
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
      CuteQVirtualKeyboardInputContextPrivateCall2 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall2>(taken[2]);
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
      CuteQVirtualKeyboardInputContextPrivateCall3 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall3>(taken[3]);
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
      CuteQVirtualKeyboardInputContextPrivateCall4 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall4>(taken[4]);
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
      CuteQVirtualKeyboardInputContextPrivateCall5 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall5>(taken[5]);
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
      CuteQVirtualKeyboardInputContextPrivateCall6 call = reinterpret_cast<CuteQVirtualKeyboardInputContextPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVirtualKeyboardInputContextPrivate::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK35QVirtualKeyboardInputContextPrivate10metaObjectEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardInputContextPrivate::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN35QVirtualKeyboardInputContextPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardInputContextPrivate::tr(s, c, n));
}

//  QVirtualKeyboardInputContext
//      *QVirtualKeyboardInputContextPrivate::q_func()
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContext *ritual_ZN35QVirtualKeyboardInputContextPrivate6q_funcEv(
    QVirtualKeyboardInputContextPrivate *self) {
  return self->q_func();
}

//  const QVirtualKeyboardInputContext
//      *QVirtualKeyboardInputContextPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QVirtualKeyboardInputContext *ritual_ZNK35QVirtualKeyboardInputContextPrivate6q_funcEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->q_func();
}

//  void QVirtualKeyboardInputContextPrivate::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate24qt_qmlMarker_uncreatableEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QVirtualKeyboardInputContextPrivate::QVirtualKeyboardInputContextPrivate(
//      QVirtualKeyboardInputContext *q_ptr)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContextPrivate *ritual_ZN35QVirtualKeyboardInputContextPrivateC1EP28QVirtualKeyboardInputContext(
    QVirtualKeyboardInputContext *q_ptr) {
  return new CuteQVirtualKeyboardInputContextPrivate(q_ptr);
}

//  void QVirtualKeyboardInputContextPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate4initEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->init();
}

//  QVirtualKeyboardInputContextPrivate::~QVirtualKeyboardInputContextPrivate
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivateD1Ev(
    QVirtualKeyboardInputContextPrivate *self) {
  delete self;
}

//  bool QVirtualKeyboardInputContextPrivate::focus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QVirtualKeyboardInputContextPrivate5focusEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->focus();
}

//  void QVirtualKeyboardInputContextPrivate::setFocus(bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate8setFocusEb(
    QVirtualKeyboardInputContextPrivate *self,
    bool focus) {
  self->setFocus(focus);
}

//  QRectF QVirtualKeyboardInputContextPrivate::keyboardRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK35QVirtualKeyboardInputContextPrivate17keyboardRectangleEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return new QRectF(self->keyboardRectangle());
}

//  void QVirtualKeyboardInputContextPrivate::setKeyboardRectangle(QRectF
//      rectangle)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate20setKeyboardRectangleE6QRectF(
    QVirtualKeyboardInputContextPrivate *self,
    const QRectF *rectangle) {
  self->setKeyboardRectangle(*rectangle);
}

//  QRectF QVirtualKeyboardInputContextPrivate::previewRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK35QVirtualKeyboardInputContextPrivate16previewRectangleEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return new QRectF(self->previewRectangle());
}

//  void QVirtualKeyboardInputContextPrivate::setPreviewRectangle(QRectF
//      rectangle)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate19setPreviewRectangleE6QRectF(
    QVirtualKeyboardInputContextPrivate *self,
    const QRectF *rectangle) {
  self->setPreviewRectangle(*rectangle);
}

//  bool QVirtualKeyboardInputContextPrivate::previewVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QVirtualKeyboardInputContextPrivate14previewVisibleEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->previewVisible();
}

//  void QVirtualKeyboardInputContextPrivate::setPreviewVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate17setPreviewVisibleEb(
    QVirtualKeyboardInputContextPrivate *self,
    bool visible) {
  self->setPreviewVisible(visible);
}

//  QString QVirtualKeyboardInputContextPrivate::locale() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK35QVirtualKeyboardInputContextPrivate6localeEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return new QString(self->locale());
}

//  void QVirtualKeyboardInputContextPrivate::setLocale(const QString
//      &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate9setLocaleERK7QString(
    QVirtualKeyboardInputContextPrivate *self,
    const QString *locale) {
  self->setLocale(*locale);
}

//  QObject *QVirtualKeyboardInputContextPrivate::inputItem() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK35QVirtualKeyboardInputContextPrivate9inputItemEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->inputItem();
}

//  QtVirtualKeyboard::ShiftHandler
//      *QVirtualKeyboardInputContextPrivate::shiftHandler() const
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::ShiftHandler *ritual_ZNK35QVirtualKeyboardInputContextPrivate12shiftHandlerEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->shiftHandler();
}

//  QtVirtualKeyboard::ShadowInputContext
//      *QVirtualKeyboardInputContextPrivate::shadow() const
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::ShadowInputContext *ritual_ZNK35QVirtualKeyboardInputContextPrivate6shadowEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->shadow();
}

//  void QVirtualKeyboardInputContextPrivate::setKeyboardObserver(QVirtualKey
//      boardObserver *keyboardObserver)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate19setKeyboardObserverEP24QVirtualKeyboardObserver(
    QVirtualKeyboardInputContextPrivate *self,
    QVirtualKeyboardObserver *keyboardObserver) {
  self->setKeyboardObserver(keyboardObserver);
}

//  bool QVirtualKeyboardInputContextPrivate::fileExists(const QUrl &fileUrl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardInputContextPrivate10fileExistsERK4QUrl(
    QVirtualKeyboardInputContextPrivate *self,
    const QUrl *fileUrl) {
  return self->fileExists(*fileUrl);
}

//  bool QVirtualKeyboardInputContextPrivate::hasEnterKeyAction(QObject
//      *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QVirtualKeyboardInputContextPrivate17hasEnterKeyActionEP7QObject(
    const QVirtualKeyboardInputContextPrivate *self,
    QObject *item) {
  return self->hasEnterKeyAction(item);
}

//  void QVirtualKeyboardInputContextPrivate::registerInputPanel(QObject
//      *inputPanel)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate18registerInputPanelEP7QObject(
    QVirtualKeyboardInputContextPrivate *self,
    QObject *inputPanel) {
  self->registerInputPanel(inputPanel);
}

//  bool QVirtualKeyboardInputContextPrivate::contains(const QPointF &point)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QVirtualKeyboardInputContextPrivate8containsERK7QPointF(
    const QVirtualKeyboardInputContextPrivate *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  QtVirtualKeyboard::KeyboardFunctionKey QVirtualKeyboardInputContextPrivat
//      e::keyboardFunctionKey(QtVirtualKeyboard::KeyboardFunction
//      keyboardFunction) const
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::KeyboardFunctionKey ritual_ZNK35QVirtualKeyboardInputContextPrivate19keyboardFunctionKeyEN17QtVirtualKeyboard16KeyboardFunctionE(
    const QVirtualKeyboardInputContextPrivate *self,
    QtVirtualKeyboard::KeyboardFunction keyboardFunction) {
  return self->keyboardFunctionKey(keyboardFunction);
}

//  void QVirtualKeyboardInputContextPrivate::hideInputPanel()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate14hideInputPanelEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->hideInputPanel();
}

//  void QVirtualKeyboardInputContextPrivate::updateAvailableLocales(const
//      QStringList &availableLocales)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate22updateAvailableLocalesERK5QListI7QStringE(
    QVirtualKeyboardInputContextPrivate *self,
    const QList<QString> *availableLocales) {
  self->updateAvailableLocales(*availableLocales);
}

//  void QVirtualKeyboardInputContextPrivate::forceCursorPosition(int
//      anchorPosition, int cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate19forceCursorPositionEii(
    QVirtualKeyboardInputContextPrivate *self,
    int anchorPosition,
    int cursorPosition) {
  self->forceCursorPosition(anchorPosition, cursorPosition);
}

//  void QVirtualKeyboardInputContextPrivate::onInputItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate18onInputItemChangedEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->onInputItemChanged();
}

//  void QVirtualKeyboardInputContextPrivate::sendInputMethodEvent(QInputMeth
//      odEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate20sendInputMethodEventEP17QInputMethodEvent(
    QVirtualKeyboardInputContextPrivate *self,
    QInputMethodEvent *event) {
  self->sendInputMethodEvent(event);
}

//  void QVirtualKeyboardInputContextPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate5resetEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->reset();
}

//  void QVirtualKeyboardInputContextPrivate::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate6commitEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->commit();
}

//  void QVirtualKeyboardInputContextPrivate::update(Qt::InputMethodQueries
//      queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QVirtualKeyboardInputContextPrivate *self,
    int queries) {
  self->update(QFlags<Qt::InputMethodQuery>::fromInt(queries));
}

//  void
//      QVirtualKeyboardInputContextPrivate::invokeAction(QInputMethod::Actio
//      n action, int cursorPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate12invokeActionEN12QInputMethod6ActionEi(
    QVirtualKeyboardInputContextPrivate *self,
    QInputMethod::Action action,
    int cursorPosition) {
  self->invokeAction(action, cursorPosition);
}

//  void QVirtualKeyboardInputContextPrivate::maybeCloseOnReturn()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate18maybeCloseOnReturnEv(
    QVirtualKeyboardInputContextPrivate *self) {
  self->maybeCloseOnReturn();
}

//  bool QVirtualKeyboardInputContextPrivate::filterEvent(const QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QVirtualKeyboardInputContextPrivate11filterEventEPK6QEvent(
    QVirtualKeyboardInputContextPrivate *self,
    const QEvent *event) {
  return self->filterEvent(event);
}

//  bool QVirtualKeyboardInputContextPrivate::isEmptyState() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK35QVirtualKeyboardInputContextPrivate12isEmptyStateEv(
    const QVirtualKeyboardInputContextPrivate *self) {
  return self->isEmptyState();
}

//  void
//      QVirtualKeyboardInputContextPrivate::updateSelectionControlVisible(bo
//      ol inputPanelVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QVirtualKeyboardInputContextPrivate29updateSelectionControlVisibleEb(
    QVirtualKeyboardInputContextPrivate *self,
    bool inputPanelVisible) {
  self->updateSelectionControlVisible(inputPanelVisible);
}

//  a Python function taken by a CuteQVirtualKeyboardInputContextPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVirtualKeyboardInputContextPrivate(
    QVirtualKeyboardInputContextPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVirtualKeyboardInputContextPrivate *>(self)->take(key, call);
}
