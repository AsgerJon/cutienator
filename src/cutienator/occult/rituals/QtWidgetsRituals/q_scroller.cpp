//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qscroller.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(scroller)
#include <QtWidgets/qscroller.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtWidgets/qscrollerproperties.h>
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QScroller::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QScroller10metaObjectEv(
    const QScroller *self) {
  return self->metaObject();
}

//  QString QScroller::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QScroller2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScroller::tr(s, c, n));
}

//  bool QScroller::hasScroller(QObject *target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QScroller11hasScrollerEP7QObject(QObject *target) {
  return QScroller::hasScroller(target);
}

//  QScroller *QScroller::scroller(QObject *target)
extern "C" Q_DECL_EXPORT
QScroller *ritual_ZN9QScroller8scrollerEP7QObject(QObject *target) {
  return QScroller::scroller(target);
}

//  const QScroller *QScroller::scroller(const QObject *target)
extern "C" Q_DECL_EXPORT
const QScroller *ritual_ZN9QScroller8scrollerEPK7QObject(
    const QObject *target) {
  return QScroller::scroller(target);
}

#if !defined(QT_NO_GESTURES)
//  Qt::GestureType QScroller::grabGesture(QObject *target,
//      ScrollerGestureType gestureType)
extern "C" Q_DECL_EXPORT
Qt::GestureType ritual_ZN9QScroller11grabGestureEP7QObjectNS_19ScrollerGestureTypeE(
    QObject *target,
    QScroller::ScrollerGestureType gestureType) {
  return QScroller::grabGesture(target, gestureType);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  Qt::GestureType QScroller::grabbedGesture(QObject *target)
extern "C" Q_DECL_EXPORT
Qt::GestureType ritual_ZN9QScroller14grabbedGestureEP7QObject(
    QObject *target) {
  return QScroller::grabbedGesture(target);
}
#endif  // !defined(QT_NO_GESTURES)

#if !defined(QT_NO_GESTURES)
//  void QScroller::ungrabGesture(QObject *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller13ungrabGestureEP7QObject(QObject *target) {
  QScroller::ungrabGesture(target);
}
#endif  // !defined(QT_NO_GESTURES)

//  QList<QScroller *> QScroller::activeScrollers()
extern "C" Q_DECL_EXPORT
QList<QScroller *> *ritual_ZN9QScroller15activeScrollersEv() {
  return new QList<QScroller *>(QScroller::activeScrollers());
}

//  QObject *QScroller::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK9QScroller6targetEv(const QScroller *self) {
  return self->target();
}

//  State QScroller::state() const
extern "C" Q_DECL_EXPORT
QScroller::State ritual_ZNK9QScroller5stateEv(const QScroller *self) {
  return self->state();
}

//  bool QScroller::handleInput(Input input, const QPointF &position, qint64
//      timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QScroller11handleInputENS_5InputERK7QPointFx(
    QScroller *self,
    QScroller::Input input,
    const QPointF *position,
    qint64 timestamp) {
  return self->handleInput(input, *position, timestamp);
}

//  void QScroller::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller4stopEv(QScroller *self) {
  self->stop();
}

//  QPointF QScroller::velocity() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QScroller8velocityEv(const QScroller *self) {
  return new QPointF(self->velocity());
}

//  QPointF QScroller::finalPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QScroller13finalPositionEv(const QScroller *self) {
  return new QPointF(self->finalPosition());
}

//  QPointF QScroller::pixelPerMeter() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QScroller13pixelPerMeterEv(const QScroller *self) {
  return new QPointF(self->pixelPerMeter());
}

//  QScrollerProperties QScroller::scrollerProperties() const
extern "C" Q_DECL_EXPORT
QScrollerProperties *ritual_ZNK9QScroller18scrollerPropertiesEv(
    const QScroller *self) {
  return new QScrollerProperties(self->scrollerProperties());
}

//  void QScroller::setSnapPositionsX(qreal first, qreal interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller17setSnapPositionsXEdd(
    QScroller *self,
    qreal first,
    qreal interval) {
  self->setSnapPositionsX(first, interval);
}

//  void QScroller::setSnapPositionsY(qreal first, qreal interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller17setSnapPositionsYEdd(
    QScroller *self,
    qreal first,
    qreal interval) {
  self->setSnapPositionsY(first, interval);
}

//  void QScroller::setScrollerProperties(const QScrollerProperties &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller21setScrollerPropertiesERK19QScrollerProperties(
    QScroller *self,
    const QScrollerProperties *prop) {
  self->setScrollerProperties(*prop);
}

//  void QScroller::scrollTo(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller8scrollToERK7QPointF(
    QScroller *self,
    const QPointF *pos) {
  self->scrollTo(*pos);
}

//  void QScroller::scrollTo(const QPointF &pos, int scrollTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller8scrollToERK7QPointFi(
    QScroller *self,
    const QPointF *pos,
    int scrollTime) {
  self->scrollTo(*pos, scrollTime);
}

//  void QScroller::ensureVisible(const QRectF &rect, qreal xmargin, qreal
//      ymargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller13ensureVisibleERK6QRectFdd(
    QScroller *self,
    const QRectF *rect,
    qreal xmargin,
    qreal ymargin) {
  self->ensureVisible(*rect, xmargin, ymargin);
}

//  void QScroller::ensureVisible(const QRectF &rect, qreal xmargin, qreal
//      ymargin, int scrollTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller13ensureVisibleERK6QRectFddi(
    QScroller *self,
    const QRectF *rect,
    qreal xmargin,
    qreal ymargin,
    int scrollTime) {
  self->ensureVisible(*rect, xmargin, ymargin, scrollTime);
}

//  void QScroller::resendPrepareEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScroller18resendPrepareEventEv(QScroller *self) {
  self->resendPrepareEvent();
}

//  QScroller::QScroller(QObject *target)
extern "C" Q_DECL_EXPORT
QScroller *ritual_ZN9QScrollerC1EP7QObject(QObject *target) {
  return new QScroller(target);
}

//  QScroller::~QScroller()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QScrollerD1Ev(QScroller *self) {
  delete self;
}

//  QScrollerPrivate *QScroller::d_func()
extern "C" Q_DECL_EXPORT
QScrollerPrivate *ritual_ZN9QScroller6d_funcEv(QScroller *self) {
  return self->d_func();
}

//  const QScrollerPrivate *QScroller::d_func() const
extern "C" Q_DECL_EXPORT
const QScrollerPrivate *ritual_ZNK9QScroller6d_funcEv(
    const QScroller *self) {
  return self->d_func();
}

//  QList<QScroller *>::QList()
extern "C" Q_DECL_EXPORT
QList<QScroller *> *ritual_list_make_QScroller_ptr() {
  return new QList<QScroller *>();
}

//  void QList<QScroller *>::append(const QScroller * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QScroller_ptr(
    QList<QScroller *> *self,
    QScroller *element) {
  self->append(element);
}

//  qsizetype QList<QScroller *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QScroller_ptr(const QList<QScroller *> *self) {
  return self->size();
}

//  const QScroller * &QList<QScroller *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QScroller *ritual_list_at_QScroller_ptr(
    const QList<QScroller *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QScroller *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QScroller_ptr(QList<QScroller *> *self) {
  delete self;
}

#endif  // QT_CONFIG(scroller)
