//  Written by dev_tooling.RitualGenerator from the records of
//  QtVirtualKeyboard/qvirtualkeyboardinputcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#include <QtVirtualKeyboard/qvirtualkeyboardinputcontext.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVirtualKeyboardInputContext that Python can take functions over in. Every QVirtualKeyboardInputContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardInputContextCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVirtualKeyboardInputContextCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVirtualKeyboardInputContextCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVirtualKeyboardInputContext : public QVirtualKeyboardInputContext {
public:
  using QVirtualKeyboardInputContext::QVirtualKeyboardInputContext;
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
      CuteQVirtualKeyboardInputContextCall0 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall0>(taken[0]);
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
      CuteQVirtualKeyboardInputContextCall1 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall1>(taken[1]);
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
      CuteQVirtualKeyboardInputContextCall2 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall2>(taken[2]);
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
      CuteQVirtualKeyboardInputContextCall3 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall3>(taken[3]);
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
      CuteQVirtualKeyboardInputContextCall4 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall4>(taken[4]);
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
      CuteQVirtualKeyboardInputContextCall5 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall5>(taken[5]);
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
      CuteQVirtualKeyboardInputContextCall6 call = reinterpret_cast<CuteQVirtualKeyboardInputContextCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVirtualKeyboardInputContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QVirtualKeyboardInputContext10metaObjectEv(
    const QVirtualKeyboardInputContext *self) {
  return self->metaObject();
}

//  QString QVirtualKeyboardInputContext::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QVirtualKeyboardInputContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVirtualKeyboardInputContext::tr(s, c, n));
}

//  QVirtualKeyboardInputContextPrivate
//      *QVirtualKeyboardInputContext::d_func()
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContextPrivate *ritual_ZN28QVirtualKeyboardInputContext6d_funcEv(
    QVirtualKeyboardInputContext *self) {
  return self->d_func();
}

//  const QVirtualKeyboardInputContextPrivate
//      *QVirtualKeyboardInputContext::d_func() const
extern "C" Q_DECL_EXPORT
const QVirtualKeyboardInputContextPrivate *ritual_ZNK28QVirtualKeyboardInputContext6d_funcEv(
    const QVirtualKeyboardInputContext *self) {
  return self->d_func();
}

//  void QVirtualKeyboardInputContext::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext22qt_qmlMarker_singletonEv(
    QVirtualKeyboardInputContext *self) {
  self->qt_qmlMarker_singleton();
}

//  QVirtualKeyboardInputContext::QVirtualKeyboardInputContext(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContext *ritual_ZN28QVirtualKeyboardInputContextC1EP7QObject(
    QObject *parent) {
  return new CuteQVirtualKeyboardInputContext(parent);
}

//  QVirtualKeyboardInputContext::~QVirtualKeyboardInputContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContextD1Ev(
    QVirtualKeyboardInputContext *self) {
  delete self;
}

//  bool QVirtualKeyboardInputContext::isShiftActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext13isShiftActiveEv(
    const QVirtualKeyboardInputContext *self) {
  return self->isShiftActive();
}

//  bool QVirtualKeyboardInputContext::isCapsLockActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext16isCapsLockActiveEv(
    const QVirtualKeyboardInputContext *self) {
  return self->isCapsLockActive();
}

//  bool QVirtualKeyboardInputContext::isUppercase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext11isUppercaseEv(
    const QVirtualKeyboardInputContext *self) {
  return self->isUppercase();
}

//  int QVirtualKeyboardInputContext::anchorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QVirtualKeyboardInputContext14anchorPositionEv(
    const QVirtualKeyboardInputContext *self) {
  return self->anchorPosition();
}

//  int QVirtualKeyboardInputContext::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QVirtualKeyboardInputContext14cursorPositionEv(
    const QVirtualKeyboardInputContext *self) {
  return self->cursorPosition();
}

//  Qt::InputMethodHints QVirtualKeyboardInputContext::inputMethodHints()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QVirtualKeyboardInputContext16inputMethodHintsEv(
    const QVirtualKeyboardInputContext *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  QString QVirtualKeyboardInputContext::preeditText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QVirtualKeyboardInputContext11preeditTextEv(
    const QVirtualKeyboardInputContext *self) {
  return new QString(self->preeditText());
}

//  QString QVirtualKeyboardInputContext::surroundingText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QVirtualKeyboardInputContext15surroundingTextEv(
    const QVirtualKeyboardInputContext *self) {
  return new QString(self->surroundingText());
}

//  QString QVirtualKeyboardInputContext::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QVirtualKeyboardInputContext12selectedTextEv(
    const QVirtualKeyboardInputContext *self) {
  return new QString(self->selectedText());
}

