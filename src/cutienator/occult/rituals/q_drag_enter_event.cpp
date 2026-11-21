//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

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
  return new QDragEnterEvent(
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
  return new QDragEnterEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}
