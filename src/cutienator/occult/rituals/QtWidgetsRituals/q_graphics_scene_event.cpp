//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <cstring>

//  A QGraphicsSceneEvent that Python can take functions over in. Every QGraphicsSceneEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneEventCall1)(const void *, int *);
class CuteQGraphicsSceneEvent : public QGraphicsSceneEvent {
public:
  using QGraphicsSceneEvent::QGraphicsSceneEvent;
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
      CuteQGraphicsSceneEventCall0 call = reinterpret_cast<CuteQGraphicsSceneEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneEventCall1 call = reinterpret_cast<CuteQGraphicsSceneEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneEvent::QGraphicsSceneEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneEvent *ritual_ZN19QGraphicsSceneEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new CuteQGraphicsSceneEvent(type);
}

//  QGraphicsSceneEvent::~QGraphicsSceneEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneEventD1Ev(QGraphicsSceneEvent *self) {
  delete self;
}

//  QWidget *QGraphicsSceneEvent::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QGraphicsSceneEvent6widgetEv(
    const QGraphicsSceneEvent *self) {
  return self->widget();
}

//  void QGraphicsSceneEvent::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneEvent9setWidgetEP7QWidget(
    QGraphicsSceneEvent *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  quint64 QGraphicsSceneEvent::timestamp() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QGraphicsSceneEvent9timestampEv(
    const QGraphicsSceneEvent *self) {
  return self->timestamp();
}

//  void QGraphicsSceneEvent::setTimestamp(quint64 ts)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsSceneEvent12setTimestampEy(
    QGraphicsSceneEvent *self,
    quint64 ts) {
  self->setTimestamp(ts);
}

//  a Python function taken by a CuteQGraphicsSceneEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneEvent(
    QGraphicsSceneEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
