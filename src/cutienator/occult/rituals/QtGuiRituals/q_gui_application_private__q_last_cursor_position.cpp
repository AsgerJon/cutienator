//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qguiapplication_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QGuiApplicationPrivate::QLastCursorPosition::QLastCursorPosition()
extern "C" Q_DECL_EXPORT
QGuiApplicationPrivate::QLastCursorPosition *ritual_ZN22QGuiApplicationPrivate19QLastCursorPositionC1Ev() {
  return new QGuiApplicationPrivate::QLastCursorPosition();
}

//  QGuiApplicationPrivate::QLastCursorPosition::QLastCursorPosition(QPointF
//      p)
extern "C" Q_DECL_EXPORT
QGuiApplicationPrivate::QLastCursorPosition *ritual_ZN22QGuiApplicationPrivate19QLastCursorPositionC1E7QPointF(
    const QPointF *p) {
  return new QGuiApplicationPrivate::QLastCursorPosition(*p);
}

//  QPointF QGuiApplicationPrivate::QLastCursorPosition::operator QPointF()
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK22QGuiApplicationPrivate19QLastCursorPositioncv7QPointFEv(
    const QGuiApplicationPrivate::QLastCursorPosition *self) {
  return new QPointF(self->operator QPointF());
}

//  qreal QGuiApplicationPrivate::QLastCursorPosition::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGuiApplicationPrivate19QLastCursorPosition1xEv(
    const QGuiApplicationPrivate::QLastCursorPosition *self) {
  return self->x();
}

//  qreal QGuiApplicationPrivate::QLastCursorPosition::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGuiApplicationPrivate19QLastCursorPosition1yEv(
    const QGuiApplicationPrivate::QLastCursorPosition *self) {
  return self->y();
}

//  QPoint QGuiApplicationPrivate::QLastCursorPosition::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK22QGuiApplicationPrivate19QLastCursorPosition7toPointEv(
    const QGuiApplicationPrivate::QLastCursorPosition *self) {
  return new QPoint(self->toPoint());
}

//  void QGuiApplicationPrivate::QLastCursorPosition::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate19QLastCursorPosition5resetEv(
    QGuiApplicationPrivate::QLastCursorPosition *self) {
  self->reset();
}

//  bool operator==(const QLastCursorPosition &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN22QGuiApplicationPrivate19QLastCursorPositionERK7QPointF(
    const QGuiApplicationPrivate::QLastCursorPosition *p1,
    const QPointF *p2) {
  return operator==(*p1, *p2);
}

//  bool operator!=(const QLastCursorPosition &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN22QGuiApplicationPrivate19QLastCursorPositionERK7QPointF(
    const QGuiApplicationPrivate::QLastCursorPosition *p1,
    const QPointF *p2) {
  return operator!=(*p1, *p2);
}

//  bool operator==(const QPointF &p1, const QLastCursorPosition &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK7QPointFRKN22QGuiApplicationPrivate19QLastCursorPositionE(
    const QPointF *p1,
    const QGuiApplicationPrivate::QLastCursorPosition *p2) {
  return operator==(*p1, *p2);
}

//  bool operator!=(const QPointF &p1, const QLastCursorPosition &p2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK7QPointFRKN22QGuiApplicationPrivate19QLastCursorPositionE(
    const QPointF *p1,
    const QGuiApplicationPrivate::QLastCursorPosition *p2) {
  return operator!=(*p1, *p2);
}

//  QGuiApplicationPrivate::QLastCursorPosition::~QLastCursorPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGuiApplicationPrivate19QLastCursorPositionD1Ev(
    QGuiApplicationPrivate::QLastCursorPosition *self) {
  delete self;
}
