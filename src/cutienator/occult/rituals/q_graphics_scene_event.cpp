//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>

//  QGraphicsSceneEvent::QGraphicsSceneEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneEvent *ritual_ZN19QGraphicsSceneEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new QGraphicsSceneEvent(type);
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
