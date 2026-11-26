//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformcursor.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformcursor.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcursor.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  void QPlatformCursor::pointerEvent(const QMouseEvent &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor12pointerEventERK11QMouseEvent(
    QPlatformCursor *self,
    const QMouseEvent *event) {
  self->pointerEvent(*event);
}

#if !defined(QT_NO_CURSOR)
//  void QPlatformCursor::changeCursor(QCursor *windowCursor, QWindow
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor12changeCursorEP7QCursorP7QWindow(
    QPlatformCursor *self,
    QCursor *windowCursor,
    QWindow *window) {
  self->changeCursor(windowCursor, window);
}
#endif  // !defined(QT_NO_CURSOR)

#if !defined(QT_NO_CURSOR)
//  void QPlatformCursor::setOverrideCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor17setOverrideCursorERK7QCursor(
    QPlatformCursor *self,
    const QCursor *a0) {
  self->setOverrideCursor(*a0);
}
#endif  // !defined(QT_NO_CURSOR)

#if !defined(QT_NO_CURSOR)
//  void QPlatformCursor::clearOverrideCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor19clearOverrideCursorEv(
    QPlatformCursor *self) {
  self->clearOverrideCursor();
}
#endif  // !defined(QT_NO_CURSOR)

//  QPoint QPlatformCursor::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK15QPlatformCursor3posEv(const QPlatformCursor *self) {
  return new QPoint(self->pos());
}

//  void QPlatformCursor::setPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor6setPosERK6QPoint(
    QPlatformCursor *self,
    const QPoint *pos) {
  self->setPos(*pos);
}

//  QSize QPlatformCursor::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QPlatformCursor4sizeEv(const QPlatformCursor *self) {
  return new QSize(self->size());
}

//  Capabilities QPlatformCursor::capabilities()
extern "C" Q_DECL_EXPORT
int ritual_ZN15QPlatformCursor12capabilitiesEv() {
  return static_cast<int>(QPlatformCursor::capabilities().toInt());
}

//  void QPlatformCursor::setCapabilities(Capabilities c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor15setCapabilitiesE6QFlagsINS_10CapabilityEE(
    int c) {
  QPlatformCursor::setCapabilities(
      QFlags<QPlatformCursor::Capability>::fromInt(c));
}

//  void QPlatformCursor::setCapability(Capability c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPlatformCursor13setCapabilityENS_10CapabilityE(
    QPlatformCursor::Capability c) {
  QPlatformCursor::setCapability(c);
}

#if !defined(QT_NO_CURSOR)
//  void QPlatformCursor::setOverrideCursor(const QCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformCursor17setOverrideCursorERK7QCursor(
    QPlatformCursor *self,
    const QCursor *a0) {
  self->QPlatformCursor::setOverrideCursor(*a0);
}
#endif  // !defined(QT_NO_CURSOR)

#if !defined(QT_NO_CURSOR)
//  void QPlatformCursor::clearOverrideCursor()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformCursor19clearOverrideCursorEv(
    QPlatformCursor *self) {
  self->QPlatformCursor::clearOverrideCursor();
}
#endif  // !defined(QT_NO_CURSOR)

//  QPoint QPlatformCursor::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK15QPlatformCursor3posEv(const QPlatformCursor *self) {
  return new QPoint(self->QPlatformCursor::pos());
}

//  void QPlatformCursor::setPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPlatformCursor6setPosERK6QPoint(
    QPlatformCursor *self,
    const QPoint *pos) {
  self->QPlatformCursor::setPos(*pos);
}

//  QSize QPlatformCursor::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK15QPlatformCursor4sizeEv(const QPlatformCursor *self) {
  return new QSize(self->QPlatformCursor::size());
}
