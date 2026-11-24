//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qsimpledrag_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qsimpledrag_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QBasicDrag may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQBasicDrag : QBasicDrag {
  using QBasicDrag::startDrag;
  using QBasicDrag::cancel;
  using QBasicDrag::endDrag;
};

//  A QBasicDrag that Python can take functions over in. Every QBasicDrag
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(draganddrop)
typedef int (*CuteQBasicDragCall0)(const void *, QDrag *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQBasicDragCall1)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQBasicDragCall2)(const void *, QObject *, QEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQBasicDragCall3)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQBasicDragCall4)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQBasicDragCall5)(const void *, const QPoint *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQBasicDragCall6)(const void *, const QPoint *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQBasicDragCall7)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef int (*CuteQBasicDragCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQBasicDragCall9)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBasicDragCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBasicDragCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBasicDragCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBasicDragCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBasicDragCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBasicDragCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBasicDrag : public QBasicDrag {
public:
  using QBasicDrag::QBasicDrag;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QPlatformDrag4dragEP5QDrag")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN13QPlatformDrag10cancelDragEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag9startDragEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag6cancelEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN10QBasicDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
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
  //  Qt::DropAction QBasicDrag::drag(QDrag *drag)
  Qt::DropAction drag(QDrag *drag) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBasicDragCall0 call = reinterpret_cast<CuteQBasicDragCall0>(taken[0]);
      int given = call(this, drag, &handled);
      if (handled) return static_cast<Qt::DropAction>(given);
    }
    return QBasicDrag::drag(drag);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::cancelDrag()
  void cancelDrag() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBasicDragCall1 call = reinterpret_cast<CuteQBasicDragCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQBasicDragCall2 call = reinterpret_cast<CuteQBasicDragCall2>(taken[2]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QBasicDrag::eventFilter(o, e);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::startDrag()
  void startDrag() override {
    if (taken[3]) {
      int handled = 0;
      CuteQBasicDragCall3 call = reinterpret_cast<CuteQBasicDragCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QBasicDrag::startDrag();
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::cancel()
  void cancel() override {
    if (taken[4]) {
      int handled = 0;
      CuteQBasicDragCall4 call = reinterpret_cast<CuteQBasicDragCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QBasicDrag::cancel();
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
  //      Qt::KeyboardModifiers mods)
  void move(
      const QPoint &globalPos,
      Qt::MouseButtons b,
      Qt::KeyboardModifiers mods) override {
    if (taken[5]) {
      int handled = 0;
      CuteQBasicDragCall5 call = reinterpret_cast<CuteQBasicDragCall5>(taken[5]);
      call(this, &globalPos, static_cast<int>(b.toInt()), static_cast<int>(mods.toInt()), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
  //      Qt::KeyboardModifiers mods)
  void drop(
      const QPoint &globalPos,
      Qt::MouseButtons b,
      Qt::KeyboardModifiers mods) override {
    if (taken[6]) {
      int handled = 0;
      CuteQBasicDragCall6 call = reinterpret_cast<CuteQBasicDragCall6>(taken[6]);
      call(this, &globalPos, static_cast<int>(b.toInt()), static_cast<int>(mods.toInt()), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QBasicDrag::endDrag()
  void endDrag() override {
    if (taken[7]) {
      int handled = 0;
      CuteQBasicDragCall7 call = reinterpret_cast<CuteQBasicDragCall7>(taken[7]);
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
      CuteQBasicDragCall8 call = reinterpret_cast<CuteQBasicDragCall8>(taken[8]);
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
      CuteQBasicDragCall9 call = reinterpret_cast<CuteQBasicDragCall9>(taken[9]);
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
      CuteQBasicDragCall10 call = reinterpret_cast<CuteQBasicDragCall10>(taken[10]);
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
      CuteQBasicDragCall11 call = reinterpret_cast<CuteQBasicDragCall11>(taken[11]);
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
      CuteQBasicDragCall12 call = reinterpret_cast<CuteQBasicDragCall12>(taken[12]);
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
      CuteQBasicDragCall13 call = reinterpret_cast<CuteQBasicDragCall13>(taken[13]);
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
      CuteQBasicDragCall14 call = reinterpret_cast<CuteQBasicDragCall14>(taken[14]);
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
      CuteQBasicDragCall15 call = reinterpret_cast<CuteQBasicDragCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QBasicDrag::~QBasicDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDragD1Ev(QBasicDrag *self) {
  delete self;
}

//  Qt::DropAction QBasicDrag::drag(QDrag *drag)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZN10QBasicDrag4dragEP5QDrag(
    QBasicDrag *self,
    QDrag *drag) {
  return self->drag(drag);
}

//  void QBasicDrag::cancelDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag10cancelDragEv(QBasicDrag *self) {
  self->cancelDrag();
}

//  bool QBasicDrag::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QBasicDrag11eventFilterEP7QObjectP6QEvent(
    QBasicDrag *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  void QBasicDrag::startDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag9startDragEv(QBasicDrag *self) {
  self->startDrag();
}

//  void QBasicDrag::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag6cancelEv(QBasicDrag *self) {
  self->cancel();
}

//  void QBasicDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE(
    QBasicDrag *self,
    const QPoint *globalPos,
    int b,
    int mods) {
  self->move(
      *globalPos,
      QFlags<Qt::MouseButton>::fromInt(b),
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  void QBasicDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS4_16KeyboardModifierEE(
    QBasicDrag *self,
    const QPoint *globalPos,
    int b,
    int mods) {
  self->drop(
      *globalPos,
      QFlags<Qt::MouseButton>::fromInt(b),
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  void QBasicDrag::endDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag7endDragEv(QBasicDrag *self) {
  self->endDrag();
}

//  void QBasicDrag::moveShapedPixmapWindow(const QPoint
//      &deviceIndependentPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag22moveShapedPixmapWindowERK6QPoint(
    QBasicDrag *self,
    const QPoint *deviceIndependentPosition) {
  self->moveShapedPixmapWindow(*deviceIndependentPosition);
}

//  QShapedPixmapWindow *QBasicDrag::shapedPixmapWindow() const
extern "C" Q_DECL_EXPORT
QShapedPixmapWindow *ritual_ZNK10QBasicDrag18shapedPixmapWindowEv(
    const QBasicDrag *self) {
  return self->shapedPixmapWindow();
}

//  void QBasicDrag::recreateShapedPixmapWindow(QScreen *screen, const QPoint
//      &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag26recreateShapedPixmapWindowEP7QScreenRK6QPoint(
    QBasicDrag *self,
    QScreen *screen,
    const QPoint *pos) {
  self->recreateShapedPixmapWindow(screen, *pos);
}

//  void QBasicDrag::updateCursor(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag12updateCursorEN2Qt10DropActionE(
    QBasicDrag *self,
    Qt::DropAction action) {
  self->updateCursor(action);
}

//  bool QBasicDrag::canDrop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBasicDrag7canDropEv(const QBasicDrag *self) {
  return self->canDrop();
}

//  void QBasicDrag::setCanDrop(bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag10setCanDropEb(QBasicDrag *self, bool c) {
  self->setCanDrop(c);
}

//  bool QBasicDrag::useCompositing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QBasicDrag14useCompositingEv(const QBasicDrag *self) {
  return self->useCompositing();
}

//  void QBasicDrag::setUseCompositing(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag17setUseCompositingEb(QBasicDrag *self, bool on) {
  self->setUseCompositing(on);
}

//  void QBasicDrag::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag9setScreenEP7QScreen(
    QBasicDrag *self,
    QScreen *screen) {
  self->setScreen(screen);
}

//  Qt::DropAction QBasicDrag::executedDropAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK10QBasicDrag18executedDropActionEv(
    const QBasicDrag *self) {
  return self->executedDropAction();
}

//  void QBasicDrag::setExecutedDropAction(Qt::DropAction da)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag21setExecutedDropActionEN2Qt10DropActionE(
    QBasicDrag *self,
    Qt::DropAction da) {
  self->setExecutedDropAction(da);
}

//  QDrag *QBasicDrag::drag() const
extern "C" Q_DECL_EXPORT
QDrag *ritual_ZNK10QBasicDrag4dragEv(const QBasicDrag *self) {
  return self->drag();
}

//  void QBasicDrag::enableEventFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag17enableEventFilterEv(QBasicDrag *self) {
  self->enableEventFilter();
}

//  void QBasicDrag::disableEventFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag18disableEventFilterEv(QBasicDrag *self) {
  self->disableEventFilter();
}

//  void QBasicDrag::restoreCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag13restoreCursorEv(QBasicDrag *self) {
  self->restoreCursor();
}

