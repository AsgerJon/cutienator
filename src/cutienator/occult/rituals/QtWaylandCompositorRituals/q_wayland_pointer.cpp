//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandpointer.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandpointer.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *QWaylandPointer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QWaylandPointer10metaObjectEv(
    const QWaylandPointer *self) {
  return self->metaObject();
}

//  void *QWaylandPointer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QWaylandPointer11qt_metacastEPKc(
    QWaylandPointer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandPointer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QWaylandPointer11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandPointer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandPointer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QWaylandPointer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandPointer::tr(s, c, n));
}

//  QWaylandPointerPrivate *QWaylandPointer::d_func()
extern "C" Q_DECL_EXPORT
QWaylandPointerPrivate *ritual_ZN15QWaylandPointer6d_funcEv(
    QWaylandPointer *self) {
  return self->d_func();
}

//  const QWaylandPointerPrivate *QWaylandPointer::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandPointerPrivate *ritual_ZNK15QWaylandPointer6d_funcEv(
    const QWaylandPointer *self) {
  return self->d_func();
}

//  QWaylandPointer::QWaylandPointer(QWaylandSeat *seat, QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandPointer *ritual_ZN15QWaylandPointerC1EP12QWaylandSeatP7QObject(
    QWaylandSeat *seat,
    QObject *parent) {
  return new QWaylandPointer(seat, parent);
}

//  QWaylandSeat *QWaylandPointer::seat() const
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZNK15QWaylandPointer4seatEv(
    const QWaylandPointer *self) {
  return self->seat();
}

//  QWaylandCompositor *QWaylandPointer::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK15QWaylandPointer10compositorEv(
    const QWaylandPointer *self) {
  return self->compositor();
}

//  QWaylandOutput *QWaylandPointer::output() const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZNK15QWaylandPointer6outputEv(
    const QWaylandPointer *self) {
  return self->output();
}

//  void QWaylandPointer::setOutput(QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer9setOutputEP14QWaylandOutput(
    QWaylandPointer *self,
    QWaylandOutput *output) {
  self->setOutput(output);
}

//  uint QWaylandPointer::sendMousePressEvent(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
uint ritual_ZN15QWaylandPointer19sendMousePressEventEN2Qt11MouseButtonE(
    QWaylandPointer *self,
    Qt::MouseButton button) {
  return self->sendMousePressEvent(button);
}

//  uint QWaylandPointer::sendMouseReleaseEvent(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
uint ritual_ZN15QWaylandPointer21sendMouseReleaseEventEN2Qt11MouseButtonE(
    QWaylandPointer *self,
    Qt::MouseButton button) {
  return self->sendMouseReleaseEvent(button);
}

//  void QWaylandPointer::sendMouseMoveEvent(QWaylandView *view, const
//      QPointF &localPos, const QPointF &outputSpacePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer18sendMouseMoveEventEP12QWaylandViewRK7QPointFS4_(
    QWaylandPointer *self,
    QWaylandView *view,
    const QPointF *localPos,
    const QPointF *outputSpacePos) {
  self->sendMouseMoveEvent(view, *localPos, *outputSpacePos);
}

//  void QWaylandPointer::sendMouseWheelEvent(Qt::Orientation orientation,
//      int delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer19sendMouseWheelEventEN2Qt11OrientationEi(
    QWaylandPointer *self,
    Qt::Orientation orientation,
    int delta) {
  self->sendMouseWheelEvent(orientation, delta);
}

//  QWaylandView *QWaylandPointer::mouseFocus() const
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_ZNK15QWaylandPointer10mouseFocusEv(
    const QWaylandPointer *self) {
  return self->mouseFocus();
}

//  QPointF QWaylandPointer::currentLocalPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QWaylandPointer20currentLocalPositionEv(
    const QWaylandPointer *self) {
  return new QPointF(self->currentLocalPosition());
}

//  QPointF QWaylandPointer::currentSpacePosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QWaylandPointer20currentSpacePositionEv(
    const QWaylandPointer *self) {
  return new QPointF(self->currentSpacePosition());
}

//  bool QWaylandPointer::isButtonPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWaylandPointer15isButtonPressedEv(
    const QWaylandPointer *self) {
  return self->isButtonPressed();
}

