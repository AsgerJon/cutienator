//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QMouseEvent *QMouseEvent::clone() const
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZNK11QMouseEvent5cloneEv(const QMouseEvent *self) {
  return self->clone();
}

//  QMouseEvent::~QMouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMouseEventD1Ev(QMouseEvent *self) {
  delete self;
}

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos,
//      Qt::MouseButton button, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFN2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    const QPointingDevice *device) {
  return new QMouseEvent(
      type,
      *localPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
//      QPointF &globalPos, Qt::MouseButton button, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_N2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    const QPointingDevice *device) {
  return new QMouseEvent(
      type,
      *localPos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
//      QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton button,
//      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, const
//      QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_S4_N2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    const QPointingDevice *device) {
  return new QMouseEvent(
      type,
      *localPos,
      *scenePos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
//      QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton button,
//      Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
//      Qt::MouseEventSource source, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QMouseEvent *ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_S4_N2Qt11MouseButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEENS5_16MouseEventSourceEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    Qt::MouseButton button,
    int buttons,
    int modifiers,
    Qt::MouseEventSource source,
    const QPointingDevice *device) {
  return new QMouseEvent(
      type,
      *localPos,
      *scenePos,
      *globalPos,
      button,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      source,
      device);
}

//  QPoint QMouseEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QMouseEvent3posEv(const QMouseEvent *self) {
  return new QPoint(self->pos());
}

//  QPoint QMouseEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QMouseEvent9globalPosEv(const QMouseEvent *self) {
  return new QPoint(self->globalPos());
}

//  int QMouseEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent1xEv(const QMouseEvent *self) {
  return self->x();
}

//  int QMouseEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent1yEv(const QMouseEvent *self) {
  return self->y();
}

//  int QMouseEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent7globalXEv(const QMouseEvent *self) {
  return self->globalX();
}

//  int QMouseEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent7globalYEv(const QMouseEvent *self) {
  return self->globalY();
}

//  QPointF QMouseEvent::localPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QMouseEvent8localPosEv(const QMouseEvent *self) {
  return new QPointF(self->localPos());
}

//  QPointF QMouseEvent::windowPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QMouseEvent9windowPosEv(const QMouseEvent *self) {
  return new QPointF(self->windowPos());
}

//  QPointF QMouseEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QMouseEvent9screenPosEv(const QMouseEvent *self) {
  return new QPointF(self->screenPos());
}

//  Qt::MouseEventSource QMouseEvent::source() const
extern "C" Q_DECL_EXPORT
Qt::MouseEventSource ritual_ZNK11QMouseEvent6sourceEv(
    const QMouseEvent *self) {
  return self->source();
}

//  Qt::MouseEventFlags QMouseEvent::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QMouseEvent5flagsEv(const QMouseEvent *self) {
  return static_cast<int>(self->flags().toInt());
}
