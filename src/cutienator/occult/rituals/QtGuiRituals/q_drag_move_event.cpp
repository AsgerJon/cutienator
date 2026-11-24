//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QDragMoveEvent that Python can take functions over in. Every QDragMoveEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(draganddrop)
typedef void * (*CuteQDragMoveEventCall0)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteQDragMoveEventCall1)(const void *, bool, int *);
class CuteQDragMoveEvent : public QDragMoveEvent {
public:
  using QDragMoveEvent::QDragMoveEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(draganddrop)
  //  QDragMoveEvent *QDragMoveEvent::clone() const
  QDragMoveEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDragMoveEventCall0 call = reinterpret_cast<CuteQDragMoveEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDragMoveEvent *>(given);
    }
    return QDragMoveEvent::clone();
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDragMoveEventCall1 call = reinterpret_cast<CuteQDragMoveEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QDragMoveEvent *QDragMoveEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragMoveEvent *ritual_ZNK14QDragMoveEvent5cloneEv(
    const QDragMoveEvent *self) {
  return self->clone();
}

//  QDragMoveEvent::~QDragMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDragMoveEventD1Ev(QDragMoveEvent *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 16)
//  QDragMoveEvent::QDragMoveEvent(const QPoint &pos, Qt::DropActions
//      actions, const QMimeData *data, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, Type type)
extern "C" Q_DECL_EXPORT
QDragMoveEvent *ritual_ZN14QDragMoveEventC1ERK6QPoint6QFlagsIN2Qt10DropActionEEPK9QMimeDataS3_INS4_11MouseButtonEES3_INS4_16KeyboardModifierEEN6QEvent4TypeE(
    const QPoint *pos,
    int actions,
    const QMimeData *data,
    int buttons,
    int modifiers,
    QEvent::Type type) {
  return new CuteQDragMoveEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      type);
}
#endif  // QT_DEPRECATED_SINCE(6, 16)

//  QDragMoveEvent::QDragMoveEvent(QPointF pos, Qt::DropActions actions,
//      const QMimeData *data, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, Type type)
extern "C" Q_DECL_EXPORT
QDragMoveEvent *ritual_ZN14QDragMoveEventC1E7QPointF6QFlagsIN2Qt10DropActionEEPK9QMimeDataS1_INS2_11MouseButtonEES1_INS2_16KeyboardModifierEEN6QEvent4TypeE(
    const QPointF *pos,
    int actions,
    const QMimeData *data,
    int buttons,
    int modifiers,
    QEvent::Type type) {
  return new CuteQDragMoveEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      type);
}

//  QRect QDragMoveEvent::answerRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QDragMoveEvent10answerRectEv(const QDragMoveEvent *self) {
  return new QRect(self->answerRect());
}

//  void QDragMoveEvent::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDragMoveEvent6acceptEv(QDragMoveEvent *self) {
  self->accept();
}

//  void QDragMoveEvent::ignore()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDragMoveEvent6ignoreEv(QDragMoveEvent *self) {
  self->ignore();
}

//  void QDragMoveEvent::accept(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDragMoveEvent6acceptERK5QRect(
    QDragMoveEvent *self,
    const QRect *r) {
  self->accept(*r);
}

//  void QDragMoveEvent::ignore(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDragMoveEvent6ignoreERK5QRect(
    QDragMoveEvent *self,
    const QRect *r) {
  self->ignore(*r);
}

//  a Python function taken by a CuteQDragMoveEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDragMoveEvent(
    QDragMoveEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDragMoveEvent *>(self)->take(key, call);
}

//  QDragMoveEvent *QDragMoveEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragMoveEvent *ritual_own_ZNK14QDragMoveEvent5cloneEv(
    const QDragMoveEvent *self) {
  return self->QDragMoveEvent::clone();
}

#endif  // QT_CONFIG(draganddrop)