//  void QWaylandPointer::addClient(QWaylandClient *client, uint32_t id,
//      uint32_t version)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer9addClientEP14QWaylandClientjj(
    QWaylandPointer *self,
    QWaylandClient *client,
    uint32_t id,
    uint32_t version) {
  self->addClient(client, id, version);
}

//  wl_resource *QWaylandPointer::focusResource() const
extern "C" Q_DECL_EXPORT
wl_resource *ritual_ZNK15QWaylandPointer13focusResourceEv(
    const QWaylandPointer *self) {
  return self->focusResource();
}

//  uint32_t QWaylandPointer::toWaylandButton(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
uint32_t ritual_ZN15QWaylandPointer15toWaylandButtonEN2Qt11MouseButtonE(
    Qt::MouseButton button) {
  return QWaylandPointer::toWaylandButton(button);
}

//  uint QWaylandPointer::sendButton(struct wl_resource *resource, uint32_t
//      time, Qt::MouseButton button, uint32_t state)
extern "C" Q_DECL_EXPORT
uint ritual_ZN15QWaylandPointer10sendButtonEP11wl_resourcejN2Qt11MouseButtonEj(
    QWaylandPointer *self,
    struct wl_resource *resource,
    uint32_t time,
    Qt::MouseButton button,
    uint32_t state) {
  return self->sendButton(resource, time, button, state);
}

//  void QWaylandPointer::outputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer13outputChangedEv(QWaylandPointer *self) {
  self->outputChanged();
}

//  void QWaylandPointer::buttonPressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer20buttonPressedChangedEv(
    QWaylandPointer *self) {
  self->buttonPressedChanged();
}

//  void QWaylandPointer::enteredSurfaceDestroyed(void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer23enteredSurfaceDestroyedEPv(
    QWaylandPointer *self,
    void *data) {
  self->enteredSurfaceDestroyed(data);
}

//  void QWaylandPointer::pointerFocusChanged(QWaylandView *newFocus,
//      QWaylandView *oldFocus)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandPointer19pointerFocusChangedEP12QWaylandViewS1_(
    QWaylandPointer *self,
    QWaylandView *newFocus,
    QWaylandView *oldFocus) {
  self->pointerFocusChanged(newFocus, oldFocus);
}

//  uint QWaylandPointer::sendMousePressEvent(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
uint ritual_own_ZN15QWaylandPointer19sendMousePressEventEN2Qt11MouseButtonE(
    QWaylandPointer *self,
    Qt::MouseButton button) {
  return self->QWaylandPointer::sendMousePressEvent(button);
}

//  uint QWaylandPointer::sendMouseReleaseEvent(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
uint ritual_own_ZN15QWaylandPointer21sendMouseReleaseEventEN2Qt11MouseButtonE(
    QWaylandPointer *self,
    Qt::MouseButton button) {
  return self->QWaylandPointer::sendMouseReleaseEvent(button);
}

//  void QWaylandPointer::sendMouseMoveEvent(QWaylandView *view, const
//      QPointF &localPos, const QPointF &outputSpacePos)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QWaylandPointer18sendMouseMoveEventEP12QWaylandViewRK7QPointFS4_(
    QWaylandPointer *self,
    QWaylandView *view,
    const QPointF *localPos,
    const QPointF *outputSpacePos) {
  self->QWaylandPointer::sendMouseMoveEvent(
      view,
      *localPos,
      *outputSpacePos);
}

//  void QWaylandPointer::sendMouseWheelEvent(Qt::Orientation orientation,
//      int delta)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QWaylandPointer19sendMouseWheelEventEN2Qt11OrientationEi(
    QWaylandPointer *self,
    Qt::Orientation orientation,
    int delta) {
  self->QWaylandPointer::sendMouseWheelEvent(orientation, delta);
}

//  void QWaylandPointer::addClient(QWaylandClient *client, uint32_t id,
//      uint32_t version)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QWaylandPointer9addClientEP14QWaylandClientjj(
    QWaylandPointer *self,
    QWaylandClient *client,
    uint32_t id,
    uint32_t version) {
  self->QWaylandPointer::addClient(client, id, version);
}
