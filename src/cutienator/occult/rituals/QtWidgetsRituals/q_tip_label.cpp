//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtooltip_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtooltip_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QTipLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTipLabel10metaObjectEv(
    const QTipLabel *self) {
  return self->metaObject();
}

//  QString QTipLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTipLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTipLabel::tr(s, c, n));
}

//  QTipLabel::QTipLabel(const QString &text, const QPoint &pos, QWidget *w,
//      int msecDisplayTime)
extern "C" Q_DECL_EXPORT
QTipLabel *ritual_ZN9QTipLabelC1ERK7QStringRK6QPointP7QWidgeti(
    const QString *text,
    const QPoint *pos,
    QWidget *w,
    int msecDisplayTime) {
  return new QTipLabel(*text, *pos, w, msecDisplayTime);
}

//  QTipLabel::~QTipLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabelD1Ev(QTipLabel *self) {
  delete self;
}

//  void QTipLabel::updateSize(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel10updateSizeERK6QPoint(
    QTipLabel *self,
    const QPoint *pos) {
  self->updateSize(*pos);
}

//  bool QTipLabel::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTipLabel11eventFilterEP7QObjectP6QEvent(
    QTipLabel *self,
    QObject *a0,
    QEvent *a1) {
  return self->eventFilter(a0, a1);
}

//  void QTipLabel::reuseTip(const QString &text, int msecDisplayTime, const
//      QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel8reuseTipERK7QStringiRK6QPoint(
    QTipLabel *self,
    const QString *text,
    int msecDisplayTime,
    const QPoint *pos) {
  self->reuseTip(*text, msecDisplayTime, *pos);
}

//  void QTipLabel::hideTip()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel7hideTipEv(QTipLabel *self) {
  self->hideTip();
}

//  void QTipLabel::hideTipImmediately()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel18hideTipImmediatelyEv(QTipLabel *self) {
  self->hideTipImmediately();
}

//  void QTipLabel::setTipRect(QWidget *w, const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel10setTipRectEP7QWidgetRK5QRect(
    QTipLabel *self,
    QWidget *w,
    const QRect *r) {
  self->setTipRect(w, *r);
}

//  void QTipLabel::restartExpireTimer(int msecDisplayTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel18restartExpireTimerEi(
    QTipLabel *self,
    int msecDisplayTime) {
  self->restartExpireTimer(msecDisplayTime);
}

//  bool QTipLabel::tipChanged(const QPoint &pos, const QString &text,
//      QObject *o)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTipLabel10tipChangedERK6QPointRK7QStringP7QObject(
    QTipLabel *self,
    const QPoint *pos,
    const QString *text,
    QObject *o) {
  return self->tipChanged(*pos, *text, o);
}

//  void QTipLabel::placeTip(const QPoint &pos, QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel8placeTipERK6QPointP7QWidget(
    QTipLabel *self,
    const QPoint *pos,
    QWidget *w) {
  self->placeTip(*pos, w);
}

//  QScreen *QTipLabel::getTipScreen(const QPoint &pos, QWidget *w)
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN9QTipLabel12getTipScreenERK6QPointP7QWidget(
    const QPoint *pos,
    QWidget *w) {
  return QTipLabel::getTipScreen(*pos, w);
}

//  void QTipLabel::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel10timerEventEP11QTimerEvent(
    QTipLabel *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QTipLabel::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel10paintEventEP11QPaintEvent(
    QTipLabel *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QTipLabel::mouseMoveEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel14mouseMoveEventEP11QMouseEvent(
    QTipLabel *self,
    QMouseEvent *e) {
  self->mouseMoveEvent(e);
}

//  void QTipLabel::resizeEvent(QResizeEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel11resizeEventEP12QResizeEvent(
    QTipLabel *self,
    QResizeEvent *e) {
  self->resizeEvent(e);
}

#if QT_CONFIG(style_stylesheet)
//  void QTipLabel::styleSheetParentDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTipLabel25styleSheetParentDestroyedEv(QTipLabel *self) {
  self->styleSheetParentDestroyed();
}
#endif  // QT_CONFIG(style_stylesheet)

#endif  // QT_CONFIG(tooltip)
