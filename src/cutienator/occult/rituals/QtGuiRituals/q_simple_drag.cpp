//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qsimpledrag_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qsimpledrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSimpleDrag may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSimpleDrag : QSimpleDrag {
  using QSimpleDrag::startDrag;
  using QSimpleDrag::cancel;
  using QSimpleDrag::move;
  using QSimpleDrag::drop;
};

//  A QSimpleDrag that Python can take functions over in. Every QSimpleDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSimpleDragCall0)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSimpleDragCall1)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSimpleDragCall2)(const void *, const QPoint *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSimpleDragCall3)(const void *, const QPoint *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef int (*CuteQSimpleDragCall4)(const void *, QDrag *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSimpleDragCall5)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQSimpleDragCall6)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQSimpleDragCall7)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef int (*CuteQSimpleDragCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQSimpleDragCall9)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSimpleDragCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSimpleDragCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSimpleDragCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSimpleDragCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSimpleDragCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSimpleDragCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSimpleDrag : public QSimpleDrag {
public:
  using QSimpleDrag::QSimpleDrag;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag9startDragEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag6cancelEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QPlatformDrag4dragEP5QDrag")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QPlatformDrag10cancelDragEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag7endDragEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK13QPlatformDrag13defaultActionE6QFlagsIN2Qt10DropActionEES0_INS1_16KeyboardModifierEE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK13QPlatformDrag14ownsDragObjectEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(draganddrop)
  //  void QSimpleDrag::startDrag()
  void startDrag() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSimpleDragCall0 call = reinterpret_cast<CuteQSimpleDragCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSimpleDrag::startDrag();
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QSimpleDrag::cancel()
  void cancel() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSimpleDragCall1 call = reinterpret_cast<CuteQSimpleDragCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSimpleDrag::cancel();
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QSimpleDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
  //      Qt::KeyboardModifiers mods)
  void move(
      const QPoint &globalPos,
      Qt::MouseButtons b,
      Qt::KeyboardModifiers mods) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSimpleDragCall2 call = reinterpret_cast<CuteQSimpleDragCall2>(taken[2]);
      call(this, &globalPos, static_cast<int>(b.toInt()), static_cast<int>(mods.toInt()), &handled);
      if (handled) return;
    }
    QSimpleDrag::move(globalPos, b, mods);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QSimpleDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
  //      Qt::KeyboardModifiers mods)
  void drop(
      const QPoint &globalPos,
      Qt::MouseButtons b,
      Qt::KeyboardModifiers mods) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSimpleDragCall3 call = reinterpret_cast<CuteQSimpleDragCall3>(taken[3]);
      call(this, &globalPos, static_cast<int>(b.toInt()), static_cast<int>(mods.toInt()), &handled);
      if (handled) return;
    }
    QSimpleDrag::drop(globalPos, b, mods);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  Qt::DropAction QBasicDrag::drag(QDrag *drag)
  Qt::DropAction drag(QDrag *drag) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSimpleDragCall4 call = reinterpret_cast<CuteQSimpleDragCall4>(taken[4]);
      int given = call(this, drag, &handled);
      if (handled) return static_cast<Qt::DropAction>(given);
    }
    return QBasicDrag::drag(drag);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::cancelDrag()
  void cancelDrag() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSimpleDragCall5 call = reinterpret_cast<CuteQSimpleDragCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QBasicDrag::cancelDrag();
  }
#endif  // QT_CONFIG(draganddrop)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
  //  bool QBasicDrag::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSimpleDragCall6 call = reinterpret_cast<CuteQSimpleDragCall6>(taken[6]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QBasicDrag::eventFilter(o, e);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::endDrag()
  void endDrag() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSimpleDragCall7 call = reinterpret_cast<CuteQSimpleDragCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QBasicDrag::endDrag();
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  Qt::DropAction QPlatformDrag::defaultAction(Qt::DropActions
  //      possibleActions, Qt::KeyboardModifiers modifiers) const
  Qt::DropAction defaultAction(
      Qt::DropActions possibleActions,
      Qt::KeyboardModifiers modifiers) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSimpleDragCall8 call = reinterpret_cast<CuteQSimpleDragCall8>(taken[8]);
      int given = call(this, static_cast<int>(possibleActions.toInt()), static_cast<int>(modifiers.toInt()), &handled);
      if (handled) return static_cast<Qt::DropAction>(given);
    }
    return QPlatformDrag::defaultAction(possibleActions, modifiers);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  bool QPlatformDrag::ownsDragObject() const
  bool ownsDragObject() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSimpleDragCall9 call = reinterpret_cast<CuteQSimpleDragCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformDrag::ownsDragObject();
  }
#endif  // QT_CONFIG(draganddrop)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSimpleDragCall10 call = reinterpret_cast<CuteQSimpleDragCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSimpleDragCall11 call = reinterpret_cast<CuteQSimpleDragCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSimpleDragCall12 call = reinterpret_cast<CuteQSimpleDragCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSimpleDragCall13 call = reinterpret_cast<CuteQSimpleDragCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSimpleDragCall14 call = reinterpret_cast<CuteQSimpleDragCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSimpleDragCall15 call = reinterpret_cast<CuteQSimpleDragCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSimpleDrag::QSimpleDrag()
extern "C" Q_DECL_EXPORT
QSimpleDrag *ritual_ZN11QSimpleDragC1Ev() {
  return new CuteQSimpleDrag();
}

//  void QSimpleDrag::startDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSimpleDrag9startDragEv(QSimpleDrag *self) {
  self->startDrag();
}

//  void QSimpleDrag::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSimpleDrag6cancelEv(QSimpleDrag *self) {
  self->cancel();
}

//  void QSimpleDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSimpleDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE(
    QSimpleDrag *self,
    const QPoint *globalPos,
    int b,
    int mods) {
  self->move(
      *globalPos,
      QFlags<Qt::MouseButton>::fromInt(b),
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  void QSimpleDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSimpleDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE(
    QSimpleDrag *self,
    const QPoint *globalPos,
    int b,
    int mods) {
  self->drop(
      *globalPos,
      QFlags<Qt::MouseButton>::fromInt(b),
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  a Python function taken by a CuteQSimpleDrag, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSimpleDrag(
    QSimpleDrag *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSimpleDrag *>(self)->take(key, call);
}

//  void QSimpleDrag::startDrag()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSimpleDrag9startDragEv(QSimpleDrag *self) {
  static_cast<OwnQSimpleDrag *>(self)->OwnQSimpleDrag::startDrag();
}

//  void QSimpleDrag::cancel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSimpleDrag6cancelEv(QSimpleDrag *self) {
  static_cast<OwnQSimpleDrag *>(self)->OwnQSimpleDrag::cancel();
}

//  void QSimpleDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSimpleDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE(
    QSimpleDrag *self,
    const QPoint *globalPos,
    int b,
    int mods) {
  static_cast<OwnQSimpleDrag *>(self)->OwnQSimpleDrag::move(
      *globalPos,
      QFlags<Qt::MouseButton>::fromInt(b),
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  void QSimpleDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSimpleDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE(
    QSimpleDrag *self,
    const QPoint *globalPos,
    int b,
    int mods) {
  static_cast<OwnQSimpleDrag *>(self)->OwnQSimpleDrag::drop(
      *globalPos,
      QFlags<Qt::MouseButton>::fromInt(b),
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

#endif  // QT_CONFIG(draganddrop)
