//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/scroller_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/scroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on ScrollTicker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnScrollTicker : ScrollTicker {
  using ScrollTicker::timerEvent;
};

//  const QMetaObject *ScrollTicker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12ScrollTicker10metaObjectEv(
    const ScrollTicker *self) {
  return self->metaObject();
}

//  void *ScrollTicker::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12ScrollTicker11qt_metacastEPKc(
    ScrollTicker *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int ScrollTicker::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12ScrollTicker11qt_metacallEN11QMetaObject4CallEiPPv(
    ScrollTicker *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString ScrollTicker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12ScrollTicker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ScrollTicker::tr(s, c, n));
}

//  ScrollTicker::ScrollTicker(Scroller *scroller, QObject *parent)
extern "C" Q_DECL_EXPORT
ScrollTicker *ritual_ZN12ScrollTickerC1EP8ScrollerP7QObject(
    Scroller *scroller,
    QObject *parent) {
  return new ScrollTicker(scroller, parent);
}

//  void ScrollTicker::start(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ScrollTicker5startEi(ScrollTicker *self, int interval) {
  self->start(interval);
}

//  void ScrollTicker::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12ScrollTicker4stopEv(ScrollTicker *self) {
  self->stop();
}

//  void ScrollTicker::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN12ScrollTicker10timerEventEP11QTimerEvent(
    ScrollTicker *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void ScrollTicker::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12ScrollTicker10timerEventEP11QTimerEvent(
    ScrollTicker *self,
    QTimerEvent *event) {
  static_cast<OwnScrollTicker *>(self)->OwnScrollTicker::timerEvent(event);
}
