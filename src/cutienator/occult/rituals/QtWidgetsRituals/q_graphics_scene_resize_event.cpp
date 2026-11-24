//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QGraphicsSceneResizeEvent that Python can take functions over in. Every QGraphicsSceneResizeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneResizeEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneResizeEventCall1)(const void *, int *);
class CuteQGraphicsSceneResizeEvent : public QGraphicsSceneResizeEvent {
public:
  using QGraphicsSceneResizeEvent::QGraphicsSceneResizeEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSceneResizeEventCall0 call = reinterpret_cast<CuteQGraphicsSceneResizeEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneResizeEventCall1 call = reinterpret_cast<CuteQGraphicsSceneResizeEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneResizeEvent::QGraphicsSceneResizeEvent()
extern "C" Q_DECL_EXPORT
QGraphicsSceneResizeEvent *ritual_ZN25QGraphicsSceneResizeEventC1Ev() {
  return new CuteQGraphicsSceneResizeEvent();
}

//  QGraphicsSceneResizeEvent::~QGraphicsSceneResizeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneResizeEventD1Ev(
    QGraphicsSceneResizeEvent *self) {
  delete self;
}

//  QSizeF QGraphicsSceneResizeEvent::oldSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK25QGraphicsSceneResizeEvent7oldSizeEv(
    const QGraphicsSceneResizeEvent *self) {
  return new QSizeF(self->oldSize());
}

//  void QGraphicsSceneResizeEvent::setOldSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneResizeEvent10setOldSizeERK6QSizeF(
    QGraphicsSceneResizeEvent *self,
    const QSizeF *size) {
  self->setOldSize(*size);
}

//  QSizeF QGraphicsSceneResizeEvent::newSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK25QGraphicsSceneResizeEvent7newSizeEv(
    const QGraphicsSceneResizeEvent *self) {
  return new QSizeF(self->newSize());
}

//  void QGraphicsSceneResizeEvent::setNewSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneResizeEvent10setNewSizeERK6QSizeF(
    QGraphicsSceneResizeEvent *self,
    const QSizeF *size) {
  self->setNewSize(*size);
}

//  a Python function taken by a CuteQGraphicsSceneResizeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneResizeEvent(
    QGraphicsSceneResizeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneResizeEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
