//  Written by hand on 2026-11-25 from
//  QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shadowinputcontext_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Left out: nothing. The constructor and 'setInputContext' are private,
//  and are written, as private members may be named.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/shadowinputcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtVirtualKeyboard/qvirtualkeyboardinputcontext.h>
#include <cstring>

//  A QtVirtualKeyboard::ShadowInputContext that Python can take functions over in. Every QtVirtualKeyboard::ShadowInputContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_ShadowInputContextCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtVirtualKeyboard_ShadowInputContextCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShadowInputContextCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShadowInputContextCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShadowInputContextCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShadowInputContextCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtVirtualKeyboard_ShadowInputContextCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtVirtualKeyboard_ShadowInputContext : public QtVirtualKeyboard::ShadowInputContext {
public:
  using QtVirtualKeyboard::ShadowInputContext::ShadowInputContext;
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
      CuteQtVirtualKeyboard_ShadowInputContextCall0 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall0>(taken[0]);
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
      CuteQtVirtualKeyboard_ShadowInputContextCall1 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall1>(taken[1]);
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
      CuteQtVirtualKeyboard_ShadowInputContextCall2 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall2>(taken[2]);
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
      CuteQtVirtualKeyboard_ShadowInputContextCall3 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall3>(taken[3]);
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
      CuteQtVirtualKeyboard_ShadowInputContextCall4 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall4>(taken[4]);
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
      CuteQtVirtualKeyboard_ShadowInputContextCall5 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall5>(taken[5]);
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
      CuteQtVirtualKeyboard_ShadowInputContextCall6 call = reinterpret_cast<CuteQtVirtualKeyboard_ShadowInputContextCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtVirtualKeyboard::ShadowInputContext::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QtVirtualKeyboard18ShadowInputContext10metaObjectEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->metaObject();
}

//  QString QtVirtualKeyboard::ShadowInputContext::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QtVirtualKeyboard18ShadowInputContext2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtVirtualKeyboard::ShadowInputContext::tr(s, c, n));
}

//  void QtVirtualKeyboard::ShadowInputContext::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext24qt_qmlMarker_uncreatableEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QtVirtualKeyboard::ShadowInputContext::ShadowInputContext(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::ShadowInputContext *ritual_ZN17QtVirtualKeyboard18ShadowInputContextC1EP7QObject(
    QObject *parent) {
  return new CuteQtVirtualKeyboard_ShadowInputContext(parent);
}

//  void
//      QtVirtualKeyboard::ShadowInputContext::setInputContext(QVirtualKeyboardInputContext
//      *inputContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext15setInputContextEP28QVirtualKeyboardInputContext(
    QtVirtualKeyboard::ShadowInputContext *self,
    QVirtualKeyboardInputContext *inputContext) {
  self->setInputContext(inputContext);
}

//  QObject *QtVirtualKeyboard::ShadowInputContext::inputItem() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QtVirtualKeyboard18ShadowInputContext9inputItemEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->inputItem();
}

//  void QtVirtualKeyboard::ShadowInputContext::setInputItem(QObject
//      *inputItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext12setInputItemEP7QObject(
    QtVirtualKeyboard::ShadowInputContext *self,
    QObject *inputItem) {
  self->setInputItem(inputItem);
}

//  QRectF QtVirtualKeyboard::ShadowInputContext::anchorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QtVirtualKeyboard18ShadowInputContext15anchorRectangleEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return new QRectF(self->anchorRectangle());
}

//  QRectF QtVirtualKeyboard::ShadowInputContext::cursorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QtVirtualKeyboard18ShadowInputContext15cursorRectangleEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return new QRectF(self->cursorRectangle());
}

//  bool
//      QtVirtualKeyboard::ShadowInputContext::anchorRectIntersectsClipRect()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard18ShadowInputContext28anchorRectIntersectsClipRectEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->anchorRectIntersectsClipRect();
}

//  bool
//      QtVirtualKeyboard::ShadowInputContext::cursorRectIntersectsClipRect()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard18ShadowInputContext28cursorRectIntersectsClipRectEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->cursorRectIntersectsClipRect();
}

//  bool QtVirtualKeyboard::ShadowInputContext::selectionControlVisible()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard18ShadowInputContext23selectionControlVisibleEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->selectionControlVisible();
}

//  void
//      QtVirtualKeyboard::ShadowInputContext::setSelectionOnFocusObject(const
//      QPointF &anchorPos, const QPointF &cursorPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext25setSelectionOnFocusObjectERK7QPointFS3_(
    QtVirtualKeyboard::ShadowInputContext *self,
    const QPointF *anchorPos,
    const QPointF *cursorPos) {
  self->setSelectionOnFocusObject(*anchorPos, *cursorPos);
}

//  void QtVirtualKeyboard::ShadowInputContext::updateSelectionProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext25updateSelectionPropertiesEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->updateSelectionProperties();
}

//  void QtVirtualKeyboard::ShadowInputContext::inputItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext16inputItemChangedEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->inputItemChanged();
}

//  void QtVirtualKeyboard::ShadowInputContext::anchorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext22anchorRectangleChangedEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->anchorRectangleChanged();
}

//  void QtVirtualKeyboard::ShadowInputContext::cursorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext22cursorRectangleChangedEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->cursorRectangleChanged();
}

//  void
//      QtVirtualKeyboard::ShadowInputContext::anchorRectIntersectsClipRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext35anchorRectIntersectsClipRectChangedEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->anchorRectIntersectsClipRectChanged();
}

//  void
//      QtVirtualKeyboard::ShadowInputContext::cursorRectIntersectsClipRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext35cursorRectIntersectsClipRectChangedEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->cursorRectIntersectsClipRectChanged();
}

//  void
//      QtVirtualKeyboard::ShadowInputContext::selectionControlVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext30selectionControlVisibleChangedEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  self->selectionControlVisibleChanged();
}

//  void QtVirtualKeyboard::ShadowInputContext::update(Qt::InputMethodQueries
//      queries)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard18ShadowInputContext6updateE6QFlagsIN2Qt16InputMethodQueryEE(
    QtVirtualKeyboard::ShadowInputContext *self,
    int queries) {
  self->update(Qt::InputMethodQueries::fromInt(queries));
}

//  QVariant
//      QtVirtualKeyboard::ShadowInputContext::queryFocusObject(Qt::InputMethodQuery
//      query, QVariant argument)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QtVirtualKeyboard18ShadowInputContext16queryFocusObjectEN2Qt16InputMethodQueryE8QVariant(
    QtVirtualKeyboard::ShadowInputContext *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->queryFocusObject(query, *argument));
}

//  QtVirtualKeyboard::ShadowInputContextPrivate
//      *QtVirtualKeyboard::ShadowInputContext::d_func()
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::ShadowInputContextPrivate *ritual_ZN17QtVirtualKeyboard18ShadowInputContext6d_funcEv(
    QtVirtualKeyboard::ShadowInputContext *self) {
  return self->d_func();
}

//  const QtVirtualKeyboard::ShadowInputContextPrivate
//      *QtVirtualKeyboard::ShadowInputContext::d_func() const
extern "C" Q_DECL_EXPORT
const QtVirtualKeyboard::ShadowInputContextPrivate *ritual_ZNK17QtVirtualKeyboard18ShadowInputContext6d_funcEv(
    const QtVirtualKeyboard::ShadowInputContext *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQtVirtualKeyboard_ShadowInputContext, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtVirtualKeyboard_ShadowInputContext(
    QtVirtualKeyboard::ShadowInputContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtVirtualKeyboard_ShadowInputContext *>(self)->take(key, call);
}