//  QRectF QVirtualKeyboardInputContext::anchorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK28QVirtualKeyboardInputContext15anchorRectangleEv(
    const QVirtualKeyboardInputContext *self) {
  return new QRectF(self->anchorRectangle());
}

//  QRectF QVirtualKeyboardInputContext::cursorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK28QVirtualKeyboardInputContext15cursorRectangleEv(
    const QVirtualKeyboardInputContext *self) {
  return new QRectF(self->cursorRectangle());
}

//  bool QVirtualKeyboardInputContext::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext11isAnimatingEv(
    const QVirtualKeyboardInputContext *self) {
  return self->isAnimating();
}

//  void QVirtualKeyboardInputContext::setAnimating(bool isAnimating)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext12setAnimatingEb(
    QVirtualKeyboardInputContext *self,
    bool isAnimating) {
  self->setAnimating(isAnimating);
}

//  QString QVirtualKeyboardInputContext::locale() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QVirtualKeyboardInputContext6localeEv(
    const QVirtualKeyboardInputContext *self) {
  return new QString(self->locale());
}

//  QObject *QVirtualKeyboardInputContext::inputItem() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK28QVirtualKeyboardInputContext9inputItemEv(
    const QVirtualKeyboardInputContext *self) {
  return self->inputItem();
}

//  QVirtualKeyboardInputEngine *QVirtualKeyboardInputContext::inputEngine()
//      const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputEngine *ritual_ZNK28QVirtualKeyboardInputContext11inputEngineEv(
    const QVirtualKeyboardInputContext *self) {
  return self->inputEngine();
}

//  bool QVirtualKeyboardInputContext::isSelectionControlVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext25isSelectionControlVisibleEv(
    const QVirtualKeyboardInputContext *self) {
  return self->isSelectionControlVisible();
}

//  bool QVirtualKeyboardInputContext::anchorRectIntersectsClipRect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext28anchorRectIntersectsClipRectEv(
    const QVirtualKeyboardInputContext *self) {
  return self->anchorRectIntersectsClipRect();
}

//  bool QVirtualKeyboardInputContext::cursorRectIntersectsClipRect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QVirtualKeyboardInputContext28cursorRectIntersectsClipRectEv(
    const QVirtualKeyboardInputContext *self) {
  return self->cursorRectIntersectsClipRect();
}

//  QVirtualKeyboardInputContextPrivate *QVirtualKeyboardInputContext::priv()
//      const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardInputContextPrivate *ritual_ZNK28QVirtualKeyboardInputContext4privEv(
    const QVirtualKeyboardInputContext *self) {
  return self->priv();
}

//  QVirtualKeyboardObserver
//      *QVirtualKeyboardInputContext::keyboardObserver() const
extern "C" Q_DECL_EXPORT
QVirtualKeyboardObserver *ritual_ZNK28QVirtualKeyboardInputContext16keyboardObserverEv(
    const QVirtualKeyboardInputContext *self) {
  return self->keyboardObserver();
}

//  void QVirtualKeyboardInputContext::sendKeyClick(int key, const QString
//      &text, int modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext12sendKeyClickEiRK7QStringi(
    QVirtualKeyboardInputContext *self,
    int key,
    const QString *text,
    int modifiers) {
  self->sendKeyClick(key, *text, modifiers);
}

//  void QVirtualKeyboardInputContext::commit()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext6commitEv(
    QVirtualKeyboardInputContext *self) {
  self->commit();
}

//  void QVirtualKeyboardInputContext::commit(const QString &text, int
//      replaceFrom, int replaceLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext6commitERK7QStringii(
    QVirtualKeyboardInputContext *self,
    const QString *text,
    int replaceFrom,
    int replaceLength) {
  self->commit(*text, replaceFrom, replaceLength);
}

//  void QVirtualKeyboardInputContext::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext5clearEv(
    QVirtualKeyboardInputContext *self) {
  self->clear();
}

//  void QVirtualKeyboardInputContext::setSelectionOnFocusObject(const
//      QPointF &anchorPos, const QPointF &cursorPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QVirtualKeyboardInputContext25setSelectionOnFocusObjectERK7QPointFS2_(
    QVirtualKeyboardInputContext *self,
    const QPointF *anchorPos,
    const QPointF *cursorPos) {
  self->setSelectionOnFocusObject(*anchorPos, *cursorPos);
}

//  a Python function taken by a CuteQVirtualKeyboardInputContext, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVirtualKeyboardInputContext(
    QVirtualKeyboardInputContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVirtualKeyboardInputContext *>(self)->take(key, call);
}
