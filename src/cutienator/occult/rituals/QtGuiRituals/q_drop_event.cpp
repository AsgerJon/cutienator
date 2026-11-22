//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QDropEvent *QDropEvent::clone() const
extern "C" Q_DECL_EXPORT
QDropEvent *ritual_ZNK10QDropEvent5cloneEv(const QDropEvent *self) {
  return self->clone();
}

//  QDropEvent::~QDropEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDropEventD1Ev(QDropEvent *self) {
  delete self;
}

//  QDropEvent::QDropEvent(const QPointF &pos, Qt::DropActions actions, const
//      QMimeData *data, Qt::MouseButtons buttons, Qt::KeyboardModifiers
//      modifiers, Type type)
extern "C" Q_DECL_EXPORT
QDropEvent *ritual_ZN10QDropEventC1ERK7QPointF6QFlagsIN2Qt10DropActionEEPK9QMimeDataS3_INS4_11MouseButtonEES3_INS4_16KeyboardModifierEEN6QEvent4TypeE(
    const QPointF *pos,
    int actions,
    const QMimeData *data,
    int buttons,
    int modifiers,
    QEvent::Type type) {
  return new QDropEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      type);
}

//  QPoint QDropEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QDropEvent3posEv(const QDropEvent *self) {
  return new QPoint(self->pos());
}

//  QPointF QDropEvent::posF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QDropEvent4posFEv(const QDropEvent *self) {
  return new QPointF(self->posF());
}

//  Qt::MouseButtons QDropEvent::mouseButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QDropEvent12mouseButtonsEv(const QDropEvent *self) {
  return static_cast<int>(self->mouseButtons().toInt());
}

//  Qt::KeyboardModifiers QDropEvent::keyboardModifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QDropEvent17keyboardModifiersEv(const QDropEvent *self) {
  return static_cast<int>(self->keyboardModifiers().toInt());
}

//  QPointF QDropEvent::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QDropEvent8positionEv(const QDropEvent *self) {
  return new QPointF(self->position());
}

//  Qt::MouseButtons QDropEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QDropEvent7buttonsEv(const QDropEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  Qt::KeyboardModifiers QDropEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QDropEvent9modifiersEv(const QDropEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  Qt::DropActions QDropEvent::possibleActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QDropEvent15possibleActionsEv(const QDropEvent *self) {
  return static_cast<int>(self->possibleActions().toInt());
}

//  Qt::DropAction QDropEvent::proposedAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK10QDropEvent14proposedActionEv(
    const QDropEvent *self) {
  return self->proposedAction();
}

//  void QDropEvent::acceptProposedAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDropEvent20acceptProposedActionEv(QDropEvent *self) {
  self->acceptProposedAction();
}

//  Qt::DropAction QDropEvent::dropAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK10QDropEvent10dropActionEv(const QDropEvent *self) {
  return self->dropAction();
}

//  void QDropEvent::setDropAction(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDropEvent13setDropActionEN2Qt10DropActionE(
    QDropEvent *self,
    Qt::DropAction action) {
  self->setDropAction(action);
}

//  QObject *QDropEvent::source() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK10QDropEvent6sourceEv(const QDropEvent *self) {
  return self->source();
}

//  const QMimeData *QDropEvent::mimeData() const
extern "C" Q_DECL_EXPORT
const QMimeData *ritual_ZNK10QDropEvent8mimeDataEv(const QDropEvent *self) {
  return self->mimeData();
}
