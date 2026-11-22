//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QDragEnterEvent that Python can take functions over in. Every QDragEnterEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDragEnterEventCall0)(const void *, int *);
typedef void (*CuteQDragEnterEventCall1)(const void *, bool, int *);
class CuteQDragEnterEvent : public QDragEnterEvent {
public:
  using QDragEnterEvent::QDragEnterEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QDragEnterEvent *QDragEnterEvent::clone() const
  QDragEnterEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDragEnterEventCall0 call = reinterpret_cast<CuteQDragEnterEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDragEnterEvent *>(given);
    }
    return QDragEnterEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDragEnterEventCall1 call = reinterpret_cast<CuteQDragEnterEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QDragEnterEvent *QDragEnterEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragEnterEvent *ritual_ZNK15QDragEnterEvent5cloneEv(
    const QDragEnterEvent *self) {
  return self->clone();
}

//  QDragEnterEvent::~QDragEnterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDragEnterEventD1Ev(QDragEnterEvent *self) {
  delete self;
}

//  QDragEnterEvent::QDragEnterEvent(const QPoint &pos, Qt::DropActions
//      actions, const QMimeData *data, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QDragEnterEvent *ritual_ZN15QDragEnterEventC1ERK6QPoint6QFlagsIN2Qt10DropActionEEPK9QMimeDataS3_INS4_11MouseButtonEES3_INS4_16KeyboardModifierEE(
    const QPoint *pos,
    int actions,
    const QMimeData *data,
    int buttons,
    int modifiers) {
  return new CuteQDragEnterEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QDragEnterEvent::QDragEnterEvent(QPointF pos, Qt::DropActions actions,
//      const QMimeData *data, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QDragEnterEvent *ritual_ZN15QDragEnterEventC1E7QPointF6QFlagsIN2Qt10DropActionEEPK9QMimeDataS1_INS2_11MouseButtonEES1_INS2_16KeyboardModifierEE(
    const QPointF *pos,
    int actions,
    const QMimeData *data,
    int buttons,
    int modifiers) {
  return new CuteQDragEnterEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  a Python function taken by a CuteQDragEnterEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDragEnterEvent(
    QDragEnterEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDragEnterEvent *>(self)->take(key, call);
}

//  QDragEnterEvent *QDragEnterEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragEnterEvent *ritual_own_ZNK15QDragEnterEvent5cloneEv(
    const QDragEnterEvent *self) {
  return self->QDragEnterEvent::clone();
}
