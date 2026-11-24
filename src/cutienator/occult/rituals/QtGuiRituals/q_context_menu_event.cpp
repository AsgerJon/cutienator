//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_CONTEXTMENU)
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QContextMenuEvent that Python can take functions over in. Every QContextMenuEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_CONTEXTMENU)
typedef void * (*CuteQContextMenuEventCall0)(const void *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteQContextMenuEventCall1)(const void *, quint64, int *);
typedef void (*CuteQContextMenuEventCall2)(const void *, bool, int *);
class CuteQContextMenuEvent : public QContextMenuEvent {
public:
  using QContextMenuEvent::QContextMenuEvent;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN11QInputEvent12setTimestampEy")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  QContextMenuEvent *QContextMenuEvent::clone() const
  QContextMenuEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQContextMenuEventCall0 call = reinterpret_cast<CuteQContextMenuEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QContextMenuEvent *>(given);
    }
    return QContextMenuEvent::clone();
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

  //  void QInputEvent::setTimestamp(quint64 timestamp)
  void setTimestamp(quint64 timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQContextMenuEventCall1 call = reinterpret_cast<CuteQContextMenuEventCall1>(taken[1]);
      call(this, timestamp, &handled);
      if (handled) return;
    }
    QInputEvent::setTimestamp(timestamp);
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[2]) {
      int handled = 0;
      CuteQContextMenuEventCall2 call = reinterpret_cast<CuteQContextMenuEventCall2>(taken[2]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QContextMenuEvent *QContextMenuEvent::clone() const
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_ZNK17QContextMenuEvent5cloneEv(
    const QContextMenuEvent *self) {
  return self->clone();
}

//  QContextMenuEvent::~QContextMenuEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QContextMenuEventD1Ev(QContextMenuEvent *self) {
  delete self;
}

//  QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos,
//      const QPoint &globalPos, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_ZN17QContextMenuEventC1ENS_6ReasonERK6QPointS3_6QFlagsIN2Qt16KeyboardModifierEE(
    QContextMenuEvent::Reason reason,
    const QPoint *pos,
    const QPoint *globalPos,
    int modifiers) {
  return new CuteQContextMenuEvent(
      reason,
      *pos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

#if QT_DEPRECATED_SINCE(6, 4)
//  QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos)
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_ZN17QContextMenuEventC1ENS_6ReasonERK6QPoint(
    QContextMenuEvent::Reason reason,
    const QPoint *pos) {
  return new CuteQContextMenuEvent(reason, *pos);
}
#endif  // QT_DEPRECATED_SINCE(6, 4)

//  int QContextMenuEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent1xEv(const QContextMenuEvent *self) {
  return self->x();
}

//  int QContextMenuEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent1yEv(const QContextMenuEvent *self) {
  return self->y();
}

//  int QContextMenuEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent7globalXEv(const QContextMenuEvent *self) {
  return self->globalX();
}

//  int QContextMenuEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent7globalYEv(const QContextMenuEvent *self) {
  return self->globalY();
}

//  const QPoint &QContextMenuEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QContextMenuEvent3posEv(const QContextMenuEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint &QContextMenuEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QContextMenuEvent9globalPosEv(
    const QContextMenuEvent *self) {
  return new QPoint(self->globalPos());
}

//  Reason QContextMenuEvent::reason() const
extern "C" Q_DECL_EXPORT
QContextMenuEvent::Reason ritual_ZNK17QContextMenuEvent6reasonEv(
    const QContextMenuEvent *self) {
  return self->reason();
}

//  a Python function taken by a CuteQContextMenuEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QContextMenuEvent(
    QContextMenuEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQContextMenuEvent *>(self)->take(key, call);
}

//  QContextMenuEvent *QContextMenuEvent::clone() const
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_own_ZNK17QContextMenuEvent5cloneEv(
    const QContextMenuEvent *self) {
  return self->QContextMenuEvent::clone();
}

#endif  // !defined(QT_NO_CONTEXTMENU)