//  void QBasicDrag::exitDndEventLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBasicDrag16exitDndEventLoopEv(QBasicDrag *self) {
  self->exitDndEventLoop();
}

//  QBasicDrag as the QObject it is built on
extern "C" Q_DECL_EXPORT
QObject *ritual_cast_QBasicDrag_QObject(QBasicDrag *self) {
  return static_cast<QObject *>(self);
}

//  a Python function taken by a CuteQBasicDrag, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBasicDrag(QBasicDrag *self, const char *key, void *call) {
  return static_cast<CuteQBasicDrag *>(self)->take(key, call);
}

//  Qt::DropAction QBasicDrag::drag(QDrag *drag)
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_own_ZN10QBasicDrag4dragEP5QDrag(
    QBasicDrag *self,
    QDrag *drag) {
  return self->QBasicDrag::drag(drag);
}

//  void QBasicDrag::cancelDrag()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBasicDrag10cancelDragEv(QBasicDrag *self) {
  self->QBasicDrag::cancelDrag();
}

//  bool QBasicDrag::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QBasicDrag11eventFilterEP7QObjectP6QEvent(
    QBasicDrag *self,
    QObject *o,
    QEvent *e) {
  return self->QBasicDrag::eventFilter(o, e);
}

//  void QBasicDrag::startDrag()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBasicDrag9startDragEv(QBasicDrag *self) {
  static_cast<OwnQBasicDrag *>(self)->OwnQBasicDrag::startDrag();
}

//  void QBasicDrag::cancel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBasicDrag6cancelEv(QBasicDrag *self) {
  static_cast<OwnQBasicDrag *>(self)->OwnQBasicDrag::cancel();
}

//  void QBasicDrag::endDrag()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QBasicDrag7endDragEv(QBasicDrag *self) {
  static_cast<OwnQBasicDrag *>(self)->OwnQBasicDrag::endDrag();
}

#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(draganddrop)
