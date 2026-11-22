//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

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
  return new QDragMoveEvent(
      *pos,
      QFlags<Qt::DropAction>::fromInt(actions),
      data,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      type);
}

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
  return new QDragMoveEvent(
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
