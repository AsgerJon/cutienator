//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandkeyboard.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandkeyboard.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QWaylandKeyboard::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QWaylandKeyboard10metaObjectEv(
    const QWaylandKeyboard *self) {
  return self->metaObject();
}

//  void *QWaylandKeyboard::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QWaylandKeyboard11qt_metacastEPKc(
    QWaylandKeyboard *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandKeyboard::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QWaylandKeyboard11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandKeyboard *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandKeyboard::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QWaylandKeyboard2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandKeyboard::tr(s, c, n));
}

//  QWaylandKeyboardPrivate *QWaylandKeyboard::d_func()
extern "C" Q_DECL_EXPORT
QWaylandKeyboardPrivate *ritual_ZN16QWaylandKeyboard6d_funcEv(
    QWaylandKeyboard *self) {
  return self->d_func();
}

//  const QWaylandKeyboardPrivate *QWaylandKeyboard::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandKeyboardPrivate *ritual_ZNK16QWaylandKeyboard6d_funcEv(
    const QWaylandKeyboard *self) {
  return self->d_func();
}

//  QWaylandKeyboard::QWaylandKeyboard(QWaylandSeat *seat, QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandKeyboard *ritual_ZN16QWaylandKeyboardC1EP12QWaylandSeatP7QObject(
    QWaylandSeat *seat,
    QObject *parent) {
  return new QWaylandKeyboard(seat, parent);
}

//  QWaylandSeat *QWaylandKeyboard::seat() const
extern "C" Q_DECL_EXPORT
QWaylandSeat *ritual_ZNK16QWaylandKeyboard4seatEv(
    const QWaylandKeyboard *self) {
  return self->seat();
}

//  QWaylandCompositor *QWaylandKeyboard::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK16QWaylandKeyboard10compositorEv(
    const QWaylandKeyboard *self) {
  return self->compositor();
}

//  quint32 QWaylandKeyboard::repeatRate() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QWaylandKeyboard10repeatRateEv(
    const QWaylandKeyboard *self) {
  return self->repeatRate();
}

//  void QWaylandKeyboard::setRepeatRate(quint32 rate)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard13setRepeatRateEj(
    QWaylandKeyboard *self,
    quint32 rate) {
  self->setRepeatRate(rate);
}

//  quint32 QWaylandKeyboard::repeatDelay() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QWaylandKeyboard11repeatDelayEv(
    const QWaylandKeyboard *self) {
  return self->repeatDelay();
}

//  void QWaylandKeyboard::setRepeatDelay(quint32 delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard14setRepeatDelayEj(
    QWaylandKeyboard *self,
    quint32 delay) {
  self->setRepeatDelay(delay);
}

//  void QWaylandKeyboard::setFocus(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard8setFocusEP15QWaylandSurface(
    QWaylandKeyboard *self,
    QWaylandSurface *surface) {
  self->setFocus(surface);
}

//  void QWaylandKeyboard::sendKeyModifiers(QWaylandClient *client, uint32_t
//      serial)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard16sendKeyModifiersEP14QWaylandClientj(
    QWaylandKeyboard *self,
    QWaylandClient *client,
    uint32_t serial) {
  self->sendKeyModifiers(client, serial);
}

//  void QWaylandKeyboard::sendKeyPressEvent(uint code)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard17sendKeyPressEventEj(
    QWaylandKeyboard *self,
    uint code) {
  self->sendKeyPressEvent(code);
}

//  void QWaylandKeyboard::sendKeyReleaseEvent(uint code)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard19sendKeyReleaseEventEj(
    QWaylandKeyboard *self,
    uint code) {
  self->sendKeyReleaseEvent(code);
}

//  QWaylandSurface *QWaylandKeyboard::focus() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK16QWaylandKeyboard5focusEv(
    const QWaylandKeyboard *self) {
  return self->focus();
}

//  QWaylandClient *QWaylandKeyboard::focusClient() const
extern "C" Q_DECL_EXPORT
QWaylandClient *ritual_ZNK16QWaylandKeyboard11focusClientEv(
    const QWaylandKeyboard *self) {
  return self->focusClient();
}

//  void QWaylandKeyboard::addClient(QWaylandClient *client, uint32_t id,
//      uint32_t version)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard9addClientEP14QWaylandClientjj(
    QWaylandKeyboard *self,
    QWaylandClient *client,
    uint32_t id,
    uint32_t version) {
  self->addClient(client, id, version);
}

//  uint QWaylandKeyboard::keyToScanCode(int qtKey) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QWaylandKeyboard13keyToScanCodeEi(
    const QWaylandKeyboard *self,
    int qtKey) {
  return self->keyToScanCode(qtKey);
}

//  void QWaylandKeyboard::focusChanged(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard12focusChangedEP15QWaylandSurface(
    QWaylandKeyboard *self,
    QWaylandSurface *surface) {
  self->focusChanged(surface);
}

//  void QWaylandKeyboard::repeatRateChanged(quint32 repeatRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard17repeatRateChangedEj(
    QWaylandKeyboard *self,
    quint32 repeatRate) {
  self->repeatRateChanged(repeatRate);
}

//  void QWaylandKeyboard::repeatDelayChanged(quint32 repeatDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard18repeatDelayChangedEj(
    QWaylandKeyboard *self,
    quint32 repeatDelay) {
  self->repeatDelayChanged(repeatDelay);
}

//  void QWaylandKeyboard::focusDestroyed(void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard14focusDestroyedEPv(
    QWaylandKeyboard *self,
    void *data) {
  self->focusDestroyed(data);
}

//  void QWaylandKeyboard::updateKeymap()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandKeyboard12updateKeymapEv(QWaylandKeyboard *self) {
  self->updateKeymap();
}

//  void QWaylandKeyboard::setFocus(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QWaylandKeyboard8setFocusEP15QWaylandSurface(
    QWaylandKeyboard *self,
    QWaylandSurface *surface) {
  self->QWaylandKeyboard::setFocus(surface);
}

//  void QWaylandKeyboard::sendKeyModifiers(QWaylandClient *client, uint32_t
//      serial)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QWaylandKeyboard16sendKeyModifiersEP14QWaylandClientj(
    QWaylandKeyboard *self,
    QWaylandClient *client,
    uint32_t serial) {
  self->QWaylandKeyboard::sendKeyModifiers(client, serial);
}

//  void QWaylandKeyboard::sendKeyPressEvent(uint code)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QWaylandKeyboard17sendKeyPressEventEj(
    QWaylandKeyboard *self,
    uint code) {
  self->QWaylandKeyboard::sendKeyPressEvent(code);
}

//  void QWaylandKeyboard::sendKeyReleaseEvent(uint code)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QWaylandKeyboard19sendKeyReleaseEventEj(
    QWaylandKeyboard *self,
    uint code) {
  self->QWaylandKeyboard::sendKeyReleaseEvent(code);
}

//  void QWaylandKeyboard::addClient(QWaylandClient *client, uint32_t id,
//      uint32_t version)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QWaylandKeyboard9addClientEP14QWaylandClientjj(
    QWaylandKeyboard *self,
    QWaylandClient *client,
    uint32_t id,
    uint32_t version) {
  self->QWaylandKeyboard::addClient(client, id, version);
}
